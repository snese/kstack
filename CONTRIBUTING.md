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

## Custom Skills (Personal Use)

Want to add your own skills without them being overwritten by `git pull`?

Put them in the `custom/` directory — it's gitignored:

```
kstack/
├── custom/              ← your personal skills (gitignored)
│   └── my-custom-skill/
│       └── SKILL.md
├── plan-product/        ← kstack skills (tracked by git)
...
```

Then symlink manually:
```bash
ln -sf ~/.kiro/skills/kstack/custom/my-custom-skill ~/.kiro/skills/my-custom-skill
```

## Skill Design Rules

- **One skill = one cognitive mode.** Don't blend planning with review.
- **Be opinionated.** Vague skills produce vague results.
- **Include output format.** The agent needs to know what shape the response should take.
- **No personal config.** Skills must work for any Kiro CLI user.
- **No external dependencies.** Pure Markdown. No binaries, no npm, no API keys.
- **Defensive pre-flight.** Skills that depend on git should detect non-git environments gracefully.

## Eval Test Cases

Every skill must have evals. Format:

```yaml
- id: descriptive-name
  prompt: "What the user would say"
  expectations:
    - "Observable behavior the agent should exhibit"
    - "Another expected behavior"
```

Include adversarial test cases:
- Vague or empty input
- Wrong environment (e.g. non-git repo for ship)
- Trivially correct input (e.g. clean code for code-review)
- User trying to override safety checks

Expectations should be:
- **Observable** — can be verified from the output
- **Specific** — not "does a good job" but "produced an ASCII diagram"
- **Independent** — each expectation can pass or fail on its own

## Testing

Manual: run each eval prompt through `kiro-cli chat` and check expectations.

Automated: use any LLM-as-judge framework that reads `test_cases.yaml`.

## CI

Every push runs:
1. SKILL.md front matter validation (name + description required, name must match directory)
2. Eval YAML structure validation (id + prompt + expectations required)
3. Setup script syntax check
4. Setup install/verify/remove integration test
