# Exercise 01 - Context experiment: same prompt, without and with an ADR

**Time:** 10 minutes · **Book:** chapter 3, Curating Context · **You need:** any coding agent

**What you will see:** the agent is not "smarter" in the second run. The environment is.

## Steps

1. **Work outside this repository**, so the agent cannot see its rules:

   ```
   mkdir ../ctx-demo
   cp exercises/01-context-adr/quote.py exercises/01-context-adr/check_money.py ../ctx-demo/
   cd ../ctx-demo
   ```

2. **Open loop.** Start your agent in `ctx-demo` and send:

   > In quote.py, add a function that applies a 7.5 % surcharge for special colours to a net
   > price and returns the new price.

   Run `python check_money.py quote.py`. Most agents write `net * 1.075` or use `round()` -
   the check reports it.

3. **Add the context.** Undo the change (`cp ../novoferm-agentic-sdlc-demo/exercises/01-context-adr/quote.py .`),
   then copy the decision record:

   ```
   mkdir docs
   cp ../novoferm-agentic-sdlc-demo/docs/adr/ADR-001-money-in-cents.md docs/
   ```

4. **Closed loop.** Start a **new** session and send:

   > Read docs/ADR-001-money-in-cents.md. Then, in quote.py, add a function that applies a
   > 7.5 % surcharge for special colours to a net price and returns the new price. When you are
   > done, run `python check_money.py quote.py` and fix what it reports.

   The result uses integer arithmetic, and the check is green.

## If your agent got it right in step 2

Good models often do. Then ask yourself: would it get it right *every* time, for *every*
colleague, with *every* model? The ADR and the check make the answer yes.

## Take to your own repo

- One ADR in four parts: title + status, context, the absolute constraint (MUST / MUST NOT),
  code reference. Keep it under one screen.
- Every rule you can check with a script, check with a script (`check_money.py` is 40 lines).
- Sample result: `solutions/01-context-adr/quote.py`
