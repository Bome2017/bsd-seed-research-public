# Official Birch--Swinnerton-Dyer crux

Primary source: Andrew Wiles, official Clay Mathematics Institute problem
description, `clay_birchswin.pdf`.

For an elliptic curve `C/Q`, write the Taylor expansion at `s=1` as

```text
L(C,s) = c (s-1)^r + higher-order terms,  c != 0.
```

The Millennium Prize conjecture states:

```text
r = rank C(Q).
```

Thus `L(C,1)=0` if and only if `C(Q)` is infinite. The refined conjecture also
predicts the leading coefficient using `Sha_C`, the regulator, real period,
local factors, and rational torsion.

This control's crux-bearing object is not a status label such as “BSD verified
for a family.” It is the analytic behavior of `L(C,s)` at `s=1` and its
universal equality with the Mordell--Weil rank.

Source bytes:

```text
SHA256(clay_birchswin.pdf) =
c25dc966dd0051a60ac04593aef344d8aa89a51abedccbedadc5dc42099ddc6a
```
