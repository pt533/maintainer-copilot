import json
import typer

from .triage import triage_issue_file

def main(issue_file: str):
    result = triage_issue_file(issue_file)
    print(json.dumps(result, ensure_ascii=False, indent=2))

def run():
    typer.run(main)

if __name__ == "__main__":
    run()
