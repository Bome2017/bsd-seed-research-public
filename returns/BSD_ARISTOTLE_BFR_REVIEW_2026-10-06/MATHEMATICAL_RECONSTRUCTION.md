# Independent reconstruction of BFR

Grade: written review under retained seed imports. Not formalized here.

Fix p in {2243,4547,5843}. Write V=E[p]. Import residual surjectivity,
the saturated rank-two Mordell-Weil basis, and the Tamagawa data from the
bound release record. The parity import is needed only for the last
vanishing implication.

## A. The local generator is divided in L

At 2243 and 5843, the finite quotients E(Q_p)/E_1(Q_p) have orders 2242
and 11688. Multiplication by p is an automorphism on these quotients, so
E_1/pE_1 maps isomorphically to E(Q_p)/p. The formal logarithm and the
auxiliary point's parameter valuation one give the local generator R_p.

At 4547, translate x=X+1516. The resulting minimal equation has all
coefficients in pZ_p. Pannekoek's Theorem 1 implies E_0(Q_p) is
topologically Z_p; the index-p subgroup E_1 is pE_0. P2 is a smooth
affine reduction point, hence nonzero in E_0/E_1. The component group
has order 2, so P2 also generates E(Q_p)/p. The independent addition
certificate provides a second verification: pP2 lies in E_1 minus E_2.
Here R_p lies in E_1=pE_0, so its local Kummer class vanishes.

The field L includes all p-torsion and p-division points of P1, P2 and
R_p. At every place of L above p it therefore kills the local Kummer
line. The two quadratic embeddings change R_p to its negative, with no
effect on the span. At 4547 use the division of P2 instead.

## B. Restriction kills exactly the rational-point subspace

Let K=Q(E[p]), F=Q(sqrt(d_p)), K'=KF and G0=Gal(K'/Q). The negative
integer d_p is a p-adic unit, while d_p times either sign of p has odd
p-valuation and cannot be a rational square. Thus F is quadratic and
different from the unique quadratic subfield of K. Residual
surjectivity gives G0=GL2(F_p) times C2.

The central element (-I,+1) acts by -1 on V and on V epsilon. Its
order-two subgroup has no invariants in either coefficient module and
has vanishing higher cohomology since 2 is invertible. The
Hochschild-Serre spectral sequence therefore kills all cohomology of
G0 with either coefficient module.

The normal translation group P=Gal(L/K') embeds equivariantly into
V plus V plus V epsilon. Its projection onto V plus V is surjective:
otherwise a nonzero linear combination of the two rational Kummer
classes would restrict to zero over K', contradicting H1(G0,V)=0 and
the saturated basis. Distinct C2-actions separate the isotypic pieces.
Since this ambient direct sum is semisimple, P is V squared plus
either zero or V epsilon. In particular Hom_G0(P,V) has dimension two.
No assertion about the nonvanishing of the third Kummer class is needed.

Inflation-restriction now identifies H1(Gamma,V) with these two
translation maps: both the H1(G0,V) and H2(G0,V) terms vanish. A second
inflation-restriction sequence identifies the kernel of global
restriction to L with W=E(Q)/p, spanned by P1 and P2. This is an exact
kernel statement, not merely an upper bound.

## C. The image factors through the p-inverted class group

Away from p, the local Tamagawa numbers are prime to p. A local Kummer
class can therefore be represented by a point in the identity
component. Multiplication by p on that component is etale and
surjective on the geometric special fibre, so the point can be divided
over the maximal unramified extension. Its restriction to inertia is
a coboundary. After passing to L, the coefficient representation is
trivial, so that coboundary is zero. This remains true when L is
ramified at that place.

At p, part A gives zero on the full decomposition group, not just
inertia. Class field theory therefore sends every restricted Selmer
class into Hom_Gamma(Cl(O_L[1/p])/p,V). Part B shows the kernel is W;
the Kummer exact sequence gives the claimed injection of Sha[p].

## D. Multiplicity and parity

Suppose s independent maps arise from Sha[p]. The joint map A -> V^s
is surjective. Indeed, V^s is a direct sum of simple modules. A proper
image admits a nonzero map from the quotient to V. Composing would
give a scalar linear dependence among the original maps, since
End_Gamma(V)=F_p. This uses semisimplicity of V^s; it does not assert
Maschke semisimplicity of every Gamma-module in characteristic p.

It follows that p^(2s) divides #A and hence the p-inverted class number.
If dim B<=1, or if p^4 fails to divide that class number, then s<=1.
Retained parity makes s even, hence s=0. A nonzero element of any
p-primary torsion group has a nonzero multiple of order p, so Sha[p]=0
implies Sha[p-infinity]=0 without first assuming finiteness.

## E. Limits

Nothing above bounds s or dim B. The argument remains consistent
with any even excess that can occur in the receiver. At 4547 the
third translation constituent may vanish; the exact degree is then
2p^4|GL2(F_p)| instead of 2p^6|GL2(F_p)|. The proof needs neither choice.
No reverse comparison at these bad primes, fixed annihilator, new
primary vanishing, or uniform bound is established.

Primary checks: [Pannekoek, Theorem 1](https://arxiv.org/pdf/1211.5833);
[Dainobu, Propositions 3.2 and 2.8](https://arxiv.org/pdf/2304.05035).
