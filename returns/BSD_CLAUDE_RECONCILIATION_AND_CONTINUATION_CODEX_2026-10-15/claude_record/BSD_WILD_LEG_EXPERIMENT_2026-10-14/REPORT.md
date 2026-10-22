# Wild-leg experiment — REPORT

Claude (Opus 5.5), 2026-10-14. Bounded discovery experiment on rank-2 controls with a1 = 0; a few CPU-minutes.
No pushes, messages or paid compute. **Endpoint effect: none. FIN, ORDER9 and Q36 are unchanged.**

## Verdict: THE p-ADIC DIRECTION IS PART OF THE SAME FORM, WITH LOCAL FACTOR (a_p - 1)^2

Wild direction: W = (1+pZ)/(1+p^2 Z) inside (Z/p^2)^x, the first layer of the cyclotomic Z_p-direction where p-adic
L-functions live. Wild height w(Q) = phi(-a/b mod p^2), the tame recipe mapped to W (exact mod p^2 because a1 = 0).

| stage | law tested | result |
|---|---|---|
| 1. sealed list (`PREDICTIONS_SEALED.md`, eb2e6d2d…) | factor F in {a_p-1, a_p-2, 1, 1-a_p, a_p}, sign +-1 | **all FAIL** (best 5/24 pure, 38/110 mixed) |
| 2. post-hoc, same data | F = (a_p-1)^2, from Mazur–Tate–Teitelbaum (theta_{p^2} on W = alpha^2 L_p, leading term x (1-1/alpha)^2) | 24/24 pure, 110/110 mixed (not evidence) |
| 3. sealed confirmation on FRESH rows (`confirm/RULE.md`, 8466b34d…) | the single law F = (a_p-1)^2, sign +1 | **98/98 pure (94 nonzero), 288/288 mixed (253 nonzero)** |

Confirmation rows: four curves never used before (571b1, 681c1, 707a1, 709a1, Sha_an = 1) at p = 5..73, l <= 400, plus new
rows on 389a1, 664a1, 655a1 (p = 37..73, or l in (400,600]). Per curve every row matched. Structural checks: augmentation 0
and first-order terms 0 at 386/386 rows; the forced wild-squared coefficient at level l p^2 equals (a_l-2) * c2w(p^2) at
288/288. Both polarization identities hold for the wild heights, so w is a quadratic form, as the recipe needs.

Laws now confirmed on controls (level M; the factor depends only on the legs in M):
- tame leg l:  (a_l - 2) = -#E(F_l) = -(1 - alpha_l)(1 - beta_l)   (mod l-1)    [10-07, two-leg]
- wild leg p:  (a_p - 1)^2 = (1 - alpha_p)^2                            (mod p)     [this report]
- leading term at level M = (product of leg factors) * K_E * det(universal height pairing on the M-kernel lattice).

## What this shows
- The p-adic class at p (wild direction) and the tame classes at auxiliary l = 1 mod p are ONE form: the mixed term
  couples them bilinearly through the same K_E and the same pairing. Within one prime p, reopener 3 holds numerically.
- Each kind of leg pays a different local factor. Tame legs see both Frobenius eigenvalues once; the p-adic leg sees the
  unit root twice. Over a function field, the constant-field direction is unramified and pays no factor; over Q no
  direction is unramified (Minkowski), so every finite direction pays a factor at its ramified place.
- Still true (two-leg report): no finite-level identity couples p to p' != p. The cross-prime link must be global.

## Limits
Controls only; a1 = 0 models only (the sigma-function's t^2 term is a1/2); ordinary non-anomalous p; mod p only (depth 1).
The squared factor was found after the sealed list failed; it then passed a fresh sealed test. Same-session work.
