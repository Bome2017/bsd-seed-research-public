# Second addendum — the explicit eta-character attempt

**Tier: EXPLORATORY CONVENTIONAL PROOF ATTEMPT.** Not a proof of the H41 seed, not a certification,
not a formalization, not a novelty claim. Neither
`CODEX_H41_SEED_RESEARCH_FREEZE_001` (`ac82f3ad…`) nor
`H41_SEED_FREEZE_ADDENDUM_001` (`82b6730f…`) is reopened or modified by this object.

## 1. What is carried

`01_attempt/` holds the operator's attempt byte-identically:

    h41_eta_character_attempt.zip
        sha256 7b2c4be30114edc65b2d25931c49cc7f9cc13e21cab40a86c4debf73547feafe
    PROOF_ATTEMPT.md          the construction, its scope, and the unproved comparison
    check_eta_candidate.py    the symbolic and direct-sum checker
    exact_checks.json         its recorded output

The document labels its own status in its first three lines and states the unproved comparison and
the untreated `a = 1` case explicitly. That labelling is carried unaltered and is not softened here.

## 2. The construction

For `p = 2^n − 1` a Mersenne prime with `n ≥ 5` and `N = 2p`:

    f_p(z) = η(z)^(2p−1) · η(2z)^(2−p) · η(pz)^(p−2) · η(2pz)^(1−2p)

a weight-zero modular unit on `Γ₀(N)` with trivial character, whose divisor is

    div(f_p) = ((p²−1)/8)·([0] − [∞])

Because every divisor order is even, `√f_p` gives an unbranched double cover; its monodromy is an
`F₂`-character `χ_p` on integral homology. With `γ_p = [[(2p+1)/3, 1],[2p, 3]] ∈ Γ₀(N)` sending
`0 ↦ 1/3`, the logarithmic eta law gives

    (log f_p(γ_p z) − log f_p(z)) / 2πi  =  −(p−1)(p+3)/12  =  −(4j+1)(12j+5)   for p = 24j+7

which is odd, hence `χ_p({0,1/3}) = 1` in `F₂`.

## 3. Independent audit — 18 checks, 18 PASS

`receipts/verify_eta_attempt.py`, output in `receipts/VERIFICATION_OUTPUT.txt`. Every formula was
re-derived rather than read; exact arithmetic throughout, no floating point.

| Checked | Result |
|---|---|
| `Σ r_d = 0`, `Σ d·r_d = −3(p²−1)`, `Σ (N/d)·r_d = +3(p²−1)` | confirmed symbolically |
| `∏ d^{r_d} = 2^(3−3p)·p^(−p−1)`, both exponents even → rational square | confirmed |
| The `divisor_matrix` **is** the Ligozat cusp-order formula | confirmed against an independent implementation, at all four cusps |
| `div(f_p) = ((p²−1)/8)([0]−[∞])`, intermediate cusps vanish | confirmed |
| `γ_δ = [[A, δ],[N/δ, 3]]` has `det = 3A − N = 1` for every `δ ∣ N` | confirmed |
| `s(1,3) = 1/18`, `s(2,3) = −1/18` | confirmed by direct summation |
| The reciprocity closed forms for `s(3,p)`, `s(3,2p)` | confirmed against direct sums at `p = 31, 127` |
| The winding `−(p−1)(p+3)/12` from Apostol's logarithmic law | reproduced at `p = 31, 127, 8191`: `−85, −1365, −5592405`, all odd |
| `(p−1)(p+3)/12 = (4j+1)(12j+5)` for `p = 24j+7` | confirmed symbolically |
| `p ≡ 7 mod 24` and `p ≡ 1 mod 3` at every admissible `n` | confirmed |
| `(p²−1)/16` integral, so `div(f_p) = 2D` | confirmed |

`receipts/THEIR_CHECKER_REPLAY.txt` records that the attempt's own checker runs in isolation and
reproduces its shipped `exact_checks.json` **byte-identically** (`78ef5c2a…`).

Two observations from the audit, neither a defect:

