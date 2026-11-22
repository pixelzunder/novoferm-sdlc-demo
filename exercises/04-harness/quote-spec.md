# Specification: quote with VAT

## Objective
Sales can show a customer a quote with line items, net total, VAT and gross total.

## Behaviour
1. `build_quote(config, rules)` returns a `Quote` for a valid configuration.
2. Line items, in this order: the panel (`panel:<surface>`), the drive (`drive:<name>`, listed
   even when it costs 0), then one item per option (`option:<name>`) in alphabetical order.
3. `net_cents` is the sum of the line items and equals `pricing.net_price_cents`.
4. `vat_cents` is `net_cents` times the VAT rate of the rule set, rounded half up to the cent.
   `gross_cents = net_cents + vat_cents`.
5. An invalid configuration raises `pricing.InvalidConfigurationError`.

## Shape
New module `src/doorcfg/quote.py`:

- `LineItem` (frozen dataclass): `label: str`, `amount_cents: int`
- `Quote` (frozen dataclass): `items: tuple[LineItem, ...]`, `net_cents: int`,
  `vat_cents: int`, `gross_cents: int`
- `build_quote(config: DoorConfiguration, rules: RuleSet) -> Quote`

## Out of scope
Discounts, currencies other than euro, output formatting.

## Constraints
ADR-001, ADR-002. The VAT rate is already in `data/rules.json` (`vat_percent`).
