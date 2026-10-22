# The remaining 4547 receiver defect is globally zero

Date: 2026-10-06.

**Status: DERIVED_UNDER_RETAINED_RECEIVER_INPUTS.** This is a written deduction,
not a new Lean theorem, an independent certification of the full receiver
construction, a primary-vanishing result, or a literature-novelty claim.

The deduction strengthens the *global* comparison in the reviewed return at
commit `6c1cb9398ce6d4791fc7988ee18893cd74bc1cdf`. It does not assert equality
of all pulled-back local conditions.

## 1. Fixed arithmetic objects

Use the minimal seed

\[
 E:y^2=x^3-x^2-66020924x-65074271436,
 \qquad P_2=(-2394,281520).
\]

For a prime p >= 5, set V = E[p] and

\[
 d_p=1-p^2-66020924p^4-65074271436p^6,\quad
 F_p=\mathbf Q(\sqrt{d_p}),\quad K'_p=\mathbf Q(E[p])F_p.
\]

The auxiliary point is R_p = (p^(-2), sqrt(d_p)p^(-3)). Let L_p be the retained
Galois division field obtained from K'_p by adjoining p-division points of
P_1, P_2, and R_p, and let Gamma_p = Gal(L_p/Q). The coefficient action on V
is the one coming from E/Q; in particular, the independent quadratic factor
acts trivially on V. Define exactly the same receiver as the reviewed return:

\[
 B_p=\operatorname{Hom}_{\Gamma_p}
       (\operatorname{Cl}(\mathcal O_{L_p}[1/p])/p,V).
\]

This is the ordinary class group with primes above p inverted, not a ray
class group. Let W be the global Kummer image of E(Q)/pE(Q). For every place v,
write f_v = delta_v(E(Q_v)/pE(Q_v)) in H^1(Q_v,V). Let S_p be the inverse image
of B_p under global restriction to L_p.

**RETAINED INPUT R1.** The corrected proof's finite-group descent, full-image,
basis, and forward-comparison inputs give

\[
 0\longrightarrow W\longrightarrow S_p\longrightarrow B_p\longrightarrow0,
 \qquad \operatorname{Sel}_p(E/\mathbf Q)\subseteq S_p.
\]

**RETAINED INPUT R2.** For p = 4547, every element of S_p satisfies f_v at every
place v other than 4547. This is the specialization of sections 4-5 of the
corrected proof, not an extra assumption of global exactness. The only
exceptional away-from-p pairs in that proof are (p,q) = (19,2243), (59,2243),
and (487,5843), none of which occurs when p = 4547.

**RETAINED INPUT R3.** The reviewed BFR result proves that delta_p(P_2)
spans f_p when p = 4547. In particular, it is nonzero. The source is BFR,
MATHEMATICAL_RECONSTRUCTION.md, section A. Section 3 below checks the concrete
arithmetic and applies the published local theorem again.

**RETAINED INPUT R4.** The current corrected proof establishes
B_p = Sel_p/W = Sha(E/Q)[p] for every other prime p >= 5, under its listed
inputs. This note does not independently recertify all those earlier inputs.

## 2. General single-relaxation lemma

**THEOREM (printed local-duality input).** For an elliptic curve over a local
field of characteristic zero, the local Kummer image f_v is its own
annihilator in H^1(Q_v,E[p]) under the local Tate pairing formed with the Weil
pairing. No good-reduction assumption is needed. See Poonen-Rains,
Proposition 4.10 and its proof, arXiv:1009.0287, pp. 17-18. Their odd-degree
case applies to [p], whose degree is p^2; the conventional overall sign of the
pairing does not alter its annihilators.

**THEOREM (printed reciprocity input).** For global classes c,k in H^1(Q,E[p]),

\[
 \sum_v \operatorname{inv}_v(c_v\smile_{e_p} k_v)=0.
\]

This follows from reciprocity for the global Brauer class c cup k. The exact
Brauer sequence is displayed in Poonen-Rains, proof of Theorem 4.13, p. 19.
All places are included. Only finitely many local terms can be nonzero.

**DERIVED LEMMA.** Suppose S is a subspace of H^1(Q,E[p]) containing Sel_p,
and every c in S satisfies the finite local condition away from a single
place v0. Suppose a global Selmer class k has localization spanning f_v0,
and dim f_v0 = 1. Then S = Sel_p.

**Proof.** Take c in S. At v != v0, both c_v and k_v belong to f_v, so
self-annihilation gives inv_v(c_v cup k_v) = 0. Global reciprocity then gives

\[
 \langle c_{v_0},k_{v_0}\rangle_{v_0}=0.
\]

