# Independent review of the proposed uniform primitive-divisor calculation

2026-10-20. Same-team mathematical review, not a formal certificate. The
seed's reduction types and retained local representation theorems are
inputs. This review does not recertify those input computations.

**Verdict: the proposed deduction is supported under those inputs.** It
removes the primitive S-divisor term on the stated cofinite domain. It does
not remove the ordinary class kernel or bound the ordinary unit norm rank.

Write `V=E[p]`, and use the actual point/covector incidence correspondence
`lambda(v)=1`. Work in the faithful scalar component `chi(a)=a`, with inverse
character on the covector side. The integral character projector exists
over `Z_p`, since the scalar group has order `p-1`.

## 1. Multiplicative places

For `q != p` with multiplicative reduction and `p` prime to the minimal
discriminant valuation, inertia is the full transvection group of order p.
In a suitable basis it acts by

    (x,y) -> (x+t*y,y).

Its point orbits comprise:

- the p-1 formal fixed points `(x,0)`, indexed by nonzero x;
- the p-1 off-formal orbits of size p, indexed by nonzero y.

The covector action is contragredient. Its fixed orbits are `(0,b)`,
indexed by nonzero b, and its size-p orbits are indexed by nonzero first
coordinate a.

For a primitive prime-divisor coefficient, the incidence entry is

    e(target)/e(source) * number of incident source points in its orbit.

The ramification factors are essential. On the nontrivial scalar
components, this gives exactly:

    formal point channel -> nonfixed covector channel: p * inversion;
    off-formal point channel -> fixed covector channel: inversion.

The cross term is the sum of a nontrivial character over `F_p^*`, hence
zero. Inversion identifies chi with its inverse. Thus the two integral
channels have factors p and 1, up to units; this is not merely a mod-p rank
calculation.

Let epsilon be +1 for split reduction and -1 for nonsplit reduction.
Frobenius is `epsilon*diag(q,1)` modulo inertia. It acts on the two point
channels by `epsilon*q` and `epsilon`. The p-channel survives decomposition
invariants exactly when

    epsilon*q = 1 mod p, equivalently p divides q-epsilon.

The unit channel survives exactly when epsilon=1. Its index is zero.
The source and target character conditions match by the contragredient
action. Consequently

    t_D,chi(q) = 1 if p divides q-epsilon, and 0 otherwise.

No additional p-index is introduced by the invariant projection here:
after inertia is taken, the relevant orbit action factors through
prime-to-p scalar multipliers.

For the retained seed data:

    q=3:    epsilon=-1, v_q(Delta_min)=2, q-epsilon=4;
    q=2243: epsilon=+1, v_q(Delta_min)=1, q-epsilon=2242=2*19*59;
    q=5843: epsilon=-1, v_q(Delta_min)=2, q-epsilon=5844=12*487.

Therefore these places give no primitive-divisor defect outside
`{19,59,487}` for p>=5.

## 2. Additive places

At 2, a preliminary description as potentially multiplicative was
incorrect. The actual invariant valuations are `v_2(c4)=4` and
`v_2(Delta)=8`, so `v_2(j)=4`. The curve is potentially good. The wild
`I_1^*` symbol alone must not be used to infer potentially multiplicative
reduction in residue characteristic two.

The repair uses the common geometric inertia action. After potential good
reduction, inertia acts through origin-preserving automorphisms of the
geometric special-fibre elliptic curve. This finite group has order
dividing 24 and acts faithfully on Tate modules away from two. The actual
coefficient-five point field has a single prime above two with ramification
index 24. Its inertia orbit therefore has size 24. The geometric inertia
group has order 24: its reduction at five is injective because its order
is prime to five, and the orbit size is already 24.

In particular it contains a nontrivial involution. An order-two
nonidentity matrix in characteristic-zero `SL_2` is `-Id`; geometrically
the same automorphism is `[-1]`. This is one common inertia automorphism,
not separately chosen incompatible elements for different coefficient
primes. It acts as `-Id` on every Tate module with coefficient p>=5, and
remains nontrivial modulo p. Thus every decomposition orbit has scalar
stabilizer containing -1, and its faithful scalar component is zero.

At 4547, for p different from 4547, the retained type III has tame
potentially good inertia of order four, whose square is `-Id`. The same
argument eliminates its faithful scalar divisor component.

These conclusions require the actual local data and the common
potential-good inertia theorem. They are not consequences of additive
reduction alone. In particular the calculation at two is justified by
`v_2(j)` and the authenticated coefficient-five ramification, not by the
incorrect potentially-multiplicative assertion.

## 3. Coefficient place

At good ordinary p, inertia acts through the full cyclotomic character on
the formal line. The quotient is unramified with Frobenius eigenvalue
alpha. If alpha is not 1 modulo p:

- the nonzero formal orbit has all scalar multipliers in its stabilizer;
- on each nonformal decomposition orbit, combining Frobenius with a
  suitable inertia element realizes scalar multiplication by alpha.

The second assertion remains true for split and nonsplit residual
extensions: inertia has all first-coordinate diagonal multipliers, and
when a transvection is present its parameter corrects the off-diagonal
coordinate. The nontrivial scalar stabilizer eliminates the faithful
character component. This proof should not be shortened to an assumption
that ordinary inertia itself is transitive.

At good supersingular p over `Q_p`, the retained full level-two fundamental
character inertia acts transitively on the nonzero vectors. Again the
faithful scalar divisor component is zero.

For this seed, rational 2-torsion makes `#E(F_p)` even. Hasse's bound
excludes divisibility by p for p>=7: the only possible positive multiples
in the interval would be p or 2p, the former odd and the latter above the
upper endpoint. At p=5 the retained exact count is 8. Hence the necessary
good nonanomalous condition follows on the stated good-prime domain.

## 4. Scope

Combining the places gives

    t_D,chi = 0

for good p>=5 outside `{19,59,487}`, subject to the retained local source
identification. This concerns the finite ramification set S. It is not an
assertion that faithful divisors at all rational primes vanish.

The resulting complete-source upper template is still

    dim K <= ((p+1)/2 - r_U) + k_C,

where `r_U` is an authenticated incidence-norm rank on ordinary units and
`k_C` bounds the full relevant ordinary class-map kernel. In particular,
discarding the class term because the valuation term is zero would be
invalid. The class sector does not disappear in the original seed's
positive-excess coefficient-three example, which is outside this domain.
