# RETURN — Lane B1: upper half of Sha(E/Q)[3^inf] without the SU gap (Fable 5.1, 2026-09-29)

## STATUS: GAP_AT
- **Step.** Argument step 1, first bullet: "Kato at f_m gives L_{f_m} ∈ Ch(f_m)", in the normalization
  that Skinner's congruence L_f ≡ L_{f_m} (mod p^m) uses.
- **Missing statement:** MS-B1 below. Kato proves an integral divisibility for f_m at p = 3, but for a
  p-adically normalized L. The needed comparison with the canonical-period L is in none of the sources read.
- It is not refuted. It is not OBSTRUCTED: no step was shown to need Ch ⊆ (L).
- **Kill tests.**
  - K-B1a: FAIL (a gap, not a refutation).
  - K-B1b, K-B1c: NOT RUN, per TASK.md's rule to stop at the first failure.
  - Argument steps 1–3 were not carried out as a result.

## Collision check: PASS (NOTES.md, "Collision check")
- B1 uses the Kato (upper-bound) direction. That is not the stop register's failed Eisenstein
  lower-bound arrow (STRUCTURAL_STOP_REGISTER l.9–11).
- It reopens neither R1 nor R2, and makes no FIN claim.

## K-B1a — what holds (WORKING_K_B1a.md; Kato read at source from Numdam, sources/)
- **Kato Thm 17.4** (Ka l.8265–8280) needs:
  - good ordinary reduction (17.1: p ∤ N, a_p a unit);
  - for the integral part (3): ω and γ good for one lattice (17.5), p ≠ 2, and (12.5.2), where
    (12.5.2) is the condition image ⊇ SL2(Z_p).
- **Image condition: PASS for every f_m.**
  - (12.5.2) enters only through 12.5(4), proved in §13.14 (Ka l.6345–6350).
  - §13.14 uses it for lattice homothety, for the freeness in 12.4(3), and for Thm 13.4(3)
    (Ka l.5937–5941).
  - Thm 13.4(3) needs σ ∈ Gal(Q̄/Q(ζ_{p^∞})) with Coker(1−σ) free of rank 1, residual irreducibility,
    and p ≠ 2.
  - Skinner's replacement of (12.5.2) by (a) + (b) (Sk l.936–963) is therefore confirmed against
    Kato's own text.
  - For f_m: 3 ∤ M; ρ̄ = GL₂(F₃); 2243 ∥ M; ρ̄ is ramified at 2243; take τ ∈ I_2243 (Carayol).
  - Serre's lemma, and the Z₃-image of ρ_{f_m}, are not needed and were not checked.
- **Integral versus rational.** 17.4(3) is integral: it holds at every height-one prime, (3) included.
  But its L is L_{α,ω,γ} with ω "good": the image of ω in D_dR(V'') must generate
  H⁰(Q_p, Ẑ_p^ur ⊗ T''(k−1)).

## K-B1a — the failure
- **The normalization Skinner uses is different.** His transfer uses L^Σ_{f_m} from Sk (2-4-1)/(2-4-2),
  with SU §3.3.3 canonical periods. There, ω = the q-expansion-normalized f_m, and γ^± is a basis of
  H¹(Γ₁, Sym)[λ] (SU l.1522–1548). This is the L in (2-6-3) (Sk l.1062–1075).
- **Relation between the two.** If ω_good = c_m·f_m, then L^can(f_m) = c_m·L^good(f_m) (Ka 12.5(1),
  paraphrased; γ matched).
  - For elliptic curves, the good ω is the Néron differential (Ka l.8298–8300), and c is the Manin
    constant.
  - Here k_m ≥ 8 > p = 3, which is outside the Fontaine–Laffaille range.
- **No source makes the comparison.**
  - SU Thm 3.5.6 (SU l.2277–2279, citing "17.14", evidently 17.4) states the canonical form without
    argument.
  - Skinner corrects only the image hypothesis.
  - Kato compares ω with the q-expansion only in weight 2.

## MS-B1 — the exact missing statement
**Setting.** M = N/3. The f_m ∈ S_{k_m}(Γ₀(M)) are Skinner's forms (Sk l.1032, l.1101–1102), with O as in
Sk §3.1 and Σ ⊇ {ℓ | N}. L^Σ_{f_m} is Sk (2-4-2), with SU §3.3.3 canonical periods.

**(MS-B1)** For infinitely many m:

  L^Σ_{f_m} ∈ O · L^Σ_{p-adic,α,ω,γ}(f_m) for some pair (ω, γ) good for one G_Q-stable O-lattice (Ka 17.5).

**One-way sufficient condition.** Let T_B be the étale realization of M(f_m)_(p) ⊗ O. MS-B1 follows if both:
- SU's γ^± is good for T_B;
- every ω good for T_B has 3-integral q-expansion (the analogue of the Manin constant being integral).

**What MS-B1 would give.** Kato 17.4(3), with (a) + (b), gives L^Σ_{f_m} ∈ Ch^Σ(f_m) in Λ_O. That is the
input the transfer drafted in WORKING_ONE_SIDED.md needs. That draft is UNAUDITED.

## Observation for the coordinator (not a regrading)
- SU Thm 3.6.4's proof (SU l.2400–2405) uses SU Thm 3.5.6 in canonical form. Skinner Thm 2.5.2 for f_m
  rests on SU Thm 3.6.4.
- So the printed proof of Skinner Thm A for this seed passes through the same unargued transcription, as
  well as through the SU Prop 12.3.6 item from Lane 1.
- This does not show that Thm A fails. S.3's grade and wording are untouched by this lane.

## Grades (kept separate)
- **Checked here, from printed sources read at source:**
  - Kato 17.4 quoted with all its hypotheses.
  - Skinner's (a) + (b) replacement matches Kato §13.14 / 13.4(3).
  - (a) and (b) hold for every f_m at p = 3.
- **UNCHECKED:**
  - MS-B1.
  - γ-goodness for T_B (standard Artin comparison; not verified at source).
  - All of WORKING_ONE_SIDED.md.
  - K-B1b and K-B1c.
  - This consequence, derived from the unaudited draft: if v₃(c_m) ≥ −b for infinitely many m, then
    Sha[3^∞] is finite with #Sha[3^∞] ≤ 3^{2+b}.
- **CONJECTURE:** none asserted.
- **Possible sources for MS-B1 (UNCHECKED; none attempted).**
  - A Λ-adic Eichler–Shimura comparison for ordinary families (Ohta), if its hypotheses allow p = 3.
  - A Kato-type divisibility at the multiplicative prime itself, in Néron normalization. Kato 17.4 does
    not give this (it needs p ∤ N).

## Files
- NOTES.md, RESUME.md, STATE.json: the log and state (written first).
- WORKING_K_B1a.md: Kato statement, hypothesis checks, and the failure, with file:line citations.
- WORKING_ONE_SIDED.md: a draft transfer (S1–S9), written before the failure. It is UNAUDITED.
- sources/: Kato2004_AST295.pdf (from Numdam), its pdftotext output (.txt, the "Ka" line numbers),
  and KATO_SOURCE.sha256.
- Citation keys:
  - Sk = inputs/Skinner2016_published.txt
  - SU = ~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/p3_r1_r2_2026-09-19/sources/SkinnerUrban_MC.txt
    (author copy)

## Unchanged
- R1 and R2 (3.1)–(3.9) were not reopened.
- No computation, prime run, push or message.
- Nothing was written outside this folder.

FIN, ORDER9 and Q36 are unchanged.
