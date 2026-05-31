from pathlib import Path

BUG_WORDS = {"error", "bug", "crash", "failed", "failure", "exception", "traceback"}
QUESTION_WORDS = {"how", "why", "can", "does", "question", "help"}
FEATURE_WORDS = {"feature", "request", "would like", "enhancement", "support"}

def simple_summary(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "Empty issue."
    joined = " ".join(lines)
    return joined[:220] + ("..." if len(joined) > 220 else "")

def suggest_labels(text: str) -> list[str]:
    lowered = text.lower()
    labels = []

    if any(word in lowered for word in BUG_WORDS):
        labels.append("bug")
    if any(word in lowered for word in QUESTION_WORDS):
        labels.append("question")
    if any(word in lowered for word in FEATURE_WORDS):
        labels.append("enhancement")
    if not labels:
        labels.append("needs-triage")
    if "version" not in lowered or "environment" not in lowered:
        labels.append("needs-info")

    return list(dict.fromkeys(labels))

def missing_information(text: str) -> list[str]:
    lowered = text.lower()
    checks = {
        "app version or commit SHA": ["version", "commit", "sha"],
        "runtime or OS environment": ["environment", "os", "ubuntu", "windows", "macos", "linux"],
        "steps to reproduce": ["steps to reproduce", "reproduce", "how to reproduce"],
        "expected behavior": ["expected", "should happen"],
        "actual behavior": ["actual", "happened", "instead"],
    }

    missing = []
    for name, keywords in checks.items():
        if not any(keyword in lowered for keyword in keywords):
            missing.append(name)
    return missing

def triage_issue_file(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    return {
        "summary": simple_summary(text),
        "label_candidates": suggest_labels(text),
        "missing_information": missing_information(text),
    }
