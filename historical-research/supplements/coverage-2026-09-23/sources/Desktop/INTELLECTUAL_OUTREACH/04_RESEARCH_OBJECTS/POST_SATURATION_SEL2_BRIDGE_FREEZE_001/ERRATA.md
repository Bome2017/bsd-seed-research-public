# Errata

Recorded, never silently repaired. Every entry below remains uncorrected in the
frozen artifacts it describes; downstream objects carry it forward unedited.

---

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and
nonsplit `I₁` at 31 into a row that was about the **twist**. `BSD_CHAIN.md` §4 is
authoritative: the twist has **nonsplit `I₄` at 2, split `I₁` at 31**. The
Tamagawa product `(2,1,2)` is unaffected, and no downstream conclusion changes.

Status: carried in every packet since, unedited. Not repaired in place.

---

## E2 — PRO_1 cites a mathlib identifier that does not exist at the pin (new)

`01_pro_1/FINAL_REFEREE_REPORT.md`, source register `[M14]`, cites
`Submodule.exists_basis_of_pid`.

At `8f9d9cff6bd728b17a24e163c9402775d9e6a365` that identifier occurs **only inside
the module doc-comment** of `Mathlib/LinearAlgebra/FreeModule/PID.lean` (line 34).
It is not a declaration. The real declarations are:

    Mathlib/LinearAlgebra/FreeModule/PID.lean:299  Submodule.basisOfPid
    Mathlib/LinearAlgebra/FreeModule/PID.lean:533  Submodule.smithNormalForm

**Assessment.** PRO_1 transcribed a stale name from mathlib's own doc-comment, so
the defect originates upstream. The ingredient `[M14]` classifies — generic PID
module algebra, `ALREADY_IN_MATHLIB` — is genuinely present under the two real
names, and `Submodule.smithNormalForm` (also cited) is correct. **No
classification, verdict, or dependency changes.**

Status: uncorrected in `01_pro_1/`. Do not edit the frozen report.
Evidence: `receipts/PINNED_MATHLIB_LOCAL_VERIFICATION.txt` §E.

---

## E3 — PRO_2 references an artifact it did not deliver (new)

`02_pro_2/REFEREE_REPORT.md:40` and `02_pro_2/MATHLIB_SURVEY.md` both cite
`PINNED_SOURCE_REGISTER.json` as the place where "all usable positive declarations
are named and sourced".

That file is **not in the return**. Delivered: `ARISTOTLE_TASK.md`,
`DEPENDENCY_GRAPH.json`, `DEPENDENCY_GRAPH.md`, `MATHLIB_SURVEY.md`,
`PRE_COMPARISON_RECONSTRUCTION.md`, `REFEREE_REPORT.md`, `STAGE_II_COMPARISON.md`.

**Assessment.** `MATHLIB_SURVEY.md` contains a prose source register `[M01]–[M20]`
naming files and declarations, so the evidence is not lost — only the machine-
readable duplicate is. All 19 paths it cites were verified present locally.

Status: `EXTRACTION_STATUS = NOT_DELIVERED`. **Not reconstructed.** If the operator
wants it, request it from the same run; do not synthesise a replacement and do not
back-fill it into `02_pro_2/`.

---

## E4 — the operator's quoted convergence block is an 11-row transcription (new)

The reconciliation headline supplied by the operator omits two rows that appear in
**both** referee reports: `STAGE_I_INDEPENDENCE = PASS` and
`MATHLIB_SELMER_OBJECT = PRESENT`.

The second matters. Read without its disambiguation, `PRESENT` invites exactly the
error both referees warn against. Both immediately qualify it: PRESENT refers only
to `IsDedekindDomain.selmerGroup`, the Dedekind-domain object `K(S,n)`, and PRO_1
adds the explicit row `MATHLIB_ELLIPTIC_SELMER_OBJECT = ABSENT`.

Status: the operator's block is preserved verbatim in `STATUS.md`. The missing rows
are restored in a **separate** block below it rather than inserted into it.
