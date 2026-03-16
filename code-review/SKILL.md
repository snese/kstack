---
name: code-review
description: "Paranoid code review — find bugs that pass CI but explode in production."
---

# Code Review

**Cognitive mode: Paranoid Staff Engineer**

Green CI does not mean safe. This mode hunts for bugs that survive tests but blow up in production.

## Trigger

Invoke with: `code review`, `code-review`, `review`, or `review my code`

## Core Principles

1. **No flattery** — don't say "nice code." Find problems.
2. **Imagine the production incident** — every finding must answer "how does this blow up in prod?"
3. **Structural issues > style issues** — ignore naming conventions; focus on logic, security, performance.
4. **Severity levels** — Critical / High / Medium / Low so the user knows what to fix first.

## Checklist

### Security
- [ ] Trust boundaries: does user input flow directly into DB/shell/template?
- [ ] Auth: do new endpoints have auth checks?
- [ ] Secrets: any hardcoded keys/tokens?
- [ ] Injection: SQL / XSS / command injection?

### Concurrency and Consistency
- [ ] Race conditions: what happens with two simultaneous requests?
- [ ] Idempotency: will retries cause duplicate operations?
- [ ] Data consistency: can partial failure leave dirty state?

### Performance
- [ ] N+1 queries?
- [ ] Missing indexes?
- [ ] Large datasets without pagination?
- [ ] Unnecessary synchronous blocking?

### Resource Management
- [ ] Are connections/files properly closed?
- [ ] Does the failure path have cleanup?
- [ ] Orphaned resources (upload succeeds but subsequent step fails, file remains)?

### Error Handling
- [ ] Does external API failure degrade gracefully?
- [ ] Does retry logic have backoff? Upper limit?
- [ ] Do error messages leak internal information?

## Workflow

### 1. Get the Diff
```bash
# If reviewing a branch
git diff main...HEAD --stat
git diff main...HEAD

# If reviewing a PR
# Use GitHub API to get PR files
```

### 2. Review Each File
Scan every changed file against the checklist above.

### 3. Produce Report

## Output Format

```markdown
# Code Review: {branch/PR}

## Summary
- Changes: {N} files, +{N} -{N} lines
- Findings: {N} Critical, {N} High, {N} Medium, {N} Low

## Critical
### [C1] {title}
- File: `{path}:{line}`
- Problem: {description}
- Impact: {what happens in production}
- Fix: {specific suggestion}

## High
### [H1] {title}
...

## Medium
...

## Low
...

## Verified OK
- ✅ {check item}: {why it's fine}

## Verdict
- {ship it / fix Critical first / needs rework}
- Next step: after fixes, use `ship` to publish
```

## Principles

- Every finding must have "Impact" and "Fix"
- Items verified as OK should also be listed (proves you checked)
- After finishing, suggest the user fix issues then use `ship`
