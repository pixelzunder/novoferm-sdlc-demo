"""Net price calculation.

ADR-001: money is an integer number of cents. No floats, no round().
"""

from __future__ import annotations

from doorcfg.models import DoorConfiguration, Violation
from doorcfg.rules import RuleSet, validate

MM2_PER_M2 = 1_000_000


class InvalidConfigurationError(ValueError):
    """Raised when a price is requested for a configuration that breaks a rule."""

    def __init__(self, violations: list[Violation]) -> None:
        super().__init__(", ".join(violation.code for violation in violations))
        self.violations = violations


def divide_half_up(numerator: int, denominator: int) -> int:
    """Integer division that rounds half up (for non-negative numbers)."""
    return (2 * numerator + denominator) // (2 * denominator)


def panel_price_cents(config: DoorConfiguration, rules: RuleSet) -> int:
    area_mm2 = config.width_mm * config.height_mm
    return divide_half_up(area_mm2 * rules.surfaces[config.surface], MM2_PER_M2)


def net_price_cents(config: DoorConfiguration, rules: RuleSet) -> int:
    """Net price in cents. Raises InvalidConfigurationError for invalid configurations."""
    violations = validate(config, rules)
    if violations:
        raise InvalidConfigurationError(violations)

    total = panel_price_cents(config, rules)
    total += rules.drives[config.drive].price_cents
    total += sum(rules.options[name].price_cents for name in config.options)
    return total
