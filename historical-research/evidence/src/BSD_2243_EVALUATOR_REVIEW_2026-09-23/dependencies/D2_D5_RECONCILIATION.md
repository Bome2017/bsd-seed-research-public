# D2 and D5 for the 2243 certificate, reconciled against the sources already on disk (2026-09-23)

## Scope and sources

**Certificate** (S1, sufficient direction only): K ≢ 0 (mod 2243) ⟹ Sha(E/Q)[2243^∞] = 0, with K = 1024·Z the depth-two coefficient a_{2,3} (SW normalization). Nothing is claimed if K ≡ 0.

**Sources** (read-only). Abbreviations:
* **SK** = `…/audits/p3_r1_r2_2026-09-19/sources/Skinner2016_published.txt`, Skinner, *Multiplicative reduction and the cyclotomic main conjecture for GL2*, PJM 2016.
* **J89** = `…/sources/Jones1989_extra_zeros_reading_order.txt`, Jones, *Iwasawa L-functions for multiplicative abelian varieties*.
* **SW** = `…/p11/aristotle_handoff/ARISTOTLE_C11_RESULT/sources/SteinWuthrich2013_shark.txt`, Stein–Wuthrich, Math. Comp. 2013.

The first two live under `/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19`.

The master record's own freshness check was run first. The result was RECONCILIATION_REQUIRED, listed in §4. This document changes no claim in the master record.

## D2: the extra T factor, char(X_Gr) = T · char(X_cl) at p = 2243 (split)

**What SK proves.**
* **Definitions** (§2.3, SK l.424–437 and l.533–551). M = T_f ⊗ Λ*_O with M⁺ ⊂ M, and Σ = {p}.
  * **Greenberg Selmer group:** Sel_{Q∞,L}(f) = ker( H¹(G_S, M) → H¹(I_p, M⁻)^{G_{Q_p}} × ∏_{ℓ≠p} H¹(I_ℓ, M)^{G_{Q_ℓ}} ).
  * **S:** the kernel of the stricter map (2-3-2), to H¹(Q_p, M⁻) × ∏_{ℓ≠p} H¹(I_ℓ, M)^{G_{Q_ℓ}}. X is its dual, and it is independent of the auxiliary S.
* **The extra factor** (§3.2, l.1192–1228). By Proposition 2.3.2 there is an exact sequence 0 → S → Sel_{Q∞,L}(f) → H¹(F_p, (M⁻)^{I_p}) → 0.
  * The last term is 0 unless α_p = 1 (split multiplicative), in which case it is L/O with trivial Γ-action.
  * Hence **Ch_L(f) = (γ − 1)·Ch_L(f)′ in the split case** (l.1217–1221), where Ch′ is the characteristic ideal of X.
  * With Theorem A, (L_f) = Ch_L(f), so L_f = (γ − 1)·L′_f and Ch′ = (L′_f) (l.1224–1228).
* **Hypotheses used by this step.** Proposition 2.3.2 (l.559–560) needs k ≡ 2 (mod p − 1), ρ̄ irreducible, and X_{Q∞,L}(f) torsion; the last comes from Theorem A.
  * Theorem A (l.67–74) needs p ≥ 3, ordinary, (i) k ≡ 2 (mod p − 1), (ii) ρ̄ irreducible, (iii) some q ∥ N with q ≠ p and ρ̄ ramified at q.
  * For E at 2243: k = 2; ρ̄ irreducible and (iii) with q = 3 or 5843 were verified in S1 (D1).
  * **The ℒ ≠ 0 hypothesis (Theorem B (iii)) is not used by this step.** It enters only in Theorem B's special-value formula (l.1229 on).

