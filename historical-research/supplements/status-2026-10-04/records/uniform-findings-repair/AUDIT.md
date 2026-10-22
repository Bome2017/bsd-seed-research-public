# Review of the October 3 uniform-step findings

**Overall: CONFIRMED_WITH_CORRECTIONS for the surviving restricted lemmas;
the document's global closure conclusion is NOT established.**

This is a focused audit of the load-bearing implications, their domains,
and exact controls. It is not a new audit of the seed's entire release or
an independent source replay of every Hida, Coleman, DFG, or height theorem
mentioned by the workers. Unproved source applications remain unproved.
The original files have not been modified.

## A: the adjoint tangent and its pairing

What survives: for an actual F_p-linear self-extension of V, its connecting
map delta:H^1(V)->H^2(V) gives

    dim H^2(M)=2 dim H^2(V)-rank(delta).

The alternating sign of the trace-zero self-dual extension on the strict
domain is consistent with the standard duality sign rule. Alternation by
itself supplies no dimension bound on the excess. Those statements do not
prove the claimed universal failure of deformation methods.

Corrections:

1. L3's extension to a pairing on full Selmer groups for **ANY** lifting
   Selmer structure is not justified. A compatible exact triangle and
   dual local conditions must be supplied. The global cup/PT map on its
   stated strict right-hand domain does not by itself supply that triangle.
2. L5 treats Z_p/p^2 as an F_p-linear tangent ring. It has characteristic
   p^2, not p, and is not F_p[epsilon]/epsilon^2. A comparison of two
   mod-p^2 representations is not obtained by writing `(T_g-T_E)/p`
   without a chosen compatible lattice comparison. The asserted Flach =
   adjoint + cyclotomic decomposition is not proved by this calculation.
3. In a ramified coefficient ring, a uniformizer direction need not be a
   weight direction. The proposed supersingular replacement does not
   establish the required Coleman tangent or its nontriviality. The lane
   has not earned ordinary-and-supersingular coverage from that sentence.
4. The L9 reduction to SURJ plus RANK is too strong. Put d=dim Sel_p and
   epsilon=rank loc_p on full Selmer. Then h=dim H^2(V)=d-epsilon and
   0<=rank(delta)<=h. If epsilon=1 and d=2, h=1 and
   2h-rank(delta)<=2 even when delta has rank zero. If d>=4, h>=3 and
   the inequality is impossible. Thus on epsilon=1 the dimension criterion
   is already equivalent to primary vanishing, without surjectivity.
5. At p=5 the generic Hasse argument needs the separate count #E(F5)=8.
   Also reduction gives an injection on rational p-torsion, not the
   unqualified equality E(Q_p)[p]=E(F_p)[p] printed in L1.

An alternating form on a larger space can satisfy the known restrictions;
that is a countermodel to deduction from those restrictions, not to an
additional arithmetic identity.

## B: heights and secondary operations

The arithmetic calculation has a useful, narrower meaning. It evaluates
the cyclotomic height of the TWO KNOWN POINTS and the line

    L = W intersect ker(loc_p),       W=E(Q)/p.

It does not calculate an unknown basis of the full strict Selmer group.
When localization of W has rank one, the exact sequence is

    0 -> L -> S0 -> Sha[p] -> 0.

Calling L all of S0 at unsettled primes assumes away the very excess under
investigation. The ranks of localization on W and on full Selmer must also
be distinguished outside this rank-one case.

The preserved numerical claim is: the displayed PARI-normalized height on
L is nonzero in the 40 good ordinary samples through 200. At p=17 the full
2x2 point-height matrix is singular modulo p, while its restriction to L
is nonzero. Thus even the numerical phrase 'nondegeneracy at every prime'
requires a specified domain. Primes 19 and 59 in the sample are outside
the lane's stated Bstar domain. No finite sample proves a cofinite claim.

The official PARI documentation confirms the ordinary-height combination
used by the code. A fresh precision-12 replay is recorded in checks/. The
separate comparison with a particular integral global Bockstein still has
to be supplied; it is not certified by this numerical replay.

The tensor/Tate-twist obstruction restricts particular coefficient maps.
It does not classify all higher operations. Vanishing after the Weil
contraction does not prove that the tensor-valued cup products needed for
an arbitrary Massey defining system vanish. Nor does one nonzero first
obstruction on L prove that every operation on S0/L is undefined. The
claimed exhaustive conclusion in L6 therefore does not follow.

