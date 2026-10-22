# ASSUMPTIONS — A2: every hypothesis, tagged

Tags: **FORMAL_ASSUMPTION** · **PROVED_IN_PACKAGE** · **IMPORTED_ARITHMETIC_THEOREM** · **NOT_PART_OF_THIS_TASK**.

Almost every A2 target is unconditional pure mathematics: group theory or elementary number theory. The hypotheses inside
targets are ordinary mathematical premises of the abstract statements. The table records how each premise would be supplied
when the abstract statement is applied to the elliptic curve, which package A2 never does.

| target | premise | tag (when applied to the curve) | justification / source |
|---|---|---|---|
| P1–P5, H0 | `AddMonoid.IsTorsion G` | IMPORTED_ARITHMETIC_THEOREM | Sha is torsion (standard) |
| P3, P4 | zero primary parts outside a finite set | NOT_PART_OF_THIS_TASK | for Sha this is WC (2), whose antecedent J_E ≠ 0 is OPEN; see package A1 |
| P3, P4 | finite primary parts on the finite set | NOT_PART_OF_THIS_TASK | WC (1) for good p (A1); the exceptional primes 2243, 4547, 5843 are OPEN (Codex) |
| J1–J4 | `∀ p ∈ P, p.Prime` | FORMAL_ASSUMPTION | P is a set of primes (Codex's P) |
| J2–J4, L7 | depth function h and its finiteness | NOT_PART_OF_THIS_TASK | h = Codex's h_p, computed from Ota witnesses (package A1); its finiteness/boundedness IS the open antecedent |
| L7 | lattice vector z ≠ 0 with depth ≤ v_p(content z) outside B | NOT_PART_OF_THIS_TASK | Codex WC §4: "the missing input is the comparison with that primitive integral lattice". Never to be constructed here |
| H2 | \|G[2^∞]\| = 1, \|G[3^∞]\| = 9, \|G[5^∞]\| = 1 | IMPORTED_ARITHMETIC_THEOREM | retained seed theorems: Sha[2^∞] = 0; Sha[3^∞] ≅ (Z/3)² (relative to Skinner, R1/R2 carried); Sha[5^∞] = 0 (sealed) |
| H2 | odd-primary orders are squares | IMPORTED_ARITHMETIC_THEOREM (Cassels–Tate) | for finite Sha, the Cassels–Tate pairing is nondegenerate and alternating (for elliptic curves), so each primary order is a square. The abstract step "alternating nondegenerate pairing into a cyclic group ⇒ square order" is stretch S1 (PROVED_IN_PACKAGE if achieved) |
| H2 | `[Finite G]` | NOT_PART_OF_THIS_TASK | this is FIN itself, and H2 is a statement *under* FIN. Codex: "FIN alone does not determine the order" |
| B1, B2, CM3 | valuation data v p | FORMAL_ASSUMPTION | valuation model of d ∈ ∏ Z_p: d_p Z_p = p^{v_p(d_p)} Z_p (exact) |
| S1 | pairing into ZMod N | FORMAL_ASSUMPTION | Cassels–Tate takes values in ℚ/ℤ; on a finite group of exponent N its image lies in (1/N)ℤ/ℤ ≅ ZMod N |

## Hostile checks passed
- **No hidden J_E ≠ 0.** J-targets characterise when J is nonzero; none asserts it for a specific h.
- **No hidden FIN.** H2 has `[Finite G]` as an explicit premise, and its conclusion is only 9t², which CM4 shows cannot be
  improved to 9.
- **Finite support and local finiteness are separate.**
  - P5 states that both are needed.
  - CM1 shows that local finiteness alone fails.
  - CM1′ shows that finite support alone fails.
  - CM2 and CM3 show that nonzero or finite local data do not give finite support.
- **No LINE, GPR, ETNC, BSD, FIN or FORMULA** input.
