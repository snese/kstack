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

## Pre-flight Checks

Before starting, verify the environment:

1. **Is this a git repo?** Run `git rev-parse --is-inside-work-tree`. If not → stop and report "Not a git repository."
2. **Is there a remote?** Run `git remote -v`. If no remote → stop and report "No git remote configured."
3. **Detect hosting platform** from remote URL:
   - `github.com` → use GitHub API for PR
   - `gitlab.com` → use GitLab API for MR
   - Other → push only, skip PR creation, report "PR skipped: unsupported hosting platform"

## Workflow

### 1. Verify State
```bash
# Confirm in a git repo
git rev-parse --is-inside-work-tree || { echo "❌ Not a git repository."; exit 1; }

# Confirm on a feature branch
BRANCH=$(git branch --show-current)
DEFAULT=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main")
if [ "$BRANCH" = "$DEFAULT" ]; then
  echo "❌ You're on $DEFAULT. Can't ship. Switch to a feature branch first."
  exit 1
fi

# Confirm no uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
  echo "❌ Uncommitted changes. Commit or stash first."
  exit 1
fi
```

### 2. Sync with default branch
```bash
git fetch origin
git rebase origin/$DEFAULT
# If conflict → stop and report. Don't resolve automatically.
```

### 3. Run Tests (if the repo has them)
Detect and run:
- `package.json` with test script → `npm test` or `bun test`
- `pytest.ini` / `pyproject.toml` / `setup.py` → `pytest`
- `go.mod` → `go test ./...`
- `Cargo.toml` → `cargo test`
- `Makefile` with test target → `make test`
- None found → skip, report "⏭️ no tests detected"

Failure → stop and report.

### 4. Push
```bash
git push origin HEAD
```

### 5. Open PR / MR
- **GitHub**: create PR via API. Title from branch name or first commit. Body from commit log.
- **GitLab**: create MR via API.
- **Other**: skip, report push URL only.

### 6. Report

## Output Format

```markdown
# Ship Report

## Status: ✅ Shipped / ❌ Failed at Step {N}

| Step | Status |
|------|--------|
| Git repo | ✅ / ❌ not a repo |
| Branch check | ✅ `{branch}` / ❌ on default branch |
| Clean state | ✅ / ❌ uncommitted changes |
| Sync | ✅ / ❌ conflict |
| Tests | ✅ / ⏭️ no tests / ❌ failed |
| Push | ✅ |
| PR/MR | ✅ {URL} / ⏭️ unsupported platform |

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
- If the platform is unsupported for PR, a successful push is still a successful ship.
