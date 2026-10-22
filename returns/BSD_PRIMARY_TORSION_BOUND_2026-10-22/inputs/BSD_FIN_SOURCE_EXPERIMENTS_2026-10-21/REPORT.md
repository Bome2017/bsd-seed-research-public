# FIN continuation: exact source experiments and an obstruction to the current analytic estimate

**21 October 2026 — NO_NEW_COMPLETE_SEED_BOUND.**

I executed new bounded experiments on the actual coefficient-five point field. They did not produce the needed ordinary units or a smaller complete class-lift allowance. The return also proves that the specific October 20 whole-class-order expression cannot, by itself, reach the parity-relaxed source bound of three at any good coefficient prime.

**FIN, ORDER9 and Q36 remain open. No new primary component was settled.** These are scoped exclusions and an algorithm-selection result, not progress through the missing small arithmetic bound.

## 1. Norm-one source experiment, followed by its multiplicative closure

The retained degree-24 seed field is A=Q(w), with monic even F(w), scalar σ of order four, and τ=σ² taking w to −w. New families were built to have relative norm one by construction, rather than hoping a random source would pass the norm test.

| Exact test | Outcome |
|---|---:|
| Rational Cayley candidates (bw+a)/(bw−a) | 20,180 |
| Quadratic Cayley candidates (a+bw²+cw)/(a+bw²−cw), after deduplication | 272 |
| Candidates passing necessary trace integrality | 0 |
| Independent full multiplication-matrix sample checks | 17 passed |
| Quadratic generators factoring exactly into the rational family | 12 |
| Remaining generator scalar orbits with private unramified norm support | 20,440 out of 20,440 |
| Independent direct-product verification of private support | all 20,440 passed |

Nonintegral trace rejects an ordinary unit but does not rule out products. The adaptive closure calculation addressed that gap. After removing the twelve exact redundancies, every generator has a rational-prime factor of its norm which occurs in no other generator norm and does not divide the polynomial discriminant. Its scalar orbit supplies an independent pair of anti-invariant divisor directions. The written proof shows that the full tested scalar-closed multiplicative family contains no ordinary unit except 1, and saturation adds no non-torsion units.

The rational subfamily has a stronger separate mod-five exclusion: every private norm remainder is not a fifth power. Its scalar-closed divisor map is injective modulo five, so it supplies no nonzero ordinary virtual-unit class either. This stronger mod-five conclusion is NOT asserted for the 260 irreducible quadratic generators.

See SOURCE_FAMILY_PROOF.md, CAYLEY_RESULT.json, CAYLEY_INDEPENDENT.json, COMBINED_SUPPORT_RESULT.json, COMBINED_DIRECT_CHECK.txt, and LINEAR_MOD5_CHECK.json. The full evidence package contains the raw exact traces, norms, gcd certificates and sources.

## 2. The earlier positivity result does not make the existing class estimate small

Let B_p denote exactly the upper-bound expression (G) in the October 20 SCALING.md. It bounds the order of the entire relative class group using the discriminant-based shortest-vector regulator estimate. It is not the class number itself.

Using the already retained type-III contribution at 4547, I derive

    B_p > 1000^((p²−1)/4) > p^4

for every good coefficient prime p≥5. The proof only bounds the strength of that expression. In particular, it DOES NOT say that the actual class group is large or nonzero.

Even granting maximal removal of the unit term, substituting only floor(log_p B_p) for the class allowance can never give an upper bound of three. Thus evaluating the previously unknown discriminants more accurately within the same formula cannot finish this route. A stronger regulator estimate, a different class estimate, or genuine class-map/local cuts remain possible; none is ruled out by this calculation.

This sharpens the interpretation of the previous return: its uniform positivity gate is a valid deduction, but it does not provide a viable finishing mechanism using this whole-order estimate alone. See ANALYTIC_OBSTRUCTION_PROOF.md and ANALYTIC_OBSTRUCTION.json.

## 3. What remains genuinely unresolved

On the retained valuation-zero domain, the needed complete source bound still has the form

    dim K_chi <= (p+1)/2 − r_U(p) + k_C(p).

The parity-relaxed sufficient estimate is r_U−k_C≥(p−5)/2. The present experiments do not establish that inequality, even independently at the calibration prime five. They do not reduce k_C from its previous coarse allowance and do not construct a new ordinary unit that increases r_U.

The remaining meaningful direction is a certified presentation or independent bound for the *surviving faithful class-lift kernel*, imposing global and local conditions with one compatible unit repair. A partial generator list still cannot be treated as complete. Neither extending the excluded Cayley families nor merely computing more discriminant data within expression (G) addresses that obligation.

No new complete class-presentation producer or cofinite bound was obtained in this turn. The negative outcome is explicit rather than recast as a conditional FIN theorem.

## 4. Computation and review boundaries

The polynomial and scalar-action identification with the actual seed are retained inputs, read from the pinned repository. They were not independently re-established by a fresh maximal-order computation. All new trace, norm, gcd, and factor identities use exact arithmetic. A clean-directory replay rebuilt both C programs and regenerated all raw outputs: twelve deterministic result files matched byte-for-byte, and four summaries matched after excluding elapsed times. The private-support producer and direct-product verifier are different C/GMP implementations; the 17 trace samples use companion matrices rather than the producer's logarithmic-derivative/Newton-sum formula. These are implementation checks, not independent human or proof-assistant certification of the written arguments.

PARI/GP is unavailable in this execution environment; installation/download attempts failed. A separate bounded Wolfram call for actual degree-24 fundamental units produced no result. A first Wolfram call had a malformed Root function and was rejected; a corrected call encountered a backend error; the final corrected bounded call returned no result. None is a completed class/unit computation. The first pure-Python batch-GCD pass exceeded its bound; the completed producer was changed to GMP and independently checked. No unfinished output was accepted.

No paid computation, p53/743 production run, main merge, research-release change, or asynchronous task was started. The requested order remains (1) FIN research, then (2) the 53/743 certificate, then (3) Q36. Stages two and three are not claimed complete or launched.

## Source base

Bome2017/bsd-seed-lab at 77d4b331885138eb1f3f93d8063b06d6d7eb730b, incorporating the October 20 field/class construction at ceadfa43 and October 21 positivity return. Specific inputs: seed_five/construct.out and construct.gp under BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20; relative_source/fields.gp under BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20; and theory/SCALING.md under BSD_CLOSED_CLASS_CONSTRUCTION_2026-10-20.
