# RANK2_GLOBAL_OBJECT_COMPOSITION — seed (2243,12)

Theorem-design lane. NOTHING MERGED. Append-only working document; partial conclusions are written as they are reached.
Inputs read: F3 (large-p Sha hunt), F4 (second-derivative rationality hunt). Local primary texts used for interfaces:
`…GLOBAL_ARCHITECT…/fable_audits/F4_work/sources/D/ota_1509.00682.txt`, `…/D/bks2_2103.11535.txt`,
`~/BSD_ABC_REVIEW_2026-09-17/sources/BKS24_jmsj76.txt`, `…/KIM_2203.12159.txt`.

Status labels used below: PROVED (in print, hypotheses checked for the seed by F3/F4 or here), DERIVED (proved here, needs a
referee), FORMULATED (precise statement, unproved), HEURISTIC, KILLED.

## 0. Notation

- E the seed, r = 2, E(Q) = Z/2 × Z·P1 × Z·P2, W := ∧²(E(Q)/tors) = Z·ω, ω := P1∧P2.
- S = squarefree product of good primes; G_S = Gal(Q(μ_S)/Q) (or its ± quotient); I_S ⊂ R[G_S] augmentation ideal;
  gr^k(G_S) := I_S^k/I_S^{k+1}. For S = ℓ prime: gr^k(G_ℓ) ≅ R/(ℓ−1) for every k ≥ 1.
- θ_S = Σ_a [a/S]^+ σ_a ∈ R[G_S] the Mazur–Tate element; R = Z[1/bad] with Ota's finite bad set (for the seed: primes
  ≤ 3, primes of N; every p ≥ 5 with p ∤ N stays non-invertible — F3 row 0).
- Norm relation (from the Hecke relation on modular symbols, ℓ ∤ SN):  π^{Sℓ}_S θ_{Sℓ} = (a_ℓ − σ_ℓ − σ_ℓ^{-1}) θ_S.

## 0.1 First structural observation (written 04:55Z, before the tests) — HEURISTIC, to be sharpened below

The family Θ_E := (θ_S)_S IS a p-independent characteristic-zero object (it is equivalent to the distribution
χ ↦ τ(χ)L(E,χ̄,1)/Ω^± of all twisted central values). Ota's Thm 1.2 puts Θ_E in ∏_S I_S². Its universal leading term
θ̃_E := (θ_S mod I_S³)_S lives in 𝓛 ⊂ ∏_S gr²(G_S) — a product of FINITE groups, hence a module over Ẑ = ∏_p Z_p with no
Z-structure: θ̃_E = (θ̃_{E,p})_p and "θ̃_E ≠ 0" says nothing about almost all p-components.
So the obstruction in TEST 1 is not that the source depends on p. It is that the target of the leading-term map has no
rational line. The Mazur–Tate conjecture supplies exactly such a line: Z·𝓡_E with 𝓡_E := (J_S·R_S(ω))_S the tame regulator
family of the generator ω of W. Wall 1 then splits into
  (P) primitivity of 𝓡_E at p (a statement about P1, P2 only — Chebotarev-type, see TEST 2), and
  (L) the line statement θ̃_E ∈ Q·𝓡_E with one rational scalar m (the missing compatibility).
