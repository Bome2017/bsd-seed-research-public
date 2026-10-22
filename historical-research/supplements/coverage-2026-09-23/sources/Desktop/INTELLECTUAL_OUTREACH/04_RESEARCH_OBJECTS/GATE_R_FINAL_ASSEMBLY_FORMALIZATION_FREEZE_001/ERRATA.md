# ERRATA

Recorded, not repaired, as always.

## E1 — the platform attribution banner, and a gap in my own first check

`README.md` differs from the shipped byte string in **both** returns: nine lines of Aristotle
attribution text, identical in the two returns and therefore platform-generated rather than run
work.  Full text and treatment in `receipts/PLATFORM_BANNER_OBSERVED.txt`.

**The gap is mine.**  My first inherited-bytes check compared only `*.lean`, `lakefile.toml`,
`lake-manifest.json` and `lean-toolchain`, and reported "40 files checked, 0 altered."  That
sentence was true of what it checked and misleading about what it implied, because it silently
omitted every `.md` and `.txt` I had shipped.  The alteration surfaced only when I replayed the
returned manifest, which does cover them.  Corrected figure: two files differ in each return —
the deliverable and `README.md`.  Correction going forward: an inherited-bytes check must
enumerate the shipped manifest, not a hand-written extension list.

## E2 — my construct scanner was silently broken and printed a row of zeros

My first forbidden-construct scan reported every token as 0 in both returns.  It was broken:
the file list was passed as an unquoted zsh variable, which does not word-split, so `perl`
received one enormous filename, opened nothing, and produced no matches.  Zero hits for
`sorry` and zero hits for `theorem` alike.

This is the third appearance of this defect family in the programme and the second appearance
of this specific zsh trap.  It was caught only because I ran positive controls before trusting
the zeros.  The re-run scanner, with controls printed alongside every count, is
`receipts/scan.py`, and its output is `receipts/CONSTRUCT_SCAN.txt`.  The verified result is
unchanged in substance — every forbidden token is 0 in the deliverable — but the first
statement of it was worthless.

Correction going forward, restated because it keeps recurring: **a scan that reports absence
must report a positive control from the same code path in the same output.**

## E3 — inherited SelmerSet / LocalKummer hits, scoped correctly on the second pass

The whole-tree scan shows `SelmerSet` 12 and `LocalKummer` 24 in both returns.  Every hit is in
an inherited frozen file — `Run013/Selmer.lean`, `P04b/Reconnect.lean` — printed by file and
line in the receipt.  These are the certified explicit square-class definitions of the existing
base, not a cohomological Selmer object, and neither run introduced them.  Scoped to the file
under test the counts are 0.  Same family as the E6 recurrences in earlier freezes; handled the
same way, by scoping the claim to the file under test and printing every matching line.

## E4 — both runs' custody self-reports overstate

Run A: "every frozen file still matches `MANIFEST.sha256` byte for byte" — false as stated,
because of `README.md`.  Run B: "with the job file as the sole difference" — false, same cause,
and phrased more explicitly.  Neither overstatement touches a theorem.  Both reports are
preserved unedited; the check is `receipts/RUN_CLAIMS_VS_REALITY.txt`.

## E5 — one claim of Run B's that I did not verify

Run B reports an explicit two-target build at 8061 jobs.  My rebuild ran the default target at
8062 jobs and I did not reproduce the explicit invocation's count.  Recorded as **unverified**
rather than accepted or disputed.

## Carried forward, unrepaired

The six errata against Claude artifacts in
`CODEX_GATE_R_BLIND_AUDIT_FREEZE_001/ERRATA.md`, including the false "second pass" claim about
self-referential digests, and `THEOREM_STATUS.md` §3.1's finite-generation overstatement, which
this freeze now definitively settles: rank zero was reached without finite generation.

## E6 — my seal tool excluded nested indices; caught before archiving

The tool that writes `MANIFEST.sha256` excluded every file *named* `MANIFEST.sha256` at any
depth, not just this object's own. Because this object carries three complete objects inside it,
that left eight nested index files — four `MANIFEST.sha256` and four `DIGESTS.md` — covered by
neither this object's manifest nor its digest list. The symptom was a manifest with 219 entries
against a digest list with 214, a gap of five where only one was expected.

Caught before the archive was built, by checking the two counts against each other instead of
assuming the difference was the single self-entry. The tool now excludes only the two **root**
indices; nested ones are ordinary members, because inside this object they are data, not
indices. Final coverage: **223 files on disk, 223 manifest entries.**

No previously sealed object is affected: the three objects sealed earlier in this session were
checked and contain no nested index files. Recorded because the flaw was latent through four
seals before it had anything to bite.
