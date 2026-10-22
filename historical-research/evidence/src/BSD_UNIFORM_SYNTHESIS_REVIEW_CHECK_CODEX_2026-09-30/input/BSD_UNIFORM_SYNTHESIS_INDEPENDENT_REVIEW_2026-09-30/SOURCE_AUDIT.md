# Source and custody audit

## Files actually checked

The input archive was extracted without modifying the archive. All 26 entries of its `MANIFEST.sha256` matched their supplied hashes. The detailed check, including the input archive SHA-256, is in `INPUT_INTEGRITY.json`. Hash agreement is a custody check, not a mathematical verification.

Source PDFs and text are in the supplied input archive, under `sources/`. Their exact supplied URLs and hashes are copied in `SOURCE_BINDINGS.json`. The review uses the following identifiers:

| ID | Source version | Decisive anchors |
|---|---|---|
| S1 | Castella–Liu–Wan, author PDF `CLW2.pdf`, dated September 21, 2026, 45 pages | Theorem A pp.2–3 with the standing hypothesis; §1.5 p.7; §2.1 p.8; §2.4.2 and Lemma 2.10 p.13; Remark 2.20 p.16; Theorems 5.1 and 5.3 pp.35–37; §5.5 pp.39–40; (5.18) p.40; (5.21)–(5.22) p.41; period comparison pp.41–42 |
| S2 | Castella–Liu–Wan, arXiv 2608.29470v1, 44 pages | Theorem A p.3 and §1.5(3) p.7; used only to verify the old squarefree condition |
| S3 | Castella–Sano, arXiv 2601.14504v1, PDF internally dated January 22, 2026 | Definitions and parity pp.1–3; Theorem A, Corollary A and Theorem B p.3; Kato normalization p.6; determinant statement and Proposition 2.2.3 p.9 |
| S4 | Chan-Ho Kim, arXiv 2203.12159v6 | Auxiliary definitions p.4; modular-symbol normalization p.6; Theorem 1.8 p.7; parity corollary p.9 |
| S5 | Bullach–Honnor, arXiv 2511.07203v1 | Hypothesis 1.2 and Theorem 1.4(b) p.2; classical-Selmer exact sequence p.2; periods and Definition 2.2 p.8; norm/interpolation conventions p.9 |

The other source versions supplied in the archive were not needed to establish Parts A and B. No claim to a new Kriz–Nordentoft source screen is made.

## Public verification and a delivery discrepancy

Public verification was restricted to the quoted theorem sources: the author CLW PDF and author page, the older CLW arXiv PDF, and the arXiv HTML pages for Castella–Sano, Kim and Bullach–Honnor. No broad literature search was conducted.

The browser's parsed author-PDF text reported 45 pages, the September 21 date, and the revised Theorem A with (ram) and no squarefree hypothesis. The author page also linked the CLW work. However, its screenshot operation returned an image showing the old squarefree statement even for that author-PDF reference. The old arXiv screenshot showed the same statement. This is a source-delivery inconsistency; its cause was not established.

To avoid merging versions, the decisive visual check used a direct rendering of the supplied, hash-pinned `CLW2.pdf`. Its printed p.3 visibly contains (ram) and the revised theorem. The resulting image is included in `source_checks/CLW2_p3.png`. The local file is 684246 bytes, with SHA-256

    0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98

A separate binary download attempt failed, including a runtime attempt that reported DNS failure. A cache-disambiguated browser URL also failed. Accordingly this review does NOT assert a separately downloaded byte-for-byte match to the live author-hosted PDF. Its primary object is the version supplied in the user archive, corroborated by the browser's parsed theorem text. This limitation is not a newly discovered failing hypothesis of that theorem.

The pinned PDFs were natively text-extracted/read, with no OCR. Decisive local page images actually inspected include CLW pp.3 and 41, Castella–Sano p.9, Kim p.7, and BH pp.2 and 8. Additional rendered pages are included for inspection. `source_checks/anchors.json` supplies exact locations in the packet's extracted text for the principal statements.

## Retained facts and unavailable dependencies

`LOCAL_BINDINGS.json` lists 13 absolute paths on the user's machine. Those raw records were not supplied in this archive and are not available at those paths in this environment. The prior all-prime image proof, saturation certificates, Manin calculation, and production prime-certificate corpus were not replayed. In particular, the bound c_phi | 512 is retained, not independently certified by this review.

The retained seed facts used are: the specified model and conductor; rank two and no odd rational torsion; root number +1; residual surjectivity; split I_1 at 2243; the stated reduction at the other bad primes; Tam=16; and the good-prime Manin-unit assertion. No contradictory older conversation memory was used to replace them. No historical scalar normalization was silently imported into the new argument.

## Computation and custody boundary

No PARI, Sage, Magma, prime search, arithmetic certificate regeneration, production code, paid job, subagent, repository command, push, correspondence, or canonical-state update was run. The packet's `check_arithmetic.py` was not executed. The only runtime work was archive/file handling, hashes, native PDF reading/rendering, and creation/validation of this review's deliverables. New files are in the review output directory and its companion archive; the user's original uploaded artifacts were not edited.

The result is an application audit at the printed-source and retained-input grades, not an end-to-end verification of every foundational theorem or every arithmetic certificate.
