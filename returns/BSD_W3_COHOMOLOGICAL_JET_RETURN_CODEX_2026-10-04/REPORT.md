# W3 arithmetic source and a certificate using ten critical points

Date: 2026-10-04, America/Los_Angeles.

**Status: W3_SOURCE_LAW_PROVED_WITH_VARIABLE_SPECIALIZATION_CERTIFICATE.**
Written derivations under retained seed/Hida inputs and named imported theorems. Independent review of the new derivations is pending. No cofinite nonvanishing theorem or new primary vanishing is claimed.

## Result directed at the seed

For a genuine integral Kato-family coordinate F_p constructed below, the new sufficient implication is

    F_p not in (p,T,S)^4  ==>  Sha(E/Q)[p^infinity]=0.     (1)

This holds on the stated cofinite **ordinary** domain, conditionally on the retained Hida-control result. It does not require F_p(p,p) to detect the nonzero jet. The original diagonal counterexample remains valid; the new proof changes the arithmetic specializations.

## What was supplied beyond the input

1. **A genuine global source.** Ochiai's optimized integral Beilinson–Kato family supplies the arithmetic Euler system in the specified representation. The source's hypotheses and character change are instantiated in [ARITHMETIC_SOURCE.md](ARITHMETIC_SOURCE.md). We apply the index bound to this system's own class; no unknown unit ratio with the old period-normalized z_g is asserted.

2. **Ten points with an actual seed implication.** For i,j≥0, i+j≤3, take weight parameter w=10+i and cyclotomic parameter s=7+j. Each representation reduces to E[p], preserves the seed's residual local conditions, and is a noncentral critical modular twist. The integral Euler-system/Poitou–Tate argument gives

       dim Sha(E/Q)[p] ≤ v_p(F_p((1+p)^w-1,(1+p)^s-1))-2

   whenever the value is nonzero. The specialization Tor term is retained and cancels, as shown in [VARIABLE_WEIGHT_INDEX.md](VARIABLE_WEIGHT_INDEX.md).

3. **The whole jet is detected integrally.** The ten-by-ten evaluation matrix is a p-adic unit matrix for p≥5; its reduction has determinant 576. Therefore a nonzero genuine jet modulo (p,T,S)^4 gives a nonzero value modulo p^4 at one of these ten critical points. Its index is at most three, and retained parity forces the seed's primary group to vanish. [TEN_POINT_CERTIFICATE.md](TEN_POINT_CERTIFICATE.md) proves the statement, rather than inferring it from numerical checks.

4. **Three actual coefficients vanish.** A global Selmer-complex determinant argument, with the one-sided integral family Euler-system inequality, proves

       F_p in (T,S)^2.

   The two independent rational point classes are the arithmetic input for this double zero. This is not inferred from local freeness or a rank-two label. [ARITHMETIC_LOW_JETS.md](ARITHMETIC_LOW_JETS.md) retains all its additional global hypotheses and proof steps.

The remaining genuine finite value is thus

    a T^2+b TS+c S^2+d T^3+e T^2 S+f T S^2+g S^3 (mod (p,T,S)^4),

with a,b,c needed modulo p^2 and d,e,f,g modulo p. These seven coefficients are **not evaluated** in this return. A quadratic coefficient which is zero modulo p can still contribute at index three and must be retained modulo p^2.

## Finite arithmetic source, not a fabricated jet

[FINITE_ARITHMETIC_SOURCE.md](FINITE_ARITHMETIC_SOURCE.md) locates the jet in the integral gluing of four actual weight fibers, of weights 12–15. Their product ideal lies in (p,T,S)^4. This makes a finite arithmetic source precise without assuming arbitrary global lifts or dividing by nonunit interpolation denominators.

The source construction and the finite interpolation are theorems at their stated grades. Extracting the seven remaining arithmetic coefficients has not been executed. There is no new seed numerical Kato value in the check output.

## Review of the supplied packet

The local perfect-complex argument, exact base change, and pseudo-null-to-isomorphism argument are confirmed under their retained hypotheses; see [LOCAL_REVIEW.md](LOCAL_REVIEW.md). The conclusion is local. It does not show eta_p is a unit or remove all global specialization issues.

The supplied 7-entry manifest and the retained Hida return's 31-entry manifest verify. The supplied finite-ring checker reproduces its output byte-for-byte: 36,105 formal assertion groups. The new checker verifies the interpolation determinant, all ten critical ranges, 2,300 finite-ring reconstructions over 23 primes, the diagonal countercontrols, and the finite-source ideal containment. These are algebra controls, not seed Selmer computations or independent proof certification.

## Exact endpoint and remaining work

An independent proof that the genuine seven-coefficient class is nonzero for cofinitely many ordinary p would, by (1), remove that infinite ordinary primary tail. This packet does not prove such nonvanishing. No fixed p-independent ancestor is required by (1), and no equality to C_p or another existing witness has been proved here.

The finite excluded primes and the supersingular primes remain outside this result. FIN, ORDER9 and Q36 remain open. Publication in the experiment lab does not promote these written derivations into the research release.

[Review handoff](HANDOFF.md) · [Sources](SOURCES.md) · [Formal controls](checks/TEN_POINT_RESULTS.json)
