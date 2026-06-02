from maintainer_copilot.triage import suggest_labels, missing_information


def test_complete_bug_does_not_get_needs_info():
    text = """Title: Crash when starting app on Windows

Version: 0.1.0
Environment: Windows 11

Steps to reproduce:
1. Launch the app
2. Wait for startup

Expected behavior:
The app should start normally.

Actual behavior:
The app crashes immediately with a traceback.
"""
    labels = suggest_labels(text)

    assert "bug" in labels
    assert "needs-info" not in labels


def test_incomplete_bug_gets_needs_info():
    text = """Title: App crashes on startup

I get an error when launching the app.
It crashes immediately.
"""
    labels = suggest_labels(text)

    assert "bug" in labels
    assert "needs-info" in labels


def test_non_bug_does_not_get_needs_info():
    text = """Title: How do I configure labels?

Can you help me understand how to set this up?
"""
    labels = suggest_labels(text)

    assert "question" in labels
    assert "needs-info" not in labels


def test_missing_information_lists_expected_bug_fields():
    text = """Title: App crashes on startup

I get an error when launching the app.
"""
    missing = missing_information(text)

    assert "app version or commit SHA" in missing
    assert "steps to reproduce" in missing
    assert "expected behavior" in missing
    assert "actual behavior" in missing
