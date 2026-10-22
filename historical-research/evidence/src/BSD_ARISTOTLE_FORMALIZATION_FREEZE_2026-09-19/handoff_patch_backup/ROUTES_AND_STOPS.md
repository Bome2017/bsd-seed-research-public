# ROUTES_AND_STOPS — older lanes, only where they bear on FIN, FORMULA or a generalizable rank-2 mechanism

For each lane: what it established, its exact stop, and whether the stop is route-specific or structural. Records and hashes
are in `SOURCE_AND_HASH_INDEX.md`. Items marked (memory record) were carried from the project's session records and NOT
re-read in this hand-off session.

## 1. H9 (generalized Kato classes / diagonal cycles → Mordell–Weil rationality)
- **Calibration at the seed, p = 5 (Lane 1; operator-reviewed label `LANE1_H9 = CALIBRATION_COMPLETE; CURRENT_SEALED_BRANCH_MISSES_TARGET`).**
  The H9 target is explicit: Sel_str(Q,V₅E) = Q₅·(P₁ − tP₂), t = log₅P₁/log₅P₂, v₅(t) = 1, with a reproducible 5-adic
  fingerprint. Result NC5 (derived, refereed in-lane): the sealed Castella–Hsieh-branch tower output is η_K-eigen and, wherever
  defined, equals 0 — it never hits the strict line; no live descent to E(Q)⊗Q_p. — **ROUTE_BLOCKED** (route-specific stop, NOT an
  impossibility: "a future route must be genuinely different"). Sha[5^∞] = 0 is an INPUT there, never an output.
- Castella Thm A at the seed: κ₅(E) ≠ 0 spanning the strict line — CONDITIONAL on (a) an admissible (K,χ) (explicit K found:
  D = −79, −119; L(E^K,1) ≠ 0 not computed; ≈ 16 CPU-h estimate for another K) and (b) sufficiency of Castella's Assumption (A)
  at non-squarefree N⁺.
- H9R19 (memory record): the weighted reciprocity law at δ ≠ 1 is printed in BSV (Thm A); BCPV's ad-diagonal hits the pair
  (g_α,g_α) whose class CH prove is ZERO (Cor 4.8(2)), so the "big trace → L-value" arrow produces no L-value for the CH target.
- **Relevance now.** H9 classes are p-adic, per-p objects. By Castella–Hsieh / Castella, κ_p ≠ 0 ⟺ dim Sel(Q,V_pE) = 2 — per
  prime this is equivalent to finiteness of Sha[p^∞], and the direction that PROVES κ_p ≠ 0 assumes that finiteness. With
  rank = r_an = 2 and Sha[3^∞], Sha[5^∞] known, H9 supplies nothing toward FIN's tail or FORMULA unless a p-independent source
  for κ_p appears (that is `FIN_FRONTIER.md` §2). Whether the H9 stops still matter is Codex question 7.

## 2. Lane 2 (seed → fixed-prime family F_fix; p = 5) — refereed, ledger block proposed, NOT merged
- REG_CONGRUENCE: Reg₅(⟨P₁,P₂⟩) ≡ −(n+3)² mod 5³ on F_fix; ord₅ Reg₅ = 2 ⟺ n ≢ 22 mod 25. — PROVED (derived, two proofs, in-lane referees).
- INTEG (via Mazur–Tate 1991): p good ordinary, p ∤ #E(F_p)∏c_v ⇒ canonical p-adic heights in pZ_p; hence **ONE-BIT criterion:
  a₂ ≢ 0 mod p ⇒ Sha[p^∞] = 0 AND Reg_γ a unit**, no separate regulator/saturation gate. — PROVED (derived). Useful per-prime simplification.
- Converse a₂ ≢ 0 ⟸ Sha[5^∞] = 0 on n ≢ 22: CONDITIONAL on Skinner–Urban as read in the PREPRINT (published text not read).
- Verdict REGULATOR_TRANSPORTS; A2_BIT_ISOLATED: the modular-symbol bit is per curve; every non-seed member has N ≥ 8.9·10³³.
  **No global FIN content.** Stop is structural for this method ("control of a₂ on a congruence class = the target renamed").
- PARI trap found there: raw-model p-adic heights are wrong past 5²; the minimal model is canonical (Reg_γ ≡ 21 mod 25).

## 3. C1 / Zywina-family gates at p = 5 (2026-09-17; memory record) — all stops are for uniform-in-family statements
- Class-group gate: dim Sel₅ ≤ 3 + c_χ; c_χ = 0 ⇒ Sha[5^∞] = 0; degree-24 fields with log₁₀|disc| ≥ 213 — COST_BLOCKED; generic
  radical saturation gives only the two rational-point classes; Stark/Rubin–Stark evaluation unavailable.
