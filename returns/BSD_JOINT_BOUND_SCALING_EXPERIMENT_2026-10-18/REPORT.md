# Actual joint upper-bound experiment at coefficient seven

2026-10-18. Status: **ACTUAL_P7_COMPLETE_UNIT_JOINT_KERNEL_ZERO_ON_CONTROL; CLASS_CONTRIBUTION_RETAINED; NO_SEED_BOUND**.

This run executes the joint global/local proposal. It changes an unsuccessful source rather than continuing to add rows to it. The successful arithmetic is on 11a1 at coefficient 7, a rank-zero control in the same full residual-image framework, not on the rank-two seed or the earlier rank-two 389a1 control. No known Selmer or Sha value was used to construct its source or rows.

## 1. The measured improvement

The ordinary faithful-character unit space for the degree-48 point field has dimension 4. Twenty-six compact units were constructed and exactly authenticated. Their projected residues have rank 4, so they span that entire mod7 unit component without assuming the BNF supplied a fundamental-unit basis.

At each of the three actual fully split auxiliary primes 4831, 22051, 78583, the global affine-norm residue map has rank 3 on these units. An actual coefficient-prime Kummer condition has rank 1, independent of those three rows. The stacked rank is4. Therefore

\[
\boxed{\ker(\text{global norm conditions},\text{local Kummer condition})\cap U_\chi=0.}
\]

This is an upper bound on the ENTIRE ordinary character-unit space, not detection of known classes or the kernel of an incomplete list. It requires neither class completeness nor a known Sha value. It is a written/computer-assisted deduction under the retained representation and descent-source inputs, not a proof-assistant or external-human certification.

The root's separate multiplicative evaluator uses a new torsion basis and affine-line sums. At q=4831, four projected units (indices 0, 1, 16, 23) give the minor

\[
\begin{pmatrix}6&1&5&6\\3&2&0&4\\0&4&2&4\\2&4&4&3\end{pmatrix},
\qquad\det=-214\equiv3\pmod7.
\]

The first three rows are norm residues. The last row is the coefficient-prime condition. Separate successful minors occur at the other two primes. The producer's additive-function extraction and this direct norm extraction agree on rank; they are independent extractions from the same exact field and units, not independent constructions of the field.

## 2. The local condition is actual, not a geometric surrogate

For 11a1, #E(F7)=10 and a7=-2. Its ordinary nonanomalous Kummer condition is the formal-line condition. Evaluating the descent source at a formal 7-torsion point gives a necessary local seventh-power condition. The formal branch of the actual field is identified by the valuations of the universal point, not only by degree.

The calculation uses the actual quotient of units modulo P^8 and seventh powers, with a replay modulo P^9. Since the ramification index is6, every1+P^8 element is a seventh power by logarithm/exponential: division by7 leaves valuation at least2, above the convergence threshold1. Thus the extra row is not an insufficient-precision zero/nonzero heuristic. Compact-factor valuations are cancelled using a common uniformizer and the exact integer exponent relations.

On already genuine global cohomology, this local condition contributes at most one independent dimension. Its success here does not make its rank grow indefinitely with p.

## 3. Class and valuation directions are not omitted

The actual prime decompositions and primitive incidence calculation give zero surviving valuation allowance on S={7,11}. At 7 there is no faithful divisor component. At11 the source faithful divisor line maps with a7-adic unit, retaining the ramification correction. See small_conductor_divisor/.

Consequently, after the joint unit kernel is zero, any surviving complete-source class injects into the ORDINARY faithful7-class contribution. We have not certified that contribution is zero. The BNF reports class group1, but a quotient-only certification attempt hit its explicit alarm without a success marker. The complete-source-zero conclusion is therefore available only conditionally on completeness of that provisional class presentation. It is not claimed unconditionally.

This separates the two experimental results: the growing unit space has been fully controlled on this coefficient 7 control; the independent full class contribution remains unbounded. A relation matrix on finitely many represented ideals does not remove unseen classes.

## 4. Why the source was changed

On 389a1, the new method constructed units by cancelling complete principal divisors across many scalar translates. The first batch gave 99 integral relations; unlike the previous pairwise search, these were genuine multi-element relations. Exact simplification showed all products were +/-1. A second mixed-parity/smooth-norm selection and the combined cached source were tested. The final 342 factors collapse to 157 distinct elements up to sign, with divisor rank 157 and 185 relations, all again trivial. This is a scoped failure of those finite families, not absence of units in the field.

The source was then changed to the smaller-discriminant11a1 point field at the same coefficient 7. Exact torsion/field/scalar checks completed, and BNF produced compact candidates in about 12 seconds. All 26 products were independently authenticated by 144 factor ideals and 116 prime-ideal rows. Unit authentication succeeded; class certification did not. The source change and computational budgets were recorded before the new calculations.

We also checked a tempting map substitution before developing it: at one fully split prime, complete additivity equations and all affine-norm equations have the same residue kernel. Exact checks at 3, 5, 7, 11, 13, 17 match the source's coefficient-module sequence. Adding those duplicate equations cannot create extra rejection. The successful added row instead comes from the coefficient prime itself.

## 5. What this says about scaling toward the seed

The experiment now demonstrates actual complementary global and local ranks at a coefficient prime larger than 5. It supports a specific mechanism for bounding a whole unit contribution: three independent norm directions plus one independent local direction exhaust a four-dimensional arithmetic unit space.

It does not establish this rank profile on the seed, on rank-two 389a1 at 7, or for varying p. In particular, a rank-zero control has no two-dimensional point plane that must survive; its zero bound cannot be transferred to the seed. The successful p5 and p7 experiments use different curves. They are not a uniform-in-p computation for one curve.

The next genuinely arithmetic comparison would need enough admitted units on a rank-two source, plus an independently bounded complete class source or class-lift obstruction. The available 389 families failed to supply those units; the 11a1 class certificate remains incomplete. These are the actual computational limits reached here. Neither a detector nor a provisional class table is substituted for the missing bound.

FIN, ORDER9, Q36 and seed coefficient-prime coverage remain unchanged. This packet records a completed larger-prime joint UNIT upper bound, the class qualification, the unsuccessful source families, exact replay code and separate same-team review.
