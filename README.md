# maintainer-copilot

A small open-source CLI that helps maintainers triage issues faster.

`maintainer-copilot` reads a Markdown issue report and returns:
- a concise summary
- initial label candidates
- missing information to request before review

The goal is simple: reduce repetitive first-pass maintainer work so humans can spend more time on actual decisions.

## Why this project matters

Open-source maintenance includes a large amount of invisible work: reading incomplete reports, deciding initial labels, and asking for missing details before real debugging can begin.

This project focuses on one narrow but common maintainer task first:
**issue triage**.

By starting with a local-first CLI, the repository aims to build a transparent foundation for future maintainer workflows such as GitHub automation, review assistance, and release preparation.

## Current capabilities

Today the tool can:
- summarize an issue report
- suggest likely labels such as `bug`, `question`, `enhancement`, and `needs-info`
- identify missing information such as version, environment, reproduction steps, expected behavior, and actual behavior
- recognize common issue-template section headings as well as free-form issue text

Current implementation status:
- local CLI works
- issue-triage heuristics are tested
- question vs enhancement disambiguation is implemented
- issue template-aware parsing is implemented

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/pt533/maintainer-copilot.git
cd maintainer-copilot
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the project

```bash
pip install -e .
```

### 4. Run the CLI

```bash
mcopilot examples/sample_issue.md
```

## Example input

Example issue report:

```text
Title: Crash when starting app on Windows

Version: 0.1.0
Environment: Windows 11

Steps to reproduce:
1. Launch the app
2. Wait for startup

Expected behavior:
The app should start normally.

Actual behavior:
The app crashes immediately with a traceback.
```

## Example output

```json
{
  "summary": "Title: Crash when starting app on Windows Version: 0.1.0 Environment: Windows 11 Steps to reproduce: 1. Launch the app 2. Wait for startup Expected behavior: The app should start normally. Actual behavior: The app crashes immediately with a traceback.",
  "label_candidates": ["bug"],
  "missing_information": []
}
```

For an incomplete report, the tool may instead suggest labels like `needs-info` and list the details that a maintainer should request before review.

## Maintainer workflow

This repository is designed around a simple maintainer-first workflow:

1. Receive a Markdown issue report.
2. Generate a summary for quick first-pass reading.
3. Suggest likely starting labels.
4. Detect what information is still missing.
5. Let a human maintainer make the final triage decision.

This repository also uses:
- issue templates for structured reports
- pull request templates for consistent review
- labels for triage and prioritization
- milestones for roadmap tracking
- CODEOWNERS for repository ownership clarity

## Current scope

The current scope is intentionally narrow:
- local issue triage
- maintainable CLI structure
- tested heuristics for first-pass maintainer assistance
- a foundation for future GitHub Action integration

This project does **not** auto-close issues or replace human judgment.
It is intended to support maintainers, not override them.

## Roadmap

### MVP v0.2
- [x] Improve label suggestion heuristics for incomplete bug reports
- [x] Add tests for triage label and missing-information heuristics
- [x] Improve question vs enhancement disambiguation
- [x] Support issue template-aware parsing

### Next
- [ ] Add confidence scoring to triage output
- [ ] Add configurable project-specific rules
- [ ] Add structured output modes for automation
- [ ] Add GitHub Action integration for new issues
- [ ] Add PR review brief generation
- [ ] Add release note draft support

## Project status

This repository is in early development, but it is actively maintained and already usable for local issue-triage experiments and workflow design.

Recent work has focused on improving triage quality, strengthening tests, and making the CLI more useful for real maintainer workflows.

## Contributing

Feedback, bug reports, and small focused pull requests are welcome.

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

## Security

Please read [SECURITY.md](./SECURITY.md) before reporting vulnerabilities.

## License

MIT. See [LICENSE](./LICENSE).
