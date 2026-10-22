# B.7 — BSD constant C, the 2-isogenous curve E′ = E/⟨T⟩, and C′/C

Sources:
- `scripts/s07_bsd_const.sage` → `out/s07_bsd_const.out`. **Written and run by the second lane-B instance** (see RESUME §4b). I read it in
  full, and my own re-run `scripts/s07_bsd_const_rerun.sage` → `out/s07_bsd_const_rerun.out` (only the save path differs) gave
  **byte-identical output**.
- `scripts/s07a_Eprime.sage` → `out/s07a_Eprime.out` (mine: eclib saturation on E′, mwrank generators of E′).
- `scripts/s07c_scaling.sage` → `out/s07c_scaling.out` (mine: ψ*ω′ = ω). Its optional last block, which would locate ψ(E(R)), failed on an
  undefined symbol and is not used.

## 7.1 BSD constant of E

C := Ω_E · Reg(E) · ∏c_p / #E(Q)_tors² = Ω · Reg · 16/4 = 4·Ω·Reg.

**C = 3.99281263923936691806855200220915394735533662030720199…** (ball radius 1.0·10⁻⁶⁵). **Label: CERTIFIED_NUMERIC.** The inputs are:
- Ω and Reg: CERTIFIED_NUMERIC (B.6).
- ∏c_p = 16 and #tors = 2: PROVED (B.2, B.3).
- Reg(E) = Reg(P₁,P₂): the index is 1, PROVED (B.4).

Cross-check (non-rigorous): PARI `ellbsd(E)`·Reg = 3.99281263923936691806855200220915394735533662030720199382058749…, inside the ball.

**Conditional statement:** CONDITIONAL(BSD for E): L″(E,1)/2! = L^{(2)}(E,1)/2 = C · #Sha(E/Q) ≈ 3.992812639 · #Sha. With the proved parts
(Sha[2^∞] = 0, B.5; Sha[5^∞] = 0 via the derived v₂(c₀) ≤ 8 lemma, brief), #Sha would be odd and prime to 5 (and a square if finite).
No analytic value was computed here (lane A).

## 7.2 E′ = E/⟨T⟩: full invariants

| item | value | label |
|---|---|---|
| model | E′: y² = x³ + 10A x² + 9mA x = [0, 45470, 0, 91790289, 0]. ψ(x,y) = (y²/x², y(4AB − x²)/x²). Checked: ψ̂∘ψ = [2] on P₁ and P₂, and ψ is additive on P₁+P₂. Sage's Vélu codomain is isomorphic to it by (u,r,s,t) = (1, 22735, 0, 0). | PROVED (exact) |
| Δ′ | 2¹⁰·3⁴·2243²·4547³·5843 > 0, so 2 real components | PROVED |
| minimality | globally minimal: v_p(Δ′) < 12 for all p. Reduced minimal model [0, −1, 0, −597383344, 5572681004764] via (1, −15157, 0, 0), u = 1 | PROVED |
| Néron differential | ψ*ω′ = ω: Vélu scaling factor 1, and both isomorphisms have u = 1 (`out/s07c_scaling.out`) | PROVED |
| conductor | N′ = N (as required for isogenous curves) | PROVED |
| local data (PARI + Sage generic Tate agree) | 2: III* (c = 2); 3: I₄ non-split (c = 2); 2243: I₂ split (c = 2); 4547: III (c = 2); 5843: I₁ non-split (c = 1). **∏c′ = 16** | PROVED |
| torsion | E′(Q)_tors = Z/2 = ⟨T′⟩, T′ = (0,0). Evidence: `elltors`, Sage and Lutz–Nagell; the gcd of #E′(F_p) over good p ∈ [5, 80] is 2; the x² + 10Ax + 9mA discriminant is 64AB, not a square | PROVED |
| generators | **E′(Q) = ⟨T′⟩ × ⟨R′, ψ(P₁)⟩**, R′ = (−2243, −107664). Proof in 7.3. | PROVED |
| Ω′ | 0.05608980303887280889661880361586076834227009573327… = Ω (ratio 1 ± 10⁻³⁰⁰ or better) | CERTIFIED_NUMERIC |
| Reg′ | Reg(R′, ψP₁) = 17.796517472490340299174941219436038416304972463778… (radius 5.0·10⁻⁶⁵) = Reg(E). ĥ′(R′) = 4.264181004868839183701570353068131739336, ĥ′(ψP₁) = 8.622299966508759377520200415169659942687 = 2ĥ(P₁) (balls overlap), and ⟨R′, ψP₁⟩ = −4.355517221063135654581897450153025644820 | CERTIFIED_NUMERIC |
| C′ | Ω′·Reg′·16/4 = 3.9928126392393669180685520022091539473553366203072… (radius 1.1·10⁻⁶⁵) | CERTIFIED_NUMERIC |

