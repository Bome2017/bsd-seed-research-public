# RESULT — Aristotle lane A, 2026-10-07 (corrected second pass)

**Primary status: NO_BOUND_MECHANISM_FOUND_FOR_TESTED_CANDIDATES.**

FIN, ORDER9 and Q36 are **unchanged**. This return obtained none of the following:
- a new cofinite bound on `dim_Fp X_p` (`X_p = Sel_p(E/Q)/W_p = Sha(E/Q)[p]`);
- an annihilating ideal;
- a vanishing prime;
- a cross-prime nonvanishing statement.

**Corrections in this pass** (details in CORRECTIONS_2026-10-07.md):
1. The first version's "Fitting-to-Heegner" equivalence (PROOF.md Prop. 1, statement 4) is
   **withdrawn**. It identified three different Euler-system constructions without proof: the
   DLV ideals, Howard's Λ-adic system and Zhang's classical κ_n. A1 is therefore **not** reduced
   to A2, and this return contains **no new derivation**.
2. The statement that the −23 twist "was never computed" is **withdrawn**. The record contains a
   2026-09-21 computer-assisted Arb certificate, 39.512236 ≤ L′(E^{−23},1) ≤ 40.182321, and a
   2026-10-06 floating-point value 39.84727806412. Their trace is in TWIST_D23_TRACE.md: the
   metadata, tail bound, endpoints and root number recheck exactly, but the core finite sum cannot
   be replayed from the supplied archive, because its source, work units and coefficient files are
   absent.

Context: as far as this run knows, finiteness of Sha (or even of Sha[p] for all but finitely many
p) has not been proved unconditionally for any elliptic curve over Q of analytic rank ≥ 2. That is
the open problem this lane is aimed at. The run did not find a mechanism that solves it for the
seed, and it does not claim that no mechanism exists.

## Candidates tested (details in CONSTRUCTION.md, collisions in COLLISION_CHECK.md)

| # | Candidate (source) | Control map to X_p | Information beyond retained identities | Status / first failed arrow |
|---|---|---|---|---|
| A1 | Anticyclotomic Λ-adic Selmer complex over K=Q(√-23), with higher Fitting / Euler-system ideals (the source TASK.md suggested) | Exact augmentation (T=0) base change with H² kept: 0→H^1_Λ/T→H^1_f(K,T)→H^2_Λ[T]→0 and H^2_f(K,T)=H^2_Λ/T (standard; PROOF.md R2) | The augmentation image of a specified DLV generator. **Not identified**: the comparison with any classical Heegner quantity is open (C1–C4) | **Open, not developed.** It is neither reduced to A2 nor shown to give control. The DLV text is not in the archive |
| A2 | Classical Kolyvagin structure theorem (Kolyvagin 1991; Zhang's Lemma 8.4 form) | ν_p = max(s⁺,s⁻)−1. Where s⁻ = 1: ν_p=1 ⇔ Sha(E/Q)[p]=0 (record bookkeeping; PROOF.md R1) | Nonvanishing mod p of one κ_ℓ | No theorem gives a uniform κ_ℓ ≢ 0 mod p. Collides with HEEGNER_NU.md (`nu_le_two_iff_sha_of_twist`), the W3 HEEGNER_NU_NOTE.md, and the continuation return's ι(ℓ) |
| A3 | Cyclotomic Kato divisibility + Perrin-Riou/Schneider leading term (good ordinary p) | dim Sha[p] <= v_p(L_p^*) − v_p(R_p/p^2) − v_p(local factors) | p-adic L-function leading term L_p^* and normalized p-adic regulator R_p/p^2 | Needs R_p/p^2 to be a unit and L_p^* to be bounded, both uniformly in p. The first is the forbidden "wild-regulator unit". The second has no formula independent of p-adic BSD. Also ordinary-only |

The A2 domain uses s⁻ = 1. This holds cofinitely if ord_{s=1} L(E^{−23},s) = 1, which the record
supports at the grade given in TWIST_D23_TRACE.md. The A2 verdict does not depend on that grade:
even on the full domain, the uniform κ_ℓ input is missing.

A2 and A3 fail at a common arrow: a **uniform-in-p nonvanishing mod p of a p-dependent
second-order arithmetic quantity** (κ_ℓ mod p, or L_p^*/(R_p/p^2)). The first version also put A1
under this arrow. That relied on the withdrawn identification, so A1 is no longer included in it.

No Lean development was produced. No new formal step existed to check. No L-value or other
numerical computation was run. The only scripts run are the exact read-only checks in `checks/`.
