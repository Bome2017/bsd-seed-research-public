# Independent hostile review

Review date: 2026-08-22 (America/Los_Angeles)  
Reviewer role: independent hostile mathematical and certificate reviewer  
Scope: every theorem-bearing note, the certificate and its auxiliary data,
both checkers, the adversarial tests, source bindings, exact base-L-value
evidence, the retained PARI source, and the conditional BSD assembly.  No
Aristotle work was performed.

## Verdict

```text
INDEPENDENT_REVIEW                 = PASS
UNRESOLVED_MATERIAL_THEOREM_GAP    = NONE
UNRESOLVED_ORIENTATION_GAP         = NONE
UNRESOLVED_SOURCE_OVERCLAIM        = NONE
FINITE_CERTIFICATE_REPLAY          = PASS
FINITE_CERTIFICATE_IS_UNIFORM_PROOF = NO
SYMBOLIC_PROOF_REVIEW              = PASS
FINAL_PACKAGE_FREEZE               = PENDING_FINAL_MANIFEST
ARISTOTLE_HANDOFF                  = NOT_AUTHORIZED
```

This `PASS` is for the mathematical proof and source/evidence chain in the
byte versions listed below.  It is not a machine theorem certificate and it
is not a final-manifest attestation.  No material mathematical, orientation,
normalization, or source gap remains in those bytes.

The governance/status synchronization and regenerated test-run transcript
were subsequently re-attested in Section 12.  The only remaining package
operation is to generate and verify the final manifest *after* this updated
review is present.  No theorem-bearing byte may change without a new review.

## 1. Findings-first record

No unresolved P0, P1, or P2 finding remains.

Three adversarial findings arose during review and were corrected by the
author before this verdict.  I re-read and re-executed each corrected version.

1. The first base-value evidence inferred an exact rational value from
   decimals.  A proposed replacement using PARI `msfromell` was also
   insufficient: inspection of the retained PARI 2.17.4 source showed that
   `msfromell` obtains its scale using 64-bit `lfun` values and then calls
   `bestappr(...,2^32)` (`src/basemath/modsym.c`, approximately lines
   3125--3184 and 3338--3345).  I rejected that as an independently exact
   normalization certificate.  The current script does not call
   `msfromell`, `lfun`, `ellperiods`, or `bestappr`; it uses the exact Hecke
   eigenspace and exact integral cohomology lattice described in Section 8.
   The current documentation accurately discloses the discarded numerical
   route.
2. The checker originally allowed JSON integer `1` in boolean family fields
   because Python booleans are integer subclasses.  The current checker uses
   exact type checks, and three adversarial boolean-field cases now fail.
3. The checker originally verified only that each isogeny map landed on its
   target curve.  Squaring the y-coordinate made that insensitive to a sign
   reversal.  The current checker has exact signed, cross-multiplied x- and
   y-composition identities for `[2]`; an adversarial flip of either single
   y-sign fails.

These were real defects in superseded bytes, not waivers.  None is present in
the reviewed bytes.

## 2. Reviewed byte anchors

### Theorem-bearing and governance inputs

