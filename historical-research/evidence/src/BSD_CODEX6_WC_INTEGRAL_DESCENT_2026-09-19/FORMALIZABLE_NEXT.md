# Bounded formalization targets

No Aristotle submission, Lean build or package modification was launched by this session. The user assigned existing packages to Opus. This report supplies exact statements and the interpretation warning for those packages.

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

## Package-compatible conditional algebra

1. Preserve the exact WC quantifiers and zero-depth convention from EXACT_WC_ANTECEDENT.md. Required arithmetic inputs are Ota I^2 membership, the higher-Selmer-corank vanishing implication, and the primitive witness implication. Primary finiteness at excluded primes is a separate hypothesis.
2. Formalize the chain-ring lemma: a nonzero ideal D=p^d(Z/p^k), d<k, has cokernel killed by A iff d<=v_p(A). Derive the existence of a displayed generator with minimum valuation. This is U1's algebraic engine, not a proof of UC.
3. Formalize the degree-two truncated group-ring presentation T1 and the support reduction T3, with the arithmetic norm relation supplied explicitly as a hypothesis. The finite module is not a rational line.
4. Formalize the normal-basis/dual-basis coefficient isomorphism underlying L4. To call it Ota's map, a separate arithmetic instantiation must provide the formal group, normal integral basis, perfect local pairing and reciprocity identification.
5. Keep the predecessor rational-spacing and bounded-algebraicity lemmas. The common-B assembly can be formalized over rational B with explicit primary finiteness and valuation bounds. It must not introduce #Sha before proving global finiteness.

The ordinary equivalence can be recorded as a conditional composition theorem, but its Kim/Castella-Sano/Ota imports must remain named assumptions until those arithmetic theories are formalized. A compiled wrapper is not a new proof of their inputs.

## The arithmetic lemma is not ready to be 'proved by formalization'

UC has a precise statement and concrete arithmetic maps. Its proof is unknown. An interface containing 'uniform_content : exists A ...' is a useful specification; it is not an arithmetic construction of A. Formalization may protect quantifiers and expose misuse of truncated zero, but cannot remove this missing premise.

A formalization of the positive-depth ordinary converse must also preserve the auxiliary-prime restriction. The primitive proof supplies it from Kim's localization isomorphism and rank two; that argument does not automatically extend to positive depth.
