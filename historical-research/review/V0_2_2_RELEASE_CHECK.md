# v0.2.2 editorial release checks

The paper has exactly two editorial corrections: the Bertolini–Darmon bibliography and the explicit first-layer definition of t. Mathematical claim grades, the claim ledger, evidence provenance and Lean source are unchanged.

- Portable verifier: 18/18 checks passed.
- Historical and current editorial binding checks: passed.
- PDF: 32 pages, rebuilt with TeX Live; affected pages 28 and 30 visually inspected. No undefined citations/references, overfull boxes or missing glyphs. Existing nonfatal hyperref/underfull warnings remain.
- Bounded privacy-pattern scan: no matches; scope is recorded in its log.
- The unchanged Lean core was replayed in the preceding audit, not redundantly rebuilt for this editorial patch.

Logs are in `review/v0.2.2_logs/`. The root manifest binds every packaged file except itself. Prior tagged releases and their reviews retain their historical scope. The versioned Git tag identifies the final package; SOURCE_SNAPSHOT.json identifies the source commit before the PDF and final packaging metadata.
