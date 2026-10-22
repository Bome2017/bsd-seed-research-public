# General odd-prime form of the complete analytic bound

This is a symbolic extension of COMPLETE_CLASS_BOUND.md, not a new
number-field computation or an across-prime smallness result. Assume the
same full residual image and point-field construction at an odd prime p,
with complex conjugation acting as diag(1,-1). Put

    A_p=Q(nonzero p-torsion point),
    K_p=A_p^{scalar -1},
    n=p^2-1, m=n/2, d=n/4.

The embedding counts are

    signature(A_p)=(p-1, p(p-1)/2),
    signature(K_p)=(p-1, (p-1)^2/4).

There are (p-1)/2 split real places and (p-1)/2 ramified real places of
K_p in A_p. The unit ranks and their difference are

    r_A=(p^2+p-4)/2,
    r_K=(p^2+2p-7)/4,
    r_A-r_K=d=(p^2-1)/4.

Thus the relative unit lattice is quadratic in p; its dimension six
at p=5 is not a generally linear dimension p+1.

Write

    delta_p=N(d_{A_p/K_p}), Q_p=D_{K_p} delta_p=D_{A_p}/D_{K_p}.

When the explicit positivity gate

    log(delta_p) > (p^2-1) log 2                            (P)

holds, every nontrivial relative norm-one unit has all-embedding
logarithm length at least

    lambda_p=[log(delta_p)-(p^2-1)log2]/sqrt(p(p-1)).

Indeed n coordinates are available and p-1 coordinates vanish at the
ramified real places. Apply the same quadratic discriminant inequality
and Cauchy--Schwarz as in the actual-five proof. Hence its full
d-dimensional relative covolume satisfies

    V_rel >= pi^{d/2} lambda_p^d/[2^d Gamma(d/2+1)].

The norm-unit index is at most 2^{r_K}, using a ramified real place to
exclude a negative square. The metric conversion gives

    R_A/R_K=2^{(r_A-1)/2} V_rel/I
             >=2^{-(p-1)/4} V_rel.

Since (P) implies finite ramification, norm is surjective on ordinary
class groups by the Hilbert-class-field argument. Louboutin's arbitrary
ray-character bound over the degree-m base, combined with the analytic
class-number ratio, therefore gives

    |ker(N:Cl(A_p)->Cl(K_p))| <= B_p,

    B_p = 2^{1+(p-1)/4} Gamma(d/2+1) sqrt(Q_p)
          * [e log(Q_p)/(p^2-1)]^m
          / [pi^{3d/2} lambda_p^d].                      (G)

For p=5, (G) is exactly the formula whose outward evaluation produced
the length bound 97. If (P) fails, this specific shortest-vector bound
does not yield a positive denominator; the formula must not be used.
No general verification of (P), D_{K_p}, or delta_p is claimed here.

Because 2 is invertible modulo p, the anti part of Cl(A_p)[p] is the
norm kernel's p-torsion. The sum of dimensions of **all odd scalar
characters**, including nonfaithful ones, is at most floor(log_p B_p).
For p>5 there can be odd nonfaithful characters; do not identify that
whole sum with only the faithful characters. Each faithful character
has a unit sector of dimension (p+1)/2. Thus before independently
authenticated norm and local conditions, one has the coarse ceiling

    dim(complete faithful Kummer source)
       <= (p+1)/2 + floor(log_p B_p) + valuation allowance.

The previously authenticated unit-norm rank can be subtracted from the
unit term. Class-map and local-condition ranks must be authenticated on
the relevant quotient before subtracting them; ranks from overlapping
conditions cannot be added twice.

This formula quantifies what would have to improve. A useful bound
across p needs both (i) sufficiently strong control of the complete
class term (or a proved class-map rank that cancels it), and (ii) unit
norm rank growing at least linearly with p. Neither requirement is met
by (G) alone. Its square-root conductor factor, degree-m L-value bound,
and growing relative-unit dimension are explicitly present. It is not
a prime-independent finite-support theorem and does not imply FIN.

It nevertheless differs logically from a relation count on a selected
factor base: whenever its discriminant hypotheses are authenticated,
it bounds classes missing from every collected list as well.
