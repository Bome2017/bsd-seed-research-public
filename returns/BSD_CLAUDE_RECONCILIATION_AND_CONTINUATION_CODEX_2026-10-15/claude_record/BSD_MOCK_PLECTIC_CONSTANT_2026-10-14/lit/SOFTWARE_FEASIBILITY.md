# Software feasibility: Brandt modules and Gross points (local software, 2026-10-14)

**Short answer.** Sage 10.9 computes Brandt modules for a definite algebra ramified at a single prime q, at any Eichler level M. The 389a1 case (q = 389, M = 1, 33 classes, eigenline from T_2 alone) takes seconds. Each eigenvector coordinate corresponds to a right ideal class that Sage returns as a genuine ideal object supporting arithmetic.

There is no built-in Gross-point map. The direct method, about 70 lines, works and is validated against Gross's formula. It costs about 1.0–1.6 ms per Gross point. It also handles conductors divisible by primes of the Eichler level, including two-prime conductors.

The gaps:
- composite discriminant needs hand-written code (demonstrated, cheap);
- PARI has only building blocks;
- darmonpoints' plectic and quaternionic code requires Magma, which is absent.

Nothing was installed or downloaded, and no file outside `software_tests/` and this note was changed. At most 2 processes ran at once, each under `timeout 600`, with `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`. The machine has 20 logical CPUs and 16 GB RAM.

## 0. Exact commands

```
SAGE=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/sage
PY=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python   # "sage -python" is NOT supported by this conda Sage ("unrecognized arguments: -python"); scripts do `from sage.all import ...`
GP=/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp
cd /Users/bsm/BSD_MOCK_PLECTIC_CONSTANT_2026-10-14/software_tests
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
/usr/bin/time -p timeout 600 $SAGE -c 'print(version())'                                  # t1_version.out
/usr/bin/time -p timeout 600 $PY t2_brandt.py 11 1 11a1                                     # t2_p11_M1.out
/usr/bin/time -p timeout 600 $PY t2_brandt.py 5 11 55a1                                     # t2_p5_M11.out
/usr/bin/time -p timeout 600 $PY t2_brandt.py 37 1 37a1 37b1                                # t2_p37_M1.out
/usr/bin/time -p timeout 600 $PY t2_brandt.py 389 1 389a1                                   # t2_p389_M1.out
/usr/bin/time -p timeout 600 $PY t2b_scaling.py '[[1009,1],[2003,1],[4001,1],[8009,1],[389,2],[389,6],[389,10],[16001,1],[389,30],[32003,1]]' 480   # t2b_scaling.out
/usr/bin/time -p timeout 600 $PY t2c_composite.py 105 105a1                                 # t2c_composite_105.out
/usr/bin/time -p timeout 600 $PY t2d_extra.py                                               # t2d_extra.out
/usr/bin/time -p timeout 600 $PY t3_gross.py '<JSON config>'                                # t3_*.out (configs reproduced below)
/usr/bin/time -p timeout 600 $GP -q -D parisizemax=3500000000 -f < t4_pari_alg.gp          # t4_pari_alg.out
printf '%s\n' '?11' | $GP -q -f                                                            # t4_gp_section11_list.out
```

The `t3_gross.py` configs were:
- **A:** `{"p":11,"M":1,"labels":["11a1"],"gross_formula":true,"auto":{"count":12,"max_absD":400,"characters":true},"jobs":[{"D":-3},{"D":-4}]}`
- **B:** `{"p":37,"M":1,"labels":["37a1","37b1"],"gross_formula":true,"auto":{"count":12,"max_absD":400,"characters":true}}`
- **C:** `{"p":389,"M":1,"labels":["389a1"],"auto":{"count":15,"max_absD":600,"characters":true}}`
- **D (389 towers / large D):** D = -23 with c = 2, 3, 5, 7, 9, 27, 25, 81. Also D = -1559, -6359, -19799, -67031 with c = 1.
- **E:** `p=11, M=3, 33a1`: D = -31, -103, -199 with c = 1, 3, 9, 27.
- **F:** `p=5, M=11, 55a1`: auto D, plus D = -7 with c = 2, 3.
- **G:** `p=11, M=6, 66a1, 66b1, 66c1`: D = -67 with c = 1, 2, 3, 6, 12, 18, 36. Also D = -331 with c = 6, 36.

All scripts and raw outputs are in `/Users/bsm/BSD_MOCK_PLECTIC_CONSTANT_2026-10-14/software_tests/`.

## 1. Version (test 1)

