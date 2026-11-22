# Intent card: wicket door (a door inside the garage door)

## Objective
Customers can order a wicket door so they can walk in without opening the garage door.

## Behaviour - three testable acceptance criteria
1. Given a valid door that is at least as wide as the wicket door minimum width, when the
   option `wicket_door` is selected, then the configuration is valid and the net price rises
   by the wicket door price.
2. Given a door narrower than the minimum width, when `wicket_door` is selected, then
   validation returns the violation `OPTION_TOO_NARROW`.
3. Given a door with `wicket_door` and `windows`, then validation returns exactly one
   violation `OPTIONS_INCOMPATIBLE`.

## One named edge case
A door whose width is **exactly** the minimum width is valid (the limit is inclusive).

## Out of scope
Position of the wicket door (left, right, centre) and its threshold height.

## Shape
- Option name: `wicket_door`
- `data/rules.json`, per option, both optional:
  - `min_width_mm` (integer, default 0)
  - `excludes` (list of option names, default empty)
- Values for now: price 89 000 cents, `min_width_mm` 2500, `excludes: ["windows"]`,
  `requires_drive: false`
- New violation codes: `OPTION_TOO_NARROW`, `OPTIONS_INCOMPATIBLE`
- `specs/door-configuration.schema.json`: add `wicket_door` to the option enum

## Constraints
ADR-001 (money in cents), ADR-002 (rules are data: no 2500 and no option name in Python code).
Existing violation codes and existing tests stay unchanged.

## Red zones (need a human decision)
Changing prices of existing options; renaming existing violation codes.

## How we verify
New tests in `tests/test_wicket_door.py`, one per criterion plus the edge case, reading the
limit from the loaded rule set. `python scripts/verify.py` green. Evidence in the PR: output of
`python -m doorcfg --width 2500 --height 2125 --surface smooth --drive standard --option wicket_door`.
