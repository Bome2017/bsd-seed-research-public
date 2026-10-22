# New deductions and their exact status

'Proved' below means a mathematical proof in the linked local report, using the explicitly named imports. It does not mean a Lean theorem, independent referee replay, or a claim of novelty.

| Result | Hypotheses and conclusion | Proof location | Circularity / formalization |
|---|---|---|---|
| T1 | Odd p, product of cyclic p-groups: explicit diagonal and mixed decomposition of I^2/I^3 | TWO_PRIME_SUPPORT_THEOREM.md, polynomial presentation | Finite algebra; FORMALIZABLE_NOW |
| T2-T3 | Ota norm relations and I^2 membership: best depth attained at a conductor with at most two factors | TWO_PRIME_SUPPORT_THEOREM.md | No FIN. Abstract support/depth implication FORMALIZABLE_NOW; arithmetic norm relation imported |
| H1-H3 | Fixed modular parametrization, L(E,1)=0, Manin p-unit: integral cycles and exact phi_{p,S}(z_E)=t(p,S) | HOMOLOGY_SOURCE_THEOREM.md | No FIN; topology/modularity inputs. Full construction not packaged for immediate Lean compilation |
| L1-L4 | Good non-anomalous p>=5, squarefree S prime to p, maximal p-extension: U_S is an integral group-ring isomorphism | LOCAL_REGULATOR_ISOMORPHISM.md | No FIN. Normal-basis/coefficient algebra is formalizable; full proof imports local duality and formal groups |
| O1 | Seed at ordinary p outside S0: h_p=0 iff primary Sha vanishes | ORDINARY_CONVERSE_GATE.md | Deduction from Kim, Castella-Sano and Ota; converse assumes vanishing only as the antecedent of the converse |
| U1 | Evaluated explicit cycle ideal UC iff A belongs to J_E | INTEGRAL_COMPARISON_ATTACK.md | Elementary ideal/valuation deduction once the arithmetic maps are given; FORMALIZABLE_NOW as an interface theorem |
| B certificate | Positive rational B, q=4B, finite primary groups with order bounded by v_p(B): B=9 and full BSD | COMMON_B_PIVOT.md | Retained parent deduction restated with all hypotheses; FORMALIZABLE_NOW conditional algebra |

## Exact unproved arithmetic statements

**UC:** for the explicitly defined Psi_{p,k}, one nonzero integer A annihilates R_k/image(Psi_{p,k}) for a suitable k at every p in P, and that image is nonzero. The maps exist; this bound does not.

**Excluded primary finiteness:** Sha[p^infinity] is finite at p=2243,4547,5843, unless an eventual global construction treats them directly. This is inherited from the chosen WC architecture, not a new top-level goal.

**Optional converse transfer:** at ordinary p with finite positive primary Sha, attain a nonzero two-prime Kurihara witness within Ota's cyclic auxiliary set, preferably preserving Kim's minimum valuation. This would settle the remaining equivalence bookkeeping; it does not prove UC.

Neither UC nor the common-B arithmetic/real comparisons has a proof available for formalization. Encoding either as an axiom, a structure field, or a theorem hypothesis preserves the gap.

## Logical ledger

    SOURCE_AND_SPECIALIZATION = CONSTRUCTED
    LOCAL_OTA_REGULATOR_INDEX = 1
    SUPPORT_AT_MOST_TWO = PROVED
    ORDINARY_PRIMITIVE_EQUIVALENCE = PROVED_RELATIVE_TO_NAMED_IMPORTS
    UC_UNIFORM_ARITHMETIC_BOUND = OPEN
    NONZERO_INTEGER_IN_J_E = NOT_CONSTRUCTED
    ORDINARY_POSITIVE_DEPTH_CONVERSE_TRANSFER = UNVERIFIED
    FIN = OPEN
    FORMULA = OPEN

Small group-ring and valuation examples were independently evaluated by verify_finite_algebra.py. They corroborate finite algebra only and are not evidence for the seed's arithmetic antecedent.
