# Standing research admission gate

**Authority:** the user's supplied comparison and instruction to perform it, reconciled with the current source record on 2026-09-19. This document supersedes earlier *strategic admission wording* where it is more restrictive or logically incorrect. It does not supersede an earlier proof or expand the scope of a no-go theorem. The fixed obligations remain:

\[
\mathrm{FULL\ BSD}(E)=\mathrm{RANK}\wedge\mathrm{FIN}\wedge\mathrm{FORMULA}.
\]

RANK retains its computer-assisted status. FIN and FORMULA remain open. The complete seed and import qualifications are in the [master proved state](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/SEED_PROVED_STATE.md).

## 1. Fixed endpoints and usable endgames

For this seed put

\[
G=\Sha(E/\mathbb Q),\qquad q=\frac{L''(E,1)}{2\Omega\operatorname{Reg}},
\qquad |q-36|<\frac{573}{100000}.
\]

FIN means that G is finite. FORMULA, with finiteness, is `q = 4 #G`. The retained 2-, 3- and 5-primary inputs give orders 1, 9 and 1 respectively; the 3-primary input carries **R1 and R2**. Finite Sha has square order by the retained Cassels–Tate input. Therefore FIN alone permits `#G = 9 t^2`, with `gcd(t,30)=1`.

| Required output | Sufficient certificate | What remains after success |
|---|---|---|
| FIN and order nine | G finite and `#G < 441`, or `#G[n] < 441` for every positive n | The q-side of FORMULA; carried provenance obligations |
| q = 36 | q rational with reduced denominator at most 174, or quantitative algebraicity satisfying the retained separation bound | FIN and order nine; carried provenance obligations |
| FIN and FORMULA together | An independently obtained positive rational B, `q=4B`, and for every p a finite `G[p^infinity]` with `v_p(#G[p^infinity]) <= v_p(B)` | Carried provenance obligations and verification of every imported hypothesis |

These implications, their converses under the retained inputs, and their sharp scope are proved in [EXACT_ENDGAMES.md](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/EXACT_ENDGAMES.md). No sufficient certificate in the table has been established for the seed. “Less exact output” does not mean “easier proof.” The 441 and 174 endgames are assembly facts, not new global arithmetic information.

The first question for a proposal is:

> What independently accessible information does this construction give about the missing global Sha defect or the normalized real leading term, and what tool can establish it under hypotheses already available for the seed?

Do not make a global Sha condition mandatory for a route explicitly attacking only q. Its card must say that FIN and order nine remain.

## 2. Candidate card required before substantial work

1. **Endpoint and scope.** FIN, the q-side of FORMULA, full FORMULA with its Sha input, both, or neither. Give the exact seed, normalizations, quantifiers and allowed exceptional set.
2. **Complete implication chain.** Write every arrow back to the fixed endpoint and what remains afterward. Label each arrow PROVED, IMPORTED WITH HYPOTHESES, OPEN, or DISPROVED IN SPECIFIED SCOPE. Object construction alone closes no interface.
3. **First unproved arrow.** State it before developing the object. Include all nonvanishing, finiteness, integrality, exponent, comparison and compatibility assumptions.
4. **Converse and difficulty audit.** Attempt the reverse implication under the same inputs. Record PROVED EQUIVALENCE, PROVED SEPARATION, or UNKNOWN, with the attempted argument. Exhibit the actual reason a new method can help. “No converse found” is not proof of separation.
5. **Independent new information.** Identify a theorem, identity, estimate or structure whose proof does not import the target or its equivalent antecedent. Check its hypotheses for this seed. For an invented statement, write the first independent proof steps and the specific bottleneck. A named framework, precision increase or promised comparison is not evidence.
6. **Obstruction compatibility.** Apply the [constraint register](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/CONSTRAINT_REGISTER.md), including its scope boundaries. State which hypothesis of an applicable obstruction is absent, or supply a genuinely new proved mechanism. Renaming an object “mixed,” “derived,” “integral” or “global” is insufficient.
7. **Kill condition and resource cap.** Give a falsifiable failure condition, a finite deliverable, maximum model/compute effort, and the exact decision after the result. No automatic successor branch after failure.

Equivalence does not forbid research. A change of formulation can reveal an independently applicable tool. It must earn resources through that tool, not through a claimed reduction in difficulty inferred from notation.

## 3. Four immediate kill questions

