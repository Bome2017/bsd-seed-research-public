# CRITERION_SS_HOSTILE_GATE: is F2's supersingular depth-2 criterion valid for the seed? (2026-09-19)

**Auditor role.** Independent, hostile. This was a bounded source-and-algebra audit: no seed computation beyond `arbcore tmin` (seconds), and one small Sage/eclib validation (5.5 CPU-s). Nothing is merged.

**Target.** F2 §B.1 (`~/BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F2_MINIMAL_FULL_BSD_AUDIT.md`, sha256 `96e16935…`).

## VERDICT: **CRITERION_SS_VALID_WITH_CORRECTIONS**

- The implication survives every attack. With the correctly paired published inputs, a nonzero mod-p X^r coefficient of θ₁ proves Sha(E/Q)[p^∞] = 0.
- The corrections (§3) concern the congruence constant, one superfluous hypothesis, the sign labels, the explicit hypotheses list, and F2's cost figure. **None of them breaks the implication.**
- Four primary texts were read only through restatements (§5). This is a provenance caveat, not a logical gap.

## 1. Sources actually read

| source | how read | what it gives |
|---|---|---|
| Kim–Kurihara, arXiv:1804.00418v3 (= IMRN 2021), local pdf sha256 `9c0b995c…f72ddaedb` | full text, l. 100–680 | notation (§1.2.2); **Prop 1.11 = [Pol03, Prop 6.18]**; θ_n definition; ω_n, ω̃_n^±; interpolation (§3.1.4); Thms 3.2, 3.4, 3.6, 3.8, 3.9; Cor 3.10 |
| Pollack–Rubin, Ann. of Math. 159 (2004), arXiv:math/0509604 | pp. 447–450, 460–463 read at the source | **eqs (10)–(12)**: the interpolation characterising Pollack's 𝓛_E^± ("defined … in Section 6.2.2 of [Po]"); intro statement of Kobayashi's divisibility; Lemma 8.3 (level-0 control, CM case); proof of Thm 8.2 (the rank-0 analogue of this argument) |
| Kitajima–Otsuki, Tokyo J. Math. 41 (2018), arXiv:1607.03612 | pp. 1–3 read at the source | **Theorem 1.1 = B.D. Kim [J. Aust. Math. Soc. 95 (2013)] Thm 1.1**, verbatim hypotheses |
| Pollack, Duke 118 (2003) (author's pdf) | **not readable**: TLS certificate error in both fetch tools; the browser pane did not render the pdf | used only through KK Prop 1.11 and PR04 (10)–(12); the n = 1 case is re-derived independently (§2.1) |
| Kobayashi, Invent. Math. 152 (2003) | **not available** (no arXiv copy found) | used through KK Thms 3.4, 3.6(2), 3.9 and PR04's statement |

## 2. The nine attacks

### 2.1 Attack 1: the Pollack congruence (exact parity, sign, normalisation)

**KK Prop 1.11 (= [Pol03, Prop 6.18]):**

    θ_n(f) ≡ ω̃_n^∓ · L_p^∓(Q_∞, f)   (mod ω_n) in Λ_n,   n even/odd respectively

Here ω̃_n^+ = ∏_{2≤m≤n, m even} Φ_m(1+X), ω̃_n^- = ∏_{1≤m≤n, m odd} Φ_m(1+X), and ω_n = (1+X)^{p^n} − 1.
- For **n = 1 (odd)** the lower sign applies: θ₁ ≡ ω̃₁^+·L_p^+.
- ω̃₁^+ is the empty product, so **there is no cyclotomic factor**.
- (Had the L⁻ branch applied, the factor Φ₁ ≡ X^{p−1} (mod p) would kill every coefficient below X^{p−1}.)

**Independent derivation.** Λ₁ ⊗ Q_p ≅ ∏_{χ of Γ₁} Q_p(χ), and both sides are integral. So the congruence mod ω₁ is equivalent to equality at the trivial character and at the p − 1 characters of order p.
- The characters of order p come from PR04 (10) with n = 1: χ(L_p^+) = −τ(χ)L(E,χ̄,1)/Ω_E, since χ(ω̃₁^+) = 1.
- Birch's formula gives Σ_{a∈(Z/p²)^×} χ(a)[a/p²]⁺ = τ(χ)L(E,χ̄,1)/Ω_E⁺.
- The trivial character comes from PR04 (12): χ₀(L_p^+) = (p−1)L(E,1)/Ω_E. The Hecke relation a_p[c/p] = Σ_j[(c+pj)/p²] + [0] with a_p = 0 gives Σ_a [a/p²]⁺ = −(p−1)[0]⁺.
- KK's θ₁ is the image of the **half-sum** over (Z/p²)^×/{±1} of [a/p²]⁺σ_a, with [·]⁺ normalised by the Néron period Ω_E⁺.
- **So, with KK's literal conventions, θ₁ = −½·L_p^+ (mod ω₁)** at every character.
- The "≡" of Prop 1.11 therefore hides a p-adic unit (the sign and the ½ depend on the θ and period conventions). **That is harmless:** the criterion only asks whether a coefficient is nonzero mod p.

**Exact normalisation of L_p^+.** It is Pollack's signed p-adic L-function of the **odd** tower layers, characterised by PR04 (10) and (12). It lies in Λ integrally when a_p = 0 and ρ̄ is irreducible (KK §1.2.2, citing [Kur02]).

### 2.2 Attack 2: why X² divides L_p^+ (no BSD used)

1. **Control at level 0.** KK Thm 3.9 with n = 0 (ω₀^± := X; Sel^±(Q₀) = Sel(Q), since E^±(Q_{0,p}) = E(Q_p)) says Sel(E/Q,E[p^∞]) → Sel^±(Q_∞,E[p^∞])^Γ is **injective**, for both signs. The reason is E(Q)[p] = 0 (a_p = 0) and [Kob03, Lemma 9.1].
2. rank E(Q) = 2, so Sel(E/Q)[p^∞] has corank ≥ 2, so rank_{Z_p}(X^±)_Γ ≥ 2.
3. X^± is Λ-torsion (KK Thm 3.4 = [Kob03 Thm 7.3(ii)]). For torsion X, rank_{Z_p} X_Γ ≤ ord_X char(X): the rank of Γ-coinvariants is a pseudo-isomorphism invariant, and for ⊕Λ/(f_i^{e_i}) it counts the factors with f_i = X. Hence ord_X char(X^±) ≥ 2.
4. **Divisibility** (KK Thm 3.6(2)): (L_p^+) ⊆ char(X⁻). So **X² ∣ L_p^+**.

Only the Mordell–Weil rank enters. No analytic rank, no BSD, no p-adic BSD.

### 2.3 Attack 3: the direction of the divisibility

- KK Thm 3.6(2): **(L_p^∓) ⊆ char_Λ(Sel^±(Q_∞,E[p^∞])^∨)** for non-CM E with ρ̄ = E[p] surjective (Kato's Euler system via [Kob03 Thm 4.1] and [Kat04 Thm 17.4(3)]).
- PR04 intro: "the characteristic power series of the Pontryagin dual of Sel_p^±(E/Q_∞) divides 𝓛_E^±."
- So **char(X) ∣ L**, i.e. (L) ⊆ char(X). This is the Euler-system upper bound on Selmer, and it is exactly the direction the criterion needs:

      (L_p^+) = (X²·unit) ⊆ char(X⁻)  ⟹  char(X⁻) ∣ X².

- The divisibility holds **in Λ, integrally**; KK state it in Λ. It needs the residual image hypothesis: for p ≥ 5, ρ̄ surjective implies the p-adic image contains SL₂(Z_p). Without integrality a μ-factor p^μ could hide in char(X⁻) and allow a finite Sha[p]. **The seed satisfies this:** it is non-CM (j ∉ Z) and ρ̄_p = GL₂(F_p) for every odd p (merged upstream; not re-audited here).
- **The ideal (L) = (X²) is invariant** under the involution γ ↦ γ⁻¹ and under a change of the generator γ (X ↦ uX + …). So convention differences there cannot matter.

### 2.4 Attack 4: control to Q

- Sel^±(Q_n) at n = 0 **is** the classical Sel(E/Q,E[p^∞]).
- The level-0 map is injective (always) with finite cokernel, and it is an isomorphism if p ∤ Tam(E) (KK Thm 3.9; PR04 Lemma 8.3 in the CM case).

| hypothesis | seed at p = 23, 29, … | used? |
|---|---|---|
| p good supersingular | ✓ | yes |
| a_p = 0 | ✓ (automatic for p ≥ 5) | yes (the whole ± theory) |
| p ∤ Tam | ✓ (Tam = 16) | **not needed** (see below) |
| residual image | ✓ | only for the integral divisibility (2.3) |

**Why p ∤ Tam is not needed.** The argument uses **only injectivity**:
- the rank bound in 2.2;
- the surjection (X⁻)_Γ ↠ Sel(E/Q)^∨ in 2.6, which is the dual of an injection.

### 2.5 Attack 5: the no-finite-submodule step, and the Λ/(X²) versus (Λ/X)² trap

**B.D. Kim's theorem, as restated verbatim by Kitajima–Otsuki Thm 1.1:**
- F₀ is a finite extension of Q in which p is unramified; E is defined over Q; a_p = 0.
- (1) If Sel⁻^∨ is Λ-torsion, it has no nontrivial finite Λ-submodule.
- (2) The same holds for Sel⁺ if moreover p splits completely in F₀.
- For F₀ = Q both parts apply. Cotorsion holds by KK Thm 3.4. **There is no Tamagawa, residual-image or level hypothesis.**

**The step, given char(X⁻) = (X²).**
- The structure theorem gives a pseudo-isomorphism X⁻ → E with E = Λ/(X²) or (Λ/X)². There is no p-power part, since char has no p factor.
- Its kernel is a finite submodule, hence 0 by B.D. Kim. So X⁻ ↪ E with finite cokernel.
- **Case Λ/(X²):** a finite-index submodule M of Λ/(X²) ≅ Z_p·1 ⊕ Z_p·X has X·M of rank 1 (it contains X·p^k), so rank M_Γ = 1. That contradicts rank (X⁻)_Γ ≥ 2 (2.2). **The trap is avoided.**
- **Case (Λ/X)²:** X acts as 0, so X⁻ is a finite-index Z_p-sublattice of Z_p². Hence **X⁻ ≅ Z_p² with trivial Γ-action**, and (X⁻)_Γ ≅ Z_p².
- **Without B.D. Kim the conclusion would fail.** X⁻ ≅ Z_p² ⊕ F with F finite would allow Sel(E/Q)^∨ ≅ Z_p² ⊕ (finite), i.e. a finite nonzero Sha[p^∞]. The theorem is load-bearing, and it is available.

### 2.6 Attack 6: the Sha conclusion

- The dual of the injection Sel(E/Q) ↪ Sel⁻(Q_∞)^Γ is a surjection (X⁻)_Γ = Z_p² ↠ Sel(E/Q)^∨.
- The target has Z_p-rank ≥ 2, so the kernel has rank 0. Since Z_p² is torsion-free, the kernel is 0.
- So **Sel(E/Q,E[p^∞]) ≅ (Q_p/Z_p)²**.
- E(Q) ⊗ Q_p/Z_p ≅ (Q_p/Z_p)² is a divisible subgroup of full corank, so it is everything. Hence **Sha(E/Q)[p^∞] = 0**.
- The torsion E(Q)[p] = 0 is not needed at this point; it is only used for injectivity.

### 2.7 Attack 7: the mod-p coefficient test

- Mod p, ω₁ = (1+X)^p − 1 ≡ X^p, so Λ/(p, ω₁) = F_p[X]/(X^p).
- For p ≥ 5 the coefficients of X⁰ … X^{p−1} of L_p^+ mod p are those of u·θ₁ (u a unit). The correction ω₁·h changes the X² coefficient by p·h₁ + C(p,2)·h₀ ≡ 0.
- By 2.2, X² ∣ L_p^+ exactly, so L_p^+ = X²·g with g(0) ≡ u·c₂ (mod p).
- **c₂ ≢ 0 ⟹ g ∈ Λ^×**, so (L_p^+) = (X²), so char(X⁻) ∣ X².
- With ord_X ≥ 2 this gives **char(X⁻) = (X²)**, with no extra factor, μ or λ. **Knowing θ₁ mod ω₁, and even mod p, suffices.**
- **Forced self-checks:** c₀ = 0 exactly (it equals −(p−1)[0]⁺ and L(E,1) = 0), and c₁ ≡ 0 (mod p).

### 2.8 Attack 8: depth

KK: θ₁ is the image in Λ₁ = Z_p[Gal(Q₁/Q)] (Q₁ ⊂ Q(μ_{p²})) of Σ_{a∈(Z/p²)^×/±1}[a/p²]⁺σ_a. **Only denominators p² occur: depth 2.** Explicitly, with γ the image of 1 + p:

    c_k ≡ u · Σ_{a∈(Z/p²)^×} [a/p²]⁺ · C(j(a), k)   (mod p),   j(a) ≡ −(a^{p−1} − 1)/p (mod p)   (Fermat quotient)

These are the same weights as Lane 3's depth-2 X_p; the labelling a/ω(a) ≡ (1+p)^{j(a)} (mod p²) was re-verified in the validation. The seed's cusps b/p² are Γ₀(N)-equivalent to 0 (gcd(p², N) = 1), so the arbcore msl mode applies unchanged (m = p², Q = N, s = w = +1).

### 2.9 Attack 9: normalisation, Manin constant, identification

- Any period normalisation that differs from the Néron one by a p-adic unit gives the same verdict. This includes x_b = Re λ/ω₁ (= 2·[·]⁺_Néron for Δ > 0) and the curve-versus-newform factor c_E, since p ∤ c_E for good p ≥ 5 (Mazur: p ∣ c ⟹ p² ∣ 4N).
- p-integrality of the symbols: λ(b/p²) ∈ Λ_f because b/p² ~ 0 and L(E,1) = 0, and c_EΛ_f ⊆ Λ_E. So x_b ∈ (1/c_E)Z ⊆ Z_(p).
- **Exact identification needs an explicit denominator bound.** For the seed this is the existing c_E ∣ 512 (v₂(c₀) ≤ 8 and 4547 ∤ c₀), i.e. LATDEN 1024, the same theorem input as the p = 3 and p = 5 runs.
- **Full residual image** supplies the integral divisibility (2.3) and ρ̄ irreducible (KK's integrality of θ_n and L_p^±). **The seed's existing inputs suffice.**

## 3. Corrections to F2 §B.1

1. **(C1) Congruence constant.** θ₁ ≡ u·L_p^+ (mod ω₁) with a p-adic unit u (u = −½ in KK's literal conventions), not "exactly θ₁ ≡ L_p^+". This does not affect the criterion.
2. **(C2) p ∤ Tam(E) is superfluous.** Only injectivity of the level-0 control map is used. It is harmless for the seed (Tam = 16).
3. **(C3) Sign labels.**
   - Pollack's L_p^+ (odd-layer interpolant) pairs with **Kobayashi's X⁻** in KK's conventions (Thm 3.6(2); "[Pol03] = −[Kob03]"). PR04 write the same pairing as Sel^+ ↔ 𝓛^+ in their own labels.
   - F2's text is consistent with KK.
   - **The argument is sign-symmetric:** control injectivity at n = 0, cotorsion, B.D. Kim and the rank bound hold for both signs. So the label cannot break it. Cite KK Thm 3.6(2) for the pairing.
4. **(C4) Hypotheses must be explicit:**
   - p ≥ 5 good supersingular (a_p = 0 automatic);
   - E non-CM with ρ̄_p surjective (for integrality; CM would instead use the PR04 main conjecture);
   - rank E(Q) = r known **exactly**, with r ≤ p − 1;
   - symbols identified exactly under an explicit denominator bound.
5. **(C5) Cost.** F2's "≈ 120 CPU-h at 23, ≈ 190 at 29" uses the old floating-point cost model. With the rigorous pipeline the exact truncations are T_min(m = 529) = **176 282 761 626** and T_min(m = 841) = **282 833 232 031** (`arbcore tmin`, LATDEN 1024; `work/tmin_ss_seed.txt`).
   - Calibrated model: ≈ 270 CPU-h (p = 23) and ≈ 460 CPU-h (p = 29), about 500 CPU-h in one shared pass.
   - Witness files (≈ 200–310 GB) **cannot be kept** on this disk (131 GB free). The run would need KEEP_WIT = 0 with hash retention; the a_q files alone take ≈ 30–45 GB.
6. **(C6) Semi-decision.** c₂ ≡ 0 (mod p) proves nothing. The fallbacks are θ₂ ≡ Φ₁(1+X)·L_p^- (mod ω₂), which has depth 3 and needs a different coefficient analysis, or a ± main conjecture (unpublished for non-square-free N).

## 4. Small validation (Sage/eclib exact symbols; 5.5 CPU-s; consistency only)

`work/ss_validation.sage` and its output.

| curve | p (a_p = 0) | rank | ρ̄_p surj. | Sha_an | c₀ (exact) | c₁ mod p | c₂ mod p | reading |
|---|---|---|---|---|---|---|---|---|
| 446d1 | 19 | 2 | yes | 1 | 0 | 0 | **6** | criterion applies (Sha[19^∞] = 0) |
| 446d1 | 61 | 2 | yes | 1 | 0 | 0 | **20** | applies |
| 389a1 | 107 | 2 | yes | 1 | 0 | 0 | **86** | applies |
| 571b1 (contrast) | 17 | 0 | yes | 4 (2-part) | −64 ≡ 4 | — | — | rank-0 analogue (c₀ ≢ 0) applies |

- In every rank-2 case the forced pattern (c₀ = 0, c₁ ≡ 0) followed by a nonzero c₂ is observed.
- A wrong parity (a Φ₁ factor) would force c₂ = 0, so the parity claim is tested non-trivially.
- The results agree with Cremona's Sha_an.

## 5. Remaining provenance issues

| # | item | status |
|---|---|---|
| P1 | Pollack, Duke 118 (2003), Prop 6.18 in the original | unread (fetch failed on a certificate error). Used via KK Prop 1.11. **The n = 1 case is re-derived here** from PR04 (10)–(12), which were read |
| P2 | Kobayashi, Invent. 152 (2003): Thm 4.1 (divisibility), Thm 7.3 (cotorsion), Thm 9.3 / Lemma 9.1 (control) | unread (no free copy found). Used via KK Thms 3.4, 3.6(2), 3.9 and the PR04 introduction |
| P3 | B.D. Kim, J. Aust. Math. Soc. 95 (2013), Thm 1.1 | unread in the original. Used via its verbatim restatement in Kitajima–Otsuki Thm 1.1 (read) and KK Thm 3.8 |
| P4 | Kato 2004 Thm 17.4(3) (integral divisibility under a large image) | cited through KK and Kobayashi |
| P5 | KK arXiv v3 versus IMRN print | not compared |
| P6 | seed inputs at p = 23, 29: ρ̄_p surjective; rank 2 exactly; c_E ∣ 512 | upstream (merged); not re-audited here |

## 6. Answers to the six questions

1. **The theorem that survives.**
   - *Setting.* Let E/Q be non-CM, p ≥ 5 a good supersingular prime with ρ̄_{E,p} surjective, r = rank E(Q) ≤ p − 1, and θ₁ ∈ Z_(p)[Gal(Q₁/Q)] the Mazur–Tate element of [a/p²]⁺. Write θ₁ mod p = Σ c_kX^k in F_p[X]/(X^p) (γ ↦ 1+X).
   - *Hypothesis.* c₀ ≡ … ≡ c_{r−1} ≡ 0 (automatic) and **c_r ≢ 0 (mod p)**.
   - *Conclusion.* L_p^+ = X^r·unit, char(X⁻) = (X^r), X⁻ ≅ Z_p^r (trivial Γ-action), Sel(E/Q,E[p^∞]) ≅ (Q_p/Z_p)^r, and **Sha(E/Q)[p^∞] = 0**.
2. **Sign and parity.**
   - θ_n ≡ ω̃_n^∓L_p^∓ (mod ω_n) for n even/odd, so **n = 1 gives L_p^+, the odd-layer interpolant** (PR04 (10), (12): χ₀(L^+) = (p−1)L(E,1)/Ω_E), with ω̃₁^+ = 1.
   - L_p^+ pairs with Kobayashi's Sel⁻ (KK Thm 3.6(2)).
   - With KK's literal normalisation, θ₁ = −½L_p^+ (mod ω₁).
3. **p = 23 and p = 29:** **yes**, both become finite-certificate candidates (per p, SEMI). Cost ≈ 270 / 460 CPU-h with the rigorous pipeline, or ≈ 500 CPU-h shared. Witnesses cannot be retained on this disk. **Not run.**
   Larger supersingular p (131, 167, 281, …) are valid in principle, but T scales like p² (T ≈ 7.8·10⁹·p²/25, ≈ 5·10¹² at p = 131), so each costs ≳ 10⁴ CPU-h. They are not practical candidates on this host.
4. **Depth 2 suffices:** **yes.** θ₁ uses only [a/p²]⁺, and the congruence has no cyclotomic factor at n = 1.
5. **A successful bit proves Sha[p^∞] = 0:** **yes.** A certified c₂ ≢ 0 (mod p), from exactly identified symbols, gives Sha(E/Q)[p^∞] = 0 via published theorems only: Pollack/KK, Kato–Kobayashi one-sided divisibility, Kobayashi control, B.D. Kim. **No main-conjecture equality, BSD, or p-adic BSD is needed.** A failed bit proves nothing.
6. **Remaining provenance:** P1–P6 above. The logical chain is closed. The open items are unread originals behind faithful restatements and upstream seed inputs.
