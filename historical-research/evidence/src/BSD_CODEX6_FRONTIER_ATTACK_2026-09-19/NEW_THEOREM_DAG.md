# Corrected theorem DAG

The only top-level nodes are RANK, FIN, FORMULA. “NEW_LEMMA_REQUIRED” identifies an unproved statement, not a claim that it is small or tractable. “MAJOR_NEW_THEORY_REQUIRED” below describes named conjectural route packages, not a theorem that every solution must develop such theory. Executable computations may still be semi-decisions.

## Top level

| Node | Status | Exact boundary |
|---|---|---|
| RANK | PROVED / PROVED_COMPUTER_ASSISTED | Algebraic rank two and retained exact MW data; rigorous Arb analytic rank two |
| FIN | UNKNOWN | Finite-support theorem and remaining finite-primary inputs unproved |
| FORMULA | UNKNOWN | q=4 #Sha; exact arithmeticity of q unproved |

## FIN branch: selected weaker route

| ID | Node | Classification | Dependencies |
|---|---|---|---|
| F0 | Exact curve, basis, index, residual-image and Ota hypotheses | PROVED, imported | Retained seed theorem, all-odd image result; Hasse and 2-torsion |
| F2 | Sha[2^inf]=0 | PROVED, imported | Retained theorem |
| F3 | Sha[3^inf]=(Z/3)^2 | PROVED_COMPUTER_ASSISTED, imported | Skinner as printed, R1/R2 retained |
| F5 | Sha[5^inf]=0 | PROVED_COMPUTER_ASSISTED, imported | Sealed September 19 upgrade |
| FO | Ota nonzero leading term => local FIN; primitive => vanishing | PROVED | Ota 5.17/6.4 and cofiniteness; stated hypotheses |
| FW | J_E != 0 | NEW_LEMMA_REQUIRED | Actual uniform integral descent/comparison; no construction obtained |
| FA | Finiteness at 2243 and 5843 | UNKNOWN | Candidate local routes with unexecuted gates and high cost |
| FB | Finiteness at 4547 | UNKNOWN | Conventional proposed branch ROUTE_BLOCKED; other routes not disproved |
| FC | FW and F2/F3/F5/FA/FB => FIN | PROVED conditional reduction | WC; finite support and primary assembly |

The actual missing arrow is **arithmetic source -> FW**. A finite list of successful primes cannot prove FW. FW handles the good-prime tail and the finitely many good-prime nonunits; FA/FB are still required by this selected architecture.

## FIN alternatives and attempted shortcuts

| Node | Classification | Result |
|---|---|---|
| LINE common rational scalar | NEW_LEMMA_REQUIRED | Sufficient but stronger than FW; LINE=>FW proved with retained core-pair inputs |
| Direct rationalization of finite augmentation quotients | ROUTE_BLOCKED | Exact exponent-annihilation lemma |
| Profinite perfect determinant complex => finite support | ROUTE_BLOCKED | Explicit local-length-two countermodel |
| Finite free Z-object with primitive arithmetic realization | CONDITIONAL | Proved content reduction; constructing the realization remains UNKNOWN |
| Post-local-FIN BKS determinant realization | PROVED under hypotheses | Cannot establish its own local-FIN hypothesis; no cross-prime descent supplied |
| New uniform rank-two Euler/reciprocity package | MAJOR_NEW_THEORY_REQUIRED for that route | No instantiated construction or executable proof identified |
| Fixed ordinary-prime or supersingular certificate | EXECUTABLE, bounded task | May yield inconclusive bit; not a uniform theorem |
| Current H9 specialization | ROUTE_BLOCKED | Precise route-specific coefficient/specialization obstructions |
| Exterior contraction as a different type of source | PROVED algebraically | Arithmetic identification/content remains UNKNOWN |

## FORMULA branch

| ID | Node | Classification | Dependencies |
|---|---|---|---|
| Q0 | q=L''/(2 Omega Reg), Tam/torsion multiplier 4 | PROVED definition/normalization | Fixed model; retained factors |
| Q1 | Rigorous L''/2 in [35.929604,35.941023] | PROVED_COMPUTER_ASSISTED, imported | Existing Arb stream |
| Q2 | Rigorous Omega and Reg | PROVED_COMPUTER_ASSISTED | New exact-tail Decimal certificate; retained full basis |
| Q3 | 35.99427<q<36.00573 | PROVED_COMPUTER_ASSISTED | Q1+Q2 |
| Q4 | q in Q | NEW_LEMMA_REQUIRED | First unproved arrow on the minimum route |
| Q5 | den(q)<=174, or another quantitative arithmeticity certificate | NEW_LEMMA_REQUIRED | Not supplied by local lattice equality or one p-adic digit |
| Q6 | Q3+Q4+Q5 => q=36 | PROVED | Integer-spacing lemma |
| Q7 | Under FIN, #Sha=9 | UNKNOWN | Known primary parts do not exclude extra squares |
| Q8 | FIN+Q7+Q6 => FORMULA | PROVED conditional reduction | Fixed formula multiplier |
| Q9 | Rational determinant line exists under arithmetic hypotheses | PROVED | Does not imply analytic-vector rationality |
| Q10 | GPR_an / order-two archimedean regulator comparison | MAJOR_NEW_THEORY_REQUIRED for named route | No proof identified; stronger language than Q4+Q5 |
| Q11 | Bounded algebraicity instead of rationality | CONDITIONAL / UNKNOWN antecedent | Polynomial-value lemma proved; no algebraicity/bound for q |

Q7 is an arithmetic subnode needed to specialize FORMULA to q=36. It is **not** a fourth top-level goal. A full FORMULA proof could determine the order in combination with FIN and Q3 instead of presupposing Q7.

## A common-object route

| Node | Classification |
|---|---|
| Construct nonzero global integral Z_E before FIN | UNKNOWN |
| Uniform one-sided arithmetic bounds, including exceptions | NEW_LEMMA_REQUIRED |
| Real comparison q=4B for its positive rational coefficient B | NEW_LEMMA_REQUIRED |
| These bounds + Q3 + retained 3-part => full BSD | PROVED conditional reduction |

There is no evidence that these missing inputs form one tractable compatibility theorem. The DAG is finite as a description; its open arithmetic arrows do not have executable proof routes. Final classification: BSD_FRONTIER_UNKNOWN.
