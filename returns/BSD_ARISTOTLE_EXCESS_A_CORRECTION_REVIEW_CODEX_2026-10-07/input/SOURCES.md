# SOURCES (paths relative to project/; sha256 recorded at read time)

Governing documents read in full:
- TASK.md e473b74ac4c75bd834d3ee97e502f534aeb7a96b242b67ea61fb794aa98fb9ff
- COMMON_CONTRACT.md 5cc767c520ab2bc6fc255d0d51507bc9b2880f8007ea4e499e10130e289042bf
- CURRENT_FRONTIER.md 83587b2973c1391cdd98960d08ff7027dc34753272b40e6461a8c818eaaba543
- RECENT_WALLS.md b9cd394408cf8c42eee4392d2e380bb56ca86278b9334fd7a4ca3851ef3eccfd
- LOCAL_ATTEMPT.md 72f44b9610e0178fa7c10c468835ea1deb420dd7d51d64b9ab980a820180fe45

Record files read in part (first pass):
- reading_set/BSD_SEED_ARISTOTLE_2026-10-05/guide/03_WALL_ATLAS.md (grep hits; W03, W05, W23–W24 read)
  648c668dcc3d388675b0cb92f0a3216157e6968e3815454439736f3c51404ac1
- current_overlay/BSD_CURRENT_OVERLAY_2026-10-06/download_sources/4fbf3521eaa7/HEEGNER_NU.md (first ~6 kB)
  62e94b95945b2ce69bff51ddd9b8972104587f6d9603ca1393e325afb56285b0
- current_overlay/BSD_CURRENT_OVERLAY_2026-10-06/download_sources/474218aa6a00/output-final_aristotle/research_return/RESULT.md (first ~4 kB)
  40530aed676182d0ec70c9df228bffc03d8d9f8293c4845d5d759a727eba49d0
- HISTORICAL_STOPS_AND_CORRECTIONS.md (grep hits only, lines listed in COLLISION_CHECK.md)
  8aefa608256599fb57895568ab65553b928dbb4a020f7354c053da4eea0d397c

Record files read in the second pass (2026-10-07, −23 twist trace). CERT abbreviates
reading_set/BSD_SEED_ARISTOTLE_2026-10-05/working_set/repo/evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21.
- CERT/RESULT.md 66354605f2d7fbb8211c47b1bc0651a30e4d58b6b8cf6e37446dc2cb730419a8 (full)
- CERT/PROOF.md e45c4f9a2709c4ee38a48e4c44f4a6b5f7a22db77d5f80f7892e1890a43fcc49 (full)
- CERT/DESIGN.md 7c4555f1fc525fadfe5c59cb3f238b8e8beca6d6b9e5b9d4582d2d2788716827 (full)
- CERT/COMPLETION_REVIEW.json, BUILD_BINDINGS.json, EXACT_TWIST_INPUTS.json, run_T3456106495.log,
  combine_T3456106495.log, build.sh, review_completion.py (full); RESULT.json and
  INPUT_BINDINGS.json (structure and hash fields); MANIFEST.sha256 (all entries checked for presence/hash)
- reading_set/.../_work/bridge_repair_assessment_2026-09-21/MCS_TWIST_IDEAL_REVIEW.md
  16ce9618bbc7c089f98e1954c21cf6156c62821687c159a485d0146c1ab42533 (full; §3 tail bound derivation checked)
- reading_set/.../_work/bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md (full)
- reading_set/.../BSD_TWIST_D23_CERTIFICATE_2026-09-21/CERTIFICATE_CONFIRMED_AND_COVERAGE.md (full)
- current_overlay/.../BSD_ARISTOTLE_W3_P17_P19_RETURN_2026-10-06/HEEGNER_NU_NOTE.md
  f3a86b23ee3207aac02f5f25bffb38bae9f3520476245b51d1ce90a478e3bda2 (§§2–4)
- same return: w3_p17/TWIST23_RESULTS.json 01301ee2807557182da8261c7b5d34d7524b068c6a6050fbe12b88ec4cfae49d,
  w3_p17/analyze_twist.py 2d0c173bb8f36c3e2aaf4d1ed369ca83dc7cba2867bdeb76c760992e547b7a4e,
  runs/twist23_E1_tf3*.out/.log, README.md, W3_P17_REPORT.md §§1,6, CLAUDE_CHECK.md (full)
- FULL_COMPENDIUM.md headings at lines 331, 343, 520, 1039, 1075, 1099, 1172, 16399
- full_record_index/FILE_INVENTORY.jsonl.gz and BULK_BINARY_RECEIPTS.jsonl.gz (grep for d23_twist)

Not present in the archive:
- Da Ronche–Longo–Vigni, arXiv:2603.12357v1 (statements known only through LOCAL_ATTEMPT.md's
  scoped summary, which does not say which Euler system defines their ideals).
- The 2026-09-21 certificate's twist.c, retained_arbcore.c, binary, 1,030 atomic units and the C11
  coefficient segment files (see TWIST_D23_TRACE.md §3).

External theorems cited at statement level (not re-read): Kolyvagin (1991); W. Zhang (Cambridge
J. Math. 2014, Lemma 8.4 as recorded); Howard (Compositio 2004); Nekovář (Selmer complexes);
Gross–Zagier; Kato (Astérisque 295); Perrin-Riou and Schneider.
