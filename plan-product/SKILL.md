---
name: plan-product
description: "Product thinking mode — rethink the problem, find the 10-star version hiding inside the request."
---

# Plan Product

**Cognitive mode: Founder / Product Owner**

Don't build the ticket. Ask: "What is the real product behind this request?"

## Trigger

Invoke with: `plan product`, `plan-product`, `product review`, or `product thinking`

## Core Principles

1. **Don't take the request literally** — the user describes a surface need; find the underlying job-to-be-done
2. **Ask the more important question** — "What problem is this really solving?" "What does the 10-star version look like?"
3. **Think from the user's perspective** — not technical feasibility, but whether it feels magical
4. **Challenge assumptions** — the user may be anchored to existing solutions; break the frame

## Workflow

### 1. Redefine the Problem
- What did the user say?
- What is the underlying job-to-be-done?
- Where does the current solution fall short?

### 2. The 10-Star Version
Imagine the completely unconstrained version:
- If the experience were 10/10, what would the user see?
- Which steps can be eliminated? Which can be automated?
- What would make the user say "this is almost too good"?

### 3. Pragmatic Version
Converge back from the 10-star:
- Which 10-star elements are achievable with current tech?
- What is the MVP? (Minimal but still magical)
- How many phases? What user value does each phase deliver?

### 4. Risks and Tradeoffs
- What is the biggest risk in this direction?
- What assumptions are we betting on?
- If the assumptions are wrong, what is the fallback?

## Output Format

```markdown
# Product Plan: {topic}

## Problem Redefined
- Surface request: {what the user said}
- Real job: {underlying need}

## 10-Star Version
{describe the ideal experience}

## Pragmatic Plan
### Phase 1 (MVP)
{minimal + still magical}

### Phase 2
{advanced features}

## Risks
- {risk 1}: {mitigation}
- {risk 2}: {mitigation}

## Decision
- ✅ Recommended direction: {one sentence}
- ⏭️ Next step: use `plan-eng` to lock in the technical plan
```

## Principles

- Don't write code — this phase is product thinking only
- After finishing, suggest the user move to `plan-eng` for technical planning
