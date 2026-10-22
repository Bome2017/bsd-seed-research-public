# Independent proof review: completeness, invisible kernels, and common-point repair

Date: 2026-10-15. Scope: read-only audit of retained source/matrix facts and the proposed mathematical criterion. No new field arithmetic or remote job. The proposed seed pair 1213,1543 was **not evaluated by this reviewer** before the parent's seal; its selection used only their already-published point-image ranks.

## 1. The exact finite certification criterion

Let S=Sel₃(E/Q) and W=κ(E(Q)/3E(Q)). A certified complete descent source provides an injective realization of S in a finite vector space A=F₃ⁿ. Let C be a matrix of **necessary** arithmetic conditions on that source, and put U=ker C. The hypotheses needed for the argument are

    W ⊂ S ⊂ U ⊂ A.

Completeness means every true Selmer class has a coordinate in A. Independence of displayed source elements or of a list of known Selmer classes does not establish completeness.

Let D be a source-evaluation matrix whose rows kill W and whose induced map on S is an authenticated arithmetic detector. Compute

    Z = U ∩ ker D.

If Z=W, then ker(D|S)=W. Consequently D is injective on S/W=Sha[3]. This is a valid upper-control certificate on the invisible kernel. It does not require U=S and does not require that all elements of U are genuine Selmer classes.

It also does **not** imply Sha[3]=0: nonzero images can remain. The resulting bound is dim Sha[3] ≤ dim of the authenticated target, or the smaller rank of D on U. If k independent known excess classes attain an independently established upper bound k, that closes the fixed-prime dimension calculation.

If a span K of independently authenticated true classes contains W and equals U, then W⊂S⊂U=K⊂S, so S=U. This is a different way to certify completeness of the **admitted** space. It must not be confused with source completeness or with detector injectivity.

Necessary-condition rows and detector rows have different semantics. C annihilates every true class. D deliberately need not annihilate a true excess class. Appending D to C computes the *invisible* Selmer kernel, not the full Selmer group. Calling that new kernel “Selmer” would silently discard the excess the experiment was designed to see.

## 2. A stronger experiment: one common global-point repair

The existing detector at each q uses

    d_q : S/W → K_q / loc_q(W),

where K_q is the local 3-Kummer image. These per-prime quotients allow a **different** global-point combination w_q at every place. There is a stronger, still elementary arithmetic map for a finite prime set Q:

    d_Q^diag : S/W → (⊕_{q∈Q} K_q) / loc_Q(W).

The denominator is the diagonal image of one global point class. The map is well-defined because changing a Selmer representative by w∈W changes the full tuple by loc_Q(w). This is still a map on Kummer lifts; the associated torsors remain locally trivial in H¹(Q_q,E).

There is a natural surjection from the diagonal quotient to the product of the individual quotients. Therefore

    ker d_Q^diag ⊂ ∩_{q∈Q} ker d_q.

The inclusion can be strict. This is not additional global source admission; it asks whether the same point coefficients explain all the admitted local values.

### Exact matrix construction

For each q let M_q:A→F₃⁸ be the actual source-character matrix, and let W₀ contain the full global-point source columns. Stack M_q vertically into M_Q. Compute a full left annihilator L_Q of M_Q W₀, and put

    D_Q^diag = L_Q M_Q.

Use one annihilator of the stacked point matrix. Stacking the old separate annihilators computes the weaker product quotient instead.

On the containing source U, the exact invisible kernel is

    Z_Q^diag = U ∩ ker D_Q^diag
             = W + (U ∩ ker M_Q).

Indeed, D_Q^diag(x)=0 says M_Q(x)=M_Q(w) for some w∈W; since W⊂U, x−w lies in U∩ker M_Q. This equality makes an independently checkable rank/kernel test, without using known excess labels to define the rows.

For true classes, the effective target dimension is

    Σ_q dim K_q − rank(loc_Q W).

