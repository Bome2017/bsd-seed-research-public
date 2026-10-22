# Independent review of the root's explicit torsion-function experiment

2026-10-18. Reviewed search_direct.gp, CONTRACT.md, all nine direct_*.json metadata/results, and selected resultants. This reviews the root's experiment, not the reviewer's own companion-class proof. It is a same-team independent calculation, not independent certification of the whole BSD project.

## 1. The exact rational norm formula is correct

On a generalized integral Weierstrass equation put

    w=2y+a1*x+a3,
    C(x)=4x^3+b2*x^2+2*b4*x+b6,
    h(T)=w(T)-m*x(T)-b.

Then w(-T)=-w(T), and pairing every nonzero p-torsion point T with -T gives

    h(T)h(-T)=(m*x(T)+b)^2-C(x(T))=:Q(x(T)).

For odd p, the standard division polynomial D=psi_p has degree n=(p^2-1)/2 and leading coefficient p. Its roots are exactly the x-coordinates of these pairs. Thus the product over all nonzero p-torsion points is

    N_A/Q(h)=Res(D,Q)/p^3.                            (1)

Here Q always has degree3 and leading coefficient -4. The script computes

    norm(Mod(D,Q))*leading(Q)^degree(D)=Res(Q,D).

Because n is even, Res(Q,D)=Res(D,Q). Consequently the recorded integer differs from the actual total point-algebra norm by exactly the factor p^3. This factor is supported in S, so it does not affect the S-free support test. No uncomputed rational factor is hidden in that comparison.

The formula is valid for the full torsion-point etale algebra even if it decomposes; irreducibility is not necessary for the total norm identity. Claiming one field rather than the etale algebra would separately require the retained full-image input.

## 2. Support-test scope

Away from p, nonzero p-torsion points have integral coordinates on the integral Weierstrass model: a point with nonintegral coordinates lies in the formal subgroup, where multiplication by p is invertible at residue characteristic different from p. Therefore h is integral at every prime outside S. If its rational norm has no prime factor outside S, every such nonnegative valuation is zero, and h is an S-unit in every etale factor.

Conversely an S-free factor other than1 excludes h itself from being an S-unit. It does not exclude h(T)/h(-T), or its chi projection, because conjugate prime divisors can cancel. The root's contract explicitly keeps this distinction. No result in this bounded scan establishes failure of every projected candidate, failure of every bounded-height rational function, or impossibility of a source construction.

The universal survivor m=b=0 is h=w. Since [-w]=[w] modulo odd pth powers, it is scalar-minus invariant and has zero odd-character projection. Equivalently h(T)/h(-T)=-1 is a pth power. It therefore supplies no faithful odd source direction.

The two further raw S-unit candidates on 37a1 at5 have not, merely through this support screen, been shown to span a faithful character direction or to have nonzero incidence norm. These are separate operations.

## 3. Independent checks

`check_root_resultants.py` constructs psi_p from the standard division-polynomial recurrences using pairs a(x)+b(x)w and w^2=C(x). It does not call PARI or read its division polynomial. It checks degree and leading coefficient and recomputes exact SymPy resultants for36 preselected rows: (m,b)=(0,0),(1,1),(-2,1),(2,-1), on all three curves and p=5,7,11.

All36 match the saved integers exactly. Their printed S-valuations and remaining S-free parts are independently recomputed. ROOT_RESULTANT_REVIEW.json binds the nine source JSON files by SHA256 and records these checks. This is not a replay of every5637 row or any number-field fundamental-unit computation.

The producer's full bounded output has629 seed candidates and625 candidates per control, for each of three primes. Only the trivial raw candidate survives for the seed and389a1. The37a1 pair survives only at5. This supports the scoped conclusion that this particular raw-function search did not supply the missing seed unit directions. Ratios or projected combinations require their own divisor checks.

The error message for a zero resultant says "rational p torsion intersection". Strictly, a zero resultant means the rational line contains a nonzero p-torsion point over the algebraic closure, not necessarily a rational point. No accepted row triggers it; it has no effect on this output. A future general-purpose version should use the precise label.

## 4. Whole-source sufficiency and parity review

For a rank-two curve with no rational p-torsion, an independently authenticated upper bound2 for a containing Selmer space gives Sha[p]=0 directly. This needs no prior primary finiteness; vanishing of p-torsion then rules out every p-power-order element.

An upper bound3 gives only dim Sha[p]<=1. It implies vanishing if the separately retained evenness statement is valid on the claimed prime domain. It is not a consequence of rank2 alone and is not justified by invoking a perfect Cassels--Tate pairing before proving finiteness. Without an evenness premise, a divisible Q_p/Z_p contribution can have p-torsion dimension1. The general certificate correctly makes the parity alternative conditional rather than universal.

For the general class-kernel test, an authenticated complete basis of source p-torsion and actual target class characters gives k<=r-rank M. A presentation of the whole class group surjecting onto it does not automatically give a cover of its p-torsion; the documented Z/p²->Z/p counterexample is relevant. Likewise degree-p target characters need not detect p-torsion lying inside p Cl(B); the higher-order character repair in CROSS_PRIME_CERTIFICATE.md is correct.

A complete basis is not essential to the separate local-image subtraction: once a whole-space upper boundD is independently established, ell independent images of any authenticated elements give kernel dimension<=D-ell. The revised certificate now states this less restrictive version explicitly.

## Verdict

The raw-function norm/support calculation and its scoped negative outcome are supported. It is an actual source-generation experiment at larger primes, not an upper bound on the seed's whole unit or class source. It gives no cofinite bound. The conditional companion structure proved in the parallel class work must be presented separately and retains its source class-completeness hypothesis.
