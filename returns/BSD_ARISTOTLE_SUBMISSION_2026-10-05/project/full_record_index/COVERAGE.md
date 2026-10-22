# Coverage, omissions, and custody — read before claiming completeness

This is a broad captured BSD record with explicit boundaries, not a claim to have
proved every included statement or searched every inaccessible byte on the machine.
The inventory covers 4,179 discovered roots, reduced to 544 nonoverlapping directory
walks plus individually cited files. An additional pass recovered conversation
attachments and the visible user/assistant research record.

## Actual coverage

| Item | Count / disposition |
|---|---:|
| Original path identities in final catalog | 538,072 |
| Unique embedded byte objects | 283,307 |
| Bytes in those unique objects before compression | 7,024,429,358 |
| Lossless evidence volumes | 84 |
| Earlier compendium units, preserved in full | 7,042 |
| Compendium evidence references checked | 22,794 |
| File citations whose bytes are embedded | 22,725 |
| Directory / repository citations with captured descendants | 69 |
| Unresolved compendium citation paths | 0 |
| Current governing reading-room source files | 54 |
| Directly browsable current dossier files | 5,043 |
| Historical stop/correction units reproduced in full | 3,353 |
| Released claim statements with dependencies | 89 |
| Visible conversation messages preserved | 1,719 |
| Verified local Git histories | 3 bundles, 12 parts |

The original compendium, extracted units, quote/correction fields and all located
source versions remain separate. Identical bytes are deduplicated by SHA-256;
every original filename remains an alias. Different versions are never merged
because they happen to share a name.

## The scientific bytes that are external

**Raw binary computation stores larger than 1 MiB are not embedded.** Their 14,047
regular-file inventory entries total 156,808,997,323 bytes, including repeated
copies. There are 12,989 distinct digests totaling 143,585,239,078 bytes. Each was
freshly hashed from the local file during this build. Their paths, sizes, digests
and disposition are in `BULK_BINARY_RECEIPTS.jsonl.gz` and the catalog. Another
23,686 symlink aliases point to those external hashed files.

Their source producers, retained checkers, recorded results and custody manifests
are included when present in the discovered roots. A hash is not the binary data
and is not a replay. A run requiring those raw bytes must obtain them from the
recorded local source or regenerate them under the original contract. `record.py`
can explicitly restore verified local bulk files with `--include-bulk-from-local`.
This package alone cannot replay a calculation requiring an external corpus.

## Missing old upload paths

Five old temporary ZIP paths no longer exist. Each corresponding extracted dossier
was located and captured. `EXPIRED_UPLOAD_RECOVERY.json` lists the missing ZIP and
every matched surviving member. We do **not** claim to have recovered the original
ZIP bytes, its exact member order, or any absent member solely from a folder name.
The original source-binding/check records remain available for that comparison.

## Deliberate non-research exclusions

27 credential/OS metadata paths and 337 regenerable compiled outputs were excluded.
129 runtime/VCS/cache or symlink-directory locations were pruned by the published
discovery policy. Sources, toolchain identifiers and recorded build logs are kept;
the complete Lean/Python/Sage installations and package caches are not bundled.
The three principal local repositories additionally have verified full-ref Git
bundles. Other Git internals are not recursively copied. No un-fetched remote branch
or inaccessible cloud-only artifact is asserted to be present.

All 44,952 file symlinks were resolved to either an embedded digest (21,266) or an
external hashed digest (23,686). Original symlink identities and targets remain in
the catalog. The restoration tool uses verified bytes rather than creating
arbitrary filesystem links.

## Discovery scope

Discovery includes BSD/K167-named home projects; BSD-related Desktop, Downloads
and Documents material; the compendium's cited projects and slice inventory;
the current/release/cloud lab trees; this conversation's accessible remote
attachments; the exact older pasted attachments named by the user; and an explicit
supplement for the partially written earlier Aristotle handoff. Read
`DISCOVERY_ROOTS.json`, `PRUNED_DIRECTORIES.json`, and the complete compressed file
inventory for the exact boundary. This is not a forensic image of the entire Mac.

No source read errors or files changing during their individual capture were
reported. Captures are a file-by-file snapshot, not an atomic freeze of all work
on the computer. The source-stability check, when present, reports later changes
without silently replacing the captured identity.

## Search versus possession

All 538,072 paths are filename searchable. The compact full-text index covers
23,674 unique scientific prose/code objects, with a 2 MiB prefix
limit recorded per object. Vendor library sources and raw numeric tables are not
full-text indexed; embedded bytes remain retrievable in full. Search absence is
not evidence that the underlying mathematical item is absent.

## What verification means here

Source hashes, copied-source bindings, evidence-volume integrity, byte-for-byte
retrieval, citation coverage, complete unit counts, and Git bundle verification
are custody checks. They do not independently validate 283,307 mathematical files.
The new 44-card wall atlas is a source-linked synthesis, not a fresh referee report
for every theorem. Existing proof, review, computation, conjecture and formal
verification grades are retained. The three seed endpoints are unchanged.

The final coverage check also captured a [concurrent Aristotle draft](../sources/concurrent_aristotle_draft/CAPTURE_READ_FIRST.md) with 37 additional files, including its newer wall atlas and Lean templates. These are a separate timestamped snapshot with no new proof promotion.
