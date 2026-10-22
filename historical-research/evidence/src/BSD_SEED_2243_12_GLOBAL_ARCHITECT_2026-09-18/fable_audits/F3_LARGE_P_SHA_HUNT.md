# F3 — Large-p Sha hunt for the seed (2243, 12): literature-first attempt to REFUTE "no known theorem"

Session: Fable 5.1, fresh context, 2026-09-18. Read-only outside this file and `F3_work/`. Nothing merged. No computations on the seed.

**Label under attack (DAG node G23):**
"No known theorem proves Sha(E/Q)[p] = 0 for all sufficiently large p for this analytic-rank-2 seed."

**Seed.** E : y² = x³ − 22735x² + 106272484x; N = 2³·3·2243·4547²·5843 (not semistable); rank = r_an = 2, w = +1;
E(Q) = Z/2 × Z²; mod-ℓ image GL₂(F_ℓ) for every odd ℓ; Sha[2^∞] = Sha[5^∞] = 0; Sha_an = 9.

> **STATUS: FINAL (checkpoint 4, 2026-09-18 ~21:10 PDT).** The session hit its usage limit once mid-run; all five search agents
> were killed by it, but their append-only findings files survived and were integrated from disk. Working state:
> `F3_work/RESUME.md`, `F3_work/STATE.json`, `F3_work/QUERY_LOG.md`; per-cluster findings with their own query logs in
> `F3_work/agents/*.md`.

## 0. Verdict

# NOT_FOUND

No published theorem or credible preprint (searched to 18 Sep 2026) was found that implies, for this E, any of
A (Sha[p] = 0 for p > explicit p₀), B (all but finitely many p), C (Sha finite), D (a finite computation certifying A/B/C) or
E (a p-uniform rank-2 Euler-system/Kolyvagin bound). 61 candidate blocks were written by the five cluster agents (A 12, B 13, C 13, D 10, E 13), most from PDF/HTML full text at
the statement level and a marked minority at abstract level, plus the coordinator's own source checks (§5, §6). **"Not found" is not "impossible".**

**What the hostile hunt DID change** (none of it refutes the label; all of it should replace vaguer wording in the DAG):

1. **The strongest near miss is not in the DAG: Ota, Amer. J. Math. 140 (2018), Thm 1.5/6.4** (row 0) — an UNCONDITIONAL theorem, in
   ARBITRARY rank, with a **p-independent input** (the Mazur–Tate element θ_S ∈ R[G_S]) and the exact conclusion we want
   (Sha(E/Q)[p] = 0), with no Sha-finiteness, no BSD, no IMC, no ordinarity. Its Heegner twin is Darmon, Invent. 1992, Prop 5.9
   (row 0′); its 2025 Fitting-ideal form is Bullach–Honnor arXiv:2511.07203 Thm 1.4(b) (row 0″). All three fail uniformity for ONE
   and the same reason: the leading coefficient lives in I^r/I^{r+1} of a FINITE group, which only sees the primes dividing the
   group order, so every ℓ ∣ S must be ≡ ±1 mod p. One S serves finitely many p.
2. **The label can be sharpened to an exact open statement** (§4): at every good p ≥ 5 the seed satisfies Kolyvagin's conjecture
   (W. Zhang; Sweeting for supersingular p; BCGS) and, at every good ORDINARY p > 3, the refined Kurihara conjecture M_∞(δ) = 0 (Castella–Sano) — so
   G23 ⟺ "for all p > p₀ the first non-zero level of the derived system is 1 (Heegner) / 2 (Kato) and is a p-unit there".
3. **The only genuinely horizontal theorem in rank ≥ 2** is Coates–Liang–Sujatha's corank bound t_p ≤ (½+ε)p − g (row D1):
   CM only, and a growing bound. Its mechanism (non-zero algebraic L-value in the convergent range + product formula) has no
   non-CM analogue in print.
4. **As of 8 Sep 2026 the question is posed in print as OPEN** even for CM curves: Banwait §1.5 Q3 asks whether "a fixed algebraic
   number" controls the exceptional primes — the rank-2 analogue of the Heegner point. Same paper, Q1: the per-p UNIT criterion
   is heuristically expected to fail for infinitely many p, so no per-p unit criterion can be uniformised verbatim.
5. **A by-product per-prime route** (§4b, UNVERIFIED cost): Ota's theorem certifies Sha[p] = 0 at supersingular p from modular
   symbols of denominator ℓ ≈ 2p — possibly moving G19 (23, 29) from ROUTE_BLOCKED to FINITE_CERTIFICATE_CANDIDATE.

## 1. What a refutation would have to look like (the test every candidate is put to)

For this E and odd p, E(Q)[p] = 0 and E(Q)/p = ⟨P₁, P₂⟩, so

    Sha(E/Q)[p] = 0  ⟺  dim_{F_p} Sel_p(E/Q) = 2.

A theorem refutes the label only if it yields this for ALL p outside an explicit (or effectively computable) finite set, from
hypotheses that are either already proved for the seed or checkable by a finite computation. The two classical uniform-in-p
theorems show the required shape:

| analytic rank | global, p-independent object | theorem | why it is uniform in p |
|---|---|---|---|
| 0 | the rational number L(E,1)/Ω_E | Kato 2004 (+ Rubin for CM) | for p ∤ 6N with surjective ρ̄_p, #Sha[p^∞] divides (a fixed multiple of) L(E,1)/Ω_E; one number serves every p |
| 1 | the Heegner point y_K ∈ E(K), index I_K = [E(K) : Z y_K] | Kolyvagin 1990 (explicit forms: Cha 2005, Grigorov et al. 2009, Jetchev 2008) | ord_p #Sha ≤ 2 ord_p I_K for every admissible p; one point serves every p |
| 2 | **none known** | **none known** | every rank-2 method below needs auxiliary primes chosen RELATIVE TO p (ℓ ≡ ±1 mod p with a_ℓ ≡ ±(ℓ+1) mod p), or a p-adic L-function at p |

So each candidate is asked: (Q1) does it have a p-independent global input in analytic rank 2? (Q2) is the implication
"input is a p-unit ⇒ Sel_p is 2-dimensional" PROVED without assuming Sha[p^∞] finite or BSD? (Q3) do the hypotheses hold for
the seed (non-semistable N, additive primes 2 and 4547, rational 2-torsion)?

## 2. Near-miss table (strongest first)

Columns: theorem / source+status / hypotheses vs seed / uniform or per-p / EXACT MISSING STATEMENT.