| path | SHA-256 |
|---|---|
| `TARGET.md` | `b6a4cfa6d63b4c8d598f878d6bdbfa8a29a0b8a5ccba3176db1a6d906b151f6d` |
| `evidence/DESCENT_DERIVATION.md` | `08f2a668658f60c83709b17df7d2f71ea49f3435e26a92000e9ee3d3face62ec` |
| `src/curves/MODELS.md` | `22f915f3db39096f8a68ef835fcb36a5426670376d5f9a2ba7ea5dec938ae13a` |
| `src/curves/F62_INFINITY.md` | `b20c48fb8fad9010478f882889e5901a1003e570857c3b0a84ec15ae29c86c56` |
| `src/isogeny/ISOGENY.md` | `ce52eae4bdc80abc3236e87e261afa12fe57aed7bbfcaea769ff12f6d7f335d6` |
| `src/infinity/INFINITY.md` | `93bd9335a9e0b4a0be9517f81eed38c59e87985590471df70ee3502dc3b5262f` |
| `src/local_2/LOCAL_2.md` | `fc4ea548d30500db1cedd2b074723184e9d8c4ea0037d98940c4831545252f4a` |
| `src/local_31/LOCAL_31.md` | `a17811c53bdb23f530ec184ddb0d65a2d7199de077121b8a75a5cc8e78f86ba6` |
| `src/local_q/LOCAL_Q.md` | `c419ad1005f26964e00715377fb5718353b95d54b96dd77f79de04b6742b505e` |
| `src/selmer/SUPPORT_AND_GLOBAL.md` | `c35d7c706de723cfac9e7506ac26a51c41f01a33c9abfb6cff872f50efcca9c8` |
| `src/selmer/EXACT_SEQUENCES.md` | `b3c1602c6066503ae845f026c0c2eb74d3abdac03ba7daf62c7e2c2a868c18bd` |
| `evidence/BSD_BOOKKEEPING_EVIDENCE.md` | `61f9a08c44c051a6abe8503b6b4c117334bf97174032258dd2598d3ab83386a3` |
| `BSD_CHAIN.md` | `f767c276c91ea1db332d048a97fda6ea40667bf279762b7a5d26c2e259a15f2a` |
| `PRIOR_ART.md` | `3633d0b17f7e4c83cfa8f4949e01c113f79edfaa63154229ab73722d2414e35b` |

### Machine and provenance layer

| path | SHA-256 |
|---|---|
| `checker/check_certificate.py` | `a14c5b9d3432aa38c43ee96da4149de3bfff243293cd66d77a9daee8531f72f8` |
| `tests/test_checker.py` | `722766bdd04bfc6314614c82263a3979ee82ed196acfc05d42f7b7297f30606e` |
| `tests/run_tests.sh` | `fbfec54ec4817592e6b6d464a19bb0827eadec079ddec468e907c17b98a2cf3c` |
| `certificates/q13-finite-replay-v1.json` | `4d320b7d665da68ffd4f8628b1303adb7914af3d7a97d8d1fd368baffbbb876d` |
| `certificates/q13-quartic-coefficients.txt` | `5d02e484e64936e581fe01eda5a5026e4c026db053fef017ad5cd517262c9c2b` |
| `checker/exact_base_modular_symbol.gp` | `6ed0eb886e8220ab5c4011aa8b37370548867200a948303fd04d3665329d9155` |
| `evidence/EXACT_BASE_L_VALUE.md` | `4028831f688692c16aa394e3d0687613be5c7d340d4a7ed7cc3774f5f64f0e78` |
| `evidence/EXACT_BASE_L_VALUE_RUN.txt` | `af26ef1235c01516627877a1ee0639125c9c24f8a092fcc508be35512d2e2204` |
| `evidence/SOURCE_BINDINGS.tsv` | `8785d8e8bad5ee3a75732d43f69b95151b1bff8dd68da5c0a9c726ccb39bcc54` |
| `evidence/SOURCE_BINDING_CHECK.txt` | `ba3a5167269f5fe380b3778d582ea1b205779b0ba689391fb8f77349ffa4044e` |
| `evidence/CHECKER_AND_TEST_RUN.txt` | `c3d1a79245f84cc9187845aab65e7f3954126eca5107b36b8f2fc2c78ba5c98b` |
| `evidence/tooling/pari-2.17.4.tar.gz` | `02651d99c391007d384b3fadbc20abc6916b77036f9e496c99e9ce8688ca4b53` |

### Closure governance bytes

| path | SHA-256 |
|---|---|
| `PROOF.md` | `42aca37560fb281a213b781e951682c0a7d564883407720b81996c5ef3edaf17` |
| `STATUS.md` | `5f8e37bf0bfd1752150a44168cab5cef41ec114ebe7c88d189fa1528d48601a5` |
| `README.md` | `4418617e39978186fe797e0e06504a06ec6cc82ff08581e828e5ec5addc0af11` |

