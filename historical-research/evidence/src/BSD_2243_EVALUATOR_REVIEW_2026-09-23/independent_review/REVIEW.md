# Independent review: `acc2243v2.c` v2.3 (2243 pilot accumulator)

Reviewer: independent agent with a fresh context, 2026-09-23. I did not write the engine. Everything below comes from reading the code and from my own builds, replays and tests. All my files are in this folder. I did not modify anything outside it.

## Verdict: **PASS_WITH_CORRECTIONS**

The arithmetic is sound. My own build reproduces the certified small cases bit for bit.

* **m = 27.** CHUNK_DIGEST is `e24f3f4d…330681`, identical to the author's. The a_q segment root, the smooth Merkle root, the pair and smooth counts, and the number of nonzero terms all equal the certified arbcore run. All 27 exact class sums lie within 1.1·10⁻²⁵ of the certified balls. All 18 + 18 symbols are exactly the certified values on both the direct path and the DFT path.
* **m = 81.** CHUNK_DIGEST is `04a7d952…a998`, identical to the author's. All 54 + 54 symbols are exact on both paths. A_EXACT = 15851520 = 1024·15480, and UNIT_TEST FAILs as required.

The fixed-point error tally is a valid per-term bound. The 2E ℓ1 term is valid. The DFT signs are correct for both signs of w. `div_period` is a valid enclosure. The lattice identification cannot mis-identify. The weights match the certified definition.

No finding is critical. One is major:

* **F4** (the major finding): the documented isolation of stream directories between generations is false after a crash that precedes the first checkpoint. It stays fail-closed through the consumed-bytes hash check, but it must be fixed before production.

The rest are minor or notes, and none affects results obtained in the intended configuration:

* documentation: the "verbatim" claim for Part L is inaccurate;
* parameters that are not bound across the stream wrapper and the setup table;
* missing input validation in the weights;
* one undefined-behaviour path in `read_ckpt`.

The most important interpretive point is F3 together with F2. The fingerprint is blind to the high 64 bits of every class sum. At the operating radius, the (1/1024)Z identification also accepts almost any value. So a self-consistent but corrupted checkpoint yields "identified", wrong symbols. Test A3c shows this: every plus symbol shifted by +1, with every check passing. The only guard is the SHA-256 trailer, which is computed from memory at write time.

## Findings

