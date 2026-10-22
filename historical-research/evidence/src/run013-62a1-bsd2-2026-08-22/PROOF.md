# Run013 proof ledger

The exact theorem is frozen in `TARGET.md`, SHA-256
`b6a4cfa6d63b4c8d598f878d6bdbfa8a29a0b8a5ccba3176db1a6d906b151f6d`.
The symbolic proof and conditional BSD assembly have passed hostile
independent review in `evidence/INDEPENDENT_REVIEW.md`.

## A. Exact setup

- [x] The minimal-model changes of variables and Neron differential scaling
  are proved in `src/curves/MODELS.md`.
- [x] Both rational 2-isogenies, their kernels, signed composition `[2]`, and
  Kummer orientation are proved in `src/isogeny/ISOGENY.md` and replayed by
  the exact checker.
- [x] Both quartic covering families are derived from the selected Kummer
  maps.
- [x] The good-prime unramified lemma and support restriction reduce every
  global class to
  `d=(-1)^s 2^e 31^f q^g`, with `s,e,f,g in F_2`.

## B. Local and global descent

The complete proof is `evidence/DESCENT_DERIVATION.md`.  Its independently
re-derived local images are:

| place | `phi_q` image | dual image |
|---|---|---|
| infinity | both real classes | positive class |
| `2` | `{1,q}` | all unit classes |
| `31` | all four local classes | `{1}` |
| `q` | all four local classes | `{1}` |
| outside `{2,31,q}` | unramified subgroup | unramified subgroup |

Writing `d=(-1)^s 2^e 31^f q^g`, the `phi_q` intersection is
`e=0,s=f`, while the dual conditions have the unique solution
`s=e=f=g=0`.  The four retained `phi_q` classes are global Kummer images of
rational 2-torsion on `E'_q`.  Therefore

\[
 \operatorname{Sel}^{(\phi_q)}(E_q/\mathbf Q)
   =\{1,-31,q,-31q\},
 \qquad
 \operatorname{Sel}^{(\widehat\phi_q)}(E'_q/\mathbf Q)=\{1\}.
\]

The descent uses only `q>0`, `q=5 mod 8`, and `(q/31)=-1`; all literal
fields of the smaller frozen family `F_62` remain in the target.

## C. Full 2-Selmer and Sha

- [x] The exact comparison sequence includes the order-2 kernel term, so
  `#Sel_2(E_q)=4/2=2`.
- [x] Since `E_q(Q)[2]` has dimension one, the Kummer sequence forces rank
  zero and `Sha(E_q)[2]=0`.
- [x] Finiteness from Zhai/Kolyvagin then gives
  `Sha(E_q)[2^infinity]=0`.

The exact sequence is recorded in `src/selmer/EXACT_SEQUENCES.md`.

## D. Analytic and BSD chain

- [x] `F_62` is infinite by the exact `q=13` Frobenius witness and
  Chebotarev argument in `src/curves/F62_INFINITY.md`.
- [x] The exact integral modular-symbol lattice proves
  `v2(L(E,1)/Omega_E^+)=-2`; no decimal reconstruction or numerically
  normalized `msfromell` value is load-bearing.
- [x] The uniform local table is
  `c_2=2`, `c_31=1`, `c_q=2`, with Tamagawa product `4`, conductor
  `62q^2`, and minimal discriminant `-2^4*31*q^6`.
- [x] `E_q(Q)_tors` is exactly `Z/2` and the Neron period normalization has
  no missing factor of two.
- [x] Zhai gives nonvanishing, rank zero, finiteness, and twist valuation
  zero; the proved Selmer theorem then establishes `BSD(E_q,2)`.
- [x] Banwait--Huang Theorem 2.13 supplies the qualified odd-primary
  assembly and hence the strong rank-zero formula.

The last item is a public-preprint-qualified theorem chain, not an
all-published chain.  Full details and source statuses are in `BSD_CHAIN.md`
and `evidence/BSD_BOOKKEEPING_EVIDENCE.md`.

## E. Certificate and review boundary

- [x] The Python certificate replays the frozen target binding, exact curve
  and signed isogeny identities, the `q=13` witness, all 32 quartic rows,
  all 16 squareclasses, local bit predicates, and both intersections.
- [x] All 23 adversarial checker tests pass.
- [x] The source-binding checker verifies all 13 inherited hashes.
- [x] The independent hostile review reports no unresolved material theorem,
  orientation, normalization, or source gap.

The finite JSON certificate intentionally retains seven `OPEN` symbolic
obligations and reports `uniform_theorem_certified=NO`; its
`--require-theorem` negative control exits `2`.  Those labels describe the
machine protocol's scope, not the now-proved conventional theorem.  The
uniform local lemmas are proved in the theorem files and independently
re-derived by the hostile reviewer.

Aristotle remains a separate authorization gate.  No handoff archive has
been created.
