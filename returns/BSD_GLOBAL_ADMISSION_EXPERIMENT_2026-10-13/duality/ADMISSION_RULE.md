# An explicit dual obstruction at the seed prime 1783

2026-10-13. Scope: a written deduction from finite local/global duality, with exact local arithmetic. No global obstruction class is constructed. In particular the saved local basis below is not such a class. Neither the seed's known Sha[5] answer nor its Ota/Kato vanishing certificate is an input to this deduction or the local computation.

## 1. The objects and the verifiable obstruction

Let V=E[5] for the seed in the minimal model

    y²=x³−x²−66020924x−65074271436,

and let S=Sel_5(E/Q) with the actual Kummer conditions F_v at every place. Put q=1783. Define S_q by replacing F_q with zero, and S^q by replacing it with all of H¹(Q_q,V); other conditions are unchanged. Define

    L_f=F_q,
    L_s=H¹(Q_q,V)/F_q.

Both spaces are one-dimensional over F5. Weil self-duality and the Kummer annihilator property give a perfect pairing L_f × L_s -> F5, after fixing the invariant-map normalization.

The exact arithmetic object sought is one class

    c ∈ S^q,
    ∂_q c ∈ L_s nonzero.                                    (A)

This has a directly checkable effect. For any x∈S, global reciprocity applied to x and c gives

    <loc_q x, ∂_q c>_q = −Σ_(v≠q)<loc_v x,loc_v c>_v = 0.

Every term on the right vanishes because both classes satisfy the same self-dual Kummer condition there. By nondegeneracy in dimension one, loc_q x=0. Thus (A) excludes every nonzero local signature at q from the global Selmer image.

This does NOT show S equals the rational-point plane. A nonzero excess class could have zero localization at this one q. It proves precisely the non-admission of the one-dimensional family currently under test.

## 2. Exact necessity and sufficiency, without a Sha answer

Global duality for the inclusion of Selmer structures F_q=0 ⊂ F_q=F gives

    im(S -> L_f) = im(S^q -> L_s)^perp.                       (B)

Equivalently there is the exact sequence

    0 -> S_q -> S -> L_f -> (S^q)^∨ -> S^∨ -> 0,             (C)

where the middle map evaluates the local Tate pairing. The finite vector-space duals and every local condition are specified here; no claim about a characteristic ideal or a pseudo-isomorphism is used.

Consequently:

    a∈L_f extends to a global class in S
      iff <a,∂_q c>_q=0 for every c∈S^q.

Since dim L_f=1, the following are equivalent:

    (i) every global Selmer class has zero q-localization;
    (ii) S^q contains a class with nonzero singular localization;
    (iii) dim S^q = dim S + 1.

This equivalence is a source-matched way of searching for a witness, not a new bound. We must actually produce c and check its local conditions to use it independently. Its existence must not be inferred from the previously known Sha answer and then advertised as arithmetic evidence.

The imported orthogonal-complement theorem is Mazur–Rubin, Kolyvagin Systems, Theorem 2.3.4; an author-hosted formulation is Rubin, Euler systems and Kolyvagin systems, Theorem 1.10.2. A full source result also appears as Sakamoto, On the theory of higher rank Euler, Kolyvagin and Stark systems, Theorem 3.4. Source links and retrieval scope are in SOURCES.md.

## 3. The exact local coordinates at 1783

The independently replayed seed count is #E(F_1783)=1730, so a_q=54. Therefore the residual Frobenius polynomial is

    X²−54X+1783 = (X−1)(X−3) mod5.

Take torsion vectors e_1,e_2 with arithmetic Frobenius F acting by diag(1,3). The old local point R=(3,872) has [346]R=(1591,1089), a nonzero 5-torsion vector of eigenvalue1; we take e_1=(1591,1089).

For a tame inertia generator τ, the relation FτF^−1=τ^q gives the cocycle relation

    F·c(τ)=q c(τ).

Thus the unramified coordinate is the e_1 coordinate of c(F), modulo (F−1)V, while the singular coordinate is the e_2 coordinate of c(τ). Inertia must occur in eigenvalue3, not the rational e_1 line. Choose representatives

    c_ur(F)=e_1, c_ur(τ)=0;
    c_ram(F)=0, c_ram(τ)=e_2.

Their finite-quotient cocycle relations are checked exhaustively in local_row.py. A finite quotient C5(τ) ⋊ C20(F) is used so the unramified order5 cocycle is retained. C5⋊C4 would lose it.

