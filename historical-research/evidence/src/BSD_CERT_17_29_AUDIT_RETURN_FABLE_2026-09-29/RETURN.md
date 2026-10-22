# RETURN — outside numerical-output audit of the singleton certificates at p = 17, 19, 23, 29

**Status per run (2026-09-29):**

| Run | Status |
|---|---|
| p = 17, ℓ = 103 | **PASS_AT_RETAINED_GRADE** |
| p = 19, ℓ = 191 (v2) | **PASS_AT_RETAINED_GRADE** |
| p = 23, ℓ = 47 | **PASS_AT_RETAINED_GRADE** (kill test passed first) |
| p = 29, ℓ = 233 (v2) | **PASS_AT_RETAINED_GRADE** |

No DEFECT and nothing UNVERIFIABLE was found.

**Grade.** The reviewer is Claude Fable 5.1 (Anthropic). The runs were produced by Claude sessions, so this is an
independent audit by a model of the **same family** (MODEL_SAME_FAMILY). It is not the cross-family Batch C grade;
upgrade only after a cross-family check. The retained Ota, rank, image, Manin/lattice, engine and corpus imports
are unchanged and are not re-proved here.

Not audited, as instructed: p = 19 run 1 (INVALID, sealed); p = 29 at ℓ = 59; p = 29 at ℓ = 233 v1.

## Results

| | p=17 | p=19 | p=23 | p=29 |
|---|---|---|---|---|
| freeze commit → cert head | 7248cf5 → 2ca4604 | 2dd268d → bba95ca | 0f4683d → fd51a7e | 29aabc1 → 5459a7d |
| freeze commit → run start (UTC) | 14:26:26 → 14:26:39 | 20:00:29 → 20:00:38 | 15:13:10 → 15:16:37 | 20:54:26 → 21:07:27 |
| T (segments) | 33,218,887,679 (1980) | 65,783,463,935 (3921) | 14,914,945,023 (889) | 80,564,191,231 (4802) |
| receipt root (recomputed = pin) | 55095730… | 58d28b37… | a83f42e3… | c329c118… |
| balls identified exactly | 204 | 380 | 92 | 464 |
| max radius / min gap to next point | 4.85e-4 / 4.92e-4 | 1.24e-4 / 8.53e-4 | 4.84e-4 / 4.93e-4 | 1.23e-4 / 8.54e-4 |
| g; c0, c1, c2 | 5; 0, 7242, 46298 | 19; 0, −3572, −30432 | 5; 0, 9430, 103854 | 3; 0, 2320, −98942 |
| c1/p; **c2 mod p** | 426; **7** | −188; **6** | 410; **9** | 80; **6** |
| primitive roots tested | 32 | 72 | 22 | 112 |
| altered tables rejected | 11/11 | 11/11 | 11/11 | 11/11 |
| frozen checker replay | NONZERO, exit 0, identical | same | same | same |
| a_p (reduction); #E(F_p); #E(F_ℓ) | −6 (ord); 24; 106 | 4 (ord); 16; 202 | 0 (ss); 24; 44 | 0 (ss); 30; 248 |

Totals: **1,140 intervals**, 238 primitive roots, 44 altered tables plus 8 binding controls plus 12 recombination
controls, all rejected. CPU use was under one CPU-minute, one process at a time, against the 4 CPU-h cap.

## Checks (scripts in `checks/`, outputs in `out/`)

**Scope of the frozen checker, in its own words.** `singleton_check.py` says: "the label set must be exactly the
units mod l, each exactly once; unique lattice points". It reads the printed `cand`/`contains`/`unique` fields and
does not recompute them from the ball endpoints. My checks do recompute them, as listed below.

1. **Input identity** (`bind_pkg.py`, `bind_run.py`). All four PASS.
   - Each package repo has one commit, the pinned freeze. Its tree is clean: `status --porcelain --ignored` is
     empty and every blob equals `hash-object` of the working file.
   - The freeze-manifest file hashes match. The engine binary is 47d07f2e…, as pinned; the engine source is 56a43aac….
   - `singleton_check.py`, `run_singleton.sh` and `test_singleton_check.py` are byte-identical to the hashes that Batch C
     recorded.
   - LAUNCH_COMMAND equals the manifest and names the frozen launcher.
   - Chronology holds: manifest stamp ≤ commit < start < end.
   - PARAMS equals the launch command, RUN_MANIFEST and the report.
   - The receipt root was recomputed from exactly one tiled `SEG` receipt per segment. It equals the pin and the
     engine's AP_SEGROOT.
   - Each lab cert branch's parent is the same freeze commit with the identical tree. The result commit only ADDS
     files under `results/`. Its msl.txt, manifest, report, check.log and PARAMS equal the on-disk run bytes. All
     work units match UNITS_MANIFEST (9901, 19606, 4446 and 24011 files).
   - T ≥ the planner's TMIN, and T+1 = segments·2²⁴.
2. **Exact-rational interval check** (`intervals.py`). The endpoints of every printed ball are parsed to exact
   fractions, and ceil(1024·lower) = floor(1024·upper) is required. That integer must equal the printed candidate
   over 1024. Labels must be exactly 1..ℓ−1, each once; plus symbols symmetric and minus symbols antisymmetric.
   COUNT must give smooth + pairs = sum = T at the frozen T, with identity 1. `XB_PLUS_DETERMINED` must be ℓ−1 of ℓ−1.
   All PASS. Every identified plus symbol is an integer.
