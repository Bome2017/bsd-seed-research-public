# RESUME — independent review of acc2243v2.c (v2.3), started 2026-09-23 07:49 PDT

Role: independent reviewer (fresh context). Verdict PASS / PASS_WITH_CORRECTIONS / FAIL. Report only, no repairs.
Write ONLY in this folder. Sealed folders read-only. <=8 heavy threads, <=3.5 CPU-h total. No p=17. No network.
Do NOT read author summaries (S5_RESULTS.md, tests/final_driver.log) until verdict formed.

## Plan
1. hash sources; read acc2243v2.c, stream_seg.sh, shim, CODEX_CHECK_REQUEST.md, arbcore.c
2. diff kernel vs arbcore.c; checks 1-7 notes -> notes_checks.md
3. build own binary acc_review; m=27 run (W=8) in background; merges direct + DFT
4. own comparator (python exact rationals) vs SYMBOLS_m27.txt / msl_m27.txt
5. adversarial tests on copies of m27 dir
6. optional m=81
7. REVIEW.md

## Progress log
- 07:49 folder created
- 07:55 COORDINATOR UPDATE: Codex reviewer runs its own m=27 replay concurrently (8 threads). From now on W<=4 and <=4 heavy
  processes at once. Do NOT read/copy anything in /Users/bsm/BSD_2243_ACC_CODEX_CHECK_2026-09-23/ until my verdict is written;
  afterwards a separate REVIEW.md section may note disagreements.
- 07:55 source hashes verified (acc2243v2.c 295a14c2..., stream_seg.sh b1378f16..., shim 850f29fa..., arbcore.c 56a43aac...).
  Read acc2243v2.c fully, arbcore.c fully, stream_seg.sh, shim, CODEX_CHECK_REQUEST.md.
- 07:56 built acc_review (sha 71ec3383..., author binary 794702de... differs: expected, different build path; source hash equal).
  FLINT 3.3.1, Apple clang 21. No compiler warnings. m=27 run launched 07:55:54 (W=4, bg), dir m27/, log m27_run.log/.time.
  1445 units = 293 L-subunits + 1152 S-blocks.

## Working findings (draft; to be confirmed)
F-a run_L is NOT verbatim arbcore do_lseg: r=e^{-kq} chain now updated for every prime q>RT incl. a_q=0 (arbcore: only a_q!=0),
    sub-unit m-ranges with arb_pow_ui(r, ms-1), early break when T/q < m0, pairs counted per sub-range. Mathematically valid
    (ball enclosures); needs mention since the header/brief claim "verbatim". gen_block lost use_table (msl used 0 anyway). invmod
    replaced (brute force -> ext. Euclid; checked OK).
F-b fingerprint is mod 2^64 on the LOW 64 bits of i128 values: any change in the high 64 bits of an acc entry is invisible to it
    (SHA trailer is the only guard; a re-hashed tampered file passes). To demonstrate adversarially.
F-c overflow guards heuristic: i128 acc between checkpoints and merge tot[k] have no overflow check; wrap would be invisible to
    the mod-2^64 fingerprint. Realistic magnitudes (class l1 <= ~2^14 at m=27, ~2^6 at 2243^2) make it moot. note/minor.
F-d stream dir per generation is NOT guaranteed distinct: GEN = 1+max ckpt gen; a killed run that wrote no checkpoint -> restart
    reuses the same GEN and stream_gXXX_wYY dirs (orphans may share). Fails closed via hash compare, spurious failure only. minor.
F-e stream_seg.sh parameters (CURVE default seed, SEGQ hardcoded 2^24, QB, T_RUN env) are not bound to the accumulator's PARAMS;
    only segment+dir passed. Curve mismatch -> verified a_q of the WRONG curve, right length, hash matches -> silently consumed.
    Operator-error path; minor (major if generic use intended).
