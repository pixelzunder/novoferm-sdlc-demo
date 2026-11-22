# Exercise 02 - From a vague wish to a specification

**Time:** 15 minutes · **Book:** chapter 4, Shaping Intent · **Works best in pairs**
(one plays the product owner)

**What you will see:** a person who reads an ambiguous wish asks a question. An agent fills the
gap with a guess. The specification is what remains once no open questions are left.

## Steps

1. Read `wish.md`. Write down, alone, what you would build. Compare with your neighbour -
   you will not have built the same thing.

2. Let the agent ask instead of build. In this repository, send (in plan mode if your tool
   has one):

   > Read exercises/02-spec/wish.md, docs/architecture.md and the ADRs. Do not write code.
   > List the questions you need answered before this can be built, most important first.

3. Answer the questions as product owner (invent sensible answers) and fill in
   `specs/intake-template.md` as a copy: `cp specs/intake-template.md specs/wicket-door.md`.
   Keep to the format: **three testable acceptance criteria, one edge case, one out-of-scope
   item**, plus the shape (option name, error codes, new fields in `data/rules.json`).

4. Check it: could a colleague write the tests from your card without asking you anything?

## Take to your own repo

- `specs/intake-template.md` - use it for the next ticket that goes to an agent.
- Behaviour first (acceptance criteria), shape second (names, types, codes).
- Sample result: `solutions/02-spec/wicket-door.md` (exercise 03 builds on it)
