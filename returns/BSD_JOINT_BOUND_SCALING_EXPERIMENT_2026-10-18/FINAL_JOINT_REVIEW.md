# Independent final review:11a1 at coefficient7

Verdict: **the complete ordinary faithful-character unit kernel is zero under the retained field, full-image and descent-source inputs.** This is supported by actual new arithmetic. It is not a whole-source or seed bound; no class-completeness certificate succeeded.

I reviewed the coefficient-local deduction in LOCAL_CONDITION_REVIEW.md, its explicit11a1 binding in local_rank/PROOF.md and REPORT.md, and the independently reconstructed affine rows in INDEPENDENT_11A1_JOINT.json/check_11a1_joint.py. I had separately authenticated the actual26 compact source units using complete principal ideals and checked that their exact integer exponents and field/point/scalar data match the evaluator. This review retains the earlier field/maximal-order and Schaefer–Stoll source identifications, rather than recertifying that entire antecedent chain.

## Why the numerical minor gives a complete unit bound

Let U be (O_A^*/O_A^{*7})^chi for the actual degree48 nonzero7-torsion point field A. Under the retained full GL2(F7) framework, its dimension is4. In the Dirichlet logarithmic representation the faithful-character part on nonzero torsion points has dimension8; complex conjugation fixes a4-dimensional subspace. Subtracting the trivial character has no effect on chi. A contains no seventh roots of unity: the vector stabilizer has surjective determinant, so the cyclotomic degree6 subfield is not contained in its fixed field. Thus no additional7-torsion unit term is missing.

The26 columns are actual units, not merely BNF-reported candidates. The character projector is an integral lift of the mod7 idempotent; every projected column remains an actual unit class in U. The evaluator binding preserves all original integer exponents. A rank4 map evaluated on these columns therefore has rank4 on U itself. Neither fundamental-unit completeness nor class-group completeness is used in this argument. This is the decisive distinction from a detector on an incomplete source of unknown dimension.

At q=4831 the independent affine-line reconstruction supplies three necessary global rows and a fourth coefficient-local row. On columns0,1,16,23 the matrix is

    [6 1 5 6]
    [3 2 0 4]
    [0 4 2 4]
    [2 4 4 3].

I recomputed its integer determinant by the24 permutation terms: -214, hence3 mod7. The same reconstructed dataset has global rank3, local rank1 and joint rank4 at both recorded local precisions. The three affine rows alone leave a line; the local row removes it. The whole-source class term has not been used to manufacture this rank.

## Admission of the local row

A direct point count on [0,-1,1,-10,-20] gives #E(F7)=10, so the curve has ordinary nonanomalous reduction. This is its own11a1 check, not the389a1 trace reused. The actual universal-point valuations(-2,-3) identify the prime of local degree6 and residue degree1 as the formal torsion branch; the other recorded branch has integral point coordinates. The scalar map fixes the formal prime.

Every local point class can be represented by the formal group because the reduction order is prime to7. Its Kummer cocycle can be chosen in the formal torsion line V+. Weil evaluation against its nonzero formal point T annihilates V+. Therefore every actual Selmer source evaluates to a seventh power in Q7(T). This necessary direction alone is sufficient to use the row for an upper bound; the stronger converse in the root note is not required.

At ramification index6, every element of1+P^8 is a seventh power: apply the logarithm, divide by7 (leaving valuation at least2), then the exponential, whose convergence threshold is strictly greater than1. Thus the P^8 unit quotient detects the complete local seventh-power obstruction, not a stronger artificial test. P^9 supplies an arithmetic consistency check. Compact factors' valuations cancel with their exact integer exponents, so stripping a common uniformizer before taking local logs does not drop any term from the resulting actual units. The source-normalization identification remains an explicit retained assumption.

The affine split-prime rows are also necessary for genuine cohomological sources: evaluation of a Frobenius cocycle through the Weil pairing is a linear function on E[7], and every affine-line sum of such a function is zero in F7. The independent calculation reconstructs the actual torsion labeling instead of treating a random permutation of residue roots as an arithmetic affine structure.