RELATIVE_PAIRING.md supplies the exact quotient-domain repair and tests a
Schur-complement construction. It obtains no upper bound on Sha[p].

## C: contraction, Fitting ideals, and localization data

The elementary estimate Fitt_i(M) subset J^(d-i), where d is the minimal
generator count, is valid. The original one-index target was explicitly
recorded as equivalent to the endpoint under the retained inputs; this
is not a newly discovered impossibility result.

There is a substantive object mismatch. The retained construction uses

    X=((Sel_{p-infinity}(E/L))^dual)/p,
    X_B=X tensor_{F_p[C_p^r]} F_p[C_p^2],

where L retains ALL r primes of the minimum witness. The original text
expressly says it has not identified X_B with the Selmer dual of the
two-prime subfield. Lane C starts with the latter object instead. Removal
of ramified primes changes local conditions; no descent theorem identifying
these modules was supplied. Its proposed presentation of that replacement
does not settle the arithmetic property S for the original X_B.

The lane's localization table is also unreliable as printed. The script
used independently chosen elliptic-group generators for the two entries
of a row, which need not share a normalization. Its cyclic-p-rank selection
also used the wrong invariant factor. Several completed refuter files had
already caught this; the files are not all merely 'unrefuted'.

I independently checked these diagnostic cases with exact finite-field
group operations, without discrete-log generator choices:

| coefficient p | auxiliary q | projective row |
|---|---|---|
| 3 | 13 | (1,1) |
| 5 | 31 | (1,1) |
| 5 | 941 | (1,3) |
| 5 | 991 | (1,3) |

Thus the pair (941,991) has determinant ZERO modulo 5, contrary to the
claimed nonzero example. The general Kummer/Chebotarev existence proof
from the assembly is not affected. At p=3 this is only a diagnostic
calculation, not an application of an all-good-p>=5 theorem.

Further unaccepted steps: L4's local symbol needs a consistently normalized
Kummer generator; L8 confuses a T^2 characteristic ideal with injectivity
of T. The module k[[T]]/(T) direct_sum k[[T]]/(T) already disproves that
implication. No new global upper bound survives these arguments.

## D: cup-product receivers

The useful lemma survives: if x is locally zero and y is a global class,
then the cup product lies in the locally trivial H^2 group. Poitou-Tate
bounds its image by the corresponding dual strict H^1. The inference
that this forbids every first-order fixed receiver is invalid.

If an independently constructed map X->F[p] were proved injective and F
were fixed finite, then F[p]=0 for almost all p would PROVE X=0 there.
The fact that injectivity would have this consequence is the point of
the proposed method, not a contradiction or an impossibility proof.
The missing injectivity theorem cannot be assumed, but is not ruled out.

Two domain/type corrections are mandatory:

* X=ker L_ab is not automatically contained in S0=ker loc_p. It is a
  complement to W selected by two OTHER places. The explicit adjustment
  in RELATIVE_PAIRING.md is available when loc_p(W) is nonzero.
* For Cartier dual M^*=Hom(M,mu_p), V^*=V by the Weil pairing. V(-1) is
  the LINEAR dual. Accordingly (V tensor W)^*=V tensor W^vee, not the
  unqualified V tensor W^* printed in D. Some special examples have the
  correct answer, but the general formula must be repaired.

The claims about all linear maps are also broader than the tested natural
restriction, cup-product, isogeny, or coefficient maps. A coefficient-Hom
vanishing statement is not a classification of arbitrary arithmetic maps.
The submitted new receiver uses a different restriction construction and
does not contradict the valid cup-product containment.

## Replacement for findings section 6

The four lanes do not show that every uniform proof must make the T^2
coefficient of the cyclotomic p-adic L-function a unit cofinitely. That
criterion can include regulator/primitivity conditions beyond primary
vanishing, is normalization-dependent, and has not been supplied here on
the supersingular domain. It is also distinct from the retained MINIMUM
over tame-character conductors. The latter is an accepted equivalence;
it must not be silently replaced by one fixed cyclotomic direction.

Correct conclusion: these tested operations have not supplied independent
uniform control of the excess. The failures do not rule out first-order
receivers or suitably defined relative higher operations. The known-point
height calculation controls a line, not the excess quotient. A new global
object is one possible source of control; it has not been proved necessary.

The newly supplied receiver is a concrete surviving map. RECEIVER_DESCENT.md
pushes it further: outside Bstar the receiver differs from Sha[p] by at
most one local direction. This is a reverse comparison, not the missing
independent upper bound.

FIN, ORDER9 and Q36 are unchanged.
