"""Loads the rule set from data/rules.json and validates configurations against it.

ADR-002: thresholds, allowed values and prices are data. Do not hard-code them here.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from doorcfg.models import DoorConfiguration, Violation

DEFAULT_RULES_PATH = Path(__file__).resolve().parents[2] / "data" / "rules.json"

MANUAL_DRIVE = "manual"


@dataclass(frozen=True)
class Range:
    min: int
    max: int

    def contains(self, value: int) -> bool:
        return self.min <= value <= self.max


@dataclass(frozen=True)
class DriveRule:
    price_cents: int
    max_width_mm: int


@dataclass(frozen=True)
class OptionRule:
    price_cents: int
    requires_drive: bool
    min_width_mm: int = 0
    excludes: frozenset[str] = frozenset()


@dataclass(frozen=True)
class RuleSet:
    width_mm: Range
    height_mm: Range
    surfaces: dict[str, int]
    drives: dict[str, DriveRule]
    options: dict[str, OptionRule]
    vat_percent: int


def _range(raw: dict[str, Any]) -> Range:
    return Range(min=int(raw["min"]), max=int(raw["max"]))


def parse_rules(raw: dict[str, Any]) -> RuleSet:
    """Turns the JSON document into typed rules. Raises KeyError on missing fields."""
    return RuleSet(
        width_mm=_range(raw["dimensions"]["width_mm"]),
        height_mm=_range(raw["dimensions"]["height_mm"]),
        surfaces={
            name: int(entry["price_cents_per_m2"]) for name, entry in raw["surfaces"].items()
        },
        drives={
            name: DriveRule(
                price_cents=int(entry["price_cents"]),
                max_width_mm=int(entry["max_width_mm"]),
            )
            for name, entry in raw["drives"].items()
        },
        options={
            name: OptionRule(
                price_cents=int(entry["price_cents"]),
                requires_drive=bool(entry["requires_drive"]),
                min_width_mm=int(entry.get("min_width_mm", 0)),
                excludes=frozenset(entry.get("excludes", [])),
            )
            for name, entry in raw["options"].items()
        },
        vat_percent=int(raw["vat_percent"]),
    )


def load_rules(path: Path = DEFAULT_RULES_PATH) -> RuleSet:
    with path.open(encoding="utf-8") as handle:
        raw: dict[str, Any] = json.load(handle)
    return parse_rules(raw)


def validate(config: DoorConfiguration, rules: RuleSet) -> list[Violation]:
    """Returns every broken rule. An empty list means the configuration can be built."""
    violations: list[Violation] = []

    if not rules.width_mm.contains(config.width_mm):
        violations.append(
            Violation(
                "WIDTH_OUT_OF_RANGE",
                f"Width must be between {rules.width_mm.min} and {rules.width_mm.max} mm.",
            )
        )
    if not rules.height_mm.contains(config.height_mm):
        violations.append(
            Violation(
                "HEIGHT_OUT_OF_RANGE",
                f"Height must be between {rules.height_mm.min} and {rules.height_mm.max} mm.",
            )
        )
    if config.surface not in rules.surfaces:
        violations.append(Violation("UNKNOWN_SURFACE", f"Unknown surface '{config.surface}'."))

    drive = rules.drives.get(config.drive)
    if drive is None:
        violations.append(Violation("UNKNOWN_DRIVE", f"Unknown drive '{config.drive}'."))
    elif config.width_mm > drive.max_width_mm:
        violations.append(
            Violation(
                "DRIVE_TOO_WEAK",
                f"Drive '{config.drive}' supports doors up to {drive.max_width_mm} mm width.",
            )
        )

    for name in sorted(config.options):
        option = rules.options.get(name)
        if option is None:
            violations.append(Violation("UNKNOWN_OPTION", f"Unknown option '{name}'."))
            continue
        if option.requires_drive and config.drive == MANUAL_DRIVE:
            violations.append(
                Violation("OPTION_REQUIRES_DRIVE", f"Option '{name}' needs a motor drive.")
            )
        if config.width_mm < option.min_width_mm:
            violations.append(
                Violation(
                    "OPTION_TOO_NARROW",
                    f"Option '{name}' needs a door width of at least {option.min_width_mm} mm.",
                )
            )
        for other in sorted(option.excludes & config.options):
            violations.append(
                Violation(
                    "OPTIONS_INCOMPATIBLE",
                    f"Option '{name}' cannot be combined with '{other}'.",
                )
            )

    return violations
