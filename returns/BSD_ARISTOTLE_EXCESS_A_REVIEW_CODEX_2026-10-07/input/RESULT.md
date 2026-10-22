# RESULT — Aristotle lane A, 2026-10-07

**Primary status: NO_BOUND_MECHANISM_FOUND_FOR_TESTED_CANDIDATES.**

FIN, ORDER9 and Q36 are **unchanged**. No new cofinite bound on
`dim_Fp X_p` (`X_p = Sel_p(E/Q)/W_p = Sha(E/Q)[p]`), no annihilating ideal,
no vanishing prime and no cross-prime nonvanishing statement was obtained.

Context: as far as this run knows, finiteness of Sha (or even of
Sha[p] for all but finitely many p) has not been proved unconditionally for
any elliptic curve over Q of analytic rank >= 2. That is the open problem
this lane is aimed at. The run did not find a mechanism that solves it for the
seed, and it does not claim that no mechanism exists.

## Candidates tested (details in CONSTRUCTION.md, collisions in COLLISION_CHECK.md)

| # | Candidate (source) | Control map to X_p | Information beyond retained identities | First failed arrow |
|---|---|---|---|---|
| A1 | Anticyclotomic Λ-adic Selmer complex over K=Q(√-23), with higher Fitting / Euler-system ideals Θ_i (the source suggested by TASK.md) | Exact augmentation (T=0) base change of the Selmer complex. H^2 is retained: 0→H^1_Λ/T→H^1(K,T)→H^2_Λ[T]→0 and H^2(K,T)=H^2_Λ/T | The augmentation image of Θ_1, i.e. the classes **κ_ℓ mod p** of one-prime derived Heegner classes | No theorem bounds v_p(κ_ℓ) for even one ℓ uniformly in p. The Λ-adic ideal adds nothing at T=0 beyond the classical Kolyvagin system (countercontrol Y_e) |
| A2 | Classical Kolyvagin structure theorem (Kolyvagin 1991; Zhang's Lemma 8.4 form) | ν_p = max(s⁺,s⁻)−1. Where s⁻ = 1: ν_p=1 ⇔ Sha(E/Q)[p]=0 | Nonvanishing mod p of one κ_ℓ | Same arrow as A1. Collision: HEEGNER_NU.md (`nu_le_two_iff_sha_of_twist`) and the continuation return's ι(ℓ) |
| A3 | Cyclotomic Kato divisibility + Perrin-Riou/Schneider leading term (good ordinary p) | dim Sha[p] <= v_p(L_p^*) − v_p(R_p/p^2) − v_p(local factors) | p-adic L-function leading term L_p^* and normalized p-adic regulator R_p/p^2 | Needs R_p/p^2 to be a unit and L_p^* to be bounded, both uniformly in p. The first is the forbidden "wild-regulator unit". The second has no formula independent of p-adic BSD. Also ordinary-only |

The new content is a **written identification** (A1 → A2): the "particular
generator/minor" that TASK.md asks for in the higher-Fitting source is the
augmentation image of a one-prime derived Heegner class. Controlling it is
equivalent to the target on the cofinite set where the twist Selmer
dimension s⁻ is 1. So the higher-Fitting source reduces to the already recorded
derived-Heegner wall and **does not give independent control**. This is a
reduction of the candidate, not a bound. It is graded *written, unreviewed*.
The Da Ronche–Longo–Vigni paper itself is not in the archive (see SOURCES.md).

All three candidates fail at one common arrow: a **uniform-in-p
nonvanishing mod p of a p-dependent second-order arithmetic quantity**
(κ_ℓ mod p, or L_p^*/(R_p/p^2)). No source in the archive and no theorem known
to this run supplies it.

No Lean development was produced. No new formal step existed to check.
Formalizing the A1/A2 bookkeeping would duplicate `Coinvariant/KolyvaginOrder.lean`.