**Matching Skinner's S with the classical Selmer group** (the f_E of SW §6.1, l.1048–1073, defined with the Kummer conditions H¹(nQ_v, E) at every place):
* **At p (split multiplicative):** the Tate uniformization gives 0 → μ_{p^∞} → E[p^∞] → Q_p/Z_p → 0, i.e. M⁺ ↔ μ_{p^∞} and M⁻ ↔ Q_p/Z_p with trivial action.
  * For every finite K/Q_p, the Kummer image of E(K) ⊗ Q_p/Z_p = (K^×/q^Z) ⊗ Q_p/Z_p is the image of H¹(K, μ_{p^∞}) = K^× ⊗ Q_p/Z_p.
  * By the long exact sequence this image equals ker( H¹(K, E[p^∞]) → H¹(K, Q_p/Z_p) ). This is exactly Skinner's strict condition. Both groups are divisible, so they agree exactly, not just up to finite index.
  * The same holds in the direct limit over Q∞,p.
* **At ℓ ≠ p:** Q∞,v is the unramified Z_p-extension of Q_ℓ.
  * Gal(Q_ℓ^{ur}/Q∞,v) ≅ ∏_{q≠p} Z_q has no p-cohomology, so H¹_ur(Q∞,v, E[p^∞]) = 0.
  * The Kummer image E(Q∞,v) ⊗ Q_p/Z_p is 0 because ℓ ≠ p. Skinner's unramified condition (the kernel to H¹(I_ℓ, M)^{G_{Q_ℓ}}) and the classical condition are therefore both "locally trivial".
* **Elsewhere:** outside S the conditions are automatic, since G_S cohomology is unramified there; p is odd, so the archimedean place imposes nothing.
* **Lattice:** T_f = T_p E. Because ρ̄ is irreducible, Skinner's objects do not depend on the lattice (Lemma 2.1.1, l.445–450).

**Verdict D2: DISCHARGED at source level.** With X_Gr = X_{Q∞,L}(f) and X_cl = X = Sel_p(E/Q∞)^∨, SK §3.2 gives char(X_Gr) = T·char(X_cl) for split p = 2243 (T ↔ γ − 1). The inputs are Skinner's published Theorem A and Proposition 2.3.2 plus the standard local identification above. The identification is short and is written out here for independent checking; it is not quoted from a single theorem.

**By-product, an attribution correction.** SW §6.1 (l.1068–1070) credits Λ-torsion of X in the *multiplicative* case to Kato [Kat04, Thm 17.4]. SK (l.75–79) states that the case p | N "is excluded from Kato's divisibility theorem [2004, Theorem 17.4]". At 2243, torsion comes from Skinner's Theorem A (Ch_L(f) = (L_f) ≠ 0), not from Kato.

## D5: is an independent nonzero split-height certificate necessary?

**The two dependency choices.**

**(a) As in the pilot notes (S1).** Jones's Theorem 3.1 in the forward direction, plus an independent certificate that the height is nondegenerate.

**(b) SW Theorem 6.1** (l.1078–1088): ord_{T=0} f_E ≥ r, "equal to r if and only if the p-adic height pairing is nondegenerate … and X(E/Q)(p) is finite". SW attributes "the multiplicative case" to Jones [Jon89] (l.1074–1075). If (b) is admissible, the certificate's own order computation supplies nondegeneracy and D5 disappears. The chain would be:
1. ord L_p = 3 exactly: from Theorem A and D2 (ord ≥ r + 1 = 3), plus the certificate (T³ coefficient a unit).
2. Hence ord f_E = r = 2.
3. Hence, by (b), the height is nondegenerate and Sha(p) is finite.

**What the cited primary source J89 actually contains.**
* **Standing Hypothesis 1: "Ш_{p^∞}(K) is finite"** (l.112–113). It is used in the very definition of the height pairing (l.240–242: "Since we assume that the p-primary component of Ш_K is finite …"). J89 therefore never yields Sha finiteness.
  * That half of (b) is anyway available independently: the elementary control argument recorded as D4 in S1 gives corank Sel_p(E/Q) ≤ ord f_E.
