# Qualifications to the revised correction

These are scoped review arguments, not new BSD input. Prior independent review: lab commit `8ee52fb55c6788d48f288257ef12e6da7b4d8c4c`, `BSD_ARISTOTLE_EXCESS_A_REVIEW_CODEX_2026-10-07`.

## 1. What is genuinely corrected

The returned PROOF.md withdraws item 4 of the old Proposition 1. RESULT, CONSTRUCTION, ASSUMPTIONS, ENDPOINT_EFFECT and STATE now agree that A1 has not been reduced to A2 and that this return contains no new derivation. Its archive limitation is stated separately from the existence of the historical −23 certificate. These changes are accepted.

The earlier review's actual-source distinction still governs: DLRV uses a bipartite system, and its admissible-prime definition is not the classical Kolyvagin-prime definition. Naming more missing comparisons does not create a map between them. The direct nonexceptional augmentation corollary remains unavailable for the seed for the corank reason established in the prior review. More general singular-specialization arguments are not thereby refuted.

## 2. C2: use the actual printed factor

Howard, *The Heegner point Kolyvagin system*, §2.3, pp. 26–27 of the linked manuscript, defines a group-ring element Φ and constructs norm-compatible points with Q₀[n]=ΦP[n] (Lemma 2.3.3). Lemmas 2.3.8–2.3.9 track its scalar augmentation. In that normalization,

\[
\operatorname{aug}\Phi=
\begin{cases}
(p+1)^2-a_p^2,&p\text{ inert in }K,\\
(p+1-a_p)^2,&p\text{ split in }K.
\end{cases}
\]

[Primary paper](https://wstein.org/misc/sagedays18_papers/howard-the_heegner_point_kolyvagin_system.pdf), §2.3, especially the displayed definition of Φ and Lemmas 2.3.3, 2.3.8–2.3.9. We do not substitute this formula for a proof comparing DLRV's and Zhang's systems.

For this seed, the retained rational 2-torsion injects under good reduction at odd p, so #E(F_p) is even and a_p=p+1−#E(F_p) is even. For p≥7, Hasse gives |a_p|≤2√p<p−1. An even integer in that interval cannot be congruent to +1 or −1 modulo p. At p=5 the retained exact count is #E(F₅)=8, so a₅=−2, also not congruent to ±1. Therefore

\[
a_p\not\equiv\pm1\pmod p
\]

at every good seed p≥5. In the ordinary/source domain this makes both displayed augmentations units. The proof uses no Sha-vanishing assumption. It is a normalization check; it neither supplies a nonzero classical derived class nor controls an arbitrary nontrivial character component of the group-ring factor.

Thus “nothing in D controls the p-adic valuation” cannot be retained as a demonstrated failure of this scalar factor. If a different stabilization convention is intended, its exact comparison must be written first. This calculation is not acceptance of a unit comparison for every map in C1–C4.

## 3. C3: do not delete the unknown Tate-module term

For the ordinary compact Selmer group, the relevant Kummer sequence is

\[
0\to E(K)\otimes\mathbf Z_p
\to\operatorname{Sel}_{p^\infty}^{\rm compact}(E/K)
\to T_p\Sha(E/K)\to0.
\]

This is also printed at the start of Howard's paper. The rank-three Mordell–Weil input only gives a rank lower bound for the middle term unless the final term is independently controlled. Hence the correction's sentence “H¹_f(K,T) has rank 3, because rank E(K)=3” is too strong as used here. With the matching local-condition identification, replace it by “has rank at least 3.” This is sufficient for the intended warning about coordinates and control; no exact rank assertion is needed.

## 4. Residual nonvanishing remains a hypothesis

The revised D drops the first return's ordinary clause. The elementary deduction from Zhang Lemma 8.4 is sound when its nonzero residual system and sign hypotheses are satisfied. Its minimum support ν_p is not defined as a finite number unless some residual class is nonzero. Nonzero classes at higher p-power levels alone are insufficient.

Retain either a fully matched residual nonvanishing theorem on the stated domain or the nonzero residual-system premise itself. This review does not extend Zhang's ordinary nonvanishing theorem to all supersingular primes. The existing bookkeeping is not a new proof of that extension.

Source previously checked: W. Zhang, [*Selmer groups and the indivisibility of Heegner points*](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf), Theorem 1.1 and Lemma 8.4. This paragraph preserves the hypothesis from our prior audit rather than claiming a fresh complete review of Zhang's proof.

## 5. Precision and certificate scope

The supplied checker has exact hash and integer operations, but its Decimal sqrt/exp/log/power operations are rounded at 80 digits. It prints no proved accumulated error enclosure. Its “exact tail evaluation” label is therefore too strong. The calculation agrees numerically with the retained Arb output; our fresh hash-bound binary combination separately reproduces that Arb output. Neither operation is a second complete implementation of the original finite sum.

All non-floating sections of the supplied checker reproduce exactly as JSON. Its binary-floating sum differs from the supplied output by at most 2.14×10⁻¹⁴ on this host. Both versions lie inside the certified interval. We preserve both outputs and do not claim byte-for-byte reproduction of that floating section. Such agreement is corroboration, not proof of the derivative.

The two model equations can be matched explicitly by x_old=x_min+7578, y_old=y_min. Equal invariant calculations are consistent with that map. The chronology is September 21 certificate followed by October 6 float, not the reverse.

## 6. Unresolved corrections from the prior review

A3 still labels a regulator unit as logically necessary. That is false even assuming the proposed inequality: a bound on the difference of valuations could suffice. Its leading-term theorem still requires an exact hypothesis/quotient audit before being used to prove finiteness. No such joint bound or audit was obtained here.

The revised RESULT still says finiteness of Sha[p] cofinitely is open. Each fixed p-torsion group is finite as a quotient of a finite p-Selmer group. The desired assertion is cofinite vanishing, plus primary finiteness at the remaining exceptions. We make no new universal literature claim concerning all rank-two curves.