At two good completely split primes, dim K_q=2. With rank-two W and injective point localization, this target has dimension two even if **each individual quotient is zero**.

### Specific sealed candidate

The saved seed blocks at q=1213 and q=1543 each have point-image rank two. Thus their individual point quotients vanish on every genuine Selmer class. They are appropriate controls for the diagonal construction precisely because the old detector is blind there.

At each such q, write the two point columns P_q and the two named excess columns B_q in any injective local coordinates. There is a unique 2×2 matrix T_q with

    P_q T_q = B_q.

The two-prime excess detector is equivalent to

    T_1543 − T_1213.

If its determinant is nonzero, one common point vector cannot explain any nonzero combination of the two excess classes at both primes. If its rank is one or zero, preserve the corresponding actual invisible combination and test the next predeclared block. These are independently computed point-coordinate comparisons, not a determinant whose entries are defined by a Sha order. The coefficients T_q live in the fixed global point basis: changing the local torsion coordinates, root ordering or cubic-character coordinate acts simultaneously on P_q and B_q and leaves T_q unchanged. Thus subtracting the two T_q needs no identification of the two local torsion bases. A global point-basis change or excess-basis change only multiplies the difference by invertible matrices.

This experiment changes the repair condition and can find information unavailable in every individual quotient. Its outcome does not certify an upper bound unless source containment/completeness and the full-kernel test in §1 are also supplied.

## 3. What joint evaluation proves about eventual detection

Assume full residual image GL₂(F₃) and the retained explicit-descent realization. For independent genuine cohomology classes c₁,…,c_d, the joint cocycle image over Q(E[3]) is V^d, V=E[3]. The reason is exact:

* the central scalar −I kills H¹(GL₂(F₃),V), so restriction is injective;
* a proper G-submodule of V^d would impose a nonzero scalar linear relation among the restricted classes, because V is simple and End_G(V)=F₃;
* that contradicts their independence.

Chebotarev therefore supplies split primes with any allowed joint translation pattern. For ξ∉W, one can in particular choose a pattern with every point direction zero and ξ nonzero. Hence

    ∩_{all eligible split q} ker(d_q|S) = W.

The diagonal family is at least as strong and has the same intersection. Since S/W is finite-dimensional, some finite subcollection is injective. Enumerating eligible split primes and retaining all rows therefore terminates **as a fixed-p kernel-separation procedure on the full true S**. The theorem gives no effective last prime and no bound on the number of primes tested before termination.

### Finite separating collections, including individually blind primes

There is a more explicit existence statement, conditional on the same joint-evaluation and local-realization inputs. Write d=dim S. Each eligible good split prime evaluates S into the two-dimensional unramified local Kummer space V. Prescribe k=ceil(d/2) translation matrices of size 2×d whose vertical stack has column rank d. Joint evaluation and Chebotarev realize each prescribed matrix at a distinct eligible prime, up to simultaneous invertible change of its local V coordinates. Those changes do not alter the stacked column rank. The resulting localization map on S is injective, so its quotient by the one diagonal image of W is injective on S/W.

For rank-two W, the construction can require that **every individual point quotient is blind**. Write d=2+s and choose a basis beginning with the two point directions. Set k=1+ceil(s/2)=ceil(d/2). Prescribe the first local matrix as [I₂ | 0]. Prescribe each remaining matrix as [I₂ | B_j], where the stacked B_j select all s excess coordinates in successive pairs. Subtracting the first block from every other block shows that the full stack has rank 2+s. Yet the point image in each individual block is all of V, so its individual quotient is zero. All the separation is in the inconsistency of the *common* point repair.

Chebotarev specifies a conjugacy class, not a preferred local basis. On a pure translation its conjugation acts by a common element of GL₂(F₃) on the two rows of that block. This preserves both point-fullness and the point-repair matrix, so it does not spoil the construction. Finitely many bad or ramified primes can be excluded throughout.

