# What V026-D banks: the depth–length–Selmer comparison (Claude, 2026-09-30)

This is a follow-on to the V026 bank, on the same branch and before any v0.2.6 push. It records one new, checked comparison.
Nothing else changes.

**Rules for every item.**
- Bind each governing file by path and sha256.
- The claim text never exceeds its grade.
- Release grades are the names in `claims/spec/common.py` only: PROVED_WRITTEN, IMPORTED_PREPRINT, …; "DERIVED" is prose,
  not a grade.
- Implications that need a witness are kind CONDITIONAL.

## Review label (verbatim in the claims verification record of each new claim)

"Derived by ChatGPT Pro (OpenAI). Independent check by Codex (OpenAI): ACCEPT_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE.
Cross-family check of D1–D5 by Claude Opus 5.5 (Anthropic). No literature-novelty claim. Not a human review; not
formalized."

In the paper and README, use the grades and source citations plus a one-line provenance clause, as for S.3K and B.20–B.22.

## IN

### 1. NEW claim (suggested id B.23; the maintainer follows the spec's id rules), kind THEOREM
- **Grades:** PROVED_WRITTEN and IMPORTED_PREPRINT.
- **Statement.** For every good prime p ≥ 5, let:
  - d_p := dim_{F_p} Sel_p(E/Q);
  - r_p := the minimum number of distinct Kato primes supporting a mod-p unit Kurihara quantity (B.21);
  - h_p := the minimum λ-valuation (λ = ζ_p − 1) of χ(θ_K), where θ_K is the full Bullach–Honnor-normalized Mazur–Tate
    element of a real cyclic degree-p field K at its actual conductor prime to pN, and χ is a faithful character.
    h_p = +∞ is allowed.

  Then

      min(h_p, p−1) = min(r_p, p−1) = min(d_p, p−1).

  Consequently, for this rank-two E and every good p ≥ 5:

      h_p < 4  ⟺  h_p = 2  ⟺  r_p = 2  ⟺  d_p ≤ 3  ⟺  Ш(E/Q)[p^∞] = 0.

- **Mandatory scope sentences.**
  - "This is an equivalence between existence statements. It does not say that a preselected field, or every field,
    attains depth two."
  - "It supplies no witness, no new vanishing prime and no upper bound."
  - "The strict inequality < 4 and the cap p − 1 are part of the statement."
- **Proof inputs.**
  - BH (arXiv 2511.07203v1): Hyp 1.2, Thm 1.4(b), Def 2.2 (the full element and period), and Prop 2.4 (the conductor
    norm relation a_q − u − u⁻¹).
  - B.20 and B.21.
  - Residual surjectivity, which gives E(L)[p] = 0.
  - The steps: Fitting base change; minimal presentations over the local ring F_p[G], giving Fitt₀ ⊆ J^μ; the
    capped-valuation argument, where p-multiples have v_λ ≥ p − 1.
  - Record the return's derivations D1–D3 and D5 (see inputs/return/STATE.json).

### 2. NEW claim (suggested id B.24), kind CONDITIONAL: the explicit two-prime bridge
- **Grades:** PROVED_WRITTEN and IMPORTED_PREPRINT.
- **Statement.** Let q₁ ≠ q₂ be Kato primes for p, and suppose δ_{q₁q₂} is a mod-p unit. Let L be the C_p² compositum
  of the degree-p subfields of Q(μ_{q₁}) and Q(μ_{q₂}). In the total-real-period normalization,

      θ_L ≡ δ_{q₁q₂}·T₁T₂ (mod p, J³).

  Take any cyclic degree-p quotient of L that is nontrivial on both inertia groups (the diagonal quotient is one). It
  has actual conductor q₁q₂, and each of its faithful characters has exact depth 2.
- **The antecedent is a sufficient witness, not an established fact.** This is derivation D4 of the return.
- **Normalization (mandatory).** δ uses Castella–Sano's symbol Re(2πi∫f)/Ω_E^+, where Ω_E^+ = 2ω₁. That is one half
  of the production symbol for this seed.

