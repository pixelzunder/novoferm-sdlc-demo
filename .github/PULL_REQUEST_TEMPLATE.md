## Description
<!-- Written by a human: which user problem does this solve, and how does it fit the larger goal? -->

## Agentic generation context
<!-- Fill in when a significant part of the change was generated. -->
- **Agents and models used:**
- **Intent and key decisions:** <!-- the intent and the decisions, not a prompt transcript -->
- **Specification / intent card:** <!-- link -->

## Verification and accountability
- [ ] **Accountability:** I have read this change and take full responsibility for how it behaves in production.
- [ ] **Architecture:** The change follows `docs/architecture.md` and the ADRs. Changed decisions are updated in this PR.
- [ ] **Context boundaries:** No personal data, database dumps or secrets were given to the agent or are part of this change.
- [ ] **Dependencies:** Every new dependency exists in the official registry and was checked by a human.
- [ ] **Tests:** `python scripts/verify.py` is green; new behaviour has new tests.
- [ ] **Evidence:** Output, screenshot or demo that shows the feature working is attached below.

## Reviewer focus
<!-- Not formatting - the gates do that. -->
1. Does the change do what the stated intent says?
2. Are module boundaries respected, or does it couple things that should stay apart?
3. How could this pass every gate and still be wrong? (edge cases, money, concurrency, privacy)
