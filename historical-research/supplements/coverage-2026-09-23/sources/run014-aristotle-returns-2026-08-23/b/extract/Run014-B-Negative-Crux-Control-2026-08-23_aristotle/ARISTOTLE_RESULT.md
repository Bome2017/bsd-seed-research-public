# RUN014-B — negative crux-contact control: result

Job: `RUN014-B` (negative crux-contact control)
Sole input: `Run014-B-Negative-Crux-Control-2026-08-23.tar.gz`, extracted read-only to
`archive/run014-b-negative-crux-control-2026-08-23/`.
Audit date (UTC): 2026-08-23.

Input verification, run as instructed by the package:

```text
python3 verification/verify_package.py
  {"immutable_inputs":"PASS","initial_package":"NOT_REQUESTED","job_id":"RUN014-B","launch_authorized":false}   exit 0
python3 verification/replay_control.py
  {"adversarial_tests":"PASS","finite_replay":"PASS","test_summary":"OK","uniform_theorem_certified":"NO"}      exit 0
  RUN014_B_CONTROL_REPLAY=PASS
```

Claim labels used below: `PROVED`, `SUPPORTED`, `ASSERTED`, `OPEN`, and for bridges the
five required classes `PROVED_FROM_MECHANISM`, `EXTERNAL_INPUT`, `ASSUMED`,
`CONJECTURAL`, `MISSING`.

Independently machine-checked, sorry-free finite facts extracted from the archive are in
`RequestProject/Run014BFiniteChecks.lean` (builds clean against Mathlib). They certify the
`q = 13` family signature and one elementary group-theoretic step; they certify **no**
uniform statement and **no** analytic statement.

---

## A. Mechanism dependency graph

The supplied mechanism is the frozen Run013 theorem
(`seed/run013/TARGET.md`, SHA-256 `b6a4cf…51f6d`) together with its proof ledger
(`seed/run013/PROOF.md`) and post-theorem chain (`seed/run013/BSD_CHAIN.md`).

Natural coordinates. Base curve `E = 62a1`, short model `E_1 : Y² = X³ − 15X² + 64X`;
for an odd prime `q`,

```text
E_q  : y² = x³ − 15q x² + 64q² x
E'_q : y² = x³ + 30q x² − 31q² x = x(x−q)(x+31q)
φ_q  : E_q → E'_q,  ker φ_q = {O,(0,0)},   φ̂_q ∘ φ_q = [2]
```

Generators: squareclasses `d = (−1)^s 2^e 31^f q^g ∈ Q*/Q*²`, `(s,e,f,g) ∈ F_2⁴`.
Laws: local solubility of the two oriented quartic covers
`C^{(φ)}_{q,d} : n² = d u⁴ + 30q u²v² − (31q²/d) v⁴` and
`C^{(φ̂)}_{q,d} : n² = d u⁴ − 15q u²v² + (64q²/d) v⁴` at each place of `Q`.
Frozen family `F_62`: `q` prime, `q ∤ 372`, `q ≡ 5 (mod 8)`, `(q/31) = −1`,
`v_2(#Ẽ(F_q)) = 2`, `a_q(E) ≠ 0`.

```text
M1  exact models, both isogenies, signed composition [2], Kummer orientation      PROVED (project; finite parts replayed)
M2  support restriction: every class lies in Q(S,2), S = {−1,2,31,q}              PROVED conventionally; OPEN in the machine layer
M3  uniform local images at ∞, 2, 31, q and outside S                             PROVED conventionally; OPEN in the machine layer
M4  intersection ⇒ H_SEL(q):  Sel^{(φ_q)} = {1,−31,q,−31q},  Sel^{(φ̂_q)} = {1}    PROVED conventionally (the frozen theorem)
M5  isogeny–Selmer comparison with the order-2 kernel term ⇒ #Sel_2(E_q) = 2      PROVED from M4
M6  Kummer sequence + E_q(Q)[2] = Z/2 ⇒ rank E_q(Q) = 0 and Ш(E_q)[2] = 0         PROVED from M5
M7  Ш(E_q)[2] = 0 ⇒ Ш(E_q)[2^∞] = 0                                               PROVED from M6 (elementary; see below)
```

Object class produced by `M1–M7`: classes in `H¹(Q, E_q[φ_q])` and `H¹(Q, E_q[2])` cut out
by local conditions at `∞, 2, 31, q`; the finite group `Sel_2(E_q/Q)`; the Mordell–Weil
rank; the `2`-primary part of `Ш`. **All of these are algebraic (Galois-cohomological)
invariants of one prime-twist family of one isogeny class, and in the rank-`0` case only.**

