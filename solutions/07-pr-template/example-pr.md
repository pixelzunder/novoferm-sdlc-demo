## Description
Sales needs a quote with line items, VAT and gross total to show to customers. Until now the
configurator only returned a net price. This adds `build_quote`; output formatting follows in a
separate change.

## Agentic generation context
- **Agents and models used:** coding agent in the IDE, one session
- **Intent and key decisions:** implement `exercises/04-harness/quote-spec.md` exactly. The
  drive is listed even at 0 so that the customer sees it is included. VAT is rounded once on
  the net total, not per line item, so the items always add up to the net total.
- **Specification / intent card:** `exercises/04-harness/quote-spec.md`

## Verification and accountability
- [x] **Accountability:** I have read this change and take full responsibility for how it behaves in production.
- [x] **Architecture:** `quote.py` depends on `pricing` and `rules` only; no ADR changed.
- [x] **Context boundaries:** no customer data or secrets were used.
- [x] **Dependencies:** none added.
- [x] **Tests:** `python scripts/verify.py` green, six new tests.
- [x] **Evidence:** base door 2500 x 2125 mm, smooth, standard drive: net 944.00, VAT 179.36, gross 1 123.36 EUR.

## Reviewer focus
1. Is rounding VAT once on the net total what finance expects?
2. `quote.py` reuses `panel_price_cents` - is that the right dependency direction?
3. Could two options with the same name appear? (No: options are a set.)
