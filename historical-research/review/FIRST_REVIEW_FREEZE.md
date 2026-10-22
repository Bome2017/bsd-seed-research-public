# First-reviewed snapshot 0.1.1

This is the corrected local review copy dated 2026-09-23, on `review/codex-first-pass`. It is based on original release HEAD `ce6536bed8f6c20084f610fab92b55c318cf2b32`; the original frozen tag and archive remain unchanged. `FREEZE.md` is their historical receipt, not the receipt for this version.

The reviewed export contains the 25-page manuscript, 76 claims, 3,360 evidence files, the repaired coefficient verifier, replay logs, the first-review report and per-claim coverage. It contains no Git history, external coefficient corpus, private redaction configuration or paid computation results. The original Git history is not safe to push without handling the private identifiers identified in this review.

`MANIFEST.sha256` binds the files in this snapshot, excluding itself. `review/REVIEW_BINDINGS.json` separately binds the repair, review records and replay evidence. The archive hash and final commit are recorded in an external `DELIVERY.md` alongside the archive, avoiding a self-referential archive hash inside its own contents.

Run `python3 tools/verify_release.py` for portable checks. Its final output is recorded in `VERIFICATION_RUN.md`. The A3 Lean replay was separately completed against the pinned toolchain and is bound in the review logs; it need not be rerun to verify the portable checks. See `FIRST_REVIEW.md` for what the checks do and do not prove.

No release repository was created, pushed, published or shared by this review. No canonical master or original sealed computation was changed.