`sage -c 'print(version())'` printed `SageMath version 10.9, Release Date: 2026-05-04` and a DeprecationWarning, in 5.82 s wall. `gp` reports `[2, 17, 3]`. Importing `sage.all` in the env python takes about 2.5–3 s, so the small scripts below finish in about 4 s wall.

## 2. Brandt modules in Sage (test 2)

`BrandtModule(p, M)` gives the free module on right-ideal classes of an Eichler order R of level pM in the algebra ramified at {p, ∞}. Here R = `B.order_of_level_N()` and the classes are `B.right_ideals()`. The discriminant p must be prime; otherwise it raises `NotImplementedError('Brandt modules currently only implemented when N is a prime')`.

`hecke_matrix(l)` uses two algorithms:
- for l ∤ pM, the "direct" algorithm: (l+1) cyclic neighbours per class plus an equivalence test;
- for l | pM, the theta-series ("brandt") algorithm.

| (p, M) | curve(s) | classes h | `right_ideals()` | T_2 | T_29 | eigenline cut by | T_p eigenvalue | wall total |
|---|---|---|---|---|---|---|---|---|
| (11, 1) | 11a1 | 2 | 0.19–0.32 s | 0.007 s | 0.27 s | T_2 alone | +1 = a_11 | 4.1 s |
| (5, 11) | 55a1 | 4 | 0.24 s | 0.013 s | 0.52 s | T_2 alone | +1 = a_5 | 4.9 s |
| (37, 1) | 37a1, 37b1 | 3 | 0.19 s | 0.016 s | 0.43 s | T_2 alone | -1 = a_37 (37a1), +1 (37b1) | 4.8 s |
| (389, 1) | 389a1 | 33 | 0.30 s | 0.16 s | 4.7 s | T_2 alone | +1 = a_389 (T_389: 1.17 s, theta alg.) | 20.2 s |

These checks passed in every case:
- Mass: Σ 1/w_i = (p-1)ψ(M)/12 exactly, where w_i = #O_L(I_i)^×/2 is obtained from the norm-1 theta coefficient. For 389 this is 97/3, with w = (1,…,1,3).
- The class representatives are pairwise inequivalent (exact test).
- The direct and theta algorithms give equal matrices for T_2.
- The Hecke matrices commute.
- T_p is a permutation matrix (the Atkin–Lehner involution W_p).
- The eigenvector satisfies T_l v = a_l v for every good l < 30.

The 389a1 eigenvector, primitive and integral, is
(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0).
The eigenline is cut out in 0.02 s.

**Pairing with ideal classes: yes.**
- Coordinate i is `B.right_ideals()[i]`, a `QuaternionFractionalIdeal_rational` object.
- All of these ideals have right order R; their left orders O_L(I_i) vary, and those are the orders that receive CM embeddings.
- The ideals support `scale(α, left=True)` (αI), `+`, `*`, `conjugate()`, `norm()`, `left_order()`, `theta_series_vector()` and `is_right_equivalent(J, certificate=True)`. The last returns α with αJ = I.

**Convention, which is load-bearing:**
- Sage acts on row vectors (divisors): e_i T = Σ_j T_ij e_j, where T_ij counts the l-neighbours of I_i lying in class j. With W = diag(w_i), the product T·W is symmetric; W·T is not, when the w_i differ.
- The left kernel of T − a_l gives the eigen-divisor v_f. The right kernel gives the eigenfunction φ_f = W v_f; for B(11) these are v_f = (1, -1) and φ_f = (2, -3).
- Gross-point sums must use φ_f. Using v_f would give 0 at D = -15 for 11a1, where L(E^{-15},1) = 0.753 ≠ 0.

**Bad primes and non-squarefree M** (`t2d_extra.out`).
- (11, 9), (5, 4) and (3, 25) work, with mass checks and pairwise inequivalence passing.
- On every p-new rational newform found, `hecke_matrix(q)` for q | pM has eigenvalue a_q(E). That covers 99a–d, 20a, 75a–c, 55a and 66a–c, with eigenvalue 0 where q² | M.
- Old forms show up as stable subspaces of dimension 2–4.

**Scaling** (`t2b_scaling.out`, one process, exact class sets). Times are roughly linear in h. Peak resident memory was about 2 GB, at h ≈ 2300–2700.