Objects that appear in the chain but are *not produced* by the mechanism (they enter as
inputs, and the mechanism has no map to them):

```text
X1  L(E,1)/Ω(E) for the base curve, v_2 = −2       exact modular-symbol lattice replay (input to X2)
X2  L(E_q,1) ≠ 0 and v_2(L(E_q,1)/Ω(E_q)) = 0      Zhai, Asian J. Math. 20 (2016), Thm 1.5 = arXiv:1409.0231
X3  minimal local data c_2 = 2, c_31 = 1, c_q = 2, torsion Z/2      standard local theory (Tate's algorithm)
X4  odd-primary BSD assembly ⇒ strong BSD for E_q  Banwait–Huang arXiv:2601.16044 Thm 2.13 (public preprint)
```

Note on `M7`: `BSD_CHAIN.md §2` derives `Ш[2^∞] = 0` from `Ш[2] = 0` *plus* Zhai's
finiteness of `Ш`. The finiteness input is not needed — in any abelian group, vanishing of
the `2`-torsion kills all `2`-power torsion. This is machine-checked as
`Run014B.no_two_power_torsion_of_no_two_torsion`. The observation *strengthens* the
mechanism's algebraic self-sufficiency and correspondingly sharpens the negative: after
removing it, **every** remaining external input in the chain is analytic.

## B. Target dependency graph

Official crux (`seed/official/BSD_CRUX.md`, Clay/Wiles): for an elliptic curve `C/Q`, with
`L(C,s) = c (s−1)^r + …`, `c ≠ 0`,

```text
T1  the L-function L(C,s) of C, and its analytic continuation to s = 1 (modularity)
T2  r := ord_{s=1} L(C,s)                              — an analytic invariant
T3  rank C(Q)                                          — an algebraic invariant
T4  r = rank C(Q)   for EVERY elliptic curve C/Q, for EVERY value of r
T5  (refined) leading coefficient c in terms of Ш, regulator, real period, c_p, torsion
```

Control required by the target: an equality of `T2` and `T3` with the quantifier of `T4`.
The crux-bearing object is `T2` — the analytic behaviour of `L(C,s)` at `s = 1` — together
with the universal quantifier. No status label about a family substitutes for it.

## C. Exact intersection of the two graphs

```text
Mechanism ∩ Target  =  { T3 }, restricted to:
      • the single isogeny class 62a, twisted by primes q ∈ F_62;
      • the value rank = 0 only;
      • together with Ш[2^∞], which is an ingredient of T5 but not of T4.

Mechanism ∩ { T1, T2 }  =  ∅.
```

The mechanism contains no `L`-function, no modular form, no modular symbol of a twist, no
automorphic period, no `p`-adic `L`-function, no zeta element, no Heegner point, and no
Euler system. Its only contact with an analytic object anywhere in the archive is `X1`,
the exact `2`-adic valuation of `L(E,1)/Ω_E^+` **for the base curve `62a1`**, which is
computed by an independent modular-symbol lattice replay and consumed as a *hypothesis* of
Zhai's theorem. It is not produced by the descent, and it says nothing about `L(E_q,s)`.

Consequently the mechanism supplies one side of the target equality, on a restricted
family, in one rank. `verification/replay_control.py` reports
`uniform_theorem_certified = NO`, and the certificate itself keeps seven symbolic
obligations `OPEN`, so even that side is machine-certified only at the level of a finite
replay for `q = 13`.

## D–E. Every proposed bridge, with classification

