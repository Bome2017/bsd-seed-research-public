# Deterministic certificate checker

`check_certificate.py` uses only the Python standard library and exact
integer or `Fraction` arithmetic.  It never calls Sage, Magma, a network
service, or a probabilistic routine.

The version-1 protocol deliberately certifies only a finite replay layer:

- the frozen `TARGET.md` bytes;
- the exact curve constants, both oriented isogeny curve identities, and the
  signed composition `widehat(phi_q) o phi_q = [2]`;
- the complete sixteen-element squareclass ambient group;
- the two claimed target subgroups and their closure;
- an exact `q=13` point-count witness for nonempty signature data;
- every quartic coefficient for that witness, through a canonical digest;
- the full archimedean local-condition row;
- the complete finite bit tables at `2`, `31`, `q`, and outside the support;
- the intersection of those rows, yielding the two frozen target subgroups.

The finite tables use bits `(s,e,f,g)` for
`(-1)^s 2^e 31^f q^g`.  The checker independently replays these predicates:

| place | `phi` | `dual_phi` |
|---|---|---|
| infinity | all | `s=0` |
| `2` | `e=0, s=f` | `e=0` |
| `31` | all | `f=0, s=g` |
| `q` | all | `g=0, e=f` |
| outside `S` | all sixteen global candidates | all sixteen global candidates |

It does **not** promote these finite predicates—or the sample prime—to a
uniform theorem.  The support restriction, Kummer lower bounds, and the
arithmetic proofs identifying the bit tables with the local Kummer images
remain explicit open obligations.  Protocol v1 rejects any certificate that
labels one of these obligations proved without a checker-implemented proof
rule.

Here “all” outside `S={2,31,q}` is relative to the sixteen global
`Q(S,2)` candidates, each an unramified unit class at such a prime.  It does
not assert that the local image is the full group `Q_p*/Q_p*2`.

Run the finite replay:

```sh
python3 checker/check_certificate.py certificates/q13-finite-replay-v1.json
```

Demanding theorem certification currently fails by design:

```sh
python3 checker/check_certificate.py \
  --require-theorem certificates/q13-finite-replay-v1.json
```

Exit status `0` means that the certificate's declared finite scope replayed.
Exit status `2` means malformed, stale, mathematically inconsistent, or
incomplete for the requested theorem scope.

The quartic digest is over ASCII lines in this canonical order:

```text
descent|class_id|d|coefficient_u4|coefficient_u2v2|coefficient_v4
```

first all sixteen `phi` rows, then all sixteen `dual_phi` rows.  Rationals are
reduced and written as `numerator/denominator`; integers have no `/1` suffix.

## Exact base modular-symbol lattice

`exact_base_modular_symbol.gp` separately certifies the load-bearing base
valuation `v2(L(E,1)/Omega_E^+)=-2`.  It does not use PARI's numerically
normalized `msfromell`.  It isolates the `62a` plus Hecke line exactly,
computes its canonical integral lattice with `mslattice`, and combines the
path value `1/2` with the one-real-component lattice formula and the bound
optimality/Manin-constant-`1` row.  See
`evidence/EXACT_BASE_L_VALUE.md` for the normalization proof.

The exact PARI/GP 2.17.4 source archive used for replay is retained at
`evidence/tooling/pari-2.17.4.tar.gz` and bound by SHA-256.  The GP script
sets `recover=0`, so any failed assertion exits nonzero.
