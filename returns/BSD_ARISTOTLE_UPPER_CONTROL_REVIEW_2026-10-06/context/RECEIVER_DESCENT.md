# Push beyond the receiver: descent and its exact remaining local error

Status: **WRITTEN_DERIVATION; NO_NEW_UNIFORM_BOUND**.

This is a new derivation in this review, not an independent review of itself,
a novelty claim, or a new primary certificate. It uses the receiver's proved
group structure and the retained seed inputs. The finite-group argument below
is supplied in full; the exact controls are checks, not its proof.

Write k=F_p, V=k^2, G0=GL_2(k) x C2, and epsilon for the second character.
Set P=V^2 direct_sum V epsilon and Gamma=P semidirect G0, as in the submitted
receiver. P acts trivially on the coefficient V.

## 1. The finite group has H^2(Gamma,V)=0 for p>=5

First, H^i(G0,V)=0 for all i: (-I,+1) is central and acts as -1.

We also need

    H^1(G0, Hom_k(P,V))=0.                            (D1)

The summand Hom(V epsilon,V) has a central C2 acting as -1, so all its
cohomology vanishes. Each of the other two summands is End(V). To prove
H^1(GL_2(k),End(V))=0, restrict to its cyclic Sylow p subgroup U generated
by u=I+N, N=E12. Restriction is injective because the index is prime to p.
On End(V), conjugation by u^i is polynomial of degree at most two in i.
The norm over U is therefore zero for p>=5. Thus

    H^1(U,End(V))=End(V)/(Ad(u)-1)End(V).

The image of Ad(u)-1 is spanned by E12 and E11-E22. The quotient has basis
the classes of I and E21. The normalizing element diag(t,1) acts on these
H^1 classes with weights t^-1 and t^-2, respectively. The extra t^-1 comes
from its action on the generator of U. Neither character is trivial on
k^* for p>=5. No normalizer-invariant class exists. This proves (D1).

Now let 1 -> V -> H -> Gamma -> 1 be any group extension inducing the given
action. Let Ptilde be the inverse image of P. It is a central extension of
the elementary abelian P by V. Its commutator map Lambda^2 P -> V is
G0-equivariant. The scalar (-I,+1) acts as +1 on Lambda^2 P and as -1 on V,
so this map is zero. Thus Ptilde is abelian.

The p-th-power map of Ptilde is a G0-equivariant linear map f:P -> V.
If f is nonzero, semisimplicity of the particular module P gives a submodule
U0 isomorphic to V on which f is an isomorphism. The inverse image of U0 in
Ptilde is then a free (Z/p^2)-module of rank two, with a genuine G0 action
lifting the natural representation of GL_2(k).

Such a lift cannot exist for p>=5. Indeed an element of order p in GL_2(k)
is J=I+E12. Any matrix lifting it is J(I+pC) modulo p^2. Its p-th power is

    J^p (I+p sum_{i=0}^{p-1} J^(-i) C J^i) = I+pE12 != I.

The sum is zero modulo p because conjugation is quadratic in i and the
sums of 1, i, and i^2 are all zero in k for p>=5. This contradicts order p.
Consequently f=0 and Ptilde is an F_p-vector space.

Conjugation on the abelian group Ptilde factors through H/Ptilde=G0.
The sequence 0 -> V -> Ptilde -> P -> 0 therefore splits as G0-modules by
(D1). Choose a G0-stable complement P0. It is normal in H. The extension
H/P0 of G0 by V splits since H^2(G0,V)=0. Its complement lifts together
with P0 to a complement to V in H. Thus every extension splits, proving

    H^2(Gamma,V)=0.                                    (D2)

Notice the essential distinction: (D2) concerns a finite Galois group.
It does NOT say H^2(G_Q,V)=0, nor that a class group is zero.

## 2. Every equivariant receiver class descends globally

Inflation-restriction, the submitted H^1(Gamma,V)=W calculation, and (D2)
give an exact sequence

    0 -> W -> H^1(Q,V) -> H^1(L_p,V)^Gamma -> 0.         (D3)

