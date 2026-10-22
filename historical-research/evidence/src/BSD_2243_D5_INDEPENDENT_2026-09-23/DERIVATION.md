# Independent low-precision split-height derivation (working)

## Sources and object
Stein--Wuthrich section 4 (Bernardi sigma, polarization), section 4.2 (Werner-corrected split height), and section 4.4 (gamma normalization), local pinned text. Curve E has a1=a3=0; use the retained reduced model a2=-1, a4=-66020924, a6=-65074271436, with P1=(-3031,327384), P2=(-2394,281520). The change x=X+7578 has u=1 and preserves the differential.

For Q=mP on the identity component everywhere and in the formal group at p, the published formula is

    h(P) = m^-2 [2 log_p(e(Q)/sigma_p(Q)) - log_p(u(Q))^2/log_p(q)].

Here e(Q) is the positive square root of the global reduced x-denominator, not just its p-part; log_p(p)=0. This exact global height formula is the imported analytic theorem. No BSD formula, finiteness of Sha, or PARI height is used to evaluate it.

## Working mod p^2
At p=2243, the Bernardi expansion has sigma(t)=t+(a1/2)t^2+..., and a1=0. The canonical exponential correction has integral weight-two coefficient and log_E(Q) in p Z_p. Thus log(sigma_p(t)/t)=0 mod p^2; a uniform coefficient bound for the omitted terms is to be detailed before certification. Also log_E(Q)=t+O(p^2).

Write psi^* omega_E = C du/u. Scaling the Tate invariants gives C^-2 = -c6(E)/c4(E) mod p (the Tate curve has c4=1, c6=-1 mod p). Therefore

    h(P) = m^-2 [2 log_p(e(Q)/t(Q)) - k t(Q)^2/log_p(q)] mod p^2,
    k = -c6/c4 mod p.

This is not a local-logarithm-only formula: e(Q) retains the global denominator contribution.

## Denominators without large rational coordinates
Take R=2P and n=p-1, so m=2n. Verify that R is nonsingular on every bad Weierstrass fiber, and that the model is minimal (retained input). Then R belongs to E0 at every finite place. Write x(R)=a/d^2, y(R)=b/d^3 in lowest terms. The division-polynomial denominator identity on E0 is

    e(nR) = +/- d^(n^2) psi_n(R).

Its local proof and small exact controls will be supplied. With phi_n=x psi_n^2-psi_(n-1)psi_(n+1), the usual multiplication identities give

    t(nR) = -2 phi_n psi_n^2 / psi_(2n),
    U := e(nR)/t(nR) = +/- d^(n^2) psi_(2n)/(2 psi_n phi_n).

The sign is killed by the p-adic logarithm. All expressions can be evaluated modulo p^k by a memoized division-polynomial recurrence. They require no rational coordinates of nR. Division by psi_n or psi_(2n) loses their explicitly computed p-adic valuations; retain sufficient guard digits.

## q and logarithms
Put z=Delta/c4^3. Since v_p(Delta)=1 and c4 is a unit, q=z+744z^2 mod p^3 follows from j(q)=q^-1+744+196884q+... . For any unit a,

    log_p(a)/p = ((a^(p-1)-1)/p)/(p-1) mod p.

This determines log_p(q)/p from q/p mod p^2. It is computed from the model; the retained value is comparison only.

## Finite arithmetic target
For P=P1,P2,P1+P2 compute h(P)/p mod p. Polarize with (h(P1+P2)-h(P1)-h(P2))/2. A nonzero determinant of this matrix over F_p certifies v_p(Reg_p)=2 and Reg_gamma is a unit, since log_p(1+p)/p=1 mod p.

## Pre-execution budget
Only O(log p) memoized recurrence indices at modular precision initially p^5, plus three exact doublings and one exact sum. No allocation indexed by p^2 or conductor. Initial run: one process, 120 CPU-second cap, 1 GiB memory cap, 50 MiB output cap. Increase p-adic precision within these limits only to validate a determined nonzero valuation or comparison. No coefficient corpus is consumed.
