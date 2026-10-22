# F1 — Hostile audit of the p = 3 theorem chain (seed (2243,12))

Auditor: independent hostile referee (fresh context). Started 2026-09-18.
Target: `P3_THEOREM_GATE.md` (sha256 `b1713f98…`), verdict under attack: `P3_THEOREM_CHAIN_VALID`.
Rules honoured: read-only outside `fable_audits/`; no long computation; ≤ 60 CPU-s, ≤ 1 GB per run; nothing merged.

Status of this file: **COMPLETE (2026-09-18 21:10 PDT). Verdict: `P3_CHAIN_PASS_WITH_CORRECTIONS` — see the VERDICT section at the end.**
The checkpoints below are in the order they were written (A1, A2, D, E, C, B, D′, F, G), not in the order of the brief.
Network access used: read-only fetches of four papers (Chida–Hsieh arXiv:1204.2427v3; Skinner, PJM 283; Vatsal and Greenberg–Vatsal from the author's UBC page). Jones 1989 is paywalled and was not obtained.

## 0. Source custody (hashes recomputed by me)

| source | sha256 (recomputed) | matches gate's record? |
|---|---|---|
| `Skinner_1407.1093.pdf` | `02d176d8…c0a9b988` | yes |
| `SkinnerUrban_MC.pdf` | `f9faa40a…57879748` | yes |
| `SteinWuthrich2013_shark.txt` | `680283f8…897ba038` | yes |
| `p3src/Skinner_1407.1093.txt` (text extraction) | `58e40b35…d72a9060` | (not recorded by gate) |
| `p3src/SkinnerUrban_MC.txt` (text extraction) | `bd306cd9…9d29139b` | (not recorded by gate) |


## CP-A1. Skinner arXiv:1407.1093v1 read in full (l. 1–1428 of the text extraction) — raw notes

What is printed (line numbers are of `p3src/Skinner_1407.1093.txt`):

- **Thm A (l. 44–57).** "Let p ≥ 3 be a prime"; f ∈ S_k(Γ0(N)) newform, ordinary at p w.r.t. L; (i) k ≡ 2 (mod p−1); (ii) ρ̄_f irreducible;
  (iii) ∃ q ≠ p, q ∥ N, ρ̄_f ramified at q. Conclusion: Ch_L(f) = (L_f) **in Λ_O**. §2 opens "Throughout p is a fixed odd prime" (l. 196).
  ⇒ p = 3 is inside the printed range. p | N is the point of the paper (l. 59–64); Lemma 2.1.2 (l. 285) forces p ∥ N, k = 2, a_p = ±1.
- **Non-split is explicitly inside the theorem.** l. 296–299 defines split / non-split (a_p = +1 / −1) and Thm A makes no distinction.
  The only places the two cases differ in the paper: (a) l. 577–580 (H⁰(Q_p, N_x^−) ≠ 0 only if α_f = 1 and m = k−2 — a *split-only* complication);
  (b) Thm B (iii) / §3.2 — the L-invariant and the extra zero, *split only* (l. 1120–1136: "H¹(F_p,(M⁻)^{I_p}) = 0 unless α_p = 1").
  So the non-split case is the *easy* case of Skinner's paper. No hidden non-split exclusion found.
- **Conventions (l. 236–283).** ρ_f: arithmetic Frobenius, trace ρ_f(frob_ℓ) = a_ℓ, det ρ_f = ε^{k−1} ⇒ V_f ≅ V_pE (Tate module, not its dual).
  T_f^+ ↔ character α_f^{-1}ε^{k−1}; T_f^− ↔ α_f unramified with α_f(frob_p) = a_p. For the seed at 3: α_f = ψ (unramified quadratic), T^+ ≅ Z_3(1)(ψ), T^− ≅ Z_3(ψ).
  This is the Tate-curve filtration of T_3E (twisted by ψ). ✔.
- **Selmer group (l. 386–410).** M = T_f ⊗ Λ*_O with action ρ_f ⊗ Ψ^{-1}; Sel^Σ = ker{H¹(G_S,M) → H¹(I_p,M⁻)^{G_Qp} × ∏_{ℓ∈S∖Σ} H¹(I_ℓ,M)^{G_Qℓ}}.
  I.e. Greenberg's (non-strict) ordinary condition at p, *unramified* condition at ℓ ≠ p. Lattice-independent for ρ̄_f irreducible (Lemma 2.1.1 + l. 414–419).
- **L_f (l. 706–753).** Amice–Vélu/Vishik; interpolation (2.4.1) with α_p = a_p(f) when p | N and periods Ω_f^± "canonical periods of f … well-defined up to a unit in O; see [18, §3.3.3]".
  ⇒ L_f is *only* defined up to O^×; harmless for ideals.
- **A hypothesis used but not printed in Thm A: p-distinguishedness (l. 966–974).** "Suppose also that α_f^{-1}ε^{k−1} ≢ α_f (mod m)" is needed for T^+ ⊂ T over the Hida family, hence for step (b) of the proof (l. 1021–1024).
  *Checked for the seed:* α_f is unramified while α_f^{-1}ε^{k−1}|_{I_p} ≡ ω^{k−1} = ω (k ≡ 2 mod p−1), and ω|_{I_p} ≠ 1 for every odd p (for p = 3: ω is the ramified quadratic character of Q_3(√−3)).
  So the condition is **automatic** under (i) for odd p. Not a gap. (COSMETIC: gate does not mention it.)
- **Inputs imported by the proof when p | N (l. 1001–1106):** Thm 2.5.2 (= SU Thm 1 + Kato) applied to f_m ∈ S_{k_m}(Γ0(M)), p ∤ M, k_m > 2; EPW Prop. 3.4.3 (two-variable L-function, l. 979–992); Rohrlich nonvanishing; Greenberg-style Props 2.3.2/2.3.3.
  **Skinner's own erratum to SU (l. 871–876):** SU Prop. 12.3.6 cites Vatsal [20, Thm 1.1]; "It may be that the weight two specialization of the Hida family … has multiplicative reduction at p. This case is excluded in [20] … The reference to [20, Thm. 1.1] must be augmented by a reference to [4, Thm. C]" (Chida–Hsieh, then a preprint).
  **For the seed this is not a side remark: the Hida family through f_m *is* the family through f, whose weight-2 trivial-character member is f itself, multiplicative at 3. So the chain runs through Chida–Hsieh Thm C at p = 3, k = 2, p ∥ N.** ⇒ must check CH's hypotheses on p (see CP-A2).
- **Periods (l. 1339–1372 + fn. 8).** Ω_E is a Z_(p)^×-multiple of −2πiΩ_f^+ via X_1(N)-optimal E^opt, GV Prop. (3.3) (p ∤ c if ord_p N ≤ 1), surjectivity on H_1, and a prime-to-p isogeny E^opt → E (exists since E[p] irreducible). Printed inside the proof of Thm C, which itself covers "good ordinary or multiplicative reduction at a prime p ≥ 3".

## CP-A2. Block A closed — published version + the Vatsal/Chida–Hsieh dependency (sources fetched and read by me)

Extra primary sources read for this block (read via the PDF reader; nothing written outside `fable_audits/`):
- **Skinner, Pacific J. Math. 283 (2016) 171–200** (msp.org `pjm-v283-n1-p10-s.pdf`), pp. 171–173 and 183–189.
- **Chida–Hsieh, arXiv:1204.2427v3** (= Crelle 741 (2018)), pp. 1–5 and 26–30.
- **Vatsal, "Special values of anticyclotomic L-functions"** (author's copy dated 12 Aug 2003, `~vatsal/research/mew3.pdf`), pp. 1–6, 10–14.
- **Skinner–Urban** local text: l. 562, 2282–2524 (Thm 3.6.1–3.6.9), 11740–11820 (§12.3.5, Prop. 12.3.6).

**A.1 Published statement = arXiv v1 (discharges gate item P1).** PJM p. 172: "Theorem A. Let p ≥ 3 be a prime. … (i) k ≡ 2 (mod p−1); (ii) … ρ̄_f … irreducible; (iii) there exists a prime q ≠ p such that q ∥ N and ρ̄_f is ramified at q, then Ch_L(f) = (L_f) in Λ_O."
Thm C (p. 173): "good ordinary or multiplicative reduction at a prime p ≥ 3". Footnote 1 and the §2.5 erratum to SU are unchanged (p. 188). No hypothesis was added in print.

**A.2 Every printed hypothesis, checked on the seed.**
| hypothesis | seed | verdict |
|---|---|---|
| p ≥ 3 prime | p = 3 | ✔ (printed range; SU l. 562 "p is a fixed odd prime") |
| f newform of weight k, trivial character, ordinary at p | k = 2, f = f_E, a_3 = −1 ∈ Z_3^× | ✔ |
| (i) k ≡ 2 (mod p−1) | 2 ≡ 2 (mod 2) | ✔ (vacuous at p = 3 for even k, and k = 2 anyway) |
| (ii) ρ̄_f irreducible | ρ̄_3 = GL_2(F_3) (input certified upstream; not re-derived here) | ✔ given the input |
| (iii) q ≠ p, q ∥ N, ρ̄_f ramified at q | q = 2243: v_q(N) = 1; Tate curve ⇒ ρ̄_3|I_q unramified ⇔ 3 | v_q(Δ_min); v_q(Δ_min) = 1 (re-computed by me, CP-E) | ✔ |
| (implicit) p-distinguished | automatic, see CP-A1 | ✔ |
| (implicit, SU 3.6.1) L ⊇ Q[μ_{Np}, i, D_K^{1/2}], choice of K with q inert, other primes of N/q and p split | such K exist by Dirichlet/CRT (this is SU's own proof of 3.6.4, l. 2398–2399); reduction to large L is Skinner (2.3.1) | ✔ |

**A.3 The hidden dependency, traced.** Skinner's p | N proof applies SU Thm 3.6.4 to f_m (level M = N/3, weight k_m > 2). SU's proof runs over the Hida family of f_m, **which is the family of f**, and Prop. 12.3.6 specialises to *the weight-2 trivial-character member — here f itself, with p ∥ N* — and needs **μ = 0 for the anticyclotomic L-function normalised by canonical periods** (SU (12.3.5), l. 11743–11746). Vatsal assumes "N, D, p pairwise coprime" (so not p | N); Skinner (arXiv l. 871–876 = PJM p. 188) patches with **CH Thm C**.
- CH Thm C, verbatim hypotheses (p. 3, with Thm A on p. 2): "(a) p > k − 2, (b) A_p is a λ-adic unit", "(1) (D_K, N⁻) = 1, (2) the residual representation ρ̄_{f,λ} is absolutely irreducible. Then the Iwasawa μ-invariant of Θ_∞ vanishes." Level: "N = p^{n_p} N⁺N⁻" (p | N allowed).
  **Seed:** p = 3 > 0 ✔; A_p = a_3 = −1 ✔; K chosen with (D_K, 2243) = 1 ✔; GL_2(F_3) ⊂ GL_2(F̄_3) is absolutely irreducible ✔. **So the feared restriction "p > k+1" is NOT a hypothesis of Thm C** (it belongs to CH Hypothesis (CR⁺), p. 28, used only for Prop. 6.1).
- **Residual soft spot (literature-internal).** CH's Θ_∞ is normalised by the Gross period Ω_{f,N⁻} = (4π)^k‖f‖/ξ_f(N⁺,N⁻); SU need the canonical period. Vatsal's route: μ = ord_λ(C_Eis²·C_csp) (Thm 1.1), C_csp = η_0/η_B (Lemma 2.5, p. 11), where Lemma 2.5 identifies the Gross period with (g,g)/η_B — this tacitly uses freeness of the definite-quaternionic module over its Hecke algebra.
  With ρ̄ ramified at q = N⁻ every congruent form is q-new, so T_{0,𝔪} ≅ T_{B,𝔪} and C_csp is a unit — *independently of whether p | N*. What is **not** supplied in print for (p = 3, p ∥ N, N non-squarefree) is the freeness itself: CH Prop. 6.1 assumes "(CR⁺)(1) The prime p > k+1 and p ∤ N" (p. 28) — **both fail for the seed** — and Pollack–Weston's comparison is for squarefree N (as CH describe it, p. 28; PW11 itself not read).
  This is a soft spot of *the published proof of Skinner Thm A/SU Thm 3.6.4 for non-squarefree N*, shared by every use of those theorems; it is not a hypothesis of the printed theorem and I cannot show it fails. **Label: UNVERIFIED (literature-internal), not FATAL.** See Finding 1.

**A verdict:** the printed theorem covers p = 3 and non-split multiplicative reduction; every printed (and implicit) hypothesis holds on the seed. Gate row T1 is correct as a statement about what is printed.

## CP-D. Stein–Wuthrich 2013 read at the source (l. 270–570, 731–985, 1040–1102, 1157–1310, 1405–1520)

- **Thm 6.1 as printed (l. 1068–1088):** "Assume that the reduction at p is either good ordinary or of multiplicative type." f_E = characteristic series of the dual of the **classical** Selmer group Sel_p(E/∞Q) (l. 1048–1062: kernel of H¹(nQ,E(p)) → ⊕_υ H¹(nQ_υ,E), all places). ord_{T=0} f_E ≥ r, with equality **iff** the p-adic height is nondegenerate **and** Sha(E/Q)(p) is finite; then the leading term has the valuation of ε_p·∏c_υ·#Sha(p)·Reg_γ/(#E(Q)(p))², "unless the reduction is split multiplicative". Non-split is inside the printed statement.
- **ε_p (l. 499–503):** "ε_p = 1 − 1/α = 0 if p is split multiplicative, 2 if p is nonsplit" (first power, not squared, in the multiplicative case). ε_3 = 2 is a 3-adic unit. ✔
- **Exact valuation formula (Algorithm 11.1 step 4, l. 1474–1478 and its proof l. 1494–1511):** for "a good ordinary prime or a prime at which E has nonsplit multiplicative reduction", ord_p #Sha(p) = ord_p f*_E(0) − ord_p ε_p − Σ ord_p c_υ − ord_p Reg_γ (+2 ord_p #E(Q)(p)). For the seed at 3: **ord_3 #Sha[3^∞] = ord_3 f*_E(0) − ord_3 Reg_γ**, since ε_3 = 2, ∏c_υ = 16 (re-computed, CP-E) and #E(Q)_tors = 2.
- **No hidden 3-power from the local term at 3:** #Ẽ_ns(F_3) = p + 1 = 4; there is no L-invariant and no Tate-period term in the non-split case (those occur only in the split formula (5.2) and in the split height of §4.2, l. 863–871). ✔
- **Height used (l. 825–832):** "If the reduction is nonsplit multiplicative, we use the same formula (4.1) to define the p-adic height as for the good ordinary case", i.e. ĥ_p(P) = 2 log_p(e(P)/σ_p(P)) with the canonical (Mazur–Tate) σ_p ∈ Z_p[[t]]; Reg_γ = Reg_p / log_p(κ(γ))^r (l. 975–983).
- **Provenance of the multiplicative case:** attributed to Jones [Jon89] (l. 1074–1077); the non-split bookkeeping sentence (l. 1300–1302) carries no citation. Jones 1989 is paywalled; **not read by me either** ⇒ stays UNVERIFIED-provenance (gate's P4).
  My own sanity argument that non-split ≡ "good ordinary, non-anomalous" (not a substitute for the citation):
  (a) E_0(Q_3) = norm-one units of Z_9 = T(Q_3) for the non-split torus T; by Tate–Nakayama, Ĥ⁰(G_n, T(K_nQ_9)) ≅ (G_n ⊗ X_*(T)) and Gal(Q_9/Q_3) acts on it by −1, so its invariants vanish for p odd ⇒ every point of E_0(Q_3) is a universal norm from the cyclotomic tower (finite index, prime to 3 — exactly as for good ordinary non-anomalous p; in the split case the index is infinite, which is why split is exceptional);
  (b) hence Schneider's norm-adapted height = Mazur–Tate's canonical (σ-function) height, with no log(u)²/log(q) correction; (c) the local descent term at 3 is H¹(Γ, D^{G_{Q∞,3}}) with D = Q_3/Z_3(ψ), and D^{G} = D[2] = 0.
- **Kato at multiplicative p:** SW "Kato's Theorem 7.3" (l. 1192–1199) asserts f_E | L_p in Λ for *semistable* p with ρ_p surjective, citing Kato 17.4 (good ordinary) and Kobayashi (split). For non-split no reference is given, and Skinner (PJM p. 172) says the case p | N "is excluded from Kato's divisibility theorem". ⇒ **the one-sided bound #Sha[3^∞] ≤ 9 cannot be booked as an independent Kato fallback; at p = 3 both divisibilities rest on Skinner Thm A.** (Finding 5.)

## CP-E. Regulator block — rerun + an INDEPENDENT 3-adic height (new; closes the gate's §4 "still assumed" and P5)

All runs: PARI/GP 2.17 (`run040 …/sage-env/bin/gp`), one process, `ulimit -t 60`, each ≤ 0.2 CPU-s. Scripts and outputs in `fable_audits/F1_work/`.

**E.1 Rerun of the gate's script** (`rerun_p3_reg_robust.gp`, byte-copy of `runs/p3_reg_robust.gp`): output **identical** to `runs/p3_reg_robust_output.txt` (diff empty).

**E.2 Invariants re-computed by me** (`f1_indep_height_output.txt`, l. 1–12):
- change of variables seed → minimal model = `[u,r,s,t] = [1, 7578, 0, 0]` ⇒ **u = 1** ✔; minimal model `[0,−1,0,−66020924,−65074271436]`;
- Δ_min = 2⁸·3²·2243·4547³·5843², N = 2³·3·2243·4547²·5843 ✔;
- (ℓ, Kodaira, c_ℓ, a_ℓ) = (2, I₁*, 2, 0), (3, I₂, 2, −1), (2243, I₁, 1, +1), (4547, III, 2, 0), (5843, I₂, 2, −1); **∏c = 16**, all prime to 3 ✔; **v₂₂₄₃(Δ) = 1** ⇒ ρ̄₃ ramified at 2243 ✔;
- torsion Z/2 = ⟨(−7578,0)⟩; `ellisomat` = [1,2;2,1] (isogeny class = two curves, one 2-isogeny) ✔; #Ẽ_ns(F₃) = 4, ε₃ = 2; root number +1.
- ⟨P₁,P₂⟩ is saturated at every prime ≤ 100 (`ellsaturation` returns the unimodular change (P₁+P₂, −P₁); real regulators equal to 38 digits) — consistent with the upstream "index 1".

**E.3 Independent height (`f1_indep_height.gp`).** Does not call `ellpadics2`/`ellpadicheight`, uses no Tate parameter and never leaves Q₃:
1. exact series over Q: x(t), z(t) = formal log, Bernardi σ_B = z·exp(−∬(x(z) − z⁻²)); family σ_c = σ_B·exp(−c z²/2);
2. **Mazur–Tate characterisation:** scan c ∈ (1/3)Z/81 for 3-integrality of σ_c(t) through degree 31. **Exactly one class survives: c ≡ 22 (mod 81)** (c+3⁻¹ fails at t³, c+1 at t⁵, c+3 at t⁷, c+9 at t¹³, c+27 at t¹⁹). Existence + uniqueness is what the theory predicts for ordinary (incl. multiplicative) reduction;
3. Q = 8P has non-singular reduction at all five bad primes and lies in E₁(Q₃) (v₃ t(8P) = 1, 2, 1 for P₁, P₂, P₁+P₂), so ĥ(P) = (1/64)·2·log₃(e(Q)/σ₃(t(Q))) — literally SW (4.1), with no local correction terms and no dependence on the branch of log₃ (the argument is a 3-adic unit).

| entry | independent (c = 22) | PARI `ellpadicheight·[1,−s2]` | agree mod |
|---|---|---|---|
| h₁₁ | 3 + 3³ + 2·3⁴ + 2·3⁵ + 2·3⁶ + … | 3 + 3³ + 2·3⁴ + 2·3⁵ + 3⁶ + … | 3⁶ |
| h₂₂ | 2·3 + 3² + 2·3³ + 2·3⁴ + 2·3⁵ + 0·3⁶ + 0·3⁷ + … | 2·3 + 3² + 2·3³ + 2·3⁴ + 2·3⁵ + 0·3⁶ + 0·3⁷ + 2·3⁸ | 3⁸ |
| h₁₂ | 2·3 + 2·3⁵ + 0·3⁶ + 2·3⁷ + … | 2·3 + 2·3⁵ + 0·3⁶ + 3⁷ + … | 3⁷ |
| det | 3² + 3⁴ + 2·3⁵ + 3⁶ + 3⁷ + … | 3² + 3⁴ + 2·3⁵ + 3⁶ + 2·3⁷ + … | 3⁷ |

The disagreement sets in exactly where my c (known mod 81) stops determining the value (δc·z² with ord z = 1, 2, 1 ⇒ 3⁶, 3⁸, 3⁷). Ratios independent/PARI ≡ 1, so **PARI's normalisation is SW (4.1) on the nose, including the factor 2**. Shifting c by 27 moves det only at 3⁶.
⇒ **ord₃ Reg₃ = 2 (det ≡ 9 mod 27) holds for the true Mazur–Tate canonical height, independently of PARI's Tate-curve path.** The gate's rank-one-update lemma (algebra verified: det(H + c·llᵀ) = det H + c·lᵀadj(H)l, exact, no c² term) is no longer needed as a safety net, and its unproved premise ("PARI is off by at most a 3-integral c") is superseded.

**E.4 Normalisation cross-check against the printed paper.** `ellpadicregulator(446d1, 5)` = 2·5 + 2·5² + 5⁴ + 4·5⁵ + 2·5⁷ + O(5⁸) = SW (4.2) digit for digit.

**E.5 ord₃ log₃(4) = 1** (and = 1 for every topological generator of 1+3Z₃) ⇒ **ord₃ Reg_γ = 2 − 2·1 = 0.** κ(γ) = 1+p = 4 is also the generator built into P_n(T) (SW l. 361–368), so the two normalisations match.

**E.6 "Can a non-split Tate-height ambiguity shift det by a factor 3?"** Not found. (i) log branch: irrelevant, see 3; (ii) twist over Q₉ / Tate parameter: never used by the integrality route, and the Tate route (PARI) agrees with it; (iii) L-invariant correction −log(u)²/log(q_E): split case only (SW l. 863–871); that the non-split Schneider height is the plain σ-height is printed in SW l. 831–832 and is consistent with the universal-norm computation in CP-D. **Block E: PASS, strengthened.**

## CP-C. Periods — Greenberg–Vatsal READ AT THE SOURCE (discharges gate item P3)

Source: Greenberg–Vatsal, "On the Iwasawa invariants of elliptic curves" (author's copy `~vatsal/research/gv.pdf`, = Invent. Math. 142 (2000) 17–63), pp. 31–40. (Journal pagination not compared: provenance-only.)
- **Standing hypotheses (p. 32):** "let p be a fixed odd prime. We assume that E has either good ordinary or multiplicative reduction at p, corresponding to the two cases (N,p) = 1 and (p,N/p) = 1". No split/non-split distinction, no p ≥ 5. The p-distinguished/semistability conditions needed when p | N "will be true … if f corresponds to an elliptic curve" (p. 32).
- **Canonical periods (pp. 32–33):** Γ = Γ₁(N); θ^α : S₂(Γ₁(M),Z_p)_𝔪 ≅ H¹_par(Γ₁(M),Z_p)^α_𝔪 for admissible α ("If E[p] is irreducible, then α is arbitrary"); δ_f^α = θ^α(f); Ω_f^α δ_f^α = ω_f^α.
- **Prop. (3.1) (p. 34):** "Assume that E is optimal in its isogeny class, and that p is a prime of either good ordinary or multiplicative reduction for E. Then the numbers Ω_E^α and (−2πi)Ω_f^α are equal up to a factor which is a p-adic unit."
- **Thm (3.2) = Mazur Cor. 4.1 and Prop. (3.3) (pp. 34–35):** "Assume that N is divisible by at most the first power of p. Then the integers c₀ and c₁ are equal up to a unit factor in Z_p. The integer c₁ is a p-adic unit." Seed: ord₃ N = 1 ✔.
- **Remark (3.4) (p. 37) — exactly the statement the chain needs:** "If E does not admit any p-isogenies, so that E[p] is irreducible, then it is clear that the Néron periods of any isogeneous curve differ from those of E by a p-adic unit. Thus in this case we obtain Ω_E^α = Ω_f^α, for any choice of sign." (Equality up to a p-adic unit and the factor −2πi of (3.1).)
- **SU's period = GV's period.** SU §3.3.3 (l. 1522–1548) uses M(f)_(p) = H¹(Γ₁(N), Z(f)_(p))[λ_f] (full cohomology), GV use H¹_par. H¹_par is the kernel of restriction to the cusps, whose target is torsion-free, so H¹_par is saturated in H¹; a cuspidal λ_f has no boundary component; hence H¹[λ_f] = H¹_par[λ_f] integrally, and δ_f^± generates it because f is primitive (a₁ = 1) and θ^α is a T_𝔪-isomorphism. ⇒ the two Ω_f^± agree up to Z_(p)^×. ✔ (argument mine, elementary.)
- **The 2-isogeny class.** Class = {E, E′} joined by one 2-isogeny (re-computed). Whichever is X₁(N)-optimal, β : E^opt → E has degree | 2, β*ω_E = c·ω_{E^opt} with c | 2, and the real-period ratio is c/m with m | 4. **No factor 3 can enter.** ✔
- **Same L-function.** GV (24) L(f,ζ−1) = τ(ρ⁻¹)α_p^{−m}L(f,ρ,1)/((−2πi)Ω_f^α) and SW (l. 518–521) L_α(E,ζ−1) = α^{−(n+1)}p^{n+1}G(χ⁻¹)⁻¹L(E,χ⁻¹,1)/Ω_E coincide for ρ = χ⁻¹, m = n+1 (τ(ρ⁻¹)τ(ρ) = p^m for even ρ). SW's Ω_E is the Néron period (×2 when E(R) has two components — here Δ > 0, so ×2): a 3-adic unit. The run's x_b = Re λ(r)/ω₁ with λ f-normalised is this normalisation up to the same factor 2.
- **The X₀-Manin constant is NOT needed for the theorem chain** (only c₁ enters, and 3 ∤ c₁ by (3.3)); it is needed only for the rounding lattice of the numerical run (block F). The gate says the same (§3(2)). ✔
- Not re-audited (internal to Skinner's published proof): that EPW's canonical period at the weight-2 p-new point equals SU's (Skinner Prop. 2.6.1).

**Block C: PASS at the source.**

## CP-B. Selmer identification — proof supplied (no discrepancy at all, not merely "finite")

Claim: Skinner's Sel_{Q∞,Q₃}(f) (Σ = {3}, T_f = T₃E) **equals** SW's classical Sel₃(E/∞Q) as a group; Λ-structures agree up to the involution ι: γ ↦ γ⁻¹, which preserves ord_{T=0} and the valuation of the leading coefficient.
1. *Shapiro:* H¹(G_S, T⊗Λ*(Ψ⁻¹)) ≅ H¹(Q_S/Q_∞, E[3^∞]), compatibly with local conditions (Greenberg 1989, Prop. 3.2 — standard; **cited, not read**). SU l. 2499–2508 print the resulting equality in the good ordinary case only.
2. *ℓ ≠ 3.* Q_{∞,w}/Q_ℓ is the unramified Z₃-extension, so G_{Q∞,w}/I_w has order prime to 3 and "unramified" = "zero"; the Kummer image is zero because E(Q_{∞,w}) ⊗ Q₃/Z₃ = 0. Skinner prints the first half (l. 553). ✔
3. *At 3, Kummer = strict ordinary condition.* Let K = Q_{∞,η}, K′ = K·Q₉. Over K′, E is the Tate curve: E(K′) = K′^×/q^Z, C = μ_{3^∞}, and κ(P_u ⊗ 3⁻ⁿ) is the image under H¹(K′,μ_{3ⁿ}) → H¹(K′,E[3ⁿ]) of the Kummer class of u. With H¹(K′,μ_{3^∞}) = K′^× ⊗ Q₃/Z₃ (Hilbert 90) this gives im κ_{K′} = im(H¹(K′,C) → H¹(K′,E[3^∞])) — for *every* K′ ⊇ Q₉, no deep ramification needed. Gal(K′/K) has order 2, invertible on 3-primary modules, so the idempotent (1+σ)/2 gives H¹(K,·) = H¹(K′,·)^σ, (E(K′)⊗Q₃/Z₃)^σ = im(E(K)⊗Q₃/Z₃), and the equality descends: im κ_K = ker(H¹(K,E[3^∞]) → H¹(K,D)), D = Q₃/Z₃(ψ).
4. *At 3, strict = Skinner's (inertia) condition.* The defect is H¹(G_K/I_K, D^{I_K}) = D/(Frob − 1)D. K/Q₃ is totally ramified, so Frob acts on D through ψ(Frob) = a₃ = −1 and D/(−2)D = 0. Skinner prints this: "H¹(F_p,(M⁻)^{I_p}) = 0 unless α_p = 1" (l. 1120). **The gate's defect and its vanishing are correct.** ✔
5. *Lattice:* T_f is homothetic to T₃E (Skinner Lemma 2.1.1(b)); L = Q₃, O = Z₃ is allowed (Q(f) = Q).
COSMETIC: the gate's fallback sentence ("a finite discrepancy does not change them") is true but not what happens; in the split case the discrepancy is Q_p/Z_p, not finite, so the sentence should not be reused elsewhere.

**Block B: PASS** (steps 2–5 proved here; step 1 standard with citation).

## CP-D′. Numerical addendum to block D — the non-split bookkeeping has no stray factor of 3 (`F1_work/f1_nonsplit_bsd_check.gp`, 0.3 CPU-s)

p-adic BSD in the s-variable, L_p^{(r)}(1)/r! = ε_p·∏c_υ·#Sha·Reg_p/#tors², tested with ε₃ = 1 − 1/a₃ = 2 and the plain σ-height (PARI `ellpadicL` from modular symbols vs `ellpadicregulator`; curve data from the local Cremona tables):
| curve | a₃ | rank | ord₃ L-side | ord₃ (ε·∏c·Reg/tors²) | L-side / rhs | Cremona Sha_an |
|---|---|---|---|---|---|---|
| 57a1 | −1 | 1 | 1 | 1 | 1 + O(3⁷) | 1 |
| **681c1** | −1 | **2** | 2 | 2 | **1 + O(3⁶)** | 1 |
| 681b1 | −1 | 0 | 2 | 0 | 2·3² + O(3¹⁰) | 9 |
| 33a1 | −1 | 0 | 0 | 0 | 2 + O(3¹⁰) | 1 |
The factor 2 occurs exactly on the two curves with Δ > 0 (`f1_factor2_output.txt`): PARI divides by the least real period, SW by the Néron period; a 3-adic unit (the seed also has Δ > 0). 681c1 is the same configuration as the seed (rank 2, non-split at 3) and the identity holds to 3⁶ in exactly the gate's normalisation. This is evidence about *conventions* (no hidden 3, no missing log₃(4), ε₃ to the first power), not a proof of Thm 6.1.

## CP-F. Depth-4 approximation and the rounding lattice

- **SW Prop. 3.5 (l. 451–490), re-derived.** w_{n−1}(T) = (1+T)^{3^{n−1}} − 1 divides P_{n+1} − P_n (Lemma 3.2: both interpolate ∫χ_r dμ for r ≤ n−1, and the total mass for r = 0); Gauss + Lemma 3.4 give ord₃(a_{n+1,j} − a_{n,j}) ≥ e_{n−1,j} − max(c_n,c_{n+1}), e_{n,j} = min_{1≤i≤j} ord₃ C(3ⁿ,i). Telescoping needs the bound for **every m ≥ n** (e is non-decreasing; c_m must be 0 for all m ≥ 4, not only m = 4).
- **Exponent.** e_{3,j} = [3,3,2,2,2,2] for j = 1..6 (computed; C(27,1) = 27, C(27,2) = 351 = 27·13). ⇒ **e_{3,2} = 3: a_{4,2} ≡ a₂ (mod 27)** and a_{4,1} ≡ a₁ (mod 27) provided c = 0. Depth 5 gives mod 81. ✔ (matches gate, Lane 3 §4, AUDIT_C item 11, AUDIT_D l. 46.)
- **Depth-4 measure.** Multiplicative case: μ_α(a + 3^kZ₃) = α^{−k}[a/3^k]⁺, single term (SW l. 312–320); α = a₃ = −1, α⁻⁴ = 1. κ(γ) = 1+p = 4 is built into P_n. ✔
- **c = 0 for all depths (my derivation).** gcd(3^m, N) = 3 and gcd(3, N/3) = 1, so for every m ≥ 1 each b/3^m is Γ₀(N)-equivalent to the *single* cusp of denominator 3, which is W_{N/3}(∞), hence Q-rational; φ(1/3) ∈ E(Q)_tors (Manin–Drinfeld), of order t | 2. With φ*ω_E = c_E·2πi f dz: t·c_E·λ(r) ∈ Λ_E, and Λ_E is rectangular (Δ > 0), so x_b = Re λ(b/3^m)/ω₁ ∈ (1/(t c_E))Z ⊆ (1/(2c_E))Z. c_E = c₀·(1 or 2) and 3 ∤ c₀ by Mazur (3 ∥ N; GV Thm (3.2)) ⇒ every symbol of every depth is 3-integral ⇒ **c_m = 0 for all m** ✔. (GV Prop. (3.7) prints L(E,T) ∈ Λ for E[p] irreducible, including p ∥ N, "details omitted".)
- **Lattice at denominator 81.** The gate's (1/(2c_E))Z ⊆ (1/1024)Z follows from the corrected Wuthrich Prop. 1 (2·#tors·c_E·[r]⁺/c_∞ ∈ Z with #tors = c_∞ = 2; Wuthrich's Ω⁺ is the least real period in the rectangular case, l. 225–227, so his [r]⁺ = x_b) **given the upstream inputs v₂(c₀) ≤ 8 and 4547 ∤ c₀** (not re-audited here). ✔
  *Sharper, free:* U₃ with a₃ = −1 gives a₃λ(0) = λ(0) + λ(1/3) + λ(2/3), so L(E,1) = 0 forces Re λ(1/3) = 0 exactly, and λ(b/81) − λ(1/3) ∈ Λ_f with c_EΛ_f ⊆ Λ_E ⇒ **x_b ∈ (1/c_E)Z ⊆ (1/512)Z** — a factor-2 rounding margin the run may use as an extra check (every x_b must have even numerator over 1024).
  *Why 4547 ∤ c₀ is load-bearing:* a stray denominator 4547 would move x_b by multiples of 1/(1024·4547) ≈ 2.1·10⁻⁷, **below** the certified error 2.5·10⁻⁶, so the "within error of the lattice" check cannot detect it; it must come from the upstream Edixhoven check. (A stray extra factor 2 *would* be detected.)
- SW's [r]⁺ = x_b/2 (Néron period = 2ω₁): unit. **Block F: PASS** (with the two remarks above).

## CP-G. Final arithmetic inference

Given: (a) Ch(X) = (L₃(E,T)) in Z₃[[T]] (blocks A, B, C); (b) SW Thm 6.1 for non-split p (block D); (c) ord₃ Reg_γ = 0 (block E); (d) a_{4,2} ≡ a₂ (mod 27) (block F); (e) the run: ord₃ a_{4,2} = 2.
1. (d)+(e): a₂ ≡ 9u (mod 27), u ∈ {1,2} ⇒ a₂ ≠ 0 and **ord₃ a₂ = 2 exactly**.
2. Thm 6.1 (first sentence) gives ord_T f_E ≥ r = 2; by (a) ord_T L₃ = ord_T f_E ≥ 2 (so a₀ = a₁ = 0 is *forced*; no appeal to the functional equation or to L(E,1) = 0 is needed), and a₂ ≠ 0 gives **ord_T f_E = 2 = r**.
3. Thm 6.1 ("equal to r if and only if …"): **Sha(E/Q)(3) is finite** and the 3-adic height is non-degenerate. Finiteness is an output, not an input. ✔
4. Leading terms: ord₃ a₂ = ord₃ f*_E(0) = ord₃ ε₃ + Σ ord₃ c_υ + ord₃ #Sha(3) + ord₃ Reg_γ − 2 ord₃ #E(Q)(3) = 0 + 0 + ord₃ #Sha(3) + 0 − 0. ⇒ **#Sha(E/Q)[3^∞] = 3² exactly** — an equality, because (a) is an equality of ideals (both divisibilities from the single source Skinner Thm A). ✔
5. Cassels–Tate: on a finite Sha[3^∞] the pairing is non-degenerate and alternating (Cassels 1962 for elliptic curves; for odd p antisymmetric ⇒ alternating anyway), so Sha[3^∞] ≅ A × A, #A = 3 ⇒ **(Z/3)²**. Z/9 is impossible: an alternating form on a cyclic group is identically 0. ✔
The generator γ is the same in L₃ (P_n uses 1+p), in Λ ≅ Z₃[[T]] and in Reg_γ; any other topological generator changes T by a unit power series and log κ(γ) by a unit. **Block G: PASS.**

**Addendum to CP-A2 (CH Thm 5.7 = detailed Thm C, p. 25).** "In addition to (ST) and (ord), we assume that (1) p > k − 2 and p ∤ 2^{r₀}, (2) ρ̄_{π,λ} is absolutely irreducible." (ST) "is always satisfied if (D_K, N⁻) = 1" (p. 22); (ord) is ordinarity with p-adically normalised f_{π′}; r₀ = #{q | (D_K,N⁻)} = 0. All hold for the seed at p = 3.

---

# VERDICT

## 1. `P3_CHAIN_PASS_WITH_CORRECTIONS`

I could not break the chain. Every printed hypothesis of every theorem in it holds on the seed, the one computed input (ord₃ Reg_γ = 0) is now confirmed by an implementation that shares no code path or formula with PARI's Tate-curve height, and the three "open identifications" are discharged at the source (periods: Greenberg–Vatsal, read) or by proof (Selmer groups, CP-B). No FATAL finding. The corrections are to the gate's *text and provenance table*, plus one literature-internal dependency that the gate does not mention and that I can only label UNVERIFIED.

| block | result | basis |
|---|---|---|
| A Skinner Thm A | PASS (printed theorem; published version read) — one literature-internal UNVERIFIED item | CP-A1, CP-A2 |
| B Selmer identification | PASS — groups are *equal*; proof supplied | CP-B |
| C Periods | PASS at the source (GV Prop. 3.1, 3.3, Rem. 3.4) | CP-C |
| D SW Thm 6.1, non-split | PASS as printed; Jones 1989 unread | CP-D, CP-D′ |
| E Regulator | PASS, strengthened by an independent computation | CP-E |
| F Depth 4 / lattice | PASS; e_{3,2} = 3; two text remarks | CP-F |
| G Final inference | PASS; equality, finiteness and (Z/3)² all follow | CP-G |

## 2. Numbered findings

1. **UNVERIFIED (literature-internal — the only non-trivial risk found).** Skinner's proof of Thm A for p | N applies SU Thm 3.6.4 to the higher-weight members f_m of the Hida family of f. SU Prop. 12.3.6 then needs **μ = 0 for the anticyclotomic p-adic L-function of the weight-2, trivial-character member of that family, normalised by canonical periods** (SU (12.3.5), l. 11743–11746) — and for the seed that member is f itself, with 3 ∥ N. Vatsal excludes p | N; Skinner (arXiv l. 871–876 = PJM p. 188) patches this with Chida–Hsieh Thm C, whose hypotheses I checked verbatim and which **do** hold at p = 3, k = 2 (p > k−2, A_p unit, (D_K,N⁻) = 1, ρ̄ absolutely irreducible; (ST), (ord), p ∤ 2^{r₀}). But CH's Θ_∞ is normalised by the *Gross* period. Passing to the canonical period needs η_B/ξ_f to be a unit (freeness of the definite-quaternionic module; tacit in Vatsal's Lemma 2.5). C_csp = η₀/η_B is a unit here because ρ̄₃ is ramified at q = 2243 (independent of p | N), but the freeness statement is supplied in print only by CH Prop. 6.1 under (CR⁺)(1) "**p > k + 1 and p ∤ N**" — both fail for the seed — or by Pollack–Weston for squarefree N (as described by CH p. 28; PW11 not read), and N = 2³·3·2243·4547²·5843 is not squarefree.
   *Scope:* this is not a hypothesis of the printed theorem, I have not shown that anything fails, and the same soft spot underlies every application of SU/Skinner with non-squarefree N. It is, however, load-bearing for **integrality in Λ** (not just Λ ⊗ Q₃), i.e. for exactly the power of 3 the run is meant to read off, and because Kato does not cover 3 | N there is no second source for either divisibility.
   *Cheapest discharge:* read Pollack–Weston (Compositio 2011) §6 and the later period comparisons (leads from memory, **not verified**: Kim–Ota on congruence ideals/integral periods; Castella–Kim–Longo on anticyclotomic invariants in Hida families; Hung on non-vanishing mod ℓ with canonical periods), or put the question to an author. *Recommended label for the final theorem:* "PROVED, citing Skinner (2016) Thm A as printed", with this dependency recorded.
2. **REPAIRABLE — repaired here.** Gate §4's closing premise ("PARI's Tate-curve height differs from Schneider's canonical height by at most such a c, times a 3-unit") was unproved, and a 13-curve calibration is evidence, not proof; the rank-one-update lemma is correct algebra resting on that premise. `F1_work/f1_indep_height.gp` computes the Mazur–Tate canonical height from the integrality characterisation alone (unique c ≡ 22 mod 81) and reproduces PARI's h₁₁, h₁₂, h₂₂ and det to 3⁶, 3⁷, 3⁸, 3⁷ with ratio ≡ 1. **ord₃ Reg₃ = 2, ord₃ log₃4 = 1, ord₃ Reg_γ = 0** stand without the premise. Discharges gate P5 and Lane 3's O-4.
3. **UNVERIFIED (provenance; = gate P4).** Jones, Duke 59 (1989), is paywalled and unread by everyone in the project including me. SW Thm 6.1 *as printed* covers "multiplicative type" and singles out only the split case, so the citation is exact; but the sentence "the nonsplit case never differs from the good ordinary case" (SW l. 1300–1302) carries no reference. Supporting, not replacing: the universal-norm computation (CP-D) and exact numerical p-adic BSD on the non-split curves 57a1 (rank 1) and 681c1 (rank 2) in the gate's normalisation (CP-D′).
4. **REPAIRABLE (text).** The gate's provenance table is stale after this audit: P1 (published Skinner — identical Thm A, PJM p. 172) and P3 (GV) are discharged by direct reading; row T3 "(G–V itself not read)" should cite GV Prop. (3.1), Prop. (3.3) and **Remark (3.4)**; P2 (Greenberg LNM 1716) can be replaced by the self-contained argument of CP-B, leaving only Shapiro's lemma cited; P5 is discharged by Finding 2.
5. **COSMETIC (structural, already known to Lane 3).** At p = 3 both divisibilities come from the single source Skinner Thm A. SW's "Kato's Theorem 7.3" is unsourced at non-split p and Skinner states that p | N is excluded from Kato 17.4, so there is no Kato-only bound #Sha[3^∞] ≤ 9. The gate's optional visibility audit would make only the *lower* bound independent of Skinner.
6. **COSMETIC.** Skinner §2.6 uses p-distinguishedness (α_f⁻¹ε^{k−1} ≢ α_f mod 𝔪), which is not a printed hypothesis of Thm A and is not mentioned by the gate. It is automatic for odd p under (i), since ω is ramified at p and α_f is not.
7. **COSMETIC.** Gate §3(1): "a finite discrepancy does not change them" is not what happens (the two Selmer groups are equal) and would be wrong reasoning in the split case, where the discrepancy is Q_p/Z_p. Also the Λ-structures agree only up to ι: γ ↦ γ⁻¹, which is harmless for ord_{T=0} and for the valuation of the leading coefficient.
8. **REPAIRABLE (text).** Gate §2, last row: (i) c = 0 in SW Prop. 3.5 requires 3-integrality of [a/3^m]⁺ for **all** m ≥ 4, not only at 81 — true, because every b/3^m is Γ₀(N)-equivalent to the one rational cusp 1/3 (CP-F); (ii) the row should name its upstream inputs v₂(c₀) ≤ 8 and **4547 ∤ c₀**; the latter is invisible to the run's own "within error of the lattice" check (1/(1024·4547) ≈ 2·10⁻⁷ < 2.5·10⁻⁶); (iii) the sharper lattice x_b ∈ (1/c_E)Z ⊆ (1/512)Z is available for free since [1/3]⁺ = 0.
9. **COSMETIC.** Skinner's (2.4.1)/(3.2.3) write the trivial-character multiplier as a square also when p | N, whereas MTT/SW have 1 − 1/α_p to the first power. For α_p = −1 these are 4 and 2, both 3-adic units, and at non-trivial characters the formulas coincide with SW's and GV's (CP-C). No effect on the chain.
10. **UNVERIFIED (upstream inputs, outside this audit's scope).** ρ̄₃ = GL₂(F₃); rank E(Q) = 2 with E(Q)/tors = ⟨P₁,P₂⟩ (3-saturation re-confirmed by `ellsaturation`, all primes ≤ 100); v₂(c₀) ≤ 8; 4547 ∤ c₀; and the run's own floating-point certification (the gate's stated precondition).

## 3. Exactly what a successful ord₃(a_{4,2}) = 2 run would prove

**Inputs.** (I1) ρ̄_{E,3} is irreducible. (I2) rank E(Q) = 2 and ⟨P₁,P₂⟩ has index prime to 3 in E(Q)/tors. (I3) c_E | 2⁹, i.e. v₂(c₀) ≤ 8 and 4547 ∤ c₀. (I4) A run that identifies every x_b = Re λ(b/81)/ω₁, b ∈ (Z/81)^×, as an element of (1/1024)Z with a *proved* error < 1/2048, passes the forced checks (a_{4,0} = 0, a_{4,1} ≡ 0 mod 27, Hecke relations, [1/3]⁺ = 0), and returns ord₃ a_{4,2} = 2.
**Published theorems used, as printed.** Skinner, PJM 283 (2016), Thm A · Greenberg–Vatsal, Invent. 142 (2000), Prop. (3.1), (3.3), Rem. (3.4) · Stein–Wuthrich, Math. Comp. 82 (2013), Prop. 3.5 and Thm 6.1 (Schneider, Perrin-Riou; Jones for multiplicative p) · Mazur–Tate (canonical σ) · Cassels (alternating pairing). **Not used:** Kato's divisibility, the Manin conjecture, p-adic BSD, any statement at p ≠ 3.

**Then, for E : y² = x³ − 22735x² + 106272484x:**
1. The Pontryagin dual of Sel₃(E/Q_∞) is Λ-torsion and its characteristic ideal is generated by L₃(E,T) in Z₃[[T]].
2. ord_{T=0} L₃(E,T) = 2 = rank E(Q), and ord₃ of its leading coefficient is 2.
3. **Sha(E/Q)[3^∞] is finite, #Sha(E/Q)[3^∞] = 9 exactly, and Sha(E/Q)[3^∞] ≅ (Z/3Z)².**
4. The 3-adic height pairing on E(Q) is non-degenerate (already certified: ord₃ Reg₃ = 2).
5. With the proved Sha[2^∞] = Sha[5^∞] = 0: #Sha(E/Q)[30^∞] = 9, equal to the certified numerical Sha_an = 9.

**It would not prove:** anything at p ∉ {2,3,5}; finiteness of Sha(E/Q); the complex BSD formula or the rationality of L″(E,1)/(Ω·Reg).
**Other outcomes** are as in the gate's table and remain decisive under the same chain: ord₃ a_{4,2} = 0 ⇒ Sha[3^∞] = 0; ord₃ = 1 ⇒ impossible (square order), i.e. a pipeline or theory error; a_{4,2} ≡ 0 (mod 27) ⇒ #Sha[3^∞] ≥ 81 or infinite — go to depth 5.

## 4. Remaining provenance-only issues (complete list)

| # | item | status after this audit |
|---|---|---|
| R1 | Jones 1989 (multiplicative case of SW Thm 6.1) | **unread** (paywalled). Finding 3 |
| R2 | Freeness / Gross-vs-canonical period bridge behind SU Prop. 12.3.6 at p = 3, 3 ∥ N, N non-squarefree; Pollack–Weston 2011 unread | **unread / literature-internal.** Finding 1 |
| R3 | Greenberg 1989, Prop. 3.2 (Shapiro compatibility of local conditions) | cited, not read; standard |
| R4 | EPW Prop. 3.4.3: canonical period at the weight-2 p-new point = SU's | internal to Skinner's published proof; not re-audited |
| R5 | Mazur–Tate 1991: existence/uniqueness of the integral σ at a multiplicative prime, p = 3 | not read; confirmed numerically on the seed (unique c mod 81; agreement with the Tate-curve formula) |
| R6 | GV read in the authors' copy, not the Inventiones print | pagination/wording not compared |
| R7 | Upstream nodes: ρ̄₃ = GL₂(F₃); rank and generators; v₂(c₀) ≤ 8; 4547 ∤ c₀ | not re-audited here (Finding 10) |
| R8 | The run's floating-point certification (gate precondition: rigorous streaming core) | outside scope; must be in place before the result is labelled |
| — | gate P1 (published Skinner), P3 (GV), P5 (PARI Tate-path height) | **discharged** by this audit |
| — | gate P2 (Greenberg LNM 1716 §2) | superseded by the proof in CP-B (except R3) |

## 5. Recommendation on the label

Keep the gate's conclusion; change its verdict string from `P3_THEOREM_CHAIN_VALID` to **VALID (published-theorem level), with R1 and R2 recorded as open provenance**, and apply Findings 2, 4, 7, 8 to the text. Nothing found here argues against authorising the depth-4 run: every outcome remains decisive under the chain, and the soft spot in Finding 1 is a property of the literature, not of the seed or of the computation.

*Audit complete. Files: this report; `F1_work/` (8 scripts/outputs, all ≤ 0.3 CPU-s). Nothing outside `fable_audits/` was written; nothing merged; no long computation rerun.*
