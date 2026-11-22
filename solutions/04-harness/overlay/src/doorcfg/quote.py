"""A quote with line items, VAT and gross total. ADR-001: integer cents only."""

from __future__ import annotations

from dataclasses import dataclass

from doorcfg.models import DoorConfiguration
from doorcfg.pricing import InvalidConfigurationError, divide_half_up, panel_price_cents
from doorcfg.rules import RuleSet, validate

PERCENT = 100


@dataclass(frozen=True)
class LineItem:
    label: str
    amount_cents: int


@dataclass(frozen=True)
class Quote:
    items: tuple[LineItem, ...]
    net_cents: int
    vat_cents: int
    gross_cents: int


def build_quote(config: DoorConfiguration, rules: RuleSet) -> Quote:
    """Builds the quote. Raises InvalidConfigurationError for invalid configurations."""
    violations = validate(config, rules)
    if violations:
        raise InvalidConfigurationError(violations)

    items = (
        LineItem(f"panel:{config.surface}", panel_price_cents(config, rules)),
        LineItem(f"drive:{config.drive}", rules.drives[config.drive].price_cents),
        *(
            LineItem(f"option:{name}", rules.options[name].price_cents)
            for name in sorted(config.options)
        ),
    )
    net_cents = sum(item.amount_cents for item in items)
    vat_cents = divide_half_up(net_cents * rules.vat_percent, PERCENT)
    return Quote(items, net_cents, vat_cents, net_cents + vat_cents)
