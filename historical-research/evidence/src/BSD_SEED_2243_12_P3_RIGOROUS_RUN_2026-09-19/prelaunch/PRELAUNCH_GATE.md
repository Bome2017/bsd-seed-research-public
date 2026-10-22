# PRELAUNCH_GATE: rigorous p = 3 run (seed 2243,12), recorded 2026-09-18T23:07:05-0700

| # | gate item | result | evidence |
|---|---|---|---|
| 1 | core MANIFEST.sha256 (1718 files; manifest sha256 f94c90c7…) | **1718/1718 OK** before rebuild; also 1718/1718 OK after rebuild | core_manifest_verify.txt, core_manifest_hash.txt, core_manifest_after_rebuild.txt (empty = no mismatch) |
| 2 | rebuild from source once (`./build.sh`) | exit 0; the rebuilt binaries are **byte-identical** to the MANIFEST entries; smoke test on 24a1 (m = 81/27/9) reproduces 8/8 stored artifacts byte for byte | build_output.txt, source_and_binary_hashes.txt, smoke_test_24a1.txt |
| 3 | guard refuses the seed without authorization | exit 2 and no directory created, both with P3_AUTHORIZED unset and with P3_AUTHORIZED=no | guard_test.txt |
| 4 | authorization | operator message 2026-09-19: run authorized; launch uses P3_AUTHORIZED=yes | LAUNCH_COMMAND.txt |
| 5 | targets p = 3 ONLY | script default TARGETS="81:3:1 27:3:1" (m = 81 and 27, Q = N/3, s = +1); no p = 7 | script_defaults.txt |
| 6 | LATDEN / T | LATDEN = 1024; T_min(81) = 14 832 175 873 (T_min − 1 fails); operational T = 14 847 836 159 = 885·2²⁴ − 1; m = 27: T_min 4 830 360 876, T = 4 831 838 207 = 288·2²⁴ − 1; **all equal to P3_RUN_PLAN.md** | tmin_check.txt |
| 7 | no stale processes | 0 apwit / wverify / arbcore / swstream / sage / gp / validation jobs; background load ≈ 2.8 (OS and apps) | stale_process_check.txt, system_snapshot_before.txt |
| 8 | resources at launch | disk: 161Gi free of 932Gi; memory free (system-wide): 70%; swap: total = 4096.00M  used = 2468.25M  free = 1627.75M  (encrypted); thermal: CPU_Speed_Limit 100, no warnings | system_snapshot_before.txt |

Source identities: arbcore.c 56a43aac…, apwit.c e6cca7ff…, fastap.c 7d3f4d51…, wverify.c 128e7960…, run_p3.sh 6b7b071c…, p3_check.py 1922291c….
Toolchain: Apple clang 21.0.0; FLINT 3.3.1; GMP 6.3; MPFR 4.2.2; PARI 2.17.4 (producer only); Python 3.13.2; macOS 26.7.
Workers: J = W = 16 (80 % of 20 logical CPUs); governor may reduce to 12 / 10 on sustained memory pressure, swap growth or throttling.
Witness retention: KEEP_WIT auto → 1 (free disk ≥ 60 GB); projected ≈ 18.3 GB witnesses + 2.65 GB a_q files.
Start time: 2026-09-18T23:07:05-0700.
