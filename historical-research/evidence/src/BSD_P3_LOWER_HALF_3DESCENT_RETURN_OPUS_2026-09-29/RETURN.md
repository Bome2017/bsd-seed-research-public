# Lane B2 return — explicit certificate that #Sha(E/Q)[3] ≥ 9 (Opus 5.5, 2026-09-29)

**Status: CERTIFIED.** Two ternary cubics C₁, C₂ over Z pass every check of the standalone exact verifier
`verify_certificate.gp` (items 1–3 of TASK.md), with no GRH, no class group, and no Skinner–Urban input.
Replay: `gp -q -D parisizemax=4000000000 -f verify_certificate.gp < /dev/null` (0.3 s CPU; it reads no files).
Log: `logs/verify_certificate.log`. E = [0,−1,0,−66020924,−65074271436], P₁ = (−3031, 327384), P₂ = (−2394, 281520).

## The cubics
- C₁: 61x³ + 31x²y + 15x²z − 7xy² − 56xyz − 139xz² + 20y³ + 75y²z − 23yz² + 27z³ = 0
- C₂: 92x³ + 49x²y + 73x²z − 61xy² + 50xyz + 31xz² − 35y³ + 58y²z − 58yz² − 31z³ = 0

## What the verifier recomputes from the coefficients (exact arithmetic only)
1. **Jacobian.** c₄(Cᵢ) = 3169004368 = c₄(E) and c₆(Cᵢ) = 56243184546880 = c₆(E) exactly (scaling s = 1), so
   Jac(Cᵢ) ≅ E over Q (Artin–Rodriguez-Villegas–Tate). The invariants come from Hessian covariants,
   q₄ := (d/dε)H(U+εH(U))|₀ / U and H(H(U)) = A·U + B·H(U); the verifier calibrates c₄ = q₄/12, c₆ = B/16,
   A = 48c₄² on the generic Weierstrass cubic before use. disc(Cᵢ) = Δ(E) = 2⁸·3²·2243·4547³·5843² (minimal models).
2. **Everywhere local solubility.** R: z = 0 meets Cᵢ in a real binary cubic of odd degree. At every ℓ | 3·N·disc(Cᵢ),
   i.e. ℓ ∈ {2, 3, 2243, 4547, 5843}, an explicit P with v_ℓ(U(P)) > 2·min_j v_ℓ(∂_jU(P)) (multivariate Hensel):

   | ℓ | C₁: P, v(U), min v(∇U) | C₂: P, v(U), min v(∇U) |
   |---|---|---|
   | 2 | (1,1,1), 2, 0 | (0,1,1), 1, 0 |
   | 3 | (0,0,1), 3, 0 | (0,1,1), 1, 0 |
   | 2243 | (0,2190,1), 1, 0 | (1,1133,1), 1, 0 |
   | 4547 | (0,1019,1), 1, 0 | (0,2364,1), 1, 0 |
   | 5843 | (0,4267,1), 1, 0 | (0,4914,1), 1, 0 |

   **Where "Lang" is used:** for every other prime ℓ, ℓ ∤ 6·disc(Cᵢ), so Cᵢ mod ℓ is a smooth plane cubic (the
   primitive discriminant, equal to (c₄³−c₆²)/1728 up to a unit at ℓ ≥ 5, vanishes on singular cubics over F̄_ℓ).
   Hasse–Weil then gives a smooth F_ℓ-point, and Hensel lifts it. So [Cᵢ] ∈ Sel₃(E/Q).
3. **Independence.** φ_T(ξ) := e₃(·,T)_*(res_L ξ) ∈ L^×/L^×³ is a homomorphism H¹(Q,E[3]) → L^×/L^×³, where
   L = Q[w]/(w⁸ − 1188376638w⁴ − 7030398068360w² − 117686586145348587) and T ∈ E(L)[3]. The verifier computes
   - φ_T(κ(Pᵢ)) = f_T(Pᵢ), with f_T the tangent line at the flex T (Silverman X.1);
   - φ_T([Cᵢ])^{±1} as the Cardano class of the line algebra of the unique L-rational triangle U + t₀H(U) of the
     Hesse pencil. Here t₀ ∈ L is a root of the quartic Q with Δ(U + tH) = κ·Q(t)³, checked by substitution. The
     3 lines are the ⟨T⟩-cosets of the flex torsor, a μ₃-torsor via e₃(·,T), and their étale algebra L[s]/(g),
     g = triangle restricted to z = 0, is L[z]/(z³ − c) with c = −q/2 + ε/6, ε² = −disc/3 (ε checked by squaring).
   - Uniqueness of the L-rational subgroup ⟨T⟩: ψ₃/(X − x_T) has no root mod the degree-1 prime (13, w − 1).
   - Cubic residue symbols of (κP₁, κP₂, C₁, C₂) at degree-1 primes (p, w − r), p ≡ 1 mod 3, p ∤ disc:
     the F₃-rank is 4 over 79 primes. The certifying rows are (13,1): [1,1,0,1], (13,12): [2,0,0,0], (67,50): [2,1,2,0]
     and (97,92): [1,1,2,1], with determinant 2 ≠ 0 in F₃. Inverting any single class does not change the rank.
4. **Conclusion.** κ(P₁), κ(P₂), [C₁], [C₂] are F₃-independent in Sel₃(E/Q), so dim Sel₃ ≥ 4. E(Q)_tors = Z/2 is
   checked, so E(Q)[3] = 0, and with rank E(Q) = 2 (imported; only rank ≤ 2 is needed): dim E(Q)/3E(Q) = 2.
   Hence **dim Sha(E/Q)[3] ≥ 2, i.e. #Sha(E/Q)[3] ≥ 9** (Sha[3] ⊇ (Z/3)²).

