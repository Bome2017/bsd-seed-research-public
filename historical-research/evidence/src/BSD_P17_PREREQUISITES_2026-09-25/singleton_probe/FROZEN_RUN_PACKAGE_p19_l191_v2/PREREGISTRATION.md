# Pre-registration: singleton Ota witness at p = 19, l = 191 (frozen 2026-09-26, before launch; NOT launched)

**Version 2.** Run 1 (FROZEN_RUN_PACKAGE_p19_l191, commit f587b88, T = 62,360,911,871) returned INVALID: a fail-closed identification margin (see seed_runs/p19_l191/RESULT_P19_RUN1_INVALID.md and margin_probe/). No witness value was computed from it.
- This version changes **only T**, by the rule: T = the aligned cutoff at which 2·tail/Ω⁺ ≤ ¼ of the identification
  budget (`arbcore tmin` at 4× lattice density = 65780747552).
- The engine, the checker, the lattice (1/1024)ℤ and the acceptance rules are unchanged.
- T cannot change the witness value; it only makes identification certifiable. A margin probe (margin_probe/) shows
  every label unique at ¼ of the budget, even with symbols 16× larger than at l = 191.

**The run.** Exactly one run:
- the seed E: y² = x³ − 22735x² + 106272484x, with p = 19 (good ordinary (a_19 = 4)) and l = 191;
- Q = N = 6503188012738584, sign +1, T = 65783463935 (3921 segments of 2²⁴; `arbcore tmin` = 62359832734) and LATDEN 1024.

**The corpus.**
- The coefficient corpus is the EXTENDED corpus, read through `corpus_ext_4553/view/ap` (links only; read-only).
- Segments 0..3280 are the sealed p = 13-run corpus; segments 3281..4552 come from corpus_ext_4553 (and, for k > 4553,
  segments 4553..4801 from corpus_ext_4802).
- The new segments were produced by the certified apwit and verified by the REPAIRED verifier `wverify_distinct`, and
  every new witness passed the distinct-factor scan.
- Acceptance is `corpus/CORPUS_CHECK_4553.json`: all_ok, and it reproduces the earlier pinned roots. The extension
  record is commit e40c8d0 (corpus_ext_4553 record).
- Stage W is not run by this launcher.
- **Pinned receipt root** over segments 0..3920: 58d28b3721d5fd6fcde3e8f5ef66d262ba7dd0bc98d9fb085c744fc7a9bdfce3.

**Admissibility** (PARI, `adm_19_29.txt`):
- #E(F_191) = 202, with E(F_191) ≅ ℤ/202, so E(F_191)[19] = 0;
- v_19(191 − 1) = 1, and 191 ∤ 19N;
- #E(F_19) = 16, so 19 is not anomalous, and 19 ∤ N.

**Grade.**
- Ota Thm 1.5/6.4 carries no ordinary-reduction hypothesis at p (audit item 5). Its other hypotheses are uniform in odd
  p: A.3 surjectivity, Tamagawa 16, torsion ℤ/2, c_E | 2⁹.
- The acceptance code is byte-identical to the frozen p = 17 package's `checker/` (20/20 controls).

**Prediction recorded before launch** (`prescreen/`: a Mazur–Tate tame-regulator diagnostic, conjecture-based,
calibrated 11/11). det H = 2 ≢ 0 (mod 19). If Sha[19] = 0 and the MT refined conjecture holds, then c₂ ≢ 0 is
predicted. This is not part of the certificate.

**Three outcomes, fixed now:**
1. **NONZERO** (exit 0), accepted only if every binding passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 191;
   - the numeric COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 19).

   Then **Sha(E/ℚ)[19^∞] = 0** (Ota), at the audited grade. With 17 and 23 settled, the next possible order (conditional on FIN) moves from 3249 to 7569 = 9·29² while 29 is open, or to 8649 = 9·31² if 29/233 is also NONZERO.
2. **INCONCLUSIVE_ZERO** (exit 3). This says only that c₂ ≡ 0 (mod 19), and nothing about Sha[19^∞] is concluded.
   - Because the pre-screen predicted nonzero, a zero would be conditional evidence (via the MT refined conjecture)
     that 19 | #Sha. That would be a finding to report, not an automatic action.
   - The next candidate, l = 229 (pre-screen det 4), is NOT launched automatically.
3. **INVALID** (exit 2), or any refusal or crash. **Stop** and diagnose. It is never read as a mathematical zero.

A zero or invalid result here does not affect the accepted results at 17 and 23.
