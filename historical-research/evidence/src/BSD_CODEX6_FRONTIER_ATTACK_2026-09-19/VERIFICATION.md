# Final verification record

- Handoff manifest: 11/11 entries match at first check and final recheck.
- Handoff referenced small-file hashes: 35/35 match at first check and final recheck. This includes custody of the p5 manifest file, not replay of all its members.
- Source snapshot: 75/75 files match the full hashes in SOURCE_SNAPSHOT.json. Reading scope is explicit per entry.
- Required report/state files exist; JSON parses; Markdown fences balance; all local Markdown targets resolve.
- Numerical script replayed at 100 digits/30 terms and 80 digits/24 terms. Recorded outputs reproduce exactly. Strong intervals nest in the weaker intervals.
- Arithmetic fields agree exactly under system Python 3.13.2 and bundled Python 3.12.14. Each final replay used less than 0.12 CPU-second. Details: REPLAY_VERIFICATION.json.
- Exact rational checks prove the D=174 spacing inequality and place both 36-1/175 and 36+1/175 inside the current interval.
- Source folders were not edited. No prime-symbol run, L-series stream rerun, proof-assistant session, or historical archive rebuild was performed.

The mathematical prose was checked locally against the quoted Ota hypotheses, the source's core-pair normalization, the exact local-height and AGM identities, and the explicit countermodels. This was not a separate external referee review or a Lean kernel proof.

MANIFEST.sha256 is generated last and binds every regular file in this output directory except itself. It does not hash external linked sources; those have their separate SOURCE_SNAPSHOT.json binding.
