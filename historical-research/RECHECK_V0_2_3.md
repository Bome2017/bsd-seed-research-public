# v0.2.3 (local, unreleased): the formal check of the finite part

This revision preserves v0.2.2 (tag `v0.2.2-private-review`, commit `2a726213`) and adds one thing: the Lean check of the
deduction behind the vanishing of `Sha[p^∞]` at `p = 5, 7, 11, 13`, together with its evidence.

1. **Paper.** A new Remark 4.4 (`rem:a4lean`) follows Remark `rem:smallcert` in §4. Later §4 numbers shift by one
   (`thm:sha3` is now Theorem 4.5).
   - `paper/seed_bsd.tex` is historically bound, so its title-page date and tag stay those of v0.2.2.
   - `paper/release_id.tex` states that this is an untagged local revision. It gives the base snapshot commit as plain
     text, with no link.
2. **Claims.** `LEAN_CHECKED` is added to S.5, S.7, S.11, S.13 and the criterion B.1, together with:
   - evidence items: the formal-check package, both proof runs, the axiom reports and the replay report;
   - a `formal_check` verification entry;
   - a qualification: every imported theorem enters as a hypothesis (including the unit property of `epsilon_p`), and
     the certified symbol tables enter as hash-bound data;
   - a `post_master` note.

   No statement text, no other claim and no other grade changes. S.3 is unchanged; its separate formal check has not
   been run.
3. **Evidence.** Eight files are added, each byte-identical to its original: the package, both proof returns, both axiom
   logs, the returns manifest, the replay report and the packet index. No existing evidence file changes.
   - The generic `tools/build_evidence.py` would also rewrite 122 reviewed provenance rows and 7 reviewed exclusion rows.
     The changes are metadata only: the categories `review_restored` and `post-master source audit`, binding
     descriptions, source roles, originally empty source-hash fields, and exclusion wording.
   - The new `tools/build_evidence_transition.py` prevents this. It dry-runs the unmodified builder with the same privacy
     configuration and proves that each reviewed row's content and privacy disposition are unchanged. It then keeps
     that row byte for byte, and appends only the rows declared in `review/A4_EVIDENCE_ADDITIONS.json`.
   - Its log is `review/A4_EVIDENCE_TRANSITION.json`. Its `--self-test` rejects 12 kinds of undeclared change.

**Bindings.** `review/A4_FORMAL_CHECK_APPLIED.json` is the transition record: base, historical and current bindings,
base copies, the exact claim delta, the evidence, the paper edit and the version labels.
- Five files bound by earlier reviews change: `claims/claims.json`, `claims/CLAIM_INDEX.md`, `evidence/PROVENANCE.tsv`,
  `README.md` and `tools/verify_patch_release.py`.
- Their v0.2.2 bytes, and those of every other edited file, are preserved under `review/history/v0.2.2/`.
- The earlier assertions still run, against those preserved bytes. None is deleted or loosened.
- `tools/verify_patch_release.py` then checks that the v0.2.3 delta is exactly the declared one.
- The unmodified `tools/verify_release.py` passes, and so do its maps `REVIEW_BINDINGS.json` and
  `SECOND_REVIEW_BINDINGS.json`, which cannot be redirected. No edited path is among their entries.

From the bundle root run:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
shasum -a 256 -c MANIFEST.sha256
```

**Controls.** On throwaway copies of this tree, the patch checker passes the unmodified copy and rejects each of seven
corruptions:
- an old provenance row altered, and separately altered with its hash re-bound in the record;
- a sixth claim's grades changed, plain and re-bound;
- one preserved history byte;
- one character of the inserted remark;
- a break-set path dropped from the record.

The re-bound variants are rejected by the specific delta checks, not merely by a hash.

**Not changed.**
- Theorem statements, other grades, certificates, Lean sources, `tools/verify_release.py` and `paper/seed_bsd.tex`.
- The Makefile. Its dependency list omits `release_id.tex`, so the final PDF was built with `latexmk -g`.
- The mathematics. The formal check certifies deductions from listed hypotheses only; it checks neither the imported
  theorems nor the numerical symbol certificates.

FIN, ORDER9 and Q36 remain open. No new computation or research branch is authorized by this revision.
