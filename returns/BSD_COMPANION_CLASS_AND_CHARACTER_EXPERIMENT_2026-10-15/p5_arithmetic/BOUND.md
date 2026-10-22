# Whole-source arithmetic bound at coefficient five

Let A be the actual field of a nonzero point of E[5], let B be the nonzero-covector companion, and let S contain the primes above 5 and the bad reduction prime. Write sigma for the field automorphism induced by multiplication by 2 on E[5]. The descent character is chi(2)=2 in F5; the paired companion character is chi^-1(2)=3. Projection onto either character is integral over Z5 because the scalar group has order four.

Let K_chi be the scalar-compatible affine-incidence norm kernel in A(S,5), before any extra local Selmer rows. This definition includes all virtual units and all class-supported directions. The retained scalar-descent theorem embeds the corresponding Selmer source into this global kernel; no claim that every global kernel class is locally admitted is needed for an upper bound.

## 1. Actual fields and full image

`field.gp` and `control37/field.gp` give an irreducible polynomial of degree 24, a point T=(x,y) satisfying the curve equation, and a literal automorphism sigma taking T to 2T. The independent manual doubling check gives 4T=-T and T nonzero. Thus T has order five. Its coordinates generate the field by the recorded primitive-element construction. The Galois action is transitive on all 24 nonzero torsion points and hence irreducible.

For 389a1 the model invariants are Delta=389, c4=112, c6=-856. For 37a1 they are Delta=37, c4=48, c6=-216. These are minimal multiplicative models at the sole bad prime, with discriminant valuation one. Tate inertia therefore contains a nontrivial transvection on E[5]. This claim only concerns the prime-to-5 bad place.

An irreducible subgroup of GL2(F5) containing a transvection contains a conjugate transvection with a different fixed line. In a basis given by those two lines the two transformations have forms U(a) and L(b), with a,b nonzero. Their powers give U(1), L(1), which generate SL2(F5). The Weil-pairing determinant is the surjective mod-5 cyclotomic character. Hence the full image is GL2(F5). The finite generation check in `replay.py` confirms that the two displayed elementary matrices generate all 120 elements of SL2(F5); the group argument, rather than the finite check alone, explains the implication.

## 2. Ordinary character-unit rank

Complex conjugation has eigenvalues 1 and -1 on E[5]. There are four real embeddings of A and ten conjugate pairs. Equivariant Dirichlet identifies the rational unit representation with the augmentation-zero module on these 14 archimedean places. In a nontrivial scalar character the augmentation condition removes nothing. Both faithful characters have rank three, checked by their scalar permutation in `CHECK_DIVISORS.json`. The field has real embeddings, so it contains no fifth roots of unity other than 1.

The ordinary Kummer exact sequence gives

    dim_F5 A(empty,5)^chi = 3 + dim_F5 Cl(A)[5]^chi.

This includes all ordinary class-supported directions, regardless of whether representatives were listed by an experiment.

## 3. Primitive valuations

For any norm-admitted class, its source valuation vector modulo five belongs to the kernel of the primitive divisor incidence map. Zero valuation vector means an ordinary virtual-unit class, not necessarily an ordinary unit; the class term in the preceding equation is why the ordinary class-group input is indispensable.

At 389, the exact point-field arithmetic gives two primes above 5, with (e,f)=(4,1),(5,4), both fixed by sigma. Their faithful-character part is zero. Above 389 it gives four (5,1) primes in a scalar four-cycle and two (1,2) primes in a scalar two-cycle. Only the four-cycle contributes to either faithful character. The actual normalized incidence divisor coefficient is the ramification ratio 1/5 times an incidence count 5. It is therefore one, not five. The complete orbit argument and finite verification are in `../general_character/LOCAL_DIVISOR_PROOF.md` and `LOCAL_DIVISOR_CHECK.json`. Thus t_D,chi=0.

At 37, the exact prime decomposition above 5 is again (4,1),(5,4), both scalar-fixed. Above 37 the primes have (e,f)=(5,2),(5,2),(1,4); the scalar action swaps the first pair and fixes the third. All stabilizers contain sigma^2=-1, so there is no faithful-character source divisor. Again t_D,chi=0, without needing a target divisor calculation.

Consequently, for both controls,

    dim_F5 K_chi <= 3 + dim_F5 Cl(A)[5]^chi.

The bound applies before any local admissibility tests, to the whole surviving global source rather than only known elements.

## 4. The conditional arithmetic input and resulting bound

The saved BNF outputs return ordinary class groups C3 for 389 and C2 for 37. On their GRH-dependent grade these imply Cl(A)[5]=0 and therefore

    dim_F5 K_chi <= 3.

Both full and quotient-only certification attempts are retained, including their failure markers. They do not make the displayed class groups unconditional. The class-5-zero premise is explicit. An eventual successful quotient-only certificate for either computed group would suffice, without fundamental-unit saturation or an exact class-number equality. It has not been obtained here.

No negative class correction from a provisional quotient is used; no known Sha or Selmer rank is an input. No conclusion that dimension is exactly two or that Sha vanishes is asserted.
