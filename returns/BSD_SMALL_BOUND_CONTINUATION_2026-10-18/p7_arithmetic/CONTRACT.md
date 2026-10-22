# Coefficient-seven actual arithmetic continuation

Pre-registered 2026-10-18 before field/norm computation.

Goal: on control 389a1, construct its actual degree-48 nonzero seven-torsion point field, authenticate global units and test the incidence norm in scalar character sigma_3 -> 3 mod7. The complete ordinary character unit dimension is four under the full-image hypotheses. A witnessed norm rank r would give a complete-unit kernel bound 4-r. No result about the class-supported part follows without independent class control. No seed Sha value or known Selmer dimension is an input.

Predictions: exact torsion field degree48; scalar3 has order6; unit-character rank4. Norm rank is deliberately NOT predicted from p5. Accept actual nonzero norm witnesses only after unitness is certified algebraically. Residue rank is a lower bound on actual norm rank, never a claim of equality. BNF completeness cannot be inferred from a successful unverified computation.

Budgets: each arithmetic process <=120 seconds; cumulative expensive arithmetic <=360 seconds. Persist raw point field before reduction, field before BNF, and BNF before any certification. No blind BNF retries. If BNF fails, retain exact arithmetic reached and stop this lane, rather than expanding resources or calling a boundary a theorem.

Endpoints FIN, ORDER9, Q36 are unchanged by this bounded control experiment unless a separately proved seed implication is completed (none is presumed).
