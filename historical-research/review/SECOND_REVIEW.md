# Lattice and privacy follow-up (interim 0.1.2 work)

The later paper-only review response in `PRO_REVIEW_RESPONSE.md` governs the final 0.2.0 sharing snapshot. The interim 0.1.2 snapshot was not uploaded.

23 September 2026. The user authorized another check and a private GitHub upload. This review starts from the history-free v0.1.1 archive (SHA-256 `f89013d854b7453808fd8f947ea2333a5adeaebdc4357b54177a2bbdba702ed6`). Original releases, master records and source folders remain unchanged.

## What was checked

The follow-up `BSD_SEED_LATTICE_IMPORT_CHECK_2026-09-23` report was read against the underlying Manin gate, its governing referee corrections and the cited local CNS statements. The intersection-bound arithmetic was rederived:

`(2*mu-4*c') - 3*(mu/6-c'+mu/4) = 3*mu/4-c'`.

Dividing by the retained positive intersection lower bound `mu/12` gives `K <= 9-12*c'/mu < 9`, hence the integer bound `K <= 8`. This verifies the algebra of the estimate, not an independent construction of the integral modular-curve model. The geometric premises remain those of the written project proof and the source imports it lists. The new report does not turn this derived lemma into a published theorem or a human-reviewed proof.

The local arithmetic was rerun for the seed and its displayed 2-isogenous partner. A separate exact implementation checks the valuations and j-invariant, counts a good curve with j=1728 over F_4547, and checks each certificate denominator separately. This check does not itself enumerate the entire rational isogeny class or prove the integral-model geometry.

## Corrections to the new report

1. **There is no nine-power margin for the released lattice.** From `v_2(c0) <= 8`, `c_E | 2*c0`, one obtains `2*c_E | 2^10`. That is exactly the worst-case requirement for `(1/1024)Z`. The historical margin of nine compared an older target `v_2(c0) <= 17` with the proved bound eight; it cannot be transferred to the current lattice requirement. The original new report is preserved as evidence; this paragraph supersedes its sensitivity sentence.
2. **The old local-check script was not fail-closed.** It printed failure text but always exited successfully. Its combined product of lower-level denominators was also less explicit than its label. The new `tools/replay/lattice_local_checks.py` tests denominators separately and exits nonzero on a failing check. An injected failure is tested by the release verifier. The historical script is not overwritten.
3. **Additive trace zero is not the supersingularity test.** The relevant input is potentially good reduction with j=1728 and `4547 = 3 mod 4`, not just `a_4547=0`. The local replay and current wording use that input. A direct point count on `y^2=x^3-x` supplies a small independent arithmetic check.

## Direct Edixhoven source check

Theorem 4.6.3 was checked directly in [Edixhoven's 1989 thesis](https://websites.math.leidenuniv.nl/edixhoven/publications/1989/phd-thesis.pdf), printed pp. 60-61 (PDF pages 61-62). Its potentially supersingular branch excludes p from the optimal Manin constant for p>7, with the stated additive-type exclusions and absence of a rational p-isogeny. The seed's type III and p=4547 satisfy these conditions; the isogeny exclusion is supplied by the retained rational-isogeny theorem. This upgrades the theorem-statement reading grade from a recorded quotation to a direct primary-source check. It does not claim a fresh proof of the thesis or of Mazur's theorem. The thesis is cited and hash-identified, not redistributed here.

The two published restatements remain corroborating sources. The CNS passages for component multiplicities, the Frobenius-kernel description and rational singularities at 2 were checked locally. Katz-Mazur, the adjunction input and mass formula are still not newly reconstructed from their original proofs. Step B's geometry at 2 remains the highest-value human review target for A.4.

## Numerical and operational scope

The v0.1.1 package passed its 13 portable checks before changes. The current verifier adds the local-lattice replay and its failing-control test. No coefficient corpus extension, new large certificate, paid computation or renewed 2243 run occurred. The previous A3 Lean, full saturation and 3-adic height replays are retained and hash-bound; their unchanged code was not pointlessly rerun.

The 2243 pilot still contains the old coefficient verifier; this was confirmed by a byte comparison with the legacy source. Production remains blocked on installing the repaired verifier **and** correcting its independent F4 restart defect. Uploading this evidence does not authorize running that pipeline.

## Release and privacy

The recursive follow-up scan found a known private identifier inside `returned/AWARE.tar.gz`, within another nested tarball. The first review had not descended through that second layer. The redundant outer archive is excluded from this version. All ten nonarchive outer files already match the unpacked copies byte for byte; all 15 substantive inner records also remain, with the existing redaction where needed. Only 18 AppleDouble metadata entries have no retained counterpart. The exclusion and content-coverage proof are recorded in `evidence/EXCLUDED.tsv` and `review/followup_logs/nested_archive_coverage.json`. No claim referenced the removed container.

The evidence builder now inspects nested TAR and ZIP containers, excludes unreadable or over-budget archives, and has a regression that reproduces the privacy failure using dummy identifiers. Earlier v0.1/v0.1.1 archives should not be used for sharing without this correction.


This version is a new Git root created from the reviewed archive, not a push of the old local history. Known private identifiers and credential patterns are checked before upload, including archive contents. Researcher names, documented correspondence paraphrases and local provenance paths remain, as already disclosed; the destination is private. Bulk coefficient data, source-paper PDFs, credentials and private redaction configuration are outside the repository.

`SHARING.md` is the current entry point for readers and AI reviewers. Prior reports saying that nothing had been uploaded describe their historical snapshots. The local external delivery receipt records the actual GitHub visibility and pushed commit after upload. FIN, ORDER9, Q36 and all uncomputed witnesses retain their existing status.
