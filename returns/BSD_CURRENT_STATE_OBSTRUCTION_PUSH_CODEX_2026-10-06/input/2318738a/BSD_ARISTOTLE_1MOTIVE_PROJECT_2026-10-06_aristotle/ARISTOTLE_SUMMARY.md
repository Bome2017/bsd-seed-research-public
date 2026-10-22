# Summary of changes for run ed200e47-d6b4-400d-a22e-9dae82e65d66
**STATUS: ETNC_CIRCULAR.** The full write-up, with every claim labelled, is in `ONE_MOTIVE_RESULT.md`. The Lean skeleton is `RequestProject/OneMotive/Skeleton.lean`. It builds with no `sorry`, and every new theorem uses only `[propext, Classical.choice, Quot.sound]` under `#print axioms`.

**Step 1 (PROVED, no FIN).**
- Sel(ℚ,M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n; for n = 2 there is an extra ℤ/2.
- PRE-CHECK (a)–(c) are correct as stated. The proof uses:
  - H¹(F,ℤ) = 0 and the fact that u has trivial kernel, so H⁰(F,M_E) = E(F)/⟨P₁,P₂⟩ ≅ ℤ/2 over ℚ;
  - the Kummer-sequence diagram chase;
  - Ш²(ℚ,ℤ²) = 0 by Chebotarev.
- The only arithmetic input is that P₁, P₂ generate E(ℚ) modulo torsion (IMPORTED from the record).
- ∞, p = 3 and the bad primes need no special care.
- One correction to keep in mind: the local condition at p is rationally the strict condition (dimension 0), not Bloch–Kato (dimension 2).
- Like the record's receiver B_p, this identifies Sel with Ш[p] but gives no bound. The difference is that M_E is fixed before p is chosen.

**Step 2 (PROVED, recorded only).** BSS and Sakamoto do not apply: M_E[p] is reducible, and T/(τ−1)T always surjects onto ℤ_p² (Lean: `coinvariants_not_free_rank_one`).

**Step 3 (Macias Castillo–Sano, checked against the arXiv source).**
- Their technical Hypothesis 2.11:
  - Parts (i) and (iv) hold at every odd p outside the bad primes (PROVED).
  - The receiver's own local condition fails 2.11(ii), because H⁰(ℚ_p, T_pM_E) has rank one.
  - The ordinary datum T⁻ = T_pẼ satisfies all of 2.11 at good ordinary non-anomalous p, with core rank 0 (PROVED).
  - At supersingular p no core-rank-0 datum passes (PROVED, using the IMPORTED irreducibility of V_pE locally at supersingular p).
- No Greenberg filtration gives the Bloch–Kato condition (PROVED). So their framework cannot produce the BK complex of PRE-CHECK (f).
- The core-vertex Hypothesis 2.17 is **not verified** (HEURISTIC, plausible):
  - Every Stark-system prime satisfies q ≢ 1 mod p (Lean: `not_cyclic_of_two_dim_torsion`).
  - The existing core-vertex criteria assume irreducibility, so none applies here.
- Cartier dual: its dual datum gives the dual line, so it does no better; its natural (Panchishkin) datum fails 2.11(iii).
- G2's 𝓜: its ordinary datum fails 2.11(ii).
- Because 2.11 does hold for T_pM_E at ordinary p, HYPOTHESES_FAIL is not the right status.

**Step 4 (determinant line).**
- det RΓ̃(T_pM_E) ≅ det RΓ̃(T_pE) ⊗ det RΓ̃(ℤ_p)^{⊗2}. The lattice quotient carries the condition that is relaxed at p.
- H⁰(M_E)/p = 0 gives H̃⁰ = 0, and the Kummer map sends ℤ_p² isomorphically onto E(ℚ)⊗ℤ_p.
- Acyclicity holds exactly when Ш[p^∞] is finite and the cyclotomic p-adic height determinant det H_p is nonzero. Then #H̃² = #Ш[p^∞]·p^{v_p(det H_p)}.
- This rests on identifying the connecting map with the p-adic height (Nekovář; IMPORTED, not re-derived).
- Corrections to PRE-CHECK (f):
  - H¹_f(ℚ, V_pM_E) ≅ V_pШ is correct for Bloch–Kato (PROVED), but that complex lies outside this framework.
  - In the framework's complex, H̃¹ also contains ker H_p.
  - The relevant special value is the p-adic leading term, not L*(E,1)/(Ω·Reg).

**Step 5.**
- The only canonical element the 1-motive supplies is the acyclicity trivialization. Its index is #Ш[p^∞] times the p-adic regulator index: tautological, and it exists only under p-local finiteness of Ш and nondegenerate heights.
- s_p ≐ x_{ℚ,Σ}·#Ш[p^∞] shares the #Ш factor but has a different cofactor (Kato coordinate versus wild regulator).

**Step 6.**
- A fixed index A_M would force FIN-tail and p-unit p-adic regulators for almost all p (Lean: `global_index_forces_finite`).
- The only way to define A_M without #Ш is the zeta / leading-term (ETNC) normalization, which brings in q. Removing the regulator instead gives back s_p, i.e. G1. This is the stop condition, hence ETNC_CIRCULAR.

The Properties table lists the five Lean results (marked proved) and the Kummer-data definition.

FIN, ORDER9 and Q36: unchanged.