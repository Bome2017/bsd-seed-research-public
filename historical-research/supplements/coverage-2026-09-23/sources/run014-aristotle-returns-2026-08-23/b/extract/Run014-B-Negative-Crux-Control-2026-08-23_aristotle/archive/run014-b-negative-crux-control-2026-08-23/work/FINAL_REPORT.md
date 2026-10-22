# Run014-B final report

```text
JOB_ID = RUN014-B
INPUT_VERIFICATION = PASS (verify_package.py exit 0, immutable_inputs = PASS)
FINITE_REPLAY = PASS (replay_control.py exit 0, uniform_theorem_certified = NO)
CONTROL_SOURCE = RUN013_62A1
MECHANISM_COORDINATES = squareclasses (-1)^s 2^e 31^f q^g in Q(S,2), S = {-1,2,31,q};
  local solubility of the oriented quartic covers C^(phi)_{q,d} and C^(dual phi)_{q,d};
  the isogeny-Selmer groups Sel^(phi_q)(E_q/Q), Sel^(dual phi_q)(E'_q/Q); derived
  Sel_2(E_q/Q), rank E_q(Q), Sha(E_q)[2^infinity]
OFFICIAL_CRUX_OBJECT = ord_{s=1} L(C,s) for every elliptic curve C/Q, and its equality
  with rank C(Q) for every value of r (seed/official/BSD_CRUX.md)
EXPLICIT_ACTION_ON_CRUX_OBJECT = NONE. The mechanism acts only on the algebraic node
  rank C(Q), and only for C = E_q with q in F_62, and only in the case rank = 0.
EXTERNAL_OR_IMPORTED_DEPENDENCIES =
  Zhai arXiv:1409.0231 Thm 1.5 (L(E_q,1) != 0 and its 2-adic valuation) -- load-bearing;
  Banwait-Huang arXiv:2601.16044 Thm 2.13 (odd-primary assembly), which itself consumes
  L(E_q,1) != 0 and BSD(E_q,2) and rests on further preprints;
  standard local theory for the Tamagawa/period table.
FIRST_MISSING_OBJECT_OR_BRIDGE = a 2-adic analytic-algebraic comparison for the NON-CM
  curve 62a1 and its prime twists: a 2-adic L-function / zeta element with explicit
  reciprocity, or equivalently the rank-zero 2-converse
  corank_{Z_2} Sel_{2^infinity}(E_q/Q) = 0 => L(E_q,1) != 0.
  The corpus's only rank-zero 2-converse (Burungale-Tian arXiv:2506.03465) requires CM;
  62a1 has multiplicative reduction at 2 and 31, hence non-integral j, hence no CM.
CRUX_CONTACT = NO
FINITE_CERTIFICATE_DESIGN = NOT_AUTHORIZED (Operator 2 gate fails at step 4: the official
  crux-bearing object does not exist in the supplied mechanism)
```

Full audit, including the mechanism and target dependency graphs, the intersection, and
the classification of all twelve candidate bridges, is in `ARISTOTLE_RESULT.md` at the
top level of the returned project; the decision log is `work/DECISION_LOG.md`.
