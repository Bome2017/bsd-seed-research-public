# A relative analytic reconstruction certificate, and its admission test

Date: 2026-10-22. Status: **VALID SUFFICIENT CERTIFICATE DERIVED FROM RETAINED
FIELD INPUTS; NOT ADMITTED BY THE PRESENT SEED DATA.** No new class-group
bound, unit, Hecke L-value, coefficient prime, or BSD endpoint is established.

This is a different certificate from repeating `bnfcertify(B,1)`. It replaces
unknown class-generation and relation indices by an independently saturated
relative unit subgroup and a rigorously evaluated analytic class-number
ratio. Both arithmetic inputs are missing in the checked completed packets.
The derivation below is written mathematics, not kernel-checked formalization.

## 1. Exact field, lattice, and integer factors

Retain the actual seed point field A at coefficient five, degree 24 and
signature (4,10), and K=A^{<tau>}, degree 12 and signature (4,4). Here tau is
scalar -1. Both roots-of-unity groups are {+/-1}. These are not CM fields.
The exact field inputs and the prior proof are copied under `inputs/` with
hashes and original-path provenance in `inputs/BINDINGS.json`.

Let E=ker(N:O_A^* -> O_K^*), including {+/-1}. It has rank six. Use the
all-embedding Euclidean logarithm metric, counting both complex embeddings
separately. Write V for covol(Log E). The retained proof gives

    V > b := 31756,
    R_A/R_K = 64 V / I,
    I=[O_A^*:O_K^* E] is a power of two, 1 <= I <= 128.       (1)

The factor 64 is required. In this metric V_L=sqrt([L:Q])R_L/2^{r_2(L)/2};
the embedded seven-dimensional K-unit lattice scales by 2^{7/2} and is
orthogonal to E. Combining the two signatures gives 64. The bound 128,
rather than 256, uses the fact that two real places become complex: norms
cannot be negative squares there. Thus the norm-image index injects into
O_K^*/({+/-1}O_K^{*2}), of order 2^7.

Finite ramification of A/K implies surjectivity of Cl(A)->Cl(K): in the
compositum with the ordinary Hilbert class field of K, Chebotarev gives a
split prime in every K ideal class. Consequently

    h_rel := h_A/h_K = |ker(Cl(A)->Cl(K))|                 (2)

is an actual positive integer, not an unspecified rational class ratio.
On the five-primary part this kernel is the tau=-1 component, containing
both faithful scalar characters. Its five-primary length bounds each
character's five-rank, but does not separate those characters.

With Q=D_A/D_K and psi the quadratic Hecke character for A/K, the retained
analytic class-number formula gives

    T := sqrt(Q)L_K(1,psi)/(2*pi)^6 = h_rel R_A/R_K.       (3)

All powers of two, roots of unity, and signatures in (1)--(3) are inherited
from, and explicitly checked against, `inputs/COMPLETE_CLASS_BOUND.md`.

## 2. Recovering the five-primary length without class generation

Suppose six explicitly represented relative units generate, with +/-1,
a subgroup E0 of full rank in E. Let

    j=[E:E0],    V0=covol(Log E0)=j V.

Equations (1)--(3) imply the exact rational identity

    t := T/(64 V0) = h_rel/(I j).                         (4)

If E0 is independently five-saturated in E, then 5 does not divide j.
Since I is a power of two, equation (4) proves

    v_5(t)=v_5(h_rel).                                   (5)

This controls the complete relative five-primary group: no factor-base
spanning claim, absent prime-ideal class, hidden relation index, or S-class
quotient is silently omitted. It does require the actual full-rank unit
subgroup and its five-saturation. Five-saturation of an unrelated partial
class presentation would not suffice.

An elementary sufficient saturation test is available. For units
u_1,...,u_6, exhibit auxiliary prime-ideal residue maps away from five
whose matrix on these units has rank six over F_5. Fifth powers have zero
image. The map E/E^5 -> A^*/A^{*5} is injective: if e=a^5 in A, valuations
show a is a unit, and N(a)^5=1 in K. The real embedding of K forces
N(a)=1. Thus a belongs to E. Full residue rank proves the six classes are
independent in E/E^5, hence 5 does not divide j. This is an actual arithmetic
rank test, not an inference from six units merely being nontrivial.

## 3. Rational reconstruction with a proved denominator bound

Take positive rigorous intervals V0 in [V0-,V0+] and T in [T-,T+],
tightening V0- to at least b using the retained lower bound. By
V>b and V0=jV,

    j <= J := floor(V0+/b),    D := 128 J.                (6)

D bounds the denominator of the reduced fraction t. The interval

    I_t = [ T-/(64 V0+), T+/(64 V0-) ]                   (7)

contains t. If

    width(I_t) < 1/D^2,                                 (8)

there is at most one rational in I_t with reduced denominator at most D.
Indeed, distinct a/b and c/d with 1<=b,d<=D differ by at least 1/(bd),
hence at least 1/D^2. This argument needs no numerator bound. Equations
(4) and (6) establish existence; an executable certificate should supply
the candidate reduced rational, its containment, denominator bound, and
five-adic valuation. One should not equate a floating-point approximation
with a rational merely because it is visually near one.

