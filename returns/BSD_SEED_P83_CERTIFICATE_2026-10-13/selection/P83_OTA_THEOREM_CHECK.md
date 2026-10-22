# Actual unresolved seed certificate: coefficient 83, auxiliary 167

Date: 2026-10-13. Status: **THEOREM_ELIGIBLE_UNDER_RETAINED_INPUTS; WITNESS_NOT_COMPUTED_HERE**.

This is a fresh primary-source application check and independent small arithmetic, not a certification of an unevaluated numerator. It imports the project's rank, image, Tamagawa, period and modular-symbol custody inputs at their existing grades.

## 1. Source statement

Ota, *Kato's Euler system and the Mazur–Tate refined conjecture of BSD type*, [arXiv:1509.00682v1](https://arxiv.org/pdf/1509.00682), freshly opened and text-checked in this run: §1.2 pp.2–3, Theorem 5.17 p.36, and Theorem 6.4 pp.37–38. Under its prime-to-6N, non-anomalous, Tamagawa and full Tate-module-image hypotheses, a nonzero rank-r leading augmentation term at an admissible squarefree conductor implies Sha[p]=0. A good auxiliary prime is admissible here if it is 1 modulo p and its reduced p-torsion is cyclic. Theorem 5.17 gives augmentation order at least the Mordell–Weil rank. No primary-finiteness premise or conjectural tame-regulator identity is imported. Definition 2.1 and Remark 2.2 distinguish the full-group normalization from the half-normalized real-group convention.

## 2. Every local hypothesis at 83/167

The seed is `y^2=x^3-22735x^2+106272484x`, with retained conductor
`N=6503188012738584=2^3*3*2243*4547^2*5843`.

| Hypothesis | Evidence |
|---|---|
| coefficient p=83 prime and p>=rank=2 | direct primality test; rank two retained |
| p does not divide 6N | gcd=1, recomputed |
| p does not divide any Tamagawa number | retained product16, gcd(83,16)=1 |
| p does not divide #E(F_p) | fresh exact count92; a83=-8 |
| good reduction at p | p does not divide retained conductor |
| full action on T_83E | retained residual-image theorem A.3 and its p>=5 integral lifting argument |
| no complex multiplication | retained; also follows from full image |
| ell=167 good, distinct from p | primality and gcd(167,83N)=1 recomputed |
| ell=1 modp, v_p(ell-1)=1 | 166=2*83 |
| E(F_ell)[83] cyclic | actually zero: fresh #E(F167)=168; trace a167=0 |
| modular-symbol p-integrality | matched retained symbol lattice (1/1024)Z, 83 does not divide1024 |

`check_p83.py` recomputes both point counts by two exact methods, direct point enumeration and quadratic-residue counting. It computes the smallest primitive root g=5. These are small arithmetic checks, not modular-symbol computation. Ordinarity at83 is true but is not the relevant restriction in this Ota application. Supersingularity at auxiliary167 is allowed.

The full-image hypothesis is genuinely p-adic. The master map lines98–99 explicitly retain the lifting argument and period/Manin qualifications. This check does not independently reconstruct that universal theorem or erase its grade.

## 3. Exact coefficient to calculate

Use the frozen pipeline plus symbols `s_a=[a/167]^+` in its authenticated omega1 convention for every 1<=a<=166. Let

`x(a)=ind_5(a) mod83`, represented in {0,...,82},

`c_k=sum_(a=1)^166 binom(x(a),k)*s_a`, k=0,1,2.

The target is `c2 mod83`, with c0 exactly zero and c1 zero modulo83. In F83[C83]/(T^3), T=sigma-1, this is the actual expansion of the projected group-ring element; no regulator enters its computation. Since x(-a)=x(a), the minus symbols cancel and the plus projection is the relevant one. The retained Ota/pipeline period comparison and the possible real-group factor1/2 are units at83. Thus nonzero is independent of these already matched unit conventions. A new unexplained factor83 is not allowed.

If a table is represented as integers n_a=1024*s_a, use the inverse of1024 modulo83 for coefficient reduction; do not round the resulting residue or silently change to a predicted scale. The certified interval stage must first identify every symbol uniquely in the fixed lattice, with every input coefficient segment covered by the authenticated receipts. Hashing output files does not replace that arithmetic check.

The actual binomial coefficient is x(x-1)/2, not x^2 without proving cancellation of c1. Changing the primitive root to g^u rescales c2 by u^(-2) when c0,c1 vanish; fixing g=5 avoids an unnecessary comparison.

## 4. Fail-closed outcome

1. All input coverage, interval/lattice identification, symmetry, curve/model and normalization checks pass; c0=0 and c1=0mod83; **c2!=0mod83**: Ota implies Sha(E/Q)[83]=0. Any nonzero83-primary group has an element of order83, so this proves **Sha(E/Q)[83^infinity]=0** without prior finiteness.
2. Same checks pass but c2=0mod83: this auxiliary is inconclusive. It does not prove Sha nonzero or invalidate the seed conjecture.
3. Any source, completeness, arithmetic or consistency check fails: INVALID/NO_VERDICT; not a zero coefficient.

No comparison with `288*(a167-2)*R_83,167` is part of acceptance. Any prediction belongs in a sealed diagnostic file excluded from the certificate computation and checker. A mismatch cannot be repaired by changing normalization after the result.

## 5. Endpoint effect

The current canonical record does not list coefficient83 as settled. A successful fresh83 certificate would add a genuine base-field primary vanishing result. It would not raise the conditional next-order floor25281, because53 remains unsettled. It would not prove the infinite tail, FIN, ORDER9 or Q36.

This application is independent of the newer Kato-content formula's exclusions19/59/487. Those exclusions are not Ota exclusions; conversely Ota cannot be extended to bad coefficient primes2243/4547/5843 by this argument.

## 6. Retained file bindings

- `BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md`, retained rank, conductor, full image, lattice/Manin facts and unresolved endpoint ledger.
- `BSD_P53_L743_RUN_2026-10-01/FROZEN_RUN_PACKAGE_p53_l743/THEOREM_PROFILE.md`.
- Same package `spec/SINGLETON_SPEC_v1_audited.md`, especially sections1–3 and7.
- `BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/CURRENT_STATE.md`, read in this run; no83 coverage listed.

The p53 implementation and frozen acceptance contract are precedents; they must be bound to the new p83/ell167 parameters and new output. Reusing a p53 success label is not a83 certificate.
