# openai/math scan for the BSD seed — return of 2026-10-11 (Claude, Fable 5.1)

**ONLY_CONDITIONAL_ITEMS; NO_NEW_SEED_BOUND; CODEX_REUSE_LEADS_CLOSED; TWIST_2_PART_DERIVED_LAB_SIDE (desk-check pending).**

Read [REPORT.md](REPORT.md) first (status, inventory, the one conditional item, killed items, specific answers,
risks, next actions), then [CODEX_LEADS_CROSSCHECK.md](CODEX_LEADS_CROSSCHECK.md) (independent re-read of the six
reuse leads in the Codex 2026-10-11 screen; all closed). [SOURCES.md](SOURCES.md) records what was read and how.

What this return establishes, at its grades:
- openai/math @ fd4aeeb2 contains no statement applicable to the seed curve E (Selmer corank ≥ 2 at every prime):
  nothing for FIN (uniform part or the named remainder 59, 487, 2243, 4547, 5843), ORDER9, Q36, lemma TH at 5843,
  or any lab computation cost. Model reading of the manuscripts with file:line citations; not a proof audit.
- The one instance whose hypotheses the seed data satisfy is the rank-0 twist E^{-7}: family 002, if its ~31,000-line
  unrefereed chain were sound, would give #Ш(E^{-7}/Q) = 49 exactly (grade ceiling IMPORTED_PREPRINT; the lab records
  49 as a BSD prediction and has moved the twist off the critical path). The chain audit is explicitly declined.
- Lab-side, with published inputs only: a 2-isogeny descent gives dim Sel_2(E^{-7}/Q) = 1, rank 0 and
  Ш(E^{-7}/Q)[2^∞] = 0 (evidence/verify/e7_two_isogeny_descent.py and e7proof/, two implementations, three controls
  including the seed itself). Grade on desk-check: PROVED_COMPUTER_ASSISTED; review level now: MODEL_SAME_FAMILY.
- No openai/math Lean artifact covers any arithmetic family; every openai/math statement stays IMPORTED_PREPRINT.

Layout: `evidence/map/` (12 manuscript/sweep maps), `evidence/candidates.json`, `evidence/assess/` (7),
`evidence/verify/` (6 lens records + the descent and hypothesis scripts), `evidence/codex_leads/` (6 assessments +
6 refutations), `evidence/workflow_*.js` (the two orchestration scripts), `context/SEED_CONTEXT.md` (the brief given
to every agent, including the lab state as of 4a251748), `checks/` (twist BSD-quotient replay). Paths of the form
`scratchpad/scan/...` inside REPORT.md map to `evidence/...` here. `MANIFEST.sha256` binds every file; the custody
record is `../OPENAI_MATH_SCAN_CUSTODY_2026-10-11.json`. Custody certifies bytes, not theorems.

FIN, ORDER9 and Q36 are unchanged.
