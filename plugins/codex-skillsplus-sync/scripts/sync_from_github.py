#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import time
import urllib.request
import zipfile
from pathlib import Path


REPO_OWNER = "zhuguang-ZFG"
REPO_NAME = "codex_skillsplus"
REPO_BRANCH = "main"
SYNC_NAMESPACE = ".codex-skillsplus"
CACHE_STATE = Path(SYNC_NAMESPACE) / "sync-state.json"
MIN_SYNC_INTERVAL_SECONDS = 6 * 60 * 60

MANAGED_BLOCK_START = "<!-- codex-skillsplus-sync:start -->"
MANAGED_BLOCK_END = "<!-- codex-skillsplus-sync:end -->"

REQUIRED_PATHS = [
    ("skills/karpathy-guidelines", ".codex/skills/karpathy-guidelines"),
    ("skills/karpathy-guidelines-zh", ".codex/skills/karpathy-guidelines-zh"),
    ("EXAMPLES.md", f"{SYNC_NAMESPACE}/EXAMPLES.md"),
    (".cursor/rules/karpathy-guidelines.mdc", ".cursor/rules/karpathy-guidelines.mdc"),
]


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync codex_skillsplus project guidance from GitHub into the current project."
    )
    parser.add_argument("--project-root", help="Target project root. Defaults to detected workspace root.")
    parser.add_argument("--repo-owner", default=REPO_OWNER)
    parser.add_argument("--repo-name", default=REPO_NAME)
    parser.add_argument("--branch", default=REPO_BRANCH)
    parser.add_argument("--force", action="store_true", help="Ignore sync interval and refresh immediately.")
    parser.add_argument("--silent", action="store_true", help="Suppress non-error output.")
    return parser.parse_args()


def log(message: str, silent: bool) -> None:
    if not silent:
        print(message)


def candidate_project_roots() -> list[Path]:
    candidates: list[Path] = []
    for key in (
        "CODEX_PROJECT_ROOT",
        "CODEX_WORKSPACE_ROOT",
        "PROJECT_ROOT",
        "INIT_CWD",
        "PWD",
    ):
        value = os.environ.get(key)
        if value:
            candidates.append(Path(value).expanduser())
    candidates.append(Path.cwd())
    return candidates


def looks_like_plugin_runtime(path: Path) -> bool:
    lowered = str(path).lower().replace("/", "\\")
    return "\\.codex\\plugins\\" in lowered or "\\plugins\\codex-skillsplus-sync" in lowered


def detect_project_root(explicit: str | None) -> Path | None:
    if explicit:
        return Path(explicit).expanduser().resolve()

    for candidate in candidate_project_roots():
        try:
            resolved = candidate.resolve()
        except FileNotFoundError:
            continue
        if looks_like_plugin_runtime(resolved):
            continue
        return resolved
    return None


def state_path(project_root: Path) -> Path:
    return project_root / CACHE_STATE


def should_skip_sync(project_root: Path, force: bool) -> bool:
    if force:
        return False
    path = state_path(project_root)
    if not path.exists():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    synced_at = data.get("synced_at")
    if not isinstance(synced_at, (int, float)):
        return False
    return (time.time() - synced_at) < MIN_SYNC_INTERVAL_SECONDS


def download_repo_zip(owner: str, repo: str, branch: str, silent: bool) -> Path:
    url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
    log(f"[codex-skillsplus-sync] Downloading {url}", silent)
    fd, tmp_path = tempfile.mkstemp(suffix=".zip")
    os.close(fd)
    target = Path(tmp_path)
    with urllib.request.urlopen(url) as response, target.open("wb") as out:
        shutil.copyfileobj(response, out)
    return target


def extract_repo(zip_path: Path) -> Path:
    temp_dir = Path(tempfile.mkdtemp(prefix="codex-skillsplus-sync-"))
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(temp_dir)
    extracted = list(temp_dir.iterdir())
    if len(extracted) != 1 or not extracted[0].is_dir():
        raise RuntimeError("Unexpected GitHub archive layout.")
    return extracted[0]


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def sync_required_paths(repo_root: Path, project_root: Path) -> None:
    for src_rel, dst_rel in REQUIRED_PATHS:
        src = repo_root / src_rel
        dst = project_root / dst_rel
        if src.is_dir():
            copy_tree(src, dst)
        else:
            copy_file(src, dst)


def update_claude_md(repo_root: Path, project_root: Path) -> None:
    source = (repo_root / "CLAUDE.md").read_text(encoding="utf-8")
    target = project_root / "CLAUDE.md"
    managed = (
        f"{MANAGED_BLOCK_START}\n"
        "The block below is managed by codex-skillsplus-sync.\n\n"
        f"{source.strip()}\n"
        f"{MANAGED_BLOCK_END}\n"
    )

    if not target.exists():
        target.write_text(source, encoding="utf-8")
        return

    existing = target.read_text(encoding="utf-8", errors="ignore")
    if MANAGED_BLOCK_START in existing and MANAGED_BLOCK_END in existing:
        before, remainder = existing.split(MANAGED_BLOCK_START, 1)
        _, after = remainder.split(MANAGED_BLOCK_END, 1)
        merged = before.rstrip() + "\n\n" + managed + after.lstrip()
    else:
        merged = existing.rstrip() + "\n\n" + managed
    target.write_text(merged, encoding="utf-8")


def write_state(project_root: Path, owner: str, repo: str, branch: str) -> None:
    path = state_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "repo_owner": owner,
        "repo_name": repo,
        "branch": branch,
        "synced_at": time.time(),
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    project_root = detect_project_root(args.project_root)
    if project_root is None:
        eprint("[codex-skillsplus-sync] Unable to detect project root. Skipping sync.")
        return 0

    if should_skip_sync(project_root, args.force):
        log("[codex-skillsplus-sync] Recent sync found. Skipping refresh.", args.silent)
        return 0

    zip_path: Path | None = None
    extracted_root: Path | None = None
    try:
        zip_path = download_repo_zip(args.repo_owner, args.repo_name, args.branch, args.silent)
        extracted_root = extract_repo(zip_path)
        sync_required_paths(extracted_root, project_root)
        update_claude_md(extracted_root, project_root)
        write_state(project_root, args.repo_owner, args.repo_name, args.branch)
        log(f"[codex-skillsplus-sync] Synced guidance into {project_root}", args.silent)
        return 0
    except Exception as exc:
        eprint(f"[codex-skillsplus-sync] Sync failed: {exc}")
        return 1
    finally:
        if zip_path and zip_path.exists():
            zip_path.unlink(missing_ok=True)
        if extracted_root and extracted_root.parent.exists():
            shutil.rmtree(extracted_root.parent, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