* **Theorem 2.1** (l.293–294): the pairing is nondegenerate **iff α and g are quasi-isomorphisms.**
  * **Proposition 1.1** (l.177–193) makes "g is a quasi-isomorphism" equivalent to "order of vanishing = Z_p-rank of M^Γ", i.e. semisimplicity at T = 0. With Sha finite and Jones's control, that rank is r.
  * **α's quasi-isomorphism is not obtained from an order computation.** Its cokernel is H²(O_L, A′_{p^∞})^Γ (l.270–276). J89 proves this finite only *from* nondegeneracy (Lemma 2.2, l.302–306), and the remarks in §3.2 (l.860–861) are likewise conditional on nondegeneracy.
* **Theorem 3.1** (l.680–720; split case l.711–720): ρ ≥ r + 1 always, and *if* ⟨,⟩_p is nondegenerate, then ρ = r + 1 and the leading-term formula holds. **The converse ρ = r + 1 ⟹ nondegenerate is not stated anywhere in J89.** The whole text was read: §§1–3, Propositions 3.5–3.6, Corollary 3.7.

**Verdict D5: NECESSARY at the retained grade, unless the project changes that grade explicitly.**
* **SW 6.1's multiplicative "iff" is secondary-source packaging.** Its cited proof (J89) establishes only the forward direction, and α's quasi-isomorphism is left conditional. The same SW paragraph misattributes multiplicative torsion to Kato 17.4.
* **The retained practice points the same way.** The 3-primary theorem, also at a multiplicative prime (p = 3, non-split), supplied an independent nondegenerate-height certificate (F1 CP-E) rather than importing an "iff".

**Ways to discharge D5, in increasing order of cost and uncertainty:**
1. **An independent computation.** The extended split height regulator at 2243 must be nonzero, by a second code path independent of PARI's `ellpadicheight` / `ellpadicregulator`. For example: the Tate-curve p-adic σ function (product formula) with Werner's correction, plus the away-from-p contributions, mod p³, for the two generators. PARI already gives det ≡ 2181·p² ≢ 0 (mod p³).
   * The cost is a few hours of implementation and validation. Validation would use the S1 calibration curves 446d1 at p = 223, 655a1 at p = 131 and 707a1 at p = 101.
   * The computation takes seconds.
2. **A source lemma.** Show α is a quasi-isomorphism for this E, i.e. H²(O_L, A′_{p^∞})^Γ is finite, from Λ-torsion of X (a weak-Leopoldt-type statement for Jones's fppf cohomology).
   * The converse would then follow from J89 Theorem 2.1 and Proposition 1.1, with Sha finiteness supplied by D4.
   * This is research-grade and was not attempted here.
3. **A grade decision (yours).** Import SW Theorem 6.1 "as published" for the split case, recording the attribution gap above as a qualification.

## Other dependencies (unchanged by this reading)

* **D1** (Skinner Theorem A hypotheses): verified in S1, imported as published.
* **D3** (canonical versus Néron/Gross periods at p ∣ N): as at p = 3; "Skinner as published", with internal SU provenance open at the Euler-removal interface (master §2).
* **D4** (finiteness first): elementary; now also covers the Sha half of any "iff".
* **D6** (J89 Theorem 3.1, forward direction, split clause): read. Its hypotheses 2–4 hold. Hypothesis 4 is log_p q ≠ 0, satisfied since ℓ_γ(E) ≡ 1799 ≢ 0 (mod 2243). Hypothesis 1 is supplied by D4.
* **D7** (SW Proposition 3.5 and the lattice): read in S1.
* **D8** (engine): under independent review, in parallel.

## Master-record status seen while doing this

`verify_master.py` (read-only, run with a local ripgrep) returns **RECONCILIATION_REQUIRED**:
* three `changed_bound_source` entries in `BSD_SEED_P13_RUN_2026-09-21` (another session's run);
* `discovery_scope_changed`: the new BSD_2243_* folders, including a Codex review folder;
* `research_root_set_changed`.

This reading changes no master claim. Updating the master record belongs to an authorized reconciliation and was not done here.
