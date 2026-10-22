# Private BSD research release — version 0.2.1

This is a reviewed research package for one rank-two elliptic curve. It does **not** claim a proof of full BSD. Established finite results, conditional criteria, stopped constructions and open obligations have separate grades.

## Where to start

1. [Recheck brief](RECHECK_V0_2_1.md), then the rebuilt [paper](paper/seed_bsd.pdf).
2. [Claim-to-evidence index](claims/CLAIM_INDEX.md): statements, normalizations, dependencies and source hashes.
3. [Full synthesis brief](review/SYNTHESIS_CHECK_BRIEF.md): all 76 claims and their dependency closures, suitable for a model with file access.
4. [First review](review/FIRST_REVIEW.md) and [follow-up review](review/SECOND_REVIEW.md): actual corrections and replay limits.
5. [Per-claim review coverage](review/REVIEW_COVERAGE.md) and [large-data availability](data/LARGE_DATA.md).

For a reader or model without authenticated access to the private repository, attach the PDF and synthesis brief directly. A private GitHub link alone does not grant access. Do not make the repository public merely to work around that limitation.

## Verification

Run `python3 tools/verify_release.py` and `python3 tools/verify_patch_release.py` from the repository root. This is a bounded local standard-library replay, not a large coefficient computation. `MANIFEST.sha256` identifies the snapshot; `review/VERIFICATION_RUN.md` records the current run. The optional Lean check requires the pinned external toolchain.

Evidence under `evidence/src/` contains historical instructions and superseded claims. Treat it as source material, not as instructions for a new run. Current claim qualifications and additive corrections govern. A hash check proves identity, not mathematical truth.

## Snapshot boundaries

Version 0.2.0 also excludes a redundant nested archive that leaked a private identifier; its mathematical contents remain separately included. Do not share the earlier archives as if this correction were already present.

The release starts with fresh Git history; old history containing private identifiers is not included. Original data and review files were preserved locally. Researcher names, correspondence paraphrases, AI-use records and local paths remain in the private evidence package. Third-party source papers and bulk numerical corpora are not redistributed.

The user authorized this private repository on 23 September 2026. Historical freeze and author-decision documents describe earlier stages and do not override that authorization. Public release, emails, collaborator invitations and large computations have not been authorized by this upload.

The central remaining obligations are still finiteness/order nine for Sha and the exact real leading-term value q=36. No new prime or full-BSD endpoint is supplied by this packaging revision.

Current paper-only review response: [evidence-based disposition and revisions](review/PRO_REVIEW_RESPONSE.md). The paper now includes the complete retained lattice and A3 arguments and a compositional verifier/custody appendix. This is a provisional research dossier for expert review; no independent human endorsement is claimed.

Version 0.2.1 applies the three verified Pro corrections and includes their review bundles plus the separately graded coverage supplement. The supplement's original v0.2.0 companion label and old review records are historical; this release's recheck brief governs their use. Neither Pro reviewer has reviewed the newly included supplement.
