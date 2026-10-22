# Supersingular signed comparison — active calculation

User instruction: continue working toward full BSD, preserve checkpoints, and use failed calculations as constraints rather than as a reason to stop the project. No subagents. No edits to sealed inputs or the frozen master.

Work here is a mathematical working record, not a new master map. Read STATE.json and the end of CHECKPOINTS.jsonl, then DERIVATION.md when present.

Latest checkpoint: SIGNED_MINIMAL_LAMBDA_BRIDGE.md supplies a written proof of the supersingular forward implication, conditional on BLV's theorems and retained seed hypotheses. Read that file and SELF_CHECK.md before the earlier DERIVATION.md, which records the weaker first-character calculation. The exact specialization equality removes finite Lambda errors; the equivariant residual presentation balances the tau ranks; a minimal quadratic signed coefficient then leaves no seed Sha in the plus quotient. Independent review is pending. No signed moment has been evaluated, no primary component has been newly settled, and FIN/ORDER9/Q36 remain open.

Seed: E: y^2 = x^3 - 22735 x^2 + 106272484 x, K = Q(sqrt(-7)). Retained ranks: (r+,r-)=(2,0). Ordinary c2 witness remains open. The latest catch-up record explicitly identifies the supersingular signed case A3 as the next uncovered comparison.

Endpoint: FIN/order control at supersingular primes; no direct real FORMULA claim. Intended chain: an explicitly normalized signed arithmetic witness -> a bound on the classical Selmer quotient -> vanishing of the seed's p-primary Sha. The second arrow must be proved; an ordinary derived-height theorem cannot be transferred without checking its hypotheses.

First calculation: use BLV v2 sections 4.3, 5.1, 5.3–5.4 and Theorem A to determine the minus first-layer element, augmentation control, and the precise arithmetic consequence of a minimal signed coefficient. Minus is non-exceptional for both split and inert supersingular primes. Do not assume that its order is the ordinary square-root order two.

Admission: this addresses a separate infinite set excluded by the ordinary theorem. Signed local points replace the unavailable ordinary unit root. Success in merely constructing a signed series is not a Sha bound; record the exact achieved implication.

Source: /Users/bsm/run013-bsd-scout-2026-08-22/_evidence/txt/2306.17784.txt and https://arxiv.org/html/2306.17784v2 .

Do not inherit two transcription errors in recent secondary summaries: c2bar = b_(p-3)/2, not -b_(p-3); the BD finite group is Sha/Div(Sha), not Div(Sha). Nonzero derived regulators are not necessarily units.
