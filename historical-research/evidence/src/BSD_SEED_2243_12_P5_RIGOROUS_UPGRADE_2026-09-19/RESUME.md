# RESUME: seed (2243,12) rigorous p = 5 upgrade (replaces the CERT-NUM node N7 of the master certificate by a successor; old files untouched)
If the session dies:
1. Read STATE.json (phase) and run/logs/timeline.log (pipeline progress).
2. Pipeline: ~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/p3plan/run_p3.sh (generic target list; guard variable is named P3_AUTHORIZED)
   with TARGETS="25:1:1 5:1:1" LATDEN=1024 OUT=<this dir>/run; exact relaunch command in prelaunch/LAUNCH_COMMAND.txt. Resumable.
3. Never launch p = 7 or depth > 2 here. Never edit ~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18 or the LP5 / gate directories.
- 06:28:48 launched (J=W=16), stage W 467 segments. Relaunch: prelaunch/LAUNCH_COMMAND.txt
- 07:01:24 stage W done (467/467; root fcd02437...); stage A m=25 running.
- 07:2x FINAL: P5_RIGOROUS_SHA5_ZERO_CONFIRMED. All checks/replays PASS. P5_MANIFEST.sha256 written last (verify: shasum -a 256 -c P5_MANIFEST.sha256).
