# Changelog

## v0.1.0 (2026-03-17)

Initial release. Inspired by [gstack](https://github.com/garrytan/gstack) for Claude Code, rebuilt for Kiro CLI.

### Skills
- **plan-product** — Product thinking mode: rethink the problem, find the 10-star version
- **plan-eng** — Engineering planning: architecture diagrams, failure modes, test matrix
- **code-review** — Paranoid code review: find bugs that pass CI but explode in prod
- **ship** — One-command shipping: sync → test → push → PR
- **qa** — QA testing: diff-aware, health score, severity classification
- **retro** — Engineering retrospective: data-driven, actionable

### Infrastructure
- `setup` script with install / remove / verify
- GitHub Actions: weekly upstream gstack tracking
- Eval test cases for all 6 skills
- MIT license

### Upstream
- Tracking gstack at `3e3843c`
