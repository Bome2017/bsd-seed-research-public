# RUN014-C2 — final report

## 0. Return status

```text
RETURN: NO
```

The supplied mechanism does **not** establish the stated target (`TARGET.md`: the strong
Birch and Swinnerton-Dyer conjecture for elliptic curves over Q — item 4 of the enumeration).

Against the four enumerated claims:

| claim | statement | verdict |
|---|---|---|
| 1 | strong BSD formula for the specific twists `E_q`, `q ∈ F_62` | **established**, by the mechanism together with named external theorems, all of which were located and read; two of the three decisive external sources are in `literature/`, one of those is an unpublished preprint |
| 2 | strong BSD formula for **every** quadratic twist of 62a1 | **not established** — first missing implication in §5 |
| 3 | rank equality for **every** elliptic curve over Q | **not established** — nothing in the mechanism bears on it |
| 4 | the full conjecture for every elliptic curve over Q (**the stated target**) | **not established** |

Claim 1 must not be promoted to claim 2, 3 or 4: `F_62` is a set of primes of positive
Dirichlet density (not all primes, not all squarefree twist parameters), and 62a1 is one
curve.  The Lean statement `Run014.seven_not_mem_F62` records the elementary fact that the
family is a proper subfamily.

Preflight: `python3 verification/verify_package.py` exits 0 with
`immutable_inputs: PASS`, `package_result: VALID` (50 manifest entries).  No input file was
edited, deleted or regenerated; everything produced by this run lives under `work/` (plus a
Lean development in the surrounding project, `RequestProject/Run014Audit.lean`).

## 1. Notation

`E = 62a1`, minimal model `y² + xy + y = x³ − x² − x + 1`, `Δ_E = −496 = −2⁴·31`, `N = 62`,
`E(Q)_tors ≅ Z/4` (the point `(1,0)`), `E(Q)[2] ≅ Z/2`, `c_2 = 4`, `c_31 = 1`,
`L^(alg)(E,1) = L(E,1)/Ω_E = 1/4`.

For a prime `q`, `E_q` is the quadratic twist by `q`, with model
`y² = x³ − 15q x² + 64q² x`, and `E'_q : y² = x(x−q)(x+31q)` its `φ_q`-quotient.

```text
F_62 = { q prime : q ∤ 372, q ≡ 5 (mod 8), (q|31) = −1, v_2(#E(F_q)) = 2, a_q ≠ 0 }.
```

## 2. The implication chain for claim 1

Each step is classified `PROVED_FROM_MECHANISM`, `EXTERNAL`, `CONJECTURAL` or `MISSING`.
Detailed evidence per step is in `work/CLAIM_LEDGER.md`; every computation was re-run here
(`work/replay/`), and the finite/elementary steps were machine-checked in Lean.

**S1. Models and isogeny.**  `E_q`, `E'_q`, `φ_q`, `φ̂_q`, the two Kummer coverings and the
support set `S = {2, 31, q}` are as displayed.  → `PROVED_FROM_MECHANISM`
(re-derived; the integral twist model has discriminant `−2⁴·31·q⁶`).

**S2. `Sel^{(φ_q)}(E_q/Q) = {1, −31, q, −31q}` and `Sel^{(φ̂_q)}(E'_q/Q) = {1}`
for every `q ≡ 5 (mod 8)` with `(q|31) = −1`.** → `PROVED_FROM_MECHANISM`.
Independently recomputed with my own everywhere-local-solubility engine for
`q = 13, 29, 37, 53, 61, 181, 197, 229`; the 2-adic exclusion of `−1, 31, −q, 31q`, the
archimedean exclusion, the mod-31 identity and the mod-q root-freeness are machine-checked
(`Run014.phi_local_two_exclusion`, `Run014.dual_real_exclusion`, `Run014.g_sq_mod_31`,
`Run014.g_no_root_mod_q`).

**S3. `Sel_2(E_q/Q) ≅ Z/2`, `rank E_q(Q) = 0`, `Sha(E_q/Q)[2^∞] = 0`.**
→ `PROVED_FROM_MECHANISM` (the isogeny–Kummer exact sequences used are standard descent
theory, i.e. `EXTERNAL` as machinery).  From `dim Sel^φ = 2`, `dim Sel^φ̂ = 0`:
`rank + dim Sha[φ] + dim Sha'[φ̂] = 2 + 0 − 2 = 0`.