Since k_v0 spans f_v0, this says c_v0 belongs to f_v0^perp = f_v0. Hence c
satisfies every local Selmer condition. The reverse inclusion was assumed.
This argument works also when v0 is the coefficient prime p and when E has
additive reduction there. It does not calculate the full pulled-back local
subspace at v0. QED.

## 3. Concrete verification of the missing specialization

**DERIVED ARITHMETIC.** At p = 4547, substitute x = X + 1516. The translated
minimal model is

\[
 y^2=X^3+4547X^2-59129188X-161680134380.
\]

Its three coefficients below X^3 are p times 1, -13004, and -35557540.
Moreover v_p(Delta) = 3 and v_p(c4) = 1. The point P_2 has smooth affine
reduction

\[
 (X,y)=(637,4153)\quad\hbox{in }\mathbf F_{4547}^2.
\]

It lies on y^2 = X^3, and 2y = 3759 mod p is nonzero. In particular, this is
not the identity O in the smooth group. The included integer-only script
reproduces these identities; the reduction check is not a numerical p-adic
zero test.

**THEOREM (Pannekoek, Theorem 1).** In a minimal additive model over Q_p whose
Weierstrass coefficients all belong to p Z_p, E_0(Q_p) is topologically Z_p,
apart from explicit cases at p = 2,3,5,7. Thus the theorem applies here.

**DERIVED.** The standard reduction sequence gives [E_0:E_1] = p, so E_1 is
the unique index-p subgroup p E_0. Because P_2 is smooth affine, it belongs
to E_0 but not E_1. It therefore generates E_0/p E_0. The retained component
number is 2, a p-unit, so E_0/p E_0 maps isomorphically to E(Q_p)/p E(Q_p).
Consequently k = delta(P_2) is a global Selmer class and its localization
spans the one-dimensional space f_p. No non-Wieferich assertion for an
infinite set of primes is used.

For completeness, the retained quotient orders at the other bad places are
4,8,2242,11688 at q = 2,3,2243,5843. Each is prime to 4547. The corrected
proof's pro-q/formal-group and local-duality arguments therefore give no
additional exceptional local condition at these places. Good places,
including possible ramification from the auxiliary quadratic field, are
already handled by that proof's section 4. At the real place, odd-primary
H^1 is zero.

## 4. Finish the global comparison

Apply the lemma to S = S_4547, v0 = 4547, and k = delta(P_2), using R2-R3.
It follows that

\[
 S_{4547}=\operatorname{Sel}_{4547}(E/\mathbf Q).
\]

Using R1 and the global Kummer exact sequence gives the natural identification

\[
 \boxed{B_{4547}\simeq\Sha(E/\mathbf Q)[4547].}
\]

Together with R4 this yields

\[
 \boxed{B_p\simeq\Sha(E/\mathbf Q)[p]\quad\text{for every prime }p\ge5.}
\]

This conclusion uses neither parity nor finiteness of Sha. Its proof grade
remains a written derivation under the receiver inputs. It is not asserted
that the local pulled-back condition at 4547 equals f_4547: the possible
extra *local* direction simply cannot occur as the localization of a class
satisfying all the other required global conditions.

## 5. Exact endpoint consequences and non-consequences

**DERIVED, with the separately retained even-parity input.** For every p >= 5,

\[
 \dim_{\mathbf F_p}B_p\le1
 \iff B_p=0
 \iff\Sha(E/\mathbf Q)[p^\infty]=0.
\]

The last equivalence does not require finiteness: a nonzero p-primary torsion
element has a nonzero multiple of order p. With the retained exact 2- and
3-primary certificates, proving this condition at every p >= 5 would give
FIN and ORDER9. A cofinite statement alone still leaves its finite exceptions;
Q36 remains a separate obligation.

**NO NEW BOUND.** The sufficient dim B_p <= 1 condition was already available
in the third review, including at 4547. Removing its last comparison defect
does not improve that sufficient numerical threshold. No receiver dimension,
class number, source valuation, or primary group is evaluated or bounded here.

There is a specific reason not to turn this proof into another upper-control
experiment: pairing against P_2 eliminates a possible failure of a local
Selmer condition. It is identically zero on classes that are already Selmer.
It therefore supplies no additional constraint on the actual Sha contribution.
An independent class-group estimate is still entirely legitimate; exactness
would transfer it, not make it circular.

The useful changes are an exception-free global comparison and a stronger
consistency check: under retained parity an actual one-dimensional receiver
is impossible even at 4547. A one-dimensional *candidate* relation kernel
need not equal B_p and is not a counterexample to this statement.
