# SUPERSINGULAR LANE: freeze addendum, 2026-09-22

This addendum is additive. `ORDINARY_LANE_FREEZE.md` is unchanged (sha `5ee2cd0f…`) and remains the canonical ordinary
record. The addendum supersedes only the rows in that file that list the supersingular primes as open (§2
"supersingular analogue A3: OPEN" and §4 "supersingular … A3, OPEN").

Promotion was authorized by the user on the condition that a Lean replay of the bridge's algebraic core builds without
`sorry`. It built clean.

---

## 1. Status: `A3 = CONDITIONAL_FORWARD_BRIDGE_PROVED`

    for all p >= 5,  p ∤ 7N,  E supersingular at p :
        M_2(p) != 0   ==>   Sha(E/Q)[p^inf] = 0,

        M_2(p) = Σ_{j=0}^{p-1} j^2 · ψ̄_f(γ^j P_1)      (P_1 = BLV's traced conductor-p^2 Gross point)

This holds prime by prime: `M_2(p)` is a different object at each `p`. For the same primes, `M_0(p) = M_1(p) = 0`
unconditionally, and `b̄_2 = +M_2/2`, where `b_2` is the `T²` coefficient of BLV's primitive minus square-root
series. So `ord_T(F⁻ mod p) = 2 ⟺ M_2(p) ≠ 0`.

## 2. One forward architecture for every good prime

    for all good p >= 5 with p ∤ 7N (ordinary or supersingular):
        M_2(p) != 0   ==>   Sha(E/Q)[p^inf] = 0

* **Ordinary** (frozen lane): `c̄_2 = −M_2/2` given `M_1 = 0`. See run 1's Lean statement, and the erratum
  `~/BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_ERRATUM_2026-09-22.md` (`c̄_2 = c_{p−3}/2`).
* **Supersingular** (this addendum): `b̄_2 = +M_2/2`. The minus sign is used throughout, and it is non-exceptional for
  split and inert `p` alike.

## 3. Quantifier status, stated bluntly

    M2_NONVANISHING  =  OPEN AT EVERY PRIME          (quantifier level 0)
    NO PRIME WAS GAINED BY THIS BRIDGE.

What changed is narrower: the supersingular primes (23, 29, 131, 167, 281, … infinitely many, by Elkies) no longer
lack a forward theorem. FIN, ORDER9 and Q36 are unchanged: **OPEN**.

## 4. Grades

| component | grade | evidence |
|---|---|---|
| Algebraic core (bridge §§2–4): no finite torsion, balanced τ-ranks, `d ≥ 2`, `d = 2 ⇒ Ш^∨ = 0`, `b̄_1 = 0 ⇒ M_1 = 0` | **LEAN-VERIFIED**: Lean 4.32.2, Mathlib `905b9581…`; 0 errors, 0 warnings; axioms `propext, Classical.choice, Quot.sound` only | `~/BSD_A3_LEAN_CORE_2026-09-22/A3Core.lean` (sha `f7a3c861…`), `build6.log` (sha `07ec913c…`), `REPORT.md` |
| Arithmetic inputs (I1) control, (I2) exact length, (I3) τ-equivariant freeing-set presentation + base-layer eigenspace equality, (I4) `rank E(Q) = 2` | **SOURCE-CHECKED** against BLV arXiv 2306.17784v2 (local sha `b0e9c254…`); imported, not formalized | `~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_REVIEW_2026-09-22/REVIEW.md` §1 (sha `22b8c7eb…`) |
| Structural Λ-module facts (f.g. over ℤ_p when μ = 0; λ-rank; topological nilpotence; characteristic ideal at one point) | standard Iwasawa algebra; hypotheses in the Lean file | `REPORT.md` hypothesis ledger (S1–S4) |
| Modeling: τ-module ↔ ±-graded form | **partly Lean-verified**: `(F/uF)⁻ ≅ F⁻/u(F⁺)` is proved. Eigenspace exactness for the base-layer kernel and cokernel is standard and not formalized. | `REPORT.md` (M1) |
| Imports inside BLV | Thm 7.1 equality (Step 4 rests on Fouquet–Wan / BSTW / CCSS); Thm 5.2 (Iovita–Pollack; Burungale–Kobayashi–Ota). Published theorems, not read by the project. | `REVIEW.md` §5 |
| Retained seed inputs | `ρ̄_p` surjective for all `p ≥ 3` (Sage, computational grade); `rank E(Q) = 2` (project grade); Hyp 1.1 (6),(7) checks | `REVIEW.md` §1 |

The Lean replay also sharpened the statement:
* (I1) is used only as a τ-compatible surjection `X ↠ Sel(E/K)^∨`.
* (I3) is used only through its minus-part equality.
* The μ = 0 hypothesis is implied by finite `λ = d`.

## 5. Ordinary lane: `ORDINARY_SECOND_PROOF_AVAILABLE` (recorded, NOT substituted)

The bridge's §§2–4 argument contains nothing specific to supersingular primes. With `ε = ∅` it runs at ordinary `p`,
and it gives a second proof of the frozen ordinary bridge. That proof bypasses:
* BD derived heights 2.18/2.23/Lemma 3.1,
* the Cassels–Tate shortcut,
* the `D = −7` certificate.

The frozen ordinary proof stays the canonical route. The second proof is recorded only, not substituted.

## 6. Frontier after this addendum

| primes | forward bridge | status of `Sha(E/Q)[p^∞] = 0` |
|---|---|---|
| good ordinary `p ≥ 5`, `p ∤ 7N` | frozen ordinary lane | conditional on `M_2(p) ≠ 0` |
| good supersingular `p ≥ 5`, `p ∤ 7N` | **this addendum** | conditional on `M_2(p) ≠ 0` |
| `2, 3, 5, 7, 11, 13` | fixed-prime certificates | per canonical ledger: `0, (Z/3)², 0, 0, 0, 0` |
| `2243, 4547, 5843` | none (bad; outside BLV) | **UNCOVERED** |

The remaining gaps are:
* the uniform nonvanishing `M_2(p) ≠ 0`, open at every prime;
* the three bad primes;
* the real leading-term comparison.

## 7. Provenance

* **Bridge:** written by a separate session (`~/BSD_SUPERSINGULAR_SIGNED_BRIDGE_2026-09-22/`, sha `ed44d90d…`).
* **Source review and Lean replay:** this session.
* **Status:** nothing sealed was edited. No novelty claim, and no FIN or BSD claim.
