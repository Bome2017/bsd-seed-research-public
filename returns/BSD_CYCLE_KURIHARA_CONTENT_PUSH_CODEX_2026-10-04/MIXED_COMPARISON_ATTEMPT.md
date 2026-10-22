# Constructing and testing the mixed comparison

Grade: written algebraic and correspondence derivations, with exact controls. The constructions below use the actual complete-packet definitions in SOURCED_TARGET.md. They do not prove or refute the seed-specific ideal membership itself.

## A. Assemble two variables before comparing

For the closed lift D set v_j=z((beta_j)_*D), and define v'_j=v_(j+2)-2v_(j+1)+v_j. The supplied construction gives sum_j v_j=-1. Form an actual coefficient sequence, encoded as

    A(g)=sum_j v'_j g^j in k[C_p],       T=g-1.

With F(g)=sum_j v_j g^j, the exact group-ring identity is A=(g^(-1)-1)^2 F. The inverse comes from the chosen forward shift on coefficients; it has the same degree-two leading factor as (g-1)^2.

The exact finite differences give M_0(A)=M_1(A)=0 and M_2(A)=-2. Since the coefficient of T^2 is (M_2-M_1)/2,

    A(g)=-T^2 mod T^3.                                   (M1)

Now construct the group-algebra map g |-> sigma tau. This substitutes T=X+Y+XY. Apply the mixed projector Q from SOURCED_TARGET.md. It is integral at p; there is no division by p and no one-prime oldform inversion. It yields

    Q(A(sigma tau))=-2XY in M.                           (M2)

This is an executed algebraic construction of the proposed mixed unit. It works in the precise quotient requested, not just in two unrelated one-variable examples.

The actual homology packet, however, has class

    Q(Theta_n^z)=eta delta_n XY,      eta=2c_E,

where Theta_n^z uses z(C_(a,n)) as its coefficients. Consequently the difference between the constructed and prescribed objects is exactly

    Q(A(sigma tau))-Q(Theta_n^z)
        =(-2-eta delta_n)XY.                             (M3)

Equation (M2) neither bounds nor evaluates the delta in (M3). It would be wrong to call the map g |-> sigma tau a map of the underlying arithmetic packets: it relabels an abstract cyclic group, and supplies none of the complete modular-symbol coefficients in (T1).

There is also an exact limit on the simplest proposed label realization. A homomorphism from the source Borel B to an abelian p-group kills U, since U is contained in [B,B]. Thus sending its chosen unipotent generator to sigma tau does not extend to such a homomorphism of the full deck group. This only excludes that label-realization recipe. Correspondences and linear maps are not all group homomorphisms, so it is not a general impossibility result for an arithmetic comparison.

## B. Repair the coefficient identification by applying differences to the genuine packet

Instead of substituting labels on (M1), start with the genuine Theta_n. For any F in k[C_p x C_p], direct multiplication gives

    [XY] ((sigma-1)(tau-1)F) = epsilon(F).               (M4)

Equivalently, in coefficient coordinates the mixed finite difference has weighted moment sum_(i,j) ij Delta_1 Delta_2 F_(i,j)=sum_(i,j) F_(i,j). This identity includes cyclic wraparound.

The actual Theta_n lies in J^2, so epsilon(Theta_n)=0. Therefore this entirely arithmetic replacement yields zero in M, even if delta_n was already nonzero. It moves Theta_n into J^4:

    Q(XY Theta_n)=0 in M.                                (M5)

The diagonal version also fails in the same specified way. With h=sigma^r tau^s,

    [XY] ((h-1)^2 F)=2rs epsilon(F).

It is zero for F=Theta_n. Thus combining both auxiliary primes first does not fix the discrepancy for these finite-difference recipes.

The degree shift is the relevant difference. The closed construction creates degree two by differentiating a coefficient sequence with unit *total sum*. The arithmetic packet already starts in degree two because its constant and linear parts vanish. Applying the same differences to it raises, rather than extracts, its degree.

## C. Extract degree two without those extra differences

The repair to (M5) is to use Q(Theta_n) directly. That does preserve the desired coefficient: it gives delta_n XY. I tested whether the actual conductor norm equations, now imposed simultaneously in the two-variable quotient, determine it from the nonzero closed-cycle value.

They do not determine it in that quotient. In the basis

    1, X, Y, X^2, XY, Y^2

of R/J^3, the retained rank lower bound removes the first three entries. The two Kato conductor projections remove X^2 and Y^2. The kernel of these five coordinate conditions is exactly k XY. Every c XY, including c=0, has the same zero projections.

