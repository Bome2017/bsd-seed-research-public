# Pre-registration: singleton Ota witness at p = 47, l = 283 (frozen 2026-09-27, before launch; NOT launched)

**Version 4 (Batch C).** This is an out-of-sample test of a sealed prediction, run on the user's "go C" of 2026-09-27
(BATCH_C_PLAN_v2.md, corrected per Codex audit `BSD_PRO_FOLLOWUP_LEAN_BATCH_C_AUDIT_CODEX_2026-09-27`; preflight PASS). The engine, checker, lattice
(1/1024)ℤ and acceptance rules are those of v2. T follows the v2 rule: the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of
the identification budget, i.e. `arbcore tmin` at LATDEN 4096 = 98202218916. The 1024 value was 93134121704.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 47 (good ordinary (a_47 = 4)) and l = 283;
- Q = N = 6503188012738584, sign +1, T = 98213822463 (5854 segments of 2²⁴) and LATDEN 1024;
- the primitive root is the checker's smallest one, g = 3.

**The corpus.** It is read through `corpus_ext_6445/view/ap` (read-only), with acceptance CORPUS_CHECK_6445.json (all_ok). The pinned receipt root over segments 0..5853 is 9fc6b8e850307d586046f31e038a58ac1af2f6f468e60ab52761f8375bbff643. It was recomputed at freeze time from the verifier
receipts. The same method reproduces the 29/233 v2 and 19/191 v2 pinned roots.

**Admissibility** (PARI, `corpus/ADMISSIBILITY.txt`):
- #E(F_283) = 288, with E(F_283) ≅ ℤ/288, so E(F_283)[47] = 0;
- v_47(283 − 1) = 1, and 283 ∤ 47N;
- #E(F_47) = 44, so 47 is not anomalous, and 47 ∤ 6N and 47 ∤ Tam = 16.

**Grade.**
- Ota Thm 1.5/6.4 (Assumption 4.1: p ∤ 6N·∏m_ℓ, together with surjectivity). The other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/`. Its negative controls were re-run at
  freeze time and all passed (`margin_probe/CONTROLS_RUN_2026-09-26.log`).

**The sealed prediction** (`prescreen/PREDICTIONS_2026-09-27_ADDENDUM_2.md`, sha256 2be68ea10c09204dbeb49a76688b0274d37108848f0017eba6b5ae3dda0b490b) is c₂ ≡ 42 (mod 47). It
comes from det H(E) = 38, K = 288 and #E(F_l) = 288. The checker never reads it.

**Outcomes, fixed now** (ADDENDUM_1; recorded on three separate axes):
1. **Numerical certificate.** NONZERO (exit 0) or INCONCLUSIVE_ZERO (exit 3) count as ACCEPTED only if every binding
   passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 283;
   - the COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 47).

   INVALID (exit 2), or any refusal or crash, means **stop** and diagnose. It is never read as a zero.
2. **Arithmetic consequence.**
   - A certified NONZERO gives **Sha(E/ℚ)[47^∞] = 0** (Ota), whether or not it matches the prediction.
   - A certified ZERO says nothing about Sha.
3. **Prediction.**
   - An equal residue is a MATCH.
   - Anything else, **including a certified zero**, is a DISAGREEMENT. It triggers a check of the coefficient and
     tame-regulator conventions. It never triggers a recalibration, a change of prediction, or an alternate-l run.

**Order and stop rule (Batch C).** 43/173, then Stage W and CORPUS_CHECK_6445, then 47/283, then 31/311.
Stop and report before continuing on any INVALID, any prediction disagreement (a zero included), a failed
corpus check, or a cap breach. Conditional bound: 16,641 after 31; 19,881 after 31 and 43; 25,281 after all three.

**Resources.** Estimated 13.0 CPU-h (conservative). The Batch C cap is 100 CPU-h, 40 GiB new disk, a 60 GB free floor, $0.
