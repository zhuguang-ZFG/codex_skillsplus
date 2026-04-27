# Karpathy Guidelines Examples

Use this file only when the current task needs concrete examples of how to apply the skill.

## Table of Contents

- Think before coding
- Keep it simple
- Make surgical changes
- Drive toward verifiable success

## Think Before Coding

### Example: Hidden assumptions

User request:

```text
Add a feature to export user data.
```

Bad response pattern:

- Assume all users should be exported.
- Assume the format should be JSON or CSV.
- Assume the destination should be a local file.
- Assume which fields are safe to export.

Better response pattern:

```text
Before implementing, clarify:
1. Export all users or a filtered subset?
2. Browser download, API response, or background job?
3. Which fields are allowed?
4. Roughly how much data is expected?
```

### Example: Multiple interpretations

User request:

```text
Make the search faster.
```

Better response pattern:

```text
"Faster" could mean lower latency, higher throughput, or better perceived speed.
The simplest next step depends on which one matters most.
```

## Keep It Simple

### Example: Over-abstraction

User request:

```text
Add a function to calculate discount.
```

Bad response pattern:

- Create strategy classes.
- Add configuration objects.
- Add multiple discount types before they are needed.

Better response pattern:

```python
def calculate_discount(amount: float, percent: float) -> float:
    return amount * (percent / 100)
```

Rule of thumb:

- Add complexity only after a real new requirement forces it.

### Example: Speculative features

User request:

```text
Save user preferences to database.
```

Bad response pattern:

- Add caching.
- Add notifications.
- Add merge strategies.
- Add configuration flags.

Better response pattern:

- Save the provided preferences to the database in the most direct way.

## Make Surgical Changes

### Example: Drive-by refactor

User request:

```text
Fix the bug where empty emails crash the validator.
```

Bad response pattern:

- Rewrite adjacent validation logic.
- Add new username rules.
- Reformat comments and whitespace.

Better response pattern:

- Change only the email handling needed to avoid the crash.
- Preserve the existing style and unrelated behavior.

### Example: Style drift

User request:

```text
Add logging to the upload function.
```

Bad response pattern:

- Reformat quotes.
- Add type hints.
- Rewrite return logic.
- Change error handling style globally.

Better response pattern:

- Add the needed logger setup.
- Insert log lines around the existing success and failure paths.
- Keep the surrounding coding style intact.

## Drive Toward Verifiable Success

### Example: Vague task

User request:

```text
Fix the authentication system.
```

Bad response pattern:

- Review code.
- Make improvements.
- Test changes.

Better response pattern:

```text
Define the exact failure first.
If the issue is "password change should invalidate old sessions," then:
1. Reproduce with a failing test.
2. Implement session invalidation.
3. Verify the new test passes.
4. Verify existing auth tests still pass.
```

### Example: Multi-step change

User request:

```text
Add rate limiting to the API.
```

Better response pattern:

```text
1. Add a basic limit for one endpoint -> verify: requests over the limit return 429
2. Apply through middleware -> verify: multiple endpoints are covered
3. Add shared storage if needed -> verify: counters persist across instances
```

## Summary Heuristics

- If you are guessing, stop and surface the guess.
- If you are abstracting, ask whether the requirement exists today.
- If you are editing nearby code, ask whether the request truly needs it.
- If you cannot prove success, define a better check before continuing.
