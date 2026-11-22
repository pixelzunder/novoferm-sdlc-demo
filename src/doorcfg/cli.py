"""Command line entry point: python -m doorcfg --width 2500 --height 2125 ..."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from doorcfg.models import DoorConfiguration
from doorcfg.pricing import net_price_cents
from doorcfg.rules import load_rules, validate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="doorcfg", description="Fictional door configurator")
    parser.add_argument("--width", type=int, required=True, help="width in mm")
    parser.add_argument("--height", type=int, required=True, help="height in mm")
    parser.add_argument("--surface", required=True)
    parser.add_argument("--drive", default="manual")
    parser.add_argument("--option", action="append", default=[], help="repeatable")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = DoorConfiguration(
        width_mm=args.width,
        height_mm=args.height,
        surface=args.surface,
        drive=args.drive,
        options=frozenset(args.option),
    )
    rules = load_rules()
    violations = validate(config, rules)
    result = {
        "valid": not violations,
        "violations": [{"code": v.code, "message": v.message} for v in violations],
        "net_price_cents": None if violations else net_price_cents(config, rules),
    }
    print(json.dumps(result, indent=2))
    return 1 if violations else 0