(TO CHECK against the primary texts: exact normalisation of the MT conjecture — my recollection of J_S and the Euler factor
a_ℓ − 2 versus #E(F_ℓ) does not close under S ↦ Sℓ; see §1.)

## 1. Interface check against the primary text (Ota arXiv:1509.00682, local txt l. 212–275) — 05:10Z

- Prop 2.3(1): π_{Sℓ/S} θ_{Sℓ} = −Fr_ℓ(1 − a_ℓ Fr_ℓ^{-1} + Fr_ℓ^{-2}) θ_S  (= (a_ℓ − Fr_ℓ − Fr_ℓ^{-1}) θ_S). Matches §0.
- Prop 2.3(2): χ(θ_S) = τ_S(χ) L(E,χ^{-1},1)/Ω^{χ(−1)} for χ of conductor S.
- **Conjecture 2.4 (Mazur–Tate), exact form:** S squarefree prime to N. Then θ_S ∈ I_S^{r}, Sha finite, and
      θ̃_S = |Sha| · Σ_{T|S} (−1)^{ν(T)} J_T · η_r(μ_{S,T}(d_T))   in  I_{S+}^{r}/I_{S+}^{r+1},
  J_T = #coker(E(Q) → ⊕_{ℓ|T}E(F_ℓ) ⊕ ⊕_{ℓ|N}E(Q_ℓ)/E_0(Q_ℓ)), d_T the discriminant of the G_T-valued height pairing
  E(Q) × E_T(Q) → G_T, μ_{S,T} the transfer-type map G_T → G_S, η_r the map Sym^r → gr^r (MT (2.5), (2.6), (3.1)).
- CORRECTION to §0.1: the regulator side is the ALTERNATING DIVISOR SUM, not J_S R_S alone. This repairs the closure
  problem I flagged: a_ℓ − 2 = (ℓ − 1) − #E(F_ℓ) is matched term by term by the T ∌ ℓ and T ∋ ℓ summands. Define
      𝓡_S(ω) := Σ_{T|S} (−1)^{ν(T)} J_T · η_2(μ_{S,T}(d_T(ω)))  ∈ gr²(G_{S+}) ⊗ R,     𝓡_E := (𝓡_S(ω))_S.
  d_T is computed from a basis of E(Q)/tors and a basis of E_T(Q)/tors with compatible orientation, so it is a function of
  the ORIENTED GENERATOR ω ⊗ ω of (∧²E(Q))^{⊗2} — independent of the sign of ω. For the seed this is a canonical element.
- Thm 1.5 (special case of 6.4): p non-invertible in R, S squarefree, all ℓ|S good, ℓ ≡ 1 (p), E(F_ℓ)[p] cyclic;
  θ̃_S ≢ 0 mod p·gr^r ⇒ Sha[p] = 0 and p ∤ J_S. PROVED, unconditional.
- Remark 2.5(1)(a): if |G_S| ∈ R^× then I_S = I_S² = … — the algebraic form of "one S serves only the p dividing |G_S|".

## 2. TEST 1 — Ota + BKS: can (θ_S)_S be assembled before reduction mod p?  — 05:45Z

**Construction (DERIVED, elementary).** Let 𝒮 = admissible squarefree S (good primes ℓ, E(F_ℓ)[p] cyclic for all p ≥ 5).
- 𝓔 := {(x_S) ∈ ∏_{S∈𝒮} R[G_S] : π_{Sℓ/S} x_{Sℓ} = (a_ℓ − Fr_ℓ − Fr_ℓ^{-1}) x_S}. Θ_E := (θ_S)_S ∈ 𝓔 (Ota Prop 2.3(1)).
- Ota Thm 1.2 ⇒ Θ_E ∈ 𝓔^{(2)} := 𝓔 ∩ ∏ I_S². Leading-term map λ: 𝓔^{(2)} → 𝓜 := ∏_S gr²(G_{S+}) ⊗ R; θ̃_E := λ(Θ_E).
- Θ_E is p-independent and of characteristic zero; by Prop 2.3(2) it is the same datum as the distribution of twisted
  central values χ ↦ τ(χ)L(E,χ̄,1)/Ω^±. **So "the source object depends on p" is NOT the obstruction.** YES: the dependence
  on ℓ ≡ 1 (p) can be moved entirely into the realisation map real_{p,S}: 𝓜 → gr²(G_{S+}) ⊗ Z/p.

**Exact algebraic obstruction (DERIVED).** 𝓜 is a product of finite groups: 𝓜 = ∏_p 𝓜_p is a module over Ẑ = ∏_p Z_p, and
θ̃_E = (θ̃_{E,p})_p. In a Ẑ-module the components at different p are unrelated: there is no functional 𝓜 → (torsion-free
R-module) through which "θ̃_E ≠ 0" could force θ̃_{E,p} ≢ 0 for almost all p. (Remark 2.5(1)(a) is the finite-level shadow.)
Hostile question 8 fails for 𝓜, and it fails for every quotient of 𝓔^{(2)} built from augmentation quotients.
What is missing is therefore not an object but a **Z-structure on the target**: a rank-one R-submodule 𝓛_Z ⊂ 𝓜 with
θ̃_E ∈ 𝓛_Z ⊗ Q ∩ 𝓜. For a free rank-one 𝓛_Z = R·𝓡, membership reads θ̃_E = m·𝓡 with ONE m ∈ R[1/D], and then
"m ≠ 0" does control almost all p — PROVIDED 𝓡 is p-primitive for almost all p.

**Where BKS enters.** BKS's η^BSD = (L″/(2Ω⁺R_∞))·ω is, in this language, the pair (rational line Q·ω, scalar). The MT
conjecture 2.4 says: 𝓛_Z = R·𝓡_E (tame regulator family of ω, §1) and m = |Sha|. The design question becomes which part
of that is needed for Wall 1 (answer in §6: only the LINE part, not the value of m, not finiteness of Sha).

## 3. TEST 4 — derived Kato / Kurihara + Ota: do the per-p maps factor through the universal object? — 05:50Z

YES (PROVED in print, assembled here). For n = ℓ1ℓ2 ∈ 𝒮 put g_n = gcd(ℓ1−1, ℓ2−1) and let
  pr_n : gr²(G_n) → G_{ℓ1} ⊗ G_{ℓ2} ≅ Z/g_n  be the multilinear projection.
Then δ_n^{univ} := pr_n(θ̃_n) = Σ_a [a/n]^+ (σ_a|ℓ1 ⊗ σ_a|ℓ2) ∈ (G_{ℓ1}⊗G_{ℓ2}) ⊗ R is a **p-independent Kurihara number**, and for
every p | g_n with ℓ_i Kolyvagin primes for p, δ_n^{univ} ⊗ Z/p^k is Kurihara's δ_n (Kim 2203.12159 §1; Kurihara 2014).
The derived Kato classes map to these by Kato's reciprocity law / Kurihara–Kim (δ_n ~ exp*_p(κ_n^{Kato})); Ota's
Darmon–Kolyvagin derivatives of order 2 at one prime give the diagonal components gr²(G_ℓ).
Diagram (all arrows PROVED):

   Beilinson–Kato elements (K_2 of modular curves, p-independent, motivic)
        │ étale realisation at p                         │ modular symbols (Betti)
        ▼                                                ▼
   z^{Kato}(p) ∈ ES(T_pE)  ──Kolyvagin derivative──►  κ_n(p)  ──exp*_p──►  δ_n ⊗ Z_p  ◄──real_{p,n}── θ̃_E ∈ 𝓜
                                                                                         ▲
                                                                     Θ_E = (θ_S)_S ∈ 𝓔^{(2)} (Ota 1.2)

So the universal Mazur–Tate object EXISTS and recovers every Ota/Kurihara per-p witness (this is outcome 3 of the brief,
UNIVERSAL_MAZUR_TATE_OBJECT_FOUND, in the weak sense). It does not by itself move Wall 1, for the reason in §2: its
coefficient module has no rational line. The arrow that is missing is on the OTHER side of 𝓜 (the regulator side).

## 4. TEST 2 — Ota + ∧²E(Q): canonical determinant comparison — 06:00Z (clock times in this file are approximate)

**Canonical comparison (DERIVED; it is MT's regulator read functorially).** The G_T-valued height is a homomorphism
E_T(Q) → Hom(E(Q), G_T). Its second exterior power is a map ∧²E_T(Q) ⊗ ∧²E(Q) → Sym²(G_T) → gr²(G_T), and
∧²E_T(Q) = [E(Q):E_T(Q)]_{free}·∧²E(Q). Hence for every T there is a canonical R-linear map

      Reg_T^{MT} : (∧²E(Q))^{⊗2} ⊗ R → gr²(G_{T+}) ⊗ R,      and   Reg^{MT} := (Σ_{T|S}(−1)^{ν(T)} J_T η_2 μ_{S,T} Reg_T^{MT})_S : (∧²E(Q))^{⊗2} ⊗ R → 𝓜.

The source is the SQUARE of the determinant line, canonically Z·ω^{⊗2} (the sign of ω cancels). So the basis ambiguity
the brief worries about is absent already at the level of lines; what the known basis buys is COMPUTABILITY of
𝓡_E = Reg^{MT}(ω^{⊗2}) at every S. The Néron–Tate regulator is the archimedean member of the same family:
Reg_∞ : (∧²E(Q))^{⊗2} → R, ω^{⊗2} ↦ det⟨P_i,P_j⟩_{NT}.

**Tame height, explicit form used below (HEURISTIC normalisation, numerically validated).** For ℓ good, p | ℓ−1, and
Q = (a/d², b/d³) ∈ E(Q) with nonsingular reduction everywhere and Q ∈ E_1(Q_ℓ):  h_ℓ(Q) = class of a/b = t(Q)/d(Q) in
F_ℓ^×/±1 ⊗ Z/p (tame analogue of the MT p-adic height log_p(σ_p(t)/d); only the leading term t of σ_p survives the tame
character). In regime A (p ∤ n_ℓ = #E(F_ℓ)) it extends to E(Q) ⊗ Z/p by h_ℓ(P) = (c n_ℓ)^{-2} h_ℓ(c n_ℓ P), c = 4.

**Numerical probe of primitivity (P)** (`runs/tame_height_probe.gp`, `.out`; PARI 2.17.3, exact arithmetic, seconds):
quadraticity checks h(P1−P2), h(P1+2P2) against the bilinear form pass at EVERY (p,ℓ) tested ([0,0]), and

   p=5: ℓ=11 det 2 | ℓ=41 det 0 | ℓ=61 det 4 | ℓ=71 det 1          p=7: ℓ=29 det 1 | ℓ=43 det 5 | ℓ=71 det 5

(det = 4h(P1)h(P2) − B(P1,P2)² mod p.) So 𝓡_ℓ(ω) ≢ 0 mod p at six of seven pairs: (P) holds for the seed at p = 5, 7, and
the zero at (5,41) is the expected ≈1/p degeneracy rate. [This validates the FORM of the pairing, not MT's normalisation.]

**Lemma P (FORMULATED; believed provable by Chebotarev).** For every prime p ≥ 5 of good reduction with ρ̄_p surjective
and every k ≥ 1 there are infinitely many admissible ℓ ≡ 1 (p^k), p ∤ #E(F_ℓ), with det(h_ℓ|⟨P1,P2⟩) ≢ 0 mod p.
Proof design: x∪y = 0 in H²(G_{Q,Σ},μ_p) (Hasse + isotropy of Kummer images), so x∪y = dε with ε ∈ C¹(G_{Q,Σ},μ_p); then
h_ℓ(x,y) = [u_0(x,y)]_ℓ + c_ℓ(x,y), u_0 ∈ Q^× fixed (supported on Σ) and c_ℓ = ε(Fr_ℓ) − e((ρ̄(Fr_ℓ)−1)^{-1}x(Fr_ℓ), y(Fr_ℓ))
a class function on the Heisenberg-type extension cut out by (E[p], x, y, ε, μ_{p^k}, u_0^{1/p}). Surjectivity of
Fr ↦ (h(x,x),h(x,y),h(y,y)) ∈ F_p³ then follows from linear disjointness of the three central extensions. NOT YET PROVED;
it is a statement about P1, P2 only (no L-values, no Sha).

**Probe extended** (`runs/tame_height_probe2.gp/.out`): quadraticity passes everywhere; det ≢ 0 mod p at
p=11: ℓ=23,67,89 | p=13: ℓ=53,79,131 | p=17: ℓ=103,137 | p=23: ℓ=47,139 (10 of 10). With §4: 16 of 17 pairs primitive.
**Regime K makes Lemma P unnecessary for the main line:** for the multilinear (Kurihara) component at n = ℓ1ℓ2 with
Kolyvagin primes for p^k, primitivity is "det(loc_{ℓi}(P_j)) ∈ (Z/p^k)^×", which is the standard Chebotarev step of every
Kolyvagin argument (P1, P2 independent in E(Q)/p, ρ̄_p surjective) — PROVED technology, uniform in p ≥ 5, any k.

## 5. TEST 3 — BKS + known basis: everything collapses to ONE scalar per realisation — 05:50Z

Because ∧²(E(Q)/tors) = Z·ω, each rank-two comparison in print is a scalar identity once ω is fixed:

| realisation | proved structure (rank-one module) | the scalar | what is conjectural |
|---|---|---|---|
| Kato/Kolyvagin at p (F_can, core rank 1) | KS(T_pE) free of rank 1 (Mazur–Rubin); κ^{Kato} ∈ KS | m_p: κ^{Kato} = m_p·κ^{ω}, κ^{ω} the primitive system normalised on ω (§5.1) | nothing, if Sha[p^∞] finite; m_p := 0 otherwise (then κ_n = 0 for ν(n) ≤ 2) |
| tame Mazur–Tate at S | θ_S ∈ I_S² (Ota 1.2) | θ̃_S = m_S·𝓡_S(ω^{⊗2}) wherever 𝓡_S is primitive | that m_S is independent of S (= (L1)) and of p (= (L2)) |
| cyclotomic p-adic (ordinary p) | BKS24 Thm 1.9 (generalised Rubin formula, PROVED) | L_p^{(2)}/2 = ε_p·m_p^{cyc}·Reg_p(ω) | Reg_p ≠ 0 (Schneider) — NOT needed in the tame direction |
| anticyclotomic definite, K with rank E^K = 0 | θ_K = square-root element; Castella–Hsieh Cor 5.1 (PROVED): κ_{α,α^{-1}} = C·(θ̄_{f/K}/h^{(2)}(P1,P2))·(P1⊗log P2 − P2⊗log P1) | μ_{K,p} := θ̄_{f/K}/h^{(2)}(ω), LINEAR in ω | μ_{K,p} ∈ Q, p-independent |
| archimedean | — | q_∞ := L″(E,1)/(2Ω Reg_∞(ω^{⊗2})) | q_∞ ∈ Q (Wall 2) |

BKS Conj 1.1/1.6 (GPR) at p ⟺ m_p = ι_p(q_∞)·tors²/Tam·(explicit); MT Conj 2.4 ⟺ Sha finite and m_S = |Sha| for all S.
**Isolated scalar:** 𝔪_E := (m_p)_p ∈ ∏_{p≥5 good} Q_p. Known integrally: m_p ∈ Z_p (Ota integrality + primitivity), and
at good ordinary p the IMC (Kato + Skinner–Urban; holds for the seed, F3 row D3) gives v_p(m_p) = v_p(#Sha[p^∞]·Tam/tors²)
when Sha[p^∞] is finite. **No Fitting-ideal statement (Ota 1.5, Bullach–Honnor 1.4(b), Kim, Sakamoto) can see more than
v_p(m_p): ideals of Z_p are blind to units.** The unit part u_p = m_p/p^{v_p(m_p)} is the entire open content.

### 5.1 The ω-normalised primitive system and the log-free formula (DERIVED; assumes Sha[p^k] = 0 for the k in play)
Let n = ℓ1ℓ2 be core for F_can (Kolyvagin primes mod p^k, M_n := (loc_{ℓi}(P_j)) invertible mod p). Then
H¹_{F_can^n}(Q,T/p^k) = ⟨P1,P2,c_3⟩ with exp*_p(c_3) = 1, and the Stark system value is ε_n = a_n·P1∧P2∧c_3. Passing from
n to n′ = ℓ1ℓ2′ through n″ = ℓ1ℓ2ℓ2′ and using global reciprocity for the class c_4 (exp*(c_4) = 0, sing_{ℓ2′} = 1), Cramer's
rule gives sing_{ℓ2}(c_4) = −det M_{n′}/det M_n, hence a_{n′}·det M_{n′} = ∓ a_n·det M_{n′}²/det M_n, i.e.

      δ_n = exp*_p(κ_n) = (const independent of n) · det(M_n)²   — no p-adic logarithm survives.

This is exactly the shape of MT's prediction (|Sha|·J_n·cross term of tame heights; at Kolyvagin primes the tame height is
the Tate–Lichtenbaum pairing, which identifies (E(F_ℓ)/p^k)^{⊗2} with G_ℓ ⊗ Z/p^k). So (L1) on the multilinear components in
regime K is Kolyvagin-system rigidity, not a new conjecture. [NEEDS REFEREE: signs, the identification with MT (3.1), and
the case Sha[p^k] ≠ 0, where det(M_n)² must be replaced by the Fitting-type minor of Kim's structure theorem.]

## 6. ARCHITECTURE — the object Z_E, the statement LINE, and the conditional theorem — 06:05Z

### 6.1 Object
   Z_E := m · ω^{⊗2}  ∈ (∧²E(Q))^{⊗2} ⊗ Q  ≅ Q        (coefficient ring: Q, in fact R = Z[1/6N] by 6.3(a))
defined by the requirement Reg^{MT}(Z_E) = θ̃_E in 𝓜 (on multilinear components: δ_n^{univ} = m·𝓡_n^{mult}(ω^{⊗2}) for all
admissible n = ℓ1ℓ2). Existence of Z_E is the statement

   **LINE.** There are coprime a, b ∈ Z∖{0} with  b·δ_n^{univ} = a·𝓡_n^{mult}(ω^{⊗2})  in (G_{ℓ1}⊗G_{ℓ2}) ⊗ R  for every admissible n = ℓ1ℓ2.

(Full form: b·θ̃_S = a·𝓡_S(ω^{⊗2}) for all admissible S.) Uniqueness of m = a/b follows from 6.3(b).
MT Conj 2.4 ⇒ LINE with m = |Sha|. Rationality part of MTT p-adic BSD + direction-independence of m_p ⇒ LINE.
LINE asserts NO finiteness of Sha, NO value of m, NO archimedean statement: it is strictly weaker than MT and than BKS 1.1.

### 6.2 Realisations
- real_{p,n}(Z_E) := Reg^{MT}_n(Z_E) ⊗ Z/p^k = δ_n ⊗ Z/p^k  → feeds Ota Thm 1.5 / Kim–Pollack Thm 1.1 / Kim Thm 1.8 (PROVED machines).
- real_∞(Z_E) := Reg_∞(Z_E) = m·det⟨P_i,P_j⟩_{NT}.  NO theorem or mechanism identifies this with L″(E,1)/(2Ω)·tors²/Tam.
- anticyclotomic linear variant (K imaginary quadratic, rank E^K = 0, definite setting): Z_E^{(K)} := μ_K·ω ∈ ∧²E(Q) ⊗ Q,
  LINEAR in ω because the second derived height is alternating on E(K)^+ = E(Q); p-adic realisation PROVED in the form
  κ_{α,α^{-1}} = C·μ_{K,p}·(P1⊗log P2 − P2⊗log P1), μ_{K,p} = θ̄_{f/K}/h^{(2)}(P1,P2) (Castella–Hsieh Cor 5.1, F4 row C1).
  Expected μ_K² = m·(L(E^K,1)-side constants): Z_E^{(K)} is the "square root" object, predicted ±6·ω·(K-constants) for the seed
  (√(#Sha·Tam/tors²) = 3·2). HEURISTIC; recorded because it is the literal shape "Z_E = m·(P1∧P2)" asked for in the brief.

### 6.3 Conditional theorem (DERIVED — needs a referee; inputs listed)
**Theorem C.** Assume LINE and the normalisation fact (N): for n core at p^k (Kolyvagin primes mod p^k, M_n = (loc_{ℓi}P_j)
invertible), 𝓡_n^{mult}(ω^{⊗2}) ⊗ Z/p^k = u·det(M_n)²·(g_1⊗g_2), u a unit. Let p ≥ 5 be any prime with p ∤ N. Then
 (a) p ∤ b;  (b) Sha(E/Q)[p^∞] is finite;  (c) if p ∤ a then Sha(E/Q)[p^∞] = 0.
Hence Supp(Sha) ⊂ {p | a} ∪ {2,3} ∪ {p | N}: Wall 1, with an explicit exceptional set.
Proof. Chebotarev (P1,P2 independent in E(Q)/p, ρ̄_p surjective) gives, for every k, a core n at p^k. (a) if p | b then
a·det(M_n)² ≡ 0 mod p, absurd. (c) δ_n ≡ (a/b)u·det² ≢ 0 mod p, so θ̃_n ≢ 0 mod p·gr² and Ota Thm 1.5 gives Sha[p] = 0
(equivalently Kim–Pollack 2505.09121 Thm 1.1). (b) If Sha[p^∞] were infinite, the p-parity theorem gives
corank Sel_{p^∞} ≥ 4, and Ota's (1.2) gives θ_S ∈ Z_p ⊗ I_S^{min(3,p)} = Z_p ⊗ I_S³ for every admissible S, so δ_n ⊗ Z_p = 0
for all n; with n core at p^k this forces p^k | a for every k, so a = 0. ∎
Inputs: Ota (1.2) and Thm 1.5 (unconditional; every p ≥ 5, p ∤ N is non-invertible in R for the seed, F3 row 0);
p-parity (Dokchitser–Dokchitser / Kim / Nekovář); Chebotarev; (N) (a Tate–Lichtenbaum computation about P1,P2 only, §5.1 —
NOT yet checked against MT (3.1)). Not used: IMC, ordinarity, finiteness of Sha, BSD, BKS, Schneider.

### 6.4 What information about m is needed (brief, item (A))
- For Wall 1: m ∈ Q^× only. Integrality at good p ≥ 5 is automatic (6.3(a)). The ideal (a) bounds Supp(Sha).
- With the IMC at good ordinary p (known for the seed): v_p(m) = v_p(#Sha[p^∞]) — the ideal (m) IS the good-ordinary part of #Sha.
- The unit parts of m (sign, 2- and 3-parts) matter only for comparison with q_∞, i.e. for Wall 2.

### 6.5 Decomposition of LINE and what is actually open
 (L1) local line at p: θ̃_{E,p} ∈ Z_p·𝓡_{E,p}. On multilinear components in regime K this is Kolyvagin-system rigidity (§5.1);
      it DEFINES m_p ∈ Z_p unconditionally, in the tame direction, with no appeal to Schneider's conjecture. ATTACKABLE NOW.
 (L2) (m_p)_p ∈ ∏ Z_p is a rational number. THE MISSING COMPATIBILITY. It has no finite-level content beyond (L1): for any
      finite set of primes CRT supplies an integer, so (L2) can only be proved by producing m globally. Known global sources:
      |Sha| (needs FIN: circular), q_∞ (needs an archimedean reciprocity law = BKS 1.6), an index of a geometric class in
      ∧²E(Q) (does not exist over Q, §7).
 Weaker-looking variants are NOT weaker: "∃ x ≠ 0 with v_p(m_p) ≤ v_p(x) ∀p" is equivalent to FIN + (L1) (take x = #Sha·Tam).

### 6.6 Both walls at once
LINE never touches L″. The smallest statement found that hits BOTH walls is BKS Conj 1.6 (GPR) for almost all p WITH its
complex scalar: it gives q_∞ ∈ Q (F4 CP-1), LINE with m = q_∞·tors²/Tam, hence FIN at good p ≥ 5 by Theorem C, hence the
hypotheses of BKS24 Thm 1.14 one prime at a time. Intermediate: LINE + GPR at ONE prime p_0 ⇒ q_∞ = m·Tam/tors² EXACTLY
(rational with known value), i.e. FORMULA up to the identification m ↔ #Sha at the finitely many p | 6N·a.
So: FULL BSD(seed) ⟸ LINE ∧ GPR(p_0 = 5) ∧ finite per-prime work at p | 6N·a.   [new reduction; both inputs open]

### 6.7 Falsifiable numerical consequences (proposed, NOT run; each needs modular symbols of denominator ℓ at N ≈ 6.5e15)
 T-a (normalisation-free, tests (L1)): at p = 5 the ratio θ̃_ℓ/(n_ℓ·det h_ℓ) mod 5 must agree at ℓ = 11, 61, 71 (det values 2, 4, 1 in §4).
 T-b (tests direction independence at p = 5): tame ratio at ℓ = 11 versus the completed cyclotomic L_5 run (a_2 ≡ 2, Reg_γ ≡ 21 mod 25).
 T-c (tests (L2), needs ≥ 4 primes): residues of m at p = 5, 7, 11, 13 (ℓ = 11, 29, 23, 53) must all be of the form ±9·2^j for ONE j
      (2-power = unknown Manin/period normalisation): 26 admissible tuples out of 2880. A failure KILLS LINE (and MT) on the seed;
      a pass is the first cross-prime sighting of Sha[3] ≅ (Z/3)² from outside p = 3.

## 7. TEST 5 — plectic / function-field design, extracted formally (no theorem imported) — 06:15Z

| design element | function field (Yun–Zhang) | what Q has | status over Q |
|---|---|---|---|
| base of the two legs | X × X over F_q, with partial Frobenii | no Spec Z ×_{F_1} Spec Z | ABSENT — this is the one property with no analogue |
| category of the object | H_c^{2}(Sht², ·)_π ⊃ H¹(X,V_π) ⊗ H¹(X,V_π) by Künneth over F_q: ∧²/Sym² of H¹ IS an H² of a space | ∧²H¹_f(Q,V) is an exterior power of an Ext-group, not a cohomology group of any motive over Q; zero-cycles on E×E land in T(E×E)(Q), conjecturally torsion | ABSENT integrally |
| the two-leg object | Heegner–Drinfeld cycle, a Z-coefficient class | Kolyvagin derivatives of Beilinson–Kato elements: classes in motivic cohomology with FINITE coefficients Z/g_n, all p | g_n at once | PRESENT with Ẑ-coefficients only |
| realisations | ℓ-adic cycle class; intersection pairing = "height"; L^{(r)} via relative trace formula | étale at each p (Kato); Betti (modular symbols → θ_S); NO archimedean realisation at s = 1 (Beilinson's regulator of BK sees L(E,2)) | tame/p-adic PRESENT, archimedean ABSENT |
| output | one scalar identity L^{(r)} = ⟨Z,Z⟩ (YZ do not relate Z to ∧^r MW either) | one scalar m with θ̃_S = m·𝓡_S | = LINE |

**Exact categorical obstruction (DERIVED).** Everything rank-two that exists over Q has coefficients in a product of finite
rings (𝓜, motivic cohomology mod g_n). Integral (Z- or Q-coefficient) rank-two classes require ∧²H¹ to be realised as a
cohomology group receiving cycle classes; over F_q this is Künneth on X², over Q nothing plays the role of X².
**Weaker substitute sufficient for THIS seed.** Because ∧²E(Q) has rank one, no class is needed — only the scalar. The
function-field output is also only a scalar. So the substitute object is Z_E = m·ω^{⊗2} (or √m·ω, §6.2), whose existence is
LINE: "the Ẑ-coefficient object is the reduction of a Q-coefficient one". The seed's simplification is real but it removes
the GEOMETRY of the object, not the RATIONALITY problem.

## 8. TEST 6 — determinant / Fitting route without an element — 06:20Z

**Formal obstruction (DERIVED, elementary, exact).** Let L = Q·e be a Q-line and Λ_p ⊂ L ⊗ Q_p a Z_p-lattice for each p.
(Λ_p)_p comes from a Z-lattice D ⊂ L iff Λ_p = Z_p·e for almost all p, and then D = ∩_p(Λ_p ∩ L); if Λ_p ≠ Z_p e for
infinitely many p with v_p → the intersection is 0 or non-finitely-generated. Apply to L = (∧²E(Q))^{⊗−2} ⊗ Q·(period basis),
e the basis given by ω, Λ_p = p-adic determinant lattice of the Selmer complex (defined when Sha[p^∞] is finite) = m_p^{±1}Z_p e:
   D_E := ∩_p (Λ_p ∩ L)  is a p-independent submodule of Q, defined with no choice, and   D_E ≠ 0 finitely generated ⟺ FIN.
So a p-independent Fitting/determinant ideal EXISTS iff Wall 1 holds: the route is a restatement. An ideal carries only
the valuations (v_p(m_p))_p; to know they vanish for almost all p one must exhibit a non-zero ELEMENT of D_E — a rational
number x with v_p(x) ≥ v_p(m_p) for all p. In rank 0 that element is L(E,1)/Ω (Kato), in rank 1 the Heegner index
(Kolyvagin); in rank 2 it is the m of LINE. **One cannot avoid constructing an element.**
ETNC reading: zeta element = q_∞·e via the archimedean period-regulator isomorphism; FORMULA ∧ FIN ⟺ q_∞·e generates every Λ_p.
Compatibility (D) of the brief ⟺ "the generator m·e found on the tame side equals q_∞·e" ⟺ BSD formula. Nothing weaker.
Verdict for TEST 6 alone: NO_COMPOSITION_WITH_EXACT_OBSTRUCTION (the obstruction is the lattice lemma above).

## 9. Positioning against the closest printed statement (BKS II, arXiv:2103.11535, local txt l. 228–420, 796–907) — 06:30Z

Read in the primary text (semantic novelty check, not grep):
- Hyp 2.2(iii): p ∤ 6mN·#tors·Tam·∏_{ℓ|pmN}#E^{ns}(F_ℓ) — BKS II works exactly in my REGIME A, where Conj 2.3 simplifies to
  θ_{F,S} = (−1)^{ν(m)}·L^{alg}_S·R_F in I^r/I^{r+1}, R_F = det⟨x_i,x_j⟩_F. My det(h_ℓ) of §4 is R_F for F ⊂ Q(μ_ℓ) of degree p.
- (17): η^{alg} := L^{alg}_Σ·(x ⊗ ε_Σ(x)), x a basis of ∧^r E(Q)_{tf}, "independent of the choice of x" — this IS ω^{⊗2} of §4.
- Def 4.3: the p-adic determinantal zeta element z_Q ∈ det^{-1}_{Z_p}RΓ(Z_Σ,T); iso (16) with ∧^rH¹ ⊗ ∧^{r−1}H^{2,*}_{tf}.
- **Thm 4.6 (PROVED): z_Q = η^{alg} ⇒ Conj 2.3.** Prop 4.4: algebraic GPR (Conj 3.4) ⇒ z_Q = η^{alg}. §2.1 assumes Sha(E/Q) finite.

Consequences for this lane:
1. (L1) is the LINEARISED Thm 4.6: when Sha[p^∞] is finite the target of (16) ⊗ Q_p is the LINE Q_p·(ω ⊗ ε_Σ(ω)), so
   z_Q = m_p·Eul_Σ·(ω ⊗ ε_Σ(ω)) for a unique m_p ∈ Q_p with no conjecture at all, and the proof of Thm 4.6 (image of z_Q under
   the Darmon-norm/Bockstein diagram; l. 1230–1237) is linear in the scalar. Hence θ_{F,S} = (−1)^{ν(m)} m_p·Eul·R_F for all F in
   regime A. [NEEDS REFEREE: that the printed proof uses L^{alg} only through linearity.] If Sha[p^∞] is infinite, Ota's (1.2)
   gives θ̃ = 0 and m_p := 0. So (L1) is a theorem-level statement; m_p is DEFINED for every good p ≥ 5 with surjective image.
2. **LINE ⟺ "rational zeta element" (RZ): ∃ ζ = m·ω^{⊗2} ∈ (∧²E(Q))^{⊗2} ⊗ Q with z_Q^{(p)} = ι_p(ζ)·Eul_Σ for all good p ≥ 5.**
   BKS II Conj 3.4 for all p ⟺ RZ with m = L^{alg} AND Sha finite. RZ drops both. This is the precise sense of "strictly weaker".
3. What is NOT in BKS I/II: Theorem C (RZ with m ≠ 0 ⇒ Sha[p^∞] finite at every good p ≥ 5 and zero for p ∤ m). They cannot
   state it because finiteness is assumed in §2.1 before η^{alg} exists. The implication uses Ota's UNCONDITIONAL extra vanishing
   (corank ≥ 4 ⇒ θ_S ∈ I³) against primitivity of the regulator family — a composition Ota + BKS II that I did not find in F3/F4
   or in either paper. [Novelty claim is semantic but same-session; flag for an independent check.]

## 10. HOSTILE SELF-CHECK (the brief's eight questions, applied to Z_E / LINE / Theorem C) — 06:35Z

1. Secretly chooses p?  NO for the object (Θ_E, θ̃_E, 𝓡_E, m are p-free). YES by design for the realisation maps. But the
   EXISTENCE of Z_E is LINE, an all-p statement: the object is conjectural, only its would-be realisations are proved.
2. Secretly assumes Sha finite?  Theorem C: NO (inputs listed in 6.3). §5.1 and §9.1 assume Sha[p^k] = 0 / Sha[p^∞] finite, but
   they only MOTIVATE (L1); Theorem C uses LINE in its tame form, which is stated without Selmer groups. Caveat: LINE with
   m ≠ 0 IMPLIES finiteness at good p, so LINE is at least as deep as FIN there. It is a mechanism, not a free lemma.
3. Secretly assumes BSD or BKS?  NO. MT 2.4 ⇒ LINE, BKS II 3.4(∀p) ⇒ LINE; neither converse is used.
4. Does S depend on p?  The family runs over ALL admissible S; S(p) is chosen only inside real_{p,S}. Same as TEST 1.
5. Does the archimedean map involve L″?  **NO — this is the failure.** real_∞(Z_E) = m·Reg_NT; nothing relates m to q_∞ except
   the BSD formula itself or BKS 1.6 with its complex scalar. LINE does not touch Wall 2. (D) of the brief is NOT achieved.
6. Genuine rank two?  YES: primitive double zero; core rank 1 with Selmer rank 2; θ_S ∈ I² by Ota, not a product of two
   rank-one factors. The anticyclotomic variant is (2,0)-type over K (L(E^K,1) ≠ 0), not (1,1).
7. Exists over Q?  Θ_E, θ̃_E, 𝓡_E, m_p: YES, unconditionally. Z_E: iff LINE. No function-field input is used anywhere.
8. Coefficient ring integral enough?  Q (in fact Z[1/6N]) for Z_E: YES, that is the whole point of LINE. 𝓜 (where the proved
   objects live): NO — product of finite groups; §2 proves no quotient of it can be.
Kill attempts that did NOT kill: (i) MT normalisation mismatch under S ↦ Sℓ — resolved by the alternating divisor sum (§1);
(ii) "regulator side might depend on log_p" — it does not (§5.1); (iii) "(P) might fail" — 16/17 numerically, and regime K
needs only standard Chebotarev. Kill attempts that DID cut scope: BOUND and D_E are restatements of FIN (§6.5, §8); (L2) has
no finite-level content, so no finite computation can prove LINE — T-a…T-c can only refute it or make it plausible.

## 11. VERDICT (this lane) — ONE_MISSING_COMPATIBILITY, scoped to WALL 1
Everything composes — universal MT object (§2–3), canonical regulator map from (∧²E(Q))^{⊗2} (§4), per-p rigidity defining
m_p (§5, §9), proved per-p machines (Ota/Kim), conditional Theorem C (§6.3) — EXCEPT the single statement (L2):
(m_p)_p is one rational number. Wall 2 is untouched; the only statement found that hits both walls is BKS 1.6 for almost
all p with its complex scalar (§6.6). TEST 6 alone: NO_COMPOSITION_WITH_EXACT_OBSTRUCTION (lattice lemma, §8).

### 9.1 Linearity CONFIRMED in the primary text (BKS II l. 1230–1270) — 06:40Z
ψ_Q : det^{-1}_{Z_p}RΓ(Z_Σ,T) ⊗ Q_p ≅ Q_p ⊗_Z (∧^rE(Q) ⊗_Z ∧^rE(Q)), ψ_Q(η^{alg}) = L^{alg}_Σ·(x⊗x) (26); Lemma 5.5:
(Reg_F ∘ π_{Q,f} ∘ φ_Q)(η^{alg}) = (−1)^{ν(m)} L^{alg}_S·R_F, and ψ_Q = (−1)^{ν(m)}(#E(F_p)/p)(π_{Q,f}∘φ_Q). All maps are Z_p-linear on a
rank-one module, so for ANY z with ψ_Q(z) = λ·Eul_Σ·(x⊗x) the image is (−1)^{ν(m)}λ·Eul_S·R_F. Therefore
      **m_p := ψ_Q(z_Q^{(p)}) / (Eul_Σ · ω^{⊗2}) ∈ Q_p**
is defined with no conjecture (Sha[p^∞] finite), the p-adic determinant line IS Q_p ⊗ (∧²E(Q))^{⊗2}, and
   Z_E ∈ (∧²E(Q))^{⊗2} ⊗ Q  with  ψ_Q(z_Q^{(p)}) = Eul_Σ·ι_p(Z_E) for every good p ≥ 5      ( = RZ = LINE )
is the exact characteristic-zero object the brief asks for. [Still to referee: that θ_{F,S} = (Reg_F∘π_{Q,f}∘φ_Q)(z_Q) is
proved in BKS II §5 without using Conj 3.4 — Prop 5.1/5.4 read only at the level of their statements.]
