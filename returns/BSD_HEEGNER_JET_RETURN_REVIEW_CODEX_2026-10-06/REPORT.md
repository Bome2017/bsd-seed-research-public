# Revised Heegner return and completed W3 constructor: review

Date: 2026-10-06. Status: **SOURCE_CERTIFICATES_REPLAYED; EXISTING_SEED_EVALUATOR_CONNECTED; UNIFORM_BOUND_OPEN**.

The two Pro assessments recommend opposite priorities. They each identify valid ingredients, but neither establishes that its preferred lane is closer to a uniform theorem. The concrete change in these returns is that W3 now supplies recombinable source rows, and its weight-two extraction can use an evaluator already present in the project. I connected and checked that extraction against the seed's old, certified p=5 data. No new primary component or uniform bound was obtained.

The Heegner two-prime criterion is valid on the matched ordinary domain. However, for the fixed field Q(sqrt(-23)), the retained finiteness of the twist's Sha implies that the proposed two-prime allowance does not relax the infinite-tail problem. The deduction below makes that qualification precise.

This review reads the supplied returns and targeted prior evidence. It is not a fresh audit of the entire BSD archive, the retained Hida construction, or all theorem imports. No new Lean build was run, and no remote Aristotle job was launched or messaged. The originals remain unchanged.

## 1. What changed in the W3 return

The earlier progress transcript lacked provenance for its elimination rows. The completed return fixes that specific problem. I reran `cert_seed.py` in a scratch copy, after reading its source. All three certificate files reproduce byte-for-byte:

- order-zero multipliers;
- order-one residual;
- order-two residual.

The summary agrees after excluding elapsed times. The checker regenerates the specified rows and recombines their multipliers on all columns. This is independent execution of the supplied implementation, not an independent implementation of every Hecke action or formal verification of the global arithmetic source.

The result remains narrower than four actual W3 values. At p=31, order zero is a multiple of the seed's vanishing central value. The selected first- and second-order pieces retain the Lambda-adic mass coefficients and weight-two symbol values; they do not evaluate them. The order-two output is not a complete modulo-31^4 certificate. In particular the source report explicitly leaves Lambda_2 unknown.

The quadratic forcing statement is conditional on the retained source identification, global double zero, functional equation, and cofinite integral Hida domain. Membership of 31 in that domain is explicitly unverified in the return. Switching the pilot to 17 does not, by itself, verify membership of 17 either.

## 2. The seed evaluator exists, and the connection has now been tested

Pro is correct that the missing weight-two oracle is available elsewhere in the project. The existing pinned `arbcore msl` supports composite denominators. This is established both by its parameter checks and by the historical, certified seed computations at m=25 and m=81. It is not necessary to invent composite-modulus support.

I added a downstream reader for the evaluator's exact rational XB candidates. It checks complete unit-residue coverage, plus symmetry, p-integral denominators, and the recorded containment/uniqueness flags. Those checks do not replace the producer's interval, lattice, or coefficient-corpus certificates.

Using the retained seed outputs at m=5 and m=25, the reader gives

    (ell_0, ell_1, ell_2, ell_3) = (0, 0, 2, 0) modulo 5.

The supplied `weight2_jet.py` gives the identical vector on those same exact values. The ell_2=2 result agrees with the separately written September 19 downstream certificate. This tests the connection to actual seed arithmetic without running a new Fourier evaluation. It is a replay of an old settled case, not a new Sha result or a p=5 application of the W3 theorem.

There is also a small simplification. For every p>=5 and i<=p-2, the lower-level term in the ordinary measure contributes zero to ell_i modulo p. Therefore ell_2 modulo p needs only the p^2-denominator table. `CYCLOTOMIC_EXTRACTION.md` proves this and preserves the period convention. The p-denominator table remains useful as a distribution/Hecke control, but it is not mathematically necessary to extract this residue.

The old p=5 computation already used this cancellation in that case. The general statement and reader are operational consolidation, not a claim of literature novelty or new uniform arithmetic.

### Exact cutoff check

I ran only the pinned evaluator's cheap cutoff planner, with the historical stricter quarter-tail setting. No symbol-evaluation job or coefficient production ran.

| Denominator | Minimum cutoff | Aligned coefficient segments | Fits existing 6,445-segment corpus |
|---|---:|---:|---|
| 17 | 5,582,260,929 | 333 | Yes |
| 289 | 100,324,370,478 | 5,980 | Yes |
| 31 | 10,302,967,622 | 615 | Yes |
| 961 | 341,242,174,491 | 20,340 | No |

Thus Pro's rough 5,600 / 18,600 segment estimates were low, but its main feasibility observation for p=17 survives. All 6,445 coefficient paths currently exist; their content integrity is retained from the sealed corpus receipt, not freshly rechecked in this review. The binary hash matches the pinned engine. A future run still needs its ordinary prelaunch bindings and resource cap.

