# ADR-001: Money is an integer number of cents - APPROVED

## Context

Prices are added, multiplied by areas and percentages, and compared in tests. Binary floating
point cannot represent most decimal amounts exactly (`0.1 + 0.2 != 0.3`). A price that differs
by one cent between two runs is a defect a customer can see on an invoice.

## The absolute constraint

- You MUST represent every amount of money as an `int` in cents. Name the variable with the
  suffix `_cents`.
- You MUST NOT use `float`, `round()` or the `/` operator on amounts.
- You MUST express percentages as integers (percent or basis points) and apply them with
  integer arithmetic.
- You MUST round half up with `pricing.divide_half_up(numerator, denominator)`.

## Code reference

`src/doorcfg/pricing.py` - `divide_half_up` and `panel_price_cents` show the pattern.
