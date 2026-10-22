# E08: gate T0, a non-invariant functional for the level-change witness (cloud theory session)

**Map part:** F3(c), parked; T0 is the reopening condition (E05 `AUDIT.md` §6.2). Lemma A was narrowed by the
independent review (finding F06). **HOW:** a theory attempt, chosen by the user on 2026-09-25. **Status:** prepared, not
launched.

## Background (all in `reference/`; read before deriving)

- **The level-change construction:** `reference/level_change_result/RESULT.md` and its `references/`. It defines
  R = ℤ/p^k, P_S, M_S, δ_S, Ξ_{S,W}, D_W^−, B_S, z_E, Θ_H, c₂, d_l and the Γ(l)/Borel model.
- **E05's audit:** `reference/e05/AUDIT.md`, especially §§1–3, §5 and §6, and its correction note
  `reference/e05/CORRECTIONS.md`.
  - **F13.** For every admissible (p, k, S), z_E B_S(Ξ) = z_E(C_{p,k,S}) = c₂(Θ_H). The named "open target" is the retained
    witness itself.
  - **Lemma B.** For ψ: M → R, set Λ_ψ(v) = Σ_{g∈P} ψ(gv)g⁻¹. Then ψ(Dv) = τ(DΛ_ψ(v)), and ψ(D₂⁻v) = c₂(Λ_ψ(v)).
  - **Lemma A, narrowed by the review.**
    - F·d_l = F ⟹ F(Ξ) = 0.
    - F·d_l = ρ(d_l)·F ⟹ F(Ξ) ∈ (ρ(d_l) − 1)M′. This vanishes only when the target action is trivial, or when a later
      map kills that augmentation part, as in lower-level detection. **It is not zero in general:** the identity on
      F₇[C₇] keeps D₂⁻ ≠ 0.
  - **E05 item 5's analysis of the continuations.**
    - T_r with r prime to NS gives a_r·Θ_H times a group element.
    - Diamond-intertwining correspondences composed with B_S give Mazur–Tate data at another starting class.
    - Correspondences **outside the normalizer of ⟨d_l⟩** remain open. These are the general SL₂(F_l) elements in the
      Γ(l) model; B_S already uses the unipotent ones.
    - The reciprocity map on these curves is the Kato mechanism, already imported through Ota.
  - **§6.3.** At ordinary p, depth-zero witness vanishing is equivalent to Sha[p^∞] = 0
    (`references/EXACT_WC_ANTECEDENT.md`:60).
    - A p-uniform success would therefore be FIN-strength, not an easier route.
    - A success at one fixed p gives h_p ≤ bound at that p only.

## The gate T0 (E05 §6.2)

Name a functional ψ′ on M_S that comes from a **stated** correspondence or reciprocity map and is **not** invariant
under d_l. Then prove:

- **(i)** c₂(Λ_ψ′(δ_S)) = u·c₂(Θ_H), with u ∈ R^× or with an explicitly controlled error term;
- **(ii)** a bound on divisibility. For R = ℤ/p^k, prove depth(c₂(Λ_ψ′(δ_S))) ≤ b for an explicit b < k, meaning the
  class is nonzero modulo p^(b+1). At least one fixed p is enough. This is an **upper** bound on the p-adic valuation.

**Non-circularity (required for (ii); corrected before launch, 2026-09-25).**
- Prove the bound without assuming any of the following:
  - the nonvanishing of the original witness c₂(Θ_H);
  - primary Sha vanishing, Sha[p^∞] = 0;
  - h_p = 0;
  - the retained WC antecedent.
- **Logical equivalence of the conclusions is permitted.** Proving an equivalent statement by a genuinely independent
  argument is a valid proof.
- What does not count is assuming the target, or renaming it without adding an argument.
- Identify the new geometric or reciprocity input, and explain how it proves the bound rather than restating it.

## Tasks

**A. Setup (`work/e08/SETUP.md`).**
- Restate the definitions you use, with source lines.
- State Lemma A in its narrowed form and Lemma B.
- Confirm or refute F13 from the references. If you refute it, stop and report.

