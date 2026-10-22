# Pre-registration: singleton Ota witness at p = 41, l = 83 (frozen 2026-09-26, before launch; NOT launched)

**Version 3.** This is an out-of-sample test of a sealed prediction, run on the user's authorization of 2026-09-26
(Codex handoff `BSD_NEXT_PARALLEL_HANDOFF_CODEX_2026-09-26`, LOCAL_TWO_TESTS.md). The engine, checker, lattice
(1/1024)ℤ and acceptance rules are those of v2. T follows the v2 rule: the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of
the identification budget, i.e. `arbcore tmin` at LATDEN 4096 = 28127211721. The 1024 value was 26640254534.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 41 (good ordinary (a_41 = 6)) and l = 83;
- Q = N = 6503188012738584, sign +1, T = 28135391231 (1677 segments of 2²⁴) and LATDEN 1024;
- the primitive root is the checker's smallest one, g = 2.

**The corpus.** It is read through `corpus_ext_4802/view/ap` (read-only), with acceptance CORPUS_CHECK_4802.json
(all_ok). The pinned receipt root over segments 0..1676 is e442e6c1b7db0b58d7ee07882958aa2a73caf6a701fdccc6c20575926a1ffc99. It was recomputed at freeze time from the verifier
receipts. The same method reproduces the 29/233 v2 and 19/191 v2 pinned roots.

**Admissibility** (PARI, `corpus/ADMISSIBILITY.txt`):
- #E(F_83) = 92, with E(F_83) ≅ ℤ/92, so E(F_83)[41] = 0;
- v_41(83 − 1) = 1, and 83 ∤ 41N;
- #E(F_41) = 36, so 41 is not anomalous, and 41 ∤ 6N and 41 ∤ Tam = 16.

**Grade.**
- Ota Thm 1.5/6.4 (Assumption 4.1: p ∤ 6N·∏m_ℓ, together with surjectivity). The other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/`. Its negative controls were re-run at
  freeze time and all passed (`margin_probe/CONTROLS_RUN_2026-09-26.log`).

**The sealed prediction** (`prescreen/PREDICTIONS_2026-09-26.md`, sha256 4853a5fbdb0a6a16a63c13681a010f19d47d7e439c493c565988372b51396ffd) is c₂ ≡ 15 (mod 41). It
comes from det H(E) = 19, K = 288 and #E(F_l) = 92. The checker never reads it.

**Outcomes, fixed now** (ADDENDUM_1; recorded on three separate axes):
1. **Numerical certificate.** NONZERO (exit 0) or INCONCLUSIVE_ZERO (exit 3) count as ACCEPTED only if every binding
   passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 83;
   - the COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 41).

   INVALID (exit 2), or any refusal or crash, means **stop** and diagnose. It is never read as a zero.
2. **Arithmetic consequence.**
   - A certified NONZERO gives **Sha(E/ℚ)[41^∞] = 0** (Ota), whether or not it matches the prediction.
   - A certified ZERO says nothing about Sha.
3. **Prediction.**
   - An equal residue is a MATCH.
   - Anything else, **including a certified zero**, is a DISAGREEMENT. It triggers a check of the coefficient and
     tame-regulator conventions. It never triggers a recalibration, a change of prediction, or an alternate-l run.

**Order and stop rule.** (41, 83) runs first. (37, 149) runs only if (41, 83) is ACCEPTED and MATCHES. After (37, 149),
stop. Neither result moves the 8649 order threshold while 31 is open.

**Resources.** Estimated 3.3 CPU-h. The cap for both runs together is 12 CPU-h, 16 GiB RAM, 10 GiB disk, $0.
