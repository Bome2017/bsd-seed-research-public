# Seed combination ledger

Date: 2026-10-07. Lab baseline: 56a799e002c80d6928b90f081c99b56935d202b5.
This is a dependency calculation from the sources and project files listed in
INPUT_BINDINGS.json. It is not an exhaustive reading of the project or literature.

The objective is cofinite vanishing of Sha(E/Q)[p], followed separately by
the exceptional primary FIN obligations, ORDER9 and Q36.

## BKS: the arrows must remain separate

| Arrow | Actual input/test | Seed substitution and verdict |
|---|---|---|
| Two point classes → positive rank of global H² | Kummer inclusion and global Euler characteristic h¹−h²=1 | h²≥1 without deleting T_pSha. **Established under retained basis and standard cohomology.** |
| H² rank lower bound → weak cyclotomic Kato order | Actual integral smoothed source; height-one Kato inequality and derived control | z_∞∈U M. **Written deduction in WEAK_ORDER_PROOF.md; independent review pending.** |
| Weak order → nonzero derivative | Requires order exactly one, not at least one | **Open.** The new deduction constructs a derivative that may be zero. |
| Derivative → Mordell–Weil Bockstein expression | Source-matched analytic comparison and the correct cohomology target | **Open.** Do not replace H¹ by MW using the finiteness being sought. |
| Algebraic formula → analytic formula | BKS II Lemma 3.5 identifies their constants under BSD | **Unavailable as a proof of FIN.** Algebraic constant contains #Sha. |
| Cyclotomic analytic formula → tame degree-two comparison | Requires a finiteness-free determinant comparison and integral Euler/period tracking | **Not established.** The e_p factor has valuation −1. |
| Exact tame comparison with fixed rational α → cofinite vanishing | G2 detecting prime, α nonzero, integrality, Ota implication | **Valid conditional endpoint.** TAME_COMPARISON.md gives every scalar. |
| q_E regarded as a fixed rational α | Rationality plus nonzero q_E | **Rationality open.** The retained positive enclosure gives nonzero real q_E only. |
| Finite tame observations → rational α | Needs independent cross-prime compatibility or bounded-height theorem | **Not established.** Matching residues of 288 are evidence, not this theorem. |
| Fixed-p W → same nonzero scalar for all p | Needs cross-prime input | **Not established.** W includes the possibility of a zero scalar. |

## Exact versions and source scope

Use the published 2024 BKS I for its numbering. Its Hypothesis 2.2 includes
primary finiteness; §4 retains that assumption. Theorem 1.3 also requires
finiteness over the extension. Proposition 4.4 proves weak cyclotomic
divisibility. Its proof, rather than its printed statement, is adapted here.
No stronger finite-extension order theorem is imported without its assumptions.

BKS II 2103.11535v1 separates analytic Conjecture 3.1 from algebraic
Conjecture 3.4; its §2.1 assumes whole-Sha finiteness. The latter constant
contains #Sha. Lemma 3.5 invokes BSD. Theorem 4.1 uses the algebraic conjecture.
These labels cannot be interchanged.

The retained project proof of W is a specific weaker, p-primary adaptation
of part of that determinant argument. Its existence is not a license to
remove every finiteness assumption in the papers.

## Apply the seed's actual local facts

| BKS II Hypothesis 2.2 item / normalization | Calculation | Disposition |
|---|---|---|
| Tame squarefree conductor | F_ℓ has conductor ℓ | Met at a G2 prime. |
| Auxiliary primes of good reduction | ℓ∤pN | Met by G2. |
| p∤6N·tors·Tam | tors=2, Tam=16; exclude bad coefficient primes | Met on S_* complement. |
| p∤#E(F_p) | 2-torsion, Hasse, #E(F_5)=8 | Met at every good p≥5. No ordinary restriction. |
| p∤bad nonsingular counts | 2242=2·19·59; 5844=12·487 | Explains 19,59,487 exclusions. |
| p∤#E(F_ℓ) | Frob_ℓ=−I gives #E(F_ℓ)≡4 | Met. Frob unipotent with a_ℓ≡2 is a DIFFERENT auxiliary set. |
| Full residual image | Retained seed theorem | Imported at its existing grade, not recomputed here. |
| Truncation at coefficient prime | e_p=#E(F_p)/p | Valuation −1; never a p-unit. S_ℓ and Σ_ℓ differ. |
| Real period | Production least-real period versus BKS total real period | Factor 1/2 retained in the tame comparison. |
| Taylor coefficient | Rank two | L*(E,1)=L''(E,1)/2, not L''. |

Passing these local rows does not discharge the analytic conjecture or the
global finiteness assumptions of the printed comparison theorem.

## Other corrected routes

These rows preserve the two October 7 independent reviews; the papers for
these rows were not all re-read in this pass.

| Route | Already resolved | Actual remaining arithmetic; scoped status |
|---|---|---|
| Howard specialization factor | Augmentation equals (p+1)²−a_p² in the inert case and (p+1−a_p)² in the split case; seed a_p≠±1 mod p | These are units on the source domain. They do not identify DLRV, Howard and classical Zhang systems. |
| Direct nonexceptional DLRV augmentation | Its claimed corank-one specialization conflicts with known point directions | That direct application is excluded. Singular/derived specialization is **open**, requiring actual source classes, comparison and error terms. |
| A1→A2 | C1–C4 not supplied; auxiliary-prime sets differ | The asserted identification stays withdrawn. No false collision rule. |
| Heegner ν_p | Retained criterion on its nonzero residual-system/sign domain | Uniform one-prime nonvanishing remains unproved. Do not extend ordinary theorems to supersingular primes by notation. |
| −23 twist | Existing rank-one certificate restored; core subsequently recovered and recombined | Retain certified project input, distinct from an independently rerun finite sum. It does not provide seed cofinite vanishing. |
| A3 leading term | A nonunit regulator does not kill a comparison of correlated valuations | Source hypotheses and an independent bound on v_p(L_p*)−v_p(R_p/p²)−v_p(local terms) remain unproved. |
| Receiver / order-three excess | Exact or domain-qualified identifications with Sha[p] | No independent upper control follows from renaming the quotient. |
| Broad global-support B | Updated package prepared | Separate unsubmitted experiment; this ledger is not evidence that B will succeed or fail. |

## A usable next mathematical question

There are two different possible continuations, with different payoffs:

1. **Pointwise primary finiteness:** prove the actually constructed first
   cyclotomic derivative nonzero in rational cohomology without using Sha
   finiteness to identify the target. The conditional corollary in
   WEAK_ORDER_PROOF.md then gives primary finiteness at that p. Merely doing
   this separately at more primes is not the requested cofinite vanishing theorem.
2. **Uniform vanishing:** prove (T1) or a sufficient unit-valued version for
   a fixed independently constructed rational α and G2-detecting tame primes.
   The exact deduction to the seed endpoint is (T1)→(T2)→G2→Ota. The special
   α=q_E version additionally needs rationality. A wholly different independent
   uniform estimate remains admissible.

The finite-order source proof supplies a derivative, not the independent
arithmetic control required by either continuation. This return has not
proved either nonvanishing statement.
