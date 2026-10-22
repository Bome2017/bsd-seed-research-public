# Lane 3 / B_invariants — RESUME (restartable state)

Last checkpoint: 2026-09-18T23:18:32Z ; CPU used so far: 567.5 s (cap 1800 s)

## 0. AUDIT_B REPAIR (repair agent, 2026-09-18T23:10Z–23:18Z) — DONE (all 5 corrections applied; no rebuttal)
Referee verdict (`../audits/AUDIT_B.md`): PASS_WITH_CORRECTIONS. One BLOCKING correction (#1), four NON_BLOCKING (#2–#5).
- #1 BLOCKING: `scripts/s04b_enum_lib.gp` line 16 passes `[Mmax, min(emax,Mmax)]` to `hyperellratpoints`, which truncates the
  DENOMINATOR range for the 8 quartics with |s| > 7579 (s = ±2A, ±2B, ±AB, ±2AB). Fix: `[Mmax, emax]`. Then rerun every s04b script.
  Old lib and old outputs are preserved first in `scripts/superseded_truncbox/` and `out/superseded_truncbox/`.
- #2 (non-blocking): 4e used only the refined constant (H = 20.679). Planned: rerun at λ₀ = 4.2 with B = 20.329 (H = 24.529,
  estimated ≈ 2 CPU-min) with the new script `scripts/s04b_pari_lam42_crude.gp`.
- #3: mark `out/s07b_Eprime_enum.out` dead (failed self-validation line; cited by no claim). #4: state that route (b) needs only the
  lower-side refined constant. #5: reword the headline (route (a) complete as delivered; route (b) complete after the box fix).
