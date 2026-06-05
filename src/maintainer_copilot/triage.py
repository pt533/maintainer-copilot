import re
from pathlib import Path

BUG_WORDS = {"error", "bug", "crash", "failed", "failure", "exception", "traceback"}
QUESTION_WORDS = {"how", "why", "can", "does", "question", "help"}
FEATURE_WORDS = {"feature", "request", "would like", "enhancement", "support"}

SECTION_ALIASES = {
    "version": "version",
    "app version": "version",
    "commit sha": "version",
    "environment": "environment",
    "runtime or os environment": "environment",
    "os": "environment",
    "steps to reproduce": "steps_to_reproduce",
    "reproduction steps": "steps_to_reproduce",
    "how to reproduce": "steps_to_reproduce",
    "expected behavior": "expected_behavior",
    "what did you expect?": "expected_behavior",
    "what did you expect": "expected_behavior",
    "actual behavior": "actual_behavior",
    "what happened?": "actual_behavior",
    "what happened": "actual_behavior",
}


def simple_summary(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "Empty issue."
    joined = " ".join(lines)
    return joined[:220] + ("..." if len(joined) > 220 else "")


def _normalize_section_name(name: str) -> str | None:
    normalized = re.sub(r"\s+", " ", name.strip().strip(":").lower())
    return SECTION_ALIASES.get(normalized)


def parse_issue_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_lines
        if current_key:
            value = "\n".join(current_lines).strip()
            if value:
                sections[current_key] = value
        current_key = None
        current_lines = []

    for raw_line in text.splitlines():
        stripped = raw_line.strip()

        markdown_heading = re.match(r"^#{1,6}\s+(.+?)\s*$", stripped)
        if markdown_heading:
            normalized = _normalize_section_name(markdown_heading.group(1))
            if normalized:
                flush()
                current_key = normalized
                continue

        if ":" in stripped:
            head, _, tail = stripped.partition(":")
            normalized = _normalize_section_name(head)
            if normalized:
                flush()
                current_key = normalized
                if tail.strip():
                    current_lines.append(tail.strip())
                continue

        if current_key:
            current_lines.append(raw_line.rstrip())

    flush()
    return sections


def suggest_labels(text: str) -> list[str]:
    lowered = text.lower()
    labels = []

    bug_like = any(word in lowered for word in BUG_WORDS)

    lines = [line.strip().lower() for line in text.splitlines() if line.strip()]
    title = lines[0] if lines else ""
    question_like = any(word in lowered for word in QUESTION_WORDS)
    feature_like = any(word in lowered for word in FEATURE_WORDS)

    question_title_prefixes = (
        "title: how",
        "title: why",
        "title: can",
        "title: does",
        "how",
        "why",
        "can",
        "does",
    )

    if bug_like:
        labels.append("bug")
    if question_like:
        labels.append("question")
    if feature_like and not title.startswith(question_title_prefixes):
        labels.append("enhancement")
    if not labels:
        labels.append("needs-triage")

    missing_bug_context = any(
        phrase not in lowered
        for phrase in [
            "version",
            "steps to reproduce",
            "expected behavior",
            "actual behavior",
        ]
    )

    if bug_like and missing_bug_context:
        labels.append("needs-info")

    return list(dict.fromkeys(labels))


def missing_information(text: str) -> list[str]:
    lowered = text.lower()
    sections = parse_issue_sections(text)

    checks = {
        "app version or commit SHA": (
            ["version", "commit", "sha"],
            "version",
        ),
        "runtime or OS environment": (
            ["environment", "os", "ubuntu", "windows", "macos", "linux"],
            "environment",
        ),
        "steps to reproduce": (
            ["steps to reproduce", "reproduce", "how to reproduce"],
            "steps_to_reproduce",
        ),
        "expected behavior": (
            ["expected", "should happen"],
            "expected_behavior",
        ),
        "actual behavior": (
            ["actual", "happened", "instead"],
            "actual_behavior",
        ),
    }

    missing = []
    for name, (keywords, section_key) in checks.items():
        has_section = bool(sections.get(section_key))
        has_keywords = any(keyword in lowered for keyword in keywords)
        if not has_section and not has_keywords:
            missing.append(name)
    return missing


def triage_issue_file(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    return {
        "summary": simple_summary(text),
        "label_candidates": suggest_labels(text),
        "missing_information": missing_information(text),
    }
