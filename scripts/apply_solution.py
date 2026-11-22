"""Copies a sample solution into the working tree: python scripts/apply_solution.py 03

Undo with `git restore . && git clean -fd tests src` (this discards your own changes too).
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    matches = sorted((ROOT / "solutions").glob(f"{argv[0]}-*/overlay"))
    if not matches:
        print(f"No overlay solution for exercise '{argv[0]}'. See solutions/ for reference files.")
        return 1
    overlay = matches[0]
    for source in sorted(path for path in overlay.rglob("*") if path.is_file()):
        target = ROOT / source.relative_to(overlay)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        print(f"copied {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
