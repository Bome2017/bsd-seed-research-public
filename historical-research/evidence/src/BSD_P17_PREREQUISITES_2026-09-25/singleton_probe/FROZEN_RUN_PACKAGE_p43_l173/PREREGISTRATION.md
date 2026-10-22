# Pre-registration: singleton Ota witness at p = 43, l = 173 (frozen 2026-09-27, before launch; NOT launched)

**Version 4 (Batch C).** This is an out-of-sample test of a sealed prediction, run on the user's "go C" of 2026-09-27
(BATCH_C_PLAN_v2.md, corrected per Codex audit `BSD_PRO_FOLLOWUP_LEAN_BATCH_C_AUDIT_CODEX_2026-09-27`; preflight PASS). The engine, checker, lattice
(1/1024)ℤ and acceptance rules are those of v2. T follows the v2 rule: the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of
the identification budget, i.e. `arbcore tmin` at LATDEN 4096 = 59468143596. The 1024 value was 56369526596.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 43 (good ordinary (a_43 = -8)) and l = 173;
- Q = N = 6503188012738584, sign +1, T = 59475230719 (3545 segments of 2²⁴) and LATDEN 1024;
- the primitive root is the checker's smallest one, g = 2.

**The corpus.** It is read through `corpus_ext_4802/view/ap` (read-only), with acceptance CORPUS_CHECK_4802.json (all_ok). The pinned receipt root over segments 0..3544 is 80b814ed11cb387bbca86919c4ce01fcb6afe68bc9a0f037006777307ddbbf6a. It was recomputed at freeze time from the verifier
receipts. The same method reproduces the 29/233 v2 and 19/191 v2 pinned roots.

**Admissibility** (PARI, `corpus/ADMISSIBILITY.txt`):
- #E(F_173) = 196, with E(F_173) ≅ ℤ/98 × ℤ/2, so E(F_173)[43] = 0;
- v_43(173 − 1) = 1, and 173 ∤ 43N;
- #E(F_43) = 52, so 43 is not anomalous, and 43 ∤ 6N and 43 ∤ Tam = 16.

**Grade.**
- Ota Thm 1.5/6.4 (Assumption 4.1: p ∤ 6N·∏m_ℓ, together with surjectivity). The other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/`. Its negative controls were re-run at
  freeze time and all passed (`margin_probe/CONTROLS_RUN_2026-09-26.log`).

**The sealed prediction** (`prescreen/PREDICTIONS_2026-09-26.md`, sha256 4853a5fbdb0a6a16a63c13681a010f19d47d7e439c493c565988372b51396ffd) is c₂ ≡ 15 (mod 43). It
comes from det H(E) = 17, K = 288 and #E(F_l) = 196. The checker never reads it.

**Outcomes, fixed now** (ADDENDUM_1; recorded on three separate axes):
1. **Numerical certificate.** NONZERO (exit 0) or INCONCLUSIVE_ZERO (exit 3) count as ACCEPTED only if every binding
   passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 173;
   - the COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 43).

   INVALID (exit 2), or any refusal or crash, means **stop** and diagnose. It is never read as a zero.
2. **Arithmetic consequence.**
   - A certified NONZERO gives **Sha(E/ℚ)[43^∞] = 0** (Ota), whether or not it matches the prediction.
   - A certified ZERO says nothing about Sha.
3. **Prediction.**
   - An equal residue is a MATCH.
   - Anything else, **including a certified zero**, is a DISAGREEMENT. It triggers a check of the coefficient and
     tame-regulator conventions. It never triggers a recalibration, a change of prediction, or an alternate-l run.

**Order and stop rule (Batch C).** 43/173, then Stage W and CORPUS_CHECK_6445, then 47/283, then 31/311.
Stop and report before continuing on any INVALID, any prediction disagreement (a zero included), a failed
corpus check, or a cap breach. Conditional bound: 16,641 after 31; 19,881 after 31 and 43; 25,281 after all three.

**Resources.** Estimated 7.9 CPU-h (conservative). The Batch C cap is 100 CPU-h, 40 GiB new disk, a 60 GB free floor, $0.