F-f weights: alpha not validated in {+1,-1} (alpha=2 treated as +1); p not checked prime; gcd(p, LATDEN) not checked. minor.
F-g merge ignores S-block leaf hashes (arbcore printed SMOOTH_MERKLE_SHA256); audit trail reduced. note.
F-h SYMBOLS_m27/m81 files hold VALUES (70 = 71680/1024), not units of 1/1024 (brief wording); certified msl XB lines confirm.
- 08:01 m27 run DONE: 343 s wall, 1357.9 user + 5.4 sys CPU-s (0.379 CPU-h). Merges direct + DFT + weights done.
  CHUNK_DIGEST e24f3f4d...330681 == author; AP_SEGROOT ca234d65... == certified; COUNT == certified.
  tools/indep_merge.py: ALL PASS (coverage, own fingerprint, count, digest recomputed, 27/27 class sums within E of certified
  SDUMP (max diff 1.1e-25), 18/18 plus + 18/18 minus EXACT, both paths; mpmath rederivation OK). -> m27_indep_compare.txt
  weights m27 n=3: A_EXACT r=1 1290240, r=2 3262464, r=6 1452032 (PASS mod3=2), r=7 464896 (PASS mod3=1) == reviewer
  tools/weights.py; alpha=2 silently treated as +1 (F-f confirmed). NONZERO_ONLY balls contain own Z_int; never excludes wrongly.
  acb_dft convention checked (tools/dftconv): exp(-2 pi i jk/n) at n=7,27,81,2243,6561.
- 08:05 launching m81 (W=3) in background; adversarial runs W=1 alongside (<=4 heavy threads).
- 08:07 adv_ckpt.sh -> adv_ckpt_results.txt: A1 no-fix flip -> self-hash FATAL; A2 low-half flip rehashed -> fingerprint FATAL;
  A3 high-half flip rehashed -> ACCEPTED (digest differs, symbols same); A3b bit-96 flip -> ACCEPTED, 18/18+18/18 "identified"
  but WRONG (identification is ~99% for arbitrary values: radius 4.842e-4 vs half-spacing 4.883e-4); A3c +n*2^64 on S_0 ->
  every plus symbol +1, all "identified", fp/coverage/count pass (concrete silent-wrong input). A4 delU -> "ckpt record";
  A5 delU+NREC -> "units missing" (fp mismatch too); A6 dup -> "unit covered twice"; .tmp dup ignored; missing ckpt -> coverage
  (fp still matches!); truncated -> "not terminated"; m/T/sign -> PARAMS FATAL; Q+1 -> gcd FATAL; A8 record moved -> accepted,
  identical; A9 UT edited -> PARAMS FATAL; ACC_SELECT at merge -> FATAL; run with other UT -> FATAL; rerun complete -> gen 2 no-op.
- 08:09 adv_stream.sh -> adv_stream_results.txt: fail/tampered/nohash/partial/multi-absent/non-exec/pre-produced bad sha/absent
  all FATAL; copy_ok, pre good sha, and REAL stream_seg.sh (certified apwit+wverify, 48 CPU-s) give the IDENTICAL record as the full
  run (U 105 fp 4fe80083... hash da9aee44...). wrongparams (verifier output of wrong params with its own consistent hash) ->
  ACCEPTED silently (F-e confirmed).
- 08:10 adv_restart.sh running (W=1 except R2 which used W=2 for ~1 min: brief 5-thread excursion with m81 W=3 -- deviation noted).
  R1b flock FATAL OK; R2 crash(13 units)+restart gen 2 digest == ref b63083a2...; R3 crash before first ckpt -> restart is
  generation 1 again (F-d confirmed); digest == ref.
- 08:12 adv_restart.sh done -> adv_restart_results.txt: tagged shards pooled == ref digest b63083a2...; single shard -> coverage
  FATAL; duplicate shard (tag C) -> "unit covered twice"; untagged shards pooled by cp (name collision) -> coverage FATAL;
  L cnt+1 (selection) -> recount FATAL; S cnt+1 (selection) -> ACCEPTED (documented limitation); full-run S cnt+1 -> identity FATAL.
