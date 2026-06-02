import json
import os
import subprocess
import sys


def test_cli_smoke_with_sample_issue():
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"

    result = subprocess.run(
        [sys.executable, "-m", "maintainer_copilot.cli", "examples/sample_issue.md"],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )

    assert result.returncode == 0

    data = json.loads(result.stdout)

    assert "summary" in data
    assert "label_candidates" in data
    assert "missing_information" in data
    assert isinstance(data["label_candidates"], list)
    assert isinstance(data["missing_information"], list)