| (p, M) | h | `right_ideals()` | first T_l | second T_l |
|---|---|---|---|---|
| (1009, 1) | 84 | 0.64 s | T_2 0.42 s | T_3 0.61 s |
| (4001, 1) | 334 | 1.47 s | 1.73 s | 2.40 s |
| (8009, 1) | 668 | 3.32 s | 3.62 s | 5.06 s |
| (16001, 1) | 1334 | 7.54 s | 7.98 s | 11.75 s |
| (32003, 1) | 2668 | 18.0 s | 19.3 s | 25.9 s |
| (389, 2) | 97 | 0.62 s | T_3 0.84 s | T_5 1.36 s |
| (389, 6) | 388 | 3.70 s | T_5 4.69 s | T_7 6.96 s |
| (389, 10) | 582 | 3.12 s | T_3 3.03 s | T_7 7.46 s |
| (389, 30) | 2328 | 36.5 s | T_7 41.3 s | T_11 73.2 s |

**Composite discriminant** (`t2c_composite_105.out`).
- `BrandtModule(105)` raises `NotImplementedError`.
- `QuaternionAlgebra(105).order_with_level(210)` raises `NotImplementedError('...only ramified at one finite prime')`.
- `maximal_order()` does work: (-7,-15) is ramified at {3,5,7}, and the order's discriminant is 105.
- A hand-written neighbour enumeration of about 40 lines works. It builds J = 11·I + x·O for x with 11 | nrd(x)/N(I), identifies classes with theta series plus `is_right_equivalent`, and runs BFS. It gave 4 classes with mass 4 = (2·4·6)/12, T_11 = [[2,4,4,2],[4,6,2,0],[4,2,2,4],[2,0,4,6]] with charpoly (x-12)·x·(x²-4x-16), and the 105a1 eigenfunction (1,-1,1,-1). Total time 0.38 s.
- Eichler orders in such algebras can be built as O ∩ O_L(J) (shown in PARI below). They are not built into Sage.

## 3. Gross points / optimal embeddings (test 3)

**Built-ins** (`sage.schemes.elliptic_curves.heegner.HeegnerQuatAlg`, reached as `heegner_points(M).reduce_mod(p)`; it uses `BrandtModule(p, M)`):
- `satisfies_heegner_hypothesis(D, c)` requires D fundamental and coprime to pM, p inert, every q | M split, and c squarefree and coprime to pMD.
- `optimal_embeddings(D, c, R)` returns all β of reduced norm |D|c² in R's Gross lattice S⁰ = (Z + 2R)^{tr=0}, via `R.ternary_quadratic_form(include_basis=True)`. It includes non-optimal (non-primitive) β: the docstring's c = 2 example lists 2(i − j − k). Nothing is filtered.
- `heegner_divisor(D)` returns, for each left order, half the number of primitive β. That counts optimal embeddings with ± identified and without unit weights; it took 0.01–0.06 s on B(11) and 0.20 s on B(389).
- `heegner_divisor(D, c > 1)` returns T_c(heegner_divisor(D)). That is not the conductor-c Gross divisor.
- No built-in gives the map Pic(O) → classes or any Galois labels. Kolyvagin-specific methods exist (`kolyvagin_sigma_operator`, `cyclic_subideal_p1`, …) but were not tested.

