# Pre-registration: singleton Ota witness at p = 31, l = 311 (frozen 2026-09-27, before launch; NOT launched)

**Version 4 (Batch C).** This is an out-of-sample test of a sealed prediction, run on the user's "go C" of 2026-09-27
(BATCH_C_PLAN_v2.md, corrected per Codex audit `BSD_PRO_FOLLOWUP_LEAN_BATCH_C_AUDIT_CODEX_2026-09-27`; preflight PASS). The engine, checker, lattice
(1/1024)ℤ and acceptance rules are those of v2. T follows the v2 rule: the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of
the identification budget, i.e. `arbcore tmin` at LATDEN 4096 = 108112514659. The 1024 value was 102543132758.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 31 (good ordinary (a_31 = -8)) and l = 311;
- Q = N = 6503188012738584, sign +1, T = 108129157119 (6445 segments of 2²⁴) and LATDEN 1024;
- the primitive root is the checker's smallest one, g = 17.

**The corpus.** It is read through `corpus_ext_6445/view/ap` (read-only), with acceptance CORPUS_CHECK_6445.json (all_ok). The pinned receipt root over segments 0..6444 is 92cd0222d32e722087897738839a560b24af45a9a44221c6271502e0ed7de60f. It was recomputed at freeze time from the verifier
receipts. The same method reproduces the 29/233 v2 and 19/191 v2 pinned roots.

**Admissibility** (PARI, `corpus/ADMISSIBILITY.txt`):
- #E(F_311) = 296, with E(F_311) ≅ ℤ/296, so E(F_311)[31] = 0;
- v_31(311 − 1) = 1, and 311 ∤ 31N;
- #E(F_31) = 40, so 31 is not anomalous, and 31 ∤ 6N and 31 ∤ Tam = 16.

**Grade.**
- Ota Thm 1.5/6.4 (Assumption 4.1: p ∤ 6N·∏m_ℓ, together with surjectivity). The other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/`. Its negative controls were re-run at
  freeze time and all passed (`margin_probe/CONTROLS_RUN_2026-09-26.log`).

**The sealed prediction** (`prescreen/PREDICTIONS_2026-09-26.md`, sha256 4853a5fbdb0a6a16a63c13681a010f19d47d7e439c493c565988372b51396ffd) is c₂ ≡ 3 (mod 31). It
comes from det H(E) = 17, K = 288 and #E(F_l) = 296. The checker never reads it.

**Outcomes, fixed now** (ADDENDUM_1; recorded on three separate axes):
1. **Numerical certificate.** NONZERO (exit 0) or INCONCLUSIVE_ZERO (exit 3) count as ACCEPTED only if every binding
   passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 311;
   - the COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 31).

   INVALID (exit 2), or any refusal or crash, means **stop** and diagnose. It is never read as a zero.
2. **Arithmetic consequence.**
   - A certified NONZERO gives **Sha(E/ℚ)[31^∞] = 0** (Ota), whether or not it matches the prediction.
   - A certified ZERO says nothing about Sha.
3. **Prediction.**
   - An equal residue is a MATCH.
   - Anything else, **including a certified zero**, is a DISAGREEMENT. It triggers a check of the coefficient and
     tame-regulator conventions. It never triggers a recalibration, a change of prediction, or an alternate-l run.

**Order and stop rule (Batch C).** 43/173, then Stage W and CORPUS_CHECK_6445, then 47/283, then 31/311.
Stop and report before continuing on any INVALID, any prediction disagreement (a zero included), a failed
corpus check, or a cap breach. Conditional bound: 16,641 after 31; 19,881 after 31 and 43; 25,281 after all three.

**Resources.** Estimated 14.3 CPU-h (conservative). The Batch C cap is 100 CPU-h, 40 GiB new disk, a 60 GB free floor, $0.
