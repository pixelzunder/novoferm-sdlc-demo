# Intent card: <feature name>

Fill this in **before** an agent builds anything - ideally product owner and developer together.
An agent honours exactly what is written down.

## Objective
<One sentence: who gets which value?>

## Behaviour - three testable acceptance criteria
1. Given ..., when ..., then ...
2. Given ..., when ..., then ...
3. Given ..., when ..., then ...

## One named edge case
<The case that is easy to get wrong: a boundary, an empty value, a conflict.>

## Out of scope
<One thing that will explicitly not be built now.>

## Shape
<Fields, types, names, error codes. Link or extend the schema in `specs/`.>

## Constraints
<ADRs that apply, modules that must not change.>

## Red zones (need a human decision)
<e.g. changes to prices, to existing error codes, to the data file format.>

## How we verify
<Which tests, which command, which evidence goes into the pull request.>