Plan / exact commands (cwd = this directory; GP = ~/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp;
GPO = `-q -D parisizemax=1000000000 -D nbthreads=1 -f`; every run is `nice -n 15` + `timeout` via run.sh, one at a time):
  1. `./run.sh s04b_box_audit 300 $GP $GPO scripts/s04b_box_audit.gp < /dev/null` (old box vs full box, 8 affected quartics, all H used)
  2. `./run.sh s04b_enum_validate 600 $GP $GPO scripts/s04b_enum_validate.gp < /dev/null`   (≈ 35 s)
  3. `./run.sh s04b_pari 300 $GP $GPO scripts/s04b_pari.gp < /dev/null`
  4. `./run.sh s04b_pari_simpleform 600 $GP $GPO scripts/s04b_pari_simpleform.gp < /dev/null`   (≈ 25 s)
  5. `./run.sh s04b_pari_lam42 300 $GP $GPO scripts/s04b_pari_lam42.gp < /dev/null`
  6. `./run.sh s04b_enum_crosscheck 300 $GP $GPO scripts/s04b_enum_crosscheck.gp < /dev/null`
  7. `./run.sh s04b_combo_heights 60 $GP $GPO scripts/s04b_combo_heights.gp < /dev/null` (does not call enumpts; must be byte-identical)
  8. `./run.sh s04b_pari_lam42_crude 900 $GP $GPO scripts/s04b_pari_lam42_crude.gp < /dev/null`   (≈ 2 CPU-min; correction #2)
  Then: edit 04 / 00 texts, append "Audit response" to 00_LANE_B.md, `python3 scripts/checkpoint.py`.
Repair progress log (appended as each step finishes):
- [23:12Z] Step 0 DONE: old lib + 6 old outputs copied to `scripts/superseded_truncbox/`, `out/superseded_truncbox/` (README there).
  One-line fix applied: `scripts/s04b_enum_lib.gp` now calls `hyperellratpoints(Q,[Mmax,emax])`.
- [23:12Z] Step 1 DONE (`out/s04b_box_audit.out`, 0.25 CPU-s): at all 7 search heights (11, 18.979, 20.679, 18.979006, 20.679006,
  22.828991, 24.528991) exactly 8 quartics had a truncated denominator range; only s = +AB gains points: X = ±48/4115 (h_r = 24.9296,
  = ±(2P₁+2P₂+T)), ±96/6275 (h_r = 24.7036, = ±(2P₁+T)), and at H = 11 also ±1/12, ±1/36 (h_r = 17.05, 16.63). EVERY extra point has
  h_r > H, so it is filtered; the enumerated sets are unchanged at every H used. No old-box point is missing from the full box.

- [23:14Z] Steps 2–7 DONE (CPU 55.7 s): reruns with the corrected library. Versus `out/superseded_truncbox/`: the ONLY differences are the
  raw quartic-point counts (+8 everywhere: 34→42 at H = 11, 74→82 at H ≥ 18.979) and wall-clock ms. Enumerated point sets, heights,
  λ ≥ 2.5, n ≤ 1.948485, λ = 4.128477550865786746999446013415042160376, n ≤ 1.179905 are unchanged; validate "agree: 1";
  `s04b_enum_crosscheck.out` and `s04b_combo_heights.out` byte-identical. → Correction #1 APPLIED; 4c/4d PROVED labels restored.
- [23:15Z] Step 8 (correction #2) LAUNCHING: `nohup ./run.sh s04b_pari_lam42_crude 900 $GP $GPO scripts/s04b_pari_lam42_crude.gp < /dev/null &`
  log `out/s04b_pari_lam42_crude.out` (+ `.time`); expected ≈ 2 CPU-min. If this session dies: check `cpu_log.tsv` for the tag; if absent and no
  gp process is running, relaunch the same command.
- [23:16Z] Step 8 DONE (correction #2; `out/s04b_pari_lam42_crude.out`, 106.2 CPU-s): λ₀ = 4.2 with B = 20.329 (max of all four
  constants), H = 24.528991, corrected full box: 12 points up to sign incl. T (the one new point vs H = 20.679 is h_r = 23.757,
  ĥ = 21.0025, a small combination); the only non-torsion points with ĥ < 4.2 are ±(P₁+P₂), ±(P₁+P₂+T); λ = 4.128477550865786746999446013415042160376
  attained, n ≤ 1.179905. Crosscheck at this H: 12 combos, 12 enumerated, missing 0, extra 0. → 4e "attained" no longer depends on the
  refined constant.
- [23:17Z] Step 9 LAUNCHING (note #3 diagnostic, dead route): `./run.sh s07b_validation_diag 600 $GP $GPO scripts/s07b_validation_diag.gp < /dev/null`
  (≈ 1 CPU-min; brute force at H = 10.5 on E′). Relaunch the same command if the session dies.
- [23:17Z] Step 9 DONE (`out/s07b_validation_diag.out`, 16.8 CPU-s): current E′ enumeration logic at H = 10.5 = brute force (7 points up
  up to sign) with both boxes; the old "equal: 0" came from an unpreserved earlier script version (output 11:06, script edit 11:08).
- [23:19Z] Text edits DONE: 04 (box statement + audit correction, "which side is needed", λ₀ = 4.2 robust rerun, certificate table,
  CPU), 00 (intro, headline, rows 4c/4d/4e, caveats 1/2/4, appended "Audit response"), s07b DEAD header + box fix (not rerun).
- Repair CPU total 178.9 s (cpu_log.tsv lines 27–35). REPAIR COMPLETE.

## 1. Current status / verdict
**COMPLETE after the AUDIT_B repair (§0; `00_LANE_B.md` "Audit response").** The verdict is unchanged: index 1 PROVED (route (a) as delivered, route (b) after the box fix). The final report is `00_LANE_B.md`. Every item B.1–B.7 is done and labeled. There are no running jobs.

## 2. Completed tasks and exact findings (item files hold the details)
- **B.1** (`01_minimal_model.md`). E₀ = [0, −22735, 0, 106272484, 0] is globally minimal: u = 1, and v_p(Δ) < 12 at every p.
  - Reduced minimal model: [0, −1, 0, −66020924, −65074271436], via x = x_r + 7578.
  - Δ = 2⁸·3²·2243·4547³·5843² > 0, so E(R) has 2 real components. The Néron differential is dx/(2y). **PROVED.**
- **B.2** (`02_torsion.md`). E(Q)_tors = Z/2 = ⟨(0,0)⟩. **PROVED.**
- **B.3** (`03_tamagawa.md`). **PROVED.**
  - c₂ = 2 (I₁*), c₃ = 2 (I₂, non-split, a₃ = −1), c₂₂₄₃ = 1 (I₁, split, a = +1), c₄₅₄₇ = 2 (III), c₅₈₄₃ = 2 (I₂, non-split, a = −1).
  - ∏ c_p = 16, and w = +1.
- **B.4** (`04_mordell_weil_saturation.md`). E(Q) = ⟨T⟩ × ⟨P₁, P₂⟩, with index exactly 1 and rank 2. **PROVED** by two routes.
  - Route (a), eclib: saturation index bound 2, and the points are proved 2-saturated. mwrank's own run says "determined
    unconditionally". mwrank's generators are P₂ and (5843, 210348) = −P₁ − P₂ + T.
  - Route (b), PARI (complete after the AUDIT_B #1 box fix, which changed no point set): Silverman bound B = 20.329 (the maximum of the refined and crude published forms, constant 0.973), plus a
    complete ratpoints enumeration over 16 quartics to naive height 22.829, plus Hermite γ₂ = 2/√3. This gives λ ≥ 2.5 and index
    n ≤ 1.948.
  - λ = min ĥ = ĥ(P₁+P₂) = 4.12847755086578674699944601341504216.
- **B.5** (`05_sha2.md`). **PROVED.**
  - dim Sel^ψ(E) = dim Sel^ψ̂(E′) = 2 and dim Sel₂(E) = 3.
  - Sha(E)[2^∞] = 0 and Sha(E′)[2^∞] = 0.
  - Tools: mwrank, Sage/Miller `two_descent_by_two_isogeny` and PARI `ellrank`, calibrated on 7 Cremona curves.
- **B.6, partial** (`out/s06_calib.out`, `out/s06_seed.out`).
  - Calibration: the ball-arithmetic Ω and Reg reproduce Cremona's values for 389a1, 1088j1 and 1088j2 to all 29 printed digits. These
    three curves have Δ > 0, 2 real components, and Ω = 2ω₁.
  - Seed, **CERTIFIED_NUMERIC**:
    - ω₁ = 0.0280449015194364044483094018079303841711350478666349665798011
    - Ω_E = 2ω₁ = 0.0560898030388728088966188036158607683422700957332699331596021
    - The ball radius is < 10⁻¹⁰⁰⁰. The exact-root AGM and the certified-isolation AGM overlap.
  - Kill multiplier k = 2: 2P lies in E₀(Q_p) for all p.

## 3. Unresolved questions
- (fixed) The translation margin in `rig_lib.sage` is now c = ceil(1 − emin) + 1.
- Seed Reg = 17.7965174724903402991749412194360384163049724637781885322663, ball radius 4.4e-65. Seed Ω = 0.0560898030388728088966188036158607683422700957332699331596021.

## 4. Active jobs
None (the repair jobs s04b_* reruns, s04b_pari_lam42_crude and s07b_validation_diag all finished rc = 0). Pre-audit note: `s07b_Eprime_enum` (PID 99234) was killed at about 18:07:40Z: `hash` is not a gp builtin, so the checkpoint write failed. About 65 CPU-s was
lost; it was logged by hand in `cpu_log.tsv`. The fixed script is on disk but is not needed (see §2b).

## 4b. Reconciliation with the second lane-B instance (coordinator message, about 18:07Z)
- Foreign files, **kept and cited** after reading them in full:
  - `scripts/s07_bsd_const.sage`, `out/s07_bsd_const.out` (11:06:01 local, the corrected α′(T′) = b′ version) and `out/s07_balls.sobj`.
  - Its CPU lines in `cpu_log.tsv`: s06_seed 11:02:12, s07_bsd_const 11:04:49 and 11:06:01.
- `scripts/rig_lib.sage` carries edits from both instances: my c = ceil(1−e_min)+1 and its assert `> 0.5`. They are compatible, so both are kept.
- Superseded: the other instance's s06_seed output of 11:02:12 was overwritten by my identical run of 11:03:37.
- No lock files were found.

## 5. Files produced with sha256
<!-- SHA-BEGIN -->
- `00_LANE_B.md` 5e4890607bd0d7287f3fdb5fa3a3a85e62f3cd4ea3dad661845fe05f58a0bc9b
- `01_minimal_model.md` 14e4bec1651e34359bf92c50049afc009f9e616a9a116acb8b4508efb68f118d
- `02_torsion.md` a0b4eee184d53f8108602ac85b8fb1192b589fb1442741d0d495c2ce82b1e607
- `03_tamagawa.md` 3dd4b648a86f180ecbdfabc42656e7f0158c1ac2f6d3504456553a876e57f516
- `04_mordell_weil_saturation.md` da3a9cc91c246892439aa3d85689beae6223b34d05ecc1a46dfae9ae049f0997
- `05_sha2.md` 93a4ee49de476edfe87ce8d888bea2677d71c7b05f760330801b6a66faa597b4
- `06_period_regulator.md` 7b3e32bcd2f536b0e1b581b3d81babf62488b081df566b24fb6083e69f0eb93f
- `07_bsd_constant_isogenous.md` 19a7d3a57d315a33a9428377bdf9cb7b6489a527160593251b5e012d1fb8a04c
- `cpu_log.tsv` fcb814a229917525ce9459c24fcfa95ca70f6ce1796ab4f8d9d480c38b4e880a
- `out/s01_03_local.out` ac6569c9f48faca459b1519a5e96dbb5adcad291947ec72ae2e1f0c02744c673
- `out/s01_03_local.time` 05ae5d113c625cd0bd650d129aa57ff41a1ac1312456f242597d099c907a892b
- `out/s01_03_sage.out` 2e8824e39cd2762c0ce66ca99cf5284f3430254c7c00ced59043ec13077879c9
- `out/s01_03_sage.time` 4addd6a13b437947faece170ed4d8bc742129c78e5835cc2aea22a954008540f
- `out/s02_torsion_cert.out` 1f585cf2e98161914e0cc857bf1b09b26260c64a204c7366d1732473748b4a38
- `out/s02_torsion_cert.time` b10b8d99646ea09fde2157b9e5c0657fbf91aff5a0fada3cfe68ca138b3e01e0
- `out/s04a_mwrank_v1_S-1.out` c154760961bff1130fe7f4a59bbf83a0f032e5cf8af95eaeadc2f8d8586e14b7
- `out/s04a_mwrank_v1_S-1.time` 25873d7740c9718506bd6ba6775759a76e7d741c9ea861b7f2035766b0a7fbc8
- `out/s04a_sage.out` e711dcc56edf80804fb1069a2932a8815122019c2471a8478252b3cfdf785e9d
- `out/s04a_sage.time` 05d9b4501abe22d1f501436ad3ebcf765f002b7ab1c96229fb30f96b8dfc6e1a
- `out/s04b_box_audit.out` 0e203dfc83f30b1349ba3f54825ae082a08e58841171518c9a05b9418b2c0cef
- `out/s04b_box_audit.time` 2a9b8ef4630210cdc17cc7d427550a71a5e11a187585b02eed96989795d4ed16
- `out/s04b_combo_heights.out` c5dc579cd6ee64386ce489a5bd6d8ab0927ff01f2fb204da9fe76ff91413a4eb
- `out/s04b_combo_heights.time` 9343768316dea21b3a1af8fc43b395ded2a5ff39ee8f9642c35add3a0612e237
- `out/s04b_enum_crosscheck.out` 137a93c329d555899a62ebf9f2dff1656b9a2b55389ae4947296a62eb67e0551
- `out/s04b_enum_crosscheck.time` 0c5495f8204f59fb7137d523d807f41bf1380fb6c3710a39948072ed4b07cd07
- `out/s04b_enum_validate.out` 0f6ab732e62a290482dd7d9c9b3fe56fdb9c7c004d70c0562e24d03e444ee531
- `out/s04b_enum_validate.time` 94aca54279fb9848ecd6ff9fd02b759892f402a1ac85e9e1f2941c6db77da0f3
- `out/s04b_lam42_crude_nohup.log` 5baf2241e1d5b247abd65a5745017c8a7f82e02093aae1ef5a8d672852294fc1
- `out/s04b_pari.out` 99b213b295e2fb009915957bb3b77fe537b1cf8b5d655ca1b83c27693a7bd2b1
- `out/s04b_pari.time` f05bb6155e9237caa7cc93b006882c332272857541e80c425652b9779110d08c
- `out/s04b_pari_lam42.out` 42417bced04cc4ff8dfb10646514c91623a4ce850a02aff120e423c22ea82c3c
- `out/s04b_pari_lam42.time` d3b5510d59e2a207a4fd4fea0ada69c3a337916a986cb300d1c12585cce7a778
- `out/s04b_pari_lam42_crude.out` 63530065986aba8d04428c106e18c243823f96a68917fe8e3c4af889afdbb8e9
- `out/s04b_pari_lam42_crude.time` 78428f240968e8bdf7ec2d399541356127ad35a7d7f58d569bc8327f495aa69a
- `out/s04b_pari_simpleform.out` 734df6422e368b670547968e4500ff90a4b5e12cbb3524410ec339421d627bcb
- `out/s04b_pari_simpleform.time` 8e7c338e06d2061fdaa502c69a275df11540ce69b5423ed2449b879b18d50989
- `out/s05_sel2.out` eb985559dc4046613dcc1cad22f9f099fb0dfb4722b214f3359ac5aac8c89e42
- `out/s05_sel2.time` ee308689ccb8574537cde5bbc37ab15691c4dc5a25908e3339bcd0b6282a9759
- `out/s06_calib.out` 6b53ac87acb50dda3b7e22699e9a570e9e92fbf8d261a9013cb3547aebd3ff16
- `out/s06_calib.time` 890260c7757f074af876917b73a810799ea5433208168307059e5f50773ceea1
- `out/s06_seed.out` 300c1b2ffedf19c8bacaa052ca4a5c96fb2cf88effd826363aebee6eed7a566f
- `out/s06_seed.time` dadf1cc6fa85a2f0b0d54d94bc3909cabaffd254d7290be08b8df2d21cded744
- `out/s06_seed_balls.sobj` 8f0c4ca5b5f15e82e33f8894a1647929be4e8379be29d7fc5d779ff078ceebf3
- `out/s07_balls.sobj` e4401377fe643685fc16fb7c596228a6011820daa61576971987466c85d7bfe0
- `out/s07_balls_rerun.sobj` e4401377fe643685fc16fb7c596228a6011820daa61576971987466c85d7bfe0
- `out/s07_bsd_const.out` cd0ba942258c50ac21ae68546ddaccd09672c65164001f2f571a9988ca840a83
- `out/s07_bsd_const.time` 87355aa498eb6f45f5bcb3fe050a0914faae32db2389376d94b6653aa75b9444
- `out/s07_bsd_const_rerun.out` cd0ba942258c50ac21ae68546ddaccd09672c65164001f2f571a9988ca840a83
- `out/s07_bsd_const_rerun.time` 88140941ca4c768bbf2d4ef9d78f83c741a79104d212ce744ae7358a01c2f91c
- `out/s07a_Eprime.out` 61392c5c0415b5d3c1677ee6a2a8b973636d053c4de37f3a9dc099bdfb7b4430
- `out/s07a_Eprime.time` a725ce7e8443986c620a3c6301ccc4150f83591340f3fe44b0232eb040d23e18
- `out/s07b_Eprime_enum.out` 11cef89f5b13b6e94e3c2168d40efdeb713694cab461c02ddb06e29a6b2e22f6
- `out/s07b_Eprime_enum.time` d0ae1403a84379f85899366b00dcd62fe0786783762c7576c5e9a64a4700e437
- `out/s07b_nohup.log` e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- `out/s07b_validation_diag.out` 1ca932b69fca17668e0e4c82b12b334a019bdfbc73a5c435a0ef2a7d49057660
- `out/s07b_validation_diag.time` 131cada9d6f01a9e203887bde8d82d91e99a0e8a136b006bd308eb63008f2c5f
- `out/s07c_scaling.out` 72ee9d98b6a72ad2917201e42bc028e989b3b4bf47a4afb796672f2387436726
- `out/s07c_scaling.time` d58533430b96fcc2b60eff08049cf37a7dc06cae91b3e33de3abdb1d96de166b
- `out/superseded_truncbox/README.txt` 2434dfe4c3c797aae107c98c29a40ec422ff8403235ae14933aab806ea893a0e
- `out/superseded_truncbox/s04b_combo_heights.out` c5dc579cd6ee64386ce489a5bd6d8ab0927ff01f2fb204da9fe76ff91413a4eb
- `out/superseded_truncbox/s04b_combo_heights.time` a4308e31ade4633a94d9cd962c98f2166cebeab917c5434e4223f481c6d3e288
- `out/superseded_truncbox/s04b_enum_crosscheck.out` 137a93c329d555899a62ebf9f2dff1656b9a2b55389ae4947296a62eb67e0551
- `out/superseded_truncbox/s04b_enum_crosscheck.time` 2a13b6fec7ec615fb2a2cce06135878c15bfa0e4f9b747b28b4cefc46726c835
- `out/superseded_truncbox/s04b_enum_validate.out` ca54139366d13d46b7d0bd1c3c2c2ea8a0fa088f92885a68b7ce126ef168bb61
- `out/superseded_truncbox/s04b_enum_validate.time` 9615237e3653b9b245f0dd29694646a6c6f15ec9b834955b223bb74dd94a28e0
- `out/superseded_truncbox/s04b_pari.out` 1b3b1dbbf2c6990c7fb04c4cf5d1aa43112380f639bc545126f9b5ac23452b90
- `out/superseded_truncbox/s04b_pari.time` 34c4cd7550ec7ca2670f3180f40dcc8b0ae3ebc26be56dda6f7a0b13bfd58de5
- `out/superseded_truncbox/s04b_pari_lam42.out` 064296b900016e1fbd24e34f1fdbc9240d52b15fae182908649073e3b0e6f508
- `out/superseded_truncbox/s04b_pari_lam42.time` 6b39095b42523d380e0a7123c939ef42148cb9258b4c6ba0ca8d4a3ade6edcbe
- `out/superseded_truncbox/s04b_pari_simpleform.out` 55164822c77e92e4a3b9927252feb98039f503a3109621747a226276e0bfad55
- `out/superseded_truncbox/s04b_pari_simpleform.time` 28035f54ece063e1b68dd5aff6ec2c668494069d6c5321fc616c48671d91ee6d
- `run.sh` 847face2631d2a6faa66a2b25e563a6610257dbb19ce25bc12de12cd249617bf
- `scripts/checkpoint.py` a327a39cca0ecc089cd314dc13bad019744942ab4967a475f88cbf4ebfcc747f
- `scripts/rig_lib.sage` 38bb5f5aa7248c74f67748033aa5d16c8dc62f1a130a39b2d40ed06ec6e9fec4
- `scripts/s01_03_local.gp` e627b8e6ab4d4cc48a37058613aa299105a48e72ba59de97b4e2572433cd6af3
- `scripts/s01_03_sage.sage` 42cd44652541b4fe819efb48e831bd39bbfef39393af132c9d693efafd530c25
- `scripts/s02_torsion_cert.gp` 72b391a9f387a1979259eba66497e6cba75da8686202efffa416ecedcaee351f
- `scripts/s04_mwrank_input.txt` 987c4bcfcba4ddede165c8448a631ceec3b276f1f937caf0ed3a84d408512988
- `scripts/s04a_sage.sage` 468af66a51ca1b8e1ada32462a4057f4b12b81395d6c69ca9d97eb8c8bb75e88
- `scripts/s04b_box_audit.gp` d141cfa918bd98e6a33eb338bf9baf5b7a2c5fef3405d1ef25533698233b582d
- `scripts/s04b_combo_heights.gp` dd4d07eef7859520b6ca98cfd267cc4bab03ad7da4b76aac477adeb4c588b1c8
- `scripts/s04b_enum_crosscheck.gp` bbbc45899fece961637eeef2d964ea2d32cab13536cb5c5b270aeb19454f3a36
- `scripts/s04b_enum_lib.gp` ad53c6585de8ec05f287435fdd42dc1f466bce1a8c7fcb2503084116ab2e3582
- `scripts/s04b_enum_validate.gp` 9d3c66d468466e887b6aa355ca6cc0d726ce42e726e6227f0e158d150bd001f0
- `scripts/s04b_pari.gp` 4b6e17f5bf5fc69d336a5c3f616f9d1d075ddb9387ec1944cd3b5357ae257c7d
- `scripts/s04b_pari_lam42.gp` 3d296973fba8e58480e1b0cf66922f87dc57454b0d1619802e857019752d78f8
- `scripts/s04b_pari_lam42_crude.gp` b1a6bb8ca236fa36b8d330ce6f1e0809f02cfdc4981fe3201a42d8ededc2e4d0
- `scripts/s04b_pari_simpleform.gp` f222f680c043ec1cc67b7ab4d7e81a57c6e87f02c22cb6568f0aceb8a161fc3f
- `scripts/s05_sel2.sage` ef4f128a90ab2b4f867cbce586d70da4bc361216a47dde3dfd6fca7d502be6b0
- `scripts/s06_calib.sage` 8ff70dd9afbc0291f314a19fbc8dd2bd7edd6503915aac05c0cec9b772d62965
- `scripts/s06_seed.sage` b3dc4476867f27811b34f7f9c938839b6e92a44fb81ec0b384fc0fee3bfef3ed
- `scripts/s07_bsd_const.sage` 79a7e57a3b25969599d630a1c9318904b8bd3a72de856140059c1804bc240c5a
- `scripts/s07_bsd_const_rerun.sage` 8d8a79da0d9c2bb183024c27642b8f0b718d58e690565a130122be26d36b2b22
- `scripts/s07a_Eprime.sage` f6b75ee864c2695ca6b4143765ff21b2dd67694e35867eeed08527a0ada4a8ab
- `scripts/s07b_Eprime_enum.gp` 9570b66bd7244480eefa27df39c1682142217a86cdccd8d3e83b029bb10c36c6
- `scripts/s07b_validation_diag.gp` c536bcb6ef574847c3c19f2d98131bfce3d2faf9ed3b7c289dd301f08adeab31
- `scripts/s07c_scaling.sage` 70a3075e1ffa55561e7e3688206cd32e59d16cadbbe8f9bbd2043ade682e9c0e
- `scripts/superseded_truncbox/s04b_enum_lib.gp` 8fd49a9eabae1d6818c5524290b7df86348e9d72aaa57415d2f101ad8bd595fa
<!-- SHA-END -->

## 6. Exact commands to resume
- Common runner: `cd B_invariants && ./run.sh <tag> <timeout_s> <cmd...>`. Output goes to `out/<tag>.out`, stderr and time to
  `out/<tag>.time`, and one line is appended to `cpu_log.tsv`.
- SAGE = `~/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/sage`; GP = same directory `/gp`.
- Seed Ω and Reg: `./run.sh s06_seed 900 $SAGE scripts/s06_seed.sage` (after the fix in `scripts/rig_lib.sage`).
- Calibration: `./run.sh s06_calib 900 $SAGE scripts/s06_calib.sage` (about 50 CPU-s).
- Checkpoint: `python3 scripts/checkpoint.py`.
- Route (b) (corrected box): `./run.sh <tag> 600 $GP -q -D parisizemax=1000000000 -D nbthreads=1 -f scripts/<tag>.gp < /dev/null` for tag in
  s04b_box_audit, s04b_enum_validate, s04b_pari, s04b_pari_simpleform, s04b_pari_lam42, s04b_enum_crosscheck, s04b_combo_heights,
  s04b_pari_lam42_crude (≈ 106 s), s07b_validation_diag.

## 7. Resources used
See the CPU line at the top (sum of `cpu_log.tsv`). Maximum RSS is about 275 MB. Cap: 30 CPU-min and ≤ 2 heavy processes.

## 8. Next three actions
1. None in lane B. AUDIT_B is answered (all corrections applied). Optional: the referee may confirm the repair.
2. (optional) Rerun `scripts/s07b_Eprime_enum.gp` as a third route for E′ generators. It is not needed.
3. (optional) Obtain the Silverman 1990 paper to confirm the transcribed constants. Route 4b does not depend on them.

## 2b. B.7 findings adopted from the second instance (`out/s07_bsd_const.out`; the author re-run `out/s07_bsd_const_rerun.out` is byte-identical, DONE)
- C = Ω·Reg·16/4 = 3.9928126392393669180685520022091539473553366203072 (radius 1e−65). PARI `ellbsd`·Reg agrees.
- E′(Q) = ⟨T′⟩ × ⟨R′, ψP₁⟩ with R′ = (−2243, −107664). The Kummer map α′(T′) = mA, α′(R′) = −2243, α′(T′+R′) = −4547 gives #E′(Q)/ψE(Q) ≥ 4; #Sel^ψ = 4 (B.5) gives ≤ 4. 2R′ = ψ(−2P₁ − P₂).
- Ω′ = Ω and Reg′ = 17.7965… = Reg (radius 5e−65), so C′ = C and **C′/C = 1 ± 5e−66**.

## 8b. B.7a findings (from `out/s07a_Eprime.out`)
- E′ = [0, 45470, 0, 91790289, 0] is globally minimal. Its reduced model is [0, −1, 0, −597383344, 5572681004764], via x = x_r − 15157.
- Δ′ = 2¹⁰·3⁴·2243²·4547³·5843 > 0, and conductor N′ = N.
- Local data: c₂′ = 2 (III*), c₃′ = 2 (I₄, non-split), c₂₂₄₃′ = 2 (I₂, split), c₄₅₄₇′ = 2 (III), c₅₈₄₃′ = 1 (I₁, non-split). ∏ = 16.
- torsion′ = Z/2. ψ(P₁) = (5184, 1355400) and ψ(P₂) = (3822025/1296, 38806079435/46656). ψ̂ψ = 2 is checked.
- eclib: the index of ⟨ψP₁, ψP₂⟩ is 2. The saturated basis {ψP₁, R = (−20187, −2906928)} has 2R = ψP₂ and Reg′ = 17.7965174724903… = Reg(E). mwrank's E′ generators are certain.
- Ω′ = Ω, certified by balls (see 2b). C′/C = 1 is PROVED in `07_bsd_constant_isogenous.md` §7.4.

## 9. Provisional vs verified
- Independently verified (≥ 2 implementations or routes): B.1–B.5, and B.7's E′ generators (Kummer-map proof plus eclib saturation).
- Certified by one ball implementation, calibrated on 3 Cremona curves: Ω, Reg, C, Ω′, Reg′, C′.
- B.7 was computed by the second instance and reproduced byte-for-byte by me.
- Independently audited: AUDIT_B (PASS_WITH_CORRECTIONS) recomputed Δ, torsion, c₂ (2-adic point count), Ω (AGM + quadrature), heights
  (own Tate series + doubling limit), Reg, C, isogeny facts, and the corrected route-(b) box (its scratchpad).
- The repair reruns for #1/#2 are author re-checks of the referee's finding (they agree with the referee's values), not a second audit.
- Provisional: none.
