# Producer predictions and stopping conditions

Sealed before arithmetic. Fixed inputs: seed model, coefficient3, cached15-generator S-Kummer source, old NF/BNF data, and the actual two point/two cubic representatives and exact unit from the preceding experiment. No L-value or Sha size is an input. The cached source may be GRH-complete; no unconditional completeness is inferred.

We compare constraints separately on: fullsource; valuation-zero source; unit subspace; their tau=-1 or norm-one part. The rows are (a) valuations and ideal classes; (b) anti-involution/norm; (c) coefficient additivity among torsion points; (d) all named local Kummer conditions. Report every independent intersection and ordering, not just one chosen filtration.

Competing outcomes: NORM_REJECTS_UNITS if some units fail tau+1; ADDITIVITY_REJECTS_NORM_UNITS if it removes additional norm-admissible units; LOCAL_REJECTS_GLOBAL_SCREEN if local constraints shrink the norm/additivity kernel; SATURATION_ON_KNOWN_UNIT if those screens leave exactly known point/unit classes; UNEXPLAINED_CANDIDATES if more remain. A unit surviving all screens is not automatically a genuine cohomology class unless its descent source comparison or explicit covering certifies it. The already certified positive unit must survive every legitimate necessary screen.

Construct rejected representatives by lexicographic basis search after recording full matrices; do not choose rows based on the desired result. Bind the actual known unit via beta1/beta2, not a printed class-dimension assumption. If exact tau action is inferred through residue evaluations, require rank15 and cached completeness and tau-stability; otherwise call it a necessary finite screen only. Do not claim finite additivity sampling is sufficient without an independent upper/lower dimension squeeze.

Initial individual jobs <=120 CPU seconds. No bnfinit/bnfcertify, no fundamental-unit expansion, no new Selmer source enumeration. Stop an expensive optional integral comparison and preserve matrices. A new arithmetic upper bound is not promised; the result is which source-side constraints do or do not distinguish point units from actual excess.
