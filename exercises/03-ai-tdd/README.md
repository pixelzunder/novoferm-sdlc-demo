# Exercise 03 - AI-TDD: you own the tests, the agent makes them pass

**Time:** 15 minutes · **Book:** chapter 5, Closing Loops · **You need:** any coding agent

**What you will see:** a test is two things - proof, and pressure on the design. The agent may
write the code. It may not move the goalposts.

Specification: `solutions/02-spec/wicket-door.md` (or your own from exercise 02).

## Steps

1. **RED - you own the intent.** Send:

   > Read solutions/02-spec/wicket-door.md and tests/test_rules.py. In
   > tests/test_wicket_door.py, write pytest tests for the wicket door: one test per acceptance
   > criterion and one for the edge case. Read limits from the `rules` fixture instead of
   > repeating numbers. Do not write or change any implementation.

   **Read every assertion.** Is the edge case really the inclusive limit? Then run
   `python scripts/verify.py` - it must be red, for the right reason.

2. **GREEN - the agent implements.** Start a new session and send:

   > The tests in tests/test_wicket_door.py fail. Implement the wicket door so that
   > `python scripts/verify.py` is green. Follow AGENTS.md. Do not modify any file in tests/.

   Check with `git status` that no test file changed.

3. **REFACTOR.** Send:

   > All gates are green. Look at validate() in src/doorcfg/rules.py: simplify it if the new
   > checks made it harder to read. The gates must stay green.

4. **Review the residue.** Open the diff and ask the one question the gates cannot answer:
   *How could this pass every gate and still be wrong?* (Look for `2500` or `"wicket_door"`
   in Python code - that would break ADR-002 and no test would notice.)

## Take to your own repo

- The three prompts above. The sentence that matters most: "Do not modify any file in tests/."
- For existing code without tests: first pin today's behaviour with tests, then change it.
- Sample result: `python scripts/apply_solution.py 03`
