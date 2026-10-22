# Executed admission of the small comparison model

Date: 2026-10-11. Status: **EXACT_MOD5_STURM_CM_RESIDUAL_ADMISSION_PASSED**.

This admits the residual arithmetic model for an experiment. It does not evaluate a CM localization map, construct the explicit torsion-module isomorphism, prove a mixed-place comparison, or settle any BSD obligation for the seed. The exact calculations below are computer-assisted using PARI/GP 2.17.3, with independent standard-library Python controls; they are not Lean/kernel certificates.

## 1. Actual curves

The curves are defined by the displayed integral a-invariants, regardless of any database label:

| Historical label | a-invariants | Conductor |
|---|---|---:|
| 2541c1 | [1,1,1,3,12] | 2541 = 3·7·11² |
| 287133c1 | [1,1,1,−1669982047,−25795561267816] | 2541·113 |
| 424347b1 | [1,1,1,1878418,−485198548] | 2541·167 |

The old partner-screen input supplies the models; the program binds its hash and extracts exactly the two named rows, then computes conductors again. At coefficient prime 5, the base has a₅=−3. The raised curves have a₁₁₃=+1 and a₁₆₇=+1 respectively; base traces are a₁₁₃=9 and a₁₆₇=−12. Hence a_ℓ≡ℓ+1 modulo 5 for both auxiliary primes, which are not ±1 modulo 5. In both cases the valuation at 5 of (ℓ+1)²−a_ℓ² is exactly one.

## 2. The full modular congruences were computed

Let f be the normalized weight-two form of the base and g_ℓ that of its proposed raised partner. Compare the actual integral cusp forms of common level 2541ℓ:

    h_ℓ(q) = f(q) − ℓ f(q^ℓ),       g_ℓ(q).

The degeneracy map V_ℓ takes f to f(q^ℓ). Thus h_ℓ is a genuine integral modular form, without pretending that its integer coefficient ℓ is an exact characteristic-zero unit root. Its modulo-5 form is the +1 stabilization because a_ℓ≡ℓ+1.

We computed **all** Fourier coefficients through the ordinary weight-two Sturm bound, including indices divisible by 5 and the bad primes:

| ℓ | Common level | [SL₂(Z):Γ₀(level)] | Bound floor(index/6) | Mod-5 differences nonzero |
|---:|---:|---:|---:|---:|
| 113 | 287133 | 481536 | 80256 | 0 |
| 167 | 424347 | 709632 | 118272 | 0 |

The constant coefficient is zero. Sturm's theorem therefore gives h_ℓ≡g_ℓ modulo 5 as modular forms. The level is not squarefree; the general congruence theorem is used, not a squarefree-newform shortcut.

The complete exact coefficient vectors are retained, compressed, with their uncompressed and compressed SHA-256 hashes in RESULT.json. A Python pass recomputes both full comparisons and both bounds from those vectors. Direct finite-field point counts, using the displayed equations rather than PARI arithmetic, independently match 274 prime coefficients below 500. These finite controls do not independently recompute every coefficient through the Sturm bounds.

Negative controls: comparing the unstabilized f with g fails first at index ℓ; replacing ℓ by 1 in the degeneracy term also fails there. The stabilization is mathematically material, not cosmetic.

By modularity, the Frobenius traces of the two mod-5 representations agree at every prime away from the relevant levels and 5. Their determinants both equal the cyclotomic character. Chebotarev and Brauer–Nesbitt identify their semisimplifications. The base representation is irreducible by §3, so the actual two-dimensional representations are isomorphic. This proves existence; it does not construct the isomorphism required for simultaneous local evaluation.

## 3. Full residual image, with an explicit small certificate

For E=2541c1, Δ=−3²·7²·11² and c₄=−143. At 3 this is multiplicative reduction with v₃(Δ)=2, prime to 5. Tate uniformization over the at-most-quadratic unramified splitting extension shows that inertia on E[5] contains a nontrivial transvection: the Tate parameter has valuation 2, so adjoining its fifth root is ramified of degree 5. Nonsplit multiplicative reduction changes Frobenius, not this inertia conclusion.

At 2, direct counting gives a₂=−1. Its characteristic polynomial X²+X+2 has discriminant −7≡3 modulo 5, a nonsquare. Thus no line can be invariant under the full image.

