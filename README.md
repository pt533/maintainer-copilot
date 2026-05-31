# maintainer-copilot

A minimal open-source starter for OSS maintainers.

This first version focuses on issue triage only:
- Summarize an issue
- Suggest labels
- Point out missing information

## Why

Open-source maintainers spend time on repetitive issue triage.
This project aims to reduce that burden with a small, understandable tool that can grow over time.

## Current scope

```bash
mcopilot examples/sample_issue.md
```

## Output

The command returns JSON with:
- summary
- label_candidates
- missing_information

## Roadmap

- [x] Local CLI for issue triage
- [ ] GitHub Action for new issues
- [ ] PR review brief
- [ ] Release draft assist
