# Candidate B2 — tame–wild compatibility through the two-variable Mazur–Tate element theta_{l p^2}

Class B: compatibility theorem between two p-dependent constructions at the same p — the tame Kurihara–Ota witness
scalar w_{p,l} = C2(theta_l)/((a_l - 2) R_{p,l}) and the wild depth-2 coefficient c_2(p) of the p-adic L-function —
established from the common integral source: the Mazur–Tate Euler system {theta_m} of E (period-normalized integral
modular symbols; p-independent).

## 1. Object, ring, lattice, primes, construction
- Object: theta_{l p^2} in Z[G_l x G_{p^2}], G_l = (Z/l)^x, G_{p^2} = (Z/p^2)^x, for a good ordinary p >= 5 and an
  auxiliary prime l with l = 1 mod p^2 (so Frob_l = 1 in G_{p^2}) and p not dividing #E(F_l).
- Lattice: Z[G_l x G_{p^2}] modulo (p, I^3), I the total augmentation ideal. Second-order coefficients a_{2,0}, a_{1,1},
  a_{0,2} in F_p (after fixing generators of the p-parts of G_l and of the wild quotient of G_{p^2}).
- Norm relations (THEOREM, Mazur–Tate / Kato Euler-system relations; integral and p-independent):
  pi_{p^2}(theta_{lp^2}) = (a_l - l - 1) theta_{p^2}, and pi_l(theta_{lp^2}) = (a_p - sigma_p - p sigma_p^{-1}) theta_l.
- DERIVED (elementary; SECOND CORRECTION, 2026-10-01 second pass, after an external review relayed by the user —
  see CORRECTIONS.md, which takes precedence over earlier wording in this file):
  Work in ONE convention throughout, the Betti / Mazur–Tate–Teitelbaum convention for theta_m built from the modular
  symbols lambda(r) = int_r^{i infinity} f. In that convention the Hecke relation a_q lambda(r) = sum_b lambda((r+b)/q)
  + lambda(q r) gives BOTH tower relations without any factor q on sigma_q^{-1}:
     pi_{mq -> m}(theta_{mq}) = (a_q - sigma_q - sigma_q^{-1}) theta_m        (q good, q not dividing m),
     pi_{mp^2 -> mp}(theta_{mp^2}) = a_p theta_{mp} - nu(theta_m),             pi o nu = (p - 1) on Z[G_m].
  (The second relation is the one the MTT alpha-stabilized measure is built from, so it pins the convention.)
  Composite, modulo p, with tau = sigma_p - 1 in I_l and sigma_p + sigma_p^{-1} = 2 + tau^2 - tau^3 + ...:
     pi_l(theta_{lp^2}) == [ a_p^2 - a_p(sigma_p + sigma_p^{-1}) + 1 ] theta_l == [ (a_p - 1)^2 - a_p tau^2 + ... ] theta_l   (mod p).
  Since theta_l mod p lies in I_l^2 (retained Kato/Kurihara lower bound), the tau^2-term lands in I_l^4 and
     a_{2,0} == (a_p - 1)^2 * C2(theta_l)   (mod p).
  The multiplier (a_p - 1)^2 is a p-UNIT at every good seed prime p >= 5: a_p == 1 (mod p) iff p divides
  #E(F_p) = p + 1 - a_p, excluded by NORMALIZATION_ADDENDUM. At p = 7 (a_7 = -2) it is 9 == 2, not 0.
  WITHDRAWN: the earlier multiplier a_p^2 - a_p + 1 (and the "vanishing at p = 7") came from mixing the Betti distribution
  relation with a Kato-style etale Euler factor a_p - sigma_p - p sigma_p^{-1}; in Kato's normalization the p-tower is
  norm-compatible (no a_p theta - nu theta relation), so the two cannot be combined. Also withdrawn before that: a_p - 1.
  For the l-step the convention is immaterial mod p because l == 1 (mod p) makes (a_l - sigma_l - l sigma_l^{-1}) and
  (a_l - sigma_l - sigma_l^{-1}) congruent in F_p[G]; at p it is material. With Frob_l = 1 in G_{p^2} (l == 1 mod p^2):
     a_{0,2} == (a_l - 2) * [T^2-coeff of e_1 theta_{p^2}] == (a_l - 2) * alpha^2 c_2(p)   (mod p),
  using ((1+T)^p - 1)/T = T^{p-1} in F_p[T] (the nu-correction of the alpha-stabilized measure has no T^2 term for p >= 5),
  e_1 = trivial-Delta projector. The addendum's #E(F_p)/p does not appear in this projection; it belongs to the BKS
  cyclotomic-derivative normalization, a different object from theta_{p^2}.

