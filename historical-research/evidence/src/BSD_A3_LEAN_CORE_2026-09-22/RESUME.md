# RESUME — Lean replay of the A3 bridge's algebraic core (§§2–4)

Instruction (user, 2026-09-22): Lean replay FIRST, then freeze-addendum promotion of A3.
Scope: formalize ONLY the algebraic implications of SIGNED_MINIMAL_LAMBDA_BRIDGE.md §§2–4 with the four
source-checked arithmetic inputs as explicit hypotheses (exact control; exact specialization lengths; tau-equivariant
free presentation + base-layer kernel/cokernel eigenspace equality; rank E(Q)=2). Do NOT formalize BLV, Gross points,
the witness, or the M2 normalization.
Deliverables: A3Core.lean (no sorry), build log, axiom report; then additive freeze addendum
CONDITIONAL_FORWARD_BRIDGE_PROVED. If the build fails: report the first failed implication, do NOT promote.
Status: DONE. Lean core replay PASS (build6.log, REPORT.md). A3 promoted by additive addendum ~/BSD_TWIST_SHA_SUPPORT_2026-09-22/SUPERSINGULAR_LANE_FREEZE_ADDENDUM_2026-09-22.md. M2 nonvanishing OPEN at every prime.
