# Exercise 05 - A gate beats a policy

**Time:** 15 minutes · **Book:** chapter 7, The Autonomy Spectrum · **You need:** an agent that
can run commands and commit

**What you will see:** "we always write tests" is a policy. An agent does not read policies,
and people forget them on Friday afternoon. A gate does not care what day it is.

## Steps

1. Activate the versioned hook (once per clone):

   ```
   git config core.hooksPath .githooks
   ```

2. **Ask for the wrong thing on purpose.** Send:

   > Add a function `opening_area_cm2(config: DoorConfiguration) -> int` to
   > src/doorcfg/models.py that returns width times height in square centimetres. Do NOT write
   > any tests for it. Then commit the change.

3. **The gate answers.** The commit is rejected: coverage is below 100 %, the report names the
   untested lines. (Some agents refuse to skip the tests or add them anyway - that is the
   model being careful, not your process being safe. Try a second model if you can.)

4. **Let the agent read the gate.** Send:

   > The commit was rejected. Run `python scripts/verify.py`, read the output, fix the cause
   > and commit again.

   The agent adds the missing test, the commit passes.

5. **Find the hole.** Run `git commit --no-verify --allow-empty -m "bypass"` - it works. A
   local hook is a courtesy. Look at `.github/workflows/verify.yml` and `azure-pipelines.yml`:
   the same gate, on the server, as a required check on `main`, is the one that holds.
   (Undo: `git reset --hard HEAD~1`.)

## Take to your own repo

- One threshold that fails the build (coverage, type errors, lint) is worth more than a page
  of guidelines. Start with the threshold you already meet today.
- Hooks live in the repository (`core.hooksPath`), not in `.git/hooks`, so every clone has them.
- Make the pipeline a required check in the branch policy.
- Sample result: `python scripts/apply_solution.py 05`
