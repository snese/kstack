# kstack

**kstack turns Kiro CLI from one generic assistant into a team of specialists you can summon on demand.**

Six opinionated workflow skills for [Kiro CLI](https://kiro.dev). Product thinking, engineering planning, paranoid code review, one-command shipping, QA testing, and engineering retrospectives — all as natural language triggers.

Inspired by [gstack](https://github.com/garrytan/gstack) for Claude Code. Rebuilt from scratch for Kiro CLI's skill system.

## Without kstack

- The agent takes your request literally — it never asks if you're building the right thing
- "Review my code" gives inconsistent depth every time
- "Ship this" turns into a long back-and-forth about what to do
- You still do QA by hand
- Retros are vibes, not data

## With kstack

| Skill | Mode | What it does |
|-------|------|--------------|
| `plan-product` | Founder / Product Owner | Rethink the problem. Find the 10-star product hiding inside the request. |
| `plan-eng` | Tech Lead / Staff Engineer | Lock in architecture, data flow, diagrams, failure modes, and test matrix. |
| `code-review` | Paranoid Staff Engineer | Find bugs that pass CI but explode in production. |
| `ship` | Release Engineer | Sync main, run tests, push, open PR. No chat, pure execution. |
| `qa` | QA Lead | Read git diff, identify affected areas, test them, produce health score. |
| `retro` | Engineering Manager | Analyze commits, reflect on what happened, identify improvements. |

## Demo: one feature, six modes

```
You:   I want to add seller photo upload to the listing app.

You:   plan product

Kiro:  "Photo upload" is not the feature. The real job is helping sellers
       create listings that actually sell. Here's the 10-star version:
       auto-identify the product, pull specs from the web, draft the
       title and description, suggest the best hero image...

You:   plan eng

Kiro:  [ASCII architecture diagram, state machine for upload → classify
       → enrich → draft pipeline, failure modes, test matrix]

You:   (implement the plan)

You:   code review

Kiro:  [C1] Race condition: two tabs can overwrite cover-photo selection.
       [H1] Trust boundary: web data into draft generation = injection vector.
       [H2] Missing: orphan cleanup for failed uploads.

You:   (fix the issues)

You:   ship

Kiro:  [Syncs main, runs tests, pushes branch, opens PR — done]

You:   qa

Kiro:  Analyzing branch diff... 8 files changed, 3 routes affected.
       Health Score: 95/100. All routes working. Ship-ready.

You:   retro

Kiro:  This week: 47 commits, +3.2k LOC, 38% tests.
       What went well: shipped complete feature in one focused push.
       Improve: test ratio below 40% — add integration tests.
```

## Install

**Requirements:** [Kiro CLI](https://kiro.dev) installed and working.

### One-line install

```bash
git clone https://github.com/snese/kstack.git ~/.kiro/skills/kstack && cd ~/.kiro/skills/kstack && chmod +x setup && ./setup
```

This clones the repo and creates symlinks from each skill directory into `~/.kiro/skills/` so Kiro can discover them.

### What gets installed

```
~/.kiro/skills/
├── kstack/              ← the cloned repo
│   ├── plan-product/
│   │   └── SKILL.md
│   ├── plan-eng/
│   │   └── SKILL.md
│   ├── code-review/
│   │   └── SKILL.md
│   ├── ship/
│   │   └── SKILL.md
│   ├── qa/
│   │   └── SKILL.md
│   ├── retro/
│   │   └── SKILL.md
│   └── setup
├── plan-product → kstack/plan-product   (symlink)
├── plan-eng → kstack/plan-eng           (symlink)
├── code-review → kstack/code-review     (symlink)
├── ship → kstack/ship                   (symlink)
├── qa → kstack/qa                       (symlink)
└── retro → kstack/retro                 (symlink)
```

Everything lives inside `~/.kiro/skills/`. Nothing touches your PATH or runs in the background. Pure Markdown — no binaries, no dependencies.

### Add to your repo (optional)

So teammates get the skills when they clone:

```bash
cp -Rf ~/.kiro/skills/kstack .kiro/skills/kstack
rm -rf .kiro/skills/kstack/.git
```

Teammates run `cd .kiro/skills/kstack && ./setup` once after cloning.

## The Lifecycle

```
  ① Describe what you want to build
         │
         ▼
┌─────────────────────┐
│   plan-product      │  ← Product brain: what is the REAL product?
│   "10-star version" │     Don't build the ticket. Rethink the problem.
└────────┬────────────┘
         │ Product direction locked ✓
         ▼
┌─────────────────────┐
│   plan-eng          │  ← Tech lead brain: how to build it right?
│   ASCII diagrams    │     Architecture, state machines, failure modes,
│   + test matrix     │     test matrix. Make the idea buildable.
└────────┬────────────┘
         │ Technical plan locked ✓
         ▼
┌─────────────────────┐
│   Implement         │  ← Normal coding
└────────┬────────────┘
         │ Implementation done
         ▼
┌─────────────────────┐
│   code-review       │  ← Paranoid brain: what blows up in prod?
│   Security, races,  │     N+1, trust boundaries, resource leaks.
│   N+1, leaks        │     No flattery. Find problems.
└────────┬────────────┘
         │ Issues fixed
         ▼
┌─────────────────────┐
│   ship              │  ← Release machine: sync → test → push → PR
│   ≤10 tool calls    │     No chat. Pure execution.
└────────┬────────────┘
         │ PR opened
         ▼
┌─────────────────────┐
│   qa                │  ← QA brain: read diff → test affected areas
│   Health score      │     Evidence-based. Health score 0-100.
└────────┬────────────┘
         │ Verified ✓
         ▼
┌─────────────────────┐
│   retro             │  ← EM brain: what actually happened?
│   Data-driven       │     Commits, LOC, wins, improvements, actions.
└─────────────────────┘
```

## Skill Details

### `plan-product`

Founder mode. Don't take the request literally. Find the job-to-be-done. Propose the 10-star version, then converge to a pragmatic MVP with risks identified.

### `plan-eng`

Tech lead mode. ASCII diagrams are mandatory. Architecture, state machines, data flow, failure mode analysis, test matrix, implementation plan with acceptance criteria.

### `code-review`

Paranoid staff engineer mode. Checklist covers security (injection, auth, secrets), concurrency (races, idempotency), performance (N+1, missing indexes), resource management (leaks, orphans), and error handling. Every finding has severity + impact + fix.

### `ship`

Release engineer mode. Verify branch state → sync main → run tests → push → open PR. Stops on failure. No questions asked. No code changes.

### `qa`

QA lead mode. Four modes: diff-aware (automatic on feature branches), URL testing, quick smoke test, full exhaustive. Produces health score 0-100 with severity-classified issues.

### `retro`

Engineering manager mode. Analyzes git history for commits, LOC, test ratio, hotspot files, coding patterns. Produces wins, improvements with root causes, and actionable items.

## Evals

Each skill includes eval test cases in `{skill}/evals/test_cases.yaml`. Format:

```yaml
- id: test-name
  prompt: "what the user says"
  expectations:
    - "what the agent should do"
    - "another expected behavior"
```

Run evals with any LLM-as-judge framework, or manually verify by running each prompt through Kiro CLI.

## Upgrading

```bash
cd ~/.kiro/skills/kstack && git pull
```

Symlinks mean the skills update immediately — no re-setup needed.

## Uninstalling

```bash
for s in plan-product plan-eng code-review ship qa retro; do
  rm -f ~/.kiro/skills/$s
done
rm -rf ~/.kiro/skills/kstack
```

## How It Works

kstack is not magic. It's six carefully written Markdown files that tell Kiro CLI which cognitive mode to use for each phase of software development.

The key insight from [gstack](https://github.com/garrytan/gstack): **planning is not review. Review is not shipping. Founder taste is not engineering rigor.** If you blur all of that together, you get a mediocre blend of all four.

kstack gives you explicit gears. Tell the agent what kind of brain you want right now.

## Differences from gstack

| | gstack (Claude Code) | kstack (Kiro CLI) |
|---|---|---|
| Runtime | Claude Code + Bun + Playwright binary | Kiro CLI only. Pure Markdown, zero dependencies. |
| Browser | Compiled Playwright binary (~58MB) | Not included — use Kiro's built-in tools or add your own browser skill |
| Install | `./setup` compiles binary + creates symlinks | `./setup` creates symlinks only |
| Skills | 9 (includes browse, qa-only, setup-cookies) | 6 core cognitive modes |
| Parallel | Conductor for 10 sessions | Use Kiro CLI's subagent system |
| Greptile | Built-in triage | Not included — add as separate skill if needed |

## Contributing

PRs welcome. Each skill is a single `SKILL.md` file — easy to read, easy to modify.

Guidelines:
- One skill = one cognitive mode. Don't blend.
- Include eval test cases for any new skill.
- Keep skills platform-agnostic (no hardcoded paths, no personal config).

## License

MIT

## Credits

Inspired by [gstack](https://github.com/garrytan/gstack) by [Garry Tan](https://x.com/garrytan). The cognitive mode switching concept and the plan → review → ship → QA lifecycle are directly adapted from gstack's design philosophy.
