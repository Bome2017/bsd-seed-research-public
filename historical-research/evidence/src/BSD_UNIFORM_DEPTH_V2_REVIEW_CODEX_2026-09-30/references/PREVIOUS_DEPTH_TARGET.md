# The exact depth target, and a broader sufficient character test

Status: **WRITTEN_DEDUCTIONS_FROM_RETAINED_AND_IMPORTED_INPUTS**. No uniform low-depth bound is proved.

## 1. What the minimal unit length measures

For a good prime p>=5 let

    r_p = min { number of prime factors of n : delta_n is nonzero mod p },

with the Kurihara quantities and admissible conductors of Castella–Sano section 1.1. Let

    X_p = Sel_{p^infinity}(E/Q)^dual,
    d_p = dim_Fp X_p/pX_p.

The application in `NEW_INPUT_APPLICATION.md` gives M_infinity=0 and r_p finite. Kim, arXiv 2203.12159v6, Theorem 1.8 supplies the higher Fitting ideals of X_p in terms of the Kurihara valuations. Its assertion does not assume Sha finite.

The seed has root number +1. The functional equation makes delta_n zero for odd numbers of auxiliary primes (Castella–Sano section 1.1.3). Kim's structure theorem therefore writes X_p as a free module of even rank rho_p together with paired finite cyclic factors:

    X_p = Z_p^(rho_p) + direct_sum_i (Z/p^(a_i))^2,  a_i>0.

For a finitely generated module over Z_p, its i-th Fitting ideal is the whole ring exactly when i is at least its minimal generator number d_p. Kim identifies, for the relevant even i,

    Fitt_i(X_p) = p^(M_i-M_infinity) Z_p = p^(M_i) Z_p.

Both d_p and the indices of possible nonzero Kurihara quantities are even. It follows that

    r_p = d_p = dim_Fp Sel_p(E/Q).

The last equality uses E(Q)[p]=0. This is a deduction from the stated structure theorem, not a bound on either side.

The dual Kummer sequence splits as Z_p-modules:

    0 -> Sha[p^infinity]^dual -> X_p -> Z_p^2 -> 0.

Consequently

    r_p = 2  <=>  Sha(E/Q)[p^infinity] = 0.

Nakayama's lemma kills the entire finitely generated primary-Sha dual here, including a hypothetical positive free rank. No finiteness assumption on Sha is inserted.

The uniform task is thus r_p=2 for all p outside one finite set. By parity it is enough to prove r_p<4. Merely proving r_p finite, or bounding it by a larger constant such as 4 or 6, is insufficient.

## 2. Why main-conjecture primitivity does not finish the argument

An abstract module illustrates the precise loss:

    X = Z_p^2 + (Z/p)^2.

It has corank two and even parity, but needs four generators. Its higher Fitting ideals are

    Fitt_2(X)=(p^2), Fitt_3(X)=(p), Fitt_4(X)=Z_p.

The pattern M_2=2 and M_4=M_6=...=0 is compatible with M_infinity=0. A primitive witness exists at length four while the quadratic one is divisible by p. This is a module countermodel to the proposed inference, not an elliptic-curve example or a disproof of BSD.

This also prevents conflating three distinct quantities: Mordell–Weil rank, the first nonzero p-adic Kato/Kurihara index, and the first mod-p unit index. In particular, the strict-corank remark in Kriz–Nordentoft cannot be used to replace the unit index by 2 without checking this distinction against the cited theorem. Kim's explicit Fitting formula is the governing statement used here.

## 3. A sufficient target that permits composite conductors

The previous singleton target is not compulsory. Let p>=5 be good for this seed and let K/Q be any real cyclic extension of degree p whose conductor m is prime to pN. For the direct comparison to the retained tame framework one may take m squarefree. Let theta_K be the full, BH-normalized projected Mazur–Tate element. For a faithful character chi, put lambda=zeta_p-1, normalized by v_lambda(lambda)=1.

Then the following sufficient criterion holds at the imported grades:

    v_lambda(chi(theta_K)) < 4
        => Sha(E/Q)[p^infinity]=0.

It is enough to establish such a value for each p outside a fixed finite set. K and m may vary with p. The conductor need not be prime, the auxiliary primes need not be G2 primes, and the value need not be 288 times a regulator.

### Proof

Bullach–Honnor Theorem 1.4(b) puts theta_K^# in the zeroth Fitting ideal of

    Y = Sel_{p^infinity}(E/K)^dual

over R=Z_p[C_p]. Large image is retained. The field is real and unramified at p, so the relevant roots-of-unity hypotheses are met. This applies to the classical Selmer object and does not assume Sha finite.

Set A=R/pR=F_p[t]/(t^p), t=gamma-1, and let d be the minimal number of generators of Y/pY over A. A minimal presentation has entries in (t); its maximal minors imply

    Fitt_0,A(Y/pY) subset (t)^d.

Fitting ideals commute with reduction. Write theta_K in powers of t. Since p has lambda-valuation p-1>=4, a character value of lambda-valuation d_0<4 has a coefficient that is a p-unit at degree d_0. Indeed terms with p-divisible coefficients have valuation at least 4, and distinct degrees below 4 have distinct lambda-valuations. Inversion # preserves this lowest degree. Thus d<=d_0<=3.

Full residual image gives E(K)[p]=0: the representation restricted to an abelian extension still has no fixed vector (its image contains the commutator SL_2). Restriction of classical Selmer groups is injective, since local Kummer conditions are preserved. Dualizing gives

    Y_G ->> X_p,

and hence d_p<=d<=3. Section 1 supplies even parity of d_p for this seed, without assuming Sha finite. Rank two gives d_p>=2. Therefore d_p=2 and the split Kummer sequence plus Nakayama gives the conclusion.

### Boundaries

- The strict inequality matters. A degree-four Fitting element is compatible with four Selmer generators; a bound <=4 is not sufficient.
- The direct degree-two BH test itself does not require the new CLW input. We used Kim plus all-good-prime Kurihara existence to justify the even-parity relaxation to degree at most three without importing a separate parity theorem.
- Keep the algebraic normalization theta_K. Translating an L-value estimate requires its actual Birch–Stevens/Gauss/period factors; nonzero complex L-values alone do not meet this test.
- This argument does not prove that a low-depth character exists. It broadens the allowed object for the outstanding estimate.

## 4. Where Kriz–Nordentoft stops

In arXiv 2310.20678v3, Corollary 5.16 takes a mod-p unit Kurihara quantity of length r as input and obtains a horizontal measure with mu=0 and lambda-invariant at most r. Corollary 5.20 then produces order-p characters with a valuation bound involving r/(p-1).

The process propagates a supplied depth bound; it does not independently lower r to two. Replacing the older ordinary-only existence input with `NEW_INPUT_APPLICATION.md` extends this machinery to all good primes, but leaves r_p uncontrolled.

Constants depending on p in an asymptotic count are not by themselves an obstacle to the desired all-p existence statement: the conductor cutoff may depend on p. The decisive missing bound is the normalized depth, below 4, under one argument covering the prime set.

The current horizontal moment results and residual distribution results inspected do not provide that bound without a low-depth input. Re-running their known implications is not a new construction.

FIN, ORDER9 and Q36 are unchanged.
