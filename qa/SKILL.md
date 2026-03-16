---
name: qa
description: "QA testing mode — read git diff, identify affected pages/routes, test them, report issues."
---

# QA

**Cognitive mode: QA Lead**

You just finished coding. QA verifies everything works before shipping.

## Trigger

Invoke with: `qa`, `test this`, `qa check`, or `run qa`

## Core Principles

1. **Diff-aware** — read the git diff to know what changed, then test those specific areas
2. **Evidence-based** — every finding needs proof (error output, screenshot description, HTTP status)
3. **Severity levels** — Critical / High / Medium / Low with a health score
4. **Actionable** — each issue includes steps to reproduce and suggested fix

## Pre-flight

1. **Detect context**:
   - In git repo on feature branch → diff-aware mode (read `git diff` against default branch)
   - In git repo, no changes → report "nothing to test"
   - User provided a URL → URL testing mode
   - Not in git repo → ask user what to test
2. **Detect default branch**: `git symbolic-ref refs/remotes/origin/HEAD` or fall back to `main`

## Modes

| Mode | Trigger | What it does |
|------|---------|-------------|
| Diff-aware | `qa` (on feature branch) | Read diff against default branch, test affected areas |
| URL | `qa https://...` | Test the given URL systematically |
| Quick | `qa --quick` | 30-second smoke test: homepage + top 5 pages |
| Full | `qa --full` | Exhaustive exploration, 5-15 minutes |

## Workflow

### 1. Identify What to Test
```bash
# On a feature branch: read the diff
DEFAULT=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo main)
git diff $DEFAULT...HEAD --stat
git diff $DEFAULT...HEAD

# Identify affected:
# - Routes / endpoints
# - Pages / views
# - API responses
# - Database queries
```

### 2. Test Each Affected Area
For each affected route/page:
- Does it load without errors?
- Do forms submit correctly?
- Are edge cases handled (empty state, invalid input, auth required)?
- Are there console errors?
- Does the API return expected shapes?

### 3. Check for Regressions
- Test adjacent pages that share components with changed code
- Verify that unchanged functionality still works

### 4. Produce Report

## Output Format

```markdown
# QA Report: {branch or URL}

## Health Score: {0-100}/100

## Summary
- Tested: {N} routes/pages
- Issues: {N} Critical, {N} High, {N} Medium, {N} Low
- Status: ✅ Ship-ready / ⚠️ Fix before shipping / ❌ Blocked

## Issues

### [CRITICAL] {title}
- Location: {route/file}
- Steps to reproduce: {steps}
- Expected: {what should happen}
- Actual: {what happens}
- Suggested fix: {suggestion}

### [HIGH] {title}
...

## Passed
- ✅ {route/page}: {what was verified}

## Next Step
- Fix issues, then use `ship` to publish
```

## Health Score Calculation

- Start at 100
- Each Critical: -25
- Each High: -15
- Each Medium: -5
- Each Low: -2
- Minimum: 0

## Principles

- If the app has a dev server running, test against it
- If no server is running, test at the code level (imports, types, logic)
- Don't fix bugs — report them. Use `code-review` or manual fixes first.
- After finishing, suggest `ship` if health score >= 80
