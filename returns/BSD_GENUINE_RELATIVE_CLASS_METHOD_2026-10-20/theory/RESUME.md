Read REPORT.md and PRESENTATION_BOUND.md. The exact upper-bound interface
is d-r_U+m-r_C+q. No full relation saturation or unit basis is needed;
generation modulo p (q=0), or an independent bound on q, is indispensable.

RELATIVE_ALGORITHM.md gives the actual pseudo-ideal invariant and content
operation being implemented by the arithmetic lane. Do not relabel an
unclosed residual ideal as a relation. Do not repeat full BNF attempts.

The unconditional BDDF Corollary 5.2 was actually tested at T=419776 and
fails there, with an exact rational failure certificate. This is not a
nongeneration result. Run `python3 check_bddf.py` from this folder to replay
against sibling review inputs; compare output with BDDF_RESULT.json.

No smaller relative-discriminant-only bound was supplied by the inspected
source. The ordinary class contribution and omitted-generator defect remain
unbounded in this theory lane. FIN, ORDER9, Q36 are unchanged.
