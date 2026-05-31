# maintainer-copilot

A small open-source CLI for OSS maintainer workflows.

The current version focuses on **issue triage**:
- summarize an issue
- suggest labels
- point out missing information before review

## Why

Maintainers spend time on repetitive first-pass work before they can make real decisions.
This project aims to reduce that overhead with a small, understandable, local-first tool.

It is intentionally starting from one narrow maintainer task:
issue triage.

## What it does

Given a Markdown issue file, `maintainer-copilot` returns JSON with:
- `summary`
- `label_candidates`
- `missing_information`

Example output:

```json
{
  "summary": "Title: Crash when starting app on Windows...",
  "label_candidates": ["bug", "needs-info"],
  "missing_information": [
    "app version or commit SHA",
    "steps to reproduce"
  ]
}
```

## Quick start

### 1. Clone

```bash
git clone https://github.com/pt533/maintainer-copilot.git
cd maintainer-copilot
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install

```bash
pip install -e .
```

### 4. Run

```bash
mcopilot examples/sample_issue.md
```

## Current scope

This repository is currently a minimal starter for:
- local issue triage
- maintainable CLI structure
- future GitHub Action integration

## Roadmap

- [x] Local CLI for issue triage
- [ ] Better label heuristics
- [ ] Configurable rules
- [ ] GitHub Action for new issues
- [ ] PR review brief generation
- [ ] Release note draft support

## Why this project matters

Open-source maintenance is not only code writing.
A lot of work is repetitive review preparation, issue cleanup, and release preparation.

This project is meant to grow into a practical maintainer assistant for those workflows.

## Contributing

This project is currently early-stage, but feedback and small improvements are welcome.

## License

MIT
