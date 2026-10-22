# Independent local arithmetic review of the uniform valuation proposal

2026-10-20. Same-team written review, not a formal certificate.

**Verdict: the coefficient-place argument is valid, including nonsplit
ordinary extensions. The initial argument at 2 was invalid but has a
uniform repair using wild inertia and the conductor exponent. With that
repair, the proposed primitive S-divisor conclusion is supported under
the retained local representation and incidence inputs.**

I read `UNIFORM_VALUATION_REVIEW.md` and the retained October 15
`general_character/LOCAL_DIVISOR_PROOF.md`. I independently computed the
seed's local invariants below. I did not repeat the other worker's
general multiplicative orbit enumeration or any class-group computation.

## 1. Good ordinary coefficient place: a scalar argument

Let p>=5 be good ordinary and let alpha in F_p^* be the unramified
quotient's Frobenius eigenvalue. In a basis adapted to the formal line,
the residual representation is upper triangular. Inertia has diagonal
characters `(chi_cyc,1)`, with chi_cyc surjective onto F_p^*.

Take a Frobenius lift with diagonal `(a,alpha)`. Choose an inertia
element with diagonal `(alpha/a,1)`. Their product h has the form

```
h = alpha*Id + b*e12.
```

In characteristic p, `h^p=alpha^p*Id=alpha*Id`. Thus the decomposition
group contains the scalar `alpha*Id`. This argument does not require a
splitting of the upper triangular representation or a separate choice
of a transvection to remove b.

If alpha is not 1, every decomposition orbit on nonzero vectors is
stabilized by a nonidentity scalar. Its faithful-character divisor
component is consequently zero. The analogous covector statement also
holds. This is stronger and simpler than correcting the off-diagonal
entry orbit by orbit.

For the seed, rational 2-torsion survives at every odd good prime, making
the point count even. For p>=7 Hasse's upper endpoint is strictly less
than 2p, while the only remaining positive multiple p is odd. Thus p
does not divide the count. At p=5 the exact retained/replayed count is
8. Therefore alpha!=1 throughout this good ordinary domain.

At good supersingular p, the retained level-two fundamental-character
description over Q_p makes inertia transitive on all nonzero vectors.
This independently eliminates the faithful divisor component. No
ordinary filtration is used in that case.

## 2. Additive place 2: correction and repair

Fresh exact GP computation on the governing model gives

```
c4 = 3169004368
c6 = 56243184546880
Delta = 16586638656786071143743744
(v2(c4),v2(c6),v2(Delta),v2(j)) = (4,6,8,4)
elllocalred(E,2) = [3,-5,[1,0,0,0],2].
```

The minimal Kodaira type is I_1^*, and the conductor exponent is 3.
However **v2(j)=4 is nonnegative**: this is potentially good reduction.
The initial statement that it is potentially multiplicative, with a
negative-unipotent inertia element, cannot be retained. At residue
characteristic two, the Kodaira label alone does not justify that claim.

The following argument repairs the conclusion for every coefficient
prime p>=5 without classifying the full inertia group.

1. The tame part of the Artin conductor of the two-dimensional Tate
   representation is at most 2. Since the actual conductor exponent at
   2 is 3, its Swan conductor is positive. Hence wild inertia has
   nontrivial image.
2. Wild inertia is pro-2. Its image in GL_2(Z_p) intersects the principal
   congruence kernel trivially: that kernel is pro-p, and a group that
   is both pro-2 and pro-p is trivial for p odd. The wild image is
   therefore a nontrivial finite 2-group, with injective reduction mod p.
3. A nontrivial finite 2-group contains a nonidentity involution. The
   Weil-pairing determinant is cyclotomic, and the p-adic cyclotomic
   character is unramified at 2. Thus the inertia image has determinant
   one. Over F_p, the only nonidentity involution in SL_2 is `-Id`.

Therefore inertia contains `-Id` modulo p, uniformly on this domain.
Every point-field decomposition orbit is fixed by the scalar -1.
Since the faithful character has chi(-1)=-1, its divisor component
vanishes.

This uses the standard Artin-conductor/Swan description of the elliptic
curve conductor, with the seed's conductor exponent 3. It does not infer
an all-p inertia description from the single p5 point-field computation.

## 3. Additive place 4547

The same exact computation gives

```
(v4547(c4),v4547(c6),v4547(Delta),v4547(j)) = (1,2,3,0)
elllocalred(E,4547) = [2,3,[1,0,0,0],2].
```

The retained type-III potentially good description at residue
characteristic greater than 3 gives tame inertia of order four. Its
square is `-Id`. For coefficient primes p>=5 different from 4547,
reduction does not kill this order-four subgroup. The faithful divisor
component again vanishes.

The prime p=4547 is outside the proposed good-coefficient-prime domain;
no coefficient-place conclusion at that bad prime is claimed.

## 4. Scope of the resulting uniform statement

At the three multiplicative bad places the primitive incidence
normalization, including ramification ratios, is the retained formula.
The exceptional factors are

```
3+1 = 4,
2243-1 = 2242 = 2*19*59,
5843+1 = 5844 = 12*487.
```

Combining those local calculations with the repaired additive and good
coefficient-place arguments supports

```
t_D,chi = 0
```

for good p>=5 outside `{19,59,487}`, for the specified finite ramification
set S of bad primes and p.

This does not assert that faithful divisor modules vanish at every
rational prime. It says that the **kernel of the primitive incidence
divisor map on this S-support** is zero. At split multiplicative places
the nonzero faithful divisor channel can instead be mapped injectively.

Ordinary class-supported virtual units remain after valuations vanish.
Accordingly the complete-source expression still retains

```
((p+1)/2-r_U) + k_C.
```

Neither k_C nor r_U is bounded here. The repair is a valid uniform
elimination of one contribution, not FIN or a complete seed bound.

## 5. Final read of the integrated proof

I subsequently read `uniform_valuation/PROOF.md` in full after the
conductor/Swan repair and the `h^p=alpha*Id` simplification were inserted.
It retains both corrections and the distinction between an injective
primitive-divisor channel and a zero divisor module. Under its explicitly
retained local and source inputs, I support the exact formula
`t_D,chi=1` at `{19,59,487}` and zero at the other good p>=5.

The integrated proof's complete-source expression still contains both
ordinary-unit rank and ordinary-class contribution, and makes no FIN
claim. I found no additional local arithmetic gap in that revised
version. This is a review of the written deduction, not an independent
recertification of the retained global source/image theorems.
