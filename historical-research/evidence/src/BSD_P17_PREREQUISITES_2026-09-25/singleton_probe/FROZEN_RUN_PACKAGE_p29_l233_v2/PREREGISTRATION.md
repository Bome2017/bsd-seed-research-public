# Pre-registration: singleton Ota witness at p = 29, l = 233 (frozen 2026-09-26, before launch; NOT launched)

**Version 2.** The v1 package (FROZEN_RUN_PACKAGE_p29_l233, commit 2f6f053, T = 76,386,664,447) was superseded before launch (SUPERSEDED_p29_l233_v1.md), after p19_l191 run 1 failed closed at the same tail margin.
- This version changes **only T**, by the rule: T = the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of the identification
  budget (`arbcore tmin` at 4× lattice density = 80552200096).
- The engine, the checker, the lattice (1/1024)ℤ and the acceptance rules are unchanged.
- T cannot change the witness value; it only makes identification certifiable. A margin probe (margin_probe/) shows
  every label unique at ¼ of the budget, even with symbols 16× larger than at l = 191.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 29 (good supersingular (a_29 = 0)) and l = 233;
- Q = N = 6503188012738584, sign +1, T = 80564191231 (4802 segments of 2²⁴; `arbcore tmin` = 76379288652) and LATDEN 1024.

**The corpus.**
- The coefficient corpus is the EXTENDED corpus, read through `corpus_ext_4802/view/ap` (links only; read-only).
- Segments 0..3280 are the sealed p = 13-run corpus; segments 3281..4552 come from corpus_ext_4553 (and, for k > 4553,
  segments 4553..4801 from corpus_ext_4802).
- The new segments were produced by the certified apwit and verified by the REPAIRED verifier `wverify_distinct`, and
  every new witness passed the distinct-factor scan.
- Acceptance is `corpus/CORPUS_CHECK_4802.json`: all_ok, and it reproduces the earlier pinned roots. The extension
  record is commit 7a51644 (corpus_ext_4802 record).
- Stage W is not run by this launcher.
- **Pinned receipt root** over segments 0..4801: c329c118a1f992b341fb45899b408a551d3f2503d4d313ac3b99a7da0f343f20.

**Admissibility** (PARI, `adm_19_29.txt`):
- #E(F_233) = 248, with E(F_233) ≅ ℤ/248, so E(F_233)[29] = 0;
- v_29(233 − 1) = 1, and 233 ∤ 29N;
- #E(F_29) = 30, so 29 is not anomalous, and 29 ∤ N.

**Grade.**
- Ota Thm 1.5/6.4 carries no ordinary-reduction hypothesis at p (audit item 5). Its other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/` (20/20 controls).

**Prediction recorded before launch** (`prescreen/`: a Mazur–Tate tame-regulator diagnostic, conjecture-based,
calibrated 11/11). det H = 21 ≢ 0 (mod 29). If Sha[29] = 0 and the MT refined conjecture holds, then c₂ ≢ 0 is
predicted. This is not part of the certificate.

**Three outcomes, fixed now:**
1. **NONZERO** (exit 0), accepted only if every binding passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 233;
   - the numeric COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 29).

   Then **Sha(E/ℚ)[29^∞] = 0** (Ota), at the audited grade. With 17 and 23 settled, the threshold moves to 8649 = 9·31² if 19/191 is NONZERO; otherwise it stays at 3249 (t = 19 open).
2. **INCONCLUSIVE_ZERO** (exit 3). This says only that c₂ ≡ 0 (mod 29), and nothing about Sha[29^∞] is concluded.
   - Because the pre-screen predicted nonzero, a zero would be conditional evidence (via the MT refined conjecture)
     that 29 | #Sha. That would be a finding to report, not an automatic action.
   - No next candidate is pre-selected: l = 349 is pre-screen ZERO, and any later l must be screened first. Nothing is launched automatically.
3. **INVALID** (exit 2), or any refusal or crash. **Stop** and diagnose. It is never read as a mathematical zero.

A zero or invalid result here does not affect the accepted results at 17 and 23.
