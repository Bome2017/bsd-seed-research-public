# Independent review: Neron-normalized kernel and explicit denominator

Reviewed repository: `Bome2017/bsd-seed-lab`  
Reviewed branch: `claude/paired-kernel-construction-phivfw`  
Pinned commit: `b358f7507759dad4a1e016c519d6f486ffca37e1`  
Date: 2026-09-24.

## Verdict

**`NORMALIZATION_AND_DENOMINATOR_SOURCE_REVIEW_PASS`**, at the retained mathematical-import grade.

No material false implication was found in the two new deductions. The strongest denominator
is `B_theta = 2^10*4547 = 4656128` for the specified degree-zero integral theta packets.
The weaker join denominator `B_join = 2^17*4547 = 595984384` also follows.
This review does not alter the expert release or certify a seed value.

The concrete improvement is that the paired-kernel route now has a specified arithmetic
acceptance rule, not just a p-integrality assertion. It does not make seed enumeration
cheap, prove the moment is nonzero, or finish finite support or the real BSD formula.

## 1. Scope and source-reading boundary

The new proof files and the two small checking programs were read through the authorized
GitHub connector at the pinned commit. The branch ref agreed with that commit when checked.
The metadata in SOURCE_BINDINGS.json records the returned Git blob identities. This was not
a fresh download/manifest verification of the entire repository. No repository write was made.

Primary statements checked:

- Kim--Ota, arXiv:1905.02926v4, Definitions 2.11--2.12; section 6.1, pairing (6.1),
  Assumption 6.3, Theorem 6.5, Remark 6.6(1), Corollary 6.7; the relevant full-Hecke definition.
- Agashe--Ribet--Stein, *The modular degree, congruence primes, and multiplicity one*,
  Theorem 2.1, the integral q-expansion duality, and Theorem 3.6/Remark 3.7.
- Cesnavicius--Neururer--Saha (CNS), arXiv:1911.09446v3, the cusp slash normalization,
  Proposition 5.14, Proposition 6.2/Example 6.3, and Theorem 6.12.

The source statements and the new interfaces were examined. The proofs of all imported
arithmetic-geometry and Taylor--Wiles results were not re-proved. The retained surjectivity,
chosen parametrization, and Manin bound `c_E | 512` keep their existing grades. In particular,
the sharper theta bound still uses that retained Manin bound; it does not make the earlier
Manin calculation unnecessary.

## 2. Unit-scale comparison

Write `P_f = <f,f>`, `P_G = <G,f>`, and `A_E` for the complex Neron period-lattice area,
not the full real period. For the chosen map of degree `ed` with
`phi_E^* omega_E = c_E (2 pi i f dz)`, integration of the area form gives

    ed A_E = 4 pi^2 c_E^2 P_f.

Consequently

    K_E(G) = (4 pi^2/A_E) P_G = (ed/c_E^2) lambda_f(G),
    K_E(v,w) = u_E psi(v)psi(w),     u_E = ed/(c_E^2 M),
    M = sum_x psi(x)^2.

The weights of the quaternionic pairing are 1 on the seed class set, and its
Atkin--Lehner transport acts on the one-dimensional elliptic eigenline by a sign.
With a primitive integral generator, the pairing ideal is therefore `(M)` locally.
The identification is of ideals/valuations, not an equality of positive numbers.

Under the checked CR+ hypotheses, KO Corollary 6.7 gives the equality of this pairing
ideal with the N-minus-new classical congruence ideal and its comparison with the
full classical ideal. The multiplicative discriminant valuations 2,1,2 imply zero
Tamagawa exponents for residual primes p >= 5. At the potentially good places 2
and 4547, the finite inertia images have order prime to p, so the averaging
idempotents show invariants and conductor exponents survive reduction. Thus the
prime-to-p residual conductor remains N.

The full integral Hecke algebra/dual integral q-expansion description matches the
classical congruence number r. ARS then gives v_p(r)=v_p(d) for p^2 not dividing N.
In the present good-prime scope this proves

    v_p(M)=v_p(d),  and hence  u_E in Z_p^times,   p >= 5, p not dividing N.

There is no need to assume p does not divide M: the matching valuations cancel.
Nor does the argument identify M with a classical degree or congruence number globally.

The nonordinary part retains KO Remark 6.6(1)'s replacement of the ordinary deformation
condition by the low-weight crystalline one. This is an explicit source-backed import,
not a new proof of that adaptation in the lab. The ordinary assumption in KO section
6.2 is not being used to justify section 6.1.

## 3. Why the denominator proof works

### 3.1 Cuspidality is an actual hypothesis

For integral z,w with deg(z)=0, put G=Theta(z,w). The constant term at any cusp
factors as a fixed local constant times deg(z)deg(w), because the relevant norm
lattices have the stated local order types and the zero-vector Gauss factors do
not depend on the ideal pair. It vanishes. At infinity, pairing nonzero lattice
vectors with their negatives makes every positive Fourier coefficient integral.
Thus G is an integral cusp form, not just a modular form vanishing at infinity.

### 3.2 The local Gauss valuation is an algebraic calculation

For an Eichler place p with level p^n, a cusp denominator with valuation e<=n,
and m=p^e, use the retained frame

    r = [[r1,r2],[p^n r3,r4]],
    ell = [[l1,l2/p^n],[l3,l4]].

In the defining Gauss exponent, the term p^n*r2*r3 vanishes modulo m.
Summing over r2 and r3 is zero unless m divides l2 and l3, and otherwise contributes
m^2. Summing over r4 forces a*r1+l1=0 modulo m, contributing m. The remaining term is

    m^3 zeta_m^(-u*v*l1*l4/a),

