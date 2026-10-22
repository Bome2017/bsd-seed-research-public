# Primitive divisor layer for 11a1, p=7

## Statement and inputs

Let A be the actual degree 48 nonzero 7-torsion point field of E=[0,-1,1,-10,-20]. Use the retained scalar character chi with sigma3 acting by 3 modulo 7, the dual covector field, and the incidence norm over lambda(v)=1. For S={7,11}, the kernel dimension on the primitive S-prime divisor layer is

    t_D,chi = 0.

This is a statement about the valuation layer of the actual-source filtration. It does not supply any assertion about units, class groups or Selmer classes by itself.

Inputs are the saved exact field and maximal order, the actual scalar 3 automorphism, standard Tate uniformization at split multiplicative reduction, and the already-derived primitive divisor incidence formula. The local arithmetic and finite orbit calculation are checked in this packet. This is a written deduction with executable exact checks, not a machine-formalized theorem.

## Actual coefficient-place source

The exact number-field decomposition at 7 has two primes with (e,f)=(6,1),(7,6). Applying the actual scalar automorphism to their HNF ideals fixes each prime. Thus its permutation module has no scalar eigenvalue3 or5 over F_7. Its faithful character source is zero. Nothing about the covector target at 7 needs to be assumed to conclude that this place contributes no source kernel.

## Actual split multiplicative place and the coefficient 5

For the given minimal equation, Delta=-11^5 and c4=496 is a unit at 11. The reduction is multiplicative of type I_5. The singular reduction point is (5,5); its tangent cone is y'^2=3x'^2 modulo 11, and 3=5^2 modulo 11. Therefore the reduction is split multiplicative. The independent local trace check gives a11=1.

Tate uniformization then gives inertia generated, after choosing a basis, by

    [[1,5],[0,1]] mod7.

The monodromy coefficient 5 is not discarded. Since 5 is invertible modulo 7, this matrix generates the full order 7 unipotent subgroup I. A Frobenius element can be adjusted by I so that the local decomposition group is

    D=< I, diag(11 mod7,1) >=< I, diag(4,1) >.

It has order 21. The scalar 3 action commutes with this group.

The actual point-field calculation finds six primes with (e,f)=(7,1), and two with (e,f)=(1,3). The actual scalar permutation is [4,1,5,3,6,2,8,7], with cycle lengths 6 and 2. These e,f data and scalar cycles exactly match the D-orbit model. This arithmetic check accompanies, and does not replace, the Tate-uniformization explanation of D and I.

## Primitive valuations, not unweighted orbit counts

Let P be a point D-orbit and Q a covector D-orbit, and let e_P,e_Q be the sizes of their inertia orbits. For a target representative lambda in Q, the primitive integer divisor map is

    u_D(Q,P)=(e_Q/e_P) * #{v in P:lambda(v)=1}.

Indeed, if v_P is a normalized valuation in A, its extension to the common splitting field is multiplied by |I|/e_P. Taking the product over the incidence fibre adds these valuations. Returning to the normalized target valuation divides by |I|/e_Q, giving the displayed formula. The resulting entries are integers because this is the actual norm on prime-divisor lattices.

The point orbits with second coordinate y=0 have scalar stabilizer of order 3 and contribute nothing to the faithful character. The six point orbits with y nonzero have inertia index 7 and carry one copy of chi, represented by the values a(P_y)=y.

In the covector module the six singleton orbits lambda=(0,b) have inertia index 1 and carry one copy of the inverse character, represented by b(Q_b)=b^(-1). The other orbits contribute nothing to it.

For lambda=(0,b), the unique relevant point orbit is y=b^(-1), and its incidence fibre contains 7 points. The normalized entry is

    (1/7)*7=1.

Thus the actual character map sends a to b and is an isomorphism modulo 7. Its kernel is zero. Omitting ramification would instead produce 7*b and a false zero map modulo 7.

At7 the source character space was zero; at 11 the primitive character map is injective. Their direct sum therefore has t_D,chi(S)=0.

## What remains separate

This computation is compatible with either a nontrivial unit kernel or a nontrivial class-supported contribution. Any complete-source upper bound still requires the root's authenticated ordinary-unit map and ordinary class input, with their own grades. No hidden class completeness or p-unit normalization is used in the divisor calculation.