The historical throughput suggests roughly 11.5 CPU-hours for m=289, not a current benchmark or a guaranteed run cost. That computation is not needed just to establish that the evaluator-to-extractor connection works: the old p=5 replay already does that.

### What a p=17 result would mean

It would supply an actual cyclotomic coefficient at an already-settled seed prime. A unit result would support the conditional quadratic forcing implication once the source/domain hypotheses are matched. It would not construct Lambda_2, the complete weight derivatives, all four values modulo p^4, or a cofinite bound.

Conversely, Sha[17]=0 does not force ell_2 to be a unit through the supplied one-way criterion. A zero ell_2 would not falsify the four-value method: other weight-direction coefficients or cubic terms could still matter. The old tame c_2 at auxiliary 103 is not this cyclotomic ell_2 at conductor 289.

The reader preserves the evaluator's real-period convention. The old Manin-constant result makes the indicated powers-of-two period changes p-units for odd p; it does not certify every comparison to an arbitrary canonical Hida period. No unknown p-factor has been set equal to one here.

## 3. Heegner: the source match is retained, and the two-prime claim needs qualification

The previous [pinned review](https://github.com/Bome2017/bsd-seed-lab/blob/fe9d9e5a2b556f7e574ab9e0718b405bc330adea/work/returns/BSD_DIRECTION_REVIEW_CODEX_2026-10-06/REPORT.md) already matched Zhang's ordinary hypotheses for the seed, including its nonsquarefree conductor, on p>=5, p not dividing 23N, p good ordinary. Repeating that match at 53 is not a new research obligation. The latest return's uncertainty about square factors is superseded by that review.

The common-modulus trace correction and finite-batch Chebotarev construction remain valid. They ensure eligible auxiliary primes, not indivisibility of their derived points. No such point was evaluated in the new return.

The ordinary first-nonzero-class criterion and sign used here are those of [Zhang, Lemma 8.4](https://math.mit.edu/~wz2113/math/online/Kconj.pdf), with the previously matched hypotheses and genuine primitive Heegner system. The lemma fixes the larger conjugation eigenspace dimension at nu+1 and bounds the other by nu. Its source was re-read for this deduction.

Let

    s_p = dim Sha(E/Q)[p],
    t_p = dim Sha(E^(-23)/Q)[p].

The retained ranks and quadratic descent give the two dimensions 2+s_p and 1+t_p. Therefore

    nu_p + 1 = max(2+s_p, 1+t_p).

In particular nu_p<=2 does imply s_p=0, using the sign and the two rational point directions. But the project already retains rank one and finite Sha for the -23 twist. Outside the finite support of that twist Sha, t_p=0, and hence

    nu_p = 1+s_p.

Thus, on that ordinary cofinite domain,

    nu_p<=2  <=>  nu_p=1  <=>  Sha(E/Q)[p]=0,

where the first equivalence uses retained parity. The nu=2 case can help at finitely many twist-exceptional primes: it requires s_p=0 and t_p=2. It does not create an independently weaker tail estimate. See `HEEGNER_TAIL_COMPARISON.md` for the proof and source boundaries.

This does not rule out Heegner arithmetic as a route to proving the estimate. It corrects the claim that merely allowing two factors has made the cofinite target materially less demanding. Supersingular coverage remains separate.

One earlier correction also remains necessary: PROOF.md still defines a squarefree failure index and divides the original modulus by it. A failed prime occurring to higher power can survive that quotient. Revision 2 discusses bad-prime filtering but does not repair this failed-prime formula. Use eligible prime sets, or remove the full power of every failed prime, as in the previous review.

## 4. What to carry forward

W3 has the more concrete implemented extraction in these two returns. The statement that its seed oracle is absent should be narrowed to the remote sandbox. However, the evidence does not justify turning that into a new prime-by-prime campaign or calling one coefficient a completed W3 source constructor.

For the user's uniform objective, the unresolved research output is still an arithmetic control across primes. On W3, the newly exposed distinction is between the computable cyclotomic coefficient and the unresolved weight-direction mass; a useful continuation must construct/control the latter or prove an independent complementary nonvanishing law. On Heegner, it must control genuine derived classes rather than repeat eligibility or the nu<=2 implication. This review has not supplied either control.

The returns should be retained, and the reusable reader should travel with any future computation. Neither Pro recommendation, as written, is enough to justify claiming that the uniform obstacle has been crossed. FIN, ORDER9 and Q36 remain open.

## 5. Custody and limits

The revised Heegner root manifest verifies 26/26; its research-return manifest verifies 27/27 against the project root. The W3 inherited root manifest verifies 166/167: README.md differs. It also does not cover the new W3 source files. Fresh archive/member bindings preserve the actual received bytes, including those additions. This is a manifest coverage issue, not evidence that the new certificate replay failed.

The compact review includes the replay comparison, exact cutoff results, old seed tables, adapter, negative controls, finite dimension controls, and proof notes. Complete supplied archives are preserved separately in the lab. Hashes establish custody; the mathematical grades above remain unchanged by publication.
