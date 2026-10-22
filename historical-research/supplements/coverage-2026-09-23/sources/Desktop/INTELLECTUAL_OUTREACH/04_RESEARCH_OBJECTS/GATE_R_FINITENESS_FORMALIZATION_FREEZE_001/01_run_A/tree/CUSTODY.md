# Custody

All 36 `.lean` files other than `RequestProject/GateRFinite/Finiteness.lean` are **frozen certified
sources**, and that includes `RequestProject/GateR/Assembly.lean`, which carries the five Gate-R
theorems as returned and independently re-verified.  Their bytes are part of the acceptance
criteria and will be compared against the manifest on return.  Do not edit, reformat, reorder,
re-indent or add imports to any of them.  If a frozen file appears to contain an error, report it;
do not repair it.

`MANIFEST.sha256` is the authority.  `DIGESTS.md` lists the same digests readably and omits its own
entry, because a document cannot state its own digest.

Return the complete project tree plus your build, type and axiom output, and your dependency list.
Do not prune the frozen sources from the return.

Two notes from previous returns in this programme, so they do not recur:

* If your wrapper preserves a copy of this input alongside your working tree, say clearly which is
  which.  A previous return shipped both, and the preserved input still carried its `sorry`s.
* If your wrapper adds files to the project — a summary, a report, an attribution banner — those
  files will not be in this manifest.  That is expected.  Do not rewrite the manifest, and do not
  claim that the job file is the only difference without checking.

## One disclosure about a frozen comment

`RequestProject/GateR/Assembly.lean` opens with a doc comment that says **"Replace every `sorry`
below."**  That comment was written for the previous job, whose targets are now proved; the run
that completed that module preserved the comment verbatim, and it is inside frozen bytes.

**There is no `sorry` in `GateR/Assembly.lean`.**  Both textual matches for the word in that file
are inside that comment.  With comments stripped the file has zero, and it elaborates with no
`sorry` warning.  The only `sorry` in this packet is the one in
`RequestProject/GateRFinite/Finiteness.lean`, which is your target.

Do not act on that stale comment and do not repair it.  As in the previous packet: a frozen comment
is not a specification.  `TASK.md` is.
