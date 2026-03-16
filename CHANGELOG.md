# Changelog

## Unreleased

### Improvements
- **setup**: Idempotent — safe to re-run, detects already-installed symlinks
- **setup**: Added `help` command and invalid argument handling
- **setup**: `remove` reports count of removed skills
- **README**: Added Requirements section (macOS/Linux/WSL, Bash 4+)
- **README**: Added Verify installation, Upgrading, Uninstalling, Troubleshooting sections
- **README**: Links to CONTRIBUTING.md and CHANGELOG.md
- **CONTRIBUTING**: Added custom skills guide (`custom/` directory)
- **CONTRIBUTING**: Added adversarial eval guidelines and CI section

### New Features
- **Upstream tracking**: Auto-categorizes changes as prompt/logic vs format-only
- **CI**: Setup integration test (install → verify → remove → re-install cycle)
- **Custom skills**: `custom/` directory gitignored for personal skills

### Evals
- **plan-product**: Added adversarial cases (vague input, overly-specific input)
- **plan-eng**: Added adversarial cases (no context, too-broad scope)
- **code-review**: Added adversarial cases (no code provided, trivially clean code)
- **ship**: Added adversarial cases (not a git repo, dirty working tree override attempt)
- **qa**: Added adversarial cases (no changes, not a git repo)
- **retro**: Added adversarial cases (empty repo, custom time period)

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
- GitHub Actions: CI (lint + eval validation + syntax) and weekly upstream gstack tracking
- Eval test cases for all 6 skills
- Issue templates (bug report, new skill proposal)
- MIT license

### Upstream
- Tracking gstack at `3e3843c`