## Controls inside the verifier run (all behave as required)
- NEG(b): C₂ replaced by the Kummer cubic of P₁ (E embedded by |2O + P₁|, class κ(±P₁)) → rank 3, REJECTED.
- NEG(b′): same with P₁ + P₂ → rank 3, REJECTED.
- NEG(c2): Weierstrass cubic of the Q(i)-twist (c₄ → 16c₄, c₆ → −64c₆) → Jacobian check fails, REJECTED.
- NEG(c3): C₂ with one coefficient perturbed → Jacobian check fails, REJECTED.
- SELF-TEST: for P₁, P₂ and P₁+P₂, the triangle/Cardano class of the Kummer cubic equals the tangent-line class,
  with the same inversion each time, at all 80 primes. So both methods compute ±φ_T.

## Kill tests
- **K-B2a (feasibility): PASS.** GRH `bnfinit(L, 1)` took 1748 s CPU (1925 s wall), with max RSS 8.3 GB and peak
  footprint 9.0 GB. Cl(L) = [12,6,2] (GRH), Reg = 2.479·10²⁴, signature [2,3] (`logs/kb2a_bnf.log`). A first attempt
  was killed after 32 CPU-min because my script printed `#K.fu`, which expands the compact units.
- **K-B2b (validation): PASS.** The full pipeline finds dim Sel₃ = 2, exactly the known value, on 681b1 and 1913b1
  (rank 0, Sha = (Z/3)², no 3-isogeny). It builds two minimal cubics for each curve, e.g. 681b1:
  9x³−3x²y−3x²z+4xy²+xyz−7xz²−y³+3y²z−yz²+2z³. The same verifier certifies them (rank-2 symbols;
  `logs/kb2b_search.log`, `logs/kb2b_verify.log`). Negative controls, each REJECTED
  (`logs/kb2b_neg681.log`, `logs/kb2b_neg1913.log`):
  (a) a class ramified only at a good prime q, built by the same pipeline with the local condition at q relaxed
  (q = 263 for 681b1, 317 for 1913b1): no Hensel point at q. The class is not in the local Kummer image, so
  C(Q_q) = ∅; (b) Weierstrass cubic (class 0) and a GL₃(Z)-transform of C₁ (repeated class): dependent;
  (c) the other curve's cubic, the Q(i)-twist, and a perturbed coefficient: Jacobian mismatch.

## Search side (GRH; not trusted by the verifier)
- Sel₃(E/Q) ⊂ L^×/L^×³: L(S,3) has 15 generators (bnfunits; Cl_S[3] = 0). Local images: dims 0, 1, 0, 0, 1 at
  2, 3, 2243, 4547, 5843. Two global conditions are needed: N_{L/L₄}(α) ∈ L^×³ and additivity at split primes;
  without them fake classes appear. Result: **dim Sel₃ = 4**, containing κ(P₁), κ(P₂) (Φ-rank 15/15 on L(S,3)).
- Class → cubic: the twisted Heisenberg algebra A_ξ = (Q × L, *_α) is reconstructed multi-modularly from primes
  of order-8 Frobenius. The cube roots are pinned by α' = α/τ(α) and r_T r_{−T} = 1. Then: lazy maximal order
  (PARI `alginit`), LLL, a rank-2 zero divisor, a 3-dimensional left ideal, and the intertwiner mod p, giving the
  cubic by CRT. Next come minimisation at 2243 (one weight-(0,0,1) step) and size reduction. 16 of the 36
  non-Kummer classes (up to sign) were processed. 12 gave cubics, all with exactly E's (c₄, c₆) after minimisation;
  for the other 4 the heuristic LLL search found no rank-1 element within its bound. The smallest independent pair
  is returned.
  Details are in METHOD.md and the code in work/ (pipeline.gp, selmer.gp, covering.gp, minimize.gp).

## Imports and scope
- Imported: rank E(Q) = 2 (release R.1/R.4, 2-descent; only rank ≤ 2 is used); the ARVT Jacobian theorem for plane
  cubics; classical Hesse-pencil geometry (flexes = base points, 4 singular members = triangles of flex lines);
  Kummer theory for the Weil pairing (Silverman X.1); Hensel; Hasse–Weil.
- Not used: GRH, class groups, Skinner/Skinner–Urban, Kato, Cassels–Tate, any L-value.
- Effect: the lower half of S.3, Sha[3^∞] ⊇ (Z/3)², is now unconditional. With B1 (#Sha[3^∞] ≤ 9, if it holds), it
  would give Sha[3^∞] ≅ (Z/3)² with no SU gap and no Cassels–Tate step. This return does not prove finiteness
  or any upper bound.

## Resources and files
- Resources: ≈ 2.5 CPU-h in total (both bnfinit attempts ≈ 1.0 h), at most 2 compute processes, peak 9.0 GB.
  No paid compute, pushes, messages, subagents, or web.
- Files: RETURN.md, verify_certificate.gp (standalone), METHOD.md, NOTES.md, RESUME.md, STATE.json, logs/,
  work/ (search code; kb2a_bnf.bin is the 645 MB GRH bnf, regenerable), MANIFEST.sha256.

FIN, ORDER9 and Q36 are unchanged.
