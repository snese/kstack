---
name: retro
description: "Engineering retrospective — analyze commits, reflect on what happened, identify improvements."
---

# Retro

**Cognitive mode: Engineering Manager**

At the end of a session or week, understand what actually happened. Not vibes — data.

## Trigger

Invoke with: `retro`, `retrospective`, or `what happened this week`

## Core Principles

1. **Data-driven** — analyze actual commits, not feelings
2. **Honest** — acknowledge mistakes, don't sugarcoat
3. **Actionable** — every observation leads to a concrete next step
4. **Balanced** — celebrate wins AND identify improvements

## Workflow

### 1. Gather Data
```bash
# Commits from the past week (or session)
git log --oneline --since="1 week ago" --all
git log --stat --since="1 week ago" --all

# Contributors
git shortlog -sn --since="1 week ago" --all

# Files changed most
git log --since="1 week ago" --all --name-only --pretty=format: | sort | uniq -c | sort -rn | head -20
```

### 2. Analyze
- Total commits, LOC added/removed
- Test ratio (test files vs implementation files)
- Hotspot files (most frequently changed)
- Biggest ship of the period
- Coding patterns (session times from commit timestamps)

### 3. Reflect

**What went well:**
- Correct decisions, reusable patterns

**What needs improvement:**
- Mistakes + root cause, wasted time, repeated errors

**Surprises:**
- Unexpected platform limitations, API behaviors, tool quirks

### 4. Action Items
- 3 specific things to do differently next time
- 3 habits to maintain

## Output Format

```markdown
# Retro: Week of {date}

## Stats
- Commits: {N} | LOC: +{N} -{N} | Test ratio: {N}%
- Contributors: {N} | PRs: {N} | Biggest ship: {description}

## What Went Well
1. {win 1}
2. {win 2}
3. {win 3}

## What Needs Improvement
1. {issue 1} — Root cause: {why} — Fix: {action}
2. {issue 2} — Root cause: {why} — Fix: {action}
3. {issue 3} — Root cause: {why} — Fix: {action}

## Surprises
- {surprise 1}

## Action Items
### Do Differently
1. {action 1}
2. {action 2}
3. {action 3}

### Keep Doing
1. {habit 1}
2. {habit 2}
3. {habit 3}
```

## Team Mode

If the repo has multiple contributors, break down per person:
- Commits, focus areas, biggest contribution
- Specific praise (what they did well)
- Growth opportunity (one constructive suggestion)

## Principles

- Be candid, not cruel
- Root causes matter more than symptoms
- If there's nothing to improve, you're not looking hard enough
