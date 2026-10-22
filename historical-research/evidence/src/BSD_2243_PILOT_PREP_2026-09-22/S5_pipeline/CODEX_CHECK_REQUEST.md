# Independent check request: 2243 accumulator prototype (S2/S5) against certified small cases

**For:** Codex (independent reviewer). **From:** the 2243 pilot-preparation session, 2026-09-23.
**Scope:** read-only review plus small local re-runs. **No cloud, no large runs**; the budget is ≤ 2 CPU-h. Do not modify anything outside a new folder `~/BSD_2243_ACC_CODEX_CHECK_<date>/`. The rigorous stream core, the p = 3 run directory and the handoff folders are sealed.

## What to check

The engine under review is `S5_pipeline/acc2243v2.c` **v2.3**. Frozen hashes are in `S5_pipeline/FINAL_BUILD_HASHES.txt`: source `295a14c2…`, binary `794702de…`. Superseded sources are kept in `S5_pipeline/probe/`:
* `acc2243v2_v2.0_frozen.c`;
* `acc2243v2_v2.1_superseded.c`;
* `acc2243v2_v2.2_superseded.c`.

The changes are:
* v2.0 → v2.1: the merge-only patch `probe/patch_v21_merge.py`;
* v2.1 → v2.2: the stream command is started with `posix_spawn` instead of `system()`, which ran concurrent calls serially on macOS;
* v2.2 → v2.3: the symbol ball is divided by the period with its radius carried separately (`div_period`), and the run lock and timing logs are opened close-on-exec.

It derives from `S2_prototype/acc2243_prof.c` (sha `9fe2cca3…`). That in turn derives from the certified core `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore.c` (sha `56a43aac…`).

Please return a verdict of **PASS**, **PASS_WITH_CORRECTIONS** or **FAIL**, with a finding list. Each finding should name the file:line, what is wrong, and a concrete failing input if one exists. Do not repair; report.

1. **Arithmetic equivalence with the certified core.**
   * Claim: the kernel, a_n generation, the Part S / Part L decomposition, the tail bound, the periods and the symbol formula are verbatim copies. The only change is that `read_apseg` takes the directory as an argument.
   * Check by diffing against `arbcore.c`, not by trusting this sentence.
2. **Exact fixed-point accumulation (`add_term`).**
   * Each Arb term [mid ± rad] adds round(mid·2⁹⁶) to an i128 and adds ⌊rad·2⁹⁶⌋ + 2 to an error tally, in units of 2⁻⁹⁶.
   * The claim to verify: the merged tally bounds |true sum − merged sum| for every class. Specifically:
     * `mag_get_d` is an upper bound, and the conversion is exact for a 30-bit mantissa;
     * `arf_get_fmpz_fixed_si` rounds to within 2⁻⁹⁶;
     * the overflow guards (term > 2¹²⁰, class sum > 2¹²⁴, radius ≥ 10¹⁸ units) are sufficient at m = 5 031 049 and T ≈ 3.9·10¹³.
3. **Fingerprints and merge checks.**
   * fp(u) = Σ z·ρ[k] (mod 2⁶⁴) is linear. The merge checks Σ_u fp(u) = Σ_k S_k ρ[k].
   * The merge also checks exact unit coverage; #smooth + #pairs = T (full run); and, for a selection, an independent recount of the pairs from a fresh sieve.
   * State what each check does and does not detect.
4. **Checkpoints.**
   * The format is: tmp file + fsync + rename, SHA-256 trailer, PARAMS lock including the selection string, per-unit records.
   * Restart semantics: units finished but not checkpointed are recomputed.
   * Are there any double-count or loss scenarios, including kill -9 during a write, two generations, and shards pooled into one directory?