The target digest agrees with the certificate binding.  The quartic file is
byte-for-byte equal to the checker's independently generated 32-row exact
`Fraction` table.  The retained PARI tarball has the SHA-256 published for
the official 2.17.4 stable source distribution.

## 3. Models, differential, quotient, maps, and orientation

Direct substitution in the long minimal equation verifies

\[
 X=4(u+1),\quad Y=8v+4u+4,
 \qquad
 Y^2=X^3-15X^2+64X.
\]

The inverse is `u=X/4-1`, `v=(Y-X)/8`.  For the twists, replacing `1` by
`q` in the displayed integral model and using `X=4(u+q)` gives

\[
 E_q:y^2=x^3-15q x^2+64q^2x.
\]

The differential calculation is exact:

\[
 \frac{dX}{2Y}=\frac12\frac{du}{2v+u+1}.
\]

Thus the short descent model is nonminimal at 2 and its raw period is not a
Neron period.  The proof chain consistently uses the minimal-model period.

For `y^2=x^3+a x^2+b x`, quotienting by `(0,0)` gives coefficients
`(-2a,a^2-4b)`.  Here `a=-15q`, `b=64q^2`, so

\[
 a^2-4b=-31q^2,
 \qquad
 E'_q:y^2=x^3+30q x^2-31q^2x=x(x-q)(x+31q).
\]

I expanded both displayed rational maps and both signed compositions.  The
maps land on the stated curves and
`widehat(phi_q) o phi_q=[2]` with the displayed y-sign, not its negative.
Independent exact rational-function probes at `(q,x)=(13,1),(13,13),
(29,2),(37,5),(53,-1),(61,3)` gave the same signed duplication formulas.

The orientation is consequently exact:

- `Sel^(phi_q)(E_q)` uses the Kummer x-map on `E'_q`, with exceptional
  value `-31q^2`, hence class `-31`;
- `Sel^(widehat(phi_q))(E'_q)` uses the Kummer x-map on `E_q`, with
  exceptional value `64q^2`, hence the identity.

The two quartics follow by substituting
`x=d u^2/v^2`, `y=dun/v^3`.  Reversing the two Selmer labels would reverse
the middle coefficients and contradict both the maps and the exact checker.

## 4. Support and local images

The discriminants of the short equations are

