# Independent desk review of the C3 finite-modulus repair

2026-10-11. Reviewed file: `notes/C3_ASSEMBLY.md`.

**Verdict: C3_FINITE_MODULUS_REPAIR_SUPPORTED_UNDER_RETAINED_INPUTS.**

The fixed-base idempotent and the Chinese-remainder/Hom-line arguments are sound. The finite proof transport through BD 5.15–5.18 is supported by the proof's actual dependencies; it is not an application of the ordinary anticyclotomic main theorem. I found no mathematical reason to demand a rational idempotent at the raised level before constructing this finite-modulus comparison.

This review is independent of the author of `C3_ASSEMBLY.md`, but is a desk review by another model agent, not human review or formal verification. The retained seed modularity, exact rational multiplicity-one module, and full residual image have not been recertified. Boston–Lenstra–Ribet and the integral geometric results imported by BD remain source dependencies.

## 1. Source read and the scope of transport

I read the preserved `BSD2005.txt`, lines 1780–2220 and 2345–2644, including the two steps of 5.17, and checked the corresponding published PDF text. Section 5 permits general Eichler level `M+`; squarefreeness belongs to `M−`. At the primes used for the graph comparisons, the relevant level exponent is one. Consequently the repeated prime factors already in the seed's `N+` do not obstruct these geometric arguments.

The 5.15 calculation uses base character-group freeness, the integral graph/Hecke comparison and the admissibility congruence. The 5.16–5.18 argument uses toric uniformization, residual isotypy, local cohomology and the exponent calculation. I found no unit-root or ordinary filtration in this finite chain. The later construction of norm-compatible classes does use the coefficient-prime level and ordinarity; it has not been transported by C3.

This supports a **written finite-proof transport**, rather than a claim that the published theorem was literally stated with no coefficient-prime level.

## 2. Fixed Hecke idempotent: the repair is adequate

Let `M` be the exact fixed base character group, and `T` its faithful integral Hecke algebra. The retained rational eigenspace must have multiplicity one in this module. It is not enough to know multiplicity one in a different space without an identification.

Given an integral Hecke element `h` separating the eigenvalue `a` from every other characteristic-zero constituent, write

`det(X-h)=(X-a)Q(X)`, `J=Q(a) != 0`.

The endomorphism `Q(h)/J` is identity on the E-line and zero on the complementary primary subspace, so it is the idempotent `e`. This remains valid if the other primary subspaces have nontrivial generalized eigenspaces: the complementary characteristic polynomial annihilates them. Since it is a polynomial in `h`, the idempotent belongs to `T[1/J]`, which is essential for the Hecke-algebra conclusion.

The `e`-factor of `T[1/J]` is exactly `Z[1/J]e`: its rational action is scalar, integral Hecke eigenvalues lie in `Z`, and all scalar operators are present. The image `eM[1/J]` is a rank-one projective module over the PID `Z[1/J]`, hence free. This gives base Hecke completion `Z_p` and a free rank-one character group for every `p` outside `J`.

Thus the proof supplies the hypothesis needed at the **fixed base**, not merely a torsion-free quotient. If a Brandt module is used instead, the fixed integral comparison and primitive-coordinate indices must be included in `J`, exactly as the assembly says. There is no numerical certificate excluding a particular seed prime from this uncomputed integer.

## 3. Raised level: where integral multiplicity one comes from

It is legitimate to reapply one uniformly quantified finite theorem for every admissible prime power. No new raised-level rational idempotent is needed in that operation.

For additional clarity, the rank-two freeness step can be written without the compressed two-generator intersection sentence in the source. Put

`V=T_p(J_ell)/I`, `R=Z/p^n`.

After residual multiplicity one, `V/pV` is the irreducible two-dimensional representation `E[p]`. The exponent calculation gives exponent exactly `p^n`. Nakayama makes `V` two-generated. Multiplication by `p^(n-1)` induces a nonzero Galois-equivariant surjection

`V/pV -> p^(n-1)V`.

Irreducibility makes this an isomorphism. Both elementary divisors of the two-generated R-module therefore have exponent `p^n`, so `V` is free of rank two over R. This retains the full integral module; it does not infer freeness solely from a residual dimension count.

**Freeness is not yet identification as a Galois representation.** That identification additionally uses the Eichler–Shimura characteristic polynomials and the absolutely irreducible residual representation, as in BD 5.17. Matching Hecke values supplies matching traces and determinants at the good Frobenii; the residual absolutely irreducible trace comparison identifies the rank-two representations. That source dependency should remain named when the argument is summarized.

