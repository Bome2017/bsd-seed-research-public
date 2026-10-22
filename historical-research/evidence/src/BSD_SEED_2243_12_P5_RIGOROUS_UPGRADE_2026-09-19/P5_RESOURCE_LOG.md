# P5_RESOURCE_LOG: rigorous p = 5 upgrade (2026-09-19 06:28 → 07:08 PDT)

**Host.** iMac i9-10910, 10 cores / 20 logical threads, 16 GB RAM, macOS 26.7.

**Authorization.**
- J = W = 16 (with automatic reduction to 14 or 12);
- ≤ 12 GB physical RAM;
- swap only as emergency headroom;
- about 20 % of CPU left for the OS.

**Sources.**
- `logs/resource_monitor.tsv`: 45 samples at 60 s.
- `run/logs/timeline.log`.
- `/usr/bin/time -l` output of the arbcore runs.
- producer `clock()` per segment.
- `logs/RESOURCE_SUMMARY.txt`.

## Workers and governor

- Launch at J = W = 16, through `monitor.sh` (the p = 3 governor retargeted). **The governor never triggered.** Its log has one LAUNCH line and an exit on ALL DONE.
- Peak simultaneous project workers: 16. Pre-launch there were no stale processes, and the load was ≈ 1.5.
- Thermal: CPU_Speed_Limit at least 86 (median 88), with no warnings.

## Time and CPU

| stage | wall | CPU | how measured |
|---|---|---|---|
| Stage W (467 segments) | **32.6 min** (06:28:49 → 07:01:24) | producer **6.22 CPU-h** (exact); stage total **8.28 CPU-h** (sampled); verifier ≈ **2.07 CPU-h** (difference) | prod-log clock(); monitor integral |
| Stage A m = 25 | **5.9 min** (352.6 s) | **1.55 CPU-h** (5 544 user + 19 sys) | /usr/bin/time -l |
| Stage A m = 5 | **1.2 min** (72.8 s) | **0.28 CPU-h** (1 011 + 5) | /usr/bin/time -l |
| **pipeline total** | **39.7 min** | **≈ 10.1 CPU-h** | |
| integrity, cross-run, downstream, primepi | < 1 min | ≈ 0.01 CPU-h | wall clock |
| replay: Stage W sample (16 segments) | 72 s | 0.28 CPU-h | /usr/bin/time -p |
| replay: Stage A, both targets | see `P5_REPLAY.md` | see `P5_REPLAY.md` | /usr/bin/time -l |

## Memory, swap, disk

| quantity | value |
|---|---|
| peak total RSS of project processes | **1.42 GB (1.35 GiB)**: arbcore msl m = 25, max RSS 1 417 019 392 bytes. Stage W ≈ 0.36 GiB for all 16 processes |
| swap | baseline 1 596 MB (other apps); max 1 596 MB; **growth +0 MB** |
| system-wide memory free | ≥ 60 % throughout |
| disk | run directory **11 GB**: witnesses 9.4 GB (kept, 467 files), a_q 1.4 GB, units 11 MB. Free space went from 142 GB to 131 GB |

## Anomalies

None: no FATAL, no failed witness, no governor action, no swapping.
