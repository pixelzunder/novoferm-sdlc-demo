# ADR-002: Rules are data - APPROVED

## Context

Product management changes ranges, compatibility rules and prices far more often than the code
changes. A threshold that is hard-coded in Python is invisible to them and is easily missed in
a review.

## The absolute constraint

- You MUST store thresholds, allowed values, percentages and prices in `data/rules.json`.
- You MUST NOT write such numbers or names as literals in `src/`.
- When a rule needs a new kind of value, you MUST extend `RuleSet` in `src/doorcfg/rules.py`
  and parse it in `parse_rules`.
- Tests SHOULD read limits from the loaded rule set instead of repeating the numbers.

## Code reference

`src/doorcfg/rules.py` - `DriveRule.max_width_mm` is a threshold that lives in the data file.