### 3. Text updates (paper §11, README status, the uniform-step open item)
- **B.22 keeps its text and provenance.** Add a cross-reference: "The converse holds by B.23 (derived 2026-09-30)."
  Do not state that B.22 itself proves the converse.
- **Replace the v0.2.6 open-target text with:**

  "Current known frontier for the uniform part of FIN on good primes: one finite set S ⊇ {2, 3, 2243, 4547, 5843}
  with dim_{F_p} Sel_p(E/Q) ≤ 3 for every p ∉ S, or any independently proved equivalent criterion. By B.21–B.23 this
  is equivalent, prime by prime, to a two-prime mod-p unit Kurihara witness. It is also equivalent to a faithful
  character value, of depth strictly below four, of the full BH element of a real cyclic degree-p field at its actual
  conductor prime to pN. Fields, conductors and estimates may depend on p."
- **Wording rules:**
  - Say "current known frontier". Never "only/all that remains".
  - Do not say "no method exists"; say "no applicable theorem was located in the screened sources".

### 4. Correction from Claude's pre-check of V026 (addendum 33): "no such value computed" is false
- **What is wrong.** B.22's qualification says "…and no such value has been computed at any prime", and the README's
  Conditional row says "no value computed". Both contradict the release's own S.17–47.
- **Why.** At each p = 17, …, 47, S.17–47 certifies the following at a singleton conductor ℓ with ℓ ∤ pN and
  v_p(ℓ−1) = 1: C₀ = C₁ = 0 and C₂ ≢ 0 (mod p), where C_k = Σ binom(ind(a), k)·[a/ℓ]⁺. That makes
  χ(θ_K) = C₂λ² + O(λ³) for the real degree-p subfield K of Q(μ_ℓ), a character value of depth exactly 2. The
  normalization differences change only p-adic units: the period factor is 2, and θ ↦ θ^# changes C₁ by a sign and C₂
  by C₁.
- **Fix, minimal.**
  - Replace the clause with "It has not been evaluated at any p ≥ 53." Do the same in the paper's B.22 passage if it
    has the clause.
  - Change the README row to "not evaluated at p ≥ 53; converse: B.23".
  - Record the reason in RECHECK_V0_2_6.md. Do not add a new claim identifying S.17–47 with B.22.

## Governing files (inputs/, byte-identical copies)
- `return/`: the 14 files of the uniform-depth v2 return. Its archive
  `~/Downloads/BSD_UNIFORM_DEPTH_V2_RETURN_2026-09-30.zip` has sha256
  ebb3d4c134c26149b4b18e0c6cc1c7a43c835cbeb4e54c0d6ab73353bd104caa, and the internal manifest is 14/14.
- `CODEX_UNIFORM_DEPTH_V2_REVIEW_REPORT.md`, `CODEX_RECORD_ADDENDUM.md` and `CODEX_SOURCE_BINDINGS.json`: Codex's
  review, from `~/BSD_UNIFORM_DEPTH_V2_REVIEW_CODEX_2026-09-30/`, manifest 27/27.
- `CLAUDE_ADDENDUM_32.md`: Claude's cross-family check.
- `CODEX_NEXT_DECISION.md` is context only. Do not bank its "expert-facing question"; the user's rule is not to hand
  math questions to experts.

## OUT
- Any claim of a uniform bound, finite support, FIN, ORDER9 or Q36.
- Any witness existence, new vanishing prime or infinite vanishing set.
- The norm inequality 0 < |N(2048·χ(θ_K))| < p⁴ as a claim or target. It is a valid sufficient condition, but no
  method for it exists; leave it out of the release.
- Changes to B.20–B.22's statements, grades or provenance, other than the one cross-reference.
- Q36 material (the return re-derived X.5; there is nothing to bank). U22.
