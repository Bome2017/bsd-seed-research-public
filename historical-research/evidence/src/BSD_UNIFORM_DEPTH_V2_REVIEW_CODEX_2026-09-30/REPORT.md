# Uniform-depth v2: independent review and decision

**Verdict: ACCEPT_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE.**

**Return status REDUCED is appropriate.** No blocking error was found in the new capped minimum-depth comparison or in the same-conductor two-prime construction. This is a new proved comparison relative to the supplied project records, not a newly proved uniform upper bound. No literature-priority claim is made.

## Integrity and scope

Archive SHA-256: `ebb3d4c134c26149b4b18e0c6cc1c7a43c835cbeb4e54c0d6ab73353bd104caa`.

The return's **14 manifest entries** verify, ZIP CRC and safe paths pass, and the four loose supplied files match their archive copies. The return's separate claim that it checked 26 original input entries is its execution record; it is not the size of this return manifest. The two locally available source PDFs were independently hashed and match its pinned BH and Kriz–Nordentoft hashes. Source statements were checked in the local texts and rendered pages; live arXiv HTML was also consulted. Original arithmetic certificates, B.20/B.21's underlying source applications, and source-paper proofs were retained rather than rebuilt.

All six attempt files, source/custody notes, controlling brief, return, and self-replay were read. This review is an independent written mathematical check, not formal verification or a seed computation.

## What survives

Write d_p=dim_Fp Sel_p(E/Q), r_p for the minimum unit Kurihara length, and h_p for the minimum lambda-depth over the real cyclic degree-p fields and faithful characters specified in the return. For every good p>=5:

    min(h_p,p-1) = min(r_p,p-1) = min(d_p,p-1).

For this rank-two seed at the retained grades:

    h_p<4  <=>  h_p=2  <=>  r_p=2  <=>  d_p<=3
           <=>  Sha(E/Q)[p^infinity]=0.

The equivalence is between existence statements. It does not say a preselected field or every field works. Conditional on a supplied two-prime unit pair, every full-support cyclic quotient of that pair's compositum works, at that same conductor.

## Decisive proof checks

1. **Source domain.** BH Hypothesis 1.2 and Theorem 1.4(b) apply to the real abelian p-extensions used here. Good reduction makes the additive condition vacuous; reality supplies the roots-of-unity alternative. The retained residual surjectivity gives the required p-adic image. The written lifting proof is valid for p>=5: the conjugation sum is quadratic in the unipotent exponent, whose first three power sums vanish modulo p. Conjugation spans sl_2 and successive pth powers lift all congruence layers.
2. **Generator lower bound.** E(L)[p]=0 follows because the residual image over an abelian extension contains SL_2(F_p). Selmer restriction is injective; local Kummer conditions need only be preserved, not identified. Duality gives Y_L coinvariants surjecting onto X_p. Thus the minimal generator number of Y_L/pY_L is at least d_p. A minimal presentation over the local group algebra has relation entries in its augmentation ideal J. Fitting base change then gives theta_L mod p in J^(d_p). This correctly retains finite and potentially divisible excess Sha.
3. **Conductor norm relation.** BH Proposition 2.4 gives a_q-u-u^(-1) for deleting a good conductor prime. At a Kato prime this reduces to −(u−1)^2/u. Multiplying the smaller-field theta, itself in J^(d_p), yields J^(d_p+2). Consequently the degree-d_p initial form vanishes on every coordinate hyperplane. In d_p variables the only surviving degree-d_p monomial is their product, with coefficient precisely delta_n in the complete total-period symbol sum.
4. **Same-conductor quotient.** A quotient nontrivial on each inertia factor has conductor n, so projection introduces no extra imprimitive Euler factor. T_i maps to s_i t+O(t²), giving leading coefficient delta_n times the product of the nonzero s_i. In particular the diagonal quotient works.
5. **Valuation cap.** A p-divisible coefficient has lambda-valuation at least p−1. For d_p<p−1 the unit leading term therefore uniquely controls the valuation. For d_p>=p−1 only the capped statement follows. The p=5 threshold is handled correctly: depth two is below four, and equality at four remains insufficient.
6. **Two-prime replay.** The quadratic formula does not assume the chosen pair is already minimum: the base rank-two lower bound suffices. Projection to either one-prime field lies in its fourth augmentation power, killing both pure quadratic coefficients. Only delta_(q1q2) T1 T2 remains.

Normalization is consistent: the BH plus symbol uses the total real period, one half of the production symbol for this seed. Minus symbols cancel on a real quotient in the full sum. No averaging, extra division by p, or deletion of an Euler factor was introduced.

## Endpoint attempts

The scoped failures are sound: augmentation-preserving maps cannot shorten fourth-order data to depth below four; distinguishing the rational-point subspace does not exclude additional Selmer directions; a higher-index unit Fitting ideal does not force the second ideal to be a unit. The paired examples are abstract module examples, not alleged elliptic-curve counterexamples.

The norm criterion is valid. For nonzero beta=2048 chi(theta_K), integrality and total ramification give v_p(Norm beta)=v_lambda(chi(theta_K)). Thus 0<|Norm beta|<p^4 suffices. **This is a stronger sufficient condition, not an equivalent reformulation of depth<4:** a shallow p-adic value may have an arbitrarily large prime-to-p part in its norm. No construction or estimate achieving the inequality was supplied. The triangle-bound calculation is accurate but supplies no such bound.

The common finite integral module, bounded-lift criterion, and conditional scalar uniqueness are also valid as explicitly conditional statements. Their required arithmetic comparison maps are unconstructed. Neither completion, the known 3-part, nor the rank-zero auxiliary twist automatically supplies them. None justifies a new endpoint claim.

## Source checks and boundaries

- [Bullach–Honnor, arXiv:2511.07203v1](https://arxiv.org/html/2511.07203v1): checked Hypothesis 1.2, Theorem 1.4(b), the period and full-element definition, and Proposition 2.4. Theorem 1.4(b) concerns the classical Selmer dual and does not acquire the separate finite-Sha hypothesis from the preceding discussion of another Selmer object.
- [Kriz–Nordentoft, arXiv:2310.20678v3](https://arxiv.org/html/2310.20678v3): Corollary 5.20 still takes witness length r as input. It does not bound r independently. The new comparison does not turn that printed estimate into an independent upper bound.

The previous project review explicitly retained only sufficiency of the low-depth character criterion. This return supplies the missing converse with its same-conductor construction. That distinguishes it from the Q36 return's rediscovery of M2. Its mathematical contribution should nevertheless be stated as a comparison, not coverage of new vanishing primes or progress already excluding excess Selmer.

The comparison covers good primes >=5, including 19,59,487. This is theorem applicability, not new primary vanishing. It gives no conclusion at the three bad primes, no common rational scalar, and no new relation to the real BSD quotient.

No original files, repositories, current maps or running tasks were changed. No messages, pushes, successor agents, paid jobs or prime computations were launched. Proposed record text and the next-step decision are separate files here.

FIN, ORDER9 and Q36 are unchanged.
