"""A deterministic gate for ADR-001: no floats, no round(), no true division.

    python check_money.py quote.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path


def problems(source: str) -> list[str]:
    found: list[str] = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            found.append(f"line {node.lineno}: float literal {node.value!r}")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            found.append(f"line {node.lineno}: true division '/' (use integer arithmetic)")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"float", "round"}
        ):
            found.append(f"line {node.lineno}: call to {node.func.id}()")
    return sorted(found)


def main(argv: list[str]) -> int:
    failed = False
    for name in argv:
        for problem in problems(Path(name).read_text(encoding="utf-8")):
            print(f"[FAIL] {name} {problem}")
            failed = True
    if not failed:
        print("[OK] Money is handled as integers (ADR-001).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
