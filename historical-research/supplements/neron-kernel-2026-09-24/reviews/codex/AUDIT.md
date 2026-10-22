# Cross-check of the returned Néron denominator result

Verdict: **RETAIN_NORMALIZATION_AND_DENOMINATOR_AT_STATED_GRADE**.

The new reconstruction-lattice prerequisite is supplied for the specified degree-zero integral seed theta packets. No material defect was found in the new deduction. This is a source-reviewed written result with retained arithmetic imports, not a formal verification or a computed seed witness.

## Identity and scope checked

- Supplied review ZIP SHA256: `77df55b11e7ea51cc06e284e720f6068aeda4551661428ec3b1215e52494db6e`.
- All 10 review manifest entries match.
- The live Cloud branch resolved to `b358f7507759dad4a1e016c519d6f486ffca37e1` when fetched for this check. All five Git blob identities named by the review match the actual commit.
- Relative to prepared handoff `e5b4dd2ea7463b6408cf56ab706dd46579071b65`, the Cloud result adds only the ten files in its own output directory.
- The local decisive-step audit was read separately. Its own stated scope excludes Phase 1; it is not a second independent audit of Kim–Ota.
- The expert repository remains clean at `2a726213a27a12f10fece5bc70137e65e30911ba`. No push, merge, new Cloud session or successor construction was performed in this check.

## Mathematical interfaces

The Cloud normalization and denominator proofs, supplied Pro review, and local audit were read. The exact local primary texts of Kim–Ota §6.1 (including Remark 6.6(1)), ARS Theorem 2.1, and CNS Proposition 5.14, Proposition 6.2 and Theorem 6.12 were checked against the stated uses.

1. **CNS domain and normalization.** Proposition 5.14 is a criterion for the general cusp forms in its domain, with the stated slash expansion. It does not require that the theta packet be a normalized newform. Its bounds are `-n`, `e-n+1/(q-1)`, and `0` at the initial, intermediate, and final components.

2. **Theta bound.** In the split local frame the two off-diagonal sums give zero off support and `q^(2e)` on support; the remaining hyperbolic sum gives `q^e` times a root of unity. Pairing nonzero dual vectors with their negatives cancels the theta factor `1/2` exactly, including at 2. The prefactor then gives the bound `e-n`. The division-place norm Gauss identity remains a retained local import; this turn did not independently implement every division-place case. The globally normalized theta transformation remains the prior written derivation; its entire analytic implementation was not rerun.

3. **Explicit differential lattice.** The bound already meets CNS at conductor-exponent-one primes. A multiplier of one local prime suffices at the intermediate components of `2^3` and `4547^2`. The stated rational-singularity conditions identify the resulting differential lattice with the Néron cotangent lattice. Consequently `D0 = 2*4547 = 9094` works for the integral cuspidal theta combinations under discussion.

4. **Pullback.** For the chosen map, `i_E^* omega_G = (ed/c_E) lambda_f(G) omega_E = c_E K_E(G) omega_E`. Thus `D0*c_E*K_E(G)` is integral. Using the retained bound `c_E | 512` gives

   `B_theta*K_E(G) in Z`, with `B_theta = 4,656,128`.

   Only one Manin factor is needed after this pullback. The Manin bound itself was not reproved here and retains its geometric dependencies.

5. **Unit scale.** The pairing-ideal and full Hecke/cusp-lattice identifications are consistent with the supplied definitions and normalization. Kim–Ota and ARS give the claimed equality of good-prime valuations at their stated import grade; this is not a global equality `M=d` or `M=r`. Kim–Ota's nonordinary crystalline adaptation stays explicitly imported. We did not reprove its Taylor–Wiles argument, the residual-image theorem, or the chosen-map/isogeny classification.

## Acceptance contract that must accompany any evaluator

For the actual analytic input, choose an integral degree-zero lift `z_p^0` of the mod-p Gross packet. If `deg(z_p)` is divisible by p, the correction

`z_p^0 = z_p - deg(z_p)[a]`

has degree zero and the same mod-p reduction. The corrected weights and chosen class must be recorded. The sharp lattice does not automatically apply to a noncuspidal anchor diagonal, even though the final anchored quotient can compute the cuspidal packet scalar.

For an admissible good prime, let `n_p=B_theta*K_E(z_p^0,z_p^0)`. Then

`n_p in Z`, and `p ∤ n_p <=> M2(p) != 0 => Sha(E/Q)[p^infinity]=0`

uses the retained forward bridge. No converse from Sha vanishing to the witness is supplied.

Use the exact final-scalar radius `1/9,312,256`, not a rounded display value. The fallback denominator is `595,984,384`, with exact radius `1/1,191,968,768`. All pair, period and tail errors must already be included. A radius bound guarantees at most one lattice point; a certified enclosure and lattice membership supply existence.

A wider interval may suffice if its scaled integer range contains no multiple of p. An interval with no lattice point at all is an inconsistency, not a unit certificate. These distinctions are correctly implemented in the attached acceptance function.

One small wording refinement in the Cloud proof is advisable when transferring it: the table headed “smallest t with p^t omega_G regular” establishes the smallest t **certified by the displayed bound**, not optimality for the actual weighted forms. The same file correctly says that sharpness of b=1 was not investigated. All decimal thresholds in display tables should be marked approximate; production uses the exact fractions.

## Executed checks

- Replayed the supplied 262 exact Eichler Gauss comparisons, wrong-phase/amplitude controls, all 13 threshold inequalities and arithmetic/relifting tests. Output agrees with the supplied JSON except for elapsed CPU time.
- Independently compared the acceptance routine to direct integer enumeration on 41,925 intervals, including negative endpoints, exact boundaries and empty-lattice cases. No disagreement.
- Confirmed rejection of eight inadmissible prime inputs.
- No numerical period quadrature was repeated; its supplied output remains a numerical cross-check, not an independent rigorous quadrature certificate from this turn.

## Endpoint effect

This closes an actual reconstruction prerequisite of the normalized paired-kernel route: its scale and a finite real reconstruction lattice no longer require computing the unknown quaternionic norm M. It is more than a constant-factor optimization.

It does not provide a seed numerator interval, prove the witness nonzero, establish a prime-family conclusion, or address the exact real leading term Q36. The integer B is a denominator for many p-dependent numerators, not a fixed integer whose prime support controls Sha. The appearance of 4547 in B does not settle the 4547-primary Sha group.

The next computational proposal must therefore address obtaining the actual seed numerators under the final error contract. A fresh denominator hunt, repeated support-first implementation or automatic production run is not warranted by this result. This cross-check launches none of those tasks.
