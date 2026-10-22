# The proposed singleton converse needs a local hypothesis

**Verdict: CONVERSE_REQUIRES_ADDITIONAL_LOCAL_INPUT.** The proposed conclusion does not follow just by subtracting one from the classical Selmer dimension. Mazur–Rubin's structure formula measures the **p-strict** Selmer group. At residual precision its dimension can equal the classical dimension, rather than being one smaller.

This is a written source check and deduction, conditional on the retained seed inputs and imported Kolyvagin-system theorems. It neither exhibits a seed counterexample to the unqualified converse nor proves that such a counterexample occurs. The earlier Mechanism B audit remains intact.

## 1. The missing local rank

Fix a good seed prime p >= 5. Let

    S_p = Sel(Q,E[p]),     r_p = dim_Fp S_p,
    lambda_p : S_p -> E(Q_p)/p E(Q_p),
    epsilon_p = dim_Fp im(lambda_p).

Here lambda_p is finite Kummer localization, not singular localization and not the ramification parameter used elsewhere. The retained E(Q_p)[p]=0 implies the local target is one-dimensional. Thus epsilon_p is 0 or 1. By definition, the p-strict group is

    S_0,p = ker(lambda_p),     dim_Fp S_0,p = r_p - epsilon_p.       (1)

There is no unconditional surjectivity in (1). Kim §2.1.6 explicitly distinguishes the canonical p-relaxed structure from its dual p-strict structure. Section 5, especially (5.1), retains precisely this localization difference.

## 2. What the primitive-system theorem actually says

Use the residual Kato system kappa^(1), with classes obtained by reducing coefficients to E[p]. Do not confuse these classes with nonzero classes at some higher p-power precision.

Kim Proposition 2.10, citing Mazur–Rubin Proposition 4.5.8, gives

    partial^(s)(kappa^(k)) = min{k, j + sum_(i>s) d_i},

where the d_i are the elementary-divisor lengths of Sel_0(Q,E[p^k]). For a primitive residual system take k=1 and j=0. If d = dim_Fp S_0,p, then d_i=1 for i<=d and d_i=0 afterwards. Therefore

    partial^(s)(kappa^(1)) = 1 for s<d, and 0 for s>=d.

In a vector space a nonzero class has divisibility 0 and a zero class has capped divisibility 1. Consequently

    min{nu(n): kappa_n^(1) != 0} = d = r_p - epsilon_p.             (2)

This is the residual statement; Kim Theorem 2.13(5), concerning the corank at p-infinite precision, is not a substitute for it.

Primitivity is available at the retained B.20/import grade: a mod-p unit Kurihara number somewhere, together with Kim Theorem 3.11 and t=0, yields a nonzero residual Kato class somewhere. This is exactly residual primitivity, not primitivity at a prescribed singleton. No new main-conjecture theorem is asserted here.

The prime-system conventions matter. Formula (2) is used with the admissible Kolyvagin primes of the structure theorem, whose rank-one local theory is required. It must not be extended by simply treating identity residual Frobenius as a rank-one local situation. The cyclic singleton refinement below uses explicit regular-unipotent detection.

## 3. Consequences when the classical dimension is two

Combining (1) and (2) gives the following cases under primitivity:

| r_p | epsilon_p | dim S_0,p | First nonzero residual Kato-class length |
|---|---|---|---|
| 2 | 1 | 1 | 1: a singleton exists |
| 2 | 0 | 2 | 2: every singleton is zero |

The retained B.21 has first unit **Kurihara-number** length r_p=2 in both rows. The difference between the first class length and the first unit-witness length is therefore epsilon_p, not automatically one.

In particular, the assertion “the first nonzero classes occur exactly one level below the first unit witness” needs epsilon_p=1. Primitivity alone does not supply that condition.

### Cyclic auxiliaries in the positive case

Suppose dim S_0,p=1, and let c generate it. The regular-unipotent affine detector from the previous audit gives a cyclic prime a at which c has nonzero finite localization. Set D=S_0,p and P=Sel_rel(Q,E[p]); under the Weil identification D is a subspace of P, and these are dual Selmer structures.

