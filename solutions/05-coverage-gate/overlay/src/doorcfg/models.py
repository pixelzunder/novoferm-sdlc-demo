"""Data structures. No business rules live here (see rules.py and data/rules.json)."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class DoorConfiguration:
    """What a customer asks for. Values are checked by rules.validate()."""

    width_mm: int
    height_mm: int
    surface: str
    drive: str
    options: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class Violation:
    """One broken rule. `code` is stable and safe to test against."""

    code: str
    message: str


MM2_PER_CM2 = 100


def opening_area_cm2(config: DoorConfiguration) -> int:
    """Area of the door opening in square centimetres (rounded down)."""
    return config.width_mm * config.height_mm // MM2_PER_CM2