with a,u,v units. This proves the support, phase, and valuation 3e, including p=2.
The division-place calculation is the previously retained rank-two nonsplit norm
Gauss sum times its two radical variables; it supplies the same 3e valuation for
e=1. Its earlier mathematical review is retained, not newly reimplemented here.

In the theta transformation, the factor 1/2 cancels exactly by ell versus -ell for
positive Fourier indices, also at p=2. The remaining prefactor has valuation
-n-2e. Every summand therefore has valuation at least e-n. Roots of unity have
valuation zero at every embedding, and sums cannot lower this bound.

### 3.3 Comparison with the actual CNS thresholds

CNS Proposition 5.14 applies to arbitrary cusp forms in its domain. Its thresholds
at a cusp with e=v_p(c), n=v_p(N) are

    -n                         e=0,
    e-n+1/(p-1)                0<e<n,
    0                          e=n.

The available theta bound is e-n. It already meets the outer thresholds.
There are no intermediate components at the three division primes, whose exponent
in N is 1. At the two repeated level primes, one extra factor of p meets all
intermediate thresholds. At 2 this is exactly one extra valuation unit; at 4547
the deficit is 1/4546 and multiplication by 4547 is sufficient.

It follows that

    D0 omega_G in H^0(X_0(N),Omega),   D0=2*4547=9094.

CNS Theorem 6.12 applies at all p>=5, at 3 because v_3(N)=1, and at 2 because
3 divides N and 3=3 mod 4. Proposition 6.2 and Example 6.3 therefore identify this
lattice with the Neron cotangent lattice. No application of the normalized-newform
Theorem 5.15 to a general theta combination is being made.

### 3.4 Pullback to E removes the apparent second Manin denominator

Let i_E:E->J_0(N) be dual to the chosen quotient, so pi_E i_E=[ed]. On the f-line,
Hecke equivariance and the pullback identity give

    i_E^* omega_G = (ed/c_E) lambda_f(G) omega_E.

The map extends to Neron models. Pulling back D0 omega_G hence yields

    D0 (ed/c_E) lambda_f(G) in Z,
    equivalently D0 c_E K_E(G) in Z.

Since c_E divides 512,

    4656128 K_E(G) in Z.

The whole-lattice 2^8 join instead gives the weaker 595984384 denominator. Neither
argument substitutes denominator support for a numerical exponent bound.

## 4. Precision and scope clarifications

1. Use the exact conditions, not rounded thresholds:

       radius < 1/9312256       for B_theta,
       radius < 1/1191968768    for B_join.

   The latter is approximately 8.38948156064438e-10. The prose decimal 8.39e-10
   is slightly larger and must not be used as a rigorous stopping threshold.
   This is a display/acceptance-rule issue, not a flaw in the lattice proof.

2. The bound as proved is for degree-zero integral packet lifts. Balanced squared
   residues do not always sum to zero over Z (for p=11 they sum to 22). Since their
   sum is divisible by p, subtracting the degree from one chosen class coefficient
   produces a degree-zero lift with exactly the same reduction modulo p. The
   actual analytic inputs and certificate must identify which lift was used.

3. The radius condition is on the FINAL normalized scalar, after all pair, anchor,
   period-area, and tail errors have been propagated. It is not a sufficient
   per-pair or per-numerator tolerance.

4. For a verified interval [L,U], lattice membership allows one to test

       [B L, B U] intersect p Z = empty.

   This can certify a unit without identifying the unique integer. An interval
   with no integer at all contradicts the claimed lattice/enclosure; it is NOT
   a successful nonvanishing certificate. A divisible recovered integer is not
   by itself a proof of nonzero Sha, because the bridge is only sufficient.

5. The remaining computation is analytic/geometric for THIS certificate route.
   This does not turn the entire BSD problem into a numerical computation: no
   nonvanishing is supplied, there is no uniform finite-support statement, and
   the real leading-term equality remains separate. The fixed denominator B is
   not a fixed nonzero integer supporting all possible Sha primes. The numerator
   still depends on p and on the Gross packet.

6. The author's 166 Gauss comparisons use complex floating arithmetic. Their
   stated tiny discrepancies are numerical checks, not exact p-adic evidence.
   The general sum identity above is a proof; the new exact finite checks below
   additionally avoid rounding in the tested cases.

## 5. Checks actually performed here

- 262 exact Eichler Gauss-sum comparisons: 166 fresh odd-prime cases at levels
  5^2,7^2,11^2 and 96 dyadic cases at level 2^3. Integer polynomials modulo the
  prime-power cyclotomic polynomial are compared, not complex approximations.
- Two deliberate wrong-phase/amplitude controls are rejected.
- All 13 cusp-threshold inequalities for the prime factors of N are checked as
  exact fractions; the two denominator integers and precision fractions match.
- Five interval-acceptance controls and nine degree-zero relift examples pass.
- Independent 110-decimal period quadrature agrees with the replayed old rational
  AGM ball: 4*pi^2/A_E = 46069.619435369159596832632935... . Quadrature agreement is
  numerical evidence, not a new certified quadrature theorem. The AGM source
  is copied unchanged from the previous uploaded handoff and identified by hash.

The small exact checks do not reconstruct any seed Hom lattice or evaluate any
seed theta numerator. No full manuscript, corpus, source theorem, or Lean replay
was repeated. The new scripts are not production evaluators.

## 6. Decision

Retain the normalization and denominator derivations, with their explicit inputs
and the scope/threshold clarifications above. Treat the denominator-existence
operation as completed at that grade. Do not commission another session simply to
find a denominator, repeat D5, or reimplement the finished support optimization.

A subsequent seed-evaluation task needs actual input geometry, a costed analytic
algorithm and a complete propagated interval budget for the specified scalar.
This review does not authorize that production run, paid compute, a merge, or any
change to the expert release.
