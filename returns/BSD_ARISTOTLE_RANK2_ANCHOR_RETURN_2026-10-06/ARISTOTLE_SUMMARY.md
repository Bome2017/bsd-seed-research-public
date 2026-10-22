# Summary of changes for run 119f14f9-6a7e-41c5-80b1-83559350e618
**STATUS: PRECISE_OBSTRUCTION.** I found no independent rank-two global identity that replaces the rank-one Gross–Zagier anchor and gives C₂(p,ℓ) ≡ m·(a_ℓ − 2)·R(p,ℓ) mod p with one rational m defined without FIN, Ш finiteness, Q36 or BSD. I also found no strictly weaker reduction. Per the delta task, I stopped after naming the first failure of each construction tried. The full return, with every claim labelled PROVED, IMPORTED or HEURISTIC, is in `BSD_ARISTOTLE_DELTA_RANK2_ANCHOR_2026-10-06/RESULT_RANK2_ANCHOR.md`.

**Why the rank-one anchor degenerates (PROVED in Lean, with the orders of vanishing as explicit hypotheses).** Write L(E/K,s) = L(E,s)·L(E^K,s), with L(E,s) vanishing to order 2 and L(E^K,s) to order at least 1. Then:
- the value and the first two derivatives of L(E/K,s) at s = 1 are zero;
- the third derivative is 3·L″(E,1)·L′(E^K,1);
- any identity of the form c·(height) = first derivative, with c ≠ 0, forces the height to be zero, so the Heegner point is torsion;
- a family of identities carrying a fixed factor equal to 0 says exactly the same thing whatever the unknown is. This is the exact form of "0 = 0 at every tame order".

**Constructions tested, with first failing admission step and the input that would change it:**
- **R1, higher-order Heegner identity over K.** Fails at step 3: the only known identity is first order and reads 0 = 0. It would take a number-field higher Gross–Zagier formula for the third derivative of L(E/K,s).
- **R2, Gross–Zagier for the twist E^K, then divide.** Fails at step 3 in two ways:
  - Dividing only moves the problem back to R1.
  - The twist's anchor lies in the (−1)-part under Gal(K/ℚ), while C₂ and (a_ℓ − 2)·R lie in the (+1)-part. I proved in Lean that no equivariant map carries one to the other when p is odd.
- **R3, Heegner points twisted by nontrivial ring-class characters.** These are genuine rank-one anchors, but they fail at step 3:
  - Their tame variable comes from ring-class fields over K, not from Gal(ℚ(μ_ℓ)/ℚ).
  - The only part that sees E itself is the Heegner point over K, which is torsion.
  - The conjectural leading term in the literature is normalized by #Ш (HEURISTIC).
- **R4, Gross-point theta element in the definite case.** Fails at step 3: Gross's formula reads 0 = 0 at the trivial character, and the degree-two term has no rational-valued version. It also has no Mordell–Weil side, so step 4 would fail too.
- **R5, a limit of rank-one anchors as the character tends to trivial.** Fails at step 1: characters of order p exist only after p is fixed, and in characteristic zero there is no derivative at the trivial character.

**The common obstruction.** Any replacement for the anchor must evaluate L″(E,1), or a fixed nonzero multiple of it, against a 2×2 height determinant, with an exact constant and no p in its definition. That is a number-field rank-two Gross–Zagier formula, which is known over function fields only (IMPORTED from the record). By the record's own result (G2 + Theorem W + Ota), any such identity would imply that Ш has finite support for the seed (IMPORTED). As far as I know, Ш finiteness is not proved for any elliptic curve over ℚ of analytic rank 2 or more (HEURISTIC).

On calibration, I checked in Lean that 4·c∞·Tam·#Ш/tors² = 4·c∞·(#Ш·Tam/tors²), and that 4·2·16·9/2² = 288 = 8·36. Under BSD this means any general Ш-free m would have to equal 4·c∞·q (HEURISTIC).

**Lean.** The file is `Rank2Anchor/Obstruction.lean`. It builds with no `sorry` and makes no claim about Ш of the seed. `#print axioms` results:
- `Rank2Anchor.leibniz`, `Rank2Anchor.ProductOrder.low_derivs_vanish`, `Rank2Anchor.ProductOrder.third_deriv`, `Rank2Anchor.ProductOrder.first_order_anchor_height_zero` and `Rank2Anchor.seed_calibration`: [propext, Classical.choice, Quot.sound]
- `Rank2Anchor.degenerate_identity_iff`: [Quot.sound]
- `Rank2Anchor.degenerate_identity_blind`: [propext, Quot.sound]
- `Rank2Anchor.equivariant_minus_to_plus_eq_zero` and `Rank2Anchor.equivariant_minus_to_trivial_eq_zero`: [propext]

**Project change.** Lake rejected the packet's original library entry in `lakefile.toml` (the hyphen in `2026-10-06` is not a valid module-name component). I commented it out with an explanation, left the packet's Lean files untouched, and made a new library, `Rank2Anchor`, the default target.

FIN, ORDER9 and Q36: unchanged.