**B. Candidates.** Attempt each class below. For each, either construct ψ′ and prove (i), or give the exact step where
it fails, with file and line where relevant. Other candidates you find are welcome; name them explicitly.
- **B1.** Correspondences outside the normalizer of ⟨d_l⟩ in the Γ(l)/Borel model: general SL₂(F_l) double cosets,
  excluding the unipotent ones B_S already uses.
- **B2.** Intertwining maps into targets with nontrivial diamond action, which the narrowing admits (corrected before
  launch, 2026-09-25).
  - **Why characters are the wrong target.** Over R = ℤ/p^k, a group of order p has no nontrivial character: χ(g)^p = 1
    forces (χ(g) − 1)^p = 0 in characteristic p, so χ(g) = 1.
  - **Nonsemisimple R[P_S]-modules.** Consider these instead, for example unipotent actions g ↦ 1 + J with J nilpotent,
    each followed by an evaluation that does not factor through the augmentation.
  - **Characteristic-zero character lifts.** These may also be investigated. Their integral specialization, and any
    division losses (for example the 1/p of Fourier inversion on an order-p group), must be explicit.
- **B3.** A reciprocity-map candidate with an integrality input beyond the Kato/Ota mechanism already imported. Do this
  only if you can name a specific map.

**C. Divisibility bound.** For every candidate satisfying (i), attempt (ii) under the non-circularity requirement.

**D. Toy test T1 (only if some ψ′ satisfies (i)).** Run it exactly as specified in E05 §6.2:
- the curve 389a1, with p = 7, l = 29, k = 1;
- the roughly 390 level-389 Manin symbols, in pure Python;
- compute c₂ via (G) and via your ψ′, and compare;
- also check c₀ = c₁ = 0 (mod 7);
- verify Ota's hypotheses for 389a1 at p = 7; do not assume them.

E05 cautioned that this might duplicate a completed "anchored toy". The custodian's records name one completed
anchored toy, and it is a different object: the paired-kernel packet at conductor 2904 (25 kernels), not a Mazur–Tate
witness at 389a1. If the references show a completed witness evaluation at 389a1, say so and do not repeat it.

**E. Verdict (pre-registered), stated first in `T0.md`.**
- **`T0_PASSED`**: some ψ′ has (i) proved and (ii) proved at ≥ 1 fixed p, and it meets the non-circularity requirement. Say what
  it gives (h_p ≤ bound at that p) and what it does not (no A, no uniformity).
- **`T0_PARTIAL`**: (i) is proved for some ψ′, but (ii) is open, heuristic, or shown only at the toy.
- **`T0_NO_CANDIDATE_AS_TESTED`**: every examined candidate fails at a named step. **No class-level exclusion may be
  stated.** "Fails as tested" only; see the review's correction of Lemma A for what goes wrong otherwise.
- **The p = 17 question.** Also answer: would any candidate give a per-prime witness cheaper than the depth-3 route at
  p = 17 for the seed? Yes, no, or unknown, with the reason.

## Rules (in addition to CLAUDE.md)

**Scope.**
- This is a theory session: attempt the mathematics directly. Compute only for T1 or for small exact checks of your own
  identities, within 2 CPU-hours total, 8 GiB RAM, 5 GiB disk, no paid resources, no subagents.
- No literature survey. Consult a primary source only for a specific identity or missing step, and cite its version
  and theorem number.

**How to state results.**
- Mark every statement as [D] derived here, [C] computed here, [M] recalled and not re-read, or [R] from the
  references.
- Do not state "impossible", "cannot" or "no X can" beyond the exact scope of a proof.
- No claim of FIN, ORDER9, Q36, UC or a new settled primary component.

**Where to write.**
- Write only in `work/e08/`. The resume file is `work/e08/RESUME.md`, not `work/RESUME.md`.
- Commit checkpoints after A, after each candidate class, and before T1.
- Copy any reference script into `work/e08/` before running it. Some write next to themselves, and `reference/` must
  stay unchanged.

## Deliverables (in `work/e08/`)

- `T0.md`: the verdict first, then each candidate with its status, the non-circularity arguments, the p = 17 answer, "What this
  changes in the map (F3(c))", and non-claims.
- `SETUP.md`.
- `checks/`: any exact checks, with a `replay.sh`.
- `RESUME.md`.
- `MANIFEST.sha256`.
