# Return — uniform-depth v2

REDUCED

**DERIVED — scope.** The finite-exceptional-set target in v2 §5 is not proved. No complete uniform vanishing construction passed all endpoint tests. The reduction below is a proved comparison at imported-theorem / retained-seed-input grade, not a positive endpoint certificate and not a universal obstruction.

## New comparison

**DERIVED.** For every good p>=5, define h_p to be the minimum lambda-valuation of a full BH Mazur–Tate character value over real cyclic degree-p fields at their actual conductors prime to pN, with +infinity allowed. Then

    min(h_p,p-1) = min(r_p,p-1)
                 = min(dim_Fp Sel_p(E/Q),p-1).

The proof uses BH Theorem 1.4(b), its exact conductor norm relation, and the retained B.20/B.21 inputs. No arithmetic level-p^k compatibility, rationality of q, or unknown Sha order is assumed.

**DERIVED — explicit rank-two bridge.** Given any two-prime Kato unit witness delta_(q_1 q_2), form the C_p^2 compositum L of the degree-p cyclotomic subfields at q_1 and q_2. In the total-real-period normalization,

    theta_L^MT mod (p,J^3) = delta_(q_1 q_2) T_1 T_2.

Every cyclic quotient nontrivial on both inertia factors has actual conductor q_1q_2 and every faithful character has exact depth 2. In particular the diagonal quotient gamma_1,gamma_2 |-> gamma is sufficient.

**DERIVED — consequence.** Under the retained inputs, (i), (ii), and (iii) of v2 §5 are equivalent to each other and to Sha[p^infinity]=0 for every good p>=5. The previously unrecorded direction (ii)->(i) is established, at the same conductor. This does not prove that these equivalent properties hold at an unsettled prime.

## Uniform attempts and first failures

**DERIVED.** Unspecified-length primitivity, filtered projection/unit-norm shortening, local separation of the rational basis, parity, and completed compatibility all stop at K-S when proposed as complete endpoints. A sufficient nonzero character-norm budget and a common finite integral Selmer presentation were formulated, but their constructions stop at K-P: the needed cofinite estimate or comparison was not established. The universal full-Sha scalar obstruction is not proved; the conditional version cannot be used unconditionally under K-F.

**DERIVED — no coverage upgrade.** No new primary vanishing, no new infinite subset of primary-vanishing primes, no cofinite vanishing set, no common rational scalar, and no total-Sha finiteness were proved. The comparison theorem itself covers every good p>=5, including 19,59,487, but its domain is not a vanishing-coverage claim.

## Execution

The requested PARI executable is absent in this container. No substitute arithmetic computation was run. Work comprised exact written derivations, source reading/theorem verification, and file handling. No subagent, push, paid computation, prime search, or seed-certificate replay was used. Source verification was confined to the quoted BH and Kriz–Nordentoft statements. The files are in this session's container, not the user's host home directory.

Read ATTEMPT_I_CHARACTER_DEPTH.md for the complete proof, ATTEMPT_II_TWO_PRIME_WITNESS.md for the independent quadratic replay, and SELF_REPLAY.md for the scope and boundary checks. No subsequent construction campaign is authorized by this return.

FIN, ORDER9 and Q36 are unchanged.