5. **Symbols via DFT** (new in v2; the error handling was changed in v2.1).
   * **v2.1 claim to check hardest.** Class sums enter the symbol computation as exact midpoints, and the accumulated rounding is added once per symbol as 2E. The argument: Σ_k |e_k| ≤ E, and every combination coefficient is ≤ 2 in absolute value.
     * Is E really an ℓ1 bound over classes? Is ≤ 2 right for both the plus (cos ± cos) and minus (sin ∓ sin) combinations?
     * Is the tail term 2·tail_MS added in the same way as in the certified core?
     * Why this matters: v2 put E on every class as a radius, and `acb_dft`'s Bluestein/Rader steps inflate input radii about 7·10⁶× at m = 2243² (`probe/probe_full.txt`).
   * **v2.3 claim.** `div_period` computes mid/Ω with `arb_div` on the exact midpoint, then adds rad/|Ω|_lower via `arb_get_mag_lower` and `mag_div`, which rounds up. Is this a valid enclosure of x/Ω for every x in the ball?
     * Why this matters: `arb_div` on a ball with about 17 accurate bits worked at reduced precision and added about |x|·2⁻²⁸ to the radius (`probe/div_diag.c`). That is 1.8·10⁻⁷ at |x| = 1.5, against a 4.8·10⁻⁷ identification margin.
   * `acb_dft` convention: FD_j = Σ_k S_k e^{−2πi jk/m}.
   * The code computes re = Re FD_b + s·Re FD_{u_b} and im = −Im FD_b + s·Im FD_{u_b}. Please re-derive both signs from the direct sum in the same file (cs = cos kb ± cos k u_b, sn = sin kb ∓ sin k u_b).
   * Local R2 test: at m = 27 and 81 the DFT and direct paths agree on every candidate and flag. At m = 81 the minus symbols also agree, which pins the sign convention.
6. **The depth-n coefficient and the tests.**
   * The dlog / ω(b) convention and C(j, r).
   * LATDEN·a_{n,r} = Σ C(j, r)·(LATDEN·x_b), and the sign handling for α = −1 and odd n.
   * `UNIT_TEST`. `NONZERO_ONLY`: floor/ceil directions in [L/p, U/p].
   * Certified anchor: m = 81, p = 3, n = 4, r = 2, α = −1 must give A_EXACT = 15 851 520 = 1024·15480, and UNIT_TEST must FAIL because 3 divides it.
7. **Streaming and fail-closed behaviour** (new in v2). Review `stream_seg.sh` and the worker in `run` mode:
   * a verifier failure, or a missing SEG line, aborts the run;
   * the consumed-bytes SHA-256 must equal the verifier's own hash (the `.sha256` companion);
   * stream directories are per generation, so orphaned children of a killed run cannot share them.
   * Is there any path by which unverified or partially written a_q is consumed?
8. **Selection, shard and tag semantics.** Can a pooled merge ever silently accept overlapping or missing units?

## Certified small cases to re-run (≤ 2 CPU-h on 10 cores)

Build the engine:

```bash
cd ~/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline && SE=~/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env && cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations -I$SE/include acc2243v2.c -L$SE/lib -Wl,-rpath,$SE/lib -lflint -lmpfr -lgmp -lpthread -o /tmp/acc2243v2_codex && shasum -a 256 /tmp/acc2243v2_codex acc2243v2
```

Run it at m = 27 with the certified verified a_q (0.73 CPU-h):

```bash
AP=~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap; /tmp/acc2243v2_codex run 0 -22735 0 106272484 0 27 2167729337579528 1 4831838207 16777216 $AP 10 /tmp/codex_m27 500000000 40 && ACC_DFT=0 /tmp/acc2243v2_codex merge 0 -22735 0 106272484 0 27 2167729337579528 1 4831838207 16777216 $AP /tmp/codex_m27 1024 > /tmp/codex_m27_merge.txt
```

**Reference values** are in `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/`: `SYMBOLS_m27.txt`, `SYMBOLS_m81.txt`, `msl_m27.txt` and `msl_m81.txt`. The expected CHUNK_DIGEST for m = 27 is `e24f3f4d4e705b42e6002bf8059430aa73ae3315bc437d2665bd99d151330681`. v2.1 changes only the merge, so the digest is the same as under v2.0.

The m = 81 run (T = 14847836159; weights `3 4 2 -1`; 2.4 CPU-h) is optional. Please write your own comparator; do not reuse `S2_prototype/T2/compare_t2.py`.

## Local results you are checking (do not take them on trust)

* `S2_RESULTS.md` covers T1, T2 and T3.
* `S5_pipeline/tests/final_driver.log` covers:
  * R1: regression against S2;
  * R2: DFT against direct;
  * R3: fresh run;
  * R4a–R4d: shards, selection, streaming, negative controls, restart from partial checkpoints;
  * R5: 2243-scale streamed, stored, crash and shard digests, and the full-size merge.

## Suggested adversarial tests

* Flip one bit in a checkpoint's array. Delete one U-record line and fix the SHA trailer yourself: does the merge still refuse? It should, via coverage or the fingerprint.
* Duplicate a unit across two pooled shards.
* Hand a streamed segment an a_q file with one value changed but the verifier's `.sha256`.
* Run a merge with a different m, Q, T or UNIT_TERMS on the same checkpoints.
* A selection token that selects nothing.
