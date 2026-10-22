# Fable coordinator's cross-model check of R25 (Opus worker): T_INT_PROVED_MODULO (2026-09-29, 19:30)

**Verdict: CONFIRMED_WITH_QUALIFICATIONS.** R25's own derivations (D1–D7) pass my check. No step is refuted, and no
stray power of 3 was found. The chain to #Sha(E/Q)[3^∞] ≤ 9 rests on two inherited inputs, listed in §4, that R25
labels honestly. It is NOT yet a closed proof of S.3; it is the best route on record and uses no Skinner, no
Skinner–Urban and no GRH.

## 1. Integrity and replays
- MANIFEST 23/23 OK. Task bundle unchanged.
- `checks/coleman_family.gp` replayed from a scratch copy: IDENTICAL output (`checks/coleman_family_replay.log`),
  including the two negative controls B3/B4 (min v₃ = −8, as they must fail).
- K-R25c (289 rank-0 curves) not replayed: at rank 0 the equality is tautological (sha_an is defined from L/Ω), so it
  only tests the constant-term normalization 2·L(E,1)/Ω, which K-R25b already fixes.

## 2. Kato citations checked at source (`Kato2004_AST295.txt`, R23 bundle)
- **12.5(4)** (l.5719–5739): assumes p ≠ 2 and (12.5.2); gives Z(f,T) ⊂ H¹(T) and length(H²(T)_𝔭) ≤ length(H¹(T)_𝔭/Z(f,T)_𝔭)
  for ANY height-one prime 𝔭 (so (3) is included: the μ-part is covered), "unless f and 𝔭 satisfy (12.5.1)". (12.5.1)
  needs length(H²_loc_𝔭) = 1. At nonsplit 3, H²_loc(T) = H⁰(Q₃(μ₃∞), E[3^∞])^∨ = 0 (my hand check: η stays nontrivial
  on the totally ramified tower, so 2x = 0 forces x = 0 on both graded pieces). No exception. ✓
- **12.4(2)** (l.5677): H¹(T) torsion-free, H¹(T)⊗Q free of rank 1. ✓ (used for injectivity, (17.13.2)).
- **17.10** (l.8417–8464): Prop 17.2 is stated for good ordinary reduction, but its ℓ ≠ p step is verbatim "lim C_ℓ^n = 0
  since H¹(Z_ℓ⊗Z[ζ_{p^n}], ·) = H¹(F_ℓ⊗Z[ζ_{p^n}], ·) and the p-cohomological dimension of ∪_n F_ℓ(ζ_{p^n}) is zero"; the
  only reduction input is the final p-step via Lemma 17.9, which R25 replaces. ✓ So the Selmer group in the limit is
  primitive at 5843 (strict = unramified = 0 there). The (1 + 5843⁻¹) factor belongs to a Σ-imprimitive group route K
  never uses. ✓
- **17.13** (l.8583–8640): the template is (14.9.3) + (17.10.1) → (17.13.1); (17.13.2) via 12.4 and the rank of Z(f);
  (17.13.3) via 17.9; (17.13.4) via 12.5(3); then 17.11 + 12.5 + 16.6 for the Coleman isomorphism at each 𝔭. R25 swaps
  exactly the three good-ordinary inputs (17.9, 17.11/17.12, 16.6) and keeps the rest. ✓
- **17.4** (l.8265): stated only for good ordinary reduction, as B1 said. R25 is a reconstruction, not a citation. ✓
- **(12.5.2) at p = 3:** on record from R24 (`R24_SRC_Elkies_rho3.md`): ρ₃ surjective via Elkies's X₉, grade COMPUTED
  with two SECONDARY completeness facts. Not re-derived here.

## 3. R25's new lemmas, hand-verified
- **D5 Step 1.** (a) H²_Iw(T⁰) = H²_Iw(T/T⁰) = 0: as above. (b) Tate pairing H¹(k_n,T⁰) × H¹(k_n,Z₃(η)) → Z₃ is perfect:
  (T⁰)^∨(1) = Z₃(η), and both H¹ are torsion-free since the H⁰ of the divisible modules vanish. (c) Kummer
  Ê(m_n) ≅ H¹(k_n,T⁰): injective, equal Z₃-ranks 3^n, torsion-free cokernel ⇒ 0. (d) Cohomologically trivial +
  Z₃-free ⇒ Z₃[Γ_n]-free of rank 1; a generator is detected by its norm to level 0. (e) log Ê(3Z₃) = 3Z₃ (p odd) and
  log c₀ = 3/2 has v₃ = 1 ⇒ c₀ generates. Hence Col_n is an isomorphism and Col : H¹_Iw(T)/H¹_Iw(T⁰) → Λ is an
  isomorphism. ✓ (Consistent with the general fact: the twisted Coleman cokernel is Z₃(η)_{Frob} = Z₃/2 = 0.)
