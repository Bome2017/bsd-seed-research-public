# V_PARI — referee report: PARI 2.17.4 p-adic height model-change defect, and the corrected seed Reg_5

Referee: fresh-context adversarial (V_PARI). Date 2026-09-18. Custody: this file, V_PARI_RESUME.md, runs_V_PARI/.
Status: COMPLETE. Verdict CONFIRMED_WITH_CORRECTIONS (sec 10). Run hashes: runs_V_PARI/MANIFEST.sha256.

## 1. Source reading (2.17.4, read-only)

- `src/basemath/ellpadic.c` sha256 370c8c5399a041fb51c8c75c1c32fb4b11d1ebbacee319cf7ae270e3a3118a29 (same hash C recorded).
- `ellpadicheight` (l.675-750):
  - l.688 `E = ellanal_globalred(e, &ch)`; l.689 `if (E != e) P = ellchangepoint(P, ch)`.
  - `ellanal_globalred` (elliptic.c l.5125) returns PARI's reduced minimal model and ch = [u,r,s,t] with E = ellchangecurve(e,ch);
    if the model is already minimal (trivial change), E == e and no back-map happens.
  - `ellchangepoint` (elliptic.c l.1572-1581): X = (x-r)/u^2, i.e. convention x_e = u^2 x_E + r (e = given model, E = minimal).
  - l.738-739: a = -2H/g^2, b = -(log_E)^2/g^2 computed ON E (the minimal model), in E's (omega_E, eta_E) basis.
  - l.740-745 (the back-map; C/R cite "743"):
        if (E != e) { u = ch[1]; r = ch[2]; a = (a + r*b)/u; b = u*b; }
- `ellpadicregulator` (ellpadic.c l.970-1003): F,G from ellpadicheightmatrix(E=given model) -> each entry from ellpadicheight on the
  given model; s2 = ellpadics2(given model); R = det(F - s2*G). So the regulator inherits whatever the back-map does.
- `ellpadics2` (l.804-840): s2 from ellpadicfrobenius of the GIVEN model (hyperellpadicfrobenius(ec_bmodel(E))), no model change.
- Doc (src/functions/elliptic_curves/ellpadicheight): h_E(P) = f*omega + g*eta with omega, eta "related to the given model",
  and g = -(log_E P)^2 with log_E "the logarithm for the formal group of E" (given model); canonical h = f - s2*g.

## 2. Referee's own derivation of the correct back-map (independent of C/R)

Notation as in PARI: e = given model, E = reduced minimal model, x_e = u^2 x_E + r, y_e = u^3 y_E + s u^2 x_E + t.
PARI computes (a', b') = (f_E, g_E) on E and must return (f_e, g_e) on e, where by its own doc g_e = -(log_e P)^2 and
the canonical height is f_e - s2_e g_e with s2_e = ellpadics2(e).

(i) omega_e = dx_e/(2y_e + a1 x_e + a3) = omega_E/u. So log_e = log_E/u and **g_e = g_E/u^2**.
(ii) s2 = b2/12 - E2(E,omega)/12, with u^2 b2_E = b2_e + 12 r and E2 of weight 2 (E2(omega_E) = E2(omega_e)/u^2), so
     **s2_E = (s2_e + r)/u^2**, i.e. s2_e = u^2 s2_E - r.
