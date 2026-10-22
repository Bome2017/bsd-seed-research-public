# Delta task: the rank-two global anchor (2026-10-06)

This project contains the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (root files and folders). Read `CURRENT_FRONTIER.md` first. **This file governs the run.** Every rule in the root `TASK.md` "Do not" list applies here.

## The one question

**Find or rule out an independent rank-two global identity sufficient for G1.**

In rank one, the exact global constant comes from three pieces. The seed has the first two; the third is missing.

| Piece | Rank one (OpenAI Result 002 §5; Gross–Zagier) | Seed (rank two) |
|---|---|---|
| (i) Tame factorization ("cup comparison") | tame derivative = (2 − a)·(Kato coordinate)·(tame height) | **Proved:** Theorem W + BKS factorization C₂(p,ℓ) ≡ (a_ℓ − 2)·s_p·R_{p,ℓ} (mod p), with s_p independent of ℓ |
| (ii) Nondegenerate auxiliaries (biextension + Chebotarev) | the "nonzero height direction" lemma | **Proved:** G2 |
| (iii) Global anchor ("spectral-height identity" + archimedean Gross–Zagier) | tame derivative of the theta element = (constant)·(tame height of a Heegner point), and the Heegner point's real height gives L′(E,1) | **Missing.** This is the target. |

A replacement for (iii) must yield, for all p outside a finite set, the congruence C₂(p,ℓ) ≡ m·(a_ℓ − 2)·R_{p,ℓ} (mod p), or a residue-level law. It must come from a characteristic-zero object, and m ∈ ℚ^× must be defined without FIN, finiteness of Ш, Q36 or BSD.

## Boundary facts any answer must respect

- **Heegner setting (ε(E/K) = −1).** L(f⊗ε_K, 1) = 0 for the seed, and the Heegner point is torsion because ord L(E/K) ≥ 3. The rank-one spectral identity reads 0 = 0 at every tame order.
  - Its first nonvanishing derivative is L‴(E/K,1) = 3·L″(E,1)·L′(E^K,1).
  - So a geometric identity in this setting must see L″(E,1).
- **Definite setting (ε(E/K) = +1).** Example: K = ℚ(√−7), with E^{−7} of rank 0 and rank E(K) = 2.
  - There are no Heegner points; the Gross-point theta element exists.
  - Its depth-two term is on record only as a per-prime criterion: M₂(p) ≠ 0 ⇒ Ш[p^∞] = 0.
- **Higher Gross–Zagier** (Yun–Zhang) is known over function fields only.
- **Plectic points** and the record's candidates K1–K11 are missing constructions.
- **Tan 1995** gives the comparison only by assuming BSD over every intermediate field, and only up to an F_p^× constant.
- **No characteristic-zero map can read m off the degree-two Mazur–Tate class.** That class lies in a finite group at every level, so any characteristic-zero map from it is zero (`3_LIVE_QUESTION/ADMISSION.md`).

## Acceptable returns (exactly one)

- **`RANK2_IDENTITY`.** An explicit identity replacing (iii): its statement, and a proof or a reduction to published theorems with exact theorem numbers. m must be defined without FIN, Ш, Q36 or BSD, and it must pass the 7-step admission test in the canonical `TASK.md`.
- **`RANK2_REDUCTION`.** A reduction of G1 to a precisely stated identity that is strictly weaker than G1. Show that it is not equivalent to FIN-tail, and that it is a residue-level statement rather than a zero-pattern one (canonical `STATUS.md` §4).
- **`PRECISE_OBSTRUCTION`.** For each construction tried: the first failing step and the input that would change it. Then stop.

## Do not (in addition to the canonical list)

- Do any W3 work, or transplant OpenAI Result 002 beyond reading its §5 spectral identity as the rank-one model.
- Run any per-prime computation.
- Survey the literature without a specific candidate identity to test.

## Return format

The same as the canonical `TASK.md`:
- one STATUS line;
- every claim labelled PROVED, IMPORTED or HEURISTIC;
- Lean with no `sorry`, plus `#print axioms` for every new theorem;
- end with "FIN, ORDER9 and Q36: unchanged" or a precise statement of what changed.
