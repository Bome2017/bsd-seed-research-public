# RESULT — C1_ULTRA_PARALLEL_NORM_RELATIONS_001

**STATUS: NO_LOWER_DEGREE_FACTORIZATION_IN_STATED_CLASS**

Date 2026-09-17. Author-side derivation for independent review.
No canonical seal, ledger or memory file was written or modified.
Phase 2 (arithmetic bridge) was NOT entered, because Phase 1 returned NEGATIVE.

--------------------------------------------------------------------------
## 1. The finding, in one sentence

The projector cutting out the retained dual component (Cl(L_d)/5)^chi of the
degree-24 field L_d = K^{H_d} is **not** in the F_5-span of any compositions
through the permutation modules F_5[G/J] for **any** subgroup J of
G = GL_2(F_5) of index < 24; the minimal index at which it becomes obtainable is
exactly 24, and the only subgroup attaining it, up to conjugacy, is H_d itself —
i.e. L_d.

## 2. Exact arithmetic significance

* By Etienne (arXiv:2411.13124v2) Thm 3.4 + Prop 1.3, the operators between the
  groups Cl(K^J)/5 that are built from ideal extension, ideal norm and field
  conjugation are exactly the double-coset operators, and these span the
  F_5-linear Hom spaces between the permutation modules.  Hence the obstruction
  covers **every** mod-5 norm/transfer/conjugation factorization of the target
  component through subfields of K = Q(E[5]) of absolute degree < 24.
* Consequently the degree-24 generator problem for L_d **cannot be bypassed**
  inside this Galois closure by any relation of the type BFHP and Etienne supply.
  The one-sided certificate route still needs unconditional generator coverage
  for Cl(L_d)/5 at degree 24.
* By the same computation there is also **no generalised norm relation for
  N_{H_d} over F_5** (Etienne Def. 2.4) with respect to index < 24, and BFHP
  Prop. 2.18(4) fails for the full Cl(K): 12 of the 20 simple
  F_5[GL_2(5)]-modules are annihilated by N_J for every J of index < 24.  So the
  unprojected problem is obstructed too.
* The only direction that does work is **upward**: the component is a summand of
  F_5[G/U], i.e. it is visible in the degree-96 field K^U = L(mu_5).  That is
  larger, not smaller, and is of no use for certification cost.

**This is not a Sha result and does not bear on b, c or r_5.**  It removes one
proposed route; it proves nothing about Sha(E/Q)[5^infinity] for any C1 member.

## 3. Why the answer is trustworthy

* Two independent implementations agree: GAP 4.15.1 over the complete subgroup
  lattice (48 conjugacy classes, 466 subgroups), and a from-scratch Python
  implementation with its own complete BFS enumeration of the 18 overgroups of
  the Sylow 5-subgroup and its own exact F_5 linear algebra.
* The Hom spaces were computed by **solving the equivariance system**, not by
  assuming a double-coset basis; the basis was then recovered and matched
  (dim End_{F_5G}(P) = 5 = |H_d \ G / H_d|, Etienne Prop. 1.3).
* All 15 conjugacy classes of index < 24 were tested with their full Hom spaces:
  43 compositions, spanning a 3-dimensional subspace of the 5-dimensional Hecke
  algebra; adjoining e raises the dimension to 4.
* **Positive controls fire.**  The same code finds a genuine exact degree-12
  factorization for the quadratic character and a degree-6 one for the trivial
  character.  Only the two faithful quartic characters are obstructed, and both
  are obstructed identically — so the result is insensitive to whether the
  convention is chi or chi^{-1}.
* The character convention was rebuilt from scratch (left action, right
  translation, contravariance of the fixed-point functor) before the projector
  was chosen; the cancellation of the anti-homomorphism against the
  contravariance is recorded in PROOF.md §1.  chi(sigma) = 2 with sigma = diag(1,2)
  was verified to be the theta*-eigenvalue, and ker(theta*) = H_d exactly.

## 4. The certificate

Inside the 5-dimensional Hecke algebra End_{F_5G}(P) with double-coset basis
T_0,...,T_4 (H_d-orbits on G/H_d of sizes 1,1,1,1,20):

    e                      = (4, 2, 3, 1, 0)
    span of ALL allowed compositions = < (1,0,0,1,0), (0,1,1,0,0), (0,0,0,0,1) >
    separating functional  Lambda    = (1, 2, 3, 4, 0)

    Lambda(each span generator) = 0 ,   Lambda(e) = 1 .

Lambda is not an ad hoc linear form: it is the Brauer-quotient evaluation at the
Sylow 5-subgroup U on the theta*-line, which is why it provably annihilates
every composition through every allowed J (PROOF.md Lemma 5.1), including maps
never listed.  A second, independent witness in the 2-dimensional annihilator is
f = (0, 4, 1, 0, 0), also with f(e) = 1.

## 5. Remaining obligation (unchanged by this result)

ARITHMETIC_INPUT_NOT_IDENTIFIED still stands.  The retained target b <= 2 for the
whole dual component is untouched.  What this task removes is one candidate
mechanism; the open input remains unconditional generator coverage for
Cl(L_d)/5, or a whole-component bound obtained some other way.

## 6. Resource use

Aggregate 107.9 CPU-seconds (51.7 first pass + 56.2 full replay; cap 300), one
process at a time, peak well under 4 GiB.
No number field, bnfinit, bnfcertify, bnftestprimes, 389a1 calibration or
modular-symbol computation was run.  No additional agents were launched.
