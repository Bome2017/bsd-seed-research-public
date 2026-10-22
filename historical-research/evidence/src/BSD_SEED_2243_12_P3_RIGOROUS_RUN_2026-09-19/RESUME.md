# RESUME: seed (2243,12) rigorous p = 3 run (depth 4)
If the session dies:
1. Read STATE.json (phase) and run/logs/timeline.log (pipeline progress).
2. The pipeline is `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/p3plan/run_p3.sh` with OUT=<this dir>/run; it is resumable:
   relaunch with the SAME environment (see prelaunch/LAUNCH_COMMAND.txt). Done segments (run/seg/<s>.done) are skipped; arbcore
   units are write-once and self-hashed; PARAMS lock prevents mixing parameters.
3. Never launch p = 7 or depth 5 from here. Never delete run/ artifacts.
- 23:07:11 launched (J=W=16). Resume: see prelaunch/LAUNCH_COMMAND.txt; monitor: monitor.sh (NO_LAUNCH=1 if the pipeline is still running).
- After ALL DONE: run in order (each from this directory):
  python3 downstream/p3_integrity.py run            -> downstream/INTEGRITY.txt
  python3 downstream/p3_downstream.py run           -> downstream/P3_DOWNSTREAM.txt
  (cd downstream && python3 make_s81_gp.py ../run && gp -q -f lane3_an2_eval.gp)  -> downstream/LANE3_AN2.txt
  replay/replay_stageW_sample.sh ; replay/replay_msl.sh ; python3 logs/summarize_resources.py
  STOP rules: any FAIL in p3_check / integrity / downstream => no BSD conclusion (case E).
- 00:13:39 stage W done (885/885, 663685727 primes, root 5f9994d9...); stage A m=81 running.
- 00:30 pipeline ALL DONE; Stage C + integrity + downstream PASS; CASE A (a_{4,2} = 15480 = 9 mod 27). Remaining: replays, reports, manifest.
- 00:5x FINAL: P3_PROVED_SHA3_ORDER_9 (a_{4,2} = 15480 = 9 mod 27, ord_3 = 2). All checks/replays PASS. P3_MANIFEST.sha256 written last; verify with shasum -a 256 -c P3_MANIFEST.sha256.
