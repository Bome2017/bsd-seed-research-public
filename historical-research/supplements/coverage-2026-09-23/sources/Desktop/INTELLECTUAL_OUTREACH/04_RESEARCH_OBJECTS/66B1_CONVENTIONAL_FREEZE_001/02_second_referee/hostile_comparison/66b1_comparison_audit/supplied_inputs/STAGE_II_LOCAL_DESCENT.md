# Stage-II extension: a direct uniform 2-isogeny descent

This is an additional derivation after the Stage-I freeze and after opening the withheld
receipts. It does not replace or edit PRE_COMPARISON_RECONSTRUCTION.md. The receipts
contain finite-field point counts, not local Selmer computations or these arguments.

Assume q is prime, q=5 mod 8, (q/3)=-1, (q/11)=+1. Put
C_q: y^2=x^3+17q x^2+64q^2 x and
C'_q: y^2=x^3-34q x^2+33q^2 x=x(x-q)(x-33q).
Let phi:C_q -> C'_q be the quotient by (0,0), and hatphi its dual.
The Kummer maps are x-coordinate squareclasses on the receiving curves, with
exceptional values at (0,0) equal to the relevant coefficient b.

## 1. Support lemma from valuations

For a curve y^2=x(x^2+a x+b) with integral a,b, at any prime l not dividing b,
every local point has even valuation of its Kummer x-class. If v_l(x)>0,
x^2+a x+b is a unit, so 2v_l(y)=v_l(x). If v_l(x)<0, x^2 is the uniquely
lowest-valuation summand of the bracket, so 2v_l(y)=3v_l(x). For v_l(x)=0
there is nothing to prove. The exceptional Kummer value b is a unit.
This applies also at l=2 and does not rely on good reduction there.

Consequently Sel^phi has representatives supported on {3,11,q}; Sel^hatphi
has representatives supported on {2,q}. A common ambient, including sign, is
Q({2,3,11,q},2), of size 32, but the separate support bounds are smaller.

## 2. The phi group

The real points of C'_q have x>=0, since all three roots are 0<q<33q and its
cubic is negative for x<0. Thus its Kummer image at infinity is positive.
The only possible phi classes are therefore
{1,3,11,33,q,3q,11q,33q}.

The quotient rational 2-torsion supplies globally the subgroup
H={1,33,q,33q}. In particular all its elements belong to every local image.
The other four possible classes are precisely the coset 3H. It suffices to
exclude 3 at Q_2.

For class d on y^2=x^3+a x^2+b x, substituting x=d(U/V)^2 gives the covering
    d W^2=d^2 U^4+a d U^2 V^2+b V^4.
For d=3 on C'_q, the chart U!=0 gives
    w^2=3-34q z^2+11q^2 z^4.
When z is 2-adically integral and even, the right side is 3 or 11 mod 16.
When z is odd, it is 12 mod 16, since q is 5 or 13 mod 16. None is square.
If v_2(z)=-r<0, write z=2^-r u with u odd and multiply by 2^(4r).
The rescaled square has right side 11q^2 u^4 = 3 mod 8, impossible.
The missing chart U=0 would require 11q^2 to be a square in Q_2,
again impossible. Hence class 3 has no Q_2 point. Because the local image
is a subgroup containing H, no class in 3H can survive either.

Thus Sel^phi(C_q/Q)=H exactly.

## 3. The dual group: the place q

Reciprocity gives (33/q)=(q/3)(q/11)=-1. We claim that every Kummer x-class
on C_q(Q_q) is trivial. For x!=0 let m=v_q(x).

If m<=0, write f(x)=x^3(1+17q/x+64q^2/x^2). The bracket belongs to
1+q Z_q, hence is a square because q is odd. Thus y^2=f(x) forces x to
be a square.
If m=1, write x=q u with u a unit. Then
f(x)=q^3 u(u^2+17u+64). The quadratic in u has discriminant 33, a
nonsquare modulo q; consequently the last bracket is a unit, and
v_q(f(x))=3 is odd. No point exists in this case.
If m>=2, write f(x)=64q^2 x(1+17x/(64q)+x^2/(64q^2)); once again the
bracket belongs to 1+q Z_q and is square, so x must be square.
The exceptional point (0,0) has Kummer class 64q^2=1, and O has class 1.
This proves that the entire dual local Kummer image at q is {1}.

