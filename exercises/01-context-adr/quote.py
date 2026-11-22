"""Tiny price helper for exercise 01. Amounts are integers in cents."""


def total_cents(base_cents: int, option_cents: list[int]) -> int:
    """Adds the option prices to the base price."""
    return base_cents + sum(option_cents)
