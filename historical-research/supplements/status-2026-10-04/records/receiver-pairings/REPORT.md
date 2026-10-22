# Seed push: receiver audit and explicit RS2 construction

Date: 2026-10-04.

**Uniform research verdict: NO_BOUND_MECHANISM from the inputs and mechanisms checked in this pass.**

**Review verdict: PAIRING_AUDIT_CONFIRMED_AT_RETAINED_INPUT_GRADE.**

**RS2 construction verdict: EXPLICIT_LAURENT_CONSTRUCTION_DERIVED; HEIGHT_COMPARISON_OPEN.**

The continuation requested by the user produced a written solution of the specific level-N Laurent-expansion task in the supplied RS2 note. Both Eisenstein factors are now expressed as finite combinations of full-level series; their required coefficient is given explicitly. A separate direct unfolding reconstructs the pairing constant without the earlier cross-cusp normalization caveat. These are analytic results, not Q36, a denominator bound, or a uniform Sha bound. See `rs2/RETURN.md` for the usable construction and its exact endpoint limit.

The uploaded pairing argument is sound at its stated scope. It does not give an independent upper bound. I tested its combination with the project's integral tame factorization, and checked an applicable published uniform divisibility theorem. Neither supplies the missing estimate. No new seed primary vanishing, uniform vanishing, or fixed annihilator was obtained.

## What was checked

1. The uploaded archive passes CRC checking and all **13/13** entries of its own manifest. Its 24 paired-group controls reproduce **byte-for-byte**. These are abstract algebra controls, not seed computations.
2. The ordinary Weil cup product of two Selmer classes vanishes by local Kummer isotropy and global Brauer injectivity. This supplies no extra membership condition.
3. The secondary pairing and higher lifting filtration have the stated radicals. The pairing detects finite layers of actual Sha; it does not eliminate them. Divisible directions survive every layer. See `REVIEW.md`.
4. I combined these layers with the retained integral result, **Corollary S′** in `context/WORKING_2.md`. A nonzero quadratic tame coefficient modulo p² would indeed imply vanishing of the entire p-primary Sha group. However, this implication is already in the record, and none of the checked inputs proves its premise for almost all p. See `BOUND_ATTEMPT.md`.
5. Çiperiani–Stix give an applicable uniform divisibility theorem, but its division takes place in the larger Weil–Châtelet group. It does not supply the higher Selmer lifts required here. See `AMBIENT_LIFT_SCREEN.md`.

## What the parts actually assemble into

The receiver identifies the group whose disappearance is needed. The pairing describes how its finite part is distributed among p-power layers. The integral factorization gives a conditional size bound if a sufficiently small valuation of an arithmetic coefficient can be established independently.

**The absent input is still that independent estimate, or an independent relation-rank/annihilator theorem.** This pass has neither constructed one nor found one in the narrowly checked sources. A theorem that merely identifies the receiver, produces principal rows, or supplies pairings does not establish it.

The user's admission rule remains applicable to uniform work: a further attempt must name its proposed bound theorem and a concrete arithmetic input toward proving it. The four categories in the strategic note are admissible forms of an answer, not four presently constructed methods. The user subsequently supplied the specific RS2/Q36 construction, which was pursued in this same pass rather than treated as a uniform-bound theorem.

## What the RS2 continuation added

The archive already removed the logarithmic denominator in `RS2_NORMALIZED_A2_VERDICT.md` on September 20. Its later L3 return had also corrected the Fourier sparsity from 9094 to 18188 and had not established the height comparison. Thus the user's October 4 normalization note is not, by itself, a new result.

The present derivation supplies a more explicit construction. With `V_d F(z)=F(dz)`, it proves

\[
D_N(s)E^*_{2,0,N}(z,s)
=N^{-s}\sum_{d\mid\operatorname{rad}N}\mu(d)d^{-s}E_2^*(dz,s).
\]

There are 32 terms for the seed. A corresponding Fricke formula handles the first factor. Taylor differentiation through order three and an explicit Bernoulli polynomial give the exact requested `mathscr A_N`. The pole orders and sparsity follow directly. The rational seed constant is

\[
C_N=270966167197441/2168324513321472.
\]

Direct unfolding, integration by parts and the local Hecke recurrence recover the seed pairing with its sign. These steps do not use an assumed Q36 identity. The construction is written and checked, but not independently certified by another researcher.

Exact controls pass for 7200 Fourier-depletion instances, four Bernoulli polynomial controls, 220 local Euler coefficients and the seed rational constants. Six numerical comparisons with independently truncated Ramanujan series meet their analytic tail bounds; two numerical Mellin integrations agree. The numerical controls use high precision, not interval arithmetic. None computes a seed primary component.

This closes the analytic Laurent task, not the old L3 improper-integral continuation or the arithmetic height comparison. In particular, a finite-dimensional complex cusp space and a rational Euler constant do not supply rationality of the projected scalar. The desired equality with the global Mordell--Weil regulator remains an unproved arithmetic theorem. No automatic coefficient-production campaign follows from the derivation.

## Precision corrections to the strategic note

These corrections concern the pasted planning text, not blocking defects in the uploaded pairing proof:

- `dim Hom_Gamma(A,V)` counts copies of V in the **semisimple head** of A, since `End_Gamma(V)=F_p`. It need not equal the total composition-factor multiplicity in A. The group algebra is not semisimple here.
- Principal relations vanish on every actual receiver map. Their rank is measured on a larger space of candidate functionals; they do not acquire nonzero rank *on* the receiver itself.
- A raw divisor-space codimension is not the relevant dimension. The sufficient test is the dimension of the correctly defined standard-functionals kernel. Cyclicity over an unspecified algebra is not a dimension bound either.
- The earlier injection `Sha[p] -> B_p` was already enough to transfer an upper bound. Exactness removes ambiguity about what survives, but is not itself a new source of that upper bound.

Details and a minimal modular-representation example are in `STRATEGY_PRECISIONS.md`.

## Custody and limitations

The archive's own historical checks of a previous 50-entry review and its 30-entry nested packet are preserved as input receipts; this pass does not claim to have freshly replayed them. The seed's residual image, saturated basis, receiver descent, parity, and the full integral tame factorization retain their previous grades. In particular, the bound attempt is conditional on that retained factorization, not a fresh audit of every BKS import.

The 24 new accounting checks use the same 24 abstract paired groups as the uploaded controls. They are not an additional independent population of arithmetic examples. No seed field, class group, new auxiliary-prime certificate, or production job was computed. Nothing was pushed or sent to another person or session.

FIN, ORDER9 and Q36 are unchanged.
