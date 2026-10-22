# Attempts to combine the recovered results

These are checks of explicit mathematical compositions. All seed and imported theorems retain their recorded grades; this is not a fresh certification of every input. No novelty is claimed. A missing arrow in one composition is not a proof that every possible route fails.

## 1. A fixed integral source does not supply the missing image bound

The September 19 [homology construction](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/HOMOLOGY_SOURCE_THEOREM.md) provides an actual finite free lattice

`H = H_1(X_0(N)(C), Z)`, `z_E in Hom(H,Z)`.

The image of `z_E` has index dividing two. The modular parametrization has `c_E | 512`. For each coefficient prime and admissible auxiliary conductor, explicitly weighted cycles satisfy

`phi_(p,S)(z_E) = t(p,S)`.

Thus the source exists before any assumption on Sha, and is primitive at odd coefficient primes. The original proof also states explicitly that this does not imply primitivity of these particular images. Its [integral comparison](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/INTEGRAL_COMPARISON_ATTACK.md) defines the evaluated cycle ideal

`D_(p,k) = < z_E(C_(p,k,S)) : eligible S > in Z/p^k`.

For one fixed nonzero integer A, the two assertions

`D_(p,k) != 0`, `A ((Z/p^k)/D_(p,k)) = 0`

at suitable k for every relevant p give the retained witness-content criterion. This was already an explicit unproved assertion in the September 19 packet.

The later receiver is defined instead from the p-division-point field:

`B_p = Hom_(Gamma_p)(Cl(O_(L_p)[1/p])/p, E[p])`.

The October 4 [local exactness proof](/Users/bsm/BSD_LOCAL_EXACTNESS_PUSH_REVIEW_CODEX_2026-10-04/input/BSD_SECOND_TORSION_LOCAL_EXACTNESS_PUSH_2026-10-03/LOCAL_EXACTNESS.md), with the retained global descent inputs, identifies this with `Sha[p]` outside the stated finite set. It does not identify `D_(p,k)` with the image of a fixed matrix over Z. Nor does it construct an integral map from this receiver into a fixed finite cokernel of the homology lattice.

Consequently the composition cannot apply the gcd-of-minors theorem to the primitive lattice alone. That theorem requires the matrix whose cokernel receives the obstruction, not just an integral source for a scalar witness. No such matrix was constructed here.

The September 24 [Néron theta lattice](/Users/bsm/BSD_NERON_RESEARCH_UPDATE_2026-09-24/repo/supplements/neron-kernel-2026-09-24/sources/cloud/02_DENOMINATOR_LATTICE.md) supplies another substantial integral object. In its notation,

`K_E(z,w) = u_E psi(z) psi(w)`

for integral class-set vectors, with a good-prime unit scale and the fixed clearing denominator `B_theta = 2^10 * 4547`. On the prescribed Gross packet this gives an integer `n_p = B_theta K_E(z_p,z_p)`. A suitable unit value would imply primary vanishing through the retained M2 criterion. The packet `z_p` still varies with p. Integrality of every `n_p`, or primitivity of psi on the whole class set, supplies no theorem that the prescribed packet's image avoids p. Replacing that packet by an arbitrary vector where psi is primitive would change the witness and is not authorized by the comparison theorem.

**Result:** neither fixed lattice, together with receiver exactness, yields a new annihilator or an upper bound. This does not refute the possibility of an additional arithmetic comparison.

## 2. Local exactness cannot replace the global numerator in the Kato bound

The old [local Ota comparison](/Users/bsm/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/LOCAL_REGULATOR_ISOMORPHISM.md) already has integral index one:

`U_S : H^1(K,T)/H^1_f(K,T) -> Z_p[Gamma]`,

and maps the localized Kato element to the Mazur–Tate element. Its last section explicitly leaves the global degree-two image uncontrolled.