1. **Does it see the missing quotient?** For FIN, what controls `Sel_n(E)/(E(Q)/nE(Q)) = G[n]`, rather than only the known Mordell–Weil image? For q, what controls the normalized scalar rather than merely displaying an analytic period?
2. **Does it cover the necessary quantifiers?** For FIN, cover all prime regimes and arbitrarily deep primary torsion, or prove a whole-group bound that covers them at once. Ordinary-only control leaves an infinite supersingular set. A q-only route must quantify its denominator or conjugate bounds instead and declare the missing Sha input.
3. **Where is the proved output comparison?** Give the exact theorem converting the constructed output into a finite arithmetic bound or quantitatively controlled q. Distinguish a bound on a whole map from the content of the distinguished image; distinguish a determinant from a bound on the Sha quotient.
4. **Is the proof independent of the endpoint?** Draw the dependencies of the first open arrow. Remove FIN, FORMULA and equivalent unsupported assumptions: which available hypotheses and new argument remain? A converse is recorded, not treated as an automatic rejection. Never use “assume the endpoint false” as an independence test for a sufficient theorem.

Failure of a universal statement's quantifiers, an applicable no-go result, or a circular proof stops that mechanism. Lack of a demonstrated tool admits at most a bounded scout.

## 4. Allowed architectures and their missing arrows

These are admissible logical designs, not ranked predictions, proven reductions, or an exhaustive classification.

| Architecture | Required independent interfaces | First open arithmetic content |
|---|---|---|
| Separate arithmetic and analytic arguments | A global Sha bound or complete prime coverage; separately a controlled arithmeticity theorem for q | Both bounds/comparisons remain open |
| Coupled scalar B | An independent construction; `q=4B`; finite-primary valuation upper bounds for every p | Construction with both interfaces, not the assignment `B=q/4` or `B=#G` |
| Global integral object Z | Proved control of actual Sha support and primary sizes; archimedean comparison with the normalized leading term | Integral content alone supplies neither map |
| Direct uniform Selmer/torsor bound | A bound on the actual quotient `G[n]` for all n, with a constant below 441 | A uniform arithmetic estimate, not a per-prime dimension calculation |

A direct global bound does not have to exhibit a point Z, a scalar B, or an explicit prime partition. A support theorem `G[p] != 0 => p | C_E` with an independent nonzero integer `C_E` is also admissible, but it still requires control of entire primary groups at the finitely many divisors. Support alone does not exclude a divisible primary part.

For a prime-partition route, retain all four coverage requirements from the earlier Albertson analogy: an independently justified exhaustive partition; a theorem uniform on each infinite part; complete certificates for the finite residue; and assembly. An explicit cutoff is needed to enumerate a claimed computational residue. Supersingular primes cannot all be assigned to that finite residue. The analogy supplies no BSD theorem.

## 5. Admission, experiments and completion labels

**REJECTED BY OBSTRUCTION:** identify the exact assertion and applicable theorem; update the register and stop that class.

**EDUCATED GUESS / SCOUT ONLY:** the endpoint chain is meaningful, but an easier independent method has not been exhibited. Before starting, specify one bounded scout: data, normalization, prediction, falsifier, cost cap and deliverable. A successful finite test is evidence for further consideration, not a universal theorem.

**ELIGIBLE FOR SUBSTANTIAL WORK:** concrete new input and seed-applicable hypotheses justify an identified next proof step; compatibility and dependency checks pass. This is a resource judgment, not a feasibility guarantee.

For a per-prime experiment, name the proposed uniform mechanism and the observation that could refute it. Explain what a pass could and could not establish. Include the real cost of the selected pipeline: the audited Criterion SS estimates are approximately 270 CPU-hours at p=23 and 460 at p=29, about 500 shared. A cheaper surrogate requires its own specification and cannot inherit certified status. This freeze authorizes no such run.

After work, classify the result as **closed required arrow**, **strict difficulty reduction with evidence**, **no-go compression with scope**, or **supporting work only**. A precise missing arrow, a new sufficient criterion, more prime certificates, or a formal proof of conditional assembly alone cannot be reported as a new solution of the arithmetic endpoint.

## 6. Continuation boundary

The DM branch is closed at its proved trace/universal-lifting failure. The modular-unit Mellin branch remains stopped at its exact-correction obstruction. The paused invention scout is not resumed and its unsealed observations are not promoted to a theorem. LINE/WC retain their valid conditional implications and unproved antecedents; they are not declared false.

The p=3 R1 and R2 records must travel with every conclusion using its order-nine input. They are not assumed to be cheap citation repairs. A1/A2 are existing conditional formal results; do not replay their finite algebra absent a defect. This governance freeze closes no FIN or FORMULA arrow and schedules no work.
