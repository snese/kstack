# Contributing to kstack

## Adding a New Skill

1. Create a directory: `mkdir my-skill`
2. Create `my-skill/SKILL.md` with this structure:

```yaml
---
name: my-skill
description: "One sentence about what this skill does."
---
```

Followed by:
- **Cognitive mode** — what persona should the agent adopt?
- **Trigger** — what phrases activate this skill?
- **Core Principles** — 3-5 rules that define the mode
- **Workflow** — numbered steps the agent follows
- **Output Format** — markdown template for the response

3. Add eval test cases: `my-skill/evals/test_cases.yaml`
4. Add the skill name to the `SKILLS` array in `setup`
5. Test it: run `./setup` then try the trigger in Kiro CLI

## Skill Design Rules

- **One skill = one cognitive mode.** Don't blend planning with review.
- **Be opinionated.** Vague skills produce vague results.
- **Include output format.** The agent needs to know what shape the response should take.
- **No personal config.** Skills must work for any Kiro CLI user.
- **No external dependencies.** Pure Markdown. No binaries, no npm, no API keys.

## Eval Test Cases

Every skill must have evals. Format:

```yaml
- id: descriptive-name
  prompt: "What the user would say"
  expectations:
    - "Observable behavior the agent should exhibit"
    - "Another expected behavior"
```

Expectations should be:
- **Observable** — can be verified from the output
- **Specific** — not "does a good job" but "produced an ASCII diagram"
- **Independent** — each expectation can pass or fail on its own

## Testing

Manual: run each eval prompt through `kiro-cli chat` and check expectations.

Automated: use any LLM-as-judge framework that reads `test_cases.yaml`.
