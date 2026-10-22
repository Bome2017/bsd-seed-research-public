# B.4 — Mordell–Weil generators, rank upper bound and FULL saturation

**Result: E(Q) = ⟨T⟩ ⊕ ⟨P₁, P₂⟩ ≅ Z/2 × Z², with T = (0,0), P₁ = (4547, 327384), P₂ = (5184, 281520).
The index [E(Q) : ⟨T, P₁, P₂⟩] is exactly 1. Label: PROVED** (two independent routes, below). Route (a) (eclib) was complete as
first delivered. Route (b) is complete only after the enumeration-box fix required by the referee (AUDIT_B correction #1,
2026-09-18; see §4.2 "Audit correction" and `00_LANE_B.md` "Audit response"). The fix changed no enumerated point set.

On the reduced minimal model E_r (x_r = x − 7578): Q₁ = (−3031, 327384), Q₂ = (−2394, 281520), T_r = (−7578, 0).

## 4.0 Rank

- **rank E(Q) ≤ 2**, from mwrank's first 2-isogeny descent: rk S^φ(E′) = 2 and rk S^φ′(E) = 2, so the "rank bound = 2" line
  (`out/s04a_mwrank_v1_S-1.out`). The second descent gives the same bound. PARI `ellrank` (Simon-style 2-descent) independently gives
  [r₁, r₂, s] = [2, 2, 0] (`out/s04b_pari.out`). **PROVED** (2-descent; two implementations).
- **rank ≥ 2**: P₁, P₂ are independent, because the height-pairing determinant is 17.7965… ≠ 0. That value is rigorous: it is
  enclosed in B.6 with a certified error below 10⁻⁵⁰. **PROVED.** So **rank = 2**.

## 4.1 Route (a): eclib / mwrank (Cremona)

- `mwrank -v 1 -S -1 -l` (eclib 20250627; `-S -1` = saturate at all primes up to a computed index bound) on E₀
  (`out/s04a_mwrank_v1_S-1.out`) returns the basis {P₂, G} with G = (5843, 210348) and regulator 17.79651747249. It ends: "The rank
  and full Mordell-Weil basis have been determined unconditionally."
- Sage `E.gens(proof=True, algorithm='mwrank_lib', use_database=False)` returns [(5184, 281520), (5843, 210348)], with
  `gens_certain() = True` (`out/s04a_sage.out`).
- Relation to P₁, P₂ (exhaustive search over small coefficients, exact point arithmetic): P₂ = P₂, and
  G = −P₁ − P₂ + T. The change-of-basis matrix [[0,1],[−1,−1]] has determinant 1. So ⟨T, P₁, P₂⟩ = ⟨T, P₂, G⟩.
- eclib saturation applied directly to [Q₁, Q₂], via `mwrank_MordellWeil.saturate(max_prime=-1)` with verbose output:
  "Saturation index bound (for points of good reduction) = 2; Tamagawa index primes are [ 2 ]; Checking 2-saturation; Points
  were proved 2-saturated (max q used = 31)". Result (ok, index, unsat) = (True, **1**, []). Sage `E.saturation([P1,P2])` gives
  index 1 and regulator 17.7965174724903.

## 4.2 Route (b): PARI ellrank + ellsaturation + an index bound proved here

**Index bound.** Let Λ = E(Q)/E(Q)_tors with the quadratic form ĥ, and let the bilinear form be ⟨P,Q⟩ = (ĥ(P+Q) − ĥ(P−Q))/4.
Let n = [Λ : ⟨P₁,P₂⟩]. Then Reg(P₁,P₂) = n²·Reg(E). By Hermite's inequality in dimension 2 (γ₂ = 2/√3, i.e. every positive definite
binary form of determinant D has a nonzero value ≤ √(4D/3)), λ := min{ĥ(P) : P ∉ E(Q)_tors} ≤ (2/√3)·√Reg(E). Hence

    n ≤ (2/√3) · √Reg(P₁,P₂) / λ.

(Torsion: E(Q)_tors = ⟨T⟩ by B.2, so [E(Q) : ⟨T,P₁,P₂⟩] = n.)

