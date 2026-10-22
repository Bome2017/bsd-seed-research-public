# Actual seed comparison: a nonzero local target with no global excess

Grade: EXACT BOUNDED COMPUTATION, WITH RETAINED GLOBAL BASIS AND SHA INPUTS.

The sealed scan stopped at the first hit

    coefficient prime p = 5,
    auxiliary good prime q = 1783,
    #E(F_1783) = 1730 = 5 * 346.

Both global basis points have zero image in E(F_1783)/5:

    P1 mod 1783 = (535,1095) = [5](159,1682),
    P2 mod 1783 = (1172,1589) = [5](289,63).

But the local quotient is nonzero. The point R=(3,872) satisfies

    [346]R = (1591,1089) != O,
    [5](1591,1089) = O.

All these are identities on the actual seed reduction, independently verified
with integer modular arithmetic. Exactly 1730 points were enumerated separately.
The first implementation used PARI ellcard/ellmul; the second uses only Python's
standard library, a Legendre-symbol count, explicit point enumeration, and the
Weierstrass group law. Every one of the 47 admitted prime rows up to the first
hit was independently reproduced, including the absence of an earlier hit.
No seed modular symbol, L-value, height or Selmer group was computed.

## Mathematical interpretation

Because E has good reduction at q and 5 != q, multiplication by 5 is an
isomorphism on its formal group. Reduction therefore gives

    E(Q_1783)/5E(Q_1783) ~= E(F_1783)/5E(F_1783) ~= F_5.

The last dimension follows from 5 exactly dividing the finite group order.
The explicit preimages above prove both P1 and P2 have zero local class.
Retaining the saturated rank-two global basis and the rational torsion of order
2, every global point consequently has zero class. Therefore

    (E(Q_1783)/5E(Q_1783)) / image(E(Q)/5E(Q)) ~= F_5.

Nevertheless the separately retained seed certificate says Sha(E/Q)[5]=0.
It follows that the canonical localization detector from Sha[5] to this
one-dimensional target has zero image. Equivalently, the local class represented
by R does not extend to a globally admissible 5-Selmer class. This conclusion
uses the retained Sha certificate; it is not a new proof of that certificate.

This distinguishes two operations which must not be conflated:

1. constructing a local point class outside the global Mordell--Weil image;
2. constructing an ALL-PLACE Selmer class with that local signature.

At the positive control, the supplied explicit Selmer representatives perform
both operations. At this actual seed place, operation 1 succeeds while operation
2 cannot succeed for a nonzero signature, under the retained Sha input.
The missing global admission step is thus visible on the seed itself, rather
than merely an abstract warning about a possible kernel or cokernel.

## Nearby comparison rows

The scan also contains places where the global point image fills the local
quotient. For example:

| q | #E(F_q) | [#E/5]P1 | [#E/5]P2 | dimension of global local image |
|---|---:|---|---|---:|
| 7 | 10 | (5,2) | (5,2) | 1 |
| 67 | 60 | O | (55,6) | 1 |
| 1721 | 1760 | (824,942) | (1151,1393) | 1 |
| 1783 | 1730 | O | O | 0 |

The nonzero quotient at 1783 does not force Sha excess; the zero quotient at the
other listed places does not prove Sha vanishing. The target is local data,
whereas actual image requires global Selmer membership.

## Bound and reproducibility

`SEED_PROBE.md` and `scan.gp` were hashed into `PRE_RUN.sha256` before execution.
The bound was q<=30000, ascending order, good q!=5 and v5(#E(F_q))=1. The first
hit was 1783. `scan.out`/`scan.err` are the raw PARI record. Replaying
`python3 verify_seed_probe.py` independently reproduces `RESULT.json`.

FIN, ORDER9, Q36 and seed coefficient-prime coverage are unchanged.