\[
 \Delta(E_q)=-2^{16}\,31q^6,
 \qquad
 \Delta(E'_q)=2^{14}\,31^2q^6.
\]

At an odd good prime outside `S={2,31,q}`, degree 2 is a unit on the formal
groups.  The finite-field kernel and cokernel both have order 2, so the local
Kummer image is exactly the unramified subgroup.  Equivalently, a global
Selmer class has even valuation there.  The direct covering valuation
argument reaches the same conclusion.  At 2 the separate primitive
valuation argument excludes odd valuation in the phi covering.  Hence the
common ambient group is the 16-element group generated by `-1,2,31,q`; the
sharper supports are

\[
 \phi:\{\pm1,\pm31,\pm q,\pm31q\},
 \qquad
 \widehat\phi:\{\pm1,\pm2,\pm q,\pm2q\}.
\]

I independently re-derived every local image.  The result is:

| place | `phi` Kummer image | dual Kummer image | decisive check |
|---|---|---|---|
| infinity | both real classes | positive class only | the dual quadratic factor has discriminant `-31q^2<0` |
| 2 | `{1,q}` = unit classes `{1,5}` | all four unit classes | primitive parity/mod-16 exclusion; explicit `E_5(Q_2)` x-classes `12,20,28` realize `3,5,7` |
| 31 | all four local classes | `{1}` | rational torsion exhausts phi; `x^2-15qx+64q^2=(x-23q)^2 mod 31`, and `23q` is a square |
| q | all four local classes | `{1}` | rational torsion exhausts phi; `(-31/q)=-1` forces the dual valuation obstruction |
| outside `S` | unramified subgroup | unramified subgroup | good-prime formal-group/cokernel argument |

The 2-adic proof checks all primitive parity cases, including candidates of
odd 2-adic valuation.  The q-adic `k=1` case has residual quadratic
`z^2-15z+64` with nonsquare discriminant `-31`; the `k<=0` and `k>1`
cases reduce to a square unit times `x`.  The analogous 31-adic cases cover
negative, zero, and positive x-valuations.  I found no cancellation or
unexamined valuation stratum.

These are uniform symbolic arguments in `q` using only `q=5 mod 8` and
`(q/31)=-1`.  Sample computations are merely corroborative.

## 5. Global intersections and full 2-Selmer/Sha

Write a global class as

\[
 d=(-1)^s2^e31^f q^g,
 \qquad s,e,f,g\in\mathbf F_2.
\]

For `phi`, the 2-adic condition is precisely `e=0,s=f`; all other named
places accept those candidates.  Its intersection is

\[
 \{1,q,-31,-31q\}.
\]

All four are actual global Kummer images of
`O,(q,0),(0,0),(-31q,0)` on `E'_q`, so the calculation is an equality, not
only an upper bound.

For the dual, the exact conditions are

```text
infinity: s=0
2:        e=0
31:       f=0 and s=g
q:        g=0 and e=f
```

Their unique intersection is the identity.  The checker independently
replays the same 16-row intersections, but the prose valuation proofs above
are what establish their uniform arithmetic meaning.

The isogeny comparison sequence has first term

\[
 E'_q(\mathbf Q)[\widehat\phi_q]/\phi_q(E_q(\mathbf Q)[2]),
\]

of order 2: `E_q(Q)[2]=ker(phi_q)`, so its image is trivial, while the dual
kernel on `E'_q` has order 2.  Exactness therefore gives

\[
 \#\operatorname{Sel}_2(E_q)=4/2=2.
\]

The 2-division quadratic has discriminant `-31q^2`, so
`E_q(Q)[2]={O,(0,0)}`.  The full Kummer sequence then forces rank 0 and
`Sha(E_q)[2]=0`; finiteness supplied by Zhai/Kolyvagin gives
`Sha(E_q)[2^infinity]=0`.  The proof correctly divides by the order-2
kernel term and never multiplies the two isogeny-Selmer orders directly.

## 6. Torsion, local factors, discriminant, and conductor

There is no rational point of order 4: a half of `(0,0)` would have
`x=+/-8q`; at `+8q` the right side is `64q^3`, not a rational square, and
at `-8q` it is negative.  Hence there is no higher 2-power torsion.  Any
odd prime torsion point would give a rational stable line on the base curve
after untwisting.  Mazur reduces this to primes `3,5,7`, and the bound
isogeny-class data show no rational isogeny of any of those degrees.  Thus

\[
 E_q(\mathbf Q)_{\rm tors}\simeq\mathbf Z/2\mathbf Z.
\]

The uniform local calculation is:

| prime | twist reduction | Tamagawa number |
|---:|---|---:|
| 2 | unramified nonsquare twist of split `I_4`, hence nonsplit `I_4` | 2 |
| 31 | unramified nonsquare twist of nonsplit `I_1`, hence split `I_1` | 1 |
| q | ramified twist of good reduction, type `I_0^*` | 2 |

At q the component cubic is `T(T^2-15T+64)`.  Its quadratic discriminant
is `-31`, a nonsquare modulo q, so it has exactly one root and `c_q=2`.
Consequently

\[
 \Delta_{\min}(E_q)=-2^4\,31q^6,
 \qquad N(E_q)=62q^2,
 \qquad \prod_p c_p=4.
\]

The q=13 public local row matches `(c_2,c_13,c_31)=(2,2,1)` and the stated
Kodaira and conductor exponents, but that sample is not used as a uniform
proof.

## 7. The prime family is infinite

The dependency-free enumeration replay gives

```text
#E(F_13)=12
a_13=2
13 mod 8=5
(13/31)=-1
```

Let `K=Q(E[8],sqrt(31))`.  Prime 13 is unramified in K.  Its Frobenius
conjugacy class fixes, for every prime r in that class, the trace and
determinant modulo 8 and the action on `sqrt(31)`.  Thus

```text
r mod 8=5
(r/31)=-1
#E(F_r) mod 8=4
a_r mod 8=2
```

The third line is exactly `v2(#E(F_r))=2`; the last makes `a_r` nonzero.
Chebotarev supplies positive density for the nonempty conjugacy class, and
removing primes dividing 372 is finite.  This proves, rather than samples,
that `F_62` is infinite.

## 8. Exact base algebraic L-value and Zhai

I rebuilt/replayed the retained PARI 2.17.4 source and audited the source
call graph.  The current script performs:

1. `msinit(62,2,1)` and `msnew`;
2. exact `ellap` checks and exact Hecke conditions
   `a_3=0,a_5=-2,a_7=0,a_11=0`;
3. `msfromhecke`, which isolates a one-dimensional rational plus eigenline;
4. `mslattice`, whose implementation evaluates rational symbols and uses
   rational/integer image-HNF operations (`modsym.c`, approximately
   lines 4840--4893);
5. exact `mseval` on `[oo,0]`, yielding the primitive plus-lattice path
   value `1/2`.

The bound row

```text
62 a 1 [1,-1,1,-1,1] 1 1
```

gives the optimal curve and Manin constant 1.  Thus the modular-symbol
lattice `L_f` equals the Neron-period lattice `L_E`.  Since
`Delta_min=-496<0`, `E(R)` has one component, and

\[
 L_E=\mathbf Z(x^+-x^-)+\mathbf Z(2x^-).
\]

Intersecting with the plus line gives exactly `Z*(2x^+)`.  The path value
`1/2` therefore proves

\[
 \left|L(E,1)/\Omega_E^+\right|=1/4,
 \qquad v_2=-2.
\]

The sign is irrelevant for nonvanishing and the 2-adic valuation.  This is
an exact integral-lattice argument; no decimal rationalization and no
numerically scaled `msfromell` output is load-bearing.

Zhai Theorem 1.5 applies exactly: E is optimal, has odd Manin constant,
negative discriminant, nontrivial rational 2-torsion, and nonzero base
L-value; `M=q` is prime to conductor 62 and is 1 modulo 4; and

\[
 v_2(\#E(\mathbf F_q))=2=-v_2(L(E,1)/\Omega_E^+)\ne0.
\]

It follows that `L(E_q,1)` is nonzero,
`v2(L(E_q,1)/Omega^+_{E_q})=0`, and Mordell--Weil and Sha are finite.  The
twist discriminant remains negative, so the full real Neron period is the
same plus period used here.

## 9. BSD at 2 and Banwait--Huang assembly

In rank zero,

\[
 v_2(\#\Sha(E_q)_{\rm an})
 =v_2(L/\Omega)+2v_2(\#E_q(\mathbf Q)_{\rm tors})
  -v_2\!\left(\prod c_p\right)
 =0+2-2=0.
\]

Section 5 gives `Sha(E_q)[2^infinity]=0`; Zhai/Kolyvagin supplies rank
equality and finiteness, and modular symbols supply rationality.  Thus every
clause of `BSD(E_q/Q,2)` in the Banwait--Huang convention is met.

I checked Banwait--Huang v3, Theorem 2.13, against the actual statement:

- E is semistable of squarefree conductor `N=62`;
- for `d=q`, the quadratic-field discriminant is `D=q` and
  `(D,3N)=1`;
- Zhai gives `L(E_q,1)!=0`;
- the preceding calculation gives `BSD(E_q,2)`;
- exact enumeration gives `a_3(E)=0`;
- the isogeny class has no rational 3-, 5-, or 7-isogeny;
- for `p=2`, prime 31 is a multiplicative ramification witness because
  `v_31(Delta)=1`; for `p=31`, prime 2 is a witness because
  `v_2(Delta)=4`;
- q is good ordinary: the family has `a_q!=0` (indeed `a_q=2 mod 8`),
  and Hasse's bound makes this nonzero modulo q.

The theorem therefore supplies all odd-primary formulas and the strong
rank-zero BSD equality once the proved Selmer identities supply the 2-part.
The project correctly labels this a qualified public-preprint assembly.
Banwait--Huang v3 and the named BSTW, CCSS, and Keller--Yin inputs are not
misrepresented as an all-published chain.

## 10. Source and prior-art audit

`python3 checker/check_source_bindings.py evidence/SOURCE_BINDINGS.tsv`
replayed all 13 absolute source paths with zero mismatch.  I also inspected
the bound PDFs/rows for the claims actually used: Zhai Theorem 1.5, the
standard oriented 2-isogeny formulas, the published quadratic-twist local
tables, Banwait--Huang Theorem 2.13 and its publication caveat, the frozen
ecdata row, and the `opt_man` row.

The prior-art language is appropriately limited.  It says no public,
source-complete proof of the exact oriented family descent was located; it
does not claim absolute novelty and expressly preserves the possible
private/unpublished-priority caveat behind the Zhai/Wan/BSTW attribution.
No source is promoted beyond its bound content.

## 11. Executions and certificate boundary

The following were executed against the hashes in Section 2:

| execution | result |
|---|---|
| `./tests/run_tests.sh` | exit 0; 23 tests, 23 pass |
| `python3 checker/check_certificate.py certificates/q13-finite-replay-v1.json` | exit 0; finite replay PASS |
| same checker with `--require-theorem` | exit 2; uniform certification refused |
| `python3 checker/check_source_bindings.py evidence/SOURCE_BINDINGS.tsv` | exit 0; 13 bindings, 0 mismatch |
| PARI 2.17.4 `gp -q -f checker/exact_base_modular_symbol.gp` | exit 0; exact path value `1/2`, exact algebraic value `1/4`, v2 `-2` |
| `python3 src/curves/point_count_62a1.py` | exit 0; projective count 12 and trace 2 |

The 23 tests include malformed schema, duplicate keys, floating values,
integer-in-boolean fields, composite witness, stale target, wrong point
count, incomplete ambient group, orientation reversal, a signed-map flip,
bad quartic data/digests, corrupted local rows, false symbolic promotion,
and theorem-mode fail-closed behavior.

The finite certificate does **not** prove the uniform theorem.  It checks one
finite witness, exact algebraic identities, exact quartic coefficients, and
the intersection of hard-coded finite bit predicates.  Its local rows at
2, 31, q, and outside S are explicitly `TABLE_REPLAYED`; its seven symbolic
obligations are explicitly `OPEN`; `uniform_theorem_certified=NO`; and
`--require-theorem` exits 2.  The uniform support and local-image lemmas are
established by the human-readable symbolic proofs independently re-derived
in Sections 3--5 of this report.  This review must not be cited as formal or
machine verification of those lemmas.

## 12. Closure re-attestation

After the initial PASS, the author synchronized only the governance ledgers
and review-status text, then regenerated the checker/test transcript.  I
audited those changes against the original reviewed hashes.

### Exact theorem-body preservation

| path | prior reviewed SHA-256 | synchronized SHA-256 |
|---|---|---|
| `src/curves/MODELS.md` | `63b3a651bf670c8b11987120ac4a837b056ced526dffa50653c5c630ddcde999` | `22f915f3db39096f8a68ef835fcb36a5426670376d5f9a2ba7ea5dec938ae13a` |
| `src/curves/F62_INFINITY.md` | `0ffd6174897922d81483b64c59c7f4b7368641aab288331e0cb79569699a33b2` | `b20c48fb8fad9010478f882889e5901a1003e570857c3b0a84ec15ae29c86c56` |
| `src/isogeny/ISOGENY.md` | `caa5cd52a93bb118dae0c0fbe1d647e0b231db55412de2307acbad522ca287c5` | `ce52eae4bdc80abc3236e87e261afa12fe57aed7bbfcaea769ff12f6d7f335d6` |
| `src/infinity/INFINITY.md` | `eb0314fd1a18977e3a486ba25b42b049b7f29502e55b022ee410544eae17f9f2` | `93bd9335a9e0b4a0be9517f81eed38c59e87985590471df70ee3502dc3b5262f` |
| `src/local_2/LOCAL_2.md` | `e2a59808ef608f3430b60df20f2938e0a9cb1309e0aee82aa22f82ff32a4cadb` | `fc4ea548d30500db1cedd2b074723184e9d8c4ea0037d98940c4831545252f4a` |
| `src/local_31/LOCAL_31.md` | `1f15fecdb2806c57ef4457ae5dd2b834015b7d10ff2d488995fa8e39de3b9f1d` | `a17811c53bdb23f530ec184ddb0d65a2d7199de077121b8a75a5cc8e78f86ba6` |
| `src/local_q/LOCAL_Q.md` | `1d7b617b50d6999bf165104fe3ff4bcdc980069d130007c7c3361a92b4c60742` | `c419ad1005f26964e00715377fb5718353b95d54b96dd77f79de04b6742b505e` |
| `src/selmer/SUPPORT_AND_GLOBAL.md` | `73e6acf588eb56103d655c1c2845cc974d8ebe9399f4d200bab78b84343b2b18` | `c35d7c706de723cfac9e7506ac26a51c41f01a33c9abfb6cff872f50efcca9c8` |
| `src/selmer/EXACT_SEQUENCES.md` | `391c9d04404083673c0793335d10bacb4edee913617faf81299899449fdb151d` | `b3c1602c6066503ae845f026c0c2eb74d3abdac03ba7daf62c7e2c2a868c18bd` |
| `evidence/DESCENT_DERIVATION.md` | `2e56c1d13750234a5b6844979a2405b9526209409ee99d6c1503ee297db43eed` | `08f2a668658f60c83709b17df7d2f71ea49f3435e26a92000e9ee3d3face62ec` |

For every row, replacing the new PASS/status text with the exact prior
status text reconstructs the prior reviewed digest.  In eight short theorem
files the editor also removed one otherwise empty terminal line; restoring
that single newline completes the same digest reconstruction.  No heading,
statement, equation, hypothesis, argument, conclusion, or source claim
changed.  This is stronger than a visual diff: theorem-body preservation is
byte-for-byte re-established against the original SHA-256 anchors.

I also read the rewritten `PROOF.md`, `STATUS.md`, and `README.md`.  Their
claims agree with the reviewed proof, preserve the public-preprint and
private-priority qualifications, state that the finite JSON certificate is
not a uniform machine proof, and retain `ARISTOTLE_HANDOFF=NOT_AUTHORIZED`.
`CERTIFICATE=PASS` is explicitly scoped to finite replay plus the separate
exact base lattice; it does not promote the seven open machine obligations.

### Replayed closure evidence

Against the synchronized bytes I reran:

- 23/23 adversarial tests: exit 0;
- finite certificate replay: exit 0, `uniform_theorem_certified=NO`;
- theorem-mode negative control: exit 2 as required;
- 13 source bindings: exit 0, zero mismatches;
- exact PARI integral modular lattice: exit 0, path value `1/2`, algebraic
  value `1/4`, and v2 `-2`.

The regenerated `evidence/CHECKER_AND_TEST_RUN.txt` accurately records those
current results and hashes.  Therefore the independent mathematical PASS
remains valid after governance synchronization.

### Remaining final-manifest operation

`MANIFEST.sha256` is intentionally absent at this re-attestation point.  It
must be generated last so that it includes this updated independent review
and every synchronized governance/evidence byte, then verified with a strict
SHA-256 replay.  Until that mechanical step succeeds, the package is not
freeze-ready.  No Aristotle handoff is authorized.
