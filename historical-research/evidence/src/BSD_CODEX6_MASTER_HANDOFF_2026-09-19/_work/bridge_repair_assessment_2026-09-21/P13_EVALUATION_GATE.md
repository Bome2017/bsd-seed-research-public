# Next executable arithmetic target: the certified C13 unit test

2026-09-21. **THEOREM_AND_CUTOFF_GATE_PASS_NO_ARITHMETIC_RUN.**

The next executable finite-primary operation is the existing cyclotomic test at 13. It uses the same certified modular-symbol engine and implication as the completed 7- and 11-primary computations. The newly certified twist remains useful to the separate Heegner comparison, but that comparison still lacks an independent method to evaluate its specialized ideal. A characteristic ideal alone cannot supply it, by the existing counterexample. No new evaluation method for that ideal was established by this gate.

## Admission and exact endpoint

* **Endpoint:** prove Sha(E/Q)[13^infinity]=0, if the sufficient test succeeds. Full FIN, ORDER9 and Q36 remain separate.
* **Independent new input sought:** the mod-13 quadratic coefficient C13=[T^2]L13(E,T), evaluated by certified modular symbols. This is a finite arithmetic calculation independent of Sha, already implemented at 7 and 11.
* **Implication:** C13 nonzero implies the analytic and characteristic series have order two with unit leading coefficients, then finite 13-primary Sha and a nondegenerate height; regulator integrality and unit local factors give Sha[13^infinity]=0.
* **Collision check:** this reuses a completed fixed-prime method. It does not assert a new uniform-tail mechanism, identify cyclotomic C13 with the anticyclotomic I3, or need to settle the auxiliary twist's 13-part. No difficulty reduction for full FIN is claimed.
* **Stopping condition:** a rigorously obtained zero leaves this unit test inconclusive. It supplies neither nonzero Sha nor permission for an automatic deeper-level or next-prime run. A certification or resource failure is an execution blocker, with saved checkpoints.

## Specialization of the retained theorem

The [completed C11 implication](../active_full_bsd/p11/PROOF.md) and [P7 proof](../../audits/P7_PRIMARY_THEOREM.md) apply with these replacements:

\[
\#E(\mathbf F_{13})=18,\quad a_{13}=-4,\quad
\alpha\equiv9\pmod{13},\quad\alpha^{-2}\equiv9,\quad
(1-\alpha^{-1})^2\equiv4.
\]

The retained full odd residual-image theorem supplies full 13-adic image. The symbols have the same prime-to-13 lattice denominator 1024. Kato's integral good-ordinary divisibility and the rank lower bound therefore apply. These source statements were re-read in the retained Stein--Wuthrich text, Proposition 3.5 and Theorems 6.1 and 7.3; this is source specialization, not a new audit of their proofs.

All torsion and Tamagawa factors are 13-units. Multiplication by 36=2*18 sends each rational point to all identity components and to the formal group at 13. The retained canonical sigma-height argument gives height entries in 13 Z13, and v13(log13(14))=1 gives Reg_gamma in Z13. If C13 is a unit, the established leading-term formula thus reads
\[
0=v_{13}(\#\Sha[13^\infty])+v_{13}(\operatorname{Reg}_\gamma),
\]
after finiteness has been deduced, not assumed. Both terms are nonnegative. This proves the stated sufficient implication with the existing source, basis, Manin and software qualifications.

## Predeclared arithmetic functional

Put S_b=[b/169]^+ in the retained omega1 normalization and
\[
j(b)=-\frac{b^{12}-1}{13}\pmod {13},\qquad 0\le j(b)\le12.
\]
The lower-level quadratic contribution is zero modulo13 because the sum of binomial(j,2), j=0,...,12, is 286. Therefore
\[
C_{13}\equiv9\sum_{b\in(\mathbf Z/169)^\times}\binom{j(b)}2S_b\pmod{13}.
\]
Folding S_b=S_(169-b) leaves 66 nonzero weighted entries among b=1,...,84. [The exact preparation script](P13_EVALUATION_GATE.py) independently derives all weights both from Fermat quotients and Teichmuller enumeration and stores their full predeclared lists in [P13_EVALUATION_GATE.json](P13_EVALUATION_GATE.json). No symbol value or residue has been guessed or computed. A one-functional optimization is not assumed; the unchanged full engine remains the available certified implementation.

## Resource gate and execution scope

The unmodified, byte-checked Arb cutoff calculation gives:

| Target denominator | Cutoff rounded to whole segments | Segments | Existing segments available | New segments needed |
|---|---:|---:|---:|---:|
| 169 | 55,046,045,695 | 3,281 | 2,333 | 948 |
| 13 | 4,026,531,839 | 240 | 240 | 0 |

The lower denominator supplies the retained independent Hecke checks. These cutoffs use the existing uniform lattice-identification error criterion; an actual run must still pass its ball, unique-lattice-point, coverage and downstream checks.

The coefficient producer, independent witness verifier, table-free Arb engine and restart/checkpoint pipeline already exist locally. Their ten retained identities passed this gate. Reuse at launch must freshly verify all reused coefficient and verifier bytes; this gate did not rehash the whole corpus. No new engine is needed. Aristotle's 32 GB does not supply its missing local coefficient corpus; a new remote package is unnecessary for this calculation.

The recent C11 segments contain about 21.7 MB each of coefficient and witness data, giving an approximately 19.2 GiB storage anchor for 948 more segments, not a proven disk upper bound. About 96.5 GiB was free during the check. Preserve the existing disk floor and stop safely if it is reached. The C13 runtime has not been benchmarked and is not inferred from the twist's 708-second run. No coefficient generation or modular-symbol run was launched by this planning gate.

If the test succeeds, the retained conditional next-order threshold changes from 9*13^2=1521 to 9*17^2=2601 under FIN. The present threshold remains 1521 because C13 is uncomputed. This is an actual possible primary theorem, not completion of full BSD or evidence for eventual prime vanishing.

## Returned scope note

The new external [SCOPE_AT_13.md](/Users/bsm/BSD_TWIST_D23_CERTIFICATE_2026-09-21/SCOPE_AT_13.md) correctly identifies the odd-primary decomposition over K and the conjunction tested by I3. Restriction/corestriction gives the invariant part and twisting gives the anti-invariant part; multiplication by two is invertible on these groups. Its sentence that bounding the twist's 13-part *is* a separate Heegner-index computation is too exclusive: that is one possible method, not a proved necessity. The seed's direct cyclotomic test above avoids that auxiliary obligation entirely. No claim that the two coordinates are equal follows.