- "Extend ω = δ(P₁)∧δ(P₂) to a residual Stark system" ⟺ Sha[5] = 0: a tautology — KILLED as a route (permanently closed).
- Proposition K: a two-prime Kurihara witness ⟺ κ₅ ≠ 0 ⟺ Sha[5^∞] finite: exact bookkeeping, not leverage.
- Fixed-E[5] family (Gate G): genus-0 degree-2 case closed negative; genus 1 open, parked.
- Transferable: ALL_ODD_RESIDUAL_IMAGE theorem (used by the seed); the "−I" vanishing-channel lemma (every subgroup of
  GL₂(F₅) of index < 24 contains −I; Lean-checked).

## 4. H41 / 62a1 / 66b1 (rank-0 twist-family programme; FROZEN) (memory record)
- Strong-BSD assembly DONE for the certified rank-0 bases 62a1 and 66b1 (Run013; BH Thm 2.13 hypotheses discharged); κ-parity, vertex exclusion, mod-4 mechanism sealed (ADDENDUM_017/018).
- **Transferable to the rank-2 seed: nothing mathematical.** Every chain there uses L(E,1) ≠ 0 (Kato / 2-descent / BH 2.13). What
  transfers is method only: the assembly pattern "per-prime closure + formula", hash-bound certificates, referee discipline.
- Do not reopen. The whole-map audit's instance-level caveat (CH §6 + BD05 Cor 3) is recorded in `FIN_FRONTIER.md` §3.

## 5. The LINE lane and its hostile audit (2026-09-18/19)
Design: `BSD_SEED_2243_12_RANK2_GLOBAL_OBJECT_2026-09-18/`; audit: `BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/`
(verdict `LINE_THEOREM_C_PASS_WITH_CORRECTIONS`). Use the AUDIT, not the design, wherever they differ. Full corrected status:
`FIN_FRONTIER.md` §1. Reusable lemmas produced (audit-derived; same-family; MT 1987 unread):
- global formula for the tame Mazur–Tate pairing: ⟨a,b⟩_ℓ = d(a+R−b)d(R)/(d(a+R)d(R−b)) mod ℓ (d = √denominator of x);
- at a Kolyvagin prime ⟨a, n_ℓa′⟩_ℓ = τ_{n_ℓ}(ā′,ā)⁻¹ (Tate–Lichtenbaum), hence ρ_n ≡ unit·det(π_{ℓi}P_j)²;
- tame height h_ℓ(Q) = [t(Q)/d(Q)] mod ℓ (validated against the global formula);
- lattice lemma: a p-independent determinant ideal exists iff FIN.

## 6. Lean / Aristotle formalizations (Lane 4; Lean v4.30.0-rc2, Mathlib 5450b53e; standard axioms only; 35 theorems)
| file | reusable content |
|---|---|
| `StepB_Intersection.lean` | `intersection_bound` (general n), `k_le_eight`: the intersection-matrix inequality behind v₂(c₀) ≤ 8 |
| `StepA_Lattice.lean` | `congruenceModuleEquiv`, `exponent_transfer`, `rank_one_index`, `stepA_master(_dvr)`: congruence-module algebra (κ cancels) |
| `Regulator_Saturation.lean` | `gram_change_of_basis`, `det_gram_change`, valuation invariance, `not_dvd_det_of_images`, `seed_index_prime_to_five`: Reg(H) = I²·Reg and mod-p saturation from a reduction matrix |
| `GL2F5.lean` | `sl_le_of_transvection`, `image_eq_top`, `neg_one_mem_of_index_lt` (index < 24 ⇒ contains −I) |
NOT formalized: modular-curve geometry (hypotheses of `k_le_eight`), the descent step between the two files, all analytic input.
Candidates for formal attack are listed in `CODEX_QUESTIONS.md` Q9.

## 7. Certificate / ReplayGuard / rigorous-core infrastructure — custody only, not mathematics
- `BSD_RIGOROUS_STREAM_CORE_2026-09-19`: untrusted producer + 145-line integer verifier for a_q, Arb engine for modular symbols
  and L″, segment Merkle roots, fresh-directory replays, negative tests. It is the trust base of the analytic rank, p = 3 and
  (sealed) p = 5 computations.
- Master certificate `SEED_2243_12_MASTER_CERTIFICATE_2026-09-18` (N0–N11, sha256 bindings, verify script).
- These prove custody and reproducibility. They do not strengthen any theorem cited "as printed".
