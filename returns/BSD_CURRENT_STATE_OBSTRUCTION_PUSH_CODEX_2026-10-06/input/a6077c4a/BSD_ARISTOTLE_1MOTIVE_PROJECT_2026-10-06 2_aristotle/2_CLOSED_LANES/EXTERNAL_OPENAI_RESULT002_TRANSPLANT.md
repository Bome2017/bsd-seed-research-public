# OpenAI math Result 002 ("Exact BSD formula from low Selmer corank"): rank-two transplant, first pass (Claude, Opus 5.5, 2026-10-06)

- **Source:** github.com/openai/math, path `preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/build/sections/`, files 01–10, read as raw LaTeX on 2026-10-06.
- **License:** Apache-2.0.
- **Verification level:** the repository states that its collection mixes verification levels and that some unformalized results may have issues. This paper's verification level was not checked here.
- **Scope of reading:** read in full: §1 (introduction), §5 (single curve), §10 (center). §9 (unit) was read through its first two lemmas and the alternating-matrix codimension lemmas. §6–8 and the companion Selmer-converse paper were **not** read.

**Status in this packet: closed as a G1 source (external methodological evidence only).** Pro's review (10-06) concurs: no Aristotle run should try to transplant Result 002 into G1. Pro reports that the §7 lemma "Bounded cuts of unary moments" is not itself rank-one-specific. A W3-only transfer is therefore conceivable, but it would improve only the per-prime W3 engine and has no endpoint effect on the uniform step.

**Verdict for G1 (the Ш-free Tame Law): `PRECISE_CORANK2_BREAK`, located at the rational anchor.** The paper's per-p integral machinery may be rank-independent. Its rational constant, however, comes from rank ≤ 1 inputs in three places, and each of them fails for the rank-two seed.

## Where corank ≤ 1 (analytic rank ≤ 1) enters

1. **The quantity being compared is defined only in rank ≤ 1.**
   - §1 defines X_p(E) = v_p(Q_E) − v_p(#Ш), with Q_E = L^{(r)}(E,1)·tors²/(r!·Ω·Reg·∏c_ℓ).
   - It is meaningful only because the analytic low-rank theorem gives finiteness and the two-primary input gives Q_E ∈ ℚ_{>0}.
   - For the seed, Q_E = q·tors²/Tam = q/4. Its rationality is RAT, which is open and is the Q36 blocker.
2. **The single-curve central identification (§5) is a rank-one Heegner argument.** In rank one, the central coordinate is identified through Proposition "Exact logarithmic comparison": log z_b / (log P)² = ± d₀·L′(E,1)/(Ω₀·H(P)). This is a Perrin-Riou-type formula, assembled from three lemmas:
   - **"Cup comparison":** Z′·log P = ±(2 − a_*)·(log z_b / log P)·h_λ(P,P). The tame linear coefficient equals the Euler factor times the Kato coordinate times the tame height. This is the rank-one counterpart of our Theorem W / BKS factorization, which we already have per p.
   - **"Spectral-height identity":** C₀·Ω₀·L(f⊗ε,1)·Z′/d₀ = ±(2 − a_*)·h_λ(Q_X,Q_X)/δ_φ.
     - Here Q_X is the Heegner point over an auxiliary K_b, chosen with the Heegner hypothesis and L(f⊗ε,1) ≠ 0.
     - This is a *tame Gross–Zagier formula*: the same kernel coefficients are evaluated by f-block projection and by intersection, following [B] §6. It supplies the rational anchor.
   - **Archimedean Gross–Zagier.**
   - **Why it fails for the seed:** for a rank-two E (root number +1), the Heegner hypothesis forces ε(E^{K_b}) = −1, so L(f⊗ε,1) = 0.
     - Q_X is then torsion, because ord L(E/K_b) ≥ 3.
     - The spectral identity reads 0 = 0, and it stays degenerate at every order in the tame variable, because L(f⊗ε,1) is a constant factor.
     - Choosing K_b with L(f⊗ε,1) ≠ 0 instead gives ε(E/K_b) = +1, and then there is no Heegner point.
     - In the Heegner setting, the first nonvanishing derivative of L(E/K,s) is the third, 3·L″(f,1)·L′(f⊗ε,1). A matching geometric formula would be a higher Gross–Zagier formula, which is not known over number fields.
3. **The pair comparison and the center (§10) need analytic rank 1 over K.**
   - Proposition "center:exact-factor" uses the simple zero of L(E/K,s) and Gross–Zagier to make P_K nontorsion.
   - It needs rank E(K) = 1 and Ш(E/K) finite, because the two rational factors have analytic ranks adding to one.
   - It needs the strict/full complex to be rationally acyclic at the center, because the compact Selmer space is the line spanned by P_K.
   - For the seed, a(E) + a(E^D) ≥ 2. At the center the strict/full complex is not acyclic, so its value is 0, and only a derived (Bockstein, p-adic-height) specialization would remain. That again gives a per-p statement with no rational anchor.

## What plausibly transfers, and why it does not give G1

- **Per-p machinery that looks rank-independent:**
  - the integral Selmer-complex models over ℤ_p[[t, u_1, …]] and the residual determinant tests;
  - integral character division;
  - the §9 divisor-removal algebra (alternating matrices, codimension two at horizontal primes);
  - the theta position-cut estimates.

  Not checked: whether §9's auxiliary-field setup (Lemma "classical:auxiliary-fields") and the §7 theta implication assume low rank.
- **Why none of it gives G1:** each of these is a p-adic statement at one prime p. At most it gives unit or main-conjecture type information about the Kato coordinate at each p, which is (K)-type and already retained at ordinary p. G1 needs a rational constant shared across p, and in this paper every such constant comes from rank ≤ 1 inputs (items 1–3).
- **External corroboration of G2's method (not of G2's statement for the seed).** §5's lemma "A nonzero height direction" uses the same mechanism as our G2:
  - the extension G_y of E by 𝔾_m from the Poincaré biextension;
  - a rational lift with Kummer cocycle (k, x), dk = −β ∪ x;
  - the nonvanishing quantity k(g) − β(g)·g_T(g_T − 1)⁻¹·x(g), compare G2's β = c − b(A − I)⁻¹a;
  - commutators on the joint kernel with k-value ±2e(x(h₁), x(h₂)) from the Weil form;
  - Chebotarev.

## W3

§7–8 (position-cut moments with growing p-level) were not read. Even if those estimates authenticated W3 source values, the gain would be per prime: W3 still carries the same constant problem as the tame scalar. **Endpoint effect: none for the uniform step.**

## The one place a rank-two analogue would have to live

A second-order tame spectral identity: the degree-two tame coefficient C₂ matched with an intersection-type quantity that does not vanish in rank two. In the Heegner setting both sides of the paper's identity vanish to all tame orders (item 2). So the geometric side would need a different object, for example Gross points in the definite case (ε = +1) or higher Heegner cycles. Neither carries a known rank-two formula over number fields. This is the record's existing frontier object (rank-two Gross–Zagier), seen in tame form.

FIN, ORDER9 and Q36 are unchanged.
