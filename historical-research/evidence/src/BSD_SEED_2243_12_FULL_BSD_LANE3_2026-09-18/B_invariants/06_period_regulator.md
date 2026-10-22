# B.6 — Real period Ω_E and regulator Reg(E) (BSD normalisation), certified

Scripts: `scripts/rig_lib.sage` (library), `scripts/s06_calib.sage` → `out/s06_calib.out`, `scripts/s06_seed.sage` → `out/s06_seed.out`
(balls saved in `out/s06_seed_balls.sobj`). Arithmetic: Arb balls (Sage `RealBallField`, 4000 bits).

## Method (rigorous)
- **Ω.** The model is globally minimal with u = 1 (B.1), so ω = dx/(2y) is the Néron differential. With Δ > 0 and real 2-division roots
  e₃ < e₂ < e₁:
  - ω₁ = ∫ over the identity component = π / AGM(√(e₁−e₃), √(e₁−e₂)).
  - Ω_E = ∫_{E(R)} |ω| = 2ω₁ (two components, same period).
  - The roots are certified isolating intervals (Sage `roots(RealIntervalField)`). For the seed they are also the exact closed forms 0 and
    (5A ∓ 3√(mA))/2, and both give overlapping balls.
  - The AGM is enclosed by b_n ≤ AGM ≤ a_n.
- **ĥ.** Let k = lcm(c_p) = 2. Then Q = kP ∈ E₀(Q_p) for every p (checked exactly), so
  ĥ(P) = k⁻²·(2λ′_∞(Q) + log den x(Q)), with the non-archimedean part exact.
  - λ′_∞ uses Tate's series (Silverman, Math. Comp. 51 (1988), §4) on the translated model x̃ = x + c, with c chosen so x̃ ≥ 2 on E(R).
  - Tail: |Σ_{n≥N}| ≤ 4^{−N}·M/6, with M ≥ sup_{E(R)} |log z|. M is obtained from interval evaluation of z at the endpoints of the
    t-ranges and at certified critical points. For the seed, z ∈ [0.3514, 7.0587] and M = 34.19. With N = 110 the tail is < 10⁻⁶⁵.
  - Normalisation is BSD/Cremona: ĥ ≈ h(x), ⟨P,Q⟩ = ½(ĥ(P+Q) − ĥ(P) − ĥ(Q)), Reg = det⟨Pᵢ,Pⱼ⟩. This equals PARI `ellheightmatrix`,
    Sage `regulator_of_points`, and eclib.

## Calibration (the brief requires 389a1 plus one Δ > 0 rank-2 curve with rational 2-torsion from curvedata)

| curve | Δ | c_p / k | Ω (ours, ball) | Cremona curvedata Ω | Reg (ours, ball) | Cremona Reg |
|---|---|---|---|---|---|---|
| 389a1 [0,1,1,−2,0] | 389 > 0 | k = 1 | 4.98042512171011015064271558388460… | 4.9804251217101101506427155839 | 0.152460177943143751624324757049455823… | 0.15246017794314375162432475705 |
| 1088j1 [0,1,0,−25,39] (rank 2, Z/2) | 69632 > 0 | ∏c = 4 | 3.43887742039039754250306643501093… | 3.4388774203903975425030664350 | 0.531665631644888496256262446826464… | 0.53166563164488849625626244683 |
| 1088j2 [0,1,0,−65,−161] (rank 2, Z/2) | > 0 | ∏c = 8 | 1.71943871019519877125153321750546… | 1.7194387101951987712515332175 | 0.531665631644888496256262446826464… | 0.53166563164488849625626244683 |

All six values agree with Cremona's 29-digit table values to the last printed digit. Our Ω equals 2 × PARI's `omega[1]`, confirming
that Cremona's Ω includes the factor 2 for two components. Individual heights agree with Sage `P.height()` to 35 digits.

## Seed values

| quantity | value | radius | label |
|---|---|---|---|
| ω₁ | 0.0280449015194364044483094018079303841711350478666349665798010652… | < 10⁻¹⁰⁰⁰ | CERTIFIED_NUMERIC |
| **Ω_E = 2ω₁** | **0.05608980303887280889661880361586076834227009573326993315960213…** | < 10⁻¹⁰⁰⁰ | CERTIFIED_NUMERIC |
| ĥ(P₁) | 4.31114998325437968876010020758482997134350639535992234526299 | 1.7·10⁻⁶⁶ | CERTIFIED_NUMERIC |
| ĥ(P₂) | 8.35089305850265450411595173586348078476577917126169058484024 | 1.7·10⁻⁶⁶ | CERTIFIED_NUMERIC |
| ĥ(P₁+P₂) = λ | 4.12847755086578674699944601341504216037567370482174039915162 | 1.7·10⁻⁶⁶ | CERTIFIED_NUMERIC |
| ⟨P₁,P₂⟩ | −4.26678274544562372293830296501663429786680593089993626547581 | 2.6·10⁻⁶⁶ | CERTIFIED_NUMERIC |
| **Reg(E) = Reg(P₁,P₂)** | **17.7965174724903402991749412194360384163049724637781885322663** | 4.4·10⁻⁶⁵ | CERTIFIED_NUMERIC (and = Reg(E) because the index is 1, B.4, PROVED) |

Cross-checks (not rigorous, independent code): PARI 2.17.3 at 120 digits gives Reg = 17.79651747249034029917494121943603841630497246377818853226630742…
and Ω/2 = 0.02804490151943640444830940180793038417113504786663496657980106521616…. Sage `regulator_of_points` at 400 bits agrees. The
PARI value lies inside our ball.

CPU: calibration 51 s, seed 28 s.
