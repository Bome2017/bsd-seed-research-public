# Continuation of Codex's interrupted class-lift coupling experiment

Written 2026-10-14 by Claude (Opus 5.5) at the user's request: Codex is unavailable until about 10-20, so this copy picks up
the run where Codex stopped. **Codex's original folder `~/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13` is untouched**; this
folder began as a byte-identical copy (257 files, `ORIGINAL_MANIFEST_AT_COPY.sha256`, verified after copying). Codex may later
resume its own folder independently; the two can then be compared.

## Where Codex stopped (from its files, not from memory)

- `CONTRACT.md` (Codex, 10-13 18:10): find a complete rank-two full-image mod-3 control with nontrivial class source, build
  the class-to-defect map c ↦ D(β_c) mod D(U), and determine which admission block excludes class directions. Branches to
  record separately: rejected by scalar action; removed by global additivity; rejected locally after unit repair; survives and
  is a point; actual excess survives. Initial cap 24 rank-two candidates, "to be reassessed only from results"; per-field cap
  90 s and 1 GiB.
- `search/SCAN_STATE.json`: all 24 initial candidates scanned. Relevant (ordinary anti-invariant C3): 718b1, 997c1, 1070a1.
  Timeouts 794a1, 817a1, 997b1 all printed CLASS=[] before timing out, so they carry no class source (GRH-provisional).
- `arithmetic/REPORT.md` (Codex draft, 18:28) and `review/` (18:17–18:28): all three relevant curves fully analyzed; in every
  admission block the class defect rank is 0 and the class direction is repaired into rational points
  (718b1 → P1+2P2, 997c1 → 2P1+P2, 1070a1 → 2P1+P2). All of Codex's reviews printed PASS (identities, saved matrices, local
  leaf replay, rational Hensel precision, 718b1 ray pushout).
- `STATE.json` was last written at 18:24 and still says "running"; `RESUME.md` says the search "continues for an
  unrepairable class; do not mark complete prematurely". No top-level REPORT, MANIFEST or publication exists.

So the one unfinished scientific task is: **continue the search for a full-image rank-two control whose ordinary class
direction cannot be repaired by global units at some admission block (class defect rank > 0)** — the branch Codex had not
observed — and close the bookkeeping.

## What this continuation does (decided here, from Codex's results)

1. Replay Codex's reviews in the copy to confirm they reproduce.
2. Reassess the cap from results (3 relevant fields in 24, all repaired): scan the **next 24** rows of the same candidate
   list with Codex's unchanged filters (isogeny index 1, 3 ∤ N, prior controls excluded) and unchanged per-field limits
   (alarm 90 s, PARI stack 1 GB, 100 s outer timeout, setrand 20261013). Scan the whole batch; do not stop at the first hit.
3. For every relevant certified field run Codex's unchanged templates: `analyze_template.gp`, `checks/coupling.py`,
   `local_certify_template.gp`, and `witnesses.gp` when the class is repaired. If the joint class defect rank is positive,
   keep the `unrepairable_lift_certificates` from `coupling.py` as the exclusion witness instead.
4. Classify each relevant curve by Codex's branches. Stop extending if an unrepairable class is found or after this batch;
   any further extension is the user's or Codex's call.
5. Do not use Sha labels, L-values or expected outcomes to infer any dimension. No paid jobs, no pushes, no seed computation.

Endpoint effect of any outcome: none on FIN, ORDER9 or Q36. This is a control experiment at coefficient 3.