**Height-difference constant.** Source: J. H. Silverman, "The difference between the Weil height and the canonical height on
elliptic curves", Math. Comp. 55 (1990) 723–743, Theorem 1.1. For an integral Weierstrass model,
−(1/24)h(j) − μ(E) − 0.973 ≤ ĥ_S(P) − ½h(x(P)) ≤ μ(E) + 1.07, where
μ(E) = (1/12)h(Δ) + (1/12)h_∞(j) + ½h_∞(b₂/12) + ½log 2* (2* = 2 if b₂ ≠ 0), and ĥ_S = ½ĥ is Silverman's normalisation. In the
BSD/Cremona normalisation (ĥ = 2ĥ_S, h(P) = log max(|num x|, den x)) this gives |h(P) − ĥ(P)| ≤ 2·max(h(j)/24 + μ + 0.973, μ + 1.07).
We use the published constant 0.973, not the smaller 0.961 that Sage and eclib use (Bremner's correction). We also take the maximum
of the two sides, so the bound holds whichever way round the inequality is read.

**Which side is needed (AUDIT_B note #4).** The enumeration argument uses only h(P) ≤ ĥ(P) + B, i.e. only the LOWER side
ĥ_S − ½h ≥ −(h(j)/24 + μ + 0.973), which gives h − ĥ ≤ 2(h(j)/24 + μ + 0.973) = 16.479 on E_r (16.455 with 0.961). This refined
lower-side form is the one implemented in Sage's `silverman_height_bound` (source read by the referee: `ell_rational_field.py`
l.2745–2756, which cites eclib `htconst.cc` for the 0.961 constant), so it is corroborated by two independent implementations.
The crude form below is transcribed from the paper's abstract only; its transcription is NOT confirmed from the primary source
(neither the lane nor the referee could retrieve the paper). It is not load-bearing: B below is the maximum of all four
one-sided constants, so B ≥ 16.479 whatever the crude form says.

On E_r: h(Δ) = 58.0706…, h(j) = 34.8182…, h_∞(j) = log 1918.7… , b₂ = −4 (so h_∞(b₂/12) = 0), μ = 5.81574…, and

    B_S = 16.47900579… (exact formula evaluated at 60 digits in `out/s04b_pari.out`).

**Robustness against transcription of the constant.** The paper is not available locally. The refined μ-form above is the one
implemented in Sage (`silverman_height_bound`) and eclib (`htconst.cc`). The paper's abstract states the cruder form
−(1/8)h(j) − (1/12)h(Δ) − 0.973 ≤ ĥ_S − ½h(x) ≤ (1/12)h(j) + (1/12)h(Δ) + 1.07. Both forms are evaluated in
`scripts/s04b_pari_simpleform.gp`, and the proof uses the **maximum of all four one-sided constants in BSD normalisation**:

    B := max(20.32899, 17.62147, 16.47901, 13.77149) = 20.328990846003278982.

For comparison, eclib's CPS bound (Cremona–Prickett–Siksek, J. Number Theory 116 (2006)) is 9.790 (`out/s04a_sage.out`). It is not
used in the proof.

**Complete enumeration.** If P is non-torsion with ĥ(P) < λ₀, then h_r(P) ≤ ĥ(P) + B < λ₀ + B (h_r = naive height on E_r). Enumeration method (script
`scripts/s04b_enum_lib.gp`), all exact:
- On E₀: y² = x(x² + ax + b), with a = −5A and b = 4AB, write x(P) = m/e² in lowest terms, m ≠ 0. Let s be the signed squarefree
  part of m, so m = sM².
- Since m·(m² + ame² + be⁴) is a square and gcd(m, e) = 1, every prime dividing s divides b. So s is one of the 16 signed squarefree
  divisors ±{1, 2, A, 2A, B, 2B, AB, 2AB} of b. Also (X, W) = (M/e, N/e²) lies on W² = sX⁴ + aX² + b/s.
- h_r(P) ≤ H forces e² ≤ e^H and |m| ≤ (1 + 7578)e^H.
- gcd(M, e) = 1 (because gcd(m, e) = 1), so X = M/e is in lowest terms with denominator e. All 16 quartics are searched with Stoll's
  ratpoints (PARI `hyperellratpoints(Q, [N, D])`, which returns the X = a/b with |a| ≤ N and 0 < b ≤ D; semantics checked by the
  referee on the s = AB quartic) with N = ⌊√(7579·e^H/|s|)⌋ + 1 and D = ⌊e^{H/2}⌋ + 1, i.e. the box |M| ≤ √(7579·e^H/|s|),
  e ≤ e^{H/2}, and the results are filtered by h_r ≤ H.
- **Audit correction (AUDIT_B #1, BLOCKING, applied 2026-09-18).** As first delivered, `scripts/s04b_enum_lib.gp` passed
  D = min(e^{H/2}, N) instead of D = e^{H/2}. For the 8 quartics with |s| > 7579 (s = ±2A, ±2B, ±AB, ±2AB) this truncated the
  denominator range, so the completeness claim was not supported by the script. The library now passes [N, D] = [Mmax, emax].
  `scripts/s04b_box_audit.gp` (`out/s04b_box_audit.out`) compares the two boxes on those 8 quartics at every search height used
  here (11, 18.979, 20.679, 22.829, 24.529). Only s = +AB gains points: X = ±48/4115 (= ±(2P₁+2P₂+T), h_r = 24.9296) and
  X = ±96/6275 (= ±(2P₁+T), h_r = 24.7036); at H = 11 also ±1/12, ±1/36 (h_r = 17.05, 16.63). Every extra point has h_r > H and is
  filtered out. All s04b scripts were rerun with the corrected library. Against the pre-audit outputs (kept in
  `out/superseded_truncbox/`), the only changes are the raw quartic-point counts (+8) and timings. Every enumerated point set,
  every height, λ and every index bound below is unchanged.
- Validation: at H = 11 the method reproduces a naive brute-force enumeration on E_r exactly: 7 points up to sign, including T
  (`out/s04b_enum_validate.out`).
- Consistency: at H = 18.979 and H = 20.679, the enumerated set equals the set of all a·P₁ + b·P₂ + εT (|a|, |b| ≤ 6) of naive height
  ≤ H: 11 points up to sign in both cases, none missing, none extra (`out/s04b_enum_crosscheck.out`).

**λ₀ = 2.5 with B = 20.329** (search height H = 22.829, e^H = 8.2·10⁹; 19.5 CPU-s with the corrected box; `out/s04b_pari_simpleform.out`): the search finds
10 non-torsion points up to sign (plus T). The smallest canonical height among them is 4.12848 > 2.5. So **λ ≥ 2.5**, and
n ≤ (2/√3)·√17.79652/2.5 = **1.948**, hence **n = 1**. **PROVED.**

The same point set is found with the refined constant (H = 18.979, 0.48 s; `out/s04b_pari.out`). Explicit combinations
a·P₁ + b·P₂ + εT with |a|, |b| ≤ 6 show a gap in naive height from 17.053 to 23.757 (`out/s04b_combo_heights.out`). This is why the
set does not change between H = 17.1 and H = 22.8.

The margins are large: Reg(P₁,P₂) is only needed to 1 digit here, and it is certified to 50+ digits in B.6.

**λ₀ = 4.2.** First run (refined lower-side constant only, B = 16.479, search height 20.679, 2.4 s; `out/s04b_pari_lam42.out`).
Robust rerun for AUDIT_B note #2 (B = 20.329, the maximum of all four constants, search height 24.529, corrected full box, 106 CPU-s;
`scripts/s04b_pari_lam42_crude.gp`, `out/s04b_pari_lam42_crude.out`): 12 points up to sign incl. T. The one point beyond the H = 20.679
set is the small combination with h_r = 23.757 and ĥ = 21.0025. The combination cross-check at H = 24.529 gives 12 combinations,
12 enumerated, 0 missing, 0 extra. In both runs the only non-torsion points with ĥ < 4.2 are ±(P₁+P₂) and ±(P₁+P₂+T), both with
ĥ = 4.128477550865786746999446013415042160376. So **λ = 4.12847755086578674699944601341504216 exactly** (attained). This gives
n ≤ 1.1799. **PROVED**, and it no longer depends on which Silverman constant is used. (The value of λ is CERTIFIED_NUMERIC by the
B.6 method. Only λ > 2.44 is needed.)

**PARI checks.** `ellrank(E_r)` = [2, 2, 0, L], and the regulator of L is 17.79651747249034029917494121943603841630, the same as
Reg(P₁,P₂). `ellsaturation(E_r, [Q₁,Q₂], 100)` returns a basis W with Reg(W)/Reg(Q₁,Q₂) = 1.000…, so the index is not divisible by
any prime < 100 (PARI's documented guarantee).

## 4.3 Certificate summary

| quantity | value | label |
|---|---|---|
| rank | 2 (upper bound: 2-descent in mwrank and PARI; lower bound: det ≠ 0) | PROVED |
| E(Q) | ⟨T⟩ × ⟨P₁, P₂⟩, index 1 | PROVED (route a: eclib saturation with its own index bound; route b, complete after the AUDIT_B #1 box fix: Silverman 1990 bound (max of both published forms, B = 20.329) + complete ratpoints enumeration to naive height 22.829 + Hermite γ₂ = 2/√3, n ≤ 1.948) |
| λ = min ĥ on non-torsion | 4.1284775508657867469994460134150421604 = ĥ(P₁+P₂) | PROVED to be attained (with B = 16.479 and with B = 20.329); value CERTIFIED_NUMERIC (B.6) |
| Reg(P₁,P₂) | 17.79651747249034029917494121943603841630… | CERTIFIED_NUMERIC (B.6) |
| height pairing | ĥ(P₁) = 4.311149983254379688760…, ĥ(P₂) = 8.350893058502654504116…, ⟨P₁,P₂⟩ = −4.266782745445623722938… | CERTIFIED_NUMERIC (B.6) |

CPU for B.4: about 70 s in total before the audit. Most of it is the brute-force validation (33 s) and the B = 20.329 search (22 s).
Audit repair (2026-09-18): box audit 0.25 s, reruns 55.7 s, robust λ₀ = 4.2 run 106.2 s.
