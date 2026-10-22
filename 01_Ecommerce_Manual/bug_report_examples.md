# Illustrative Bug Reports (NOT confirmed defects)

## DEMO-BUG-001 — Cart badge not updated after removing an item
- **Severity:** Minor | **Priority:** Medium
- **Precondition:** User is signed in and has one product in cart.
- **Steps:** Open cart; remove the product; check header cart badge.
- **Expected:** Badge shows 0 or disappears.
- **Hypothetical actual:** Badge continues to show 1.
- **Status:** Fictional demonstration; NOT discovered or reproduced.

## DEMO-BUG-002 — Checkout accepts whitespace-only first name
- **Severity:** Major | **Priority:** Medium
- **Steps:** Reach checkout; input spaces for first name; complete other fields; submit.
- **Expected:** Input rejected with useful validation.
- **Hypothetical actual:** Submission proceeds.
- **Status:** Fictional demonstration; NOT discovered or reproduced.
