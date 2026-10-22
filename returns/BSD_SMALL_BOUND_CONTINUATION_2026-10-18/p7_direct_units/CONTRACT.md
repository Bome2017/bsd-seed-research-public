# Changed-source experiment: direct integral units at coefficient seven

Pre-registered before norm evaluation. No BNF retry and no class group input.

Use the already constructed actual degree-48 389a1 point field and its maximal-order basis. Enumerate at most 2000 explicit integral candidates: nonconstant basis vectors, basis-vector pair sums/differences, and small shifts of the reduced defining generator. An exact field norm +1 or -1 proves unitness independently of class-group or fundamental-unit completeness. Exclude rational +/-1 as uninformative candidates.

Arithmetic wall budget total120 seconds: first norm scan at most60 seconds, leaving at most60 seconds for exact export, split-prime discovery and finite-field incidence norm. Persist every norm computed, not merely successful units. Stop once two independent norm residues are obtained if feasible. No claimed absence of units follows if this finite candidate set fails.

The target is a lower bound r on the norm-map rank in scalar character sigma_3 ->3, yielding a whole ordinary-unit kernel upper bound 4-r. Actual class-supported directions remain separate. No known Sha, Selmer or target norm-kernel dimension enters candidate generation.

Existing p7_arithmetic is sealed and remains unchanged.