There is no new lattice ambiguity requiring a p-unit period comparison here. The E representation itself supplies `T_pE`. Stable lattices in its absolutely residually irreducible rational representation are homothetic: after scaling one lattice into the other with nonzero residual image, irreducibility and Nakayama make the inclusion equality. Homothety gives an abstract integral Galois-module isomorphism, but no chosen normalization of that isomorphism. The Hom line in C3 is precisely what avoids making such a choice.

The comparison's Hecke actions must remain the actual Picard/Albanese actions in the monodromy sequence. They cannot be silently identified at all bad operators. BD keeps them distinct and relates them by its involution; C3's use of the natural component quotient and Picard Tate-module action is compatible with that convention. A future implementation must preserve it.

## 4. No hidden raised-prime denominator in this chain

The monodromy and component comparisons are integral. The auxiliary Euler factor's p-unit requirement is the explicit admissibility condition `p ∤ ell^2-1`. The factor selected by level raising is intentionally divisible by `p^n`. The unwanted Eisenstein modules disappear at the residually irreducible localization; their orders need not be inverted one auxiliary prime at a time.

Thus the fixed base isolation integer and the visible admissibility tests suffice for this first raised quotient, subject to the stated geometric/source inputs. This review does **not** extend that statement to an iterated raised base, the second reciprocity law, or an entire Euler system. A subsequent base has its own freeness question.

## 5. CRT and the Hom line

Let `m=prod p^n`, and use one fixed raised Jacobian with the compatible Hecke characters specified by their eigenvalues. Their kernel ideals are pairwise comaximal, because they contain coprime scalar prime powers. CRT therefore applies to the component module itself, not merely to its cardinality:

`Phi/I_m = prod_p Phi/I_(p,n)`.

The product of the finite Tate quotients is an `R[G_Q]`-module isomorphic to `E[m]`, where `R=Z/m`. For each prime-power factor the endomorphism ring of `E[p^n]` is `Z/p^n`: reduce a commuting matrix modulo p, subtract the resulting scalar, divide the remaining entries by p, and repeat. Residual full image supplies the scalar centralizer at every step. Hence

`H_m=Hom_(R[G_Q])(E[m],V_m)`

is an invertible R-module and evaluation `H_m tensor E[m] -> V_m` is an isomorphism. This is basis-free even though an isomorphism proves its existence. Finite product decomposition commutes with continuous cochains and their finite/singular local quotients. The geometric Kummer/specialization map is therefore the same map assembled by CRT, and each prime-power isomorphism proves its product an isomorphism.

Changing temporary bases cancels in the stated tensor formula. This cancellation establishes independence from the chosen Galois-module isomorphism; it should not be described as a proof that different CM orientations or different auxiliary pairs have the same scalar.

## 6. Coefficient compatibility and endpoint boundary

For a fixed auxiliary pair, the characters with smaller prime-power modulus are reductions of the larger ones: the specified Hecke generators have the same values. The original geometric maps reduce compatibly. At an admissible auxiliary prime, Frobenius over `K_ell` has eigenvalues `1` and `ell^2`, whose difference is a unit, so the relevant finite/singular rank-one local modules commute with coefficient reduction. This supplies the claimed compatibility when the geometric input and its orientation are held fixed.

It gives no compatible map between different raised Jacobians. One fixed detecting pair admits only the coefficient powers dividing its two nonzero level-raising integers. Consequently finite CRT is not a rational-globalization argument. Even extending compatibility beyond that bounded set would require an additional reason for the residues to lie in the diagonal image of a rational number.

**Recommended status:** the obstruction “5.17 works only one p at a time, so C3 cannot be assembled” should be removed. Replace it by the finite-modulus conditional construction proved here. Keep C4's additional interfaces, C8 evaluation, cross-level scalar comparison and every endpoint open. No seed prime has been certified outside `J`, no scalar has been evaluated, and no new primary vanishing follows.

## Evidence references

- Reviewed note: `/Users/bsm/BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11/notes/C3_ASSEMBLY.md`.
- Preserved source: `/Users/bsm/BSD_YUN_ZHANG_MECHANISM_READING_2026-10-07/sources/BD2005.txt`, especially §§5.1–5.6. Section 2.1 also fixes the representation and lattice conventions.
- Published source: https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf, §§5.1–5.6, printed pp.35–52.
- Earlier review: `/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work/returns/BSD_BD_INTEGRAL_REVIEW_CODEX_2026-10-07/MATHEMATICAL_REVIEW.md`, §§1–2.

No raw data were changed, no new arithmetic computation was run, and no external job or publication was made by this reviewer. **FIN, ORDER9 and Q36 remain unchanged.**
