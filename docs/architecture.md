# Architecture (context map)

## Purpose

A small, **fictional** configurator for sectional garage doors. It answers two questions:
*Can this door be built?* and *What does it cost (net)?* All rules and prices are invented for
the workshop.

## Data flow

```
customer input -> DoorConfiguration -> rules.validate() -> list of Violation
                                    -> pricing.net_price_cents() -> int (cents)
```

## Modules

| Module | Responsibility | Must not |
|---|---|---|
| `src/doorcfg/models.py` | Data structures (`DoorConfiguration`, `Violation`) | contain business rules |
| `src/doorcfg/rules.py` | Load `data/rules.json`, validate a configuration | contain thresholds or prices |
| `src/doorcfg/pricing.py` | Net price in integer cents | use floats, call the CLI |
| `src/doorcfg/cli.py` | Parse arguments, print JSON | contain rules or price logic |
| `data/rules.json` | The rule set: ranges, allowed values, prices | - |

Dependencies point one way: `cli -> pricing -> rules -> models`.

## Data model

- `DoorConfiguration`: `width_mm`, `height_mm` (int, millimetres), `surface`, `drive` (names
  from the rule set), `options` (set of names from the rule set).
- `Violation`: `code` (stable, tested) and `message` (for people, may change).

## Where to look

- Decisions: `docs/adr/` (current), `docs/adr/archive/` (superseded - do not follow).
- Input shape: `specs/door-configuration.schema.json`.
- How to verify: `python scripts/verify.py`.
