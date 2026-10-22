# Fable coordinator's cross-model check of V025-BANK (Opus worker), 2026-09-29 23:15

**Verdict: PASS, with required fixes before any push.** The bank is what it declares: v0.2.4 untouched, two local commits,
nothing pushed or tagged, every verifier passes on a clean copy, old evidence rows preserved byte for byte, seven claims
added, seven revised, no grade label changed. Three fixes are required in the follow-on commit (BANK-K); none is a
mathematical change.

## 1. Custody (mechanical): PASS
- `v0.2.5-bank` = `c4e4b83` (content) + `706efb5` (source stamp) on base `001a49f`. No upstream; no tag points at either
  commit; no remote branch contains `c4e4b83`. v0.2.4 folder: clean, HEAD `001a49f`.
- Verifiers run by me on a `git archive` copy of `706efb5` (scratchpad, not the worker's tree): `verify_release.py` 18/18;
  `verify_patch_release.py` V025_TRANSITION_PASS + PATCH_RECHECK_PASS; `verify_v025_transition.py --negative-controls`
  NEGATIVE_CONTROLS_PASS; MANIFEST 4443/4443; `build_evidence_transition.py --self-test` SELF_TEST_PASS.

## 2. The declared exception (`--retained-source-changes`): PASS
- Diff read. A listed row must be a baseline row, produced from the same source path, with released hash = baseline hash,
  live hash = declared hash, source actually changed, and not masked; duplicates rejected; the released file is left
  untouched. Undeclared content changes are still rejected. Without the flag the tool is unchanged. Seven new self-test
  cases cover: undeclared, wrong live hash, wrong released hash, unchanged source, masked row, non-baseline row, duplicate.
- The five rows are exactly the Codex-edited master files (00_READ_FIRST, MANIFEST, MASTER_BSD_DAG, RESUME,
  SOURCE_BINDINGS of BSD_CODEX6_MASTER_HANDOFF_2026-09-19). For each: released bytes = v0.2.4 bytes; live hash = the
  declaration = the hash in Codex's CHANGES.md.
- `DIAG_transition_baseline.json`: the unmodified tool fails on exactly these five (`released_content_changed`), and on
  nothing else (all other categories empty).
- Evidence tables: PROVENANCE.tsv v0.2.4 is a byte-prefix of v0.2.5 (1,178,658 → 1,215,293 bytes); REDACTIONS and
  EXCLUDED identical.

## 3. Claims: PASS
- 76 → 83: added S.3L, S.3F, S.17-47, B.16, B.17, B.18, B.19; removed none; revised exactly S.3, S.P, S.FIN, B.8, B.11,
  X.14, X.16. `grades` unchanged on every pre-existing claim. S.3 statement byte-identical; its new qualification is
  mathematics only, names the OPEN upper bound with the candidate routes "none established", and does not claim R25.
- Review labels on the new claims are honest (MODEL_SAME_FAMILY / MODEL_CROSS_FAMILY / no label where the family is not
  recorded; "no human review" everywhere).
- **Ota label.** S.17-47 grades Ota v1 as IMPORTED_PREPRINT. The paper is published: Amer. J. Math. 140 (2018), no. 2,
  495–542 (Project MUSE 688523; arXiv 1509.00682). Keeping PREPRINT for the version read is acceptable, but the
  qualification must say the print exists and that the theorem numbering used (v1 Thm 6.4 etc.) was not re-checked
  against it. **Required fix F2.**

## 4. Paper and README: PASS with one required fix
- No process markers in the paper's added lines; frontier wording is scoped ("targeted screens … found no published
  theorem"; "remains open at every prime"). Evidence-description strings in the claims spec use internal jargon in two
  places ("lane 2"); harmless, optional cleanup.
- **E1 slip (integral "Kato 12.5(4), which holds for T₃E")** is present in FOUR outward places, not three:
  `paper/sections/04_primary.tex` l.121, `RECHECK_V0_2_5.md` l.41, `claims/CLAIM_INDEX.md` l.317 and
  `claims/spec/part1_core.py` l.261 (which generates `claims/claims.json` l.809), plus `review/SYNTHESIS_CHECK_BRIEF.md`
  l.277 and `review/V025_BANK_APPLIED.json` l.624. Correct citation: Kato Thm 13.4(3) via 13.14 (12.5(4) is printed for
  V and says nothing at (3)). **Required fix F1**, through the spec + regeneration, and BANK-K's negative control must
  scan ALL released text (paper, README, RECHECK, CLAIM_INDEX, claims.json, spec, review/*.md), not only the three
  files first listed.

## 5. Known limits left as found: agreed, no follow-up needed before push
O.1/O.2 wording true but not sharp; COVERAGE counts stale; VERIFICATION_RUN from 09-23; cubics live in
`verify_certificate.gp` and B2's RETURN; SOURCE_SNAPSHOT stamped by the return's script. All acceptable as declared.

## Required before push (BANK-K)
- F1: E1 citation fix in every outward location, with a whole-tree negative control.
- F2: Ota published reference in S.17-47's qualification (label may stay IMPORTED_PREPRINT).
- F3: none mathematical. Optional: replace "lane 2" in the two evidence descriptions.
Then I check BANK-K, and the push is the user's explicit call.

FIN, ORDER9 and Q36 are unchanged.
