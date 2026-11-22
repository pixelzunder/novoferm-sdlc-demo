# Project rules for coding agents

Short and stable. If a rule here is wrong or missing, change this file in the same pull request.

1. **Context first.** Before you write code, read `docs/architecture.md` and every file in
   `docs/adr/`. Ignore `docs/adr/archive/` - those decisions are superseded.
2. **Money is integer cents** (ADR-001). No `float`, no `round()`, no `/` on amounts.
3. **Rules are data** (ADR-002). Thresholds, allowed values, percentages and prices belong in
   `data/rules.json`, never in Python code.
4. **Strict typing.** All code has type hints and passes `mypy --strict`. Use `dataclasses`.
5. **Tests are the gate.** Do not edit, delete or skip existing tests in `tests/` to make them
   pass. New behaviour needs new tests. Coverage must stay at 100 %.
6. **Verification loop.** Before you say a task is done, run

   ```
   python scripts/verify.py
   ```

   If a gate is red, read the output, fix the cause and run it again until all gates are green.
7. **Off limits.** Do not touch `.githooks/`, `.github/`, `azure-pipelines.yml` or
   `scripts/scan_sensitive.py` unless the task says so. Never commit with `--no-verify`.
8. **No new dependencies** without asking. If you believe one is needed, stop and explain why.
9. **Stop and ask** when the task contradicts an ADR or the specification leaves a question open.
   Do not fill the gap with a guess.
