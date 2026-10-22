# Review of the direct relative-index reconstruction certificate

Date: 2026-10-22. Scope: the proposed identity communicated by the source
agent; the retained `BSD_CLOSED_CLASS_CONSTRUCTION_2026-10-20/theory/COMPLETE_CLASS_BOUND.md`
read in full through its analytic formula; and the current
`sources/check_reconstruction_gate.py` and its output. No genuine seed
unit lattice or new analytic L-value was evaluated in this review.

Verdict: this is a valid sufficient certificate for the five-part of the
complete relative class number. It is not an available or computationally
feasible seed route established by this return. Its crucial arithmetic
inputs are absent.

## Constants and integrality

The retained norm on ordinary class groups is surjective, since the
quadratic extension A/K is ramified at finite primes. Therefore

    h_rel=|ker(Cl(A)->Cl(K))|=h_A/h_K

is a positive integer, not merely a rational class-number ratio. The
retained all-embedding relative logarithm covolume V satisfies

    R_A/R_K=64 V/I,

where I=[U_A:U_K E] is a power of two and I<=128. The constant64 and the
bound128 come from the actual signatures (4,10) and (4,4) and the retained
metric computation; they cannot be reused unchanged in other degrees.

If E0 is a full-rank norm-one unit subgroup with index j=[E:E0] on free
lattices, then V0=j V. With

    T=h_rel R_A/R_K=sqrt(Q) L_K(1,psi)/(2*pi)^6

one obtains exactly

    t=T/(64 V0)=h_rel/(I j).

This avoids the hidden-relation/omitted-generator cancellation in a
partial ideal presentation. It uses the independent number-field analytic
class-number formula, not elliptic BSD.

## Why residue rank six can prove five-saturation

The full relative unit rank is six. Suppose six authenticated norm-one
units give rank six under an actual fifth-power residue map. Then they
span E/E^5 and their lattice index is prime to five. The implicit
injection E/E^5 -> A*/A*^5 is valid: if e=a^5 lies in E, a is a unit,
and N(a)^5=1. The real embedding of K excludes nontrivial fifth roots of
unity, so N(a)=1 and a belongs to E. Torsion +/-1 has no five-part.

A residue matrix on only one faithful character has dimension three and
cannot certify the full rank-six index used here. Both odd character
parts, or the entire relative unit group, must be covered.

## Denominator and interval bounds

The retained V>=V_min gives

    j=V0/V <= V0_upper/V_min_lower.

A certified integer upper J for this ratio yields a denominator bound
D=128 J for the reduced rational t. If the certified ratio interval has
width strictly less than 1/D^2, it contains at most one rational with
reduced positive denominator at most D. Distinct such rationals differ
by at least 1/(bd)>=1/D^2. No numerator bound is needed for this uniqueness
statement. Existence comes from the preceding arithmetic identity, but a
computational certificate must still exhibit or isolate the rational.

If 5 does not divide j, then neither I nor j contributes a five-factor,
and for the isolated reduced rational a/b one has

    v_5(h_rel)=v_5(t)=v_5(a),   5 does not divide b.

A reconstructed denominator divisible by five would therefore fail the
stated saturation/normalization hypotheses, not prove a class value.

## Threshold check and limitations

I independently recomputed the four relative-precision thresholds from
integer fractions: 236,276,316,396 binary bits (72,84,96,120 decimal
places) for the declared hypothetical index bounds J=1,10^6,10^12,10^24.
Each is the smallest ceiling for the code's conservative majorant. This
only checks accuracy requirements once an analytic evaluator and unit
lattice exist. It estimates neither their run time nor their existence.

The checked completed packets contain no authenticated rank-six seed
relative-unit lattice. The previous one-sided Louboutin bound is not a
two-sided enclosure capable of rational reconstruction. The very large
analytic conductor also prevents interpreting modest digit requirements
as a cheap evaluation. No new BNF call, new unit search, Hecke L-value run,
class-number reconstruction, or seed bound was performed by this review.

Consequently this certificate is not a smallness theorem across primes,
and not evidence that the needed arithmetic can currently be executed.
FIN, ORDER9 and Q36 are unchanged.
