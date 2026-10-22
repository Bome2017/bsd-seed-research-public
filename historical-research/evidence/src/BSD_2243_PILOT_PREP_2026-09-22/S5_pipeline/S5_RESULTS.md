# S5: pipeline version of the accumulator; restart and recombination at 2243 scale; cloud-pilot package

Date 2026-09-23. The build is frozen; its hashes are in `FINAL_BUILD_HASHES.txt`:

| file | sha256 prefix |
|---|---|
| acc2243v2.c (v2.3) | `295a14c2…` |
| acc2243v2 | `794702de…` |
| acc2243v2_shim (portable SHA-256) | `eeb6e1bd…` |
| stream_seg.sh | `b1378f16…` |
| compat CommonDigest.h | `850f29fa…` |

## What v2 / v2.1 / v2.2 / v2.3 add to the validated S2 prototype

The arithmetic is unchanged. The data flow and the merge change:

* **Unit selection** (`ACC_SELECT`). It is part of PARAMS, so selections never mix. The merge has a selection-aware coverage check and an independent pair recount.
* **Streaming a_q** (`ACC_STREAM_CMD` + `stream_seg.sh`): produce → verify → accumulate → delete, fail closed.
  * The verifier writes into a scratch directory; the file is renamed only after exit 0 and a SEG line.
  * The accumulator checks that the SHA-256 of the bytes it consumed equals the **verifier's own hash** (the `.sha256` companion).
  * Stream directories are **per generation**.
* **Shards** (`ACC_SHARD` i/n) and **tags** (`ACC_TAG`), so checkpoints from several machines can be pooled. An `flock` run lock allows one live run per directory. There is a time-based checkpoint trigger, and workers with no units write no checkpoint.
* **Per-unit timing log** (`ACC_TIMING_LOG`), and a **`plan` mode** that lists the segments to pre-produce: segments 0–2047 at UNIT_TERMS = 10⁹.
* **Merge:**
  * CHUNK_DIGEST = SHA-256 of the class sums, the tally and the counts, for bit-identity tests;
  * DFT symbols (`acb_dft`) when m > 400;
  * `symbols.bin` with its SHA-256;
  * coefficient and unit-test output refused on a partial selection unless the output is timing-labelled.
* **v2.1 (merge only):** exact midpoints go into the symbol transform, the rounding is added once per symbol as 2E (ℓ1), and the merge prints SYMBOL_RADIUS_BUDGET and the maximum symbol radius.
* **v2.2 (run path):** the stream command is started with `posix_spawn`, so all workers stream concurrently.
* **v2.3:**
  * merge: the symbol ball is divided by the period with its radius carried separately (`div_period`);
  * run: the run lock and timing logs are close-on-exec.
* **Portable SHA-256** (`compat/CommonCrypto/CommonDigest.h`). It matches the 5 FIPS 180-4 vectors, and Apple CommonCrypto and `shasum` on real a_q segments and checkpoints, one-shot and in odd-sized chunks. With `-Icompat` the sources build unchanged on Linux.

## Defects found by this stage, all fixed before the final validation

1. **Orphaned stream children** of a killed run could share a worker directory with the restarted run's workers.
   * **This was a correctness hazard, not just a fail-closed one.** In a narrow race, two writers truncating and rewriting the same file could leave zero-filled holes in an a_q file of the correct length, and it would be consumed silently.
   * Closed by two independent guards: per-generation stream directories, and the check that the SHA-256 of the consumed bytes equals the verifier's own hash.
2. **DFT radius inflation at the production length.** `acb_dft` inflates input radii:

   | length | inflation |
   |---|---|
   | 81 | 2.3× |
   | 2243 | 1.7·10³× |
   | 2243² | **7.0·10⁶×** |

   The v2 merge would have identified no symbol at full scale. It fails closed, but the run would have been wasted. Fixed in v2.1; see `probe/PROBE_RESULT.txt` and S4 §6.