Let B_p=Hom_Gamma(Cl(O_Lp[1/p])/p,V). It is a subspace of the final term.
Every element of B_p therefore has a global preimage, unique modulo W.
Let H_L be its inverse image in H^1(Q,V). Then

    B_p = H_L/W,       Sel_p(E/Q) subset H_L.           (D4)

The second inclusion is the submitted receiver theorem. This closes the
possible global transgression obstruction; it does not establish the finite
local condition at p for every descended class.

## 3. Away from a fixed finite set, the only possible error is one local line

Put Bstar={2,3,19,59,487,2243,4547,5843} and assume p is outside Bstar.
Let S contain p, infinity, and the bad primes of E.

At a prime q outside S, E has good reduction, E[p] is unramified, and the
p-division fields of P1,P2 are unramified. Over F_p the same holds for the
p-division field of R_p: [p] on the good-reduction elliptic scheme is finite
etale because q!=p, and the point extends over the local ring by properness.
Thus the ramification index of L_p/Q at q divides 2, coming only from F_p.

A global class whose restriction is unramified over L_p is consequently
unramified at q already: on inertia the coefficient action is trivial, and
restriction across an index prime to p is injective. Hence H_L is contained
in H^1(G_Q,S,V). This argument covers the new primes dividing d(p); they
must not be silently omitted from the descent check.

At the bad primes q, the retained local calculation gives H^1(Q_q,V)=0
on this domain. The finite reduction-quotient orders are 4,8,2242,9094,11688;
their possible odd coefficient primes were excluded in Bstar. At infinity
odd-primary cohomology is zero. At p, H^1(Q_p,V) has dimension two and the
Kummer condition has dimension one. Therefore localization induces

    0 -> Sha(E/Q)[p] -> B_p -> C_p^loc -> 0,            (D5)

where C_p^loc is a subspace of H^1(Q_p,V)/H^1_f(Q_p,V), of dimension at most one.
The superscript distinguishes this local error from the project's Kurihara scalar.
Explicitly C_p^loc is the localization image of H_L modulo the finite line.
The map is independent of a lift in (D3), because W is locally finite.
Its kernel is Sel_p/W=Sha[p]. This proves (D5), without assuming finiteness
of Sha or nonzero localization of the rational points.

In particular,

    dim Sha[p] <= dim B_p <= dim Sha[p]+1.              (D6)

Using the RETAINED even-parity input for dim Sha[p], this improves the
submitted sufficient criterion to the equivalence, on this cofinite domain,

    dim B_p <= 1  <=>  Sha[p]=0.                       (D7)

If localization of W at p is nonzero, C_p^loc=0. One proof uses global
reciprocity: all other local H^1 groups vanish, so the global localization
image is isotropic in the two-dimensional local Tate space. It contains
the finite Kummer line supplied by W, whose annihilator is itself. Thus
every global class unramified outside S is finite at p. In that case

    B_p is canonically isomorphic to Sha[p].           (D8)

No cofinite non-Wieferich theorem is assumed in (D5)-(D7).

## 4. Tried upper control: precisely where it still fails

The new descent calculation eliminates the possibility that the receiver
has arbitrarily many *additional* directions unrelated to the seed, outside
Bstar. It does not eliminate the excess directions themselves. Counting
generators through (D3) or applying Poitou-Tate gives (D6), not dim B_p<=1.
Inserting dim Sel_p=2 into this count would assume the endpoint.

The submitted norm attempt still gives cor(res(c))=p^6 c=0. This is a
different map from the surjective descent map (D3); the norm's failure does
not contradict (D3), and neither is an upper bound.

A total-class-number bound also has not been supplied. The field and its
class group vary with p, so their finite orders do not provide a fixed
integer. (D2) provides no class-number estimate. Thus this pass has obtained
a reverse comparison and an at-most-one local error, but NO independent
bound on the receiver or on Sha[p]. A theorem controlling its standard
representation quotient would still be substantive arithmetic work.

This is not a reason to reject the receiver method: independent proofs of
equivalent statements are admissible. It is a reason not to count (D7)
itself as progress through uniform nonvanishing.

FIN, ORDER9 and Q36 are unchanged.
