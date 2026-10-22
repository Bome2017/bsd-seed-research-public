# 02 — The audit record

## §1. How the result was produced

Five independent lanes (2026-09-15), each with its own charter, sources and verdict file:

| lane | target | outcome |
|---|---|---|
| 1 | BCPV `W_{N_gp^r}` vs Hida `w_r` | CLOSED at STOP_A; the `α`-dictionary; **not needed** on BCPV's point model |
| 2 | the point/Kummer transition square | square formal; four mandatory typing corrections; first gap = `MPC_r(ν)` |
| 3 | is there a printed theorem closing C? | **NO**; `KLZ17 thm:ordinaryfiltration` is Λ-adic only; gap = `E′` + `D4` |
| 4 | adversarial review | route not killed; the frozen square mistyped; first gap = `(★_r)` |
| 5 | fresh prover for the finite identity | **MPC proved, `d_r = 1`**, norm element, Lemma W, tame transport, scalar D4 |

Lanes 2 and 4 reached the type corrections independently. Lane 5 wrote its proof before reading Lanes 1–4,
and then only their `00/04/05` files.

## §2. First assembly referee

Charter: operator's, five items (point object; Hom-valued D4; typed tower relation; no rank factor; tame
twist preserved), with MPC and scalar D4 as inputs and BCPV (4.9) prohibited. Verdict: **`H9R16C_CLOSED`**,
all five items PROVED.

Its own numerics (new): the tame transport `L5-T5`, never previously exercised — Lane 5's checker has no
tame case — in 3 cases × 2 primes, 91 checks, 0 failures, including the mixed-level composite
`A_r pr^t_{1,*}W_{Np^r} = (U_p)^r pr^t_{2,*}`.

Coordinator audit (`evidence/…FINAL_ASSEMBLY_REFEREE…/11_COORDINATOR_AUDIT.md`): custody of all 46 lane
files re-verified; four load-bearing citations checked verbatim in the local TeX; `(★)`, the `(U'_p)^{⊗3}`
bookkeeping and the `μ_r` computation re-derived by hand and agreeing.

## §3. Second assembly referee — behind an independence wall

Given **only the statements**, never the first referee's reasoning. Eleven files were named off-limits by
path (its `03`–`11` and its two tame-check artifacts). The wall held: no walled file appears in its ledger,
and it disclosed, unprompted, the one `ls -la` it ran (names and sizes, no content).

Verdict line **`SECOND_REFEREE = DEFECT_FOUND`**, resolving as:

    C1 = DEFECT (rank clause; scope nil) + CONFIRMED_WITH_NARROWER_HYPOTHESIS (three narrowings)
    C2 = DEFECT (orientation clause FALSE — A_r is self-adjoint; scope nil, safe direction)
    C3, C4, C6, C7, C8 = CONFIRMED
    C5 = CONFIRMED_WITH_NARROWER_HYPOTHESIS

**Both defects are in clauses that carry no weight, and one of them simplifies the theory.** The three points
it was sent at hardest — the carrier collapse; Hom-valued D4 with the contravariant `π_r^*`; the tame twist
with the normalizations — are each PROVED, and the tower constant is exactly 1, derived from scratch.

Its own numerics (new, designed blind): 124 exact checks, 2 primes, 0 failures — the `A_r`-transport on every
generator, `ρ_r(t_2)A_rt_3 = A_rt_2t_3` on random products, `U_pA_r = A_rU'_p`, `WT_ℓW = ⟨ℓ⟩^{-1}T_ℓ`,
`A_r^t = A_r`, and a tame block for **both** push-downs. It also recorded a failed first attempt at its own
`T'_ℓ` coset construction rather than discarding it.

Coordinator audit: `evidence/…SECOND_ASSEMBLY_REFEREE…/12_COORDINATOR_AUDIT.md`.

## §4. `H_π`

Identified independently by **both** referees as the single unproved load-bearing input, consumed three
times, with `C8` needing it surjective. Proved in its own lane (`evidence/…H_PI_PINNING…`), integrally, with
surjectivity, for all odd `p`, without ordinarity, without Ohta 2000 and without KLZ17's `p ≥ 5`.

Its numerics: 61 of the recorded failures are **exactly the three predicted-negative controls** (`ϖ_1^*` vs
`U'_p`; `ϖ_2^*` and `ϖ_{1,*}` vs the unprimed `U^t`) — their firing is what makes the test non-vacuous,
since if they passed, Hida's printed unprimed tower would already have been `H_π`. The `(WD-ord)`
containment check that the argument rests on passes everywhere, on 46–83 independent relations. The only
other failures are a rank-precision flag the verdict explicitly does not rest on.

Coordinator audit: `evidence/…H_PI_PINNING…/07_COORDINATOR_AUDIT.md`.

## §5. Independence properties of the record, stated exactly

* Lanes 2 and 4 reached the type corrections without reading each other.
* Lane 5 proved MPC without reading Lanes 1–4's derivations.
* The second referee derived every claim without access to the first referee's reasoning.
* The tame transport `L5-T5` has **three** independent numerical implementations (first referee, second
  referee, `H_π` lane), written without sight of one another, all passing.
* Custody was re-verified at each stage against `LANE_FILES_AT_LAUNCH.sha256`: all 46 lane deliverables
  byte-identical throughout.
