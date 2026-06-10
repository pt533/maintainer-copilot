from maintainer_copilot.triage import parse_issue_sections, suggest_labels, missing_information


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

def test_question_like_request_prefers_question():
    text = """Title: How can I configure labels for my repository?

Can you help me understand how to set this up?
"""
    labels = suggest_labels(text)

    assert "question" in labels
    assert "enhancement" not in labels


def test_enhancement_request_prefers_enhancement():
    text = """Title: Feature request: support custom default labels

I would like support for configuring default labels during triage.
"""
    labels = suggest_labels(text)

    assert "enhancement" in labels
    assert "question" not in labels

def test_question_about_support_prefers_question():
    text = """Title: Can you support configuration for labels?

How can I configure labels for my repository?
"""
    labels = suggest_labels(text)

    assert "question" in labels
    assert "enhancement" not in labels

def test_parse_issue_sections_normalizes_template_headings():
    text = """Title: Bug report

## Reproduction steps
1. Run the CLI
2. Observe the output

## What did you expect?
The command succeeds.

## What happened?
A traceback is printed.
"""
    sections = parse_issue_sections(text)

    assert sections["steps_to_reproduce"] == "1. Run the CLI\n2. Observe the output"
    assert sections["expected_behavior"] == "The command succeeds."
    assert sections["actual_behavior"] == "A traceback is printed."


def test_missing_information_uses_template_sections_and_keeps_free_form_fallback():
    template_text = """Title: Crash report

## Version
1.2.3

## Environment
Ubuntu 24.04

## Steps to reproduce
1. Run the CLI

## Expected behavior
The command succeeds.

## Actual behavior
The command crashes.
"""
    free_form_text = """Title: Crash report

Version: 1.2.3
Environment: Ubuntu 24.04
Steps to reproduce: run the CLI
Expected behavior: the command succeeds
Actual behavior: the command crashes
"""

    assert missing_information(template_text) == []
    assert missing_information(free_form_text) == []

def test_missing_information_zero_for_both_template_and_freeform():
    """template 形式と free-form 形式の両方で missing_information=[] になることを確認"""
    template_text = """Title: Bug

## Version
1.2.3

## Environment
Ubuntu

## Steps to reproduce
run cli

## Expected behavior
success

## Actual behavior
crash
"""
    free_form_text = """Title: Bug

Version: 1.2.3
Environment: Ubuntu
Steps to reproduce: run cli
Expected behavior: success
Actual behavior: crash
"""
    assert missing_information(template_text) == []
    assert missing_information(free_form_text) == []