3. **Streaming ran serially on macOS.** The worker started the stream command with libc `system()`. Concurrent calls from worker threads ran one at a time (observed; consistent with a process-wide lock in Apple's libc `system()`). In the v2.1 R5 run the stream walls were 199 → 391 → 589 s for about 197 s of work each. Results were correct, but only one producer ran at a time. Fixed in v2.2: `posix_spawn` + `waitpid`, thread-safe, with the command required to be an executable path. A smoke test streamed 4 segments of about 43 s each in 47 s of wall time.
4. **`arb_div` inflated symbol radii in proportion to |x|.** FLINT reduces the working precision to the operand's relative accuracy. A symbol ball [mid ± 1.4·10⁻⁵] carries only about 17 accurate bits, and dividing it by Ω added about |x|·2⁻²⁸: 1.8·10⁻⁷ at |x| = 1.5 (`probe/div_diag.c`).
   * The same effect was already visible at m = 81, where the maximum radius was 4.757·10⁻⁴ against a tail budget of 4.753·10⁻⁴.
   * With large symbols at full scale it would exceed the 4.8·10⁻⁷ margin. That fails closed, but wastes the run.
   * Fixed in v2.3: mid/Ω at full precision plus rad/|Ω|_lower. At m = 81 the maximum radius is now 4.753284·10⁻⁴, the budget exactly.
5. **The run lock was inherited by spawned stream children.** After a simulated crash the orphaned producers kept the `flock` alive, so the immediate restart was refused ("another live run process holds outdir/run.lock"). It failed closed; this is the v2.2 R5-B result. Fixed in v2.3 with `O_CLOEXEC` on the lock and `FD_CLOEXEC` on the timing logs. The orphans are harmless because they write only into their own per-generation stream directories.
6. **Test-harness defects**, none in the engine:
   * a signed overflow in the SHA test harness;
   * a zero-midpoint ball format in the DFT comparator;
   * zsh word splitting;
   * a vacuous empty-file hash comparison, now required to be non-empty;
   * `join` needed lexicographic sort;
   * a script edited while it was running. That R4c run was voided and rerun.

## Final validation (v2.3 build; `tests/final_driver.log`, 2026-09-23 01:36–02:17)

**24 PASS, 0 FAIL.**

| test | what | result |
|---|---|---|
| R1 (×4: both SHA builds × m = 27, 81) | v2.3 merge of the S2 checkpoints against the S2 merge | every non-symbol line byte-identical; every symbol candidate and flag identical, balls overlap, radii ≤ S2 |
| R2 (m = 27, 81) | DFT symbol path against the direct path | identical candidates and flags; radius ratio 1.0000; A_EXACT = 15 851 520 at m = 81 |
| R3 | fresh full m = 27 run, portable-SHA build, 12 threads | equals S2 and the v2.3 merge of the S2 checkpoints byte-for-byte; digest `e24f3f4d…` |
| R4a | two shards (tags), one crashed and restarted, pooled | digest equals R3. Negative control: a missing shard is refused |
| R4b | selection; crash and restart (resumed 6 units from 1 checkpoint) | digest identical. Negative controls refused: wrong selection, bad token, duplicated checkpoint, corrupted checkpoint, missing checkpoint |
| R4c | **streamed a_q**: produce → verify → accumulate → delete | streamed digest equals the certified-a_q digest `3a50588e…`; SEGHASH identical; verifier hashes equal accumulator hashes; no leftovers. Negative controls refused: a failing producer, a corrupted witness (verifier: "q=855638071: factor not prime"), a tampered stored a_q file (consumed-bytes hash check) |
| R4d | restart **from partial checkpoints** over 3 generations (39 units resumed from 5 checkpoints, then 128 from 7) | digest equals the reference |
| R5-A | **2243 scale** (m = 5 031 049, T = T_run): 47 units, including 5 top-range segments streamed at q ≈ 3.912·10¹³, pre-produced heights 10⁷–3.9·10¹³, and Part S blocks at n ≈ 10¹⁰, 10¹², 3.9·10¹³ | 217 s wall with 8 workers; peak memory 2.2 GB; digest `3ca80f2e…` |
| R5-B | crash after 12 units (checkpoint after every unit), **immediate** restart while orphaned producers still ran | resumed 6 units from 2 checkpoints; digest equals A |
| R5-C | two pooled shards | digest equals A |
| R5-D | the same 5 segments produced once and stored (no streaming) | digest equals A |
| R5-H | verifier hash against accumulator hash for the 5 streamed segments | 0 mismatches |
| R5-M | full-size merge path: DFT of length 5 031 049 (176 s), 5 028 806 symbol identifications (10.7 s), weights (timing only) | peak memory 2.7 GB; **maximum symbol radius at T_run 4.878033·10⁻⁴, exactly the tail budget**, against the threshold 4.882812·10⁻⁴ |

**Complete path at the upper planned range (local, loaded host).** One top-range chunk (a 2²⁴ segment at q ≈ 3.912·10¹³, about 536 000 primes) costs:
* **207 s wall**, spread 206.6–207.4 s over the 5 chunks;
* of which producer 181 s, verifier 24 s, accumulate 0.25 s.

The idle single-thread figure is 196 s. The ratio matches the loaded-host factor measured in S3b.

**Earlier validation logs of the superseded builds:**
* `final_driver_v2.1_partial.log`: stopped at R5 when the serial streaming was found;
* `final_driver_v2.2.log`: R5-B FAIL from the lock inheritance, and the unexplained R5-M radius excess, both fixed in v2.3.

## Not validated here (explicit)

* **Linux / cloud build and bit identity across machines.** This is the pilot's P0–P3.
* **Throughput with 64+ cores in one process.** This is the pilot's P4.
* **An independent review of the engine** (`CODEX_CHECK_REQUEST.md`).
* **Checkpoint compaction for long spot runs.** It is designed, not implemented, and needed before a full run.
