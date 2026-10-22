# Sources, custody, and verification boundary

## Controlling file

The task is controlled by PRO_BRIEF_UNIFORM_STEP_2026-09-30_v2.md, copied unchanged as INPUT_BRIEF.md. Its SHA-256 is:

    5786a977dd509417bb3d731d6c1fdadbb894eabb8e1221ee34f40a5ca3a82dc5

The 09-29 brief is superseded. In particular, the level-p^k arithmetic lifts are not proved inputs; a finite 3-primary computation is admissible; p-dependent direct constructions are admissible; and the rational-scalar architecture is optional.

## Printed sources actually used for the new comparison

**THEOREM — BH.** Dominik Bullach and Matthew H. L. Honnor, On the refined 'Birch–Swinnerton-Dyer type' conjectures of Mazur and Tate, arXiv:2511.07203v1. Theorem 1.4(b) and Hypothesis 1.2 are on printed p.2; the period and full-element definition are on p.8; Proposition 2.4's norm relation is on p.9. Their hypotheses and the exact restricted use of the norm relation are stated in Attempt (i).

The supplied PDF was read along with its supplied native text. The arXiv PDF pages 1,7,8 (zero-based) were also opened as screenshots to verify the displayed hypotheses and formulas. The paper's proof is imported, not independently reconstructed. The source's finite-Sha discussion of the integral Selmer group is not inserted into its separate classical-Selmer Fitting conclusion.

**THEOREM — KN, used to check the retained stopping point.** Daniel Kriz and Asbjoern Christian Nordentoft, Horizontal p-adic L-functions, arXiv:2310.20678v3, Corollary 5.20, printed p.43. Its assumptions include an odd p, p-unit Manin constant, no rational p-torsion, and a supplied mod-p Kurihara unit witness of length r. Its valuation bound depends on that r; the primitive-character refinement also imposes r<=p-2. The supplied native text and the displayed arXiv PDF page 42 (zero-based) were checked. This result is not used to provide an independent bound on r_p.

## Retained, not re-audited

The seed model, rank, basis saturation, reduction types, component and period conventions, modular-symbol denominator bound, residual surjectivity, settled primary parts, numerical residue rows, and B.20/B.21 are retained exactly at the grades in v2. The prior independent review's Part B was read as context. The underlying Manin, saturation, prime-certificate, and descent artifacts were not replayed. CLW, Castella–Sano, and Kim are used only through the retained B.20/B.21 statements; their source applications were not freshly re-audited here.

The p>=5 lifting from the retained residual image to the p-adic SL_2 image is rederived in Attempt (i). The new minimum-depth comparison and quadratic projection calculation are written derivations, not printed theorems and not externally reviewed in this session. SELF_REPLAY.md is explicitly same-worker review.

## File verification

All 26 entries of the supplied BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/MANIFEST.sha256 were checked successfully by file hashing. This verifies the supplied packet against its own manifest; it does not authenticate the papers' proofs or the missing host-side arithmetic certificates. No fresh live binary-hash match is claimed for the arXiv web responses.

The selected supplied-source SHA-256 values are:

    BH_2511.07203v1.pdf
    d3355b216eff780f070df45778d161d8636b4acc43f73b8c7186b1c037f52481

    Kriz_Nordentoft_2310.20678v3.pdf
    327b7e0e0d4e24fe2f2a101de3528176b2e0345cc0e9a842b98374f718a93edf

SOURCE_CUSTODY.json contains the manifest checks and source locators. The source PDFs are not duplicated in this return archive; they remain in the supplied synthesis archive.

## Runtime boundary

The work directory is /home/oai/BSD_UNIFORM_DEPTH_V2_RETURN_2026-09-30 in the current session container. A copy is supplied under /mnt/data for downloading. Neither location is the user's host home directory. NOTES.md, RESUME.md and STATE.json were initialized before any attempt file was written.

The requested gp path under /home/oai/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp does not exist in this container. No alternative mathematical runtime was used. In particular no supplied arithmetic script, prime search, modular-symbol calculation, Selmer computation, or experimental validation of the new identities was run. Python was used solely for text/file handling, JSON, hashing, and packaging. One worker was used, with no subagents, repository operations, pushes, or paid compute.

Web use was limited to checking the quoted BH and KN statements at the specified revisions. No broad literature search or current-state survey was conducted. No claim of literature novelty or universal nonexistence is made.