| id | severity | file:line | what | concrete failing input |
|---|---|---|---|---|
| F1 | minor (documentation) | acc2243v2.c:3-6, 231-249; CODEX_CHECK_REQUEST.md:23 | Part L is **not** a verbatim copy of arbcore `do_lseg` (arbcore.c:221-238). Five differences, listed after this table. The `gen_block` `use_table` argument was dropped (msl passed 0) and `invmod` was rewritten (extended Euclid; checked). All the changes are mathematically valid, and the replay agrees. | none (the claim is wrong, the code is right) |
| F2 | minor | acc2243v2.c:164, 468-471 | The fingerprint uses `(u64)z` and `(u64)tot[k]`, which are the **low 64 bits** of the i128 values. Changes in bits 64-127 are invisible to it, and those bits hold the sign and the leading ~30 significant bits of every class sum (at m = 27, \|S_k\| < 1 occupies bits up to 95). After the SHA trailer is recomputed, the merge accepts the file. The trailer hashes memory at write time, so in-memory corruption of `acc[]` before a write is also undetected. | **A3:** flip bit 64 of S_5 in a checkpoint and re-hash. The merge accepts it; only CHUNK_DIGEST changes. **A3c:** add 60225967·2⁶⁴ units to S_0 in one checkpoint and re-hash. Every plus symbol comes out exactly +1, marked "contains 1 unique 1"; coverage, fingerprint and count all pass. |
| F3 | note (interpretation) | acc2243v2.c:540-546 | "contains ∧ unique" has almost no power to **detect** bad input. At m = 27 the symbol radius is 4.842·10⁻⁴ against a half-spacing of 4.883·10⁻⁴, so an arbitrary value is "identified" with probability 2·rad·LATDEN ≈ 99.2%. At the production margin quoted in the brief (4.8·10⁻⁷) the probability is ≈ 99.9%. `XB_PLUS_DETERMINED = all` is therefore not evidence of correct class sums. Cheap redundancy exists: report the distribution of `cand mod 2^j`. At m = 27 and 81 every certified symbol is an integer, and a random identified value is an integer with probability 1/1024. | **A3b:** class sum S_5 off by exactly 1.0 (bit 96 flipped, re-hashed). Result: 18/18 plus and 18/18 minus "identified", all wrong (e.g. 59341/1024 instead of 70). |
| F4 | **major** (a false safety claim; its effect is fail-closed. I graded it minor in my independent pass and raised it after re-examining the production restart path; see the Codex section.) | acc2243v2.c:329, 431-432 (header lines 17-18) | The claim that stream directories are "per generation, never shared with orphans" is false when the killed run wrote no checkpoint. GEN = 1 + max(existing checkpoint generation), so a restart reuses the same GEN and the same `stream_gGGG_wWW` directories. Orphaned stream children no longer hold the lock (O_CLOEXEC), so they can still be writing there. For a restart with the same configuration the damage is bounded, because the consumed-bytes hash check fails closed; the result is a spurious fatal, interference or lost work. Silent acceptance would also need an orphan running with *different* stream parameters (F5) and a narrow race between the separate `.bin` and `.sha256` moves. A plausible production trigger is a parent-only kill, such as an OOM kill of the accumulator, before the first checkpoint, followed by an automatic restart. Codex independently reproduced the co-residence of an orphan and the new child in `stream_g001_w00`. | **R3:** die after 2 units with CKPT_UNITS = 40 (no checkpoint written), then restart. The restart prints `generation 1`, the same as the killed run. |
| F5 | minor (operational) | stream_seg.sh:11-15; acc2243v2.c:318-320 | The stream command receives only {segment, dir}. The curve (`CURVE` env, defaulting to the seed), T (`T_RUN` env) and SEGQ/QB (hard-coded) are **not bound** to the run's PARAMS. The `.sha256` companion proves only that the consumed bytes equal the verifier's output, not that the verifier used the run's parameters. For a curve mismatch the length checks cannot help, because the prime count does not depend on the curve. In production the streamed a_q are never stored, so there is no independent reference root to compare against. | **S5:** a stand-in verifier output for other parameters, carrying its own consistent hash, is **accepted** (exit 0). Its record hash is `d748ed5a…` instead of `da9aee44…`. |
| F6 | minor | acc2243v2.c:114-123, 366-367, 459-466, 480-486 | The setup table is the segments with s·SEGQ ≤ RT, i.e. a_p for p ≤ RT, which feed APK and AMT. It is read with **no** `.sha256` companion check, and its hash is never stored in checkpoints. The merge therefore cannot tell which table a shard used. The merge also dropped arbcore's SMOOTH_MERKLE line (see F10). | Shard 1/2 (tag D) ran with an apdir whose `ap_000000.bin` has a_5 = 0 instead of −2. It was pooled with a correct shard 0/2 (tag A) on selection `L50-69,S200-229`. The merge exits 0; coverage, fingerprint and recount pass; AP_SEGROOT is **identical** to the reference (`b1e5595d…`); only CHUNK_DIGEST differs (`28cbdf4f…` vs `b63083a2…`). In a full sharded run, the cross-sub-unit hash check on the multi-sub-unit segment 0 catches this only if every shard processes a segment-0 sub-unit. |
| F7 | minor | acc2243v2.c:443-445, 559-578 | Weights input validation is missing. alpha is used only through its sign. p is not checked to be prime. gcd(p, LATDEN) = 1 is not checked, although the UNIT_TEST reading needs it. r < 0 is not rejected. One to three trailing weight arguments are silently ignored. | `merge … 1024 3 3 1 2` (alpha = 2) prints A_EXACT = −1290240, i.e. it treats alpha as +1. The correct α⁻³·Σ would be −161280. |
| F8 | minor (robustness) | acc2243v2.c:275-276, 432, 448, 459 | `read_ckpt` returns 0 **without initializing** `ck` when `fopen` fails, and both callers ignore the return value. The stale previous-iteration `ck`, including freed arrays, is reused, which is undefined behaviour. `fopen(names[0])` is unchecked. In practice this fails closed. | One checkpoint `chmod 000`: the merge ends FATAL "unit covered twice", which is a misleading message. |
| F9 | note | acc2243v2.c:266, 460 | The i128 guard (\|S_k\| ≤ 2¹²⁴) runs only when a worker writes a checkpoint. It does not run between writes or on the merged `tot[k]`, and the mod-2⁶⁴ fingerprint would not notice a wrap. This is not a live risk. By Hasse, \|a_n\| ≤ d(n)√n, so Σ_{n≤T}\|a_n\|/n ≤ Σ d(n)n^{-1/2} ≤ 2√T(1+ln T). That is < 2^28.6 at T = 3.9·10¹³ and < 2^21.7 at T = 4.83·10⁹. So every partial class sum is < 2^124.6 units < 2¹²⁷ for any Q. The 2¹²⁴ guard can fire only spuriously (fail-closed). The u128 tally cannot overflow (≤ nterm·(10¹⁸+2)). | none |
| F10 | note | acc2243v2.c:461-466 | S-block leaf hashes are recorded but never used by the merge (arbcore printed SMOOTH_MERKLE_SHA256). S-block smooth counts are not checked for a selection; this is documented. | **R7b:** S-block `cnt`+1 in a selection, re-hashed: accepted. (In a full run the count identity catches it; A13 → FATAL.) |
| F11 | note | acc2243v2.c:271-272 | tmp + fsync + rename is done without an fsync of the directory. After a power loss the old checkpoint may reappear; its units are recomputed, so this is safe and affects durability only. | none |
| F12 | note | acc2243v2.c:76, 297-301 | MAXCK = 16384 checkpoint files per directory, fatal beyond that. Plan pooled production directories (machines × workers × generations) below this limit. | none |
| F13 | note (process) | acc2243v2.c:334-345 | Pre-produced segments are checked at run time **only if** a `.sha256` companion is present. Segments with several sub-units must be pre-produced; production should require companions for them. The mechanism works when a companion is present (S9 → FATAL, S10 → OK). | none |