- **D6 (a2).** dim H¹_f(K_n,V) = [K_n:Q₃] = dim H¹(K_n,V⁰); the image of H¹(K_n,T⁰) is saturated in H¹(K_n,T) because
  H¹(K_n,T/T⁰)_tors = H⁰(K_n,Q₃/Z₃(η)) = 0; so H¹_f(T) = im H¹(T⁰) exactly, and by BK 3.8 the classical local condition
  at 3 is Greenberg's. ✓ (a3) injectivity: a nonzero map from a rank-1 torsion-free module has torsion kernel = 0. ✓
- **D8 step 4–5.** E(Q(μ₃∞))[3] = 0 from (12.5.2); corank ≥ 2 ⇒ ord_T f_E ≥ 2; T² | f_E | L₃ forces a₀ = a₁ = 0 exactly and
  v₃(g(0)) ≤ v₃(a₂) = 2. ✓
- **The χ ↔ χ⁻¹ convention** (R25's item 4): a uniform mismatch is the Λ-involution T ↦ (1+T)⁻¹ − 1, which preserves
  divisibility and the leading T² coefficient. It cannot change the bound. ✓

## 4. The inherited inputs, now checked (19:45 update)
1. **Jones 1989 Thm 3.1: READ AT SOURCE.** The author's own copy (`sources/jones_extra_zeros.ps`, hobbes.la.asu.edu,
   "Iwasawa L-functions for multiplicative abelian varieties"; PostScript, pages reversed in the PDF). Verbatim:
   - p.1: "Let p ≠ 2 be a prime number and let K be a number field"; "a ≈ b if a/b is a unit".
   - p.6: "S_∞ := Image H¹(O_L, A⁰_{p^∞}) → H¹(O_L − T, A⁰_{p^∞}) … quasi-isomorphic to the classical p-Selmer group";
     "Since we assume that the p-primary component of Ш_K is finite".
   - p.11, Thm 2.7 (pairing ⟨,⟩_γ nondegenerate): ker g/cok g ≈ 𝓛(A)/(log_p κ(γ))^{r+e} · det⟨,⟩_p·Ш_K/(A^fin·Ã^fin) · ∏ m_l.
   - p.17, Thm 3.1: ρ ≥ r + e; if ⟨,⟩_p is nondegenerate then ρ = r + e and L_H^{(ρ)}(1) ≈ 𝓛(A)·det⟨,⟩_p·Ш_K/(A^fin·Ã^fin)·∏ m_l.
   - p.18: "If A is the Néron model of an elliptic curve with non-split multiplicative reduction at p, then ρ ≥ r.
     Furthermore, if ⟨,⟩_p is non-degenerate, then ρ = r and L_H^{(ρ)}(1) ≈ det⟨,⟩_p·Ш_K/(A_{p^∞}(K)·Ã_{p^∞}(K))·∏ m_l";
     proof line: L_H^{(ρ)}(1) = (−log_p κ(γ))^ρ f_S^{(r)}(1). So the T-leading coefficient carries (log_p κ(γ))^{−r}: the
     Reg_γ convention. The pairing is "equivalent to Schneider's analytic height" (p.6, citing his [6]), i.e. Mazur–Tate's.
   - Hypotheses for the seed at 3: p = 3 ≠ 2 ✓; nonsplit multiplicative ✓ (e = 0, 𝓛 = 1); Ш[3^∞] finite ✓ (Kato 18.4, and
     route K itself); ⟨,⟩ nondegenerate ✓ (v₃(Reg_γ) = 0 certified); m_l = c_l, A_{3^∞}(Q) = 0 ✓.
   - Caveat: this is the author's preprint copy, not the Duke 59 (1989) print; numbering could differ.
   - Correction to my first draft: Schneider 1985 II is NOT a substitute; its introduction assumes "A has good reduction
     at all primes of k above p" (`sources/Schneider_1985_II_GDZ.pdf`, p.329).