| # | Bridge (as stated or implied by the archive) | Class |
|---|---|---|
| B1 | `H_SEL(q)` + isogeny–Selmer comparison (order-2 kernel term) ⇒ `#Sel_2(E_q/Q) = 2` | `PROVED_FROM_MECHANISM` |
| B2 | `Sel_2 ≅ Z/2` + `E_q(Q)[2] = Z/2` ⇒ `rank E_q(Q) = 0`, `Ш(E_q)[2] = 0` | `PROVED_FROM_MECHANISM` |
| B3 | `Ш[2] = 0` ⇒ `Ш[2^∞] = 0` | `PROVED_FROM_MECHANISM` (archive's extra finiteness input unnecessary) |
| B4 | `L(E_q,1) ≠ 0`, i.e. `ord_{s=1} L(E_q,s) = 0` | `EXTERNAL_INPUT` — Zhai 2016 Thm 1.5; hypotheses: optimal, odd Manin constant, `Δ < 0`, `E[2](Q) ≠ 0`, `L(E,1) ≠ 0`, `ord_2(N_q) = −ord_2(L^{alg}(E,1)) ≠ 0`. Nothing in the descent implies it. |
| B5 | rank equality `ord_{s=1} L(E_q,s) = rank E_q(Q)` for `q ∈ F_62` | `EXTERNAL_INPUT` — it is exactly `B2 ∧ B4`; its analytic half is entirely `B4` |
| B6 | `BSD(E_q,2)`: `v_2(#Ш_an) = 0 = v_2(#Ш[2^∞])` | `EXTERNAL_INPUT` in part — needs `B4`'s valuation statement, the Néron-period normalisation, and the local table `X3` |
| B7 | `BSD(E_q,2)` + hypotheses ⇒ full `BSD(E_q)` (strong rank-zero formula) | `EXTERNAL_INPUT` — Banwait–Huang arXiv:2601.16044 Thm 2.13, whose hypotheses (ii) `L(E_d,1) ≠ 0` and (iii) `BSD(E_d,2)` are *consumed*; it in turn rests on further public preprints (BSTW arXiv:2409.01350, CCSS arXiv:1804.10993, Keller–Yin arXiv:2402.12781) |
| B8 | family `F_62` ⇒ universal quantifier of `T4` over all `E/Q` | `MISSING` — no mechanism-internal quantifier change exists; `F_62` is a congruence-defined set of prime twists of one curve. An infinite verified family is not a reduction of a universal conjecture |
| B9 | rank-`0` case ⇒ ranks `r ≥ 1`, in particular `r ≥ 2` | `MISSING` — the mechanism produces no Heegner point, no derivative of `L`, no Gross–Zagier input; for `r ≥ 2` neither direction is available in the supplied corpus |
| B10 | `2`-converse: `corank_{Z_2} Sel_{2^∞}(E/Q) = 0 ⇒ ord_{s=1} L(E,s) = 0` for the curves at hand | `MISSING` for this case. The only rank-`0` `2`-converse in the corpus, Burungale–Tian arXiv:2506.03465, requires `E` to have **CM**; `62a1` has multiplicative reduction at `2` and `31`, hence non-integral `j`, hence no CM. Skinner arXiv:1405.7294 and W. Zhang (CJM 2014) are rank-one; Castella arXiv:2409.01360 needs `p > 3`; Yan–Zhu arXiv:2412.20078 needs `p > 2` good ordinary. In every case an external Iwasawa/Heegner machinery, not the descent, supplies the analytic conclusion |
| B11 | Selmer-distribution route: `2^∞`-Selmer coranks ⇒ analytic ranks (Smith arXiv:2503.17619) | `CONJECTURAL` / circular — that paper's theorem runs `BSD ⇒ Goldfeld`; extracting analytic ranks from Selmer coranks there presupposes BSD |
| B12 | `H_SEL(q)` itself certified uniformly in `q` by the finite checker | `MISSING` at machine level — the certificate is `scope = finite-replay-only`, keeps `SUPPORT_RESTRICTION`, `KUMMER_LOWER_BOUND_PHI/DUAL`, `LOCAL_2/31/Q_UNIFORM`, `UNRAMIFIED_OUTSIDE_S` as `OPEN`, and `--require-theorem` fails closed. It is `PROVED` conventionally in the proof project, which is what this audit takes as the established mechanism |

Answers to the seven audit questions, in order:

1. The mechanism controls local Kummer images and the resulting `φ`/`φ̂`-Selmer groups —
   finite subgroups of `H¹(Q, E_q[φ_q])` — and, through them, `Sel_2(E_q/Q)`,
   `rank E_q(Q)`, `Ш(E_q)[2^∞]`.
2. The target requires control of `ord_{s=1} L(C,s)` for every `C/Q`, and its equality with
   `rank C(Q)`.
3. No. The mechanism acts on none of `T1`, `T2`; it acts on `T3` only for `q ∈ F_62`.
4. A `2`-adic analytic-to-algebraic comparison for non-CM curves (a `2`-adic `L`-function
   or zeta element with an explicit reciprocity law, or a Waldspurger/Gross–Zagier-type
   formula for this twist family), followed by a rank-`r` generalisation and a universality
   argument.
5. Not proved from the mechanism. Every analytic statement in the archive is imported
   (`B4`, `B7`) or is a hypothesis-side computation for the base curve (`X1`).
6. Yes — silently at three places if the chain were read as crux contact: one isogeny class
   (`62a`), prime twists only with four congruence conditions, and analytic/algebraic rank
   `0` only; the strong formula additionally restricts to a public-preprint-qualified
   odd-primary assembly.
7. Finite verification certifies neither side of any bridge in full. It replays exported
   local bit tables and their intersection for the single witness `q = 13`, and separately
   the base-curve modular-symbol valuation. It does not certify that the bit tables are the
   actual local Kummer images uniformly in `q`, and it certifies nothing about
   `L(E_q,s)`.

## F. First intrinsic blocker

```text
The supplied mechanism contains no object attached to the L-function of a twist. There is
no map, in the mechanism, from Sel^{(φ_q)}(E_q/Q) — equivalently from the local-condition
subgroup Sel_2(E_q/Q) ⊆ H¹(Q, E_q[2]) cut out at ∞, 2, 31, q — to ord_{s=1} L(E_q,s).
The first missing object is a 2-adic analytic–algebraic comparison for a NON-CM curve:
a 2-adic L-function / zeta element with an explicit reciprocity law, or an equivalent
2-converse theorem
        corank_{Z_2} Sel_{2^∞}(E_q/Q) = 0  ⟹  L(E_q,1) ≠ 0,
valid for the non-CM curve 62a1 and its prime twists. In the archive this implication is
not proved: its conclusion is imported wholesale from Zhai (arXiv:1409.0231, Thm 1.5).
```

This blocker precedes, and is independent of, the two further gaps `B8` (family → all
curves) and `B9` (rank `0` → all ranks), either of which would independently prevent the
target from being reached.

## G. Does the mechanism reach the full target?

No. The mechanism establishes an exact algebraic statement — the two oriented isogeny
Selmer groups, hence `Sel_2 ≅ Z/2`, `rank = 0`, `Ш[2^∞] = 0` — for the twists `E_q`,
`q ∈ F_62`. It computes the algebraic side of BSD for that family and nothing else. The
analytic side of every rank equality in the archive is imported from Zhai's nonvanishing
theorem, and the strong formula is imported from a preprint-qualified odd-primary assembly
that consumes both `L(E_q,1) ≠ 0` and `BSD(E_q,2)` as hypotheses. Even at the family level
the mechanism is a consumer, not a generator, of analytic input; at the universal level it
does not touch the crux-bearing object at all.

The archive itself does not claim otherwise: `TARGET.md §5` states that the target "does
not authorize a general BSD proof", `STATUS.md` records `FULL_BSD_ATTEMPT = NO`, and the
replay reports `uniform_theorem_certified = NO`. This audit confirms those scope statements
and locates the first intrinsic obstruction independently.

---

```text
RUN014_B_RESULT = NO_CRUX_BRIDGE

MECHANISM_REACHES_TARGET_OBJECT = NO

EXTERNAL_LOAD_BEARING_BRIDGE_REQUIRED = YES

UNIFORM_THEOREM_ESTABLISHED_FROM_SUPPLIED_EVIDENCE = NO

FINITE_REPLAY_OVERSTATED = NO

FIRST_INTRINSIC_BLOCKER =
  No object attached to L(E_q,s) exists in the mechanism: there is no map from
  Sel^{(φ_q)}(E_q/Q) (or from Sel_2(E_q/Q) ⊆ H¹(Q,E_q[2])) to ord_{s=1} L(E_q,s).
  The missing object is a 2-adic analytic–algebraic comparison for the non-CM curve 62a1
  and its prime twists — a 2-adic L-function / zeta element with explicit reciprocity, or
  equivalently the 2-converse corank_{Z_2} Sel_{2^∞}(E_q/Q) = 0 ⇒ L(E_q,1) ≠ 0 — which the
  archive imports from Zhai arXiv:1409.0231 Thm 1.5 rather than proving.

TARGET_SOLVED = NO

NEXT =
  Construct, for the non-CM curve 62a1 with its rational 2-isogeny, a 2-adic zeta element
  (or Waldspurger-type formula) over the twisting fields Q(√q) linking the 2-descent data
  to L(E_q,1), i.e. prove the p = 2, non-CM, rank-zero converse
  corank_{Z_2} Sel_{2^∞}(E_q/Q) = 0 ⇒ L(E_q,1) ≠ 0 without importing Zhai's theorem.
  This is the first bridge whose absence blocks crux contact; it would still leave B8
  (family → all curves) and B9 (rank 0 → all ranks) open, so it does not by itself
  approach the Millennium statement. No certificate design is authorized in this control.
```