The global dual candidates were {+/-1,+/-2,+/-q,+/-2q}. Being square in
Q_q eliminates the four q-divisible candidates by valuation, and eliminates
+/-2 because (2/q)=-1 while (-1/q)=+1. Only 1 and -1 remain.

## 4. The dual group: the place 3

The d=-1 cover on C_q is
    w^2=-1+17q z^2-64q^2 z^4.
Since q=2 mod3, its right side is 2 mod3 for every integral z, both when
z=0 mod3 and when z is a unit. If v_3(z)=-r<0, multiplication by 3^(4r)
leaves rescaled right side -64q^2 u^4=2 mod3. The chart U=0 likewise
requires -64q^2 to be square in Q_3. Each case is impossible.
Therefore -1 does not survive at 3, and Sel^hatphi(C'_q/Q)={1}.

## 5. Consequences and scope

The isogeny-Selmer comparison is exact at the terms displayed:
  0 -> C'_q(Q)[hatphi]/phi(C_q(Q)[2]) -> Sel^phi(C_q)
       -> Sel^2(C_q) -> Sel^hatphi(C'_q).
The first group has size 2, because C_q(Q)[2] is precisely ker(phi).
Thus the two computed isogeny Selmer groups give |Sel^2(C_q)|=4/2=2.
The multiplication-by-2 Kummer sequence gives
  |Sel^2(C_q)|=2^(rank(C_q(Q))+1) * |Sha(C_q)[2]|.
Hence rank(C_q(Q))=0 and Sha(C_q)[2]=0; also Sha(C_q)[2^infinity]=0.
This conclusion does not invoke BSD or floating-point L-values.

The separate residue signs have now appeared in an actual proof: their product
makes 33 a nonsquare at q, while (q/3)=-1 excludes the last dual class at 3.
No claim is made here about dropping either sign or a larger Selmer family.

## 6. Explicit full-real-period BSD(2) bookkeeping

This paragraph fixes Omega_R=integral over the entire E^q(R) of |omega_min|.
It does NOT assign a meaning to BSTW's undefined period symbol and does NOT
invoke BSTW Theorem 10.12 or make a full-strong-BSD conclusion.

The twist has one rational involution. If it had rational order 4, halving that
involution would require x=+/-8q; the corresponding y-squares are 64*33*q^3
and 64*q^3, neither a square in Q for the stated primes. Thus its rational
2-primary torsion has order 2.

At 2, the twist character is unramified and nontrivial, so split I_4 becomes
nonsplit I_4: its geometric component group Z/4 has Frobenius acting by -1,
with exactly two invariants. Hence c_2=2. At 3 and 11, the type remains I_1,
so c_3=c_11=1. At q>=5, the ramified twist of good reduction is I_0^*;
its component polynomial has exactly one residue-field root because (33/q)=-1,
so c_q=2 (the usual Tate-algorithm root count c_q=1+#roots).
Thus v_2(product of finite Tamagawa numbers)=2, and
v_2(|E^q(Q)_tors|^2)=2.

Zhai 1.7, in the least-period convention, yields v_2(Lalg_Z(E^q,1))=1.
Because the discriminant is positive, Omega_R=2 Omega^+, and the explicit
full-real analytic valuation is 0. The descent gives v_2(|Sha(E^q)|)=0,
with Sha finite by analytic nonvanishing. Both sides of the rank-zero BSD
formula in this explicitly defined convention therefore have valuation 0.
This establishes the standalone BSD(2) equality conditional only on the
established base-curve data and the cited analytic theorem, not on BSD itself.

BSTW's exact factor-of-two convention remains unaudited as recorded at the
Stage-I freeze, and its literal Theorem 10.12 additionally fails a_3(E)=0.
A BSTW-based/full-strong-BSD claim is still withheld.
