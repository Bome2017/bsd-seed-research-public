# Run013: 62a1 prime-twist BSD-at-2 proof project

Freeze date: 2026-08-22 (America/Los_Angeles)

This directory is the theorem-bearing proof project for the frozen Run013
`62a1` target.  The target is frozen under the **public-source novelty
standard**.  A possible private or unpublished priority claim behind the
Zhai--Wan--BSTW attribution remains disclosed and unresolved.

The project is deliberately narrower than a full BSD program.  It must prove
the two oriented 2-isogeny Selmer identities, replay their finite local
certificate, and then assemble the already-qualified analytic and
odd-primary inputs.  It must not claim completion before hostile independent
review.

Aristotle is downstream.  The mathematical and qualification gates now pass,
but no Aristotle handoff is authorized until a separate user authorization.
The final manifest is generated only after the independent review and all
derived status/evidence closure.

## Authority boundary

```text
RUN013                    = ASSIGNED_BSD_PROGRAM
EXACT_TARGET              = FROZEN_PUBLIC_SOURCE_STANDARD
PRIVATE_PRIORITY_CAVEAT   = DISCLOSED_UNRESOLVED
FULL_BSD_ATTEMPT          = NO
TARGET_PROOF_ATTEMPT      = ACTIVE
ARISTOTLE_HANDOFF         = NOT_AUTHORIZED
```

## Proof architecture

1. `TARGET.md` fixes models, maps, Selmer orientation, prime family, and exact
   consequences.
2. `PROOF.md` is the proof ledger.  It distinguishes proved lemmas, finite
   replay, and open symbolic obligations.
3. `src/` contains one theorem-bearing note per local or global component.
4. `certificates/`, `checker/`, and `tests/` contain the deterministic replay
   layer.  Replay is not itself a proof of unbound symbolic assumptions.
5. `BSD_CHAIN.md` records only the implication chain after the Selmer theorem.
6. `evidence/` binds inherited source material by exact path and SHA-256.
7. `MANIFEST.sha256` is regenerated last and never treated as independent
   review.
