# Architecture

## Design Philosophy

kstack is a set of Markdown files. That's it.

No runtime. No binary. No framework. Each skill is a `SKILL.md` that tells Kiro CLI how to think in a specific cognitive mode.

This is intentional. The simpler the mechanism, the more portable and maintainable it is.

## How Kiro CLI Discovers Skills

```
~/.kiro/skills/{name}/SKILL.md
```

Kiro CLI scans `~/.kiro/skills/` for directories containing `SKILL.md`. The front matter (`name`, `description`) is used for discovery. The rest of the file is the system prompt for that mode.

## Skill Structure

```
{skill-name}/
├── SKILL.md              # The skill definition
└── evals/
    └── test_cases.yaml   # Eval test cases
```

## Setup Mechanism

`./setup` creates symlinks:

```
~/.kiro/skills/plan-product → ~/.kiro/skills/kstack/plan-product
~/.kiro/skills/plan-eng → ~/.kiro/skills/kstack/plan-eng
...
```

This means:
- `git pull` updates skills immediately (symlinks follow the source)
- No copy/paste drift between repo and installed skills
- Clean uninstall: remove symlinks + repo directory

## Cognitive Mode Design

Each skill defines a distinct cognitive mode:

| Skill | Mode | Key constraint |
|-------|------|----------------|
| plan-product | Divergent thinking | Don't accept the literal request |
| plan-eng | Convergent thinking | Must produce diagrams |
| code-review | Adversarial thinking | No flattery, find problems |
| ship | Execution | No questions, no code changes |
| qa | Verification | Evidence-based, health score |
| retro | Reflection | Data-driven, actionable |

The key insight: these modes are deliberately incompatible. A good product thinker challenges assumptions; a good release engineer doesn't. Blending them produces mediocrity. Separating them produces excellence.

## Why Not a CLI Tool?

gstack (for Claude Code) includes a compiled Playwright binary for browser automation. kstack deliberately excludes this:

1. **Portability** — Markdown works everywhere Kiro CLI works
2. **No build step** — `git clone && ./setup` is the entire install
3. **Composability** — users can add their own browser/QA skills alongside kstack
4. **Maintainability** — updating a skill = editing a Markdown file
