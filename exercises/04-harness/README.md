# Exercise 04 - On the loop: one prompt, the gates decide

**Time:** 15 minutes · **Book:** chapter 6, The Complete Harness · **You need:** an agent that
can run commands

**What you will see:** you do not read every step. The harness - rules file, context map,
locked tests, strict types, coverage - steers the agent, and you look at the result.

## The harness you are using

| Job | Component | In this repository |
|---|---|---|
| Know | Rules | `AGENTS.md` |
| Know | Context | `docs/architecture.md`, `docs/adr/` |
| Do | Tools | `python scripts/verify.py`, `python -m doorcfg` |
| Verify | Hooks | `.githooks/pre-commit` |
| Verify | Gates | ruff, mypy --strict, pytest with 100 % coverage |

## Steps

1. Put the gate in place. The tests are the contract and they are not yours to change:

   ```
   cp exercises/04-harness/test_quote.py tests/
   python scripts/verify.py        # red: the module does not exist yet
   ```

2. Send **one** prompt and take your hands off the keyboard:

   > Implement the quote described in exercises/04-harness/quote-spec.md. Follow AGENTS.md.
   > Do not modify any file in tests/. Do not stop until `python scripts/verify.py` is green.

3. Watch what the agent does, not what it types: Does it read `AGENTS.md` and the ADRs first?
   Does it run the gate itself? What does it do when mypy or the coverage gate is red?

4. When it is green: `git status` (did a test change?), then read `src/doorcfg/quote.py`.

5. **Retrospective - two minutes.** If the agent needed several attempts or went wrong: which
   sentence in `AGENTS.md`, which test or which line in the specification would have prevented
   it? Change that file, not only the code.

## Take to your own repo

- The pattern of `AGENTS.md`: context first, the two or three rules an agent cannot guess, and
  one command that must be green before "done".
- One command for all gates (`scripts/verify.py`) - the same for people, agents, hook and CI.
- Sample result: `python scripts/apply_solution.py 04`
