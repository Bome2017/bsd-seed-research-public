# Independent review of the second-torsion local-exactness packet

Verdict: **CONFIRMED AT RETAINED-INPUT GRADE. NO UNIFORM UPPER BOUND.**

Reviewed on 2026-10-04. The original packet is unchanged. Its 30 manifest
entries verify, and both supplied exact programs reproduce their recorded
JSON outputs. These are integrity and formula controls, not a certification of
the seed's class groups. No novelty or human-referee claim is made.

## Local exactness: confirmed

Serre's printed pp. 273–275 were independently inspected in the scanned paper.
Proposition 11 and its e=1 corollary give the ordinary formal line and the full
cyclotomic inertia character. Proposition 12 explicitly gives the nonsplit
Cartan and, when the residue field does not contain F_(p^2), its full normalizer.
Thus the source supports precisely the Q_p hypotheses used in the packet.

In the ordinary case the construction of a nonidentity scalar is valid even
when the representation is nonsplit: multiply a Frobenius lift by inertia to
make both diagonal entries a, then take the p-th power. Non-anomalous reduction
gives a != 1. Cohomology of the torsion-field group with coefficients E[p]
therefore vanishes. A formal p-division point exists by the height-one formal
group's Weierstrass polynomial. Its translation subgroup is the formal line,
not all of E[p]. Consequently the relevant equivariant Hom has dimension one.

In the supersingular case inertia acts irreducibly, so the nonzero translation
subgroup is all of E[p]. The additional semilinear Frobenius reduces its
centralizer from F_(p^2) to F_p. The local torsion-field group has order prime
to p. Inflation–restriction again gives exactly one kernel direction.

In both cases that direction contains the nonzero Kummer class of R. Since
E(Q_p)/p is one-dimensional, the kernel is exactly the finite local condition.
No assumption on localization of the two global basis points is used.

## Completion and exact global receiver: confirmed with the named imports

The auxiliary point has t(R_p) of valuation one. Writing
P_i = a_i R_p + p S_i over Q_p shows that the chosen completion of L_p equals
Q_p(E[p], Q_3). This is valid also when both a_i vanish modulo p.

For p outside {2,3,19,59,487,2243,4547,5843}, the retained global restriction
kernel, H^2(Gamma_p,E[p])=0, and away-from-p descent checks then prove

    B_p = Hom_Gamma_p(Cl(O_Lp[1/p])/p, E[p]) ~= Sha(E/Q)[p].

In particular the earlier possible local error line is zero. The original
global image, saturation, parity and bad-local-place results remain imports
at their existing grades. This review does not replace them with new seed
certificates or extend the reverse comparison to the excluded primes.

## Support, joint tails and reduction identity: confirmed

Outside the stated polynomial discriminant and ramification exceptions,
theta-n has only degree-one supporting primes in J. The upstairs decomposition
groups lie in H, so their residue degrees divide p-1. The former p-divisible
residue-degree filter cannot remove those generic tails.

The simultaneous tuple argument is valid. The surjectivity onto V^r uses
semisimplicity of the particular direct sum of simple modules, not semisimplicity
of every Gamma-module. A prime with Frobenius (v,h) has relative Artin element
(v,h)^(p-1), with the normalization in the packet. The two reduced tails have
opposite values. Detection of every receiver coordinate does not bound their
number.

One dependency can be weakened: this tuple argument does not need the global
H^2(Gamma,V)=0 theorem. Restrict its class-field extension to H. Since |H|=p-1,
H^2(H,V^r)=0 by averaging, so a complement over H suffices for the same
Frobenius construction. Global receiver exactness still uses its retained
global descent input.

The reduction identity is exactly

    R_pencil = R_product - D(c_((theta-n))).

Its qualification about fixed reductions is necessary and correct. Choosing
different reductions that normalize principal ideals does not retrospectively
make a selected, fixed list of rows redundant.

Coordinate precision: the bound log_2(b) counts valuations in the J factor
base. If a row is expanded in actual L-prime coordinates, extending an ideal
can multiply that count by up to [L:J]=p-1. The safe L-coordinate bound is
(p-1) log_2(b), and twice that for a two-tail row. This does not affect any
identity or rank conclusion, but the two coordinate systems must not be mixed.

## Endpoint assessment

The packet closes a comparison issue. It does not lower the dimension of the
receiver or of the selected-row kernel. Even before this refinement, the
retained at-most-one local error plus parity already made a bound dim B_p<=1
sufficient for primary vanishing. Exactness sharpens what is being bounded;
it does not supply or weaken that bound.

The next documents record actual attempted extensions across the missing
rank/divisibility step, rather than counting this comparison as upper control.

Source: J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des
courbes elliptiques*, Invent. Math. 15 (1972), 259–331, section 1.11.
https://wstein.org/sage_summer/bsd_comp/Serre-properties_galoisiennes_des_points_dordre_fini_des_courbes_elliptiques.pdf

FIN, ORDER9 and Q36 are unchanged.
