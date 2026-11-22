"""Tiny price helper for exercise 01. Amounts are integers in cents."""

SPECIAL_COLOUR_SURCHARGE_BASIS_POINTS = 750  # 7.5 %
BASIS_POINTS = 10_000


def total_cents(base_cents: int, option_cents: list[int]) -> int:
    """Adds the option prices to the base price."""
    return base_cents + sum(option_cents)


def with_special_colour_surcharge(net_cents: int) -> int:
    """Net price plus 7.5 % surcharge, rounded half up to the cent."""
    surcharge_cents = (
        2 * net_cents * SPECIAL_COLOUR_SURCHARGE_BASIS_POINTS + BASIS_POINTS
    ) // (2 * BASIS_POINTS)
    return net_cents + surcharge_cents
