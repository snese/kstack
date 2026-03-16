---
name: ship
description: "One-command shipping — sync main, run tests, push, open PR. No chat, pure execution."
---

# Ship

**Cognitive mode: Release Engineer**

The branch is ready. Stop talking. Land the plane.

## Trigger

Invoke with: `ship`, `ship it`, or `ship this`

## Core Principles

1. **Don't ask questions** — the user said ship, so ship. Execute immediately.
2. **Don't change code** — this phase doesn't fix bugs or add features. Release hygiene only.
3. **Stop on failure** — if any step fails, stop and report. Don't improvise fixes.
4. **Speed** — minimum tool calls, fastest completion.

## Workflow

### 1. Verify State
```bash
# Confirm on a feature branch
BRANCH=$(git branch --show-current)
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "❌ You're on main. Can't ship. Switch to a feature branch first."
  exit 1
fi

# Confirm no uncommitted changes
git status --porcelain
```

### 2. Sync Main
```bash
git fetch origin
git rebase origin/main
# If conflict → stop and report. Don't resolve automatically.
```

### 3. Run Tests (if the repo has them)
```bash
# Detect test framework and run
# npm test / bun test / pytest / go test / cargo test / etc.
# Failure → stop and report
```

### 4. Push
```bash
git push origin HEAD
```

### 5. Open PR
Create a PR via GitHub API:
- Title: concise summary of the changes
- Body: auto-generated from commit messages
- Labels: detect from context if possible
- Base: `main`

### 6. Report

## Output Format

```markdown
# Ship Report

## Status: ✅ Shipped / ❌ Failed at Step {N}

| Step | Status |
|------|--------|
| Branch check | ✅ `{branch}` |
| Sync main | ✅ / ❌ conflict |
| Tests | ✅ / ⏭️ no tests / ❌ failed |
| Push | ✅ |
| PR | ✅ {PR URL} |

## Commits ({N})
- {commit 1}
- {commit 2}

## Changes
- {N} files, +{N} -{N} lines
- Main change: {one sentence}
```

## Principles

- The entire flow should take no more than 10 tool calls
- Don't add changelog/version bump unless the repo has that convention
- PR opened = done. Don't wait for review.
