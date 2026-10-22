# BSD seed research — public evidence edition

This is a public, history-free research record for the rank-two curve

\[
E:y^2=x^3-22735x^2+106272484x,
\quad N=6503188012738584.
\]

**Full BSD for this curve is not proved. FIN, ORDER9 and Q36 remain open.** The project has finite arithmetic results, written deductions under retained inputs, conditional certificates, and recorded unsuccessful experiments. They are not one completed proof.

The intended endpoint is

\[
\#\Sha(E/\mathbf Q)=9,
\qquad q_E=\frac{L''(E,1)}{2\Omega_E\operatorname{Reg}(E)}=36.
\]

Start with [current status and evidence](CURRENT_STATUS.md), the [graded record index](PUBLIC_RECORD_INDEX.md), and the [correction precedence](CORRECTIONS_AND_SCOPE.md). The original [release claim index](historical-research/claims/CLAIM_INDEX.md) and [manuscript](historical-research/paper/seed_bsd.pdf) retain their historical grades and dates; later records are separately graded rather than silently inserted into that release.

## What this edition publishes

This edition assembles the retained research release and the subsequent experimental record through the pinned snapshots in [publication/BUILD_SUMMARY.json](publication/BUILD_SUMMARY.json). It also includes original mathematical returns from six separate lab branches. Those records are available here, not only through private-repository links.

Written proofs, imported theorems, conditional statements, exact algebra controls, arithmetic computations, formal checks, and author/model reviews remain distinct. No human peer review, literature novelty, or complete formal verification is claimed unless a particular source record explicitly supplies it. Mathematical statements in unsuccessful experiments remain scoped to their stated hypotheses and tests.

**Publication supplies a dated public disclosure of these exact files. It does not by itself establish novelty, correctness, or priority over earlier work.** Historical private commit dates identify provenance, not earlier public disclosure. Contributions using published mathematics are attributed in their source records.

## Integrity and reuse

Run:

```sh
python3 publication/verify_public_export.py
```

This verifies the public manifest and source/transformation ledger. It is an identity check, not a proof or a large arithmetic replay. Checkers inside individual dossiers retain their own scopes; some require omitted large data or external dependencies. Do not run historical launch instructions as current authorization. Historical proof-assistant projects may include deliberate negative/axiom-injection controls; their presence is not endorsement or a claim that those controls prove a theorem. No top-level build imports every archived Lean file.

The [source bindings](publication/SOURCE_BINDINGS.json) give original repository/commit/path and original/released SHA-256. The [redaction ledger](publication/REDACTIONS.json) records privacy transformations without publishing removed text. The [omission ledger](publication/OMISSIONS.json) records excluded nested archives, bulk data and third-party source copies. Historical manifests describe their original packets and are not substituted for this edition's manifest.

The prior private repositories and their history are preserved. This public edition excludes private correspondence and does not expose those histories. Absolute local paths may remain as provenance or execution records; they are not available public storage locations.

No license is newly granted by this publication. Existing third-party notices and attribution remain applicable. All rights reserved for original material unless a file states otherwise.
