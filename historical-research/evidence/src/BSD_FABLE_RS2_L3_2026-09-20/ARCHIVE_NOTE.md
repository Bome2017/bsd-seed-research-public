# RS2 — CANONICAL ARCHIVE NOTE

Date 2026-09-20. This file is the canonical archive record of the C-RS2 thread. It is **additive**: no file in this or any
predecessor folder was edited. Where it conflicts with wording in `RS2_L3_VERDICT.md`, **this file governs**.

    RS2 = OPERATIONALLY ARCHIVED.      FORMULA ENDPOINT EFFECT = NONE.
    No successor. No arithmeticity follow-up. No renamed continuation.

## Correction 1 — the negative result is procedural, not a theorem

`RS2_L3_VERDICT.md` §6 and §7 are **too strong where they read as a nonexistence claim.** In particular the sentence
"the terminal object is an Estermann-class special value ... The route was run to the end and did not escape it" is
withdrawn as stated. **Task 3 was never closed**, so nothing here proves that RS2 cannot escape.

The strongest justified statement is:

> **No independently identified arithmetic successor survives the admission test.**

Supporting fact, and its exact limit: the coefficient construction that L3 exhibits consists of `sigma^{(N)}` divisor sums
and their derivatives, `Gamma`/`zeta` values and derivatives, `K`-Bessel and Whittaker terms, and sparse shifted
convolutions — and **no regulator, height, Heegner, or Beilinson object was identified in it**. That is a statement about
what was found, not about what exists. It is sufficient to trigger the procedural hard stop that governs this thread; it is
**not** a nonexistence theorem for some unknown future identity.

## Correction 2 — provenance grade on `kappa~_N`

The thread never obtained **Iwaniec, *Spectral Methods of Automorphic Forms*, (3.21)-(3.22)**. The cross-cusp normalization
`Y_{ba}(n,t) = zeta(2t) n^{t-1} Z_{ba}(n,t)` was reconstructed from the ANT conventions ((2-5), (4-2), (4-3)) together with
the double-coset and scaling-matrix calculation done here; the original normalization source was not independently replayed.
Accordingly:

    < A~_2, f > = kappa~_N L(f,2) L''(f,1),
    kappa~_N = - prod_{p || N} (1 - a_p/p) / [ 2 (2 pi)^3 prod_{p|N} (1 - p^{-2}) ]

is graded **WRITTEN DERIVATION WITH ONE SOURCE-CUSTODY SEAM** — not source-closed. The seam is a normalization, not a sign
(the sign was independently resolved), and it cannot affect the order of vanishing or the non-vanishing of `kappa~_N`; it
could change `kappa~_N` by an explicit non-zero rational factor.

## The durable record

**Established:**
1. The original rejection premise — "the Laurent coefficient `E^(2)` has no motivic meaning, therefore reject" — is **wrong**,
   refuted by the rank-one control argument, not merely doubted.
2. For this seed the **diagonal cusps `{infinity, 0}` are genuinely annihilated**: `p^2 | N` gives the Ramanujan sums and
   `a_n(f)` complementary support, forcing `C_N == 0`, and no archimedean regularization can reach it.
3. The **cross-cusp construction repairs exactly that**, with all five bad-prime local factors explicit and non-zero.
4. The **bad-Euler normalization `D_N`** removes the artificial five-pole phenomenon identically and eliminates the
   `prod_{p|N} log p` artefact, which was a normalization effect and not intrinsic.
5. Two exact local facts for this seed: the diagonal annihilation in (2), and the sparsity modulus
   **`18188 = 2^2 * 4547`** from `v_p(l) >= v_p(N) - 1` (strictly stronger than the `p^2`-only bound `9094`).
6. The constructive Fourier side lands in the shifted-convolution class, in which **no characteristic-zero BSD bridge was
   identified** — see Correction 1 for the exact force of this.

**Open and left open:** Task 3 — a weight-2, level-N, progression-restricted shifted-divisor continuation theorem. Not
obstructed, not proved, not pursued.

## Standing instruction

Nothing further on RS2. Do not open a successor under this or any other name. A future session that believes it has a reason
to reopen should read §7 of `RS2_L3_VERDICT.md` and Correction 1 above first, and should note that reopening requires a *new
arithmetic object identified independently* — not another analytic lemma.
