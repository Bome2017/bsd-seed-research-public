# v0.2.2: two editorial corrections

This revision preserves v0.2.1 and changes two items in the paper:

1. Restore Bertolini–Darmon, *Derived p-adic heights*, American Journal of Mathematics **117 (1995), no. 6, pp. 1517–1554**. The first review's supposed pagination correction was wrong; its historical report is preserved, not silently rewritten. The correction is confirmed by the authors' publication list and their own bibliography (BD95, page 59):
   - https://www.esaga.uni-due.de/massimo.bertolini/publications/
   - https://www.math.mcgill.ca/darmon/pub/Articles/Research/29.Millenium/millenium.pdf
2. In Appendix E define the first-layer Galois group G_1, its generator gamma_1, and t = gamma_1 - 1 as the image of T. State the existing coefficient identity in the quotient F_p[G_1]/(t^3), identified with F_p[t]/(t^3). Its coefficients, sign and conclusion are unchanged.

The earlier three v0.2.1 fixes remain present. No theorem claim or grade, core evidence source, claim ledger, Lean source, or computational certificate is changed. Version labels, the PDF and verification metadata are updated. The previous tags and source folders remain preserved.

`review/EDITORIAL_PATCH_APPLIED.json` records the before/after source identity and the historical file mapping. The old patch bindings still refer to the v0.2.1 bytes, explicitly preserved under `review/history/v0.2.1/`; they are not relabelled as reviews of this revision. `tools/verify_patch_release.py` checks both that history and the current editorial bindings.

From the bundle root run:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
shasum -a 256 -c MANIFEST.sha256
```

The first two commands are bounded portable checks; the last checks the complete packaged file manifest, including the PDF. They do not repeat the large numerical certificates or the imported geometric and arithmetic proofs. The unchanged Lean core passed a fresh pinned replay in the preceding audit; this purely editorial revision does not require another rebuild of it.

The earlier recheck briefs and reports remain historical records of their named snapshots. The 671-record coverage supplement retains its separately graded scope. FIN, ORDER9 and Q36 remain open. No new computation or research branch is authorized by this revision.
