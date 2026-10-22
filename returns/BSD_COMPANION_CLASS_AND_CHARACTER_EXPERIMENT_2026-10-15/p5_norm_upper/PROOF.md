# An actual complete-unit upper bound at coefficient 5

Completed 2026-10-17. Curve C=389a1, model y^2+y=x^3+x^2-2x.
This is an arithmetic upper-bound experiment on a control, not the seed.

## 1. The entire space being bounded

Let A be the degree-24 nonzero-5-torsion point field constructed in
../p5_arithmetic/field.gp, and B the nonzero-covector companion. The literal
scalar automorphism sigma on A sends the universal point T to 2T. Let chi
denote the residual scalar character sigma -> 2 in F5.

The exact field and local arithmetic in ../p5_arithmetic establish the full
GL2(F5) image. Equivariant Dirichlet gives dimension 3 for

    V_U = (O_A^*/O_A^{*5})^chi.

The field has real embeddings, so no fifth roots of unity add a dimension.
This dimension is a theorem about all units, not the length of a supplied
unit list. The incidence norm u takes chi to chi^-1 and, on units, defines

    u_bar : V_U -> (O_B^*/O_B^{*5})^(chi^-1).

Our goal here is an upper bound on ker(u_bar).

## 2. Actual units, without a fundamental-unit assumption

The existing BNF supplied 13 candidate units in compact product form. Its
class and fundamental-unit completeness are unconditionally uncertified.
We do not use either assertion in this section.

unit_authentication/authenticate.gp factors the principal ideals of 317
distinct factors, reconstructs them exactly, and obtains a valuation
matrix on 295 actual prime ideals. Multiplying by all 13 full integer
exponent columns gives zero. Thus the products themselves have trivial
principal ideal and are actual global units. The exact identity is replayed
from AUTHENTICATION_DATA.gp. This calculation requires no class-group
generation theorem or GRH.

For each such unit epsilon, define the actual unit

    a = epsilon^4 sigma(epsilon)^2 sigma^2(epsilon) sigma^3(epsilon)^3.

Modulo fifth powers the polynomial 4+2sigma+sigma^2+3sigma^3 is the chi
projector: (sigma-2)(4+2sigma+sigma^2+3sigma^3)=0 modulo (5,sigma^4-1).
Therefore [a] lies in V_U.

## 3. A single norm that is not a fifth power

The search rule selected the first eight fully split primes below 100000,
excluding denominators of the field/point maps. The first prime1171 was
excluded from compact-factor evaluation because a factor reduced to zero;
this does not assert the global unit is undefined there. The next prime
is q=1831. All 24 distinct torsion points and their scalar action were
checked by exact finite-field arithmetic.

For projected candidate9, the independent checker chooses a fresh basis
of C[5](F1831) and an affine line not containing zero. Its five values are

    250, 88, 215, 1268, 223.

Their product is693 modulo1831, and

    693^((1831-1)/5) = 693^366 =123 !=1 mod1831.

Every affine line not containing zero has the form lambda(x)=1 for a
nonzero linear functional lambda. Thus this product is a residue of the
actual incidence norm u(a), not an unrelated product of evaluations.
If u(a) were a fifth power in B, its residue at this good split prime
would be a fifth power. The displayed result rules that out. It also rules
out a being a fifth power, since norms preserve fifth powers.

Hence rank(u_bar)>=1. Since dim V_U=3, we have the unconditional arithmetic
upper bound, under the written full-image/incidence framework,

    dim_F5 ker(u_bar) <= 2.                         (1)

Only one authenticated unit is needed for (1). In addition, the full
projected candidate residue matrix has rank3 over the seven usable primes.
This checks that those projected units span V_U modulo fifth powers,
without assuming the candidates form a fundamental-unit basis. The norm
residue matrix has rank1; that is a lower bound on the true norm rank, not
proof that its rank is exactly1 or that the global kernel has dimension2.

## 4. Keeping every class-supported direction

Let K be the full scalar-compatible incidence-norm kernel in A(S,5), with
S={5,389}. Exact source-prime computations give no chi divisor component at5.
At389 the actual primitive divisor norm is a unit on the one-dimensional
chi component (the ramification factor is essential). Thus t_D,chi=0.
The valuations modulo5 of every class in K are zero: K is contained in
the ordinary virtual-unit space, not just in an arbitrarily selected list.

The ordinary Kummer sequence gives

    0 -> V_U -> A(empty,5)^chi -> Cl(A)[5]^chi ->0.

Its kernel under u intersects V_U in precisely the kernel bounded in(1).
Consequently

    dim K <= 2 + dim Cl(A)[5]^chi.                  (2)

More sharply, the last term can be replaced by the kernel of the actual
ideal-class norm to Cl(B)[5]^(chi^-1); see ../character_review/CLASS_MAP_BOUND.md.
No class-map value is inferred from (2).

The saved BNF reports ordinary class group C3. Under its GRH-dependent
completeness assertion, Cl(A)[5]=0, so (2) gives

    dim K <= 2.                                   (3)

This bounds the entire global source, including undiscovered classes,
CONDITIONAL on class completeness. It is stronger than the previous bound3.
The bounded bnfcertify attempts did not finish; (3) is not an unconditional
class/Selmer theorem. Unit authentication and residue nonvanishing do not
certify that no additional ideal classes exist.

## 5. Consequence and limits

This proves a complete-unit upper bound by actual arithmetic, and a
conditional complete-source upper bound at p5. No point, Sha order,
L-value, or predicted kernel dimension is used to produce the norm witness.
It demonstrates a concrete larger-prime use of the method, beyond the
coefficient3 experiments. It does not prove that the needed norm rank or
class bound persists as p grows. At general p the independent ordinary
character-unit dimension is (p+1)/2; one nonzero row is insufficient for
a uniform rank-two bound.

The p7 and p11 tests elsewhere in the packet concern geometric incidence
lattices only. They are not number-field class or unit computations.
FIN, ORDER9, Q36 and seed-prime coverage are unchanged.

Primary computational reference: PARI General number fields, sections
Class group, units, and the GRH; bnfcertify; bnfinit. The documentation
distinguishes actual units from unproved completeness, and flag1 class
quotient certification from full unit certification:
https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html
