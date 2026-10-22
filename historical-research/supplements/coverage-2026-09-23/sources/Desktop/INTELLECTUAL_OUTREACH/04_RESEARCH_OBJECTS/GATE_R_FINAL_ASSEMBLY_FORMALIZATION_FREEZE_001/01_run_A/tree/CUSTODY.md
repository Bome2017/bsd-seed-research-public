# Custody

Every `.lean` file under `RequestProject/` except `GateR/Assembly.lean` is a
**frozen certified source**.  Its bytes are part of the acceptance criteria and
will be compared against the manifest on return.  Do not edit, reformat,
reorder, re-indent, add imports to, or "clean up" any of them — including
`RequestProject/Main.lean`.  If a frozen file appears to contain an error, report
it; do not repair it.

`MANIFEST.sha256` is the authority for this packet.  `DIGESTS.md` lists the same
digests in readable form and omits its own entry, because a document cannot state
its own digest.

Return the complete project tree plus your build and axiom output.  Do not prune
the frozen sources from the return.
