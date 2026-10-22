# Independent character-bound review

2026-10-17. Scope: `general_character/PROOF.md`, `LOCAL_DIVISOR_PROOF.md`, and the two scripts, within the sealed 2026-10-15 experiment. This is a desk review and exact finite-algebra replay, not a fresh certification of any number-field class group, of full residual image, or of the prior arithmetic equivalence/class-number theorem.

**Verdict: the global source-only upper bound and the primitive divisor formula pass under their stated retained arithmetic inputs. The characterwise geometric index must not be substituted for the actual unit index.** No new seed prime or endpoint follows from this review.

## 1. The whole-source upper bound

Let `V_A,S = A(S,p)^chi`, and write `D_A,S` for the free module on all primes of A over S. The valuation homomorphism sends a class to its valuations modulo p. Its kernel is the ordinary virtual-unit group `V_A,empty`; it does not have to be represented by an ordinary unit. The latter distinction is precisely the class-supported contribution.

For `K = ker(u:V_A,S -> V_B,S)`, compatibility of norm and valuations gives

    valuation(K) subset ker(u_D mod p).

The identities `vu=uv=p` on the character lattices imply that the elementary divisors of `u_D` are only 1 and p. Consequently its mod-p kernel dimension is exactly `t_D,chi`, not merely bounded by its cokernel length. The kernel of the restricted valuation map is `K intersection V_A,empty`. The ordinary virtual-unit sequence gives

    0 -> O_A^*/O_A^{*p} -> V_A,empty -> Cl(A)[p] -> 0.

The chi-part of the first term has dimension `(p+1)/2`. Thus

    dim K <= (p+1)/2 + dim Cl(A)[p]^chi + t_D,chi.

This bounds all global admitted classes, including classes not present in a sampled list. It uses the ORDINARY class group. Replacing it by the S-class group at this step would be wrong.

Roots of unity have not been lost: under the full-image hypotheses the point and covector fields have real embeddings (complex conjugation has a nonzero fixed vector/covector). They therefore contain no odd-primary roots of unity. The tensor/completion and unit reduction introduce no extra p-torsion term. The rank follows from equivariant Dirichlet: each odd scalar component of the embedding permutation representation has complex-conjugation invariant rank `(p+1)/2`; the trivial unit summand affects only the trivial scalar character.

## 2. S-units, class quotients, and inverse characters

The retained internal scalar pullback convention gives

    u sigma_a^A = sigma_(a^-1)^B u.

Hence every target class/unit/divisor component in a characterwise statement is `chi^-1`, not chi. The scalar idempotent denominator p-1 is a p-unit.

Let `J_A` be the valuation lattice of S-units in `D_A,S`. Then

    length(D_A,S/J_A) = c_A,chi - c_AS,chi.

For the induced map `J_A -> J_B`, its cokernel length is

    t_D,chi + (c_A,chi-c_AS,chi)
              - (c_B,chi^-1-c_BS,chi^-1).

Combining with the unit map proves equation (1), including its signs. The Kummer diagram gives equation (2) as an inequality because not every class-map kernel element has an admitted virtual-unit lift. No surjectivity of that projection is needed.

## 3. Primitive divisor weights

Fix a prime of the common torsion splitting field K. For a D-orbit P of vectors and Q of covectors let e_P and e_Q be their inertia-orbit sizes. Since the normalized valuation on K restricts to `(abs(I)/e_P) v_P`, taking the product over `lambda(x)=1` gives

    u_D(Q,P) = (e_Q/e_P) * #{x in P : lambda(x)=1}.

The ramification factor is necessary. The producer's p=5 multiplicative model has fiber count 5 and e_Q/e_P=1/5 on the relevant characters, giving a unit map. Counting the fiber alone would incorrectly introduce a factor 5.

I replayed the exact model and separately read its construction: both the scalar convention and the primitive orbit valuation normalization are consistent. The actual 389 local arithmetic and the actual prime/scalar decomposition in the other lane are retained inputs to using this finite model for the number field.

## 4. Geometric index and the counterlattice

Modulo p the geometric incidence matrix has entries `(lambda(P))^(p-1-k)`. The polynomial-evaluation factorization has rank p-k; on complex-conjugation invariants its kernel dimension is `(k+1)/2`. The integral compositions are pI, so these dimensions are the geometric indices. The supplied p=5,7,11 executions replay exactly.

This is not an arithmetic unit-lattice calculation. The countercontrol is valid: keep source lattices M_1,M_3 and replace matched targets by `u(M_1)` and `p^-1 u(M_3)`. These are G-stable integral lattices in the same rational representations. The reverse maps remain integral because `vu=p`. Their invariant forward indices are 0 and 3, although the original geometric indices were 1 and 2. The aggregate remains 3. Thus neither the rational representation, the composition pI, nor the aggregate determinant determines the desired character index.

The full-minus formula is retained from the earlier arithmetic-equivalence/regulator proof, not newly re-certified here. Its use to sum over odd characters is consistent with this countercontrol. A new integral comparison of actual unit lattices would still be needed for a characterwise constant-one class-number formula.

## 5. A legitimate further sharpening

See `CLASS_MAP_BOUND.md`. The actual ideal-class correspondence can replace the full source p-class rank by the dimension of its kernel. This is an upper bound on the whole class-supported contribution, not a detector on chosen representatives. It requires the actual class map or a certified rank lower bound for that map. None is computed in this review, so it does not improve the current seed numerical bound.

## Sources and grading

Freshly opened Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf. The notation on printed page 4 confirms the central-character convention; the global source theorem is retained from the prior source audit. The Kummer exact sequences and index manipulations above are explicit deductions.

Read the earlier `INCIDENCE_NORM_REVIEW.md`, including its distinction between full minus and a single scalar character. Did not independently re-audit the class-number formula or Torzewski's paper in this review. No novelty or formal-verification claim. FIN, ORDER9, Q36 unchanged.
