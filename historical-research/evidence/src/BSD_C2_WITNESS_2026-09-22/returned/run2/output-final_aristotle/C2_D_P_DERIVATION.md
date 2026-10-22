# One bounded arithmetic derivation: the weighted Gross class `D_p`

**Scope.** Exactly one calculation is attempted here: evaluate

```
        psibar_f(D_p),        D_p = sum_{j=0}^{p-1} j^2 · gamma^j Q_1   in   J ⊗ F_p,
```

for the *actual* traced conductor-`p^2` Gross point `Q_1 = P_1(L)` of the seed, using the actual
Gross-point distribution relations and the Hecke action. The retained identity
`psibar_f(D_p) = -2·c2bar(p)` is used as given, and is re-proved here from BLV's layer-one element.

No route survey, no successor proposal, no large computation, no inference from any cyclotomic
quantity. Machine-checked statements live in `RequestProject/GrossPacket.lean` (builds, no `sorry`,
axioms `propext, Classical.choice, Quot.sound` only) and reuse `RequestProject/C2Witness.lean`.

**Working assumptions as corrected by the instruction.** `mu = 0` is kept in the Iwasawa
equivalences. The former item "M3" (vanishing of `Sha(E/K)` together with `rho_p = 4` as *the*
established equivalent criterion) is withdrawn; regulator valuations remain relevant and are not
used below. Nothing here excludes weighted equidistribution methods. Nothing here demands
polynomial time, nor a polynomial-time algorithm for individual eigenfunctional values. The seed's
reduction at `4547` is type III, so no `I_0^*` quadratic-twist shortcut is invoked; `4547` is a bad
prime and out of scope per `GATE.md` K6 in any case.

---

## 1. Objects, normalization, conductor indices

*(All labels per `GATE.md` K4.)*

| object | normalization | status |
|---|---|---|
| `E/Q`, `N = 2^3·3·2243·4547^2·5843`, `rank E(Q) = 2` | `INPUTS.md` §1 | input (proved, cited there) |
| `K = Q(sqrt -7)`, `h(-7) = 1`, `N^- = 3·2243·5843` (definite), `N^+ = 2^3·4547^2` | `INPUTS.md` §1 | input |
| `B` definite quaternion algebra, Eichler level `N^+`; `X` its Shimura set, Eichler mass `5.42e14` | `INPUTS.md` §1, §3 | input |
| `J = Z[X]` the Gross module, `J ⊗ Z_p` its `p`-adic completion | Gross/BLV | input |
| `psi_f : J ⊗ Z_p -> Z_p`, `psi_f(T x) = f(T) psi_f(x)`, **surjective** | BLV §2.5; surjectivity *is* primitivity, `INPUTS.md` §4 | input |
| `p >= 7`, `p ∤ 7N`, `E` ordinary at `p`; `a_p` the `T_p`-eigenvalue, `alpha` the unit root, `alpha + p/alpha = a_p` | standard | input |
| `Gamma = Gal(K_inf/K)`, `G_1 = Gal(K_1/K) = <gamma> ≅ Z/p`, `t = gamma - 1`, `I = (t)` | `INPUTS.md` §4 | input |
| `P_n(L) = Tr_{K~_{n+1}/K_n} P~_{n+1}(L)`: **layer `K_n` carries conductor `p^{n+1}`** | BLV §2.5 | input |
| `Q_1 := P_1(L)` (conductor `p^2`), `Q_0 := P_0(L)` (conductor `p`), `Q_{-1} := P_{-1}(L)` (conductor `1`) | BLV indexing | input |
| `v_j := psibar_f(gamma^j Q_1) in F_p`, `M_k := sum_{j<p} j^k v_j` | this file | notation |

Throughout, `F_p[G_1] = F_p[t]/(t^p)` with `gamma = 1 + t`, and `N = sum_{sigma in G_1} sigma` is the
trace (norm) element. `epsilon : F_p[G_1] -> F_p` is the augmentation.

---

## 2. The relations, written explicitly

### R1. Vertical trace (distribution) relation — the only relation internal to the tower

```
        Tr_{K_n/K_{n-1}} P_n  =  T_p P_{n-1}  -  P_{n-2}                     (n >= 2)
        Tr_{K_1/K}      P_1   =  T_p P_0      -  c_p · P_{-1}
                c_p = sigma_p + sigma_pbar = 2   if p splits in K   (h(-7) = 1, so both act trivially)
                c_p = 0                          if p is inert in K
```