3. **Coefficients** (`coeffs.py`). c_k = Σ C(ind_g(a) mod p, k)·[a/ℓ]⁺ in exact rationals, with g the least primitive
   root. The results: c0 = 0 exactly, c1 ≡ 0 (mod p), c2 mod p nonzero and equal to the report, and the generator
   matches.
   - For every primitive root h, found by its own discrete-log walk: c0 = 0, c1 ≡ 0, and c2(h) = c2(g)·u⁻² (mod p)
     with h = g^u.
   - Each orbit is exactly c2·(F_p^×)², so nonvanishing is preserved.
4. **Negative controls** (`controls.py`). The 11 altered tables per run were all rejected: duplicate label, missing
   label, changed candidate, ball with several lattice points, empty ball, plus symmetry broken, minus antisymmetry
   broken, extra label ℓ, COUNT off by one, wrong denominator, and a wide ball whose printed `unique 1` flag was kept.
   The last one shows the check does not rely on engine flags.
   - `bind_controls.py` on p = 23 rejected 8 of 8 altered bindings: wrong freeze commit, wrong cert head, engine pin,
     checker pin, pinned root, T + one segment, manifest msl hash, and one receipt digest altered in a copy.
5. **Replay** (`replay.py`). The package's frozen `singleton_check.py` (hash-checked) ran under `python3 -B` on the
   genuine outputs and the original receipt globs. Only `--out` pointed into this folder. Exit 0, empty stderr,
   **NONZERO**. The JSON is identical, key for key, to both SINGLETON_REPORT.json and logs/check.log.
6. **Ota hypotheses as used** (`hyps.py`, `hyps.gp`, `hyps_sage.sage`). Checked at each (p, ℓ):
   - p ≥ 5 is prime, p ∤ 6N, p ∤ Tamagawa product 16 (PARI reproduces N and 16).
   - p ∤ #E(F_p): my own count agrees with PARI.
   - p ≥ rank 2.
   - ℓ is prime, ℓ ∤ pN, ℓ ≡ 1 (mod p), v_p(ℓ−1) = 1.
   - p ∤ #E(F_ℓ), so E(F_ℓ)[p] = 0 is cyclic; the group is cyclic in PARI.
   - The mod-p image is surjective (Sage `is_surjective` returns True): corroboration of the retained input.
   - The production model is the minimal model under x ↦ x + 7578 (u = 1), so it is the same curve with the same
     ω₁. PARI's periods agree with the engine's Ω± balls.
   - c0 = 0 and c1 ≡ 0 are consistent with Ota 5.17 at rank 2.

   Retained, not re-verified:
   - the theorem statements;
   - the lift from mod p to the p-adic image;
   - applicability at the **supersingular** primes 23 and 29 (a₂₃ = a₂₉ = 0). The criterion as recorded in
     TARGET_R1 §2 has no ordinary hypothesis, and source audit item 5 confirmed this;
   - rank 2, c_E | 512, the 1/1024 lattice, the engine, and the corpus behind the receipt roots.

**Extra check, beyond the Batch C method** (`recombine.py`).
- Every XB symbol was rebuilt from the engine's per-residue sums S_k. These were read exactly from SDUMP, and each
  lies inside its printed S ball.
- The rebuild used mpmath interval arithmetic, PARI's periods, and a tail bound I recomputed from the engine's
  documented formula; it agrees with the printed TAIL_MS_UPPER_TIMES2 to better than 1e-8.
- All 1,140 rebuilt balls identify the same lattice points. Three controls per run were rejected: S₁ perturbed,
  wrong Q in u_b, Ω doubled.
- This tests the final combination stage only. The S_k summation and the tail-bound theorem remain retained.

## Observations (not defects)

- **p = 17 and p = 23 margins.** Their radii are 99.3% and 99.1% of the half-spacing 1/2048, because T sits just
  above TMIN on the 1/1024 planner. Uniqueness is exact for the rigorous balls, but it has almost no slack against
  an error in the retained tail bound, which enters the radius at full size.
  - Supporting, not proof: the truncated-sum centres lie at most 1.01e-10 from their lattice points (p = 23; 7.5e-11
    at p = 17), against radii of about 4.8e-4.
  - The v2 runs at 19 and 29 have radii of about 1.2e-4.
- **p = 19 chronology.** The manifest stamp 20:00:28Z is 1 s before the commit at 20:00:29Z. The run starts at
  20:00:38Z. My first test demanded the two be equal; the order is correct, and this is not a defect.
- **p = 17 launcher log.** No separate launcher stdout log was found in the package or in `singleton_probe/`.
  Launch custody rests on logs/check.log, msl.err (time -l), RUN_MANIFEST and the identical cert-17 bytes.
- **Engine stderr.** For all four runs, msl.err holds only the time -l output.
- **Not rehashed.** The large coefficient/witness files were not rehashed and their arithmetic verification was not
  rerun. That remains the bound corpus-check evidence, as in Batch C.
- **Custody.** `find -newer` shows no file changed in any source folder. Git ran with `--no-optional-locks`. Nothing was
  pushed or messaged, no subagent was used, and no producer, corpus or certificate run was made.

## Summary line for the v0.2.5 qualifier

17, 19, 23, 29: independent same-family model audit (reviewer Claude Fable 5.1, Anthropic Claude family;
MODEL_SAME_FAMILY) of the numerical outputs gives **PASS_AT_RETAINED_GRADE** for all four. It covers 1,140 exact
interval identifications, the frozen-checker replays, recomputed receipt roots and the prime-specific hypotheses. It
is not a cross-family audit, and the large corpus files were not rehashed.

FIN, ORDER9 and Q36 are unchanged.
