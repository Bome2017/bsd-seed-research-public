# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error)

Base-curve Tamagawa data transcribed into a row about the twist. `BSD_CHAIN.md` §4 is
authoritative: the twist has nonsplit `I₄` at 2, split `I₁` at 31. Product `(2,1,2)`
unaffected.

## E2 — wrapper metadata defects, both modes now recurrent

Run A: **partial wrapper**, 19 of 31 files — no manifest, no receipts, no references. Second
occurrence of this mode (first: P03a Run A).
Run B: **stale metadata**, 29/31, failing exactly the two files it changed. Eighth occurrence.

Neither is a proof defect: both rebuild clean here with zero `sorry` and standard axioms, and
all twelve inherited Lean sources came back byte-identical in both.

> **Never certify an Aristotle return from its own receipts.** Regenerate build, axiom,
> source-scan, manifest and archive evidence externally; count declarations from source.

## E3 — Claude's declaration-counting regex could match prose (new, found and fixed here)

A line-anchored regex for `^(theorem|lemma|def|abbrev) NAME` also matches the word `theorem`
where it begins a sentence **inside a block comment**. The P03d handoff's own doc comment
contains the line

    theorem therefore says exactly what it looks like it says, in the group law that is …

which a naive count reads as a declaration named `therefore`, inflating every count by one.

**Assessment.** Cosmetic, and caught before it entered any frozen claim: the first count in
this session's working notes showed 7 and 5 declarations; the correct comment-stripped counts
are 6 and 4, i.e. 5 and 3 added. All counts in this object and in
`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` are comment-stripped.

**Scope check.** Earlier freezes used the naive regex. It inflates a count only when a doc
comment contains a line *beginning* with `theorem`/`lemma`/`def`/`abbrev` followed by an
identifier-shaped word. That pattern was introduced by the P03d handoff's prose and does not
occur in the P01, P03a, P03b or P03c sources — their counts are unaffected. Recorded rather
than silently corrected.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3. This
object's root manifest excludes only itself, so all nested manifests are covered.

## Not an erratum: P03d's replication is the strong kind

Unlike P03c, the two P03d runs took materially different routes with zero shared helper names.
`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` measures it and calibrates against every earlier
stage. The P03c freeze's standing question — supply the route and get confirmation, or
withhold it and get a cross-check — was answered here by withholding the strategy for the
ordinary case, and it worked.