It is enough to know j is prime to five, not to know j, I, or all other
prime factors of h_rel. The denominator bound is still indispensable.
Without five-saturation, (4) gives v_5(t)=v_5(h_rel)-v_5(j), and the unknown
index can conceal the complete primary contribution. If an independently
certified upper bound v_5(j)<=a is available instead of saturation, the same
calculation gives length_5(h_rel)<=v_5(t)+a. The coarse index bound j<=J
alone gives a=floor(log_5 J). Thus saturation is sufficient for exact length,
not necessary for every possible upper-bound certificate. No such actual
unit index or independently stronger bound is supplied here.

## 4. The actual numerical admission gate

The retained input supplies only a one-sided estimate

    L_K(1,psi) <= 1511064551295557957,
    sqrt(Q) < 168960571826943275378497531250215852256375148863032392000001.

The exact outward computation gives T < 4.2*10^72 and V>b=31756.
A simple conservative sufficient precision policy, if the two positive
T,V0 intervals each have width at most epsilon times their respective
lower endpoint, is

    3 epsilon * (4.2*10^72)/(64*31756) < 1/D^2.

These are illustrative, conservative sufficient input precisions. The
unit-index bounds J below have NOT been observed for the seed:

| Hypothetical certified J | D=128J | Sufficient binary digits | Sufficient decimal digits |
|---:|---:|---:|---:|
| 1 | 128 | 236 | 72 |
| 10^6 | 128000000 | 276 | 84 |
| 10^12 | 128000000000000 | 316 | 96 |
| 10^24 | 128000000000000000000000000 | 396 | 120 |

There is also a useful optimistic absolute-L gate for THIS sufficient
reconstruction rule. Even ignoring unit-regulator interval error, the
width in (7) is at least

    sqrt(Q)*width(L)/[64(2*pi)^6 V0+].

Thus (8) requires

    width(L) < 64(2*pi)^6 V0+ / [sqrt(Q) D^2].

Write x=V0+/b>=1. Since x/floor(x)^2<2, the right side is less than

    (2*pi)^6 b/[128 sqrt(Q)] < 9.1*10^-53.                (9)

The checker uses the retained rational pi upper bound and the exact
integer floor of sqrt(Q) to verify the final inequality. Its upper value
is approximately 9.034615265876167*10^-53. This is a necessary precision
gate for the specific sufficient isolation test (6)--(8); it is NOT a
lower bound on all algorithms, proof of computational impossibility, or
assertion that every successful class certificate requires such precision.
The familiar square-root conductor scale here is about 1.69*10^59. No
direct approximate-functional-equation computation has been launched,
and no runtime estimate is being certified.

## 5. Test against the actual stored seed data

The checked completed records do not meet the admission hypotheses:

- The old relative relation family has 80 closed kernel products, all
  +/-1. The later 31-element geometric family has 84 rational-kernel
  products, all 1. Neither supplies a single non-torsion ordinary relative
  unit, much less a rank-six subgroup or its five-saturation.
- The October21 finite Cayley-family search also supplies no admitted rank-six
  relative unit set. A fresh norm-one S-unit whose divisor is nonzero is
  not an ordinary unit and cannot be inserted into V0.
- The retained Louboutin bound is an upper bound for L_K(1,psi), not a
  rigorous two-sided evaluation. It cannot isolate v_5(t). Both a trivial
  and a nontrivial five-primary class group remain compatible with it.
- The seed's earlier `bnfcertify(B,1)` timed out. This note does not rerun
  or rename that computation. A provisional class presentation plus a
  floating-point regulator is not a replacement for the missing inputs.

Therefore this turn has produced a valid sufficient certificate and a
quantified admission failure, not a small class bound or executable cheap
path to one. The pre-existing complete five-primary length ceiling 97 is
unchanged. No uniform bound at larger coefficient primes follows.

## 6. Primary-source relationship and exact replay

[Brauer/norm-relation certification, BFHP, Proposition 4.28](https://arxiv.org/html/2002.12332v4)
uses bounded unit indices, prime-to-p saturation, and numerical isolation
of an exact rational ratio. It additionally assumes a normal extension,
a suitable Brauer relation, and correct smaller-field class information.
Those hypotheses are NOT being imported to certify this seed. Equations
(1)--(9) above instead use the already retained relative class-number
formula; their purpose is to make the independent arithmetic gates exact.
BFHP Propositions 4.6 and 4.8 also give the residue saturation criterion.

[Hofmann--Johnston, Algorithm 14.1](https://arxiv.org/html/2609.15190v1)
uses a regulator lower bound to bound the index of a finite-index unit
subgroup. This supports the type of index accounting in (6); it does not
supply the missing seed units, regulator, or L-value. Its separate fast
unramified-p hypotheses must not be applied at the ramified prime five.

`python3 check_reconstruction_gate.py` checks the copied-input hashes,
all outward rational arithmetic in the precision table and (9), and
small exact rational-spacing controls. Its output is
`RECONSTRUCTION_GATE_CHECK.json`. These checks do not evaluate an L-value,
construct a unit, compute a class group, or authenticate the retained
field construction from scratch. FIN, ORDER9, and Q36 remain unchanged.