(iii) The sigma function with parameter c solves -D_omega(D_omega sigma/sigma) = x + c. With D_{omega_e} = u D_{omega_E}
     this is the same ODE as -D_E(D_E sigma/sigma) = x_E + (c + r)/u^2. Hence h_{e,c} = h_{E,(c+r)/u^2} for every c
     (u = 1: the sigma's coincide as functions and den x_e = den x_E, so this is literal; u != 1: constants cancel globally).
     Since h_{e,c} = f_e - c g_e is affine in c, comparing coefficients: g_e = g_E/u^2 (again) and **f_e = f_E - r g_E/u^2**.
(iv) Check: f_e - s2_e g_e = f_E - r g_E/u^2 - (u^2 s2_E - r) g_E/u^2 = f_E - s2_E g_E. Model-invariant, as it must be.

**Correct back-map: a = a' - r b'/u^2, b = b'/u^2.**
PARI 2.17.4 does a = (a' + r b')/u, b = u b'.
- u = 1: PARI's b is right, and its a has +r b' where -r b' is needed. So the r-term has the wrong sign, as C and R claim.
  PARI's canonical value is h + 2 r b' = h - 2r (log P)^2 with r = ch[2] (x_e = x_E + r). **CONFIRMED (derivation).**
- u != 1: PARI's canonical value is a'/u + r b'(1/u + u) - u^3 s2_E b', which is not a function of h alone. With r = 0 the
  u-error remains ((a'/u - u^3 s2_E b') vs (a' - s2_E b')), so for u != 1 the defect is NOT only a sign error in r.
- **Correction to C's PARI_DEFECT_ellpadicheight.md.** C writes "correct pair is a = u a' - r b'/u, b = b'/u", treating
  f omega + g eta as an intrinsic element of D. That pair gives canonical u*(a' - s2_E b') = u*h, which is wrong for u != 1.
  It also contradicts PARI's documented g = -(log_e P)^2, which scales by 1/u^2. The intrinsic object is
  (f omega + g eta) (x) omega^{-1}, not f omega + g eta. C's formula coincides with the correct one only when u = 1.
  This affects none of C's numbers (the family has u = 1), only the stated u != 1 prediction. It is tested in sec 5.

## 3. Referee's independent canonical height (runs_V_PARI/vp_canon.gp)

- Own Kedlaya / Monsky-Washnitzer Frobenius on y^2 = X^3 + aX + b (a = -c4/48, b = -c6/864, the same omega as the model),
  unit root from T^2 - a_p T + p, then s2 = b2/12 + c, where eta_wp + c omega is the unit eigenvector.
- Own sigma in the formal log z (Weierstrass wp-recurrence plus the E2 z^2/24 term), own formal log from the w(t) recursion,
  own nonsingularity test at every prime dividing disc, and h(P) = [log_p den x(kP) - 2 log_p sigma(z(kP))]/k^2.
- No ellpadic*/ellformal*/ellsigma call is used; PARI is used only for p-adic and polynomial arithmetic and the group law.
- Validation on 446d1 = [1,-1,0,-4,4] (reduced minimal, so PARI's back-map is not exercised):
  - my Frobenius has trace = -4 = a_5 and det = 5, to O(5^24);
  - my s2 = ellpadics2 to O(5^20) (PARI's full precision), and is stable to O(5^24) between (W,K) = (30,30) and (40,40);
  - my Gram matrix and regulator on [-2,2], [-1,3] agree with PARI to O(5^19) (PARI's full precision).
  - 446d1 Reg_5 = 3*5 + 5^2 + 4*5^3 + 4*5^4 + 2*5^5 + 2*5^6 + 4*5^7 + 4*5^8 + 3*5^10 + ... (runs_V_PARI/t2_446d1_height.gp; 0.9 s).

## 4. Seed (2243, 12): VERIFIED_NUMERIC (runs_V_PARI/t3_seed.gp, output t3_seed.out, 5.4 CPU-s)

Rechecked directly: m, A, B prime and all ≡ 11 (mod 24); P1, P2 on the curve; disc = 2^8 3^2 2243 4547^3 5843^2;
a5 = -2; #E(F5) = 8; Tamagawa product 16; ellglobalred ch = [1, 7578, 0, 0], so u = 1 and r = 7578 = (5A-1)/3.
The minimal model is [0,-1,0,-66020924,-65074271436] with b2 = -4. Multiplier k = 8 (my nonsingularity test passes at every bad prime).

| quantity | result |
|---|---|
| my s2 (raw) vs PARI ellpadics2 (raw) | agree to O(5^26) |
| my s2(min) - (s2(raw) + r) | O(5^33): identity (ii) of sec 2 holds |
| my Gram, raw model vs my Gram, minimal model | agree to O(5^32) (u = 1 model invariance of the sigma definition) |
| **my canonical Reg_5** | 5^2 + 3·5^3 + 3·5^4 + 3·5^5 + 4·5^6 + 4·5^8 + 4·5^9 + 5^10 + 5^11 + 4·5^12 + 4·5^13 + 4·5^14 + 5^15 + 3·5^16 + 3·5^17 + 2·5^18 + 5^19 + 2·5^20 + 3·5^22 + 4·5^24 + 3·5^25 + 3·5^26 + 4·5^27 + 2·5^28 + 2·5^29 + 3·5^30 + 4·5^31 + 4·5^32 + O(5^33) |
| PARI ellpadicregulator on ellchangecurve(e, ch) (minimal) | = mine to O(5^28), PARI's full precision |
| PARI ellpadicregulator on the raw model | 5^2 + 2·5^4 + 3·5^5 + 3·5^7 + …; v5(raw - canonical) = 3 exactly |
| PARI raw Gram - (my H - 2r·l l^T), with l = my own formal logs | O(5^27), O(5^27), O(5^28): the defect formula holds entrywise |
| PARI raw G matrix + l l^T | O(5^28): PARI's b = -(log)^2 is right for u = 1; only a is wrong |
| log P1, log P2 (own formal log) | valuations 2 and 1 |
| canonical Reg_5/25 mod 25 | 16 (raw model gives 1) |
| **canonical Reg_gamma = Reg_5/log_5(6)^2** | 1 + 4·5 + 4·5^2 + 3·5^3 + …, **≡ 21 (mod 25)** (raw model gives 6) |

Verdicts on the three seed claims:
- "canonical Reg_5 = 5^2 + 3·5^3 + 3·5^4 + 3·5^5 + …": **CONFIRMED** by an independent sigma-function implementation, in agreement with PARI on the
  minimal model. C's longer expansion (to O(5^27)) is checked in sec 7.
- "Reg_gamma ≡ 21 (mod 25)": **CONFIRMED**.
- "raw-model value correct only mod 5^3": **CONFIRMED**. v5(raw - canonical) = 3 exactly. Hence ord5 Reg_5 = 2 and Reg_5/25 ≡ 1 (mod 5) survive,
  but Reg_5/25 mod 25 and Reg_gamma mod 25 do not.
- Why the error has v5 ≥ 3 in general (C's one-line argument, rechecked): by the matrix determinant lemma,
  det(H - 2r l l^T) = det H - 2r l^T adj(H) l exactly (no r^2 term). Here r ∈ Z, v(l_i) ≥ 1 (P_i reduces into E(F5), and 8·log lands in 5Z_5),
  and for rank 2 adj(H) has the entries of H, which lie in 5Z_5 (U3 INTEG; also observed). So v5(error) ≥ 1 + 1 + 1 = 3 on every member,
  with no condition on r. For the seed it is exactly 3.

## 5. Three F_fix members: VERIFIED_NUMERIC (runs_V_PARI/t4_members.gp, output t4_members.out, 20.2 CPU-s)

For each member I rechecked m ≡ 2243 (mod Q), n ≡ 12 (mod Q), isprime(m, A, B), all three ≡ 11 (mod 24), P1 and P2 on the curve, a5 = -2, #E(F5) = 8,
Tamagawa product 16, ch = [1, r, 0, 0] with r = (5A-1)/3. Precision O(5^24) requested.

| (m, n) | n mod 25 | canonical ord5 Reg5 (mine) | v5(PARI_min - mine) | v5(PARI_raw - mine) | v5(PARI_raw - det(H - 2r l l^T)) | ord5 PARI_raw | Reg_gamma unit mod 25 |
|---|---|---|---|---|---|---|---|
| (138706163, 12) | 12 | 2 | 26 | 4 | 26 | 2 | 11 |
| (158905763, 673332) | 7 | 2 | 26 | 3 | 26 | 2 | 11 |
| (222871163, 2019972) | 22 | **4** | 26 | 3 | 26 | **3 (wrong)** | 16 (ord Reg_gamma = 2) |

- My canonical Reg5 mod 5^22 equals C's `members_canonical.csv` column Reg_D on all three rows, and my Reg_gamma unit mod 25 equals C's column.
- **Scope correction to "raw-model value is correct mod 5^3".** It holds as a statement about digits: v5(raw - canonical) ≥ 3 on every row, as the
  sec 4 argument shows. But on the n ≡ 22 (mod 25) class the canonical Reg5 itself has v5 = 4. There the raw value has the **wrong
  order** (3 instead of 4). "ord5 is unaffected" is true only where the canonical ord is 2 (the seed included). R's note says the same.

## 6. Models with u != 1: VERIFIED_NUMERIC (runs_V_PARI/t5_u_ne_1.gp, output t5_u_ne_1.out, < 1 CPU-s)

Construction: e_u = ellchangecurve(E_min, chu) and P_u = ellchangepoint(P_min, chu). PARI's own ellglobalred(e_u)[2] = ch = [u, r, s, t] maps back.
(a', b') = ellpadicheight(E_min) (validated against my implementation in sec 3-5), h = a' - s2(E_min) b'.

| case | back-change ch | PARI(e_u) vs source prediction [(a'+rb')/u, u b'] | PARI(e_u) vs referee's [a' - rb'/u^2, b'/u^2] | b'/u^2 vs -(ellpadiclog on e_u)^2 | PARI canonical on e_u (f - s2_u g) vs h | C's pair gives |
|---|---|---|---|---|---|---|
| 446d1, chu=[1/7,0,0,0] | [7,0,0,0] | agree O(5^19), O(5^20) | differ at v = -1, 0 | agree O(5^20) | differ at v = -1 (h has v = -1) | 7·h |
| 446d1, chu=[7,0,0,0] (non-integral model) | [1/7,0,0,0] | agree | differ at v = -1, 0 | agree | differ at v = -1 | h/7 |
| 446d1, chu=[1/2,3,1,5] | [2,-12,-2,-16] | agree | differ at v = -1, 0 | agree | differ at v = -1 | 2·h |
| 446d1, chu=[1,3,1,5] (u = 1 control) | [1,-3,-1,-2] | agree | a differs at v = 0; b agrees O(5^20) | agree | differ at v = 0 | h |
| 446d1, chu=[1/5,0,0,0] (u = p) | [5,0,0,0] | agree O(5^18), O(5^21) | differ at v = -2 | — | **ellpadics2 raises** "hyperellpadicfrobenius: H is singular at 5", so ellpadicregulator also raises | — |
| seed P1, chu=[1/7,0,0,0] | [7,0,0,0] | agree O(5^21), O(5^24) | differ at v = 1, 4 | agree O(5^24) | differ at v = 1 = v(h): leading digit wrong | 7·h |
| seed P2, chu=[1/7,0,0,0] | [7,0,0,0] | agree | differ at v = 2 | agree | differ at v = 2 = v(h) | 7·h |
| seed P2, chu=[1/3,1,0,0] | [3,-9,0,0] | agree | differ at v = 3, 2 | agree | differ at v = 2 | 3·h |

The referee's pair reproduces h to PARI's full precision in every case (v = 19 to 22). Also s2(e_u) = u^2 s2(E_min) - r to O(5^20) everywhere it is defined.

Seed regulator on the u = 7 model: ellpadicregulator = 4·5^2 + 5^3 + 4·5^4 + … against canonical 5^2 + 3·5^3 + …
- The ord (2) survives by accident, but Reg_5/25 mod 5 is already wrong (4 instead of 1).

Findings:
- **u != 1 is worse than a sign error.** PARI multiplies b by u where it should divide by u^2, and divides a by u.
  - The canonical height comes out wrong at its leading p-adic digit, including when u is a 5-adic unit (u = 7, 2, 3, 1/7).
  - So it is not true that "only the r-term sign" is wrong. The source line needs both fixes: a = a' - r b'/u^2, b = b'/u^2.
- **C's proposed "correct transformation" is wrong for u != 1.** It returns u·h exactly (ratios 7, 1/7, 2, 3 observed).
  - It is correct for u = 1, which covers every number C reports.
- u = p: the height silently returns a wrong [f, g] (v = -2 error), but the regulator raises an error instead of returning garbage.
- For the family model, u = 1 on every member. Nothing in C, R or U depends on the u != 1 behaviour.

## 7. Sage 10.9 comparison: VERIFIED_NUMERIC (runs_V_PARI/t6_sage.sage, output t6_sage.out, 5.4 CPU-s)

Sage's `padic_height` (sage/schemes/elliptic_curves/padics.py, Harvey/MST, with Kedlaya from Sage's own monsky_washnitzer; no PARI ellpadic call)
- uses the same normalization as PARI's f - s2 g: the 446d1 Gram matrix matches mine and PARI's entry for entry;
- gives identical Gram matrices on the raw model and on `minimal_model()` for the seed and all three members (Sage handles u = 1 changes correctly).

| curve | Sage det (raw = min) | = mine? |
|---|---|---|
| seed | 5^2 + 3·5^3 + 3·5^4 + 3·5^5 + 4·5^6 + 4·5^8 + 4·5^9 + 5^10 + 5^11 + 4·5^12 + 4·5^13 + 4·5^14 + 5^15 + 3·5^16 + 3·5^17 + 2·5^18 + 5^19 + 2·5^20 + O(5^21) | yes, to O(5^21) |
| (138706163, 12) | 5^2 + 5^3 + 5^4 + 5^5 + 5^6 + 2·5^7 + 2·5^8 + 4·5^9 + 3·5^10 + 3·5^12 + 5^13 + 4·5^14 + 2·5^15 + … | yes, digits through 5^15 |
| (158905763, 673332) | 5^2 + 5^3 + 5^4 + 3·5^6 + 4·5^7 + 5^8 + 2·5^9 + 4·5^10 + 2·5^11 + 5^12 + 3·5^13 + 3·5^14 + 5^15 + … | yes |
| (222871163, 2019972) | 5^4 + 2·5^5 + 2·5^6 + 2·5^7 + 3·5^8 + 2·5^9 + 2·5^11 + 3·5^12 + 4·5^13 + 4·5^14 + 2·5^15 + … (ord 4) | yes |
| 446d1 | 3·5 + 5^2 + 4·5^3 + 4·5^4 + 2·5^5 + 2·5^6 + 4·5^7 + 4·5^8 + 3·5^10 + … | yes |

So three independent implementations agree on every canonical regulator: the referee's sigma code, Sage's padics.py, and PARI on the minimal model.
PARI on the raw model disagrees with all three from 5^3 (seed and two members) or 5^4 (the member (138706163, 12)).

## 8. Minimal reproduction for a bug report (NOT filed; nobody contacted) — runs_V_PARI/t7_repro.gp, output t7_repro.out

```
\\ ellpadicheight/ellpadicregulator depend on the Weierstrass model (canonical p-adic height must not)
E = ellinit([0,0,1,-1,0]); P = [0,0]; p = 5; n = 10;      \\ 37a1, a_5 = -2, good ordinary
H(e,Q) = ellpadicheight(e,p,n,Q) * [1, -ellpadics2(e,p,n)]~;   \\ canonical height as in ??ellpadicheight
F = ellinit(ellchangecurve(E, [1,1,0,0]));   PF = ellchangepoint(P, [1,1,0,0]);    \\ u = 1, r = 1
G = ellinit(ellchangecurve(E, [1/2,0,0,0])); PG = ellchangepoint(P, [1/2,0,0,0]);  \\ u = 2
H(E,P)                 \\ 5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + 5^10 + O(5^11)   (= Sage 10.9 on all three models)
H(F,PF) - H(E,P)       \\ 3*5^2 + 5^3 + ...  should be O(5^11)
H(G,PG) - H(E,P)       \\ 2*5 + 4*5^2 + ...  should be O(5^11)
[ellpadicregulator(E,p,n,[P]), ellpadicregulator(F,p,n,[PF]), ellpadicregulator(G,p,n,[PG])]   \\ three different values
r = ellglobalred(F)[2][2]; g = ellpadicheight(E,p,n,P)[2];
H(F,PF) - H(E,P) - 2*r*g                      \\ O(5^11): for u = 1 the error is exactly 2*r*g = -2*r*log(P)^2
QG = ellmul(G, PG, 8); ellpadicheight(G,p,n,QG)[2] + ellpadiclog(G,p,n,QG)^2   \\ 2*5^2 + ...: contradicts the doc's g = -(log_E P)^2
```
- Same output on PARI 2.17.4 (source-matched build) and on PARI 2.17.3 (Sage env). The defect is at least as old as 2.17.3.
  The 2.17.4 CHANGES file mentions no fix to ellpadicheight.
- Sage 10.9 gives 5 + 5^2 + 5^3 + 3·5^6 + 4·5^7 + 5^9 + 5^10 + O(5^11) on E, F and G alike (runs_V_PARI/t8_sage37.sage, .out).
- Cause: ellpadic.c (2.17.4) lines 740-745, `a = (a + r*b)/u; b = u*b;`.
  Proposed fix (sec 2): `b = b/u^2; a = a - r*b;` in that order (the new b already carries 1/u^2).

## 9. Normalization anchor and cross-checks of author/Lane-1 claims

**446d1 against the published source** (runs_V_PARI/t10_446d1_SW.gp/.out). Source: Stein–Wuthrich 2013, local text
`~/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt`, lines 819-824, generators (2,0), (1,-1) (l.540).
- My E2(E0, omega) = 3·5 + 4·5^2 + 5^3 + 5^4 + 5^5 + 2·5^6 + 4·5^7 + 3·5^9 + O(5^10). This equals SW's printed value to their full precision.
- My Reg_5 = 2·5 + 2·5^2 + 5^4 + 4·5^5 + 2·5^7 + 4·5^8 + 2·5^9 + O(5^10). This equals SW (4.2) to O(5^10).
- So the referee's implementation uses SW's normalization.
- 446d1 is a reduced minimal model (ellglobalred ch = [1,0,0,0]), so it cannot detect the back-map defect. C and R make the same remark. **CONFIRMED.**

**C's full seed expansion** (C-SEED, to O(5^27)) matches mine digit for digit through 5^26. **CONFIRMED.**
The v1 values C and R flagged (ord 3 on the n ≡ 22 class) are raw-model artifacts. Sec 5 row 3 and the Lane-1 check below show this. **CONFIRMED.**

**R §6.1 derivation** (u = 1 only): σ = σ'·exp(-r z^2/2), f = f' - r g, s2 = s2' - r, and PARI returns f' + r g. This is correct and matches sec 2 at u = 1.
- R does not claim anything for u != 1.
- Imprecision (COSMETIC): R says "raw-model PARI Reg5 is correct **exactly** mod 5^3". The error is v5 ≥ 3, which is 3 at the seed but 4 at (138706163, 12),
  so "at least mod 5^3" is the accurate statement. R's own corollary ("ord reliable only when it equals 2") is exactly right.

**U10** ("PARI Gram matrices differ between models by 2·Δ(b2/12)·log P_a·log P_b"): for u = 1 translations Δ(b2/12) = r exactly, so this is the same law.
**CONFIRMED** for u = 1. It is false as stated for u != 1 (sec 6), though U does not use u != 1.

**Master-certificate ADDENDUM_001** (read-only; sha256 ec33fbea…3a4a):
- Its rank-one argument (ord change ≥ 3 for any c ∈ Z_5) agrees with sec 4.
- Its entry valuations [h11, h12, h22] = [1, 1, 2] agree with mine.
- Its sentence "only Reg5 mod 5^3 is model-independent" is about PARI's outputs.
  - The canonical value is now fixed beyond 5^3 by three independent implementations (sec 4, 7): C-SEED.
  - It should not be read as "digits beyond 5^2 are unknowable".

**Lane-1 L2A (UNVERIFIED comparison material; I do not edit it).**
- `s03_lib.gp` feeds the RAW family model to PARI 2.17.3, which has the same defect (sec 8).
- Its heights mod 25 are unaffected: the entrywise error 2r·l_i l_j has v ≥ 2.
- Its reported "ord5 Reg PARI = 3" rows are artifacts. I recomputed them (runs_V_PARI/t9_lane1_out.gp/.out, 4.8 CPU-s, all members rechecked prime with a5 = -2):

| (m, n) | L2A reports | canonical (mine) | PARI minimal | PARI raw |
|---|---|---|---|---|
| (4643, 72) | 3 | **4** | 4 | 3 |
| (683, 228) | 3 | **4** | 4 | 3 |
| (24923, 72) | 3 | **4** | 4 | 3 |
| (1523, 372) | 3 | **4** | 4 | 3 |
| (347, 204) | 4 | 4 | 4 | 4 |
| (947, 96) | 4 | 4 | 4 | 4 |

- So L2A's step-4 text "members … with n = 22 mod 25 have ord Reg_5 = 3" and step-5 "(24923,72), (1523,372) … ord5 Reg5 = 3" are wrong: the canonical ord is 4.
- Its "≥ 3" predictions and "Reg_gamma is not a unit" conclusions survive.
- The canonical value 4 agrees with R-FAIL/C-CE (ord ≥ 4 on n ≡ 22 mod 25, exactly 4 on the witnesses).

## 10. Verdict

**CONFIRMED_WITH_CORRECTIONS.**

Confirmed:
1. The PARI 2.17.4 back-map at ellpadic.c l.740-745 (`a = (a + r*b)/u; b = u*b;`) is wrong.
   - When u = 1 it is exactly a sign error on r: the output is canonical - 2r·log(P)^2, bilinearly -2r·log P_i·log P_j.
   - Evidence: my derivation (sec 2), plus entrywise agreement to O(5^26-28) with my own logs on the seed and 3 members.
   - PARI 2.17.3 has the same defect (sec 8).
2. Invisible on reduced models (446d1). The workaround (PARI on ellchangecurve(e, ellglobalred(e)[2]) = PARI's reduced minimal model) gives the canonical value,
   and so does Sage 10.9 on any model.
3. Seed canonical Reg_5 = 5^2 + 3·5^3 + 3·5^4 + 3·5^5 + 4·5^6 + 4·5^8 + 4·5^9 + 5^10 + 5^11 + 4·5^12 + … (C's full expansion to O(5^27) confirmed).
   - Three independent implementations agree: mine, Sage, and PARI-minimal.
   - My implementation is anchored to the published SW (4.2) value.
4. Canonical Reg_5/25 ≡ 16 (mod 25) and Reg_gamma ≡ 21 (mod 25); the raw model gives 1 and 6.
5. The raw-model seed value agrees with the canonical one exactly mod 5^3 (v5 of the difference = 3), so ord5 Reg_5 = 2 and Reg_5/25 ≡ 1 (mod 5) stand.
   N5 stands.
6. On the family, v5(raw - canonical) ≥ 3 always (determinant lemma, r ∈ Z, v(log) ≥ 1, H ⊂ 5Z_5), and raw ord = 2 ⇔ canonical ord = 2.
   Where the canonical ord is ≥ 4 (the n ≡ 22 mod 25 class), the raw ord can be wrong: 3 instead of 4 on (222871163, 2019972).

Corrections:
- C1 (CORRECTION, C's PARI_DEFECT_ellpadicheight.md, "Correct transformation"):
  - The stated correct pair a = u a' - r b'/u, b = b'/u is wrong for u != 1. It returns u·h (observed ratios 7, 1/7, 2, 3).
  - The correct pair is a = a' - r b'/u^2, b = b'/u^2. C's "predicts a'u vs a'/u, b'/u vs u b'" is therefore also not the right comparison.
  - C's numbers are unaffected because u = 1 on the family.
- C2 (CORRECTION, scope of "sign error in r"): for u != 1, PARI also scales wrongly: b·u instead of b/u^2, and a/u.
  - The canonical height is then wrong at its leading digit, even for 5-adic-unit u (sec 6).
  - For u = p, ellpadicheight silently returns a wrong [f,g], but ellpadics2/ellpadicregulator raise.
  - A bug report must describe both parts. Proposed fix: `b = gdiv(b, gsqr(u)); a = gsub(a, gmul(r, b));`.
  - Structural reading: PARI's line is the inverse (e -> E) of C's D-intrinsic map. So it is a direction reversal, which for u = 1 is exactly the sign of r.
- C3 (COSMETIC, R §6.1): "correct exactly mod 5^3" should read "correct at least mod 5^3". The error is v = 4 at (138706163, 12).
- C4 (CORRECTION, cross-lane, Lane-1 L2A; not ours to edit):
  - its "ord5 Reg = 3" rows for (4643,72), (683,228), (24923,72), (1523,372) are raw-model artifacts of PARI 2.17.3; the canonical ord is 4;
  - its ≥ 3 claims survive.
- C5 (COSMETIC, ADDENDUM_001): "only Reg5 mod 5^3 is model-independent" refers to PARI outputs. The canonical digits are determined (item 3).

Compute used: about 40 CPU-s of gp and 12 CPU-s of Sage. One process at a time, RSS < 100 MB, load1 < 9 throughout.
