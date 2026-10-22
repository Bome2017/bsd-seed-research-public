# Partial-relation cancellation: bounded execution

Status: **NO_NEW_UNIT_SOURCE; SELECTED_SCALAR_FAMILY_EXCLUDED_BY_ACTUAL_PRIVATE_PRIMES.**

The changed experiment was executed. It produced no unit to send to the norm/local evaluator, so it contributes no unit-kernel upper bound or class-supported bound. The field is the degree-48 nonzero 7-torsion point field of the rank-two -47 twist of 11a1, a control rather than the original seed.

## What was actually available

The prior relative-unit run saved all 14,326 exact norms and deterministic stage/candidate coordinates, but not all element vectors. This run reconstructed only eighty selected elements and required exact agreement with their saved norms. Four were in the previously excluded top-twenty panel; seventy-six were not. No full weighted search or BNF was repeated.

The earlier instrumented PARI collector exported only candidates passing its smooth filter. Its rejected mixed partial relations were not saved. The new operation therefore used the retained weighted-search norm log to look for shared support before requiring full smoothness; it is not claimed as a new class-group algorithm.

## Selection and exact execution

An exact product/remainder-tree batch GCD calculation on all norms, after removing rational primes through 1000, took 6.92 seconds. It found 5,519 norms with some shared residual support, none fully smooth over that base, and none whose unmatched cofactor was one.

The field called `private` in the JSON is precisely n/gcd(n, product of the other residual norms). It is an unmatched-multiplicity cofactor, not automatically a product of globally unique primes. No exclusion is inferred from it.

The eighty-row panel uses the sealed lexicographic score: unmatched-cofactor bit length, residual-cofactor bit length, full-norm bit length, original row index. No graph-component prioritization was used. This is a bounded feasibility screen, not an exhaustive graph optimization.

Reconstruction took 16.30 seconds. All eighty elements were mixed under tau and exactly reproduced their saved norms. The selected unmatched cofactors have at most 49 bits.

A subsequent sealed exact pivot gate took 6.10 seconds. For every selected element it found and proved a prime q with norm valuation one, formed the actual prime ideal P=(alpha)+(q), and verified P differs from tau(P), with exact alpha membership and nonmembership witnesses. Independent Python checked that q occurs in exactly its own row of the full 14,326-row log. All eighty passed.

A 1.09-second scalar check verified the six actual HNF images of each prime are distinct. On each orbit the six translated anti-divisors have block e_j-e_{j+3}; the faithful projector gives (5,4,6,2,3,1) modulo seven. These disjoint private blocks prove rank eighty for the faithful projected columns and rank 240 for all 480 translated columns. Exact inverse identities account for the entire integral divisor kernel. Thus every ordinary unit product in this selected scalar subgroup is 1, and seventh-root repairs within the field cannot create a new source from it.

This early exact exclusion made complete factorization of all eighty ideals unnecessary. No incomplete factorization was treated as an ordinary-unit certificate. Total arithmetic was about 30.9 seconds, with maximum recorded GP RSS about 101 MB. The expensive stage was stopped before execution, rather than spending the remaining budget on a family already excluded.

## What changes next

The experiment explains why mere shared rational support was insufficient here: every selected candidate retained an actual private prime-ideal direction, even after scalar projection. A successful cancellation construction must arrange repeated *actual prime-ideal* support rather than just reduce norms. That is a selection requirement, not a new FIN theorem or a recommendation to rerun the same scan at a larger bound.

This is a complete finite-family exclusion, not a bound on undiscovered units or classes. It does not exclude the remaining 14,246 saved elements or other source families. The class-map lane remains logically separate. FIN, ORDER9 and Q36 are unchanged.

See PROOF.md for the exact algebra and retained hypotheses, RESULT.json for the eighty distinct witness primes and full-log occurrence checks, and the GP files for actual vectors/ideal HNFs. No repository publication was made by this worker.
