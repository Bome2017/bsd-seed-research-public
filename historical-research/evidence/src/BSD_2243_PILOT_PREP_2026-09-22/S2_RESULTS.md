# S2: accumulator prototype and its validation

Date 2026-09-22. Source `S2_prototype/acc2243.c`; the profiling copy `acc2243_prof.c` differs only in benchmark
switches. It is derived from the rigorous stream core's `arbcore.c` (sha `56a43aac…`).

**Copied verbatim from `arbcore.c`:**
* the kernel and the gap-exponential table;
* a_n cofactor generation and the Part S / Part L decomposition;
* the unitary-cusp symbol formula;
* the tail bound and the periods;
* the verified-a_q segment reader, with SHA-256.

**Changed (data flow only):**
1. **Exact fixed-point integer class sums per worker**, with 96 fractional bits in `__int128`. Each Arb term
   [mid ± rad] contributes round(mid·2^96). The quantity ⌈rad·2^96⌉ + 1 goes into an exact error tally, and an
   overflow guard sits at 2¹²⁴. Merging is integer addition, so results are order-independent.
2. **Part L sub-units** (segment, cofactor range), sized by a per-dyadic-interval integer estimate, with an early
   break once T/q < m₀.
3. **Cumulative per-worker checkpoints.** Each is written to a temporary file, fsynced and renamed into place, with a
   SHA-256 trailer and a PARAMS lock. Every completed unit is recorded with a **linear fingerprint** (Σ z·ρ[k] mod
   2⁶⁴), its term count, its pair or smooth count, and its input hash. Restart skips recorded units.
4. **Merge** checks, before printing any class sum or symbol:
   * exact unit coverage;
   * Σ fingerprints ≡ fingerprint of the merged array;
   * #smooth + #pairs = T;
   * the a_q segment root.

   It then prints the class sums and symbols. Optionally it prints the exact depth-n coefficient a_{n,r} in the
   certified (Lane 3 / SW) convention, the unit test, and the nonzero-only ball test.

## Validation

| test | what | result |
|---|---|---|
| **T1** | 8 small Δ > 0 curves; M = 5, 7; split and non-split; w = ±1; m = M², M³; unit size forced tiny, frequent checkpoints | **PASS 16/16. 3 648 exact eclib symbols** contained in the new engine's balls; coverage, fingerprint and count identity hold |
| **T3** | seed at m = 27, T = 12·2²⁴ − 1, certified verified a_q: runs at W = 1 and W = 8; a W = 4 run crashed after 23 units (4 checkpoints left), then restarted with W = 3 | **PASS.** All three merges are **bit-identical**: 45 class-sum and symbol lines, fingerprint `32e1386d…`, rounding tally, 90 400 127 terms. Identical also **across versions**: the results before and after the unit-planning fix agree although the decomposition changed from 1 242 to 67 units |
| **T2** | **retained certified cases**: seed at m = 27 (T = 4 831 838 207) and m = 81 (T = 14 847 836 159), with the certified verified a_q (885 segments) | **PASS 7/7.** Every class sum overlaps the certified msl ball. **All 36 + 108 symbol values are identical to the certified ones.** The smooth and pair counts equal the certified run's. **a_{4,2} = 15480 exactly**, the certified value, which pins the weight and discrete-log convention the 2243 certificate uses. The unit test **correctly fails** at p = 3, where 3 ∣ a_{4,2}: nothing is claimed there |

**Performance** at m = 81: 2.4 CPU-h against the certified core's 3.0 CPU-h. At m = 27: 0.73 CPU-h against 0.92.

## Defects found by the tests (all fixed before the passing runs)

* **The shell does not word-split `$C`** (zsh), so the program received too few arguments and indexed past argv
  (segfault). Fixed with argc guards ("FATAL: too few arguments") and bash argument arrays. The first T3 attempt was
  vacuous for this reason and is not counted.
* **Retained a_q files are full 2²⁴ segments.** A non-aligned T makes the reader refuse the trailing data. The check
  failed closed as designed; T must be k·2²⁴ − 1.
* **Sub-unit planning** used the segment's maximum cofactor bound for every prime, which over-split the √T segment
  about 1 000×. Fixed with the dyadic estimate and the early break. Results were unchanged (bit-identical), and the
  run was 4.3× faster.

## Not yet validated (explicit)

* **Symbol extraction at m ≈ 5·10⁶.** The merge's symbol loop is the core's O(m·φ(m)) direct sum, which is fine for
  the tests but not at 2243. The production merge needs the length-m DFT (`acb_dft`), which is timed in S3 and not
  yet wired into `merge`.
* **The nonzero-only ball test and the weighted scalar at large m.** They are exercised at m = 81 only.
* **Independent review of the prototype source and tests**, planned for Codex per the user's instruction.
* **The trust boundary.** The prototype is a new engine: its fixed-point conversion, checkpoint format and merge are
  new trusted code, validated by T1–T3 but not formally verified. The producer is untrusted, and its buffer fix
  produced identical verified a_q (ap_sha256 match).