Hence the coefficient tested in (T1) is precisely the information those two norm projections discard. This is a calculation of the actual quotient and the actual leading norm equations, not a generic matrix objection. It does not assert that arbitrary c is realized by this curve's modular symbols.

The same issue remains if one starts with higher-conductor primitivity: an augmentation-preserving group map takes J^r into J^r. For a length at least four it gives no nonzero class in M. Dividing a Kato factor -(u-1)^2/u or applying an abstract degree-lowering differential would require an additional identity with the canonical lower-conductor packet. No such identity follows from (M4).

## D. Can lifting the two primes jointly evade the oldform degeneracy?

For this one tested repair, the four old degeneracy transfers at level N ell_1 ell_2 have period matrix the tensor product

    [[ell_1+1,a_(ell_1)],[a_(ell_1),ell_1+1]]
       tensor
    [[ell_2+1,a_(ell_2)],[a_(ell_2),ell_2+1]].

This follows by composing the two prime-to-each-other degeneracy correspondences. Modulo p all four entries of each factor are 2, so the tensor product is the 4-by-4 all-4 matrix. It has rank one; its mixed difference row (1,-1,-1,1) is zero. Thus simultaneously using both primes does not invert this *old-transfer* comparison either.

This does not prove failure of arbitrary homology cycles at the higher level, Ihara-type statements, or level-raising classes. The singular old-transfer pairing is not a theorem that the whole homology pushforward has rank one. I have not substituted that stronger false conclusion.

## E. Hecke closure and Manin relations

The closed cycle itself satisfies the integral correspondence reduction (A3). On the z quotient its effect is multiplication by -2. Hecke translates of an admitted packet contribute a_m delta_n; integer combinations and allowed unit reparametrizations contribute only linear combinations of the admitted values. They cannot supply membership of a unit unless those values already have unit content.

Manin's path additivity and triangle identities remain valid for both kinds of cycle. Writing R_p as a sum of ordinary modular symbols does not group those summands into the required complete discrete-log packets. The unproved grouping/content identity is exactly the one being requested. No claim is made that all possible new uses of Manin relations have been excluded.

## F. Combine many admissible pairs, not just one

The preceding tests do not dispose of the user's weaker ideal-membership proposal, which allows any finite combination of pairs. I therefore also used the strongest retained cross-pair identity: the reviewed October 1 scalar extension in its coherent source normalization,

    delta_ab=C_p e_a e_b D_ab^2.                          (M6)

It holds on the retained good-prime domain, including zero Mordell--Weil localization and degenerate pairs. The local factors e_a,e_b are units, and the two-class Kummer--Chebotarev construction supplies a pair with D_ab nonzero without assuming Sha vanishing. These are imports from that review, not re-proved arithmetic input here.

Put mu_ab=e_a e_b D_ab^2. Since at least one mu_ab is a unit, (M6) gives an equality of evaluated ideals for the cyclic admissible family:

    (delta_ab : all cyclic pairs)=(C_p).                 (M7)

For *any* finite proposed coefficient family b_ab one therefore has

    sum b_ab delta_ab=C_p sum b_ab mu_ab.                 (M8)

In particular the attempted construction b_ab=-2/mu_ab at a determinant-nonzero pair yields -2C_p, not -2. Allowing more pairs changes the second factor in (M8); it does not evaluate the first. Using 1/C_p in those coefficients would assume the desired nonvanishing.

This does not make a common rational scalar across different primes necessary, and it does not exclude a new arithmetic proof of (M8)=-2. It shows specifically why the retained inter-pair reciprocity relations, together with the closed-cycle period alone, have not supplied that equation. An independent inhomogeneous comparison remains to be proved.

The exact controls retain both C_p=0 and C_p!=0. They do not assert which value occurs at an unsettled seed prime.

## Outcome of these concrete attempts

The two-variable algebraic unit in (M2) exists. The attempt to identify its coefficients arithmetically fails at (M3). Applying the finite differences to the correct coefficients instead gives the explicit zero (M5). Omitting those extra differences preserves the canonical coefficient but does not evaluate it; it is the free mixed coordinate of the conductor-projection system.

No relation of the form -2=sum a_(ell_1,ell_2) delta_(ell_1 ell_2), with independently derived coefficients, has been constructed. Nor has such a relation been disproved for the seed. These results stop this tested construction from being called a uniform vanishing proof; they are not a proof that no further arithmetic comparison can exist.