The Weil form on V is alternating. The induced degree-one cup-Weil local Tate form on H¹ is symmetric: the cup-product sign cancels the alternating sign. The two coordinate lines are isotropic and pair nontrivially. In normalized dual bases its matrix is

              [0 1]
              [1 0].

The value1 is a dual-basis normalization, not an asserted numerical invariant of a global class. Before that normalization the off-diagonal is some specified nonzero unit. The candidate exclusion test is simply a*b≠0, so this unit cannot affect exclusion.

An independent local calculation in ../local_pairing/ additionally computes a reduced finite-field Tate pairing using Sage and a separate Miller implementation. It finds a nontrivial row on R and trivial rows on the two basis points. That authenticates the local functional. It still supplies no global lift c.

Our own local_row.py computes the full 5-torsion over F_(1783^4), finds the eigenvalue3 vector, computes its nontrivial Weil pairing with e_1, and confirms the Frobenius compatibility. All 30,000 tested cocycle identities pass. The x-division polynomial has factor degrees 1,1,2,4,4. On the 24 nonzero torsion points the Frobenius cycles have degrees 1^4,4^5.

## 4. A concrete global construction target, not just a local class

Schaefer–Stoll supplies an explicit full-p-descent representation, even without a rational 5-isogeny. Let A be the degree24 étale algebra of the nonzero 5-torsion points. Under full residual image it is a field, whereas the control's isogeny permits a much smaller algebra.

Corollary 7.9 in their long version identifies H¹(Q,V) inside A×/A×5 by two equations:

    σ_2(β) = β² mod A×5,
    u(β) = 1 mod B×5.                                       (D)

Here σ_2 is induced by T↦2T on the torsion scheme. The map u is the incidence-algebra norm of Proposition 7.10; it is not the ordinary field norm to Q and must not be replaced by it. The image also preserves the unramified-outside-S condition.

The seed's retained Tamagawa product is16, so each Tamagawa number is prime to5. Lemma4.5/Proposition4.6 show that away from5 the Kummer condition equals the unramified condition. Thus it suffices to seek

    β ∈ A({5,1783},5)

satisfying (D), whose5-local class lies in the actual Kummer image, and whose1783 singular coordinate equals1. Once a certified basis of A({5,1783},5) and the local maps are available, this is a concrete affine linear system overF5:

    (σ_2−2)x=0,
    u x=0,
    pr_(H¹(Q_5,V)/F_5) loc_5(x)=0,
    ∂_1783(x)=1.                                            (E)

The notation F_5 in the third line means the local Kummer condition, not the coefficient field. No condition on an unknown Sha order enters (E).

An arbitrary unit or ray-class character in the torsion field is insufficient: it must obey both cohomological equations and the5-local condition. Conversely a solution of (E), with those maps certified, would be the desired explicit reciprocity obstruction. This specifies a constructive arithmetic task, not a theorem already completed. No S-unit/class-group computation in degree24 is run here, and feasibility is not asserted from the field degree alone.

The local source is not a scalar ramified order5 character of Q_1783. Since1783−1=1782 is prime to5, none exists. V-valued ramification nevertheless exists in the eigenvalue3 direction. Its scalar Kummer realization uses the residue-degree4 factors, where1783^4−1 is divisible by5.

## 5. Source collision tests

1. The existing Kato derivative lies in the integral point plane, hence its mod5 reduction is unramified at1783. Linear combinations of existing point classes and this derivative have singular coordinate0. They cannot solve the last equation in (E).
2. A routine order5 cyclotomic Kolyvagin derivative at1783 is not available: there is no order5 quotient of (Z/1783Z)×. This excludes that particular source operation, not V-valued ramification or other Euler systems.
3. For the earlier BD/CM architecture,1783 passes the elementary positive-sign admissibility tests at5 and is inert in Q(√−7). This was checked exactly. Full geometric source eligibility and a nonzero singular reciprocity value are additional obligations. The previous lab notes already leave actual CM-image evaluation and the relevant reciprocity realization open. We did not relaunch that route or infer a nonzero global class from the elementary congruences.
4. The old detector/Chebotarev argument guarantees places detecting any globally existing class. It does not construct a global class for a prescribed local signature; its arrows go the other way.

## 6. What is now executable and what is not

The local functional, torsion eigendirections, cocycle equations, and the shape of the global acceptance system are explicit. A witness β solving(E) is not supplied. These results therefore do not replace the missing arithmetic admission calculation with a local toy calculation. They furnish a typed target whose outputs can be independently checked, and whose successful construction would explain the1783 negative case without taking known Sha vanishing as input.
