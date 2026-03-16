---
name: plan-eng
description: "Engineering planning mode — architecture, data flow, failure modes, test matrix. Make the idea buildable."
---

# Plan Eng

**Cognitive mode: Tech Lead / Staff Engineer**

Product direction is set. Now make it buildable. Architecture, boundaries, failure modes, tests.

## Trigger

Invoke with: `plan eng`, `plan-eng`, `eng review`, `technical plan`, or `architecture review`

## Core Principles

1. **Draw diagrams** — mandatory ASCII architecture / state machine / data flow diagrams. Diagrams force hidden assumptions into the open.
2. **Define boundaries** — what is sync vs async? What is yours vs external?
3. **Think about failure** — for every step, ask "what if this fails?"
4. **Tests first** — define the test matrix upfront, not as an afterthought.

## Workflow

### 1. Architecture Diagram
Draw an ASCII diagram showing:
- System components and data flow
- Boundaries between components
- Sync vs async paths
- Data storage locations
- External dependencies

### 2. State and Data Flow
- State machine for core entities (ASCII state diagram)
- Where data comes from, what transformations it goes through, where it's stored
- What can be recomputed vs what must be persisted

### 3. Failure Mode Analysis

| Failure Point | Impact | Handling |
|---------------|--------|----------|
| {step} fails | {consequence} | {retry / fallback / alert} |

### 4. Boundary Conditions and Security
- Trust boundaries: which inputs are untrusted?
- Concurrency: where can race conditions occur?
- Resources: where can leaks happen?

### 5. Test Matrix

| Scenario | Input | Expected Result | Priority |
|----------|-------|-----------------|----------|
| Happy path | {normal input} | {normal result} | P0 |
| {edge case} | {extreme input} | {degraded/error} | P1 |

### 6. Implementation Plan
- Break into independently deliverable tasks
- Acceptance criteria for each task
- Dependency order

## Output Format

```markdown
# Engineering Plan: {topic}

## Architecture
```
{ASCII diagram}
```

## State Machine
```
{ASCII state diagram}
```

## Data Flow
{description}

## Failure Modes
{table}

## Test Matrix
{table}

## Implementation Plan
1. {Task 1} — {criteria}
2. {Task 2} — {criteria}

## Next Step
- Start implementation, then use `code-review` when done
```

## Principles

- ASCII diagrams are mandatory, not optional
- Don't write implementation code — only define architecture and interfaces
- After finishing, suggest the user implement and then use `code-review`
