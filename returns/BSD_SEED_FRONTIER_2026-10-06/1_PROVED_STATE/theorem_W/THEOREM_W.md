# RETURN — w_(p,ℓ) auxiliary independence (Fable 5.1, 2026-09-29)

## STATUS: PROVED
Grade: written deduction from retained imports, same session, not independently reviewed.
An independent audit (Codex, audit-only role) is the recommended next step before it is merged anywhere.

## Theorem W
Let E be the seed (minimal model, saturated basis P1, P2). Let p be a prime with
  p ∉ B* = {2, 3, 19, 59, 487, 2243, 4547, 5843}   (B* = B \ {5}; every p ∉ B qualifies).
Let ℓ ≠ ℓ′ be primes with ℓ ≡ ℓ′ ≡ 1 (mod p), ℓℓ′ ∤ pN, p ∤ #E(F_ℓ)·#E(F_ℓ′), and R_(p,ℓ), R_(p,ℓ′) ≠ 0 in F_p.
Define w_(p,ℓ) = C2(p,ℓ)/((a_ℓ − 2)·R_(p,ℓ)) with the production conventions: one ω₁ period; the smallest
primitive root g_ℓ used both in T_ℓ = σ_g − 1 and in ind_g; the same basis for every ℓ. Then
  **w_(p,ℓ) = + w_(p,ℓ′) in F_p.  The sign is +1.**  If Sha[p] ≠ 0, the common value is 0.

Why B*: 2, 3 divide 6N; 2243, 4547, 5843 are bad; 19, 59 | 2242 = #E^ns(F_2243); 487 | 5844 = #E^ns(F_5843)
(Hyp 2.2(iii) fails at these). 5 is admissible: 5 ∤ #E(F_5) = 8. Anomalous p cannot occur (Lemma A1).
Convention sensitivity: w is invariant under a joint change of generator, basis or period. A mismatched generator
multiplies w by a square s⁻²; the Artin reciprocity sign and σ ↔ σ⁻¹ drop out because the regulator is quadratic.

## Proof map
- Kill tests: K-A1 PASS, K-A2 PASS, K-A3 PASS (KILL_TEST_KA1.md, KILL_TEST_KA2_KA3.md).
- Branch Sha[p] ≠ 0: Ota v1 Thm 6.4 contrapositive gives C2 = 0 at every admissible ℓ. Its proof runs through
  Kato classes, a mod-p Selmer count (Cor. 4.19) and p-parity; no step assumes Sha finite.
- Branch Sha[p^∞] = 0 (WORKING_1, WORKING_2): work in the compositum F′ = F_ℓF_ℓ′, whose group is C_p × C_p.
  (1) The exact Hecke distribution relation π(θ_ℓℓ′) = (a_ℓ′ − σ − σ⁻¹)θ_ℓ, which is unconditional.
  (2) The tame pairing of F′ splits as H^(ℓ)x + H^(ℓ′)y. This uses no Hyp 2.2 clause.
  (3) BKS II (27) for F′ (the step that uses Hyp 2.2 and Sha[p^∞] = 0): θ_ℓℓ′ is one scalar μ times
      det(H^(ℓ)x + H^(ℓ′)y) in I′²/I′³.
  (4) Projecting to each factor gives w_(p,ℓ) = μ/((a_ℓ − 2)(a_ℓ′ − 2)), which is symmetric in ℓ, ℓ′.
- The unit problem flagged by the Codex audit (§3) is avoided rather than solved. One field carries both
  auxiliaries, so their separate units are never compared.

## Exact checks (CHECKS.md)
- Seed Hyp 2.2 data. No good p ≤ 10⁷ has a_p = 1.
- 389a1 at p = 7 on 5 composita C_7×C_7:
  - the exact distribution relation holds, and its wrong-sign control is rejected;
  - the full 3-coefficient proportionality holds, including the mixed term; the flipped-cross-term control is
    rejected 5/5;
  - w_ℓ = w_ℓ′ = +1 every time;
  - the generator-mismatch control gives s⁻² exactly.

## Scope (what is NOT claimed)
- Not the value of w (288 is not derived), not w ≠ 0 when Sha[p^∞] = 0, not v_p(#Sha).
- Mod p. Q_p-level (or mod p²) Σ-independence of m_p stays open (T-a §5).
- By-product (derived as in T-a §4, not separately checked): T-a's mod-p (1b) extends from p = 5 to every
  p ∉ B* with Sha[p^∞] finite, for admissible pairs with R ≠ 0.
- Endpoint effect: NONE (OVERVIEW K2). It turns admission item 3 from w_(p,ℓ) into a single w_p for p ∉ B*.
  It is not progress on G1 and not a difficulty reduction.
- No new c₂ certificate, no seed prime run, no build, no push, no message, no subagent.

**FIN, ORDER9 and Q36 are unchanged.**
