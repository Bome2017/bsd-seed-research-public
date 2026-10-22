# Sources and custody for this return
- openai/math: public GitHub repository, cloned read-only (shallow, blob-filtered) at commit
  fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (HEAD of main at 2026-10-11, no delta vs the Codex pins). 719 manuscripts /
  372 families. Text extraction with pdftotext -layout; LaTeX sources read from preprints/*/build/. No code from the
  clone was executed. The clone is not part of this package (3.2 GB); paths in the evidence files are relative to it.
- lana-agents/elliptic-curves (Lean, pinned by openai/math lakefile at bebec3fc): three source files fetched from
  raw.githubusercontent.com by the L5 cross-check agent for declaration binders (read only).
- Lab records read: branch research/state-sync-2026-10-04 at 9793ff7b and 4a251748 (CURRENT_STATE.md, LATEST_RETURN.md,
  AGENTS.md, work/returns/README.md, the Codex returns BSD_OPENAI_MATH_SCREEN_CODEX_2026-10-11,
  BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11, BSD_NEW_SOURCE_DELTA_CODEX_2026-10-11,
  BSD_SHII_THETA_PERIOD_PUSH_CODEX_2026-10-11; the Claude audits BSD_OPENAI_RELEASE_AUDIT_CLAUDE_2026-10-06 and
  BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06; FULL_COMPENDIUM.md lines 947-949, 1123, 1137, 1147-1155), the release
  claims SEED_CLAIMS_v026.md, and work/plectic_step2_return_2026-09-30/.
- Method: two Workflow runs (scripts in evidence/): 9 manuscript readers + 3 sweeps -> consolidation -> per-candidate
  assessment -> three adversarial lenses (hypotheses / proof dependency / value-circularity) -> synthesis + critic;
  and 6 assessors + 6 refuters for the Codex reuse leads. All agents Fable 5.1; ~75 agents in total; outputs in
  evidence/. These are model readings of unrefereed manuscripts, not proof verification.
- Computation: checks/twist_bsd_quotient.py (pure Python, < 1 s): AGM periods and the BSD quotient of the twist E^{-7};
  reproduces the lab's PARI record (Omega_E, Omega_{E^{-7}}, Tamagawa 32, torsion Z/2, predicted #Sha = 49).
- Not done: no arxiv access (network policy); no PARI/Sage/Lean available; no build of the Lean library; no commit to
  any branch other than the one named in the custody record; no change to the research repository.