The five differences behind F1 (Part L versus arbcore `do_lseg`):
1. The e^{−κq} chain `r` is advanced for **every** prime q > RT, including those with a_q = 0 (line 238). arbcore advances it only when a_q ≠ 0 (arbcore.c:226-228).
2. Sub-units start at m₀ via `arb_pow_ui(r, m₀−1)` and k = (m₀−1)q mod m (242-243).
3. The loop exits early once T/q < m₀ (237).
4. Pairs are counted per sub-range (240).
5. Each term is formed with `arb_mul` and then accumulated in fixed point, instead of `arb_addmul` into a ball.

**Corrections to make before production:** F4, F5, F6, F7, F8, and the F1 documentation. Strongly recommended hardening:
* F2: a full-width fingerprint, for example Σ hi64·ρ′_k as well, or the value mod 2⁶¹−1.
* F3: a lattice-residue statistic in the merge output, and/or a replicated CHUNK_DIGEST on part of the production units.
* F10: print SMOOTH_MERKLE_SHA256 again.

## Checks 1-7

**1. Arithmetic equivalence with arbcore.c.** I compared function by function with a normalizing diff script.
* **Identical to arbcore.c:** `tail_ms`, `small_primes`, `sieve`, `seg_bounds`, `periods`, `curve`, `set_kappa`, `is_bad`, `hexs`, `fatal`, and the EG/AMT table setup (366-372 against arbcore 346-351). The Part S loop matches arbcore's msl `do_block` except for the accumulation: same w = e^{−κ·lo}, same `arb_mul_si`/`arb_div_ui`, same w·Q1 step, same leaf hash.
* **Parameter-level changes:** `read_apseg` and `load_table` now take the directory. `gen_block` dropped `use_table`.
* **Rewritten:** `invmod` (correct). Part L; see F1.
* **Symbol formula:** the direct path is identical to arbcore's. The tail term is identical (`ub = 2·ubound(tail_ms)`, added to both Re and Im before dividing by Ω±).

The replay supports equivalence:
* the certified per-unit `nnz` sums to 2169602069, equal to my `nterm`;
* smooth 1580993508 and pairs 3250844699 equal the certified counts;
* AP_SEGROOT `ca234d65…` equals the certified value;
* SMOOTH_MERKLE, recomputed from my stored S-block leaf hashes, is `71635921…`, equal to the certified value;
* the class-sum midpoints are within 1.1·10⁻²⁵ of the certified exact SDUMP midpoints.

The residual difference is expected from the different r-chain rounding.

**2. The fixed-point tally (`add_term`, lines 157-165) is valid.**
* z is `arf_get_fmpz_fixed_si(mid, −96)`, which truncates, so \|z·2⁻⁹⁶ − mid\| < 2⁻⁹⁶. I tested this on 200k random values of both signs across exponents −140 to +40, with 0 violations.
* `mag_get_d` is an upper bound, exact for rad > 2⁻¹⁰⁰⁰, and it returns 2⁻¹⁰⁰⁰ below that. `ldexp(·, 96)` is exact. I tested 200k random mags with 0 violations.
* The tally adds ⌊rs⌋ + 2 ≥ rs + 1 ≥ (rad + \|mid − z·2⁻⁹⁶\|)·2⁹⁶. So each term satisfies \|true − z·2⁻⁹⁶\| ≤ tally·2⁻⁹⁶, and E = Σ tally·2⁻⁹⁶ ≥ Σ_k \|e_k\|.
* The guards act before the add (term > 120 bits) or on the radius (≥ 10¹⁸ units, which also catches inf). The class-sum guard is discussed in F9 (sufficient by an a-priori bound).
* No term can be dropped or counted twice. Every nonzero term goes through exactly one `add_term`. Skipped terms (a_q = 0, AMT[m] = 0, a_n = 0) are exactly zero. The term count equals the certified `nnz`.
* At m = 27, err/nterm = 2.0000 exactly: every term radius was < 2⁻⁹⁶.

**3. Symbol extraction, signs and error propagation.**
* **(a) DFT signs.** I checked FLINT 3.3.1 `acb_dft` against a direct sum at n = 7, 27, 81, 2243 and 6561. It computes w_j = Σ v_k e^{−2πijk/n} (0 mismatches; the conjugate convention gives n−1 mismatches). Therefore Re FD_j = Σ S_k cos(2πjk/m) and −Im FD_j = Σ S_k sin(2πjk/m).
  * s = +1: re = Re FD_b + Re FD_{u_b} and im = −Im FD_b + Im FD_{u_b}.
  * s = −1: re = Re FD_b − Re FD_{u_b} and im = −Im FD_b − Im FD_{u_b}.
  * Both agree with the code (527-529) and with the direct sums cs = cos kb ± cos k·u_b and sn = sin kb ∓ sin k·u_b, which are verbatim from arbcore.
  * Empirical confirmation of this derivation:
    * s = +1, m = 27: direct and DFT XB lines are identical, and 36/36 match certified.
    * s = −1, m = 27: the m = 27 class sums re-merged with the sign in PARAMS edited. Direct and DFT are identical, and 36/36 balls contain my own mpmath evaluation of the formula.
    * m = 2243 (prime length, Bluestein/Rader), both signs: `symbols.bin` is byte-identical between the direct and DFT paths. This was a plumbing run at T = 2²⁴−1 with Q = Q/2243; nothing is identified there, which is expected.