## 7.3 Proof that E′(Q) = ⟨T′, R′, ψP₁⟩ (independent of saturation on E′)

1. **Kummer map.** For E′: y² = x³ + a′x² + b′x the map α′: E′(Q) → Q*/Q*², (X,Y) ↦ X, T′ ↦ b′, O ↦ 1, is a homomorphism with
   kernel ψ(E(Q)) (Silverman–Tate, *Rational Points on Elliptic Curves*, §III.5, applied to the pair C = E, C̄ = E′ with ā = −2a,
   b̄ = a² − 4b). The computed values are:
   - α′(T′) = 9mA ≡ mA = 10198921
   - α′(R′) = −2243
   - α′(T′+R′) = −4547
   - α′(ψP₁) = α′(ψP₂) = 1

   The images of T′ and R′ are distinct, nontrivial, and multiply to α′(T′+R′). So #E′(Q)/ψE(Q) ≥ 4.
2. **Upper bound.** E′(Q)/ψE(Q) injects into Sel^ψ(E/Q), which has order 4 (B.5: mwrank and Miller, independently). So
   E′(Q)/ψE(Q) = {0, T′, R′, T′+R′} exactly.
3. **Conclusion.** Since E(Q) = ⟨T, P₁, P₂⟩ (B.4, PROVED), E′(Q) = ⟨T′, R′, ψP₁, ψP₂⟩. The relation 2R′ = ψ(−2P₁ − P₂), found by exact
   search, gives ψP₂ = −2R′ − 2ψP₁. Hence E′(Q) = ⟨T′⟩ × ⟨R′, ψP₁⟩. **PROVED.**
4. **Independent cross-check.**
   - eclib: `saturation([R′, ψP₁])` gives index 1, and `saturation([ψP₁, ψP₂])` gives index 2 (`mwrank_MordellWeil.saturate`, index
     bound 2, 2-saturation proved with q ≤ 31).
   - mwrank `gens(proof=True)` on E′ returns (12914, −107664) and (20341, −1355400) on the minimal model (= R′, ψP₁ after the shift
     x_r = x + 15157), with `gens_certain` = True.
   - The regulators agree.

## 7.4 C′/C and Cassels' consistency check

- **Exact reduction.**
  - ĥ′∘ψ = 2ĥ (the canonical height is multiplied by deg ψ), so Reg(ψ(E(Q))) = 2²·Reg(E).
  - [E′(Q)/tors : ψE(Q)/tors] = 2 by 7.3: the coset T′ is torsion and R′ is not. So Reg′ = 4Reg/2² = Reg exactly.
  - ∏c′ = ∏c = 16 and #tors′ = #tors = 2.
  - Hence C′/C = Ω′/Ω exactly.
- **Ω′/Ω ∈ {1/2, 1} a priori.** ψ*ω′ = ω, and ψ: E(R) → E′(R) is a 2-to-1 covering onto an open subgroup (kernel {O, T} ⊂ E(R)). So
  Ω = ∫_{E(R)} ψ*|ω′| = 2·∫_{ψE(R)} |ω′| = 2Ω′/[E′(R) : ψE(R)], with [E′(R) : ψE(R)] ∈ {1, 2}.
- **Certified value.** Ω′/Ω = 1 ± 10⁻³⁰⁰ (ball). This excludes 1/2.
- **C′/C = 1 exactly: PROVED.** This uses standard facts that are not re-derived here (ĥ′∘ψ = deg ψ·ĥ; the covering argument) plus the
  certified ball, which is needed only to separate 1 from 1/2. The ball value alone is **CERTIFIED_NUMERIC** 1.0000…0 ± 5.3·10⁻⁶⁶.
- **Cassels.** If Sha(E) and Sha(E′) are finite, Cassels' isogeny-invariance gives #Sha(E)/#Sha(E′) = C′/C = 1. Independently and
  unconditionally, **Sha(E) ≅ Sha(E′)**:
  - For odd ℓ, ψ restricts to an isomorphism Sha(E)[ℓ^∞] → Sha(E′)[ℓ^∞], because ψ̂∘ψ = [2] and ψ∘ψ̂ = [2] are automorphisms of
    ℓ-primary groups.
  - Both 2-primary parts are 0 (B.5).
  - Label: PROVED. **The consistency check passes.** It is a check, not new information about #Sha.