The localization P -> H_f^1(Q_a,E[p]) is surjective because c already maps nontrivially. Poitou–Tate duality for strict versus finite conditions on P at a says that relaxing the a-condition on D adds no global classes: the possible new singular localization is annihilated by the whole finite line. Hence D_(a-relaxed)=D. Imposing transverse instead of finite now gives

    D_(a-transverse) = ker(D -> H_f^1(Q_a,E[p])) = 0.

Thus a is a residual core vertex. The primitive residual stub theorem (Kim Theorem 2.7 and Proposition 2.9 in its finite-coefficient form) makes kappa_a^(1) a generator of the one-dimensional relaxed Selmer module at a. In particular kappa_a^(1) is nonzero. This provides a cyclic singleton; no unproved scalar finite-singular isomorphism at an identity-Frobenius prime is used.

Conversely, if a cyclic singleton is nonzero, (2) gives dim S_0,p <= 1. The retained rank two gives r_p >= 2, while epsilon_p <= 1, so (1) forces r_p=2 and epsilon_p=1. Equivalently, at these retained grades,

    some nonzero cyclic residual singleton
        <=> [dim Sel_p = 2 AND lambda_p != 0].                    (3)

The equality with dim Sel_p=2 alone is not established. Nor is a seed prime with dim Sel_p=2 and lambda_p=0 established here.

## 4. Why a p-adic rank argument does not remove the condition

An infinite-order rational point has nonzero p-adic logarithm, but its image in E(Q_p)/pE(Q_p) may still be zero. Being nonzero over Q_p is not the same as being primitive in the integral local lattice.

The elementary lattice map Z_p^2 -> Z_p given by (x,y) -> p*x has rank one over Q_p and zero reduction modulo p. It illustrates the exact integral distinction; it is not asserted to be the seed's localization map or a complete arithmetic countermodel.

If Sha[p^infinity]=0, then S_p is the rational-point Kummer subspace. At such a prime, epsilon_p=1 says that at least one rational Mordell–Weil generator is **not** divisible by p in E(Q_p). If both generators are locally p-divisible, epsilon_p=0. Neither the global rank nor absence of local p-torsion proves that this cannot happen. No local-divisibility computation, or theorem excluding it for this seed outside finitely many p, was supplied or proved in this check.

## 5. Recommended correction to the record

Replace the proposed fourth-equivalence inference with:

> Mazur–Rubin's residual primitive-system formula places the first nonzero Kato class at length dim Sel_0(Q,E[p]), where Sel_0 is p-strict. Writing epsilon_p for the rank of finite localization Sel_p -> E(Q_p)/p, that length is dim Sel_p - epsilon_p. Thus a cyclic singleton exists when dim Sel_p=2 and epsilon_p=1; if dim Sel_p=2 but epsilon_p=0, the first residual classes occur at length two instead. We have not proved the required localization nonvanishing uniformly for the seed, so singleton nonvanishing is not yet a fourth equivalent formulation of the endpoint.

This does not show the singleton route is easier or harder computationally. It shows exactly which additional assertion is needed before calling it equivalent. No new research session, prime run, release edit, message or push was performed.

## Source and scope record

- [Kim, arXiv:2203.12159v6](https://arxiv.org/html/2203.12159v6), §2.1.6; Theorems 2.6–2.7; Proposition 2.9 and primitivity definition; Proposition 2.10; Theorem 2.13(5); Theorem 3.11; §5.2 equation (5.1). Read from the pinned PDF text and checked against the primary HTML. Proposition 2.10 attributes its formula to Mazur–Rubin Proposition 4.5.8.
- Previous audit's `CYCLIC_DETECTION_REPAIR.md` and `REPORT.md` retain the scalar lemma, local conditions and cyclic detector. No original file was changed.
- Direct attempts to retrieve the Mazur–Rubin 2004 book from Rubin's author-hosted links failed. Accordingly the structural theorem is imported through Kim's explicit statement and attribution, not represented as a fresh audit of the original book proof.
- B.20/B.21 and the seed's rank/local-torsion inputs remain retained/imported inputs. This check does not re-audit their deep proofs or numerical certificates.

FIN, ORDER9 and Q36 are unchanged.
