"""The verification gate: lint, strict types, tests with 100 % coverage.

Run it with `python scripts/verify.py`. It works the same on Windows, macOS and Linux,
for humans, for agents, in the pre-commit hook and in CI.
"""

from __future__ import annotations

import subprocess
import sys

STEPS: list[tuple[str, list[str]]] = [
    ("lint (ruff)", [sys.executable, "-m", "ruff", "check", "."]),
    ("types (mypy --strict)", [sys.executable, "-m", "mypy"]),
    ("tests + coverage (pytest)", [sys.executable, "-m", "pytest", "-q"]),
]


def main() -> int:
    for name, command in STEPS:
        print(f"\n=== {name} ===", flush=True)
        if subprocess.run(command, check=False).returncode != 0:
            print(f"\n[FAIL] Gate '{name}' is red. Fix it and run the gate again.")
            return 1
    print("\n[OK] All gates are green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