Conductor indices: the `n`-th relation relates the conductor-`p^{n+1}` point to the conductor-`p^n`
and conductor-`p^{n-1}` points; the displayed bottom case relates conductor `p^2` to conductors `p`
and `1`. `T_p` is the good-reduction Hecke operator at `p` (`p ∤ N`), not `U_p`; the classical
degeneracy shape `(a_ell - sigma_lambda - sigma_lambdabar)` at the bottom is Gross's relation for a
prime split in `K`.

*Identification proved here (not merely quoted).* This is exactly the relation forced by norm
coherence of BLV's elements. Push
`calL_{g,n} = alpha^{-n} sum_{sigma in G_n}(psi_g(sigma P_{n-1}) - alpha·psi_g(sigma P_n))·sigma`
to `Lambda_{n-1}` and group `sigma` over the fibres of `G_n -> G_{n-1}`. Since `P_{n-1}` is defined
over `K_{n-1}`, the first term contributes `alpha^{-n}·p·psi_g(tau P_{n-1})` in the `tau`-coefficient
and the second contributes `alpha^{-(n-1)} psi_g(tau Tr_{K_n/K_{n-1}} P_n)`. Equating with
`calL_{g,n-1}` gives

```
        psi_g( Tr_{K_n/K_{n-1}} P_n )  =  (alpha + p/alpha)·psi_g(P_{n-1}) - psi_g(P_{n-2})
                                       =  a_p·psi_g(P_{n-1}) - psi_g(P_{n-2}),
```

i.e. R1 under `psi_g`, with `alpha + p/alpha = a_p` appearing on the nose. So R1 is not an optional
extra input: it is the compatibility that makes `calL_g` exist.

**Effect on the packet.** `Tr_{K_1/K} Q_1 = sum_{j<p} gamma^j Q_1 = N Q_1`, so R1 is exactly one
`F_p`-linear equation:

```
        M_0 = sum_{j=0}^{p-1} psibar_f(gamma^j Q_1) = a_p·psibar_f(Q_0) - c_p·psibar_f(Q_{-1}).      (R1')
```

### R2. Hecke action at `ell ∤ N p`

`psi_f(T_ell x) = a_ell psi_f(x)`, and the Gross-point relation at an inert `ell` carries a
conductor-`c` point to conductor-`c·ell` points. Applied to `Q_1` it produces conductor-`p^2 ell`
points: these lie outside `J(K_1)`, so R2 relates the packet to *new* unknowns rather than relating
the `v_j` to each other. It supplies no equation on `(v_0, ..., v_{p-1})` alone.

### R3. Going up the tower

`Tr_{K_2/K_1} P_2 = T_p P_1 - P_0` rewrites `a_p psibar_f(gamma^j Q_1)` in terms of layer-2 values;
weighting by `j^2` expresses the target through a weighted sum over `G_2`, i.e. `p^2` unknowns in
place of `p`. Strictly more unknowns, no new equation among the old ones.

### R4. Anticyclotomic involution `iota : gamma -> gamma^{-1}`

`calL^iota = eps·calL`, `eps = ±1`, giving `v_{-j} = eps·v_j` on the packet (the stabilisation term
`alpha^{-1}psi(P_0)·N` is `iota`-invariant, so it does not disturb this).

### R5. Galois equivariance

`gamma` permutes the packet cyclically; this is the indexing already used, not an extra equation.

---

## 3. What the relations do to `D_p`: the group-algebra computation

Work in `F_p[G_1] = F_p[t]/(t^p)`, `gamma = 1+t`. From `(1+t)^p - 1 = t^p` one gets, by
differentiating twice, **exact** identities in `F_p[t]` (`GrossPacket.lean`,
`norm_element_eq_X_pow`, `weight_one_element`, `weight_two_element`):

```
        sum_{j<p}      gamma^j  =  t^{p-1}                                  (the trace element N)
        sum_{j<p}  j · gamma^j  =  -t^{p-2}(1+t)
        sum_{j<p} j^2 · gamma^j  =  t^{p-3}(1+t)(2+t)  =  2t^{p-3} + 3t^{p-2} + t^{p-1}
```

(For `p = 7`: `W_2 = 2t^4 + 3t^5 + t^6`.) Consequently, writing `Y := t^{p-3} Q_1`:

```
        D_p   =  gamma(gamma+1)·Y  =  (1+t)(2+t)·Y ,          (1+t)(2+t) = 2 + 3t + t^2  a UNIT
        N Q_1 =  t^{p-1} Q_1       =  t^2 · Y .
```

(`weightedClass_eq`, `norm_smul_eq`.) So:

* the **target** `psibar_f(D_p)` is `psibar_f` of a unit multiple of `Y`;
* the **only tower-internal relation** R1 evaluates `psibar_f` on `t^2 Y`, two steps further down
  the augmentation filtration.

Moreover the relation cannot be propagated: if `gamma^p = 1` on `J ⊗ F_p`, then for every
`lambda in F_p[G_1]`

```
        lambda · (N Q_1)  =  epsilon(lambda) · N Q_1                        (smul_mul_norm_eq)
```

because `t·N = t^p = 0`. **The `Lambda`-module generated by the distribution relation is the
one-dimensional space `F_p·N Q_1`.** Multiplying R1 by group-algebra elements — the natural way to
try to manufacture a weighted relation — returns R1 up to a scalar. This is the precise mechanism:
every relation available at the layer is an *orbit sum*, so it factors through the augmentation,
i.e. it sees only the `G_1`-coinvariants; `D_p` is a functional on the depth-`(p-3)` piece.

---

## 4. The arithmetic identity actually derived

Collecting (all four items machine-checked in `GrossPacket.lean`, the first also in
`C2Witness.lean`):

```
   (I)   psibar_f(D_p) = M_2 = -2·c2bar(p)                       [retained identity, re-proved from
                                                                  BLV's layer-one element]
   (II)  D_p = (1+t)(2+t)·(t^{p-3} Q_1),   N Q_1 = t^2·(t^{p-3} Q_1)
   (III) M_0 = a_p·psibar_f(Q_0) - c_p·psibar_f(Q_{-1}),   c_p = 2 (p split) / 0 (p inert)
   (IV)  iota-even packet  =>  M_1 = 0 ;      iota-odd packet  =>  M_2 = 0, hence c2bar(p) = 0.
```

Item (IV) is a genuine arithmetic consequence of the derivation and is worth isolating: it gives a
second, independent derivation of the first-moment vanishing (previously taken from the
unconditional Iwasawa lower order), and it shows that `iota`-evenness of the packet, i.e.
`calL^iota = +calL`, is a **necessary condition** for the witness. (At the integral level the same
computation reads: `calL^iota = -calL` forces `2c_2 = 0`, so `c_2 = 0` for odd `p`.) Label:
*identification proved here*; the determination of the sign `eps` for this seed is **not** part of
this derivation and is not claimed.

Item (III) is genuinely closed and cheap: it needs `a_p`, the split/inert behaviour of `p` in
`Q(sqrt -7)` (a Legendre symbol), and `psibar_f` at **two** specific points — the traced
conductor-`p` point `Q_0` and the conductor-`1` point `Q_{-1}`, both defined over `K` since
`h(-7) = 1`. That is two eigenfunctional evaluations, not `p`, and no enumeration of the Shimura
set is implied by the *statement* (whether those two values are themselves accessible is a separate
question that this derivation does not settle).

**But (III) is the zeroth moment, and (I) asks for the second.** The derivation stops here.

---

## 5. Does this produce a closed computation of `psibar_f(D_p)`? — No

Rank count, after imposing R4 with `eps = +1` (the only case in which the witness can be nonzero,
by (IV)). Put `w_j := v_j + v_{-j} = 2v_j` for `1 <= j <= (p-1)/2`. The independent unknowns are

```
        v_0, w_1, w_2, ..., w_{(p-1)/2}          —  (p+1)/2 unknowns,
```

and the relations supply exactly one linear equation on them,

```
        v_0 + w_1 + w_2 + ... + w_{(p-1)/2}  =  M_0   (known, by (III)),
```

while the target is the *different* linear form

```
        M_2 = 1^2·w_1 + 2^2·w_2 + ... + ((p-1)/2)^2·w_{(p-1)/2} .
```

One equation, `(p+1)/2` unknowns, and the target form is not proportional to the constraint form
(for `p >= 7` the weight vectors `(1,1,1,...)` and `(1,4,9,...)` are independent). Formally
(`exists_even_packet_moments`, `exists_even_packet_c2bar`): **for every prime `p >= 7`, every value
`a` of the trace relation and every prescribed value `c` of the witness, there is an `iota`-even
packet with `M_0 = a`, `M_1 = 0` and `c2bar(p) = c`** — realised explicitly by
`v(x) = -a·x^{p-1} + 2c·x^{p-3}` on `F_p`. The relations used are therefore consistent with the
witness being zero and with its being any unit.

