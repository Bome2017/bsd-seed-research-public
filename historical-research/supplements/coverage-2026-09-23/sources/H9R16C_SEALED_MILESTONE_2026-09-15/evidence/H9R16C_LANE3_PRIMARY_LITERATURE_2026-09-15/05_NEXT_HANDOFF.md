# 05 — Next handoff (Lane 3 → coordinator and lanes 1, 2, 4), revision v2

## To the coordinator

- **EXISTING_THEOREM_CLOSES_C = NO.** No printed theorem states C or directly implies it.
- **Nearest structural precedent: Howard 2007 §2.2** — twisted fixed-base point module,
  corestriction, twisted Kummer map, Albanese transition, Lemma 2.2.4. His point-level transition
  comes from CM moduli, which Chow–Heegner points lack.
- **Formal part.** 03 §2 (F1–F4): Kummer naturality for finite-level MRS twists over K_0, and
  Shapiro/norm compatibility for Weil restriction. The square commutes for
  τ_r^et := T_p(τ_r^MW), read through Shapiro where needed.
- **Settled by reference (upgraded after your input, verified locally).** The étale compatibility of
  the modified pairing along the tower: KLZ17 Thm 7.2.3(v), the proof of Prop 10.1.1, Rem 7.4.1 and
  Lemma 7.4.2 (via Oht00). **Scope correction:** BSV22 (109) is fixed-level (Np), integer-weight
  specialization only.
- **Remaining unprinted, expected formal:** E′ (dagger / group-ring packaging of the A_r-contraction)
  and D4 (finite-level Abel–Jacobi identity), both in 04; plus normalization transport N1–N4.
- **Cheapest next source:** Ohta 2000 (Math. Ann. 318, 557–583) for the finite-level pairing formula
  and its sign. Also still missing: Ohta 1995 (Crelle 463) and BCPV's companion [BCS] §2.1 (for N1).

## To Lane 1 (BCPV W vs Hida w)

- **Normalization now pinned (KLZ17 convention):** cohomology side W_{Np^r}^{-1}∘(U'_p)^r; forms
  side U_p^r∘W_{Np^r}^{-1}; Ohta's τ_r = W_{Np^r}^{-1} up to signs (KLZ17 Rem 7.4.1, Lemma 7.4.2,
  proof of Prop 10.1.1). **Consistency:** the two operator orders agree via BSV22 (114), since
  w_{Np} intertwines U'_p, T'_ℓ, ⟨d⟩ with U_p, T_ℓ, ⟨d⟩^{-1}.
- **Moduli definition:** KLZ17 Def 2.5.4 (point model, over Z[1/N, ζ_Q]). Relations: Def 2.5.2
  (W_Q^2, diamond conjugation, W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'}) and Rem 2.5.3 (Atkin–Li). BCPV's W is
  plausibly this operator (N1, not printed in BCPV).
- **Galois twists, per convention:** HidaC §6 / HidaL §5 w_r^σ = ⟨z⟩w_r (μ-model); Ohta (4.2.4);
  Cais Prop 2.3.6; KLZ17 Rem 2.6.1 (forms, point model).
- **Degeneracy interchange:** Cais Prop 2.3.6 (ρw_{r+1} = w_rσ; σw_{r+1} = ⟨p⟩_N w_r ρ); proof of
  KLZ17 Prop 10.1.1 (W_{Np}pr_1^* = pr_2^*W_N; W_{Np}pr_2^* = p^k pr_1^*W_N); proof of BSV22
  Lemma 6.1 (w_N pr_p^* = ⟨(p,1)⟩pr_p^* w_N).
- **p-part vs full level:** BSV22 (65)–(68) — U_p w_p = w_p U'_p ⟨p⟩_N, but U_p w_{Np} = w_{Np} U'_p.
  So the full-level W intertwines U_p and U'_p with no tame diamond.
- **Model dictionary:** printed only Λ-adically (KLZ17 Thm 7.2.3 proof: twist by 1+k+ε_N).

## To Lane 2 (the C2 square)

- **Formal:** F1–F4 (03 §2). Then write E′(a), E′(b) and D4 (04). Each looks formal from DR22 (2.17)
  and Lemma 2.8, BCPV (4.1), (4.7)–(4.9), Def 4.6, Cor 4.11, and KLZ17 Prop 7.2.1(1),(4) and
  Thm 7.2.3(v).
- **Recommended τ_r^MW := s_r ⊗ Alb(ϖ_1)** in the point model, U'_p-normalized on p-completed
  ordinary parts. This avoids hazard T9.
- **Keep the three components of s_r separate** (T2): Galois-direction norm (F3), diamond-direction
  summation (F2(4)), and the modular ϖ_{1,*}.
- **MRS twists exist only at finite level** (T3).

## To Lane 4 (checks to run against C)

- **T9:** is π^{sr} paired with BCPV's τ^et without the w_s twist?
- **T2:** is s_r called a "corestriction"?
- **T6:** is an integral tower built inside old-form subvarieties? That limit is 0 by HidaC Prop 6.4.
- **T7:** BCPV's W_{Np^r} (common tame level) vs W_{N_g p^r} (native).
- **E′(a):** does the contracted class carry exactly the ⟨χ⟩^{-1/2} factor-1 dagger, or an extra
  twist coming from W or from the Z_p[Δ]-valued pairing?
- **D4:** is it invoked only after specialization (BCPV Lemma 4.18 scope)?
- **BSV22 (109) scope:** is it cited for p-power-level compatibility? It covers fixed level only.
- **Citations:** BCPV L4.10 → DR22 **L2.4** (arXiv v1); BCPV (1.8)–(1.9) → Ohta (1.5.4) is about forms
  only; BCPV's BSV22 passage contains no W in the consulted version.

## Sources not consulted

- Ohta 2000 (Math. Ann. 318) — paywalled; the finite-level formula and sign.
- Ohta 1995 (Crelle 463) — paywalled.
- Milne 1972 — download not approved; F3 is derived inline.
- BCPV's companion [BCS].
- Published versions of DR22 and BSV22 (Astérisque 434), HidaC (PROMS 188), HidaL (Doc. Math.).
- FK12 §1.7.16; AL78 Prop 1.4–1.5; MW84 II §5 and 2.5.6; MW86 p.237.
- The unnamed "recent exposition" relayed in the operator note (unverified).
- Longo–Vigni 0903.2797 and Hida's MWCT slides were downloaded and scanned but not relied on.

## Custody

- Sources: `_work/sources/` with pdftotext `.txt` beside each. Hashes: 06.
- Ohta 1999: the user-supplied iCloud copy; its hash matches the original.
- Raw notes: `_work/NOTES_LEDGER_PART1..4.md`. Part 4 records the operator input and its verification.
- The local H5–H9 checkpoint text was read for context only (not a repair source, per the operator).
  All frozen statuses were taken from the lane prompt.

## Addendum (post-verification)

- **Lane 4:** KLZ17 Thm 7.2.3(v) is stated on *parabolic* ordinary cohomology, and the Nov 2023
  correction (KLZ17 §13) sharpens what "cuspidal branch" means. Confirm (Irr) for the actual CM
  g-family at p. Otherwise M(g)^*_par ≠ M(g)^* is possible, and the pairing input must be rechecked.
  Under (Irr), as BCPV assume, nothing changes.