* **(b) The 2E term** is a valid ℓ1 bound: Σ_k \|e_k\| ≤ E, \|cos α ± cos β\| ≤ 2 and \|sin α ∓ sin β\| ≤ 2, so \|Σ e_k c_k\| ≤ 2E. It is added in the same place as the tail term (504 and 536), and the tail term itself is handled exactly as in arbcore. The S_k midpoints are exact (`arb_set_fmpz`·2⁻⁹⁶, radius zeroed at 503). The printed S_k balls, with radius E, are valid per-class enclosures.
* **(c) `div_period` is valid.** For X ∈ [mid ± rad] and Ω₀ ∈ Ω: X/Ω₀ = mid/Ω₀ + (X−mid)/Ω₀, with the first term inside `arb_div(mid, Ω)` and \|(X−mid)/Ω₀\| ≤ rad/\|Ω\|_lower. `mag_div` rounds up and the zero-ball case is fatal. Tested at 120k points (endpoints and midpoint of x against both ends of Ω at 512 bits): 0 violations. For x = [1.5 ± 1.4·10⁻⁵], the `arb_div` radius is 4.99398·10⁻⁴ against 4.99199·10⁻⁴ for `div_period`. That difference of 2.0·10⁻⁷ confirms the v2.3 motivation.

**4. Exact identification is sound, given the external lattice hypothesis.**
* "contains" is an exact test (`arb_contains_fmpq`). "unique" is an exact test (2·LATDEN·rad < 1, using `ARF_PREC_EXACT` rounded up).
* A closed ball of diameter < 1/LATDEN holds at most one lattice point. So contains ∧ unique pins the lattice point, provided x_b ∈ (1/LATDEN)Z.
* The double-rounded candidate cannot cause a wrong identification. A wrong candidate fails "contains" and is reported as undetermined, which is fail-safe. This covers huge \|x\| (the double loses bits) as well as ties.
* See F3 for what identification does **not** detect.

**5. Checkpoints and merge checks.** Each check detects some failures and misses others:

| check | detects | does not detect |
|---|---|---|
| SHA-256 trailer | any change after the write (A1, A6d) | a re-hashed edit; corruption in memory before the write |
| PARAMS lock (includes UT and SEL) | mixed curve, m, Q, sign, T, SEGQ, UT or selection (A7 ×6, A9, A11, A10) | a different apdir or a_q content; a different setup table (F6) |
| coverage | a missing or duplicated unit or checkpoint (A5, A6, A6c, R5, R6) | — |
| fingerprint | a record/array inconsistency in the low 64 bits (A2, A5) | high-half edits (A3, A3b, A3c); moved records (A8, harmless); a missing checkpoint (A6c, where the fingerprint still matches and coverage catches it); wrong term values, since fp is built from the same z |
| count identity (full run) | layout gaps or overlaps; S or L count edits (A13) | wrong values or classes |
| selection recount | L-unit pair-count errors (R7a) | S blocks (R7b, documented) |

Restart semantics are as claimed:
* **R2:** crash after 13 units (10 of them checkpointed), then restart. The run resumes at generation 2 and the merged digest equals the reference `b63083a2…`.
* **R3:** a crash before the first checkpoint also gives an identical digest (but see F4).
* A rerun on a complete directory is a no-op.
* Tagged shards pooled into one directory give the reference digest. Duplicate shards → "unit covered twice". Untagged shards pooled by copying collide on file names → coverage FATAL.
* flock refuses a second live run in the same directory.

I found no scenario in which double counting or loss is accepted silently, apart from deliberate or in-memory edits to a checkpoint's high 64 bits (F2).

**6. Streaming fails closed**, except for the parameter-binding gap (F5):

| test | outcome |
|---|---|
| S1: stream command fails | FATAL, no checkpoint |
| S2: consumed bytes differ from the verifier-hashed bytes | FATAL |
| S3: no `.sha256` | FATAL |
| S4: partial file | FATAL "short ap file" |
| S7: multi-sub-unit segment absent | FATAL |
| S8: non-executable command | FATAL |
| S9: pre-produced file with a bad companion | FATAL |
| S11: absent file, no streaming | FATAL |
| S12: selection token that selects nothing | FATAL |
| S6 (stand-in success), S10 (pre-produced with a good companion), **S13: the real `stream_seg.sh` with the certified apwit + wverify** | record identical to the full run: U 105, fp `4fe80083…`, hash `da9aee44…` |

`stream_seg.sh` takes the hash from the verifier's SEG line, moves files only after `grep` succeeds (under `set -euo pipefail`), and writes into a scratch directory, so a partially written file is never moved. The verifier's unchecked `fwrite`s are covered by the accumulator re-hashing the bytes it consumed. Remaining gaps:
* F5: parameters are not bound;
* F4: the generation directory is reused after an early crash;
* F6: the setup-table read is not covered;
* F13: companions are optional for pre-produced segments.

