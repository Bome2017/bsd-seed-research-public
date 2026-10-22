# v0.2.5 candidate edit set (Claude, 2026-09-29), DRAFT ONLY

Nothing here has been applied to any release repository, to the claim generator, or to Codex's
`V025_CLAIM_UPDATE_DRAFT.md`. The user decides what to apply. The sources are the RUN_NOW returns and both coordinators'
checks: `~/BSD_RUN_NOW_RETURNS_CHECK_CLAUDE_2026-09-29/REPORT.md` and
`~/BSD_RUN_NOW_CHECK_FABLE_2026-09-29/RETURN_CHECKS.md`.

## 1. S.3 (Sha[3^∞] ≅ (Z/3)²): qualification wording. The grade label is unchanged; the user decides

Replace "a recorded provenance limit, not an active cleanup target" with:

> The main-conjecture input is Skinner 2016 Thm A, as printed. For this curve at p = 3, its printed proof passes through
> Skinner–Urban Thm 3.6.1. That theorem uses SU Prop 12.3.6 at two places (SU l.6122 and l.12827).
>
> The printed proof of Prop 12.3.6 fails here. At the forced inert prime 2243, the removed Euler factor 1 − 2243⁻² has
> v₃ = 1, and Vatsal's Thm 1.1 controls only the primitive factor. (12.3.5.b) prints ℓ⁻¹ where SU's own (3.4.5.b) gives
> q_v⁻¹.
>
> One use (l.6122) is repaired for this curve by a nonvanishing argument (Lemma U2). The other is the unproved statement
> SU Prop 13.4.1(ii) for the seed data.
>
> The gap lies in the Selmer LOWER-bound direction. Finiteness and #Sha[3^∞] ≤ 9 need only Kato's direction, subject
> to the one-sided transfer (B1), which has not been written yet. Skinner's printed theorem is not refuted.
>
> Added 13:10 (B1, source-checked by Claude): the Kato direction at the congruent forms f_m has its own unargued
> step. SU Thm 3.5.6 restates Kato 17.4's integral divisibility in canonical-period normalization, while Kato proves
> it for a "good" ω. The needed comparison at weights ≥ 8 > p = 3 (MS-B1) is in none of the sources read.

Provenance: lane 1 (Fable), checked by Claude against the SU text (cross-model). It is not cross-family audited.

### 1b. Added ~15:00 (R23; Claude checked it at source): finiteness at 3 without SU

> Finiteness of Sha[3^∞] does not need the main conjecture. Kato 2004 Thm 18.4 is a rational statement and allows
> p | N; the Tate-curve case is the only exception. It gives corank Sel₃^∞(E/Q) ≤ ord_{s=1} L₃(E) ≤ 2, since a₂ ≠ 0
> and a₃ = −1 (nonsplit). With rank 2, Sha[3^∞] is finite. The exact order still rests on the S.3 inputs above.

Ready as of ~15:20. B2 is CERTIFIED and was checked cross-model by the Fable coordinator; Claude pre-checked it
(REPORT addendum 4):
> The lower bound #Sha[3^∞] ≥ 9 is also unconditional (explicit 3-coverings). Only the upper bound ≤ 9 then depends
> on Skinner Thm A as printed (MS-B1). Alternatives are Ochiai 2006 under MS-R3 (regularity of the Hida Hecke algebra
> through f), or GRH together with the Cassels–Tate pairing (B3).

Provenance: R23, written by Fable in the same session as B1, and checked cross-model by Claude (REPORT addendum 3). It
is not cross-family audited.

## 2. The singleton certificates at 17, 19, 23, 29: reviewer qualifier

> An independent same-family model audit (Fable 5.1, Anthropic; MODEL_SAME_FAMILY) found PASS_AT_RETAINED_GRADE for
> all four. It covered 1,140 exact interval identifications, frozen-checker replays, recomputed receipt roots and the
> prime-specific hypotheses. At 17 and 23 the ball radii are about 99% of the lattice half-spacing: exact at the
> retained tail-bound grade, with little slack. The large corpus files were not rehashed. This is not a cross-family
> audit.

Provenance: lane 2. Claude replayed items 1–4 identically.

## 3. The K ≡ 288 records (B.11 cross-reference; MT_PRESCREEN; overview S5)

Replace the fitted "K = #Sha·Tam/tors² × 2^k" with:

> K_E = 4·c∞·#Sha·Tam/tors², where c∞ = #π₀(E(R)).
> - It is derived from BKS Conj 2.3 in the production conventions (c_per = 1/c∞, the regulator factor 4, c_N cancels).
> - It is calibrated exactly on 6 rank-2 curves, all with Sha = 1: 68/68 rows with R ≠ 0, and 7/7 zero rows.
> - For the seed, 288 = 32·9. That is consistency evidence, at conjecture grade, for #Sha ≡ 9 (mod p) at the observed
>   primes.
> - The #Sha factor was tested on 194040co6 (sha_an = 4; lane 7): 17/17 rows match, and the Sha = 1 partners match
>   40/40. Caveat: every constant there is a power of 2. An odd Sha cannot be tested locally, because all 42 rank-2
>   curves with Sha ≠ 1 below 500k have Sha = 4.

Provenance: lane 4 (Opus). Replayed identically by both coordinators; the Fable coordinator confirmed it cross-model.

## 4. New theorem entries (candidates)

- **Theorem W** (fixed-p auxiliary independence): `V025_CANDIDATE_THEOREM_W_2026-09-29.md`. Codex
  CONFIRMED_WITH_CORRECTIONS.
- **Optional: Theorem W^(k) and the corrected G2^(k)** (lane 5).
  - Grade: a written deduction, same session, not audited. Replays were cross-model checked 7/7.
  - Claude found no hidden finiteness assumption in Lemma S when checked at source.
  - Its value is conditional on a cross-prime law (Codex B item 12).

## 5. Annotation for the master DO_NOT_RESURRECT row 16 (annotate only; do not rewrite the master)

> Codex, 09-29 (B_CORRECTIONS item 7), withdrew the unqualified "such an ideal exists iff FIN". A rational line and a
> p-independent lattice can exist without FIN. What is missing is the arithmetic realization and an independent nonzero
> control.

## 6. Watch list (from lane 6; the Fable coordinator corrected the wording)

- Castella–Liu–Wan 2608.29470. A non-squarefree version would bear on the supersingular Kato-coordinate caveat. It is
  per prime, so it does not bear on FIN's quantifier.
- The nine abstract-level rows in lane 6's H08 are unchecked triage, not exclusions.

FIN, ORDER9 and Q36 are unchanged by every item above.
