# Aristotle fixed-1-motive run: canonical return (2026-10-06)

**Two runs, one verdict.**
- **Run 2318738a** used package revision 1 and returned `ETNC_CIRCULAR`.
- **Run a6077c4a** used revision 2 and returned **`NO_CANONICAL_GENERATOR`**, stopping at step 5. It independently replicates run 1.
- Claude's regrade of run 1 under revision 2 (`NO_CANONICAL_GENERATOR` at good ordinary primes, `HYPOTHESES_FAIL` at supersingular primes) matches run 2.
- Aristotle's `ETNC_CIRCULAR` stands as the globalization finding.
- The lane closes as a scoped negative. It is not an impossibility claim.

**What is new and proved: Theorem 1.** For the fixed Deligne 1-motive M_E = [ℤ² → E], u(e_i) = P_i:
- Sel(ℚ,M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n.
- For n = 2 it is an extension of Ш[2] by ℤ/2.
- The only inputs are the saturation of ⟨P₁, P₂⟩ (record) and Chebotarev (Ш²(ℚ,ℤ²) = 0).
- Unlike the class-group receiver, M_E is fixed before p is chosen, and no retained receiver hypotheses are needed.
- It is an identification, not a bound.

**Why the lane closes.**
- **The receiver's own local condition** is rationally strict at p and fails Macias Castillo–Sano Hypothesis 2.11(ii) at every odd p.
- **The ordinary datum** passes 2.11 at good ordinary non-anomalous p (core rank 0). Hypothesis 2.17 is open. At the infinitely many supersingular p, no core-rank-0 datum passes.
- **The determinant line.** #H̃²(T_pM_E) = #Ш[p^∞]·p^{v_p(det H_p)}. The only element intrinsic to M_E is the acyclicity trivialization: tautological, carrying the wild p-adic regulator, and existing only under Ш[p^∞] finite and nondegenerate heights.
- **Globalization.** A fixed index would force p-unit p-adic regulators almost everywhere; the seed already fails this at p = 17 (W3 return). The only #Ш-free normalization is ETNC (q). Dividing out the tame regulator instead gives s_p, i.e. G1.

**Files.**
- `run_2318738a_rev1/`: `ONE_MOTIVE_RESULT.md`, `ARISTOTLE_SUMMARY.md`, and `RequestProject/OneMotive/Skeleton.lean` (24 declarations on the standard axioms).
- `run_a6077c4a_rev2/`: `RequestProject/OneMotive/RESULT.md`, `RequestProject/OneMotive/Skeleton.lean` (5 theorems on the standard axioms) and `ARISTOTLE_SUMMARY.md`.
- `CLAUDE_CHECK.md`: the independent check and the regrade.

Aristotle's README banner is excluded. The original archives are `../archives/2318738a-17a5-4380-8152-96849f45a3ea-aristotle.tar.gz` and `../archives/a6077c4a-8876-4c56-afef-5687d98141a1-aristotle.tar.gz`.

FIN, ORDER9 and Q36 are unchanged.
