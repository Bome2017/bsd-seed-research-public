# v0.2.1 patch release check

The three verified Pro corrections are applied and the PDF is rebuilt. Their exact before/after hashes are in `PATCH_APPLIED.json`. The mathematical source commit is `f757b0f37c66d17aa1d08475b933780d322cb2aa`; final packaging is identified by tag `v0.2.1-private-review`.

- All 18 retained portable checks passed on the patched tree. This includes exact downstream coefficient arithmetic, the independent D5 certificate/verifier and the lattice failure control.
- The patch checker verifies the exact rational containment of the retained Arb dump, including displayed-midpoint error; both citation corrections; unchanged authoritative claim/provenance bytes; the imported report hashes; and all 681 coverage-supplement manifest entries.
- The rebuilt PDF remains 32 pages. Pages 1, 7, 25 and 30 were rendered and visually inspected. No unresolved references, overfull boxes or missing glyphs were found in the final TeX log. Nonfatal bookmark and underfull-box warnings remain.
- The targeted private-identifier/credential scan passed, including recursive archives. This is not a comprehensive privacy guarantee; documented researcher names, paraphrases and local paths remain.

The Pro reports are retained as reviews of v0.2.0, not falsely relabelled as independent checks of v0.2.1. The coverage supplement was not part of those reviews. The old second-review map and old navigation are preserved; the current map redirects only the old SHARING entry to its unchanged historical copy. New navigation and patched sources have separate bindings.

No new full corpus evaluation, Lean rebuild, primary-literature theorem audit or human review was performed for this packaging revision. No BSD endpoint or evidence grade was promoted.

Run records are in `v0.2.1_logs/`; the final root manifest binds them and the paper. ZIP-to-Git-tree verification and upload records accompany the delivered bundle outside the snapshot, avoiding a self-referential archive hash.
