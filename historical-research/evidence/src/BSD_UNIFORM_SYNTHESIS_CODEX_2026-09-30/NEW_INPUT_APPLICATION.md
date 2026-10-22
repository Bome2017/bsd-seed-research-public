# A source update that removes the separate supersingular coverage gap

Status: **SOURCE_UPDATE_APPLIES_AT_RETAINED_INPUT_GRADE**.

This is a written application of imported preprint theorems, not a reproof of those theorems or a new finite-support theorem. No primary component is newly computed or shown to vanish here.

## 1. The precise source change

Castella–Liu–Wan, *Kato's main conjecture for nonordinary modular forms*:

- arXiv 2608.29470v1, August 29, 2026, 44 pages: Theorem A requires squarefree level.
- Author-hosted `CLW2.pdf`, dated September 21, 2026, 45 pages: Theorem A has no squarefree-level requirement. At weight two it instead admits a prime q exactly dividing N at which the residual representation is ramified. The alternative root-number hypothesis is not needed for this application.

Both versions are saved and separately hashed in `sources/`. The current author version was obtained through the link on Castella's research page, which explicitly warns that its versions may be newer than arXiv.

The project's `BSD_BUILD_MAP/V025_CANDIDATE_EDITS_2026-09-29.md`, section 6, was waiting for exactly a non-squarefree version. The previous squarefree obstruction was valid for the older statement; it should not be applied to this new statement.

## 2. Seed hypotheses, for every good supersingular p >= 5

The retained minimal model is

    [0,-1,0,-66020924,-65074271436],
    N = 2^3 * 3 * 2243 * 4547^2 * 5843.

| Hypothesis | Seed verification |
|---|---|
| Newform on Gamma_0(N), trivial nebentypus | Modularity of the retained elliptic curve; weight k=2 |
| Good nonordinary p | Precisely the supersingular primes under consideration, p not dividing N |
| Fontaine–Laffaille range | 2 < p |
| Large image, a standing hypothesis before Theorem A | Retained surjectivity of E[p] for every odd p, and its p-adic consequence for p>=5 |
| (ram) | q=2243 exactly divides N; retained split multiplicative type I_1 |
| p-regular | For supersingular p>=5, a_p=0 by Hasse's bound; X^2+p has distinct roots in characteristic zero |

The (ram) check does not require a search for q depending on p. The Tate extension at 2243 has parameter of valuation 1. Its mod-p inertia class is therefore nonzero for every p different from 2243. This is the usual multiplicative-reduction ramification criterion, applied with valuation 1.

An independent exact-integer calculation on the displayed model gives

    Delta = 16586638656786071143743744,
    c4 = 3169004368,
    v_2243(Delta) = 1,
    c4 mod 2243 = 2005.

See `SEED_LOCAL_CHECK.json`. This checks the local input, not the retained all-prime image theorem. In particular, no claim is made about applying the good-prime theorem at p=2243, 4547 or 5843.

## 3. The character and integral-normalization bridge

An untracked twist or congruence factor could invalidate a mod-p conclusion. The source supplies the required bridge:

1. CLW section 2.1 uses V_f with Hodge–Tate weights 0 and 1-k. At k=2 the elliptic-curve realization is T_f(1), corresponding to T_pE with the usual modular comparison.
2. Theorem A proves Conjecture 1.1 on the omega^(k/2) component. At k=2 this is omega, not the trivial component of the untwisted representation.
3. Remark 2.20 identifies Conjecture 2.19 at eta with Conjecture 1.1 at eta*omega^(k-1). Thus the supplied theorem gives Conjecture 2.19 at eta=1 on T_f(1), the required cyclotomic component.
4. CLW section 2.4 defines the integral Kato element using gamma_f^+ + gamma_f^-, generators of the canonical quotient lattice. It is not defined using the subspace generators delta_f^+ + delta_f^-. Lemma 2.10 distinguishes them by the congruence ideal. One must not replace gamma by delta and then assume that ideal is a unit.
5. CLW section 5.6, equations (5.18), (5.21)–(5.22), explicitly gives the imprimitive Euler product and the equivalence to a determinant-basis assertion, citing Castella–Sano Proposition 2.2.3. For k=2 the component there is eta=omega^(1-k/2)=1, agreeing with step 3.
6. Castella–Sano section 2.2 uses T=T_pE and the same S-imprimitive convention: multiply the primitive Kato element by the Euler factors at primes dividing N. Their Proposition 2.2.3 identifies this determinant assertion with the characteristic-ideal formulation of Kato's conjecture. The retained modular/Manin input is p-integral with p-unit denominator at good p>=5; the seed's c_phi divides 512. The large residual image excludes a p-isogeny ambiguity.

This uses the general determinant equivalence, not CLW's subsequent rank-zero specialization. Equations involving a finite H^2 cardinality in their rank-zero application are **not** imported into rank two.

## 4. Consequence using Castella–Sano

Use Castella–Sano, arXiv 2601.14504v1, Theorem A and Corollary A. Their ordinary-prime Theorem B already covers this seed. Their older supersingular squarefree clause is now replaced by the CLW application above, through their general Theorem A.

For the seed, Tam_E=16 and p does not divide c_phi at every good p>=5. Consequently, at the stated import grade,

    for every good p >= 5,
    M_infinity(delta) = 0,
    and there is a squarefree Kato conductor n with delta_n nonzero mod p.

The Kato auxiliary primes satisfy q=1 mod p and a_q=2 mod p. They are not G2's Frobenius-minus-identity auxiliaries. No direct substitution of a G2 regulator for delta_n is asserted.

This conclusion includes both ordinary and supersingular primes. It has one argument with all-prime coverage, while the conductor n is allowed to depend on p.

## 5. Exact scope of the improvement

What was missing before: a usable nonordinary main-conjecture input for this non-squarefree conductor, needed to guarantee some mod-p Kurihara witness at supersingular p.

What is supplied now: that input and its consequence, existence of some finite-length witness at every good p>=5.

What is still missing: a bound putting such a witness at length two, or another independently proved low-depth bound sufficient to kill excess Selmer classes. The main conjecture does not supply that bound. `DEPTH_TARGET.md` makes this distinction exact.

This does not automatically regrade every historical claim involving an E11 scalar named x_Q: that scalar's lattice and Euler-factor conventions would have to be matched separately. The conclusion here concerns the precisely defined Kurihara numbers in Castella–Sano/Kim.

Underlying deep proofs remain preprint imports. This application should receive an independent check before integration into the release. No publication, novelty, or full-source-reproof claim is made.

FIN, ORDER9 and Q36 are unchanged.
