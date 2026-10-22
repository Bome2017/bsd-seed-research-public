## Addendum 32 (09-30 ~18:30): the uniform-depth v2 return (Pro, status REDUCED) CONFIRMED cross-family. A real new comparison: the converse of B.22
- **Inputs:**
  - ~/Downloads/BSD_UNIFORM_DEPTH_V2_RETURN_2026-09-30.zip; its 14-entry manifest was verified by Codex.
  - The controlling brief is the Codex-corrected uniform v2 (sha256 5786a977…, the live BUILD_MAP copy).
  - Codex's review: ~/BSD_UNIFORM_DEPTH_V2_REVIEW_CODEX_2026-09-30, manifest 27/27 OK, the zip identical;
    ACCEPT_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE.
- **Claude's check (Anthropic; the author Pro and the reviewer Codex are both OpenAI): CONFIRMED.**
  - D1: a minimal presentation over the local ring F_p[G] has its relation entries in J, so Fitt₀ ⊆ J^μ. BH Thm 1.4(b)
    and Fitting base change then give θ_L mod p ∈ J^{d_p}. μ ≥ d_p holds because restriction is injective (E(L)[p] = 0)
    and the coinvariants surject onto X_p.
  - D2: BH Prop 2.4 deletes a Kato conductor prime q with the factor a_q − u − u⁻¹ ≡ −(u−1)²/u ∈ J². So each
    coordinate-hyperplane restriction lies in J^{d_p+2}, and the degree-d_p initial form is δ_n·∏T_i.
  - D4, with d = 2: the one-prime projections lie in J⁴, which kills the T₁² and T₂² coefficients. So
    θ_L ≡ δ·T₁T₂ mod (p, J³).
    - For a quotient with s₁s₂ ≠ 0, T_i ↦ s_i·t + O(t²), so χ(θ) = δs₁s₂λ² + O(λ³).
    - p-multiples have v_λ ≥ p−1 ≥ 4, so the depth is exactly 2.
    - Every such quotient has conductor q₁q₂, and all faithful χ of one K are Galois-conjugate.
  - D3: min(h_p, p−1) = min(r_p, p−1) = min(d_p, p−1). With B.21, (i) ⟺ (ii) ⟺ (iii) ⟺ Ш[p^∞] = 0 at every good
    p ≥ 5.
- **What it is:** an exact comparison. B.22's converse is closed at the retained and imported grades.
- **What it is not:** a new vanishing prime, an infinite vanishing set, or an upper bound. The uniform wall is
  unchanged: d_p ≤ 3 outside one finite set.
- **Agreed with Codex:**
  - No construction session: the norm inequality 0 < |N(2048·χ(θ))| < p⁴ is sufficient but has no method, and
    assigning it would just hand over the missing theorem.
  - Prime computations stay frozen.
- **Differs from Codex:** the "expert-facing question" in NEXT_DECISION is not adopted. The user's standing rule is not
  to hand math questions to experts.
- **Banking:** the V026 bank is IN_PROGRESS (content 9ab7f58, stamp 8182b9c, worktree ~/BSD_SEED_V026_BANK_2026-09-30).
  The comparison goes in as a follow-on (V026-D), before any v0.2.6 push.
- **Roles from 09-30 (the user):** Fable only for tasks when needed. Claude pre-checks, and Codex does the independent
  check.