**Own implementation** (`t3_gross.py`). It works for any order O = O_{Dc²}, including c divisible by primes dividing M, which the built-in excludes.
1. For each left order O_i, take the primitive vectors β of norm |D|c² in S⁰(O_i). Primitive is equivalent to optimal (Gross's lemma). Full counts k_i come from `representation_vector_list`. In fast mode, one β comes from PARI `qfminim` on the ternary Hessian.
2. Fix one primitive β in some O_{i0} and set t = Dc² mod 2 and x = (t+β)/2 ∈ O_{i0}.
3. Represent each class of Pic(O) by a reduced primitive form (A, B, C) of discriminant Dc² (`BinaryQF_reduced_representatives`).
4. Map it to J = A·I_{i0} + (x − (B+t)/2)·I_{i0} = ψ(a)I_{i0}. The script asserts that the right order of J is R and that N(J) = A·N(I_{i0}).
5. Identify J's class by a theta-series prefix, falling back to the exact `is_right_equivalent` when buckets collide. This is rigorous because the class list is complete by the mass check.
6. Character sums Σ χ(a)φ(x_a) are computed for cyclic Pic, with the group law taken from form composition.

**Validation.**
- **Embedding counts (M = 1).** 2·m_i = k_i·u/w_i held for every class and every D and c tested: 14 + 12 + 15 + 6 runs. Here m_i is the multiplicity of class i in one orientation orbit; the conjugate orientation gives the same multiset.
- **Eichler count.** Σ_i k_i u/w_i / h(O) equals 2 for M = 1, 4 for (5, 11) (11 split), 4 for (11, 3) (3 inert, c = 3^n) and 8 for (11, 6) (2 and 3 inert, c = 2^a 3^b), as orientation counts predict.
- **Gross's formula, rank 0.** L(E,1)·L(E^D,1)·√|D| / S_D² is constant, with S_D = Σ_{a ∈ Pic(O_D)} φ_f(x_a):
  - 11a1: 0.740617449382384 over 10 discriminants, relative spread 3e-16. S_D = 0 exactly at D = -47 and -103, where PARI's `lfun` gives L(E^D,1) ≈ 1e-22.
  - 37b1: 1.282721588264931 over 10 discriminants, spread 2e-16. S_D = 0 at D = -23 and -31, where L(E^D,1) ≈ 1e-22.
- **Vanishing, rank ≥ 1.** 37a1: S_D = 0 for all 12 discriminants. 389a1: S_D = 0 for all 15 discriminants with |D| ≤ 103, for conductors c = 2, 3, 5, 7, 9, 25, 27, 81 (D = -23), and for D = -1559, -6359, -19799, -67031 (class numbers 51, 101, 202, 400). The twisted sums for nontrivial characters are mostly nonzero; for D = -1559, -6359 and -19799 and for c = 25 and 81 exactly one character, the trivial one, gives 0.

**Timings.**
- Setup takes 0.4–1.0 s.
- The Gross-point map costs 1.0–1.6 ms per point (≈ 1.2–1.3 ms for large Pic), all classes:

  | case | time |
  |---|---|
  | h(O) = 400 (389a1, D = -67031) | 0.51 s |
  | h(O) = 216 (B(11,6), c = 36) | 0.27 s |
  | h(O) = 162 (389a1, c = 81) | 0.21 s |

- Finding the embeddings is the bottleneck at large |D|c², because it grows like (|D|c²)^{3/2}:

  | method | case | time |
  |---|---|---|
  | all k_i, Sage `representation_vector_list` | B(389), c = 27 | 3.8 s |
  | all k_i, Sage `representation_vector_list` | B(11,6), c = 36 | 84 s |
  | one β, PARI `qfminim` | c = 1, |D| up to 67031 | 0.001–0.24 s |
  | one β, PARI `qfminim` | n = 150903 | 1.6 s |
  | one β, PARI `qfminim` | n = 428976 | 25 s |

**Eichler-level and two-prime conductors** (Bertolini–Darmon-type). These are cases where a prime q | M is inert in K.
- B(11, 3) with 33a1 and B(11, 6) with 66a1, 66b1, 66c1 have no optimal embedding at c = 1 (or c = 2, 3 for level 6). Embeddings appear once every inert q | M divides c: c = 3, 9, 27 and c = 6, 12, 18, 36.
- The map runs at the same per-point speed.
- The full sums over Pic(O_c) vanish there (S = 0) for every curve and c tested. This fits the harmonicity of a q-new eigenfunction: the q+1 edges at a CM vertex form one fibre of Pic. The trivial-character value is therefore not the useful invariant there; derivatives or twisted sums would be needed. Twisted sums were nonzero for many characters.

**Gaps in the own implementation.**
- One run produces one orientation orbit. The other orbits need other starting β or Atkin–Lehner operators.
- Compatibility of embeddings across conductors (x_n ↦ x_{n-1}, which norm-compatible theta elements need) is not implemented. The standard fix is to fix ψ once and walk ℓ-neighbours, which also avoids the (|D|c²)^{3/2} enumeration.

## 4. PARI/GP 2.17.3 (test 4)

`?11` lists 68 `alg*` functions, among them `alginit`, `algramifiedplaces`, `alghasse*`, `algbasis` (stored maximal order), `algnorm`, `algtrace`, `algsplit`, `algtomatrix` and the lattice suite `alglathnf`, `alglatadd`, `alglatinter`, `alglatmul`, `alglatindex`, `alglatlefttransporter`, `alglatrighttransporter`, `alglatcontains`, `alglatelement`, `alglatsubset`.

There is no Eichler-order constructor (`algeichlerbasis: unknown identifier`), and nothing for class numbers or class sets of orders, unit groups of orders, optimal embeddings or Brandt matrices.

Tiny test (`t4_pari_alg.gp`, 0.03 s), with al = `alginit(nfinit(y), [-1,-11])`:
- It is ramified at 11 and ∞, and `algdisc` = -1936 = -(4·11)², so the stored order is maximal.
- The norm form has 4 units.
- The three 2-neighbours J = 2O + xO consist of 1 principal and 2 non-principal ideals. Principality is tested by `qfminim` on the norm form; the non-principal ones have left orders (computed with `alglatlefttransporter`) with 6 units. This reproduces Sage's T_2 row [1, 2] for the w = 2 class of B(11).
- O ∩ O_L(J_3) (`alglatinter`) has index 3, which gives an Eichler order of level 3.

Verdict: PARI has usable building blocks, the same ones the sibling project's cypari2+flint code relies on, but no class-set, Brandt or Gross functionality.

## 5. darmonpoints (test 5; read only, via raw.githubusercontent.com and github.com; not installed, not run)

- **README.** It says "For most operations one does need to have Magma" and bundles Aurel Page's Magma package KleinianGroups. It provides `darmon_point`, `find_curve`, `darmon_vonk_point` and `padicperiods`.
- **Packaging.** `pyproject.toml`: version 8.3, `requires-python >=3.9`, `dependencies = []` (Sage is implicit), with Cython extensions `sparse.pyx` and `mixed_extension.pyx`. `config.ini` sets `use_magma : True`.
- **`darmonpoints.py`.** Only the classical case runs without Magma: F = Q and B = M_2(Q), called non-cohomologically, as in `darmon_point(7,EllipticCurve('35a1'),41,20, cohomological=False, use_magma=False, use_ps_dists=True)`. It finds optimal embeddings into M_2, lifts to an overconvergent (Pollack–Stevens) modular symbol, takes double integrals, then does algebraic recognition.
- **Quaternionic case (D_B ≠ 1).** This goes through `BigArithGroup` and `ArithGroup_rationalquaternion` (`sarithgroup.py`, `arithgroup.py`). Those call Magma `FuchsianGroup`, `FundamentalDomain` and `WordProblem` unconditionally (`ValueError("Should specify magma session")`), and the number-field cases do the same. The S-arithmetic group is the amalgam of the level-N and level-pN groups acting on the Bruhat–Tits tree.
- **`plectic.py`** ("Implementing Plectic SH points").
  - `PlecticGroup(p1, p2, quat_data, level, base, magma)` builds ArithGroups of level N, p0N, p1N and p0p1N, plus a single `BruhatTitsTree(p0.norm())` used for both factors. That suggests two primes of a base field with the same norm, i.e. the Fornea–Guitart–Masdeu setting, rather than two distinct rational primes. This is inferred from reading the code, not from running it.
  - It lifts a cohomology class to a harmonic cochain on T×T by solving a large sparse system.
  - It evaluates Riemann sums of products of p-adic logarithms over a depth-d covering and returns a p-adic number.
  - It always opens a Magma session and attaches KleinianGroups, so it is unusable here.
- **Scope.** The package has no definite Brandt-module, Gross-point or anticyclotomic code.

## 6. Conclusions

**Capabilities:**
- **Sage `BrandtModule`.** For prime discriminant and any coprime Eichler level M, it gives exact class sets, Hecke operators at good and bad primes, and exact eigenvectors. The classes are usable ideal objects. h ≈ 2700 classes take about 20 s plus about 20–70 s per Hecke matrix.
- **Gross-point map.** The own implementation (`t3_gross.py`) is validated. It covers Pic(O_{Dc²}) → classes for any conductor, including primes of the Eichler level and two-prime conductors, at about 1.0–1.6 ms per point, and it computes twisted sums.

**Gaps:**
- Sage has no composite-discriminant Brandt modules and no Eichler orders there; the hand-written workaround runs in under 1 s.
- No built-in Gross-point map exists, and the `heegner_divisor`/`optimal_embeddings` built-ins have the narrow semantics listed in §3.
- Embedding search scales as (|D|c²)^{3/2}; neighbour walks would avoid it.
- No conductor-compatible tower code exists.
- PARI has only primitives.
- darmonpoints' plectic and quaternionic code needs Magma.

**Related local code.** Two earlier projects contain related, independent implementations:
- `/Users/bsm/BSD_BUILD_MAP/results/e02/work/e02/src/{brandt.py,fixture.py}`: a custom Brandt module on (-1,-3) at level 8q², and conductor-25 Gross ideals via a mod-25 splitting;
- `/Users/bsm/BSD_PLECTIC_ACTUAL_EVALUATOR_ATTEMPT_CODEX_2026-09-30`: a mod-p eigenline replay. It found that a seed-scale class set of about 2.5e19 classes is infeasible.