For completeness the last finite-group inference has an exhaustive exact control. Normalize a nontrivial transvection by conjugacy and a nonzero power to T=[[1,1],[0,1]]. Irreducibility supplies a conjugate U with a different fixed line, equivalently U₂₁≠0. The checker enumerates all 20 matrices U over F₅ with trace 2, determinant 1 and U₂₁≠0. Each pair (T,U) generates all 120 elements of SL₂(F₅). Hence the residual image contains SL₂(F₅). Its determinant is surjective by the Weil pairing and the cyclotomic character, giving GL₂(F₅). The two raised representations have the same image through §2.

## 4. A CM field satisfying this model's actual conditions

Choose K=Q(√−19). The exact splitting characters are:

| rational prime | 3 | 5 | 7 | 11 | 113 | 167 |
|---|---:|---:|---:|---:|---:|---:|
| (−19/q) | −1 | +1 | +1 | +1 | −1 | −1 |

Thus take N⁻=3, N⁺=7·11²=847. Exactly one of 3,7 is inert, all primes in N⁺ split, both auxiliary primes are inert, and 5 splits. The discriminant is prime to all relevant levels and 5. Reduced positive binary quadratic-form enumeration finds exactly [1,1,5], independently confirming h_K=1. This uses no copied K=Q(√−7), which would ramify at a base bad prime.

PARI's exact rank-bounds routine returns:

- E: [2,2,0,[[0,3],[7,17]]].
- E^(−19), model [−1,−24,19,1273,−84113], conductor 917301: [0,0,0,[]].
- E₁₁₃: [1,1,0,[[39736379971/293764,7496759272384463/159220088]]].
- E₁₆₇: [1,1,0,[[480,22723]]].

The rank bounds establish the twist's rank-zero premise by descent, not numerical L-value recognition. Saturation through bound 7 also returns the same two base points. This is sufficient for their 5-saturation within this calculation, not a freshly proved all-prime saturated basis. No analytic Sha value is used and no claim about Sha(E/K)[5] follows.

## 5. Exact precision boundary

At the good prime q=13, which is different from 5 and divides none of the levels,

    a₁₃(E)=−7,      a₁₃(E₁₁₃)=a₁₃(E₁₆₇)=−2.

Their difference is −5, nonzero modulo 25. Therefore neither particular raised curve's mod-25 representation is isomorphic to E[25]. This is an exact trace obstruction for these models, not merely a failure of the chosen integer stabilization. Both comparisons remain valid modulo 5. A higher-precision experiment must construct a different admitted object; it must not silently reuse these curves at modulus 25.

## 6. Sources and proof boundaries

- W. Stein, *Modular Forms: A Computational Approach*, §9.4, Theorem 9.18 and Corollary 9.20 (PDF pages 184 and 187, zero-based): https://wstein.org/books/modform/stein-modform.pdf . The general congruence bound and Γ₀ index were freshly read.
- PARI/GP official elliptic-curve documentation, `ellan`, `ellrank`, `ellsaturation`, `ellap`: https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html . `ellrank` supplies lower and upper rank bounds using descent/Cassels pairing; the calculation does not invoke `ellanalyticrank` or `ellbsd`.
- J. S. Milne, *Elliptic Curves*, Chapter II reduction discussion and Chapter III Tate-curve discussion: https://www.jmilne.org/math/Books/EC2.pdf . Multiplicative reduction and Tate uniformization are standard imported results; the inertia and finite-group deductions above are written out.
- Standard imported modularity, Chebotarev and Brauer–Nesbitt are used solely to infer existence of the residual isomorphism from the congruence. No explicit arithmetic identification is claimed from trace equality.

The 144 exceptional Brandt integer quoted by the historical pilot is not recomputed in this admission return. It retains its prior grade if used later. This admission work has not established the old pilot's separate Sha(E/K)[5]=0 assumption and does not need it.

## 7. Reproduction

Run `python3 run_admission.py` from this folder. It executes the bound GP input through stdin, verifies both exact Sturm comparisons, runs independent point counts and finite-group controls, saves compressed full coefficient vectors and updates RESULT.json. The source model file and GP executable are hash-bound. `executed.gp`, stdout and stderr preserve the actual execution. The only stderr line in the successful run is the declared bounded stack-size warning.