`posix_spawn` + `waitpid` is correct (EINTR loop; nonzero exit or a signal → fatal). The lock is O_CLOEXEC. The timing log is FD_CLOEXEC; there is a harmless race window between `fopen` and `fcntl`.

**7. The depth-n coefficient matches the certified definition** (p3_downstream.py: μ(b + pⁿZ_p) = α⁻ⁿ[b/pⁿ]⁺, b = ω(b)(1+p)^j).
* ω(b) = b^{p^{n−1}} mod pⁿ is the Teichmüller lift.
* j = log_{1+p}(b/ω(b)), taken from a table of powers of 1+p, which generates the 1-units for odd p. The weight is C(j, r).
* The sign factor α⁻ⁿ = αⁿ for α = ±1 (571, 578).

My own implementation (Hensel iteration for ω, brute-force discrete log) on the certified symbols agrees with the engine for every case I ran:

| case (p = 3, α = −1 unless noted) | LATDEN·a_{n,r} (engine = mine) | A mod 3 | UNIT_TEST |
|---|---|---|---|
| m = 27, n = 3, r = 1 | 1290240 | 0 | FAIL |
| m = 27, n = 3, r = 2 | 3262464 | 0 | FAIL |
| m = 27, n = 3, r = 6 | 1452032 | 2 | PASS |
| m = 27, n = 3, r = 7 | 464896 | 1 | PASS |
| m = 27, n = 3, r = 1, α = +1 | −1290240 | 0 | FAIL |

NONZERO_ONLY:
* Its balls contain my own balanced-residue integers Z = −387072, 258048, 81920 and −143360, with weight masses 12, 6, 6 and 4.
* The floor/ceil directions are safe: L/p is rounded down, U/p up, then ceil and floor are taken.
* It never claimed exclusion when p \| A. At this radius (1.98-5.95) it could not exclude in the unit cases either, which is sound.

For m = 81 see below. Validation gaps are listed in F7.

## Replay results

**Build.**
* The source copy is `src/acc2243v2.c`, sha256 `295a14c2…` (matches). `stream_seg.sh` is `b1378f16…` (matches); the shim is `850f29fa…` (matches); arbcore.c is `56a43aac…` (matches).
* Build command (`build.sh`, exact line as briefed): `cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations … -lflint -lmpfr -lgmp -lpthread`. It built with no warnings, on Apple clang 21.0.0 and FLINT 3.3.1.
* The resulting binary `acc_review` has sha256 `71ec3383…`. The author's binary is `794702de…`; binaries differ and that is expected. The arithmetic outputs are identical.
* Shim test: all FIPS vectors pass, including one million 'a' fed through odd-sized updates, and real files match `shasum`. I did not do a Linux build.