* The `p ≡ 1 mod 3` condition is load-bearing twice over — it is what makes `A = (2p+1)/3` an integer,
  and it is what reduces `s(3,p)`, `s(3,2p)` to `s(1,3)` and `s(2,3)` by reciprocity. The two uses are
  independent and both are needed.
* The checker's `dedekind(h,c)` helper maps `hj ≡ 0 mod c` to `−1/2` rather than `0`. For coprime
  `(h,c)` and `1 ≤ j < c`, `c ∣ hj` forces `c ∣ j`, which cannot happen — so the branch is unreachable
  for any legitimate argument. Recorded only because a reader inspecting the helper alone would notice.

## 4. The geometric step, which the document flags for scrutiny

`PROOF_ATTEMPT.md` says the geometric/logarithmic interpretation "should receive independent scrutiny
before being promoted." On this specific point the audit is affirmative, with a reason:

`f_p` has no zeros or poles in `ℍ` — its divisor is supported at the cusps — and `ℍ` is simply
connected, so `log f_p` is single-valued there and the winding `W` is path-independent. Continuing
`√f_p` from `z` to `γ_p z` multiplies it by `exp(πiW) = (−1)^W`, while `f_p(γ_p z) = f_p(z)` by
invariance. The monodromy sign is therefore exactly the parity of `W`.

This is why the document's insistence on the **logarithmic** law with a fixed *q*-product branch,
rather than the multiplicative law, is the correct instinct: the multiplicative law genuinely would not
license the half-exponent, and the logarithmic one does.

## 5. The divisor degree is not a new number

    (p²−1)/8 = (p−1)(p+1)/8 = (p−1)·2^(n−3)        since p + 1 = 2^n exactly

giving `120, 2016, 8386560, 2147450880, 34359607296, 576460751766552576` at
`n = 5, 7, 13, 17, 19, 31` — the orders of the cusp class `[0]−[∞]` in `J₀(N)` already verified in
`CODEX_H41_SEED_RESEARCH_FREEZE_001`, with `v₂ = n − 2 = m`, reproducing the "2-exponent = m" result.

This is forced, not lucky: a modular unit with that divisor must have degree equal to the order of the
cusp class. Its value is as corroboration that the linear system was solved onto the already-audited
arithmetic rather than beside it.

## 6. A reduction of the unproved comparison, using rank one

Since `v₂((p²−1)/8) = m ≥ 3`, the degree is divisible by 8, so `div(f_p) = 2D` with

    D = ((p²−1)/16)·([0] − [∞])

integral, and the unbranched double cover is the one cut out by the 2-torsion class

    T_p = ((p²−1)/16)·([0] − [∞])  ∈  J₀(N)[2]

Now use the frozen return's own result that `U₀` is **free of rank one**. Then `U₀/2U₀ ≅ F₂`, and
`Hom(U₀/2U₀, F₂)` has exactly one nonzero element. So if `χ_p` factors through `U₀/2U₀` at all, it
**is** `α_p mod 2` — no other nonzero character exists to be. The unproved comparison therefore reduces
from an equality of characters on a full integral generating set to the single containment

    ker( H₁(X₀(N),ℤ) → U₀/2U₀ )  ⊆  ker χ_p

with nonvanishing already supplied by `χ_p({0,1/3}) = 1`.

**This is a reduction in shape, not a claim of progress on difficulty.** Proving that containment for
symbolic `p = 2^n − 1` may be exactly as hard as the original comparison. It does sharpen the proposed
`N = 62, 254` experiment: compute `ker(H₁ → U₀/2U₀)` and test whether pairing against `T_p` kills it —
one-sided, on integral data already available, and a failure kills the identification at the smallest
level.

## 7. What remains unproved — unchanged

    the identification  alpha_p mod 2 = chi_p       NOT ESTABLISHED
    the a = 1 case, target w_3 = 2 mod 4            NOT ADDRESSED; mod 2 cannot reach it
    the negative-branch seed, w_3/2^a odd           OPEN
    the positive branch                             OPEN, with additional period/numerator ambiguity

The construction side is verified. The identification is not. **The H41 seed remains unproved**, and
nothing in this object moves it. No prerequisite here is a gate, no new bottleneck is claimed, and no
model run is authorised.
