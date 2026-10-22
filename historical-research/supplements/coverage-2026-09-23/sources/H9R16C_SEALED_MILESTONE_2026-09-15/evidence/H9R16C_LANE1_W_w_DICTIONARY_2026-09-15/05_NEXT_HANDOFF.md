# 05 — Next handoff (from Lane 1)

## What downstream work may import (all with the types in 01)

1. **Model identification.** Use the ζ-free Q-isomorphism α_r: X_1(Np^r)^pt ≅ X_r^μ,
   (A,P) ↦ (A/⟨P⟩, φ = inverse of Q ↦ e_M(P,Q)) (03 L1). It is the only identification here that respects
   the Galois action, so it is the only one usable inside a Kummer square over Q or K_0.
2. **W/w.** W^BCPV_{Np^r} = ⟨c_r⟩^{-1}∘α_r^{-1}∘w_r∘α_r, where ζ^H = (ζ^B)^{c_r} (03 C1-a). δ_r = ⟨c_r⟩^{-1} is
   Q-rational, central, of finite order and not commuting with W (03 C1-b).
3. **Transition.** α_r^{-1}∘π^{r+1}_r∘α_{r+1} = ⟨u_r⟩^{-1}∘ϖ_{1,*}, with u_r ≡ p (N) and ≡ 1 (p^r) (03 C1-c).
   The towers are isomorphic via β_s = α_s∘⟨v_s⟩, v_s ≡ p^s (N), ≡ 1 (p^s) (03 C1-c').
4. **Hecke.** Under α: U'_p ↔ U(p), e'_ord ↔ e, U_p ↔ U^*(p), e_ord ↔ e^*, U'_q ↔ U(q),
   T'_ℓ ↔ T(ℓ) (03 C1-d). Diamonds: α^{-1}g_dα = ⟨d⟩^{-1} (Albanese), α^{-1}⟨d⟩_Hα = ⟨d⟩_pt (Hida Picard, 03 C1-e).
5. **A_r in Hida form.** A_r = α_r^{-1}∘w_r∘g_{c_r^{-1}}∘U(p)^r∘α_r at level N_g p^r, k = 0 (03 C1-f).
6. **Insertion rule (03 §4).** On BCPV's own curve, the modular part of τ_r^MW is ϖ_{1,*} and nothing is
   inserted. Only when Hida's w_r or π^s_r is written explicitly do ⟨c_r⟩ (g^c factor) and ⟨u_r⟩ (f factor)
   appear. Both are harmless for MRS functoriality, Kummer naturality, injectivity and dagger descent.

## What downstream work must NOT do

* Do not identify BCPV's (e'_ord, U'_p, lim_{ϖ_{1,*}}) with Hida's untwisted co-ordinary system
  (e^*, U^*(p), lim_{π_*}) inside a Kummer square. That is the Hecke-preserving ι_ζ-dictionary. It twists
  Galois by the diamond character 1 + k + ε_N (KLZ2 §7.2) and is a TYPE_MISMATCH over Q or K_0 (03 K1).
  The Galois-rational match is with Hida's **w-twisted ordinary** system.
* Do not use Albanese μ-model diamonds as the G_r-action in a ⊗_{Z[G_r]} dagger receptacle without
  composing with g ↦ g^{-1}. Doing so flips ⟨χ⟩^{-1/2} to ⟨χ⟩^{+1/2} (03 D4).
* Do not replace the full-level W_{Np^r} by the p-part W_{p^r}. That introduces ⟨p⟩_N-powers (03 K5).
* Do not drop ⟨u_r⟩ when Hida's ζ_Nζ_{p^r} convention is used. It is wrong by ε_f(p)^{±1} per level (03 K6).
* Do not use A_r (which contains W, not K_0-rational) as a vertical map of the square. It belongs only
  inside the packaged point (03 D5).

## Open items, smallest first

1. **R3 (decision, not a theorem).** State whether the H9R8 receptacle is I_r^† ⊗_Z J_r or
   I_r^† ⊗_{Z[G_r]} J_r (G_r acting through diamonds). This fixes whether 03 D4 is live.
2. **R2 (small exact test, same tooling as `_verify/`).** Extend the lattice checker to a tame pair N_g | N and
   compute the exact identity relating (ϖ^t_1)_*∘W_{Np^r} and W_{N_gp^r} under the two tame degeneracy maps,
   including the diamond. Also settle BCPV's λ_{Np^r}(g_λ) versus λ_{N_gp^r}(g). Needed only if the finite
   point is rewritten at a single level. If it is defined literally (tame pushforward first, then A_r and
   Π_Z at level N_g p^r), its étale realization matches BCPV by functoriality with no extra identity.
3. **R1 (the C2 square).** Exact statement in 04. Lane 1 has removed every Atkin–Lehner ambiguity from its
   verticals.

## Custody and independence notes

* Primary texts were read from arXiv TeX sources (BCPV, DR22, KLZ2) and open PDFs (Hida ×2, BSV, MW86);
  fetched-byte hashes and URLs are in 06. Binaries were not retained; extracted text lived in the session
  scratchpad. Ohta 1999 was not accessible; nothing here depends on it.
* The authoritative H9R16 text was read from the Google Drive checkpoint (modified 2026-09-15T17:43Z),
  not from the truncated local copies.
* The other lane directories (LANE2–LANE4) were not opened, to keep this lane independent.
* Aristotle: not ready. The statements need modular-curve moduli and MRS twists, which are not available as
  formal libraries. The finite checks in `_verify/` are exact computations, not proofs of rationality.