- 08:13 adv_setup_table.sh -> adv_setup_table_results.txt: F-i CONFIRMED: shard with divergent segment 0 (a_5 -2 -> 0) pools
  silently (coverage/fp/recount pass, AP_SEGROOT identical to reference, only CHUNK_DIGEST differs). In a full sharded run the
  cross-sub-unit hash check on multi-sub-unit segment 0 would catch it if every shard processes a segment-0 sub-unit.
- 08:14 SMOOTH_MERKLE recomputed from my m27 S-block leaf hashes == certified 71635921... (a_n streams bit-identical).
- 08:16 tools/primitives.c: mag_get_d upper bound + exact ldexp (0/200k), arf_get_fmpz_fixed_si err < 2^-96 (0/200k),
  div_period enclosure (0/120k point checks); [1.5 +- 1.4e-5]/Omega+: arb_div radius 4.99398e-4 vs div_period 4.99199e-4.
- 08:17 unreadable checkpoint (chmod 000 copy): merge FATAL "unit covered twice" -- read_ckpt returns 0 with ck uninitialized,
  callers ignore the return (UB; stale previous ck reused). Fail-closed in practice, misleading message. minor.
- 08:18 certified units_m27 sum nnz = 2169602069 == my nterm; pairs/smooth equal.
- m81 running (2360/4440 at 08:15); waiter task basw3yshu.
- 08:20 shim (compat CommonDigest.h) OK: FIPS vectors incl. million-a with odd update sizes; real files == shasum.
- 08:21 sign -1: m27 checkpoints with PARAMS edited s=1->s=-1 (class sums are sign-independent): direct == DFT XB lines;
  tools/sign_check.py: 36/36 balls contain own mpmath formula value (both signs). m=2243 plumbing (T=2^24-1, Q=Q/2243, both signs):
  symbols.bin byte-identical direct vs DFT (prime-length Bluestein/Rader path). Results in adv_m2243_plumbing.txt.
- 08:22 REVIEW.md drafted (verdict PASS_WITH_CORRECTIONS; m81 + author-comparison placeholders)
- 08:25 m81 run DONE: 1296.5 s wall, 3857.05 user + 14.03 sys (1.075 CPU-h), W=3. Merges direct+DFT with weights 3 4 2 -1:
  CHUNK_DIGEST 04a7d952...a998 == author; AP_SEGROOT 5f9994d9... == certified; COUNT == certified; SMOOTH_MERKLE 1b1f1929... ==
  certified; nterm 6667005863 == certified nnz; 81/81 class sums within E (max diff 1.35e-25); 54/54 + 54/54 EXACT both paths;
  A_EXACT 15851520 (=1024*15480) UNIT_TEST FAIL (as required); r=1 -55296, r=6 61204809728 PASS, r=7 189123254272 PASS == mine.
  CPU total so far ~1.56 CPU-h (m27 0.379 + m81 1.075 + adversarial ~0.1).
- 08:26 verdict written (REVIEW.md, m81 filled). NOW reading author summaries S5_RESULTS.md + tests/final_driver.log
- 08:27 author summaries read; comparison section written. Verdict unchanged. Now (after verdict) looking at Codex folder.
- 08:28 Codex REVIEW.md read AFTER verdict; comparison section appended; F4 raised minor->major after re-examination (verdict label unchanged).
- 08:33 integrity check: no file in the sealed folders is newer than my build.log; sources' hashes unchanged. One file in the
  pilot-prep folder (S4_cost/S4_COST_RECONCILIATION.md, mtime 07:59) changed during my run -- NOT written by me (another session).
- DONE. Final: REVIEW.md verdict PASS_WITH_CORRECTIONS (F4 major, fail-closed; F1-F3,F5-F8 minor/notes). CPU ~1.56 CPU-h.
