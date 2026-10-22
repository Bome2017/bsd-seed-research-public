# Review the local lattice before resuming the global bound

Status: W3_UNIFORM_PARTIAL. New derivation, not independently accepted.

Read LOCAL_LATTICE.md first. Priority checks:

1. Integral quotient: H^2(A)=0 and torsion-free H^1(M) give the actual
   singular quotient Q=H^1(M), with the retained rational finite line.
2. Venjakob A.2 at r=-1, eta=alpha: 1-p^r phi=1-alpha(tau_p)^-1 is
   a unit; the integral Coleman map is an isomorphism. Check the
   coefficient-DVR extension rather than invert p.
3. H^2_Iw(T0)=0 and integral finite-level descent: the tame idempotent
   is an integral generator of the required omega^-1 component, not
   just a nonzero rational vector.
4. A.67/A.73, n=1: both powers of p are present; the Gauss sum has
   character omega^-1 and has not been discarded. The desired result
   is equality exp*(Q)=p^-2 O e_g.
5. Kato 14.13 in its own period convention: the Euler factor cancels
   p^2, leaving b=v_pi(c_g L(g,2)/Omega_g). The still-unevaluated c_g
   is carried explicitly. No claim c_g=1 or c_g a unit is permitted.

The main BSD implication after this comparison is retained:

    independent v_pi(A_g)<=3 -> Sha(E/Q)[p^infinity]=0.

The next substantive arithmetic task would have to evaluate/control
the modular-period comparison and the resulting valuation for varying
g_p. This packet supplies no new reason those global valuations are
bounded. Reproving the rank-one local formula or choosing another
rational frame is not a new uniform bound.

Do not assume one Hida branch across coefficient primes, an etale
weight map, an unramified coefficient ring, or a Taylor coefficient
unit. A success on the ordinary domain leaves supersingular coverage
separate; none is added here. No fixed-prime computation is requested.

No new worker/job is authorized by this historical handoff. The user's
current request governs any continuation.
