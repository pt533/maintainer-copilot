# Contributing to maintainer-copilot

Thanks for your interest in contributing.

## Before you start

Please open an issue first for:
- larger feature ideas
- architecture changes
- behavior changes that affect CLI output

Small typo fixes and documentation improvements can be submitted directly.

## Development setup

```bash
git clone https://github.com/pt533/maintainer-copilot.git
cd maintainer-copilot
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Contribution guidelines

- Keep changes small and focused.
- Prefer simple, readable code.
- Update README when behavior changes.
- Add or update tests when logic changes.
- Avoid adding external services or API dependencies unless discussed first.

## Pull request checklist

- Explain what changed.
- Explain why the change is needed.
- Link the related issue if one exists.
- Confirm that local tests or manual checks were performed.

## Scope for early contributions

Good first contributions include:
- improving issue triage heuristics
- improving CLI help text
- refining JSON output structure
- improving docs and examples
