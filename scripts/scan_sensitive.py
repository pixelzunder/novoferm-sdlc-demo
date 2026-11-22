"""Blocks secrets and personal data before they reach the repository.

    python scripts/scan_sensitive.py            # scans the files staged for commit
    python scripts/scan_sensitive.py --all      # scans every tracked file (CI)
    python scripts/scan_sensitive.py a.py b.md  # scans the given files

Matches are reported redacted. Exit code 1 means: do not commit.
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SAFE_EMAIL_DOMAINS = {"example.com", "example.org", "localhost"}

# Paths that contain deliberate findings: the exercise 06 seed data and the scanner's own tests.
ALLOWED_PREFIXES = ("exercises/06-pii-gate/seed/", "tests/test_scan_sensitive.py")

PATTERNS: dict[str, re.Pattern[str]] = {
    "API key": re.compile(r"\bnvf_(?:live|test)_[A-Za-z0-9]{24,}\b"),
    "hard-coded credential": re.compile(
        r"(?i)(?<![a-z])(?:password|passwd|secret|api[_-]?key|token)\s*[:=]\s*[\"'][^\"'\s]{8,}[\"']"
    ),
    "IBAN": re.compile(r"\b[A-Z]{2}\d{2}(?: ?\d{4}){4} ?\d{2}\b"),
    "phone number": re.compile(r"(?<!\w)\+49[\d /()-]{8,}\d"),
    "e-mail address": re.compile(r"\b[\w.+-]+@([\w-]+(?:\.[\w-]+)+)\b"),
}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    kind: str
    excerpt: str


def redact(text: str) -> str:
    return text[:4] + "*" * max(len(text) - 4, 4)


def scan_text(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for kind, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                if kind == "e-mail address" and match.group(1).lower() in SAFE_EMAIL_DOMAINS:
                    continue
                findings.append(Finding(path, number, kind, redact(match.group(0))))
    return findings


def is_allowed(path: str) -> bool:
    return path.replace("\\", "/").startswith(ALLOWED_PREFIXES)


def scan_paths(paths: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        file = Path(path)
        if is_allowed(path) or not file.is_file():
            continue
        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        findings.extend(scan_text(path, text))
    return findings


def git_files(*args: str) -> list[str]:
    output = subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout
    return [line for line in output.splitlines() if line]


def main(argv: list[str]) -> int:
    if argv == ["--all"]:
        paths = git_files("ls-files")
    elif argv:
        paths = argv
    else:
        paths = git_files("diff", "--cached", "--name-only", "--diff-filter=ACM")

    findings = scan_paths(paths)
    if not findings:
        print(f"[OK] No secrets or personal data in {len(paths)} file(s).")
        return 0

    print(f"[BLOCKED] {len(findings)} finding(s) in {len({f.path for f in findings})} file(s):\n")
    for finding in findings:
        print(f"  {finding.path}:{finding.line}  {finding.kind}: {finding.excerpt}")
    print(
        "\nHow to fix: read secrets from environment variables, use synthetic data"
        "\n(example.com addresses, obviously fake numbers) and write [REDACTED] in documents."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
