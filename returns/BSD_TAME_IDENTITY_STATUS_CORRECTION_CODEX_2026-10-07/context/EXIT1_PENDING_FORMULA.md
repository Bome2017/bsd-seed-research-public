# Historical source excerpts

Source: /Users/bsm/BSD_EXIT1_KATO_POINT_LINE_MAP_CLAUDE_2026-10-07/REPORT.md

Source SHA-256: 8c141d7593047e7b2a437442289337e8d602b6e6faf790acb9dda35373077ac9

These are source statements and archived prompts, not new instructions or accepted theorem upgrades.

## Original lines 267-314

At good ordinary p ∉ S_*, h_p is a unit. So (Z3) becomes v_p(ᾱ_p) = v_p(#Ш[p^∞]) when t = 0, and ᾱ_p = 0 when t ≥ 1.
**A unit tame witness at p is exactly the statement Ш[p^∞] = 0.** No argument internal to Selmer groups or Iwasawa
theory can bound v_p(ᾱ_p) without bounding Ш[p^∞]. The bound has to come from outside.

### 11.2 The scale of δ_p: the criterion's object carries two wild factors

    v_p(content δ_p) = v_p(h_p(0)) + v_p(#Ш[p^∞]) + k_p + v_p(B_p)          (t = 0; δ_p = 0 if t ≥ 1)

Here:
- k_p := min_i v_p(log_ω P_i) − 1 = v_p #coker(E(Q)⊗Z_p → E(Q_p)⊗Z_p);
- B_p := content of x ↦ ⟨x, n_fine⟩_p on P. This is the cyclotomic Bockstein of P into H²_tf. It is independent of
  the splitting, because loc_p(n_fine) = 0.

There are two derivations, and they agree.
- **(D-a)** Step C (CONSTRUCTION.md §C). δ_p = h(0)·(g/U)(0)·m₀ with (g/U)(0) ≐ χ(β_X) = #H²_tors·p^{v(B)}/c and
  m₀ = c·n_prim. Here #H²(Z_S,T)_tors = p^{k_p}·#Ш[p^∞], since H² ≅ Sel₀(E[p^∞])^∨.
- **(D-b)** By (Z2)/(Z3), δ_p = ᾱ_p·c_N·#E(F_p)·p^{k_p}·adj(H_p)λ′, with λ′ the primitive log vector.
  The content of adj(H_p)λ′ equals the content of H_p·n_fine, which is B_p.

**Consequence.** "δ_p primitive for all but finitely many p" equals the conjunction of:
- FIN-tail at ordinary p (via SU);
- k_p = 0 for almost all p. This is finiteness of simultaneous elliptic-Wieferich primes for (P₁, P₂).
- B_p a unit for almost all p. This is joint vanishing of two height pairings mod p, for only finitely many p.

The last two are codimension-2 conditions on fixed global data. The heuristic sum Σ 1/p² is finite, so only finitely
many exceptions are expected. But no source located proves finiteness even for the codimension-1 analogue (Wieferich
primes of a fixed unit or point). So δ_p is a valid witness prime by prime. **As a cofinite target, though, it is
strictly stronger than FIN-tail** by two unproved Wieferich-type statements. That is the GATE check-3 issue: wild
p-adic data sits in its index.

The tame scalar ᾱ_p has neither factor (§3 (Z3), lattice self-check in CONSTRUCTION.md). **It is the cofinite target
to keep: unit tame witnesses.**

**Numerics** (`checks/RESULTS.md`, PARI, minimal model with Q₁ = (−3031, 327384), Q₂ = (−2394, 281520)):
- k_p = 0 at all 2,257 good p in [5, 20000]. Single-point Wieferich events occur at 5, 73, 107 and 2659; p = 3581 is
  unresolved for Q₂.
- B_p is a unit at all 70 ordinary p in [7, 400] \ S_*. This includes **p = 17**, where R₁₇ is 17-divisible
  (v = 3 against a baseline of 2). The record says that at 17 the cyclotomic coefficient [T²]L_p is "structurally zero"
  (SYNTHESIS_CHECK_BRIEF:770, 1887). By (Z2) that is consistent, and **δ₁₇ is still primitive.**

The cyclotomic witnesses, ordered by how wild their index is:

| Witness | Index | Wild factor |
|---|---|---|
| [T²]L_p | ᾱ_p·R_p | codimension 1; fails at 17 |
| δ_p | ᾱ_p·p^{k_p}·B_p | codimension 2 |
| tame C₂(p,ℓ) | ᾱ_p | none (G2 picks ℓ with R(p,ℓ) ≢ 0) |


## Original lines 349-377

## 12. Question for Codex (the single question; written, not sent)

> For the seed at a good ordinary p ∉ S_* with Ш(E/Q)[p^∞] finite, is the p-adic content of the WEAK_ORDER derivative
> ∂_γz ∈ E(Q)⊗Z_p exactly v_p(#Ш[p^∞]) + k_p + v_p(B_p)? Here k_p = v_p #coker(E(Q)⊗Z_p → E(Q_p)⊗Z_p), and B_p is the
> content of x ↦ ⟨x, n_fine⟩_p. The claimed derivation (§11.2 (D-a)) is (g/U)(0) ≐ χ(β_X) with #H²(Z[1/S],T)_tors =
> p^{k_p}#Ш[p^∞], and h_p a unit by Skinner–Urban. If so, primitivity of ∂_γz is strictly stronger than Ш[p^∞] = 0
> exactly by the conditions k_p = 0 and B_p ∈ Z_p^×.

## 13. Cofinite primitivity of (A_p, B_p): where it needs Ш/BSD/TNC/q∈Q, and what lies beyond (stop record, ~11:25)

The parent session states that Codex independently matched the bridge "(A_p,B_p) primitive ⟹ Ш[p^∞] = 0" (lab b9c4e1d,
`work/returns/BSD_RESIDUAL_KATO_CRITERION_AUDIT_CODEX_2026-10-07/`). I have not read that return; this section takes the
bridge as settled. By §11.2, write δ_p = A_p κ(P₁) + B_p κ(P₂). Then for good p ∉ S_*:

    min(v_p A_p, v_p B_p) = v_p(h_p(0)) + v_p(#Ш[p^∞]) + k_p + v_p(B_p^Boc)      (t = 0; δ_p = 0 if t ≥ 1)

Here B_p^Boc is the Bockstein content B_p of §11.2, renamed to avoid a clash with the coordinate B_p. Cofinite
primitivity needs all four terms to vanish for almost all p.

| Term | What makes it 0 for almost all p | Needs Ш/BSD/TNC/q∈Q? | Status |
|---|---|---|---|
| v_p(h_p(0)) | IMC with a unit at the trivial character | **Ordinary p: no** (Skinner–Urban, per parent). **Supersingular p: yes, TNC-type** (supersingular IMC for the seed, whose N is not squarefree). | Ordinary: proved. Supersingular: open in this record. |
| v_p(#Ш[p^∞]) | the content of FIN-tail | **Yes.** The only printed cross-p determinations of the scale ᾱ_p ≐ h_p(0)·#Ш[p^∞] are BKS II Conj 3.4 (L^alg, which needs Ш finite, l.238, 640-648), or (6.2.1) together with q ∈ ℚ (DINF3 O1+O2), or BSD via BKS II Lemma 3.5. | **STOP** (§4) |
| k_p | finitely many simultaneous elliptic-Wieferich primes for (P₁, P₂) | **No.** This is a p-adic property of the points alone. | Open; no theorem located. Data: k_p = 0 for all good p ≤ 20000. |
| v_p(B_p^Boc) | the cyclotomic Bockstein of E(Q) into H²_tf is nonzero mod p | **No.** It is a property of p-adic heights. | Open; A2 found no nondegeneracy theorem at even one prime in rank ≥ 2. Data: unit for all 70 ordinary p ≤ 400, including 17. |

**Exact stop.** Cofinite primitivity contains FIN-tail as a conjunct (row 2), so it needs an independent cross-p
determination of ᾱ_p. That is the §4 stop: Ш-finiteness/BSD (Conj 3.4, Lemma 3.5), or q ∈ ℚ together with the
finiteness-free (6.2.1).