## Scope that must remain attached

The conclusion is ker((G,L)|U)=0 for these authenticated necessary screens. It leaves class-supported source elements possible: a nontrivial ordinary class can have a lift whose unit correction satisfies the joint equations. Zero unit kernel makes such a correction unique when it exists; it does not prove no such class exists.

The new11a1 BNF is provisionally class1, but quotient-only certification hit its57.911-second alarm. GP's exitcode0 was correctly rejected. Hence no unconditional ordinary-class-zero or full-source-zero conclusion follows. The finalized primitive divisor calculation now establishes zero valuation contribution, as checked below. Conditional on completeness of the provisional ordinary-class presentation, the containing source is therefore zero. An S-class statement may not substitute for the ordinary class term.

The result concerns a rank-zero control, though no rank or Sha value was used to construct the units, rows or bound. It demonstrates actual joint rejection of a4-dimensional unit space at a larger coefficient prime. It is neither a result for the rank-two seed nor a bound across infinitely many coefficient primes. FIN, ORDER9 and Q36 remain unchanged.


## Finalized primitive divisor layer and class injection

I read small_conductor_divisor/PROOF.md and ACTUAL_DIVISORS.json and checked their combination with the final root PROOF.md and REPORT.md. At7 the two prime ideals have(e,f)=(6,1),(7,6), each fixed by the actual scalar automorphism, so both faithful character spaces are zero. At11 the actual scalar permutation has one6-cycle and one2-cycle; its chi3 and chi5 eigenspaces each have dimension1. Their supplied eigenvectors satisfy the literal permutation equations, and all recorded degree sums equal48.

The local curve calculation gives split multiplicative typeI5. Its monodromy coefficient5 is a unit modulo7, so the inertia group is the full unipotent group of order7. The decomposition group generated by it and diag(4,1) has order21. Independently rebuilding its point and covector orbits gives the recorded point decomposition: six(7,1) orbits and two(1,3) orbits. On the covector side there are six singleton orbits(0,b) and two(7,3) orbits.

I also rebuilt the primitive incidence entries using normalized valuations. For every target singleton(0,b), exactly the source orbit with y=b^(-1) has an incidence fibre of size7. Its source ramification index is7 and target ramification index is1, so the coefficient is(1/7)*7=1. The resulting6-by6 submatrix is a permutation matrix. The other source orbits have scalar stabilizer of order3 and no faithful component. This proves injectivity on the faithful divisor line without dropping a ramification factor. See FINAL_DIVISOR_REVIEW.json for the independently reconstructed orbit types, actual character dimensions and matrix.

Thus t_D,chi=0 on S={7,11} is supported under the retained field, Tate-uniformization and source inputs. For K defined by the ACTUAL incidence-norm condition and the necessary coefficient-local condition, its valuation vector must lie in this zero kernel. It follows that K lies in the ordinary virtual-unit source H0. The standard exact sequence

    0 -> U_chi -> H0 -> Cl(A)[7]^chi -> 0

maps a class represented by a with div(a)=7D to[D]. Since the independently checked joint unit kernel is zero, its restriction to K is injective. Therefore the final root claim

    K injects into Cl(A)[7]^chi

has the correct direction and requires no class-completeness assumption. Replacing the actual norm condition by only the finite residue rows would not by itself establish the zero valuation claim; the root definition of K correctly retains the actual norm.

The injection exposes the entire surviving class contribution. It does not bound it, prove it nonzero, or justify discarding class lifts that become S-units. No unconditional whole-source or seed result has been added by this final review.

Final definition clarification: at the parent's request, root PROOF.md now explicitly defines A(S,7) by divisibility of valuations outside S={7,11}, and K as its faithful-character subspace satisfying the actual incidence-norm seventh-power and coefficient-local conditions. This is the source to which the reviewed valuation and class injection apply. The final root proof and report hashes are bound in FINAL_JOINT_REVIEW_BINDINGS.json.