This is a statement about *this* calculation: one orbit-sum equation plus a symmetry against a
target that is a functional on a different graded piece. It is **not** an impossibility claim about
weighted equidistribution, about compressed computation, or about any other method; nothing here
excludes those.

### First unknown terms, displayed

For `p = 7` (`eps = +1` assumed), with `w_j = psibar_f(gamma^j Q_1) + psibar_f(gamma^{-j} Q_1)`:

```
        known:    v_0 + w_1 + w_2 + w_3 = M_0 = a_p·psibar_f(Q_0) - c_p·psibar_f(Q_{-1})
        target:         w_1 + 4w_2 + 2w_3 = M_2 = -2·c2bar(7)          (9 = 2 in F_7)
```

The first undetermined quantity is `w_1 = psibar_f(gamma Q_1) + psibar_f(gamma^{-1} Q_1)`, and then
`w_2`. Why the calculation does not determine them: `w_1` is a *difference* of two orbit weights,
and every relation in §2 is either an orbit sum over a full `G_n`-coset — hence annihilated by the
weighting, since it factors through `epsilon` (§3) — or a conductor-changing relation (R2, R3) that
introduces strictly more unknowns than equations. Equivalently, in the filtration language: R1
determines the image of `Q_1` in the degree-`(p-1)` graded piece only, while `w_1, w_2, ...`
and the target live at degree `p-3`.

---

## 6. Returns

**The arithmetic identity actually derived.** Items (I)–(IV) of §4. In one line, the content of the
attempted evaluation is

```
        psibar_f(D_p) = -2·c2bar(p),      D_p = (1+t)(2+t)·(t^{p-3} Q_1),
        and the distribution relation gives only   psibar_f(t^2·(t^{p-3} Q_1))
                                                    = a_p·psibar_f(Q_0) - c_p·psibar_f(Q_{-1}),
        together with:  calL^iota = -calL  =>  c_2(p) = 0.
```

**Remaining inputs.** To close the displayed evaluation one would still need, beyond `a_p`, the
Legendre symbol `(-7/p)`, and the two base values `psibar_f(Q_0)`, `psibar_f(Q_{-1})`: the
`(p-1)/2` even combinations `w_1, ..., w_{(p-1)/2}` of eigenfunctional values at the conductor-`p^2`
packet, of which the relations pin exactly one linear combination. Also unresolved, and not
addressed here: the sign `eps` of the anticyclotomic functional equation for this seed, which by
(IV) must be `+1` for the witness to have a chance.

**Does it enable an executable computation?** No. There is no executable reduction: the derivation
does not produce a computation of `psibar_f(D_p)` from independently accessible data, and it does
not reduce the work below the individual evaluation of `(p-1)/2` eigenfunctional combinations at
conductor-`p^2` Gross points. Consistent with the instruction's standard, nothing here is offered
as a reduction: there is no projector, no abstract quotient, and no proportionality scalar being
smuggled in — the one exact scalar that does appear, `(1+t)(2+t) = 2+3t+t^2`, is a named unit of
`F_p[G_1]` and is proved. Work and storage actually established: the closed part (III) costs `O(1)`
eigenfunctional evaluations plus one Legendre symbol and `a_p`; the open part is `(p-1)/2` further
evaluations, each of unquantified cost, with `O(p)` storage. No statement is made about whether
those evaluations admit compression.

**Exact endpoint consequence and quantifier level.** None. This derivation establishes
`c_2(p) in Z_p^x` at **no** prime, so it reaches **quantifier level 0** in the scale of `TASK.md`
(not level 1 "one prime"). The forward bridge `c_2(p) in Z_p^x => Sha(E/Q)[p^inf] = 0` is untouched
and no dependency error in it was found; no consequence for `Sha` follows from anything above. The
one endpoint-relevant by-product is the necessary condition in (IV): if the seed's
`calL_{f_E}` is `iota`-odd then `c_2(p) = 0` at every `p` in the lane and the universal witness
target fails — this is a conditional statement about a sign that is not determined here, and is
recorded as such, not as a verdict.

No successor proposal is made.
