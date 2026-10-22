# Sealed predictions, extra (p, l) pairs (Claude, 2026-10-06)

Written after extra_rows.gp (regulators) and BEFORE any c2 mod 5 or mod 3 was computed from the symbol tables.
Law under test: c2 == (a_l - 2) * 288 * R(p,l) (mod p), g = least primitive root mod l (the same g as the run).

| p | l | a_l | g | R(p,l) | predicted c2 mod p |
|---|---|---|---|---|---|
| 5 | 191 | -10 | 19 | 1 | 4 |
| 5 | 311 | 16 | 17 | 3 | 1 |
| 3 | 103 | -2 | 5 | 2 | 0 |

(3, 283) is not admissible: 3 | #E(F_283) = 288. Custodian-attested ordering only (same session).
