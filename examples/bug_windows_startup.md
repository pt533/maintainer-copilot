Title: Crash when starting app on Windows

Version: 0.1.0
Environment: Windows 11, Python 3.11

Steps to reproduce:
1. Install the package in a fresh virtual environment
2. Run `mcopilot sample_issue.md`
3. Observe the startup failure

Expected behavior:
The CLI should print triage JSON output.

Actual behavior:
The CLI exits immediately with an error before producing output.

Additional notes:
The same workflow worked on Python 3.10.