## 2. Intended deduction
Pencil-shape statement (TARGET): theta_{lp^2} mod (p, I^3) is a scalar multiple mu(p,l) of the discriminant quadratic
form Q(t,w) = A t^2 + B tw + C w^2 of the G_{lp^2}-valued Mazur–Tate pairing on E(Q) tensor F_p (A = tame regulator
R_{p,l}, C = p-adic regulator Reg_p mod p, B = mixed term). Then
     w_{p,l} * (a_p - 1)^2 == alpha^2 c_2(p) / Reg_p   (mod p)        [HEURISTIC SHAPE, not derived],
i.e. tame scalar = wild scalar up to the unit (a_p - 1)^2. Consistency check (corrected second pass): under p-adic BSD
the right side is alpha^2 (1 - 1/alpha)^2 m = (alpha - 1)^2 m == (a_p - 1)^2 m, so the heuristic gives w_{p,l} == m with
NO leftover p-dependent factor — consistent with the constant tame value 288 in its convention. (The earlier
"unreconciled multipliers" flag was an artifact of the withdrawn identity.) Even so, the statement only transfers the
existing quadratic coefficient c_2(p) to the tame side; it does not force it to be nonzero. It would re-derive Theorem W
(l-independence, already proved) and identify the common value with the wild scalar.

## 3. First unresolved lemma and the test that fails
Lemma needed: pencil shape WITHOUT assuming Sha[p] = 0. This is the order-2 "shape" part of the Mazur–Tate refined
conjecture for a two-variable element; the only route I know is Mazur–Rubin's Kolyvagin-system structure theory
(tame classes kappa_{ab}, Lambda-adic leading term = Bockstein regulator), where the scalar is DEFINED through the
Selmer structure (Fitting ideal of the Sha part times regulator). Hence even if proved, the identity is
     omega_p != 0  <=>  w_{p,l} != 0  <=>  Sha[p^infty] = 0 (and Reg_p unit)   (under IMC on the retained domain),
another per-prime equivalence. The wild side omega_p has no independent uniform handle: c_2(p) mod p is the
"definite theta"/M_2 frontier (OPEN). Test that fails: ask what the identity adds for cofinite p — nothing beyond
Theorem W; the common-scalar step (T0 in ledger K2) is untouched.
No tiny exact check was possible: it needs modular symbols of the seed at level l p^2 (production size; forbidden).

## 4. Collision check
Ledger K2 (Theta_E, first missing compatibility T0: leading terms in finite augmentation quotients, no rational line),
Theorem W (w_{p,l} l-independence, fixed p), two-prime scalar extension C_p (RUN_NOW addendum 34: COLLATERAL; "proving
C_p = const * w_p would be another equivalence"). B2 is the tame–wild analogue of the tame–tame C_p coherence. The new
input is the mixed coefficient a_{1,1} of theta_{lp^2} and the explicit Euler-factor bookkeeping above; neither changes
T0.

## 5. Status
COLLATERAL (equivalence of per-prime criteria). The DERIVED bookkeeping in §1 is kept as a small explicit identity, at
derived grade, not as uniform input. Not continued.

## 6. WITHDRAWN incidental observation
The earlier §6 claimed the multiplier vanishes at p = 7 for the seed and speculated a link to the definite-theta
frontier's exclusion of 7. Both are withdrawn: the correct multiplier (a_p - 1)^2 equals 2 at p = 7 and is a unit at every
good seed prime p >= 5 (CHECK_RESULTS.json, second pass). The definite-theta exclusion of 7 has no connection to this.

## 7. Correction record
Second pass, 2026-10-01: external review (relayed by the user) found the projection multiplier wrong. Root cause:
convention mixing (Betti distribution relation combined with an etale Euler factor). Corrected identity: (a_p - 1)^2.
Verdict of the candidate unchanged: COLLATERAL. See CORRECTIONS.md.