2. **Height normalization** (D8 step 7). VALIDATED empirically: `checks/rank1_check.sage`, 23 rank-1 curves with 3 ∥ N,
   a₃ = −1: v₃(a₁(L₃)) = v₃(2·sha·Tam/tors²) + v₃(h_PARI(P)) − 1 on 23/23, including 156a1, 228b1, 273a1, where a Tamagawa 3
   cancels a regulator of valuation −1. This is Reg_γ = Reg_PARI/(log₃ κ(γ))^r, the seed certificate's convention
   (v₃(Reg₃) = 2 ⇒ v₃(Reg_γ) = 0), and it matches Jones's (log_p κ(γ))^{−r}. The seed's numbers then read
   v₃(a₂) = 2 = v₃(#Ш[3^∞]) + 0 under equality, and ≤ under route K.
3. Textbook: Tate local duality and Euler characteristic, Nakayama–Rim. Standard.

## 5. Status after §4
Every printed input of the chain has now been read at source by someone in the program (Kato: worker + me; Kobayashi,
SW, Česnavičius: worker; Elkies: R24; Jones: me). S.3's upper half now rests on Kato 2004 (12.4, 12.5(4), 14.9.3, 17.10, 17.13 template), R25's explicit Coleman map, and
a printed leading-term theorem, with no Skinner, no SU and no GRH. With B2 this gives Sha[3^∞] ≅ (Z/3)². What is still missing is a SECOND reader of
R25's derived parts (one cross-model check so far). Grade proposal: S.3 upper half = PROVED_MODULO_SECOND_READER.

## 6. Recommended next
- (Done 19:45) Jones 3.1 read at source; see §4.1.
- A second independent pass on D5 Step 2–3 and D6 (Codex if any credit remains; otherwise a hostile-referee Opus
  session with the two sources only). This is the first time the program has a candidate unconditional proof of the
  3-part's upper bound; it deserves two readers.

FIN, ORDER9 and Q36 are unchanged.

## 7. Corrections after the two independent second readers (21:30; both PASS_WITH_CORRECTIONS)
Readers: `~/BSD_R25_SECOND_READER_RETURN_OPUS_2026-09-29/` (19/19) and `…_OPUS_B_2026-09-29/` (17/17), run blind to each
other and to this file until their T-files were written. Both converge on:
- **C-Kato (a correction to my §2).** The inequality printed in Thm 12.5(4) (p.222, rendered) is for V_{F_λ}(f) and
  Z(f), not for the lattice T; read literally it says nothing at 𝔭 = (3). The integral statement is **Thm 13.4(3)**
  (l.5939–5943, verified here: "length(H²(T)₀,𝔭) ≤ length(Λ_𝔭/J_𝔭) for any prime ideal 𝔭 of Λ of height one", p ≠ 2,
  with H²(T)₀ = Ker(H²(T) → H²_loc(T)) and J the ideal of Z in H¹(T) ≅ Λ). Kato's 13.14 derives 12.5(4) from it. At
  nonsplit 3, H²_loc(T) = 0, so H²(T)₀ = H²(T) and the inequality holds at (3). Its σ-hypothesis needs the 3-adic
  image (12.5.2), supplied by R24's Elkies check; ρ̄₃ = GL₂(F₃) alone would not do. D6(b)'s conclusion stands; the
  citation in D6 and in my §2 should read 13.4(3) via 13.14.
- **C-χ.** No involution is needed: derived directly from Kato 12.5(1) and Stein–Wuthrich §3.2, both sides use the
  same identification of Λ with measures; Kobayashi's two printed χ ↔ χ⁻¹ slips cancel. Kato's own L_p is SW's series
  shifted by κ, not an involution. My "harmless involution" remark in §3 is moot.
- **C-Reg.** Reader A (folder …_OPUS_2026-09-29; Opus's labeling) recomputed the seed's 3-adic regulator on the minimal model with a 3-saturated basis:
  v₃(Reg_PARI) = 2 at precisions 8, 11, 14; hence v₃(Reg_γ) = 0 in the normalization Jones's (log_p κ(γ))^{−r} requires.
  Independent of the release certificate and of my rank-1 test. The ≤ 81 scenario (a (log₃ κγ)² mismatch) is excluded.
- Minor: Dwork's lemma statement drops a unit factor; the Manin-constant step in D7 is not needed.
- No reader found a false step or a stray power of 3. Bound unchanged: #Sha[3^∞] ≤ 9, so Sha[3^∞] ≅ (Z/3)² with B2.

**Status after three readers (Fable cross-model; Opus A; Opus B):** S.3 upper half = written derivation, no Skinner, no
Skinner–Urban, no GRH; checked by three readers, no human review. Inputs it declares: the a_{4,2} certificate, the
height certificate (now independently recomputed), (12.5.2) at 3 (R24), B2.