The [integral tame factorization](/Users/bsm/BSD_W_MOD_PK_RETURN_FABLE_2026-09-29/WORKING_1.md) and [Corollary S'](/Users/bsm/BSD_W_MOD_PK_RETURN_FABLE_2026-09-29/WORKING_2.md) give a stronger conditional bound. For the actual p-primary group, write its divisible part D and finite quotient F. Under the recorded hypotheses:

- a nonzero divisible part forces every relevant degree-two coefficient to be zero;
- when the divisible part is zero, the coefficient is divisible by `#F` in `Z/p^k`.

Hence a coefficient nonzero modulo p² proves D=0 and `#F <= p`; the retained square-order property for odd-primary finite Sha forces F=0. This is a valid sufficient implication without assuming FIN first.

But this implication was already stated in [the October 4 bound attempt](/Users/bsm/BSD_RECEIVER_LIFTING_PUSH_CODEX_2026-10-04/BOUND_ATTEMPT.md). The independent missing input is its premise for cofinitely many p. Neither G2's unit tame regulator nor W's fixed-p auxiliary independence supplies that numerator.

I checked whether the explicit locally primitive auxiliary point R_p could supply it. R_p does supply the local Kummer line, including when the two rational basis points are locally divisible. Its role in the receiver proof is to kill that local line after restriction, with its quadratic character keeping the global restriction kernel equal to the two known rational-point directions. It does not identify the Kato element with a primitive Mordell–Weil determinant. Substituting R_p into that determinant would replace the rational-point module by a different, quadratically twisted module. No retained theorem identifies their zeta elements.

The [global receiver descent](/Users/bsm/BSD_UNIFORM_ARITHMETIC_HANDOFF_CODEX_2026-10-03/inputs/codex/RECEIVER_DESCENT.md) was also read. Its `H²(Gamma_p,V)=0` argument accounts for the possible exponent-p² extension by a nonlifting argument for the standard representation. I did not find a defect that would justify discarding it. This cohomology vanishing supplies descent, not a class-group multiplicity estimate.

Higher Cassels–Tate layers describe the finite exponents and persistent divisible part of the exact receiver. Formal pairing properties do not bound those quantities. Matching them with the Kato inequality gives the same conditional valuation bound above, not its independent hypothesis.

**Result:** the two local improvements can coexist with the old global bound, but do not prove the cofinite nonvanishing premise. No new criterion is claimed.

## 3. The analytic RS2 object has not been placed in the arithmetic lattice

The October 4 [Laurent construction](/Users/bsm/BSD_RECEIVER_LIFTING_PUSH_CODEX_2026-10-04/rs2/EXPLICIT_LAURENT_CONSTRUCTION.md) and [direct pairing derivation](/Users/bsm/BSD_RECEIVER_LIFTING_PUSH_CODEX_2026-10-04/rs2/PAIRING_AND_HEIGHT_TARGET.md) supply, in their named normalization,

`<H_N,f> = C_N pi^(-3) L(f,2) L''(f,1)`,

`C_N = 270966167197441 / 2168324513321472`.

The construction uses explicit finite dilation sums and parameter differentiation. H_N is a complex cusp form. The separate October 4 review, recovered from the `BSD_ALL_CHAT_ARTIFACTS` attachment and copied into `sources/`, reconstructs these identities and approves their analytic scope. It expressly supplies no rationality or height comparison.

To combine this with the Néron denominator lattice, one must first prove that the relevant normalized H_N is in that lattice, or give a suitable arithmetic realization with proved denominator control. The lattice theorem is for cusp forms arising from the specified integral theta/section construction; it is not a theorem that every complex cusp form has rational coefficients. Rationality of C_N does not prove membership of H_N in this lattice.

Even an appropriate arithmetic realization must still produce the required comparison with the certified period and Mordell–Weil regulator. In the present coordinates the sufficient equality is

`<H_N,f> = 72 C_N pi^(-3) L(f,2) Omega_E Reg(E)`.

Substitution into the displayed pairing gives q_E=36. The left-side construction does not prove this equality. Alternatively the retained Q.1 bound on the reduced rational denominator of q_E would suffice, but neither the fixed theta denominator nor the rational Euler factor is such a bound for q_E.

The September 20 normalization file already removed the product of bad-prime logarithms. The October 4 independent review explicitly withdraws the later description of that rescaling as a new arithmetic input or an overlooked live route. That correction is governing here.

**Result:** an analytic construction and an arithmetic lattice have been located; a theorem identifying the relevant object with that lattice and height data has not been constructed. Completing analytic coefficient evaluation alone would not establish the required arithmetic equality.

## 4. Full-seed accounting

The retained endpoint decomposition is:

1. A cofinite primary-vanishing theorem, plus finiteness at the remaining finite set, proves FIN.
2. FIN does not identify the order. The retained low-prime data imply `#Sha = 9` or `#Sha >= 25281`; excluding the latter still requires additional arithmetic control.
3. Q36 is the separate exact real leading-term equality. Neither FIN nor the numerical interval proves it.

The newer exact receiver is a genuine identification of the unknown group on its domain. It is not itself a bound, and a selected principal-row kernel can remain strictly larger than that receiver. Neither principle can be dropped during assembly.

The retained G2, Kurihara existence, capped-depth, scalar-comparison, and receiver statements remain usable under their exact hypotheses. No conclusion of these statements supplies the unproved premise in the compositions above. I have not shown that some different composition is impossible or that every file has been mathematically reviewed.

**Endpoint change from this turn: none.** These derivations record what was tested so they need not be sold as fresh discoveries again.
