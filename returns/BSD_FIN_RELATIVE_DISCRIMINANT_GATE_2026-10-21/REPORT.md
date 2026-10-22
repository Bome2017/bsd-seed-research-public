# October 21 FIN return: uniform local discriminant gate closed; small class bound remains open

**Status:** WRITTEN UNIFORM RELATIVE DISCRIMINANT POSITIVITY (under retained local type-III and full-image inputs); independently checked finite orbit arithmetic. Mathematical FIN, ORDER9, Q36 remain OPEN.

## What changed

For all good coefficient primes p>=5, set n=p^2-1, A_p=Q(nonzero p-torsion point), and K_p its central scalar-minus-one fixed field. The quadratic relative discriminant norm satisfies

    delta_p=2^alpha_p*p^beta_p*4547^(n/4), alpha_p,beta_p>=0.

The type-III tame inertia at 4547 forces exponent n/4; multiplicative places 3,2243,5843 contribute relative exponent zero. Consequently

    delta_p>2^n,
    lambda_p>=n*log(4547/16)/(4*sqrt(p*(p-1)))>0.

Thus the positivity gate (P) of the October 20 symbolic all-p analytic class estimate, formerly unevaluated beyond p=5, follows uniformly from the already retained seed local data. The full mathematical argument appears in PROOF.md. Running check_inertia.py reproduces nine finite orbit tables. This is not a new proof of the elliptic local reduction data; those are imported.

## Why this does not prove FIN

The whole relative five-class length bound of 97 and conservative complete-source bound 100 do not change. The new result only removes the sign uncertainty in the earlier analytic regulator lower bound. The complete faithful class-lift contribution k_C and actual joint unit rejection rank r_U are still unmeasured at the needed strength, with missing class generators not set to zero. The sufficient parity-relaxed objective on the valuation-zero domain is

    r_U(p) - k_C(p) >= (p-5)/2,

for all but finitely many p, plus remaining exceptional-primary obligations. This inequality is NOT proved or numerically established by this return.

## Exact checks and grade

The stand-alone standard-library checker enumerates the nonzero vectors in F_p^2 and the antipodal quotient under J(x,y)=(-y,x) and U(x,y)=(x+y,y). PASS at p=5,7,11,13,17,23,31,53,83; it recovers p=5 discriminant exponents 18,6,6 at 4547 and relative exponent zero at multiplicative places. These are finite controls on a written group-theoretic calculation, not new computations of class groups, global Selmer or Sha, or certification of the original local representation.

## User-directed research order

1. FIN complete joint unit/class source bound is ACTIVE. The next mathematical input must bound the entire compatible class-lift kernel or supply a certified containing-source presentation; merely improving a selected finite relation rank or repeating the excluded 196-row and 31-function constructions is insufficient. A p=5 test alone is not cofinite FIN.
2. After #1, return to the preflight-frozen p=53/ell=743 Ota singleton experiment; production has NOT been launched by this return, and the existing cap/review/permission conditions are preserved. Even a positive result adds only a settled prime.
3. After #2, return to Q36 and its missing arithmetic-to-real comparison or independently proved arithmeticity/denominator restriction, NOT just additional finite congruence fits.

The companion research repo v0.2.6 and both main branches are unchanged. Publication to this lab research branch records custody and does not certify a new theorem with a human referee.

Current source base: Bome2017/bsd-seed-lab@ceadfa43c5543cf5efd75d0ed72cad5728d6e7cc.