**S4. `E_q(Q)_tors ≅ Z/2`, `c_2 = 2`, `c_31 = 1`, `c_q = 2`, `∏_p c_p = 4`,
`Δ_min(E_q) < 0`.** → `PROVED_FROM_MECHANISM` for the statements, with two external inputs
(Mazur's semistable isogeny theorem for odd torsion; Zhai Lemma 4.5 for `c_q`).  All values
were recomputed here; note the missing `mechanism/src/tamagawa/` layer file (`FAILURE_LEDGER`
F3).

**S5. `L^(alg)(62a1,1) = 1/4`, i.e. `ord_2 L^(alg)(E,1) = −2`.** → `EXTERNAL`
(rationality: Manin; the numerical value re-derived here to `0.2500019…`).  The package's own
evidence trail for this number is incomplete (`FAILURE_LEDGER` F2); the value is however
forced independently by the arithmetic of 62a1 under BSD (`#tors = 4`, `c_2 c_31 = 4`,
`#Sha = 1` ⟹ `1/4`) and is reproduced by code calibrated on two curves whose algebraic
L-values are printed in the supplied Zhai paper.

**S6. `L(E_q,1) ≠ 0` and `ord_2 L^(alg)(E_q,1) = 0` for every `q ∈ F_62`.**
→ `EXTERNAL`, **located and read**: Zhai, *Non-vanishing theorems for quadratic twists of
elliptic curves*, `literature/txt/1409.0231.txt`, **Theorem 1.5** (lines 156–162), with
`N_q := 1 + q − a_q` defined in §1.  Hypotheses, all verified here: `E` optimal with odd
Manin constant (S7), `Δ_E < 0`, `E[2](Q) ≠ 0`, `L(E,1) ≠ 0`, `M = q ≡ 1 (mod 4)`,
`(q, 62) = 1`, and `ord_2 N_q = 2 = −ord_2 L^(alg)(E,1)` — the last is exactly the family
conditions `v_2(#E(F_q)) = 2` together with S5.

**S7. 62a1 is optimal with odd Manin constant.** → `EXTERNAL`.  Optimality is Cremona's
labelling/tables; oddness of the Manin constant is unconditional for optimal semistable
curves by Česnavičius, Compositio 154 (2018), as quoted in `2601.16044.txt` §2.5.  Neither
source is inside the package.

**S8. `E_q(Q)` and `Sha(E_q)` are finite and `rank = ord_{s=1} L(E_q,s) = 0`.**
→ `EXTERNAL` (Kolyvagin, with Gross–Zagier), quoted by both Zhai §1 and BSTW Thm 10.12; the
original papers are not in the package.

**S9. The 2-part of the BSD formula for `E_q`.** → `PROVED` from S3–S6.  With `#tors = 2`
and `∏ c_p = 4`, the analytic order of Sha equals the algebraic L-value:
`#Sha_an = L^(alg)(E_q,1)·2²/4 = L^(alg)(E_q,1)` (Lean: `sha_analytic_eq_algebraic_L`), so
`ord_2 #Sha_an = 0` by S6 and `ord_2 #Sha(E_q)(2) = 0` by S3.  They agree.

This step is the one the package exists to supply.  Banwait–Huang record (`2601.16044.txt`
§2.7(2)) that 62a1 is one of four curves in BSTW's Example 1 for which the 2-part was *not*
in fact available from the cited sources — for 62a1 the Cai–Li–Zhai route needs a prime
`p ≡ 1 (mod 4)` with `ord_2 #E(F_p) = 1`, and no such prime exists.  The mechanism's descent
plus Zhai Thm 1.5 (which is the `E(Q)[2] ≠ 0`, `ord_2 N_q = −ord_2 L^(alg)(E,1)` case) closes
precisely that hole.

**S10. Auxiliary conditions on `E`: `a_3(E) = 0`; `E[p]` absolutely irreducible for all odd
`p`; for each `p | 62` a multiplicative prime `≠ p` at which `E[p]` is ramified; `E` ordinary
at `q`.** → `PROVED` here, with Mazur external.  `a_3 = 0`; no rational 3-, 5-, 7-isogeny
(witnesses `ℓ = 5, 3, 5` with `a_ℓ² − 4ℓ` a non-residue mod `p`), Mazur for `p ≥ 11` on the
semistable curve; `v_31(Δ) = 1`, `v_2(Δ) = 4`; `a_q ≠ 0` and `|a_q| < q` give ordinarity.
Irreducibility upgrades to *absolute* irreducibility because for each `p = 3, 5, 7` there is a
prime `ℓ` (`ℓ = 11, 11, 3` respectively) of good reduction with `a_ℓ² − 4ℓ` a nonzero square
mod `p`, so `ρ̄_{E,p}(Frob_ℓ)` has two distinct eigenvalues in `F_p`; a representation whose
image contains a split non-central semisimple element cannot become reducible over an
extension while staying irreducible over `F_p`.  (Replay: `work/replay/isogeny_check.py`.)

**S11. The full BSD formula for `E_q`.** → `EXTERNAL`, **located and read**:
Burungale–Skinner–Tian–Wan, *Zeta elements for elliptic curves and applications*,
`literature/txt/2409.01350.txt`, **Theorem 10.12** (lines 6346–6368): for `E` semistable and
`M > 1` squarefree with `(M,N) = 1`, conditions (i) `L(1,E^{(M)}) ≠ 0`, (ii) the 2-part of
BSD for `E^{(M)}`, (iii) `a_3(E) = 0`, (iv) `E[p]` absolutely irreducible for all odd `p`,
(v) the ramified-multiplicative-prime condition, (vi) ordinarity at primes dividing `M`,
imply the full BSD formula for `E^{(M)}`.  Here (i) = S6, (ii) = S9, (iii)–(vi) = S10.
The same conclusion follows from Banwait–Huang `2601.16044.txt` Theorem 2.13 with the same
inputs, which is an independent packaging of the same literature.

**S12. `F_62` is infinite.** → `PROVED_FROM_MECHANISM` + `EXTERNAL` (Chebotarev).  Witness
`13 ∈ F_62` machine-checked (`Run014.thirteen_mem_F62`, with `#E(F_13) = 12`, `a_13 = 2`);
the Frobenius argument in `K = Q(E[8], √31)` was read and checked.

**Conclusion for claim 1.**  No step is `CONJECTURAL` or `MISSING`.  The chain closes:
for every `q ∈ F_62` — an infinite set — the strong BSD formula holds for `E_q`,

```text
L(E_q,1)/Ω_{E_q}  =  #Sha(E_q) · ∏_p c_p(E_q) / #E_q(Q)_tors²,   rank E_q(Q) = 0,
```

with `Sha(E_q)` finite and `Sha(E_q)[2^∞] = 0`.  Two caveats belong to the verdict rather
than to the mathematics: the decisive odd-part input (BSTW Theorem 10.12) is an unpublished
preprint whose own inputs (Skinner–Urban; Skinner, PJM 283 (2016); Kato; BSTW Cor. 10.2) are
mostly not in the package, and S7/S8 rest on published results that are likewise not in the
package.  A reader who declines unpublished authority should downgrade claim 1 to
`UNRESOLVED`; a reader who accepts it should read claim 1 as established.  Either way the
answer to the stated target is unchanged.

Numerical cross-check of the whole chain: `L^(alg)(E_q,1) = 1.0000…` for
`q = 13, 29, 37, 53, 61`, so the formula predicts `#Sha(E_q) = 1` for these `q`, consistent
with `Sha[2^∞] = 0` from the descent.

## 3. What the mechanism itself proves, stripped of external help

Exactly this: for every prime `q ≡ 5 (mod 8)` with `(q|31) = −1` (the two extra conditions
`v_2(#E(F_q)) = 2` and `a_q ≠ 0` are not used in the descent, as its own assumption ledger
states),

```text
Sel^{(φ_q)}(E_q/Q) = {1, −31, q, −31q},   Sel^{(φ̂_q)}(E'_q/Q) = {1},
Sel_2(E_q/Q) ≅ Z/2,   rank E_q(Q) = 0,   Sha(E_q/Q)[2^∞] = 0,
#E_q(Q)_tors = 2,   ∏_p c_p(E_q) = 4,
```

plus the finite base datum `ord_2 L^(alg)(62a1,1) = −2` and the infinitude of `F_62`.
Nothing analytic about the twists, and nothing about odd primes `p`, is proved inside the
mechanism; both come from the supplied literature.

## 4. Where the mechanism's own reach ends

The mechanism's reach ends at the 2-primary, algebraic side of a single congruence family.
Concretely it ends at S3–S4.  Everything beyond — the non-vanishing `L(E_q,1) ≠ 0`, its
2-adic valuation, and the `p`-part of the BSD formula for odd `p` — is imported.

For the chain to continue *inside* the mechanism, the object that would have to exist is a
`p`-adic Euler-system/main-conjecture input for `E_q` at each odd prime `p` (good ordinary,
good supersingular, multiplicative, and — for `p = q` — additive reduction), together with an
independent computation of the exact algebraic L-value `L(E_q,1)/Ω_{E_q}`.  The package
contains none of this; it borrows all of it from `2409.01350`.

## 5. The first precise missing implication (claims 2, 3, 4)

**Claim 2 (all quadratic twists of 62a1).**  The first missing implication is

> for an arbitrary squarefree `d` coprime to 62, `rank E_d(Q) = 0` and `Sha(E_d)[2^∞] = 0`,
> and `ord_2 L^(alg)(E_d,1) = 0`.

This is `MISSING`, and not merely unproved: it is false as stated for general `d`, since
infinitely many twists have odd analytic rank (root number `−1`) and hence rank ≥ 1 under
BSD, and twists of rank ≥ 2 are expected.  The mechanism's local computations consume the
congruences `q ≡ 5 (mod 8)` and `(q|31) = −1` at the places `2`, `31`, `q` (they are what
force `Sel^{(φ̂_q)} = {1}`), and Zhai Theorem 1.5 consumes `ord_2 #E(F_q) = 2` together with
prime `M`.  Drop any one of these and neither half of the argument survives.  For a twist of
analytic rank 1 one would need a Heegner-point/Gross–Zagier–Kolyvagin input plus a rank-one
`p`-part theorem; for analytic rank ≥ 2 even the finiteness of `Sha(E_d)` is open.  The
object that would have to exist: an unconditional determination of `rank E_d(Q)`,
`#Sha(E_d)` and `L^{(r)}(E_d,1)` for arbitrary `d` — i.e. BSD for the full twist family.

**Claim 3 (rank equality for every elliptic curve over Q).**  `MISSING` in the strongest
sense: no ingredient of the mechanism refers to any curve other than 62a1 and its twists.
The known unconditional results reach analytic rank ≤ 1 (Gross–Zagier, Kolyvagin) plus
`p`-converse theorems; the mechanism adds nothing outside its family.

**Claim 4 (the stated target).**  `MISSING`; it is the open Clay problem.  Even for the
single curve family treated here the odd-`p` part is imported from an unpublished preprint.

## 6. Machine-checked artifacts produced by this run

* `work/replay/base_lvalue.py` — independent recomputation of `L(62a1,1)`, the real period
  and their ratio (calibrated on X0(11) and 37B1).
* `work/replay/descent_replay.py` — independent everywhere-local-solubility engine and
  recomputation of both isogeny Selmer groups for all family primes `q < 250`.
* `work/replay/twist_data.py` — integral twist models, `Δ_min`, `a_2`, `a_31`, Tamagawa
  numbers, torsion bounds, and `L^(alg)(E_q,1)` for `q = 13, 29, 37, 53, 61`.
* `work/replay/isogeny_check.py` — absence of rational 3-, 5-, 7-isogenies on 62a1.
* `RequestProject/Run014Audit.lean` (Lean 4 + Mathlib, builds with no `sorry`; axioms
  `propext, Classical.choice, Quot.sound`) — the family witness `13 ∈ F_62`, the mod-16
  exclusion of the four `φ`-classes, the archimedean exclusion, the mod-31 and mod-`q`
  algebraic inputs, the absence of rational 4-torsion, the 2-part bookkeeping identity, and
  the scope marker `7 ∉ F_62`.