This is an existence bound on the size of a suitably chosen collection **in terms of the unknown dimension d**. It is not a bound on d, not a bound on Sha[3], not a guarantee about the first k enumerated primes, and not an effective bound on their size. It applies to genuine cohomology classes with authenticated local realizations. No field-arithmetic replay of those retained interfaces is claimed by this review. The semisimplicity used above is that V^d is a direct sum of simple modules; it does not assert that the modular group algebra is semisimple.

A complete ambient S-unit source alone does not justify applying this termination theorem to an oversized necessary kernel U. False global candidates in U need not define the genuine cocycles used in the argument, and a source-field class may become a cube in the full torsion field. Success Z=W on such U is still a valid certificate, but success is not guaranteed merely by the true-S theorem.

One can obtain a rigorous terminating fixed-p algorithm, conditional on the certified source and exact membership inputs, from a complete finite source by first applying the exact global and all-place membership tests (or interleaving those finite tests with the detector search). This is the usual finite descent problem. It is different from extrapolating source completeness from many successful residue blocks.

## 4. Concrete retained grades

* **1913b1:** complete 9-dimensional source, successful retained BNF certification, true Selmer dimension two. It can test the full-source invisible-kernel procedure at its present certified grade.
* **28042a1:** thirteen independent displayed source directions and three genuine classes, but complete source upper control was not certified. Extra signatures cannot fill that missing source-completeness premise.
* **Seed at 3:** use the prior source-completeness grade exactly as retained. The four actual point/excess columns are valid inputs for the new diagonal experiment regardless; an upper bound cannot be upgraded merely because their detector has full rank.

These distinctions are not cosmetic. A source direction absent from A is also absent from every matrix built from A. No amount of rank growth within that truncated source can exclude it.

## 5. Cross-prime scope

The construction and termination statement are for a fixed coefficient prime with a fixed complete arithmetic source. They do not bound class numbers, unit indices, source dimensions, detecting-prime heights, or the content of any Kato object uniformly as the coefficient prime varies. A successful pilot can complete or validate a fixed-p kernel calculation and reveal how common-point repair behaves. It does not by itself close FIN, ORDER9 or Q36.

## 6. Review of the completed matrix pilot

I read pilot.py and the relevant RESULTS.json entries. The implementation computes one annihilator after stacking the point matrix for the common-point detector, and separate annihilators for the old detector. Its source-containment checks use the necessary-condition rows separately. I found no mismatch between these operations and §§1–2. The all-pairs tables are explicitly retrospective; the prime-pair seal does not make the earlier field arithmetic or the all-pairs scan held out.

For the selected seed pair, the saved repair matrices in the fixed point basis are

    T_1213 = [[2,1],[0,0]],
    T_1543 = [[2,1],[1,2]].

Their difference has rank one. The producer subtracts in the opposite order to the display in §2; this only negates the row and has no effect on the kernel. The common detector has row (0,0,1,2) in the fixed order (P₁,P₂,β₁,β₂). Its invisible excess line is β₁+β₂. Including the next predeclared individually blind block, q=1699, removes that line on the supplied four-class span.

I independently checked these two conclusions by enumerating all 3⁴ combinations of the actual four saved source columns and all 3² common point combinations, directly evaluating the saved raw residue rows. This check does not use the producer's Gaussian elimination, annihilator, kernel, or solver routines. At [1213,1543] there are 27 common-kernel vectors, with excess coordinates {(0,0),(1,1),(2,2)}. At [1213,1543,1699] there are nine, with excess coordinates only {(0,0)}. Thus the first kernel is W plus the displayed line, and the second is W, **inside that supplied span**.

This is a genuine arithmetic distinction between separate and common point repair, rather than a new computation of a point or a new source-membership theorem. For the seed it establishes no statement about a source direction absent from those four columns. The 1913 whole-source calculation has the separate retained completeness input needed for its global fixed-prime conclusion. No new FIN, ORDER9 or Q36 conclusion follows from the seed experiment.