| # | candidate | source, status | seed hypotheses | p-uniform? | exact missing statement |
|---|---|---|---|---|---|
| 0 | **STRONGEST NEAR MISS — Mazur–Tate leading coefficient ⇒ Sha[p] = 0, unconditionally, in ARBITRARY rank.** θ_S ∈ R[G_S] (G_S = Gal(Q(μ_S)/Q)) is the Mazur–Tate element built from modular symbols — a **p-independent** element of a rational group ring. Thm 1.2: θ_S ∈ I_S^{r_E}. **Thm 1.5:** p not invertible in R, S a squarefree product of good primes ℓ with ℓ ≡ 1 (mod p) and E(F_ℓ)[p] cyclic; if the image θ̃_S of θ_S in I_S^{r_E}/I_S^{r_E+1} is ≢ 0 mod p, then **Sha(E/Q)[p] = 0** and p ∤ J_S (J_S = #coker(E(Q) → ⊕_{ℓ∣S}E(F_ℓ) ⊕ ⊕_{ℓ∣N}E(Q_ℓ)/E₀(Q_ℓ))). (Thm 6.4 is the general form.) | K. Ota, arXiv:1509.00682v1; Amer. J. Math. 140 (2018) 495–542. **Published, unconditional**: no Sha-finiteness, no BSD, no IMC, no ordinarity [agent B; **coord verified Thm 1.2, Rem 1.3, Thm 1.5 on PDF pp. 2–3**] | E non-CM ✓. R inverts p with p ∣ 6N·#E(F_p)·∏[E(Q_ℓ):E₀(Q_ℓ)], p with non-surjective p-adic image, p < r_E. For the seed EVERY p ≥ 5 with p ∤ N qualifies — **including the supersingular primes** (p-adic image surjective since mod-p is and p ≥ 5; Tam = 16; non-anomalous is automatic: #E(F_p) is even (rational 2-torsion), so p ∣ #E(F_p) forces 2p ≤ p + 1 + 2√p, i.e. p ≤ 5, and #E(F₅) = 8; cf. Ota Rem 1.3(4)) | the THEOREM is uniform (one statement, all p ≥ 5, explicit exceptional set) but its INPUT is not: I_S^{r}/I_S^{r+1} is a finite group supported on the primes dividing ∏_{ℓ∣S}(ℓ − 1), and Thm 1.5 needs every ℓ ∣ S ≡ 1 mod p. One S serves only the finitely many p dividing gcd_{ℓ∣S}(ℓ − 1) | **Missing: for all p > p₀ some S = S(p) with θ̃_S ≢ 0 mod p.** For S = ℓ prime this says the second-order coefficient Σ_a [a/ℓ]⁺·C(log_g a, 2) ∈ Z/(ℓ−1) is a p-unit. Predicted by the Mazur–Tate leading-term conjecture (θ̃_S = #Sha · J-type factors · disc of the G_S-valued height), i.e. it is an OUTPUT of a BSD-type conjecture, not an available input. No theorem gives mod-p non-vanishing of such sums for all large p |
| 1 | **Kolyvagin's conjecture + Kolyvagin's structure theorem.** κ^Heeg ≠ 0 and M_∞ = 0; then corank Sel_{p^∞}(E/K)^{ε} = ν_p + 1, other eigenspace ≤ ν_p; Sha/div from the indices M_i | W. Zhang, Cambridge J. Math. 2 (2014) Thm 1.1/1.2/11.2, published [agent A, journal PDF]; Sweeting arXiv:2012.11771v3 (non-ordinary p); BCGS arXiv:2312.09301v2 (to appear CJM) | **ALL satisfied** at every good ordinary p ≥ 5: ρ̄ surjective; Ram(ρ̄) = {3, 2243, 5843} for every p ≥ 5; Hypothesis ♠ puts no condition at additive primes (N⁺ may be non-squarefree). Sweeting's App. A adds the supersingular p ≥ 5 | **per-p** (Kolyvagin primes: ℓ inert in K, p ∣ ℓ+1, p ∣ a_ℓ; level raising mod p; IMC at p) | With K such that r_an(E^K) = 1: Sha(E/Q)[p^∞] finite ⟺ ν_p = 1 ⟺ some ONE-prime derived class κ_ℓ ≠ 0. **Missing: "ν_p = 1 for all p > p₀"** (and, for Sha[p] = 0, "some κ_ℓ ≢ 0 mod p"). The theorems prove ν_p < ∞, never ν_p = 1. One ℓ serves only the p dividing gcd(ℓ+1, a_ℓ) |
| 2 | **Kurihara numbers.** ord(δ) = corank Sel_{p^∞}(E/Q); ord_p #(Sel/div) = M_ρ − M_∞; M_∞ = ord_p Tam ⟺ IMC | Kim arXiv:2203.12159v6 Thm 1.8/1.10 (preprint); Castella–Sano arXiv:2601.14504 Thm A/B (preprint, Jan 2026) [coord, local texts] | satisfied at every good ordinary p > 3: (sur), p ∤ c_φ (c_φ is a power of 2), p ∤ Tam = 16 ⇒ M_∞ = 0. Supersingular case of Thm B needs N squarefree — seed fails | **per-p** (Kolyvagin primes ℓ ≡ 1 mod p, a_ℓ ≡ ℓ+1 mod p) | Sha[p] = 0 ⟺ ∃ n = ℓ₁ℓ₂ with δ_n ≢ 0 mod p. **Missing: a theorem giving such a witness for all p > p₀** (e.g. mod-p non-vanishing of a weighted sum of modular symbols of level ≈ p²). One n serves only finitely many p. Exact bookkeeping, not leverage (= memory Proposition K) |
| 3 | **Heegner points detect finiteness in arbitrary rank.** Sha(E/Q)[p^∞] finite ⟺ derived Heegner points P_n (ν(n) = r_p⁺ − 1) lie in p^∂(E(Q) + p^k E(K[n])) | Kim arXiv:2609.15328v1 (14 Sep 2026), Thm 1.1, 4.7; preprint [coord + agent A] | ordinary case applies; supersingular case needs SEMISTABLE E — seed fails (use Sweeting instead) | **per-p**; K = K(E,p); author poses the needed principle as open Question 4.6 | an equivalence, not a bound. **Missing: any principle forcing the membership for all large p.** Thm 1.7 (quantified over all p) is a splitting-field statement, wrong direction, semistable only |
| 4 | **Generalized Perrin-Riou conjecture / derivatives of Kato's Euler system.** z_F's leading term = Boc(η^BSD); with IMC ⇒ p-part of BSD in any rank | Burns–Kurihara–Sano, J. Math. Soc. Japan 76 (2024): Conj 1.1, Thm 1.3, Thm 1.14; published [coord, local text] | — | would be uniform IF proved for all p (η^BSD = (L^{(r)}(E,1)/(Ω⁺R_∞))·P₁∧P₂ is a p-independent class) | **Conjectural, and finiteness is an INPUT**: Hyp 2.2(iii) "Sha[p^∞] finite"; Thm 1.3(b); Thm 1.14 bullet 1 "Sha finite". Missing: Conj 1.1(iii) for r = 2 at almost all p WITHOUT Hyp 2.2(iii), plus rationality of L″/(Ω R) |
| 5 | **Per-p p-adic BSD via IMC + Kato.** ord_T L_p = 2 and unit leading term ⇒ Sha[p^∞] = 0 | Stein–Wuthrich, Math. Comp. 82 (2013) Thm 6.1, Thm 1.1, **Thm 12.3** (389a1: Sha[p] = 0 for 2 and all 5,005 good ordinary p < 48,859 except 16,231); Skinner–Urban 2014; Skinner 2016; published [coord, local text] | applies at every good ordinary p ≥ 5 (SU with q = 2243) and at 3, 2243, 5843 (Skinner Thm A) | **per-p** (one L_p computation per prime; "several weeks CPU" for 389a1) | **Missing: a rank-2 p-adic Gross–Zagier-type formula** expressing the leading coefficient of L_p through a p-independent algebraic number (in rank 1: Perrin-Riou/Kobayashi). Also open: Schneider's conjecture (Reg_p ≠ 0), let alone Reg_p a unit for all large p |
| 6 | **Rank-two CM criterion.** second Taylor coefficient of L_p unit ⟺ Reg_p unit and Sha[p^∞] = 0 | Banwait arXiv:2609.08431 (8 Sep 2026), preprint [Lane 3 + coord search] | CM only — seed is non-CM | per-p; §1.1 states the horizontal statement is open for every rank ≥ 2 curve | asks, does not answer, whether one of two criteria succeeds for all but finitely many split p |
| 7 | **Horizontal corank bounds for CM curves** (at most ≈ p/2, resp. 2p − g copies of Q_p/Z_p) | Coates–Liang–Sujatha, Milan J. Math. 2010; arXiv:0901.3832; published [Lane 3] | CM only | uniform, but a GROWING bound | not a vanishing statement; CM only |
| 8 | **Kolyvagin's conjecture verified on rank-2 curves** (389a1, 709a1, 718b1 at p = 3, K = Q(√−7), ℓ = 5) | Jetchev–Lauter–Stein, JNT 129 (2009) Prop 3.10 (numerical, "not provably correct" per Rem 2.2) [agent A]; Stein 2011 preprint (algebraic algorithm) [coord] | method applies to the seed for one p at a time; infeasible at N ≈ 10^15.4 | per (E, p, K, ℓ) | one ℓ serves only p ∣ gcd(ℓ+1, a_ℓ) |
| 9 | **Higher-rank Gross–Zagier conjecture** (subgroups W_p ⊂ E(K), index c·∏c_q·√Sha_an) | Stein, IMRN 2011 [coord, PDF pp.1–3] | — | p-independent SHAPE | **conjectural and conditional on BSD** + a refined Kolyvagin conjecture |
| 10 | **Generalized Kato classes** κ_p ≠ 0 ⟺ Sel 2-dimensional (rank 2) | Castella–Hsieh, Forum Math. Sigma 10 (2022); Castella Thm A; Darmon–Rotger 2016 (conjecture) [Lane 1; agent C — details in §2c rows C1–C5] | — | per-p (weight-one specialisation of Hida families at p) | an equivalence per p; the direction that PROVES κ_p ≠ 0 assumes Sha[p^∞] finite; conclusions are rational (finiteness), never Sha[p] = 0 |
| 11 | **"Sha[ℓ] = 0 for all ℓ ∉ {2,3,5,7,13} with surjective image"** | Destrempes–Malinin arXiv:1703.02215v2 Thm 5, unrefereed | would apply | uniform | **FALSE as stated** (Lane 3: 20806a1, ℓ = 11, #Sha[11^∞] = 121 by Skinner–Urban) |
| 12 | **"Sha finite for every E/Q"** | Nguyen arXiv:1309.7675, unrefereed, v1 only | would apply | — | not credible; separate audit F5 |
| 0″ | **Fitting-ideal form of row 0 (newest).** For K/Q abelian, p > 3 with image ⊇ SL₂(Z_p) (+ mild Hyp 1.2, true for almost all p for each (E,K)): (a) θ_K^{MT} ∈ I^{r_p + sp(m) + 2c}; **(b) θ_K^{MT,#} ∈ Fitt⁰_{Z_p[G]}(Sel_p(E/K)^∨)** — unconditional (no Sha-finiteness, BSD or IMC); Thm 1.7 leading-term congruences at split multiplicative primes | D. Bullach–M. Honnor, arXiv:2511.07203 (10 Nov 2025), Thm 1.4, 1.7, Cor 1.9; preprint [coord: abs + HTML via WebFetch summary — NOT read line by line] | p > 3 ✓ (SL₂(Z_p) ⊂ image for p ≥ 5) | for FIXED K it holds for almost all p — but then it only sees characters χ ≠ 1 of order prime to p, i.e. RANK-0 TWISTS with L(E,χ,1) ≠ 0. At the trivial character it reads 0 ∈ Fitt⁰ (vacuous, since Sel has rank 2) | information on Sel(E/Q) enters only through p-EXTENSIONS K/Q (conductor ℓ ≡ 1 mod p). [Coordinator's derived remark, not from the paper: for G = Z/p, Fitt⁰(M) ⊂ 𝔪^d with d = dim M/𝔪M, and u·x² ∉ 𝔪³, so "leading coefficient a p-unit" again forces dim Sel_p ≤ 2 — the same per-p criterion as row 0.] |

### 2b. Further candidates from clusters A (Heegner) and B (Kato) — all read at the source by the agents before the limit hit

| # | candidate | source, status | vs seed | p-uniform? | exact missing statement |
|---|---|---|---|---|---|
| 0′ | **Heegner twin of row 0.** θ′(E,S) ∈ E(K_S)^{⊗2} ⊗ Z[Γ_S] (Γ_S = Gal(K_S/K)) is a **p-independent** global object. Thm 2.4 (proved): θ′ ∈ I^{2ρ}, ρ = max(r⁺,r⁻) − 1, after inverting 2, 3, small primes, non-surjective p, Tamagawa primes. **Prop 5.9 (proved): if some order-ρ partial Kolyvagin derivative D_k α(S) ≢ 0 mod p then Sha(E/K)[p] = 0** and Sel_p(E/K) → ⊕_{v∣S}E(K_v)/p is onto; primes ℓ ∣ S need only be inert with p ∣ ℓ+1 (no condition on a_ℓ). Conj 2.3 (leading term = c²u²·#Sha(E/K)·J_S·R_S) is OPEN | H. Darmon, Invent. Math. 110 (1992) 123–146, published [agent A, author PDF] | all p ≥ 5 qualify (K Heegner with r_an(E^K) = 1: r = 3, r⁺ = 2, r⁻ = 1, ρ = 1); Sha-finiteness NOT assumed | object p-independent; CONTENT is not: (I^{r−1}/I^r) ⊗ Z/p = 0 unless p ∣ #Γ_S = h_K·∏(ℓ+1)/u | same as row 0: a fixed S certifies only the finitely many p ∣ #Γ_S. The all-p statement is Conj 2.3, which contains #Sha (circular) |
| 1′ | **Exact one-prime rank-2 certificate.** r_an = 2, c prime inert in K with p ∣ gcd(a_c, c+1); if the reduction of P_c = Tr(D_c y_c) in E(F_{λ²}) ⊗ Z/p is ≠ 0 then rank ≤ 2, and rank = 2 ⇒ Sha(E/Q)[p] = 0. Rem 5.3: the class [P_c] exists modulo the INTEGER ideal I = (a_q, q+1 : q ∣ c) — p-independent, but sees only p ∣ I. Verified for ten rank-2 curves at p ∈ {3,5,7}. Author (2011): proving that for EVERY p some c works "would be an extremely deep result" | W. Stein, "Kolyvagin's conjecture for specific higher rank elliptic curves", 2011 preprint, Thm 5.11 (corollary of Kolyvagin 1991) [agent A + coord pp.1–4] | theorem applies per p ≥ 5; the algorithm needs Div(X₀(N)^{ss}) at N ≈ 6.5·10¹⁵ — infeasible | per-p | a statement for all p |
| 2′ | **Kurihara numbers at ANY reduction type, no IMC, no finiteness input.** One δ_n ≢ 0 mod p with ν(n) = rank ⇒ Sel(Q,E[p^∞]) = (Q_p/Z_p)^{rank}, i.e. Sha[p^∞] = 0 for that p. Appendix (with Pollack): rank ≥ 2 curves (389.a1, 433.a1, …) at p = 7, 101; authors note no pattern in the p-variation of non-vanishing δ_n is known | C.-H. Kim (+R. Pollack), arXiv:2505.09121v1 (2025), Thm 1.1/1.2, Cor 1.11; preprint [agent B] | large image at all odd p ✓ | per-p (N₁(p): ℓ ≡ 1, a_ℓ ≡ ℓ+1 mod p) | no p-independent D with "p ∤ D ⇒ some δ_{ℓ₁ℓ₂} is a p-unit" |
| 3′ | Sakamoto: Kurihara's conjecture ⟺ IMC; Sel(Q,E[p]) ≅ ⊕_{ℓ∣d}E(Q_ℓ)⊗F_p for δ-minimal d | Doc. Math. 27 (2022), published [agent B] | good ordinary non-anomalous p ≥ 7 ✓ | per-p | Sha[p] = 0 ⟺ δ-minimal d has exactly 2 prime factors; nothing forces ν(d) = 2 for all large p |
| 4′ | Mazur–Rubin core-rank-one theory: corank of strict Selmer = ord(κ); finite ⟺ κ₁ ≠ 0. For MW rank 2: κ₁ = z_Kato = 0 for EVERY p (strict Selmer has corank ≥ 1), so the rank-0 index mechanism is structurally empty; all information sits in derived classes over p-dependent primes | Mazur–Rubin, Mem. AMS 168 (2004) Thm 5.2.12, Cor 5.2.13, Thm 6.2.4; published [agents A, B] | ✓ all p ≥ 5 | per-p | "higher rank Kolyvagin systems" (MR16, Burns–Sakamoto–Sano, Büyükboduk) means CORE rank > 1; for E/Q the core rank is 1 at every p |
| 5′ | Howard's inequality rank S_p(E/K) ≤ 1 + 2·ord_J(L): if ord_J = 1 then corank Sel(E/K) ≤ 3 = rank E(K) ⇒ Sha(E/K)[p^∞] finite | B. Howard, Compositio 140 (2004); published [agent A] | good ordinary p ≥ 5 ✓ (Thm A itself needs κ₁ ≠ 0 — false here) | per-p (Λ = Z_p[[Γ]]) | ord_J of the Λ-adic Heegner class is a p-adic quantity computed per p |
| 6′ | Derived p-adic heights / BDP leading coefficient: ord_J F_p^BDP ≥ 2(max r^± − 1), leading coefficient ∝ Reg_{p,der}·#(Sel/div)·∏c_ℓ² | Castella–Hsu–Kundu–Lee–Liu, Trans. AMS Ser. B 12 (2025); published. (Agboola–Castella's earlier version ASSUMES #Sha(E/K)[p^∞] < ∞) [agent A] | ordinary p ≥ 5 ✓; supersingular IMC needs squarefree N ✗ | per-p | insensitive to a divisible part of Sha; ord_J L_p^BDP = 2 must be computed per p |
| 7′ | Mazur–Tate conjecture from BSD + generalized Perrin-Riou | Burns–Kurihara–Sano arXiv:2103.11535 (= IMRN 2025, rnaf012), Thm 1.1 (needs full BSD for E), Cor 1.2 (unconditional only for a SIMPLE zero, N squarefree, supersingular p) [agent B] | rank 2, N not squarefree ✗ | — | **WRONG DIRECTION**: BSD ⇒ Mazur–Tate, never the converse |
| 8′ | Higher-rank Euler/Kolyvagin/Stark systems I–IV; Bullach–Burns 2509.13894 (needs L(E/K,1) ≠ 0); Burns–Macias Castillo–Wuthrich (simple zero + Sha(A_F) finite) | [agent B] | ✗ rank-0/rank-1 hypotheses or Sha-finiteness input | per-p | nothing unconditional in MW rank 2 |
| 9′ | Jetchev–Nekovář–Skinner split anticyclotomic Euler systems | announced only; cited as forthcoming in 2020–2024 papers; **could not be opened (not public)** [agent A] | needs non-trivial base class; y_K is torsion here | per-p | — |

### 2c. Cluster C — diagonal cycles, generalized Kato classes, GSp(4), rank-two Euler systems, plectic points (agent C, sources read; its final summary was cut off by the limit)

| # | candidate | source, status | vs seed | p-uniform? | exact missing statement |
|---|---|---|---|---|---|
| C1 | κ_{α,α⁻¹} ≠ 0 ⟺ dim Sel_str(Q,V_pE) = 1; Cor C: κ ≠ 0 ⇒ dim_{Q_p} Sel(Q,V_pE) = 2. **Cor B (κ ≠ 0 PROVED) ASSUMES rank 2 AND Sha[p^∞] finite** | Castella–Hsieh, Forum Math. Sigma 10 (2022) e12 (arXiv:1809.09066v4); published | per-p satisfiable (p good ordinary, split in auxiliary K, N⁻ ⊂ {3,2243,5843}, two auxiliary L-values ≠ 0) | per-p (Hida families at p, anticyclotomic p-adic L-function) | (a) the only non-circular direction needs "κ_p ≠ 0", a p-adic statement with no p-independent criterion; (b) conclusion is rational: Sha[p^∞] FINITE, never Sha[p] = 0 |
| C2 | same for CM curves (Thm B; Thm C assumes Sha[p^∞] finite) | Castella, arXiv:2204.09608v3, to appear Amer. J. Math. | ✗ seed is non-CM | per-p | — |
| C3 | non-CM version: κ_p(E) ≠ 0 ⇒ dim Sel(Q,V_pE) = 2; converse assumes dim Sel = 2 | Castella, arXiv:2312.01481 (Springer 2026), Thm 5.2.3 | (h1)–(h3) ✓; compatibility of the cited IMC inputs with 2³, 4547² ∣ N⁺ NOT verified | per-p, ordinary only | "integral non-vanishing: not addressed"; circular w.r.t. finiteness |
| C4–C5 | Darmon–Rotger: proved parts are reciprocity laws, rank-0 Mordell–Weil vanishing (their proof does NOT give finiteness of Selmer/Sha, JAMS p.7) and LOWER bounds dim Sel_p ≥ 2; rank-2 description = Conj 3.2, 3.8, 3.12. Question 1.2: rank-2 classes arise only as p-adic limits; a p-independent geometric class is doubted | Res. Math. Sci. 3:27 (2016); JAMS 30 (2017); published | — | per-p by construction | WRONG DIRECTION + conjectural |
| C6–C9 | BSV balanced diagonal classes (rank (1,1), multiplicative p inert in K); BSV Garrett p-adic BSD (a CONJECTURE + derivative formula); Darmon–Rotger Stark–Heegner (lower bounds); ABSV endoscopy (semistable, sign −1, non-triviality) | Astérisque 434 (2022); Ann. Inst. Fourier 2026; Oberwolfach Rep. 28/2023 | ✗ wrong rank pattern / p ∣ N only / semistable | per-p | no upper bound on Sel(Q,V_pE) with a genuine double zero |
| C10 | Loeffler–Zerbes GSp(4) programme (Bloch–Kato for GSp(4); BSD for modular abelian surfaces; symmetric cube) | arXiv:2003.05960v4 (Cambridge J. Math. 2026), 2110.13102v3, 2005.04786; "GSp(4)×GL(2)×GL(2)" 2011.15064 is self-described largely conjectural | ✗ every theorem has "central/critical L-value ≠ 0" as hypothesis | per-p | no theorem with a vanishing central value |
| C11 | rank-two Euler/Kolyvagin/Stark systems (Mazur–Rubin 2016; Burns–Sakamoto–Sano; BLLV; Büyükboduk–Lei) | published | "rank two" = CORE rank (f⊗g, Sym²f, E over bigger fields); core rank of T_pE over Q is 1 | per-p | a rank-2 Euler system known to be non-trivial when ord L(E,s) = 2 — does not exist |
| C12 | **The template that exists only in rank ≤ 1.** L(0,M) ≠ 0 ⇒ H¹_f(Q,M_p) = 0 for ALL BUT FINITELY MANY p (explicit exclusions); odd case: a p-INDEPENDENT Hirzebruch–Zagier cycle, but the hypothesis AJ_p(Δ) ≠ 0 is per p (p-independence = Conj 1.9). Rem 1.7: the Darmon–Rotger p-adic method controls only the local image at p, so Sha bounds from it "seem very hard" | Y. Liu, Invent. 205 (2016) Thm 1.3–1.5; JEMS 2019; Liu–Tian–Xiao–Zhang–Zhu, Invent. 228 (2022); survey arXiv:2509.16881 (ranks 0 and 1 only); published | ✗ rank-8 triple-product / Rankin–Selberg motives, never h¹(E); seed has a DOUBLE zero | **uniform in p — in analytic rank 0 only** | a rank-2 analogue: p-independent cycle + bipartite argument giving dim Sel_p = 2 for almost all p. No instance in print |
| C13 | mock plectic invariant Q_K ≠ 0 ⇒ corank Sel_{p^∞}(E/K) = 2 | Fornea–Gehrmann arXiv:2311.03100v2 Thm 3.4 (preprint); plectic Stark–Heegner points are conjectural | only MULTIPLICATIVE p ≥ 5 inert in K: p ∈ {2243, 5843} | per-p (two primes at most) | authors cannot yet verify Q_K ≠ 0; conclusion is corank, not Sha[p] = 0 |

### 2d. Cluster D — main conjectures as per-prime tools, explicit rank ≥ 2 curves, fixed E / varying p (agent D, sources read; items "5077a1" and the final 2024–26 sweep were cut off by the limit and were redone by the coordinator, §2f)

| # | candidate | source, status | vs seed | p-uniform? | exact missing statement |
|---|---|---|---|---|---|
| D1 | **The only genuinely horizontal theorem found for rank ≥ 2.** t_{E/Q,p} := Z_p-corank of Sha(E/Q)(p) ≤ (1/2 + ε)p − g for ALL good ordinary p ≥ c(E,ε) (Part I: 2p − g). Mechanism: a NON-ZERO algebraic integer ξ(p) (Hecke L-value L(ψ̄^p, p) in the absolutely convergent range, Katz divisibility) + the PRODUCT FORMULA + proved one-variable main conjectures (ψ^p lies on the same p-adic L-function as the BSD point) | Coates–Liang–Sujatha, Milan J. Math. 78 (2010) Thm 1.1/3.2 (arXiv:1005.4206v2); Part I arXiv:0901.3832; published [agent D, full PDF] | ✗ CM only (needs a p-adic L-function line through the BSD point containing a classical point in the convergent range with coefficient field K for all p) | **uniform — but the conclusion is a GROWING corank bound**, "a far cry" from t = 0 (authors) | (i) CM; (ii) corank ≤ p/2 is not corank 0 and says nothing about Sha[p]. No improvement and no non-CM analogue found (searches D7–D8) |
| D2 | Rank-two CM criterion: c̃₂(p) unit ⟺ Reg_γ unit and Sha[p^∞] = 0 (p split, outside S_E); verified at 8,047 of 8,050 (E,p), p < 30,000. **§1.5 Q3 asks, as an OPEN question (8 Sep 2026), whether a fixed algebraic number controls the exceptional p** — the rank-2 analogue of the Heegner point. Q1 heuristic: the unit condition is EXPECTED to fail for infinitely many p (≈ ½ log log X below X) | B. Banwait arXiv:2609.08431v1, Thm A/B; preprint [agent D, full HTML] | ✗ CM only | per-p; §1.1: horizontal statement open for every rank ≥ 2 curve, even "Sha[p] = 0 for infinitely many p" | Q3 itself. Note the corollary of Q1: "leading coefficient of L_p is a unit for all p > p₀" is heuristically FALSE, so no per-p unit criterion can ever be uniformised verbatim; BSD only predicts v_p(L_p^*) = v_p(Reg_γ) + tame terms |
| D3 | Cyclotomic IMC at every good ordinary p > 3 with E[p] irreducible, **no condition on the conductor** (Rem 1.3.2); p-part of BSD only for r ∈ {0,1} (Cor 1.3.1) | Burungale–Castella–Skinner arXiv:2405.00270v2, IMRN (accepted); Skinner–Urban Invent. 195 (2014) Thm 1 (one q ∥ N with ρ̄ ramified: q = 2243) [agent D] | ✓ at every good ordinary p ≥ 5, two independent routes; additive primes harmless | per-p in its OUTPUT | for r = 1 the leading term is tied to a p-independent Heegner point (BDP / p-adic Gross–Zagier); for r = 2 no such object — the paper says nothing about r ≥ 2 |
| D4 | Supersingular IMC: Kobayashi's ± conjecture for SEMISTABLE E (BSTW Thm 1.3); Kato's IMC for arbitrary reduction at p given one Steinberg prime ℓ ∥ N with ρ̄^{G_{Q_ℓ}} = 0 (Fouquet–Wan Thm 1.1) | BSTW arXiv:2409.01350v2 (preprint); Fouquet–Wan arXiv:2107.13726v3 (preprint, unrefereed; BSTW do not rely on it) [agent D] | BSTW ✗ (additive at 2, 4547; 4547 is type III, not a quadratic twist of anything semistable). Fouquet–Wan: hypotheses (1)–(3) hold with ℓ = 3 for every odd p ≠ 3 — IF that preprint is correct | per-p | an IMC never gives finiteness: one still needs ord_T = 2 and the leading-term valuation at each p |
| D5 | λ_p = r and μ_p = 0 for good ordinary p outside Σ ∪ Σ′ ∪ Π | Kundu–Ray, Trans. AMS 374 (2021) Thm 3.13 (3.16 supersingular, conditional on p-adic BSD); published [agent D] | — | "all p outside an exceptional set" — but Π = {p : p ∣ R_p/p^r} is uncontrolled ("the same is not known for Π") | **WRONG DIRECTION + ASSUMES Sha[p^∞] finite and Schneider's conjecture** (via Perrin-Riou/Schneider). Their table: Π^{≤1000} ≠ ∅ for 5 of the first 10 rank-2 curves — extra regulator divisibility occurs at a Wieferich-like rate. In positive rank NO theorem gives λ_p = rank for almost all / density-one p (rank 0 only: Greenberg + Kolyvagin + Kato) |
| D6 | Fine Sha: for E/Q of positive rank the fine Tate–Shafarevich group EQUALS Sha(E/Q)(p), every p | Wuthrich, Math. Proc. Camb. Phil. Soc. 142 (2007) Thm 3.5; published [agent D] | ✓ rank 2 | structural identity | so "fine Sha trivial for almost all p" is not a weaker target: it IS target B |
| D7 | Schneider's conjecture (Reg_p ≠ 0): open for every non-CM curve of rank ≥ 1 at every p as a general theorem (Wuthrich 2004 Thm 3 is fixed p / varying curve — wrong axis); shadow-line papers are fixed-p numerics/conjectures | Wuthrich, J. London Math. Soc. 70 (2004); Balakrishnan et al. arXiv:1610.08729, 2409.00891, 1210.2739 [agent D] | — | per-p | no theorem gives non-vanishing, let alone unit-ness, of Reg_p for all large p or a density-one set |
| D8 | "Horizontal variation of Tate–Shafarevich groups" arXiv:1712.02148 | [agent D] | — | WRONG AXIS: K varies, p fixed | — |

### 2e. Cluster E — mechanisms that bound the SET of exceptional p; seed-specific structure (agent E, sources read; "uniform open image" and its final summary were cut off and were redone by the coordinator, §2f)

| # | candidate | source, status | vs seed | p-uniform? | exact missing statement |
|---|---|---|---|---|---|
| E1 | **The rank ≤ 1 uniform package**: Kolyvagin (c₃I_K kills Sha(E/K)); ord_p #Sha ≤ 2 ord_p I_K (Cha, JNT 2005; Grigorov–Jorza–Patrikis–Stein–Tarniţă as corrected by Lawson–Wuthrich Thm 14; Jetchev, Compositio 2008: 2(ord_p I_K − max ord_p c_q)); Kato: ord_p #Sha ≤ ord_p(L(E,1)/Ω) for p ∤ 6N, ρ_p surjective | catalogued in R. L. Miller, LMS JCM 14 (2011) Thm 4.2, 4.4, 5.1–5.4; all published [agent E] | every AUXILIARY hypothesis holds for all odd p ∤ N; but r_an = 2 | **uniform in p** | every theorem has "analytic rank ≤ 1" (L(E,1) ≠ 0 or y_K non-torsion) as a hypothesis. In rank 2 both global objects vanish identically; Miller's paper states no bound for rank ≥ 2 |
| E2 | **The one genuine "explicit finite exceptional set" Bloch–Kato theorem touching the seed's newform — for the WRONG MOTIVE.** For every λ ∉ T_f = {λ ∣ Nk!} ∪ {ρ̄∣_{G_F} not abs. irreducible}: #H¹_f(Q, ad⁰) = λ-part of the congruence ideal η_f (a p-INDEPENDENT ideal ≈ modular degree). For the seed: every ℓ ∉ {2, 3, 2243, 4547, 5843}; so H¹_f(Q, ad⁰E[ℓ^∞]) = 0 for all ℓ outside an explicit finite set | Diamond–Flach–Guo, Ann. Sci. ENS 37 (2004) Thm 0.1/0.2; long version arXiv:2512.02348v2; published [agent E] | ✓ applies (second part of T_f is empty since the image is GL₂(F_ℓ)) | **uniform in ℓ** | does not transfer to H¹_f(Q,E[ℓ^∞]): (a) Taylor–Wiles identifies the ADJOINT Selmer group with a cotangent space of a deformation ring; the standard Selmer group classifies extensions of 1 by ρ_f (a residually REDUCIBLE problem: the Eisenstein-congruence method, which is per-p and gives LOWER bounds); (b) needs a NON-ZERO L-value equal to period × p-independent integer; in rank 2 H¹_f(Q,V_ℓE) is 2-dimensional for every ℓ and the true formula involves an ℓ-adic regulator no patching argument sees. No paper found doing patching for the standard representation in positive rank |
| E3 | Sel_p vs class group of Q(E[p]): the part of Sel_p unramified at p injects into Hom_G(Cl_K, E[p]); converse rank Hom_G(Cl_K/p,E[p]) ≤ rank Sel_p + #T | Prasad–Shekhar, Pacific J. Math. 312 (2021) Thm 3.1/4.1; Česnavičius, Compositio 151 (2015) (needs Z/ℓ or μ_ℓ ⊂ A[ℓ] — fails over Q); Lawson–Wuthrich (H¹(Gal(Q(E[p])/Q),E[p]) = 0); Dainobu, Banerjee–Chakraborty–Hoque, Abhishek–Kundu (lower bounds) [agent E] | hypotheses hold for all large p | hypotheses uniform; conclusion an EQUIVALENCE | **CIRCULAR**: "for all large p, rank Hom_G(Cl_{Q(E[p])}/p, E[p]) ≤ 2" is a GL₂ Vandiver-type statement, equivalent to target B by Thm 4.1; no such theorem exists for any non-CM E (matches the project's own C1 class-group gate) |
| E4 | Visibility: congruence + Mordell–Weil of the partner ⇒ NON-trivial Sha (Cremona–Mazur; Agashe–Stein; Jetchev–Stein Thm 4.1.1; Shiga arXiv:2602.19861v2 Thm 4.10); every class is visible in SOME abelian variety (Banwait–Caro–Chidambaram arXiv:2601.21519v2 Thm 1.6); Fisher: order-6, 7 elements invisible in abelian surfaces | published / preprints [agent E] | — | — | **WRONG DIRECTION**: "p ∤ modular degree / congruence number ⇒ Sha[p] = 0" is not a theorem and is false as a principle (invisible elements at level N exist; visibility at higher level constrains nothing) |
| E5 | Effective bounds #Sha ≪ N^{1/2+ε} etc. | Goldfeld–Szpiro 1995; Surroca arXiv:0801.1054; Goldfeld–Lieman (CM rank 0); Rajan, Hindry–Pacheco, Griffon (function fields) [agent E] | — | — | all ASSUME BSD / finite Sha (or are over function fields). No unconditional bound on #Sha or on its support for r_an ≥ 2 |
| E6 | Rational 2-torsion / 2-isogeny; Zywina's family | Zywina arXiv:2502.01957v1 (only Sha statement: Sha[2] = 0); 2025–26 rank constructions (Savoie 2506.17605, Koymans–Pagano, Gajović–Park, Zywina 2502.01026/2505.16960); Smith, Kane–Klagsbrun, Klagsbrun–Lemke Oliver (2-primary, varying CURVE) [agent E; several abs-only] | — | — | no theorem uses a 2-isogeny to control Sha[p] for odd p; only isogeny invariance Sha(E)[p^∞] ≅ Sha(E′)[p^∞] |
| E7 | Logachev, "Reduction of a problem of finiteness of Tate–Shafarevich group to a result of Zagier type" arXiv:math/0411346v2 | preprint, programme with acknowledged gaps [agent E] | ✗ about Siegel sixfolds; no class for an elliptic curve | — | existence of the classes is unproved |

### 2f. Coordinator gap-fill (topics the agents did not reach before the limit; search-level unless marked)

| topic | what was checked | result |
|---|---|---|
| Büyükboduk; Perrin-Riou's conjecture; Beilinson–Kato vs Heegner | Büyükboduk (ASPM 86), Büyükboduk–Pollack–Sasaki arXiv:1811.08216, Bertolini–Darmon–Venerucci (Adv. Math. 2022), Venerucci arXiv:1407.1913, BSTW Thm 1.13 | all concern loc_p(z_Kato) ≠ 0 ⟺ ord L = 1: **analytic rank ≤ 1**. Büyükboduk's "higher rank" Λ-adic Kolyvagin systems = higher CORE rank. Nothing for MW rank 2 |
| statistics / mod-p non-vanishing of modular symbols and Mazur–Tate elements | searches C14; hits: λ-invariants of Mazur–Tate elements (arXiv:2412.16629, 2512.00525), numerical refined BSD (2412.17703), μ-invariants (2408.07826) | no theorem gives mod-p non-vanishing of a Kurihara number or of a Mazur–Tate leading coefficient for all large p on a fixed curve. Kim–Pollack (2505.09121, A.1.4) say no pattern in p is known |
| level raising / bipartite Euler systems | Howard "Bipartite Euler systems" (arXiv:1202.6353), Bertolini–Darmon, Kim 2203.12161 (structure theorem, definite case), H. Wang arXiv:2004.14916 (GKS cycles, bipartite), Liu/LTXZZ (row C12) | admissible primes are defined RELATIVE TO p (p ∣ (q+1)² − a_q²); p-uniform outputs exist only in rank 0 (L-value) — row C12 |
| 5077a1 (rank 3) | search C16 | nothing beyond per-p p-adic bounds (Sage `p_primary_bound`); no new result 2020–2026 found |
| uniform open image (Serre, Zywina, Bilu–Parent–Rebolledo, Le Fourn–Lemos, Furio–Lombardo) | search C18 | no corollary about Sha found; surjectivity is a hypothesis-remover only (cf. row E3 and §3) |
| Gross–Kudla–Schoen cycles; Yuan–Zhang–Zhang | search C19; Darmon–Rotger I; Wang 2004.14916; Castella–Do arXiv:2303.06751 | rank 0 and 1 of TRIPLE-PRODUCT motives; rank-2 information only via p-adic limits (rows C1–C5) |
| Fitting ideals of BDP Selmer groups | Kim–Pal–Ray arXiv:2609.17003 (15 Sep 2026), abstract | fixed p, anticyclotomic tower; per-p |
| other claimed proofs of finiteness of Sha | search C8 | only Nguyen 1309.7675 (audit F5) and the refuted Destrempes–Malinin |

## 3. Special attack: can the set of exceptional p be bounded from …?

| source of a bound | best available statement | produces a finite exceptional set in rank 2? |
|---|---|---|
| residual image (GL₂(F_p) for all odd p) | H¹(Gal(Q(E[p])/Q), E[p]) = 0, so Sel_p ↪ Hom_G(Gal(·/Q(E[p])), E[p]); a HYPOTHESIS of every theorem above | no — it removes obstructions, it supplies no class |
| Kolyvagin-system primitivity | M_∞ = 0 PROVED for the seed at every good ordinary p ≥ 5 (W. Zhang; BCGS Thm B; Castella–Sano Thm B) | no — primitivity converts "Sha[p] = 0" into "first non-zero level is a p-unit", it does not locate that level (ν_p, resp. ρ_p) |
| Euler-system index | rank 0: L(E,1)/Ω; rank 1: [E(K) : Z y_K]. Rank 2: z_Kato and y_K vanish; the index lives in a derivative (BKS) | conjectural only (row 4) |
| Fitting ideals | determined by δ_n / κ_n with n built from p-dependent primes | no (rows 1–2) |
| height / regulator denominators | Reg_p unit is needed per p; Schneider's conjecture open | no |
| congruence primes / modular degree | bound H¹_f(Q, ad⁰E[ℓ^∞]) for all ℓ outside an explicit finite set (Diamond–Flach–Guo, row E2); visibility theory CONSTRUCTS Sha from congruences (row E4) | no — wrong motive (ad⁰), resp. wrong direction; "p ∤ modular degree ⇒ Sha[p] = 0" is not a theorem |
| class groups of Q(E[p]) | Prasad–Shekhar: an eigencomponent of Cl(Q(E[p]))/p ≅ (part of) Sel_p (row E3) | no — a GL₂ Vandiver-type statement, equivalent to the target |
| effective bounds on #Sha | all assume BSD / finite Sha, or are over function fields (row E5) | no |
| Mazur–Tate elements / Heegner θ-elements (p-independent group-ring elements) | Ota Thm 1.5; Darmon Prop 5.9; Bullach–Honnor Thm 1.4 (rows 0, 0′, 0″) | **no — closest of all.** The implication is proved and unconditional; the exceptional set of the THEOREM is explicit and finite; but its hypothesis (leading coefficient ≢ 0 mod p) can only be tested on S with every ℓ ∣ S ≡ ±1 mod p |
| a non-zero algebraic number + product formula | Coates–Liang–Sujatha (row D1) | only a corank bound ≈ p/2, CM only |
| support of an integral/motivic class | the rank-2 motivic class is P₁∧P₂ ∈ ∧²E(Q); its "BSD multiple" η^BSD is exactly BKS's object | conjectural only (row 4) |

## 4. Proposed sharpening of the label (no merge performed)

Replace "no known theorem" by the exact open statement. Fix once a Heegner field K (every prime of N split) with r_an(E^K) = 1;
then Sha(E^K/Q) is FINITE (Gross–Zagier–Kolyvagin), so Sha(E^K)[p] = 0 for p > p₁(K). For every good prime p ≥ 5 with
p ∤ D_K (ordinary: W. Zhang 2014 / BCGS; supersingular: Sweeting App. A) Kolyvagin's conjecture holds for the seed, and
Kolyvagin's structure theorem gives (w = +1 forces ν_p odd and corank Sel_{p^∞}(E/Q) = ν_p + 1):

    Sha(E/Q)[p^∞] finite   ⟺  ν_p = 1                                   (one-prime derived class κ_ℓ ≠ 0 at some level p^M)
    Sha(E/Q)[p^∞] = 0      ⟺  ν_p = 1 and M₁(p) = M_∞(p)               (p > p₁(K); M₁ − M_∞ = ½ ord_p #(Sha(E/K)[p^∞]/div))
                           ⟺  ∃ ℓ inert in K, p ∣ ℓ+1, p ∣ a_ℓ, with κ_ℓ ≢ 0 in H¹(K, E[p])     (when M_∞ = 0: ordinary p, W. Zhang)

and on the Kato side, for every good ordinary p > 3 (Castella–Sano Thm B gives M_∞(δ) = 0; Kim Thm 1.8):

    Sha(E/Q)[p^∞] = 0      ⟺  ∃ n = ℓ₁ℓ₂ (ℓᵢ ≡ 1, a_{ℓᵢ} ≡ ℓᵢ+1 mod p) with δ_n ≢ 0 (mod p)
    Sha(E/Q)[p] = 0        ⟸  ∃ ℓ ≡ 1 (mod p), E(F_ℓ)[p] cyclic, with θ̃_ℓ ≢ 0 (mod p)      (Ota Thm 1.5; any good p ≥ 5)

So **G23 ⟺ "for all p > p₀ some one-prime Heegner derived class is non-zero mod p" ⟺ (ordinary p) "for all p > p₀ some
two-prime Kurihara number is a p-unit"**. Each right-hand side is an infinite family of per-p statements whose auxiliary primes
are chosen relative to p; no p-independent source for them is known (Stein 2011: proving it for every p "would be an extremely
deep result"; Kim 2026 Question 4.6; Banwait 2026 §1.5 Q3). Not an impossibility claim.

## 4b. By-product for the architect (NOT part of the verdict; per-prime only; label UNVERIFIED until costed by the project)

Ota's Thm 1.5 / 6.4 (row 0; verified on the arXiv PDF pp. 2–3, 37–39) is a per-prime certificate the DAG does not list:

- **Hypotheses at the seed hold for every prime p ≥ 5 with p ∤ N, supersingular p included** (no IMC, no ±-theory, no p-adic
  L-function, no ordinarity): p ∤ 6N·#E(F_p)·∏m_ℓ, surjective p-adic image, p ≥ r_E = 2.
- **Input:** ONE good prime ℓ ≡ 1 (mod p) with E(F_ℓ)[p′] cyclic for every non-inverted prime p′ (Thm 6.4 takes S as in Thm 6.1;
  non-cyclicity needs p′ ∣ ℓ − 1 and p′² ≤ ℓ + 1 + 2√ℓ, which never happens for the ℓ listed below), and the modular symbols
  [a/ℓ]⁺, a ∈ (Z/ℓ)^×. Theorem 1.2 puts θ_ℓ in I_ℓ²; the test is whether its class in I_ℓ²/I_ℓ³ ⊗ Z/p ≅ Z/p is non-zero
  (leading coefficient Σ_a [a/ℓ]⁺·C(e_a, 2) − m·C(ℓ−1, 2) mod p, where σ_a = σ_g^{e_a} and Σ_a [a/ℓ]⁺e_a = m(ℓ−1)).
  The Darmon–Kolyvagin derivative may have order 2 at a single prime (this is why p ≥ r_E is required), so no second prime
  and no condition a_ℓ ≡ ℓ + 1 (mod p) is needed.
- **Output if non-zero:** Sha(E/Q)[p] = 0 (hence Sha[p^∞] = 0) and p ∤ J_ℓ. **Semi-decision:** a zero class proves nothing.
- **Why it may matter:** the symbols have denominator ℓ ≈ 2p…p·log p instead of p² (SW depth 2) or p⁵–p⁶ (the supersingular ±-route
  that makes G19 ROUTE_BLOCKED). Smallest choices: p = 23 → ℓ = 47; p = 29 → ℓ = 59; p = 131 → ℓ = 263; p = 7 → ℓ = 29;
  p = 11 → ℓ = 23; p = 13 → ℓ = 53; p = 17 → ℓ = 103 (p = 17 currently needs depth 3 because ord₁₇Reg₁₇ = 3; the G_ℓ-valued
  Mazur–Tate height is a different object and need not degenerate there). By the project's own streaming cost model
  (T ≈ 4.5·d·√N for denominator d) ℓ = 47 is ≈ 2× the completed p = 5 run. COST CLAIM UNVERIFIED — for the architect to check;
  normalisation of θ_S (Ota §2: Néron periods, strong Weil curve, t·c(E) inverted — all 2-powers here) must be matched to the
  project's x_b convention before any run.
- It does NOT touch G23: one ℓ serves only the primes dividing ℓ − 1.

## 5. What was checked

- **Coordinator:** `F3_work/QUERY_LOG.md` (C1–C25): 2025–26 sweeps in several phrasings; Kim 2609.15328 (full HTML); Ota 1509.00682
  (PDF pp. 1–4, 37–39); Stein IMRN 2011 and Stein 2011 (PDFs); Bullach–Honnor 2511.07203 (HTML summary); local texts of BKS24,
  Castella–Sano 2601.14504, Stein–Wuthrich 2013.
- **Cluster agents** (each file has its own query log and 7-item blocks): `F3_work/agents/A_heegner_kolyvagin.md` (12 candidates),
  `B_kato_kurihara_bks_mazurtate.md` (13), `C_diagonal_generalized_kato.md` (13), `D_imc_explicit_rank2.md` (10 blocks),
  `E_uniformity_mechanisms.md` (13). All five were killed by the usage limit before writing their summaries; every block on disk was
  integrated above. Sources the agents could NOT open: Kato's Astérisque 295 PDF (> 10 MB; secondary statements used);
  Jetchev–Nekovář–Skinner (not public); ABSV full paper (Oberwolfach abstract only); Crelle page of Burns–Macias Castillo–Wuthrich
  (arXiv version used). Several 2025–26 rank-construction papers and class-group papers were read at ABSTRACT level only (marked in §2e).
- **Not repeated:** Lane 3's 26 queries (Destrempes–Malinin refutation; Nguyen; Yun–Zhang; Banwait first reading).
- **Mandatory topic list — coverage:** Kolyvagin systems in higher rank (A10, C11, 4′); W. Zhang (1); Sweeting (1); Jetchev/Nekovář/
  Skinner/Wan (9′, E1, D3–D4); Castella (C1–C3, 6′); Castella–Sano (2); Burns–Kurihara–Sano (4, 7′, 8′); Loeffler–Zerbes (C10);
  Büyükboduk (2f, C11); generalized Kato / diagonal cycles, Darmon–Rotger, BSV (C1–C9); rank-two Iwasawa theory (C11, 5′, 6′);
  refined BSD / ETNC (4, 7′, 8′, 0″); BKS 2024–26 (4, 7′, 0″); Mazur–Tate (0, 0′, 0″, 7′); Kurihara numbers (2, 2′, 3′);
  visibility (E4); level raising (2f, C12, 1); congruence modules (E2); uniform open image (2f, E3); effective Sha bounds (E5);
  rational 2-torsion / 2-isogeny (E6); 389a1 (5, 8, 1′, 2′); 5077a1 (2f); explicit rank-2 curves (5, D1, D2, 1′, 2′);
  higher-rank Kolyvagin conjectures (1, 3, 9); finiteness of Sha for r_an ≥ 2 (D1, D2, 11, 12, E7).

## 6. Verified versus agent-read versus inherited

- **Verified by the coordinator at the primary source:** row 0 (Ota Thm 1.2, Rem 1.3, Thm 1.5, Thm 6.4 + proof, arXiv PDF);
  row 2 (Castella–Sano Thm A/B, Kim Thm 1.8 as quoted there; local text); row 3 (Kim 2609.15328, HTML); row 4 (BKS24 Hyp 2.2,
  Thm 1.3, Thm 1.14; local text); row 5 (SW Thm 12.3; local text); row 9 (Stein IMRN, PDF pp. 1–3); Stein 2011 in rows 8/1′ (pp. 1–4).
- **Read at the source by an agent (PDF/HTML text, theorem numbers recorded), not re-checked by the coordinator:** rows 1, 0′, 1′–9′,
  C1–C13, D1–D8, E1–E4, E7. The coordinator's memory of W. Zhang's Hypothesis ♠ agrees with agent A's reading.
- **WebFetch small-model summary only (treat as UNVERIFIED at theorem level):** row 0″ (Bullach–Honnor), Kim–Pal–Ray 2609.17003, and
  the abstract-only items in E6/E3/2f.
- **Inherited from Lane 3 / Lane 1 without re-reading:** rows 11, 12 (and the first reading of rows 6, 7, 10, since re-read by agents C, D).
- **Derived by the coordinator (not in any source; flag for referee):** the ⟺ chain in §4 (uses finiteness of Sha(E^K) to identify
  M₁ with Sha(E/K)[p^∞] for large p; parity argument for ν_p odd); the 𝔪³ remark in row 0″; the cost comparison and the list of ℓ in §4b.

## 7. Findings by severity (hostile-audit convention)

- FATAL to the label "no known theorem": **none found.**
- REPAIRABLE (wording of DAG §3 G23 table): (i) add rows 0/0′/0″ — the Mazur–Tate / Heegner θ-element theorems are the closest
  existing results and are not listed; (ii) the row "Kolyvagin's conjecture … finiteness ⟺ ν_p = 1, which is not implied" is right but
  can be stated as the exact equivalences of §4; (iii) the row "BKS 2024 Conj 1.1 would give H at almost all p" should add that
  Hyp 2.2(iii) makes finiteness an input even for the conjecture's formulation.
- COSMETIC: DAG G19 says the printed supersingular IMCs do not apply (correct for BSTW/CLW/Castella–Sano); Fouquet–Wan
  arXiv:2107.13726v3 (unrefereed) WOULD apply with ℓ = 3 if correct — worth a footnote, not a route.
- UNVERIFIED: §4b cost claim; row 0″ at theorem level.

**Verdict on the audited label: PASS_WITH_CORRECTIONS** (the label stands; the corrections are the sharpening in §4 and the missing
near misses in rows 0, 0′, 0″, D1).