**m = 27** (`run_m27.sh`; W = 4 per the coordinator's cap).
* Command: `acc_review run 0 -22735 0 106272484 0 27 2167729337579528 1 4831838207 16777216 $AP 4 m27 500000000 40`.
* 1445 units (293 L + 1152 S). 343.4 s wall; 1357.9 user + 5.4 sys = **0.379 CPU-h**; peak RSS 365 MB.
* Merges: `ACC_DFT=0 … merge … m27 1024 > m27_merge_direct.txt` and `ACC_DFT=1 … > m27_merge_dft.txt`, plus six weighted merges (`m27_merge_w*`).

| output | value |
|---|---|
| MERGE | 4 checkpoints; 0 missing; 2169602069 terms |
| FINGERPRINT | `ac56a61d710b8d46`, match |
| COUNT | smooth 1580993508 + pairs 3250844699 = T |
| AP_SEGROOT_SHA256 | `ca234d65fa40332695f5f08675ade782c9a8439bee068b69ac9b64a470002084` (= certified) |
| **CHUNK_DIGEST** | **`e24f3f4d4e705b42e6002bf8059430aa73ae3315bc437d2665bd99d151330681`** (= the author's value; bit identity across independent builds and W) |
| ROUNDING_ERR_TOTAL | 5.4768·10⁻²⁰ |
| TAIL_MS_UPPER_TIMES2 | 1.358052210·10⁻⁵ (= certified; my mpmath gives 1.35805220954·10⁻⁵) |
| max plus radius | 4.842421·10⁻⁴ against the uniqueness threshold 4.882812·10⁻⁴ (margin 4.04·10⁻⁶ in symbol units) |

My comparator (`tools/indep_merge.py`, output in `m27_indep_compare.txt`) is an independent merge in exact rationals, read directly from the checkpoint bytes. It reports **INDEP_MERGE_PASS, 0 failures**:
* 4/4 SHA trailers;
* coverage 1445/1445;
* fingerprint recomputed with my own splitmix64;
* count identity;
* CHUNK_DIGEST recomputed = the engine's value;
* 27/27 class sums within E + rad_cert of the certified exact SDUMP balls (max \|diff\| 1.13·10⁻²⁵);
* 27/27 printed S_k balls overlap the certified printed balls, on both paths;
* **18/18 plus and 18/18 minus symbols exactly equal to SYMBOLS_m27.txt with contains = unique = 1, on both the direct and DFT paths**; 36/36 printed balls contain the certified value;
* mpmath re-derivation from the exact sums: max \|x⁺ − certified\| = 7.3·10⁻¹¹ and max \|x⁻ − certified\| = 2.5·10⁻¹⁰, against a 4.84·10⁻⁴ budget.

Note: SYMBOLS_m*.txt lists symbol **values** (for example 70, which is 71680/1024), not numerators in units of 1/1024 as the brief says; the certified `msl_m27.txt` XB lines confirm this.

**m = 81** (`run_m81.sh`; W = 3, which left one slot for the W = 1 adversarial runs).
* Command: `acc_review run 0 -22735 0 106272484 0 81 2167729337579528 1 14847836159 16777216 $AP 3 m81 500000000 40`.
* 4440 units (900 L + 3540 S). 1296.5 s wall; 3857.1 user + 14.0 sys = **1.075 CPU-h**; peak RSS 285 MB.
* Merges: `merge_m81.sh`, with `ACC_DFT=0` and `ACC_DFT=1` and trailing weights `3 4 2 -1`, plus r = 1, 6 and 7 on the DFT path.

| output | value |
|---|---|
| MERGE | 3 checkpoints; 0 missing; 6667005863 terms (= certified Σ nnz) |
| FINGERPRINT | `c50fd86d63d4db43`, match |
| COUNT | smooth 4841666641 + pairs 10006169518 = T (= certified) |
| AP_SEGROOT_SHA256 | `5f9994d95c31a49e7cbd91435fd33a9cbdadc81fcc4f47439fbbf2fa5bb4713f` (= certified) |
| SMOOTH_MERKLE | recomputed from the stored leaf hashes: `1b1f1929…` (= certified) |
| **CHUNK_DIGEST** | **`04a7d9527f294aef11be2347a14ee83dba1b3bf22bb3560a3c1494789623a998`** (= the author's value) |
| E | 1.683·10⁻¹⁹ (err/nterm = 2.0000) |
| TAIL_MS_UPPER_TIMES2 | 1.333053816·10⁻⁵ |
| max plus radius | 4.753284·10⁻⁴ (margin 1.30·10⁻⁵) |
| symbols | 54/54 plus and 54/54 minus determined; direct and DFT XB and S lines identical |
| **A_EXACT** (r = 2, α = −1) | **15851520 = 1024·15480, UNIT_TEST FAIL** (3 divides it), as required |
| NONZERO_ONLY | ball [2.580e5 ± 56.8] (the printed radius includes decimal rounding), EXCLUDES_pZ 0, which is sound |

My comparator (`m81_indep_compare.txt`) reports **INDEP_MERGE_PASS, 0 failures**:
* 81/81 exact class sums within E + rad_cert of the certified SDUMP balls (max \|diff\| 1.35·10⁻²⁵);
* 81/81 printed balls overlap the certified balls, on both paths;
* **54/54 plus and 54/54 minus symbols exactly equal to SYMBOLS_m81.txt with contains = unique = 1, on both paths**; 108/108 balls contain the certified value;
* mpmath re-derivation: max \|x⁺ − certified\| = 7.5·10⁻¹¹ and max \|x⁻ − certified\| = 9.4·10⁻¹¹.

`tools/weights.py` on the certified symbols (`m81_weights_compare.txt`) agrees with the engine:

| r | LATDEN·a_{4,r}, engine = mine | UNIT_TEST |
|---|---|---|
| 1 | −55296 | FAIL |
| 2 | 15851520 | FAIL |
| 6 | 61204809728 (mod 3 = 2) | PASS |
| 7 | 189123254272 (mod 3 = 1) | PASS |

The minus symbols at m = 81 include values of 0, ±3, ±5 and others, so the minus-sign convention is pinned at m = 81 as well as at m = 27.

**CPU used by this review:** m = 27 0.379 + m = 81 1.075 + adversarial and plumbing runs ≈ 0.1, for **≈ 1.56 CPU-h**, within the 3.5 CPU-h cap.

## Adversarial outcomes

All tests ran on copies inside `adv/`. Results are in `adv_ckpt_results.txt`, `adv_stream_results.txt`, `adv_restart_results.txt`, `adv_setup_table_results.txt` and `adv_m2243_plumbing.txt`.

| test | outcome |
|---|---|
| A1: flip one array byte, trailer not fixed | FATAL "ckpt self-hash mismatch" |
| A2: flip a low-half byte (bits 24-31), re-hashed | FATAL "fingerprint mismatch" |
| **A3: flip a high-half byte (bits 64-71), re-hashed** | **accepted** (exit 0); only the digest changes |
| **A3b: flip bit 96 (S_5 changes by 1.0), re-hashed** | **accepted**; 18+18 symbols "identified", all wrong |
| **A3c: add n·2⁶⁴ to S_0 with n = round(Ω⁺/2·2³²), re-hashed** | **accepted**; every plus symbol is +1, all "identified" |
| A4: delete one U line, re-hash only | FATAL "ckpt record" |
| A5: delete one U line, fix NREC, re-hash | FATAL "units missing" (fingerprint mismatch printed as well) |
| A6: duplicate checkpoint under a matching name | FATAL "unit covered twice" |
| A6b: duplicate as `.tmp` | ignored (correct) |
| A6c: remove one checkpoint | FATAL "units missing" (the fingerprint still matches) |
| A6d: truncated checkpoint | FATAL "ckpt not terminated" |
| A7: merge with m = 81, T − 1, sign −1, Q + 2, a4 + 1 or SEGQ 2²⁵ | FATAL "merge command line does not match the checkpoints' PARAMS" (Q + 1: FATAL gcd) |
| A8: move a U record between checkpoints, both re-hashed | accepted, identical result (harmless) |
| A9: pooled checkpoint with UT edited | FATAL "PARAMS differ" |
| A10: ACC_SELECT given at merge for a full run | FATAL |
| A11: run with a different UNIT_TERMS in a finished directory | FATAL "PARAMS differ" |
| A12: rerun on a complete directory | no-op, generation 2 |
| A13: full-run S cnt + 1 | FATAL "count identity fails" |
| A14: unreadable checkpoint | FATAL "unit covered twice" (F8) |
| Streaming S1-S13 | see check 6 (only S5, the parameter mismatch, is accepted) |
| R1b: second live run in the same directory | FATAL flock |
| R2, R3, R4 | digest equals the reference |
| R5 (duplicate shard), R6 (untagged pool) | FATAL |
| R7a | FATAL recount |
| R7b | accepted (documented) |
| F6 shard with a divergent setup table | accepted |

## What this review does NOT establish

* **Production size.** Only small cases were replayed: m = 27 (T = 4.83·10⁹) and m = 81 (T = 1.48·10¹⁰). Plus a plumbing run at m = 2243 with T = 2²⁴−1 that identifies nothing. None of the following was replayed or measured:
  * the production numerics at m = 2243² = 5 031 049 and T ≈ 3.9·10¹³: DFT radius growth at that length, the 4.8·10⁻⁷ identification margin, `div_period` at that size, the magnitude of E;
  * runtime, memory, and 80 MB checkpoints;
  * multi-machine or cloud behaviour, and other FLINT versions or Linux builds (the digests are expected to match only for the same FLINT arithmetic).
* **The lattice hypothesis** x_b ∈ (1/1024)Z (M7) is an external mathematical input and was not checked. Neither was the tail bound `tail_ms` (copied verbatim from the certified core); I only reproduced its value numerically. The period formula was cross-checked numerically, not proved.
* **Producer and verifier soundness** (apwit, wverify) were not reviewed. The stream path was exercised with stand-in commands and one real segment.
* **FLINT/Arb correctness** is assumed. I only spot-tested the conventions and primitives the engine relies on.
* **The author's summaries** (S5_RESULTS.md, final_driver.log) were read only after this verdict was formed; see below. The Codex review was not consulted for this verdict.
* **Thread cap.** For about one minute, test R2 ran with W = 2 while the m = 81 run held W = 3. That is one thread over the coordinator's cap of 4. Every other run respected the cap.

## Comparison with the author's summaries (read after the verdict above was written)

Sources: `S5_pipeline/S5_RESULTS.md` and `S5_pipeline/tests/final_driver.log`.

**Where the author and I agree:**
* The m = 27 and m = 81 CHUNK_DIGESTs match my build: `e24f3f4d…` and `04a7d952…`.
* A_EXACT = 15 851 520 with UNIT_TEST FAIL.
* DFT and direct candidates and flags are identical.
* `div_period` cuts the m = 81 maximum radius to 4.753284·10⁻⁴, exactly my value.
* The v2.1 2E argument and the portable SHA-256 shim check out.
* The negative controls I repeated gave the same outcomes: duplicated, corrupted and missing checkpoints; wrong selection; bad token; failing producer; tampered stored a_q.

**Where I disagree or add to the author's account:**

1. **"The arithmetic is unchanged", and the brief's "verbatim … the only change is `read_apseg`".** This is true relative to S2 but not relative to arbcore. See F1: the r-chain now includes primes with a_q = 0, and Part L is split into sub-units. This is harmless, but it was not declared.

2. **S5 defect 1 says the orphan hazard is "closed by two independent guards".** One of those guards, per-generation stream directories, does not hold after a crash that happened before the first checkpoint (F4, reproduced in R3: the restart runs as generation 1 again). The author's R5-B tested only a restart after checkpoints had been written (generation 2).
   * Defect 5's statement that "orphans … write only into their own per-generation stream directories" has the same gap.
   * The remaining guard is the consumed-bytes hash check. It is sufficient against the zero-filled-hole race described there: a file with holes cannot match the verifier's hash. So the hazard stays fail-closed, but it rests on one guard, not two.

3. **The author's own R5-M line confirms F3 at production size.** On a *meaningless* partial selection, 5 023 954 of 5 028 806 plus symbols (99.9%) were "determined". So at the 4.8·10⁻⁷ margin, identification carries no evidence about the correctness of the class sums. The author labels these values meaningless, which is correct. The consequence for integrity checking (F2 + F3) is not drawn in S5.

4. **Not mentioned in S5 at all:**
   * F2: the fingerprint misses the high 64 bits;
   * F5: stream parameters are not bound to PARAMS;
   * F6: the setup table is not bound;
   * F7: weights input validation;
   * F8: the `read_ckpt` return path;
   * F13: companions are optional for pre-produced segments.

   F13 matters in production because `plan` lists **2048 segments (0-2047) that must be pre-produced** at UNIT_TERMS = 10⁹. Their verifier `.sha256` companions should be kept next to them, so that the run-time check applies. Otherwise only an external AP_SEGROOT comparison would catch a bad file.

   On F6: at production, segment 0 is a multi-sub-unit segment. In a full sharded run, the cross-sub-unit hash check catches a shard with a divergent segment 0 provided every shard processes at least one segment-0 sub-unit. That mitigates F6 in the full-run case, but not for selections.

5. **The author's "Not validated" list** (Linux/cloud bit identity, 64+ core throughput, checkpoint compaction) remains open. My review adds nothing on those.

## Comparison with the concurrent Codex review (read only after my verdict and findings above were written)

Source: `/Users/bsm/BSD_2243_ACC_CODEX_CHECK_2026-09-23/REVIEW.md`, together with its JSON artefacts `RESULT.json`, `NEGATIVE_TESTS.json`, `REPLAY_COMPARISON.json` and `INTEGER_RANGE_BOUNDS.json`. Nothing in that folder was used for the findings F1-F13 or the replays.

**Agreement on the facts.**
* Both reviews reproduce the m = 27 digest `e24f3f4d…` and segment root `ca234d65…` on independent builds.
* Both confirm 18 + 18 and 54 + 54 exact symbols on both paths, and A_EXACT = 15 851 520 with UNIT_TEST FAIL.
* On "verbatim": Codex also finds the claim too strong, and also notes that `run_L` advances the exponential through a_q = 0. This is my F1.
* Both find E to be a valid ℓ1 bound, the DFT signs correct, `div_period` valid, and the weights correct.
* Both give an integer-range argument that rules out i128 overflow at production size. Codex bounds the per-class term count (121 bits); I bound the global ℓ1 sum Σ d(n)n^{-1/2} (124.6 bits). Either suffices.
* The fingerprint misses high bits under a forged SHA (my F2, which I also demonstrated for in-memory-style edits).
* `load_table` does not authenticate its small-prime input (my F6, which I demonstrated with a silent pooled merge).
* **Generation reuse before the first checkpoint** (my F4). Codex demonstrated it more directly than my R3 did: an orphaned stream child and the restarted child were both live in `stream_g001_w00` for the same segment, with 0 checkpoints.

**Disagreement: the verdict label for F4.**
* Codex: **FAIL** "for the claimed crash/restart isolation of v2.3", while saying that the arithmetic core passed and that no falsely certified result was demonstrated.
* Me: **PASS_WITH_CORRECTIONS**, with F4 a major, blocking correction.

We agree the claim is false and that the fix is required before production (a durable fresh generation id, or unique scratch directories, plus a test of an early crash and of a repeated early crash). We disagree on whether a false, fail-closed isolation property should fail the whole engine.

My grounds for not failing the engine:
* With the same configuration, the orphan and the new child produce identical a_q bytes.
* Any interleaving that corrupts a file (holes, truncation) cannot match the verifier's SEG hash, so the accumulator stops. See the tests S2 and S4.
* A silent wrong result needs **in addition** an orphan running with *different* stream parameters (F5), plus a narrow race between the separate moves of `.bin` and `.sha256`.

In my independent pass I rated F4 minor. Reading Codex's review made me re-examine the production restart path. There, a parent-only kill (for example the OOM killer choosing the multi-GB accumulator while ~200 s producer children continue), followed by an automatic restart before the first checkpoint, is plausible. So I raised F4 to major. The verdict label is unchanged.

**Covered by my review and not by Codex:**
* a **fresh** m = 81 summation (digest `04a7d952…` equal to the author's; Codex merged copied checkpoints only);
* S5, silent acceptance of verifier output for mismatched parameters (F5);
* F3, identification accepting ~99% of arbitrary values; corroborated by the author's own R5-M line (99.9% "determined" on a meaningless partial selection);
* A3c, a lattice-aligned tamper that shifts every plus symbol by +1 with every check passing;
* F7, alpha silently treated as ±1;
* F8, the `read_ckpt` undefined-behaviour path;
* F13, companions optional for the 2048 pre-produced segments;
* the SIGN = −1 DFT path (m = 27 re-merge and m = 2243 plumbing);
* my own primitive tests of the FLINT functions the engine relies on, done offline. Codex instead fetched the FLINT source for `mag_get_d`.

**Outside this engine review:** Codex's D2/D5 and period-normalization remarks (plus period ω₁ versus 2ω₁) concern the mathematical inputs, not the engine. I did not assess them.
