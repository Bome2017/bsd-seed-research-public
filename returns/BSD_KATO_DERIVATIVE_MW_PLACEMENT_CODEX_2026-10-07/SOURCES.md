# Sources and reading boundary

## Retained proof inputs read in this pass

- Lab commit **d4d86454eedd7e3be2c0b398f4a8210fa4abc4a3**:
  BSD_BKS_COMBINATION_LEDGER_CODEX_2026-10-07/WEAK_ORDER_PROOF.md,
  especially §§2–4, and its ASSUMPTIONS.json and TAME_COMPARISON.md.
  These provide the precise conditional rank implication and retained
  seed/lattice scope, not a nonvanishing theorem.
- Lab commit **54637ae16c1856d065b8dada5aeab7c7ac33ced6**:
  BSD_BKS_FOUNDATION_AUDIT_CODEX_2026-10-07/FOUNDATION_CHECK.md,
  REPORT.md and SOURCES.md. These keep the transport, control and
  local-factor checks at author-audited written-proof grade.

Copies are bound in INPUT_BINDINGS.json. The two preceding complete ZIPs
are retained as context so their assumptions and historical reservations
remain available. No old sealed file has been edited.

## Primary sources checked for the new deduction

- J. S. Milne, *Elliptic Curves*, second edition,
  [author PDF](https://www.jmilne.org/math/Books/EC2.pdf), Chapter IV:
  equation (28), printed p.112, and the compatible finite Kummer diagrams,
  printed p.129. These are PDF pages 116 and 133, zero-based. The online
  text of both passages was read. The finite-level injections and natural
  transition maps are used; no Sha-finiteness assertion is imported.
- D. Loeffler and S. L. Zerbes, *Euler systems with local conditions*,
  [author manuscript](https://discovery.ucl.ac.uk/10067153/1/1710.04956v2.pdf),
  introduction, printed p.1: integral Kummer inclusion into H¹(K,T_pE).
  Its displayed Euler-characteristic calculation in the proof of
  Proposition 2.8 is already part of the retained weak-order argument.

The case split and saturation proof are written in PROOF.md. They do not
require a new deep theorem, a numerical seed computation or a claim that
the complete cohomology space is always Mordell–Weil.

## Limits

No exhaustive literature/novelty search, independent human review or Lean
formalization was performed. A bounded search of the immediate preceding
return found the explicit unresolved-placement statements addressed here;
this is not a claim that no older dossier contains a related observation.
The retained residual image and saturated basis were not recertified.
