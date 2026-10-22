# What remains before a 2243 production run (2026-09-23)

This list is complete to the best of current knowledge. It corrects my earlier four-item summary, which omitted engineering items: checkpoint compaction, Linux/cloud validation, checkpoint persistence and fleet orchestration.

**Framing.**
* **The dollar figures are modeled scenarios, not quotes or ceilings.** The ≈ $2.2k central figure assumes AWS c7a spot at the listed price, cloud per-core speed f = 1, and spot capacity for about 1 280 cores over about 4 days. None of these is measured.
* **The 2243-scale test (R5) validated machinery on 47 selected units, not the coefficient range.** No coefficient has been computed.

## A. Mathematics

| item | status | what closes it |
|---|---|---|
| D2 (char(X_Gr) = T·char(X_cl), split) | **Discharged at source level**: Skinner 2016 §3.2 plus a written Selmer-object matching (`dependencies/D2_D5_RECONCILIATION.md`) | an independent read of the matching argument |
| D5 (nondegenerate split height) | **Necessary at the retained grade.** SW Theorem 6.1's multiplicative "iff" is not supported by its cited source: Jones 1989 proves only the forward direction, under Sha finite, and leaves α's quasi-isomorphism conditional | cheapest: an independent height computation (second code path; hours; seconds of CPU). Alternatives: a source lemma for α, or a grade decision to import SW 6.1 |
| D3 (period comparison at p ∣ N) | as at p = 3: "Skinner as published", internal SU provenance open | no change proposed |
| D1, D4, D6, D7 | verified or read (S1); D4 now also covers Sha finiteness | none |
| Outcome value | K ≢ 0 closes the 2243-primary obligation (given D1–D8). K ≡ 0 proves nothing | your decision |

## B. Evaluator and pipeline

| # | item | status | notes |
|---|---|---|---|
| 1 | Independent evaluator verdict | **in progress**: Codex (`BSD_2243_ACC_CODEX_CHECK_2026-09-23`) and a fresh-context reviewer (`independent_review/`) | the author's own 24/24 test suite is not independent |
| 2 | Linux build and cloud validation | **not exercised**; no container runtime is active locally | pilot P0–P4 |
| 3 | Checkpoint volume control | **designed, not implemented** | Per-worker checkpoints are 80.5 MB each. On 20 × 64 workers that is **≈ 103 GB per restart generation** uncompacted, against ≈ 1.6 GB with one aggregated checkpoint per process. (The S4 storage line of 77 GB assumed 96 workers; at fleet scale it is understated.) This is not a correctness issue; it affects storage and merge time |
| 4 | **Checkpoint persistence across spot interruptions** | **not designed; required for spot** | The pilot launcher sets DeleteOnTermination = true and terminate-on-interruption. In a production run an interruption would destroy that instance's checkpoints, and with them all its accumulated work. Needed: an upload of each checkpoint to durable storage with a hash check, or persistent volumes with a stop-instead-of-terminate policy. The spot scenarios in S4 silently assume this |
| 5 | Fleet orchestration | **not implemented**; only the single-instance pilot launcher exists | shard assignment (`ACC_SHARD=i/N`, `ACC_TAG`), relaunch with the same shard after an interruption, monitoring, collection of checkpoints, one final merge |
| 6 | Pre-produced segments | planned, not done | Segment 0 is needed by every process. Segments 1–2047 have several sub-units each (5.9 GB, ≈ 34 CPU-h, already inside the production total) and must be present wherever their sub-units run, or on every instance |
| 7 | Final merge and packaging | engine path validated at full length (R5-M) | Recommended: a second party re-merges from the collected checkpoints independently |

## C. Queued, not started

* **The exact algebraic compression attempt.** Rewrite the weighted sum for C_{2243,3} with Manin/Hecke relations: a collision check, an exact congruence, and a full pricing. Per your ordering it waits for the evaluator review. If it succeeds, it could change the coefficient range, and so every figure above.
* **5843 is held.**

## Order proposed

1. The evaluator verdicts (Codex and the fresh-context reviewer).
2. D5 by the cheapest route (an independent height computation), if you want it discharged rather than decided by grade.
3. Items 4–5, persistence and orchestration, before any fleet run. Item 3 alongside.
4. The capped pilot, which covers items 2 and 6 and measures f.
5. Only then, a production budget decision.
