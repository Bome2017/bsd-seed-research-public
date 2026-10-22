# Scalar-compatible sources have no permanently invisible split-prime kernel

Date:2026-10-15. Written deduction under the explicit-descent module realization and residual-image inputs. No novelty claim, bound on Selmer dimension, or new coefficient-prime conclusion.

## 1. Why this question arose

The previous experiment correctly warned that a general element of the affine-line field B can be a noncube in B but become a cube in the full torsion field K. Consequently, zero residues at primes splitting in K are not automatically enough to prove that an arbitrary B-element is a cube in B.

The warning is too broad when applied to the **actual norm image of a scalar-compatible descent source**. The homogeneous character condition excludes that restriction kernel. This improves the completeness argument for the proposed detector; it does not improve its bound on the number of genuine classes.

## 2. Exact source modules

Let p be odd, V=E[p], K=Q(E[p]), G=Gal(K/Q), and assume -I belongs to G. The retained full-image hypothesis implies this. K contains mu_p by the Weil pairing.

Let A be the nonzero-torsion-point etale algebra and B the affine-line etale algebra of Schaefer--Stoll section7. Put

    M = mu_p(Abar)^(1),   N = mu_p(Bbar)^(1).

The superscript denotes the central character on which aI acts as multiplication by a. Lemma7.2 identifies H^1(Q,M) with the scalar-compatible part of A*/A*^p. Lemma7.6 gives the Galois-equivariant affine norm map u:M->N and exact geometric kernel V. Proposition7.10 realizes this map arithmetically as the incidence-algebra norm. These are the actual modules, including the cyclotomic action; they are not untwisted permutation modules.

In particular, -I acts as -1 on M and N. The order-two central subgroup C=<-I> has invertible order on p-torsion modules. Its positive-degree cohomology vanishes by averaging, and M^C=N^C=0. The Hochschild--Serre spectral sequence for C in G therefore gives

    H^i(G,M)=H^i(G,N)=0 for all i>=0.

Only i=1 is needed below.

## 3. Restriction is injective on the full scalar-compatible source

Since G_K acts trivially on M, inflation--restriction supplies

    0 -> H^1(G,M) -> H^1(Q,M) -> H^1(K,M)^G.

The left term is zero. Thus restriction to K is injective on the **entire** scalar-compatible source, including elements that fail the global norm or Selmer local conditions.

Likewise H^1(Q,N)->H^1(K,N) is injective. Therefore, for scalar-compatible alpha,

    res_K(u(alpha))=0  iff  u(alpha)=0.

If B is a field inside K, this says: the actual norm b of alpha cannot be a noncube in B that becomes a cube in K. It does not say that restriction is injective on all of B*/B*^p. The homogeneous direct summand and the simultaneous scalar condition are essential.

Corollary7.9 then identifies u(alpha)=0 with the genuine global H^1(Q,V) admission condition. No Sha finiteness, local point rank, or analytic L-value enters this implication.

## 4. A finite separating set exists for an entire finite source

Let U be any finite-dimensional scalar-compatible subspace, and let E_q denote the full source residue-character evaluation at a good rational prime q splitting completely in K, excluding the finitely many ramification and denominator primes. Suppose alpha is nonzero in U. Its restriction to G_K is a nonzero continuous homomorphism into M. The finite Galois extension obtained from its Kummer coordinates has an element on which this homomorphism is nonzero. Chebotarev supplies an eligible split rational prime with that Frobenius conjugacy class. Conjugation changes the local M-coordinate by an invertible action and cannot turn a nonzero value into zero. Thus E_q(alpha) is nonzero at some such q.

It follows that

    intersection over eligible q of ker(E_q|U) = 0.

Finite dimensionality gives a finite collection Q for which stacked E_Q is injective on all U. Greedily choosing a prime that lowers the current kernel proves an existence bound of at most dim U blocks; it does not bound the primes searched or their sizes. No statistical independence of successive primes is used.

For a point subspace W subset U, use the ambient full residue space as target:

    D_Q: U/W -> (direct sum of M-coordinate residue spaces)/E_Q(W).

False global candidates in U need not have values in the smaller two-dimensional local E-Kummer image. Only after genuine Selmer admission may one restrict the target to the sum of those local Kummer images. The calculation on the entire scalar source is made in the ambient target. The common-point detector has kernel, pulled back to U,

    Z_Q = W + (U intersect ker E_Q).

Hence some finite Q gives Z_Q=W, even if U contains false global candidates. This refines the prior proof review's caution about an arbitrary oversized source: for a **certified scalar-compatible** source with -I in the image, eventual raw split-prime separation is guaranteed. It is not guaranteed by this proof for arbitrary multiplicative source elements before scalar screening.

The same argument applied to the finite norm image u(U) proves eventual completeness of split-prime norm rejection. Finite observed zeros alone still do not certify a cube. Positive exact cube roots or an independently established image/kernel dimension are required for an effective certificate of completion.

## 5. What this does not bound

If U is certified to contain every Selmer class, a verified Z_Q=W proves that no unknown class is invisible to that particular detector. Nonzero detector images may still contain arbitrary excess. The theorem supplies no independent small bound on those images, on dim U as p varies, or on the class-group and unit indices needed to construct U.

If U is incomplete, separation of U cannot exclude a class omitted from U. In particular, this theorem does not upgrade the 28042a1 or historical seed source-completeness grades. The three BSD seed endpoints remain unchanged.

## 6. A sharp p=3 countercontrol outside the homogeneous source

For a short model y^2=x^3+a x+b with full GL2(F3) image, let m be the generic affine-line slope. The line field satisfies

    m^8 + 2a m^4 -4b m^2 -a^2/3 =0.

Its incidence cubic is

    X^3-m^2 X^2+(m^4+2a)X-(m^6+2a m^2-4b).

Writing its depressed coefficients as P,Q, exact simplification gives

    Q^2/4+P^3/27 = ((a+3m^4)(3a+m^4)/(18m^2))^2.

One Cardano term is -8m^2(m^4+3a)/27. Thus the splitting field K is B(mu_3,cuberoot(h)), with h=m^2(m^4+3a), since -8/27 is a rational cube. Irreducibility of the incidence cubic makes h a noncube in B. It becomes a cube in K, illustrating the restriction kernel on unrestricted B*/B*^3.

But h is fixed by m->-m. Its class belongs to the even component. Actual norms from the odd source satisfy b(m)b(-m) in B*^3. A nonzero multiple of the even class [h] cannot satisfy this odd condition because 2 is invertible modulo3. This explicit calculation agrees with the general homogeneous-module proof. The generic formulas assume the nonsingular full-image line-field situation; no degenerate zero denominator is silently included.

Primary source read in this run: Schaefer--Stoll, How to do a p-descent on an elliptic curve, Lemmas7.2 and7.6, Corollary7.9, Proposition7.10 and section10.1, from the bound local PDF/text cache. Full residual image and authenticated scalar source realizations remain retained arithmetic inputs. Finite module/symbolic checks are supporting controls, not a replacement for the written argument.
