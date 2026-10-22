# 04 — Numerical verification

All computation is **exact**: integer linear algebra reduced modulo two large primes
`ℓ ∈ {1000003, 999983}` (for identities and `Q`-ranks) or modulo `p^K` (for everything `p`-adic,
i.e. the ordinary projector).  No floating point anywhere.

## §0. Provenance and custody

    cp ~/H9R16C_LANE5_MPC_PROVER_2026-09-15/_verify/msym_check.py \
       /Users/bsm/H9R16C_H_PI_PINNING_2026-09-15/_verify/msym_check.py

`shasum -a 256` of both copies: `f99115c142844abb116402f9d9b32e704c67597d17df21074c39930ac374c3e8`
— **byte-identical to Lane 5's original**, which is also the hash recorded by the second assembly
referee.  Lane 5's file is imported, never edited.  Two new files are written, both in this lane's
own `_verify/`:

| file | role |
|---|---|
| `_verify/hpi_gens.py` | generator intertwinings (G1)–(G4), equivariance of `ϖ_1^*`/`ϖ_2^*`, injectivity |
| `_verify/hpi_ring.py` | ring-level: well-definedness + surjectivity of `π_r`; ordinary projector; `p`-adic parts |

## §1. The model, and the dictionary

`ManinSpace(L, mod)` is Lane 5's weight-2 Manin-symbol space for `Γ_1(L)`: the free module on symbols
`[c:d]`, `gcd(c,d,L)=1`, modulo `x + xσ = 0` and `x + xτ + xτ^2 = 0` — i.e. `H_1(X_1(L), cusps; Z)`,
which is `Z`-free.  Lane 5's declared dictionary (`msym_check.py` docstring, and Lane 5 `01`) is used
unchanged:

* `push1 := operator_matrix(S_{pM}, S_M, [I])` ⟷ `ϖ_{1,*}`;
* `pull1`, `pull2` (coset sums) ⟷ `ϖ_1^*`, `ϖ_2^*`;
* an operator written as the sum over the **standard** coset representatives (e.g.
  `U'_ℓ = Σ_{b<ℓ}[[1,b],[0,ℓ]]`, `T'_ℓ = Σ_{b<ℓ}[[1,b],[0,ℓ]] + σ_ℓ[[ℓ,0],[0,1]]`,
  `σ_ℓ ≡ diag(ℓ^{-1},ℓ) mod L`) ⟷ the **primed** operator `U'_ℓ`, `T'_ℓ`;
  its Poincaré transpose (`Σ_a [[ℓ,0],[aL,1]]`) ⟷ the unprimed one;
* `⟨d⟩ : [c:d'] ↦ [dc:dd']`.

That dictionary is not an assumption of this lane: it is the one that **reproduces the printed
statement**, DR22 l.1569 (`ϖ_{1,*}U'_p = U'_pϖ_{1,*}`), and it fails for the transpose.  Under the
opposite dictionary (reading the model as homology, so that `push1` is `ϖ_{1,*}` on
`H_1(X,\text{cusps})`, dual to `ϖ_1^*` on `H^1(Y)`, and primed ↔ unprimed swap) the *same* matrix
identities are read as the Poincaré duals of (G1)–(G4) — which are Lemma 2.2 of `03`, also verified
here as the `(E1)` block.  **Both sides of every adjoint pair are checked**, so the verification is
insensitive to which reading is taken.

**Why unit pivots are legitimate mod `p^K`** (`hpi_ring.ManinSpaceQ`): `H_1(X,cusps;Z)` is free, so
the Manin relation lattice is a *saturated* submodule of the free module on symbols, i.e. its Smith
normal form has all elementary divisors `1`.  Hence a unit pivot exists at every elimination step.
The code `assert`s this at every step; it never fired in any run.

## §2. Generator intertwinings (`hpi_gens.py`)

    cd /Users/bsm/H9R16C_H_PI_PINNING_2026-09-15/_verify
    python3 hpi_gens.py 1,5,1 5,3,1 2,3,2 7,3,1 3,5,1 > hpi_gens.log 2>&1

5 cases `(N_g,p,r)` × 2 primes `ℓ` = **10 runs**.  Levels covered:
`5→25`, `15→45`, `18→54`, `21→63`, `15→75`; `dim MS` up to `145` / `289`.
Checked per run, for `U'_p`, `U'_ℓ (ℓ|N_g)`, three `T'_ℓ` with `ℓ ∤ N_gp`, and **every** diamond
`⟨d̃⟩`, `d̃ ∈ (Z/N_gp^{r+1})^×` (20–48 of them per run, all of them, not a sample):

| check | meaning | result |
|---|---|---|
| `(G)` | `ϖ_{1,*}∘X_{pM} = X_M∘ϖ_{1,*}` | **PASS** for every primed generator |
| `(G4)` | `ϖ_{1,*}⟨d̃⟩_{pM} = ⟨d̃ mod M⟩_M ϖ_{1,*}`, **all** units `d̃` | **PASS** |
| `(E2)`,`(E2d)` | `X_{pM}∘ϖ_2^* = ϖ_2^*∘X_M`, incl. all diamonds | **PASS** for every primed generator |
| `rank(ϖ_2^*)` | `= dim MS(M)` ⟹ `ϖ_2^*` injective | **PASS**, e.g. `17/17`, `33/33` |
| `rank(ϖ_1^*)` | `= dim MS(M)` | **PASS** |
| `(W)` | `ϖ_2^* = W_{pM}∘ϖ_1^*∘W_M` (Lemma 2.3(b) of `03`) | **PASS** |
| `(deg)` | `ϖ_{1,*}ϖ_1^* = p^2` (uniqueness input (U1)) | **PASS** |
| `(E1)` | `X_{pM}∘ϖ_1^* = ϖ_1^*∘X_M` | PASS for `T'_ℓ`, `U'_ℓ (ℓ|N_g)`; **FAIL for `U'_p`** |

Totals: **214 PASS, 30 FAIL** (plus their 30 summary echoes and one final line = 61 `FAIL` strings in
the log).  Every one of the 30 failures is one of exactly **three predicted-negative controls**,
appearing once per run:

1. `(E1)` for `U'_p` — `ϖ_1^*` does **not** commute with `U'_p`.  (6 runs `p=3`, 4 runs `p=5`.)
2. `(G)` for the unprimed `U^t_p` — `ϖ_{1,*}` does **not** commute with the unprimed `U_p`.
3. `(E2)` for `U^t_p` — `ϖ_2^*` does **not** commute with the unprimed `U_p`.

These are the falsifiers of `03` §8.1–8.2: they show the primed/unprimed and `ϖ_1^*`/`ϖ_2^*`
dichotomy is real, so the proof in `03` is not a restatement of Hida's printed tower.  The control
`T_ℓ = ⟨ℓ⟩T'_ℓ` (`ℓ ∤ N_gp`) passes `(G)`, `(E1)` and `(E2)` — correctly, since away from `p` the
primed and unprimed operators differ by a diamond and both intertwine.

## §3. Ordinary projector and surjectivity of `e'ϖ_{1,*}` (`hpi_ring.py`, PART B)

`e'_ord` is computed as the **Fitting projector** of `U'_p` over `Z/p^K`: with `A := (U'_p)^{n·K+n}`
one has `A ≅ diag(unit, 0)`, so a unit-pivot reduction of `A` yields simultaneously a basis of
`im(A)` and of `ker(A)`; `e' := G·diag(I_ρ,0)·G^{-1}`.  The code then **asserts**, and the runs
confirm, `e'^2 = e'`, `e'U'_p = U'_pe'`, and that `U'_p` is invertible on `e'`-parts.

    python3 hpi_ring.py B 1,5,1,6,3 1,3,2,6,3 5,3,1,6,3 2,3,2,6,3 7,3,1,6,3 > hpi_ring_B.log
    python3 hpi_ring.py B 5,3,1,10,3 7,3,1,10,3 1,5,1,8,3 1,3,2,8,3 2,3,2,8,3 > hpi_ring_B2.log
    python3 hpi_ring.py B 5,3,1,14,3 7,3,1,14,3 5,3,1,12,3 > hpi_ring_B3.log

| `(N_g,p,r)` | `M→pM` | `dim MS` | `ρ(M)`,`ρ(pM)` | `ϖ_{1,*}e' = e'ϖ_{1,*}` | `e'ϖ_{1,*}` onto |
|---|---|---|---|---|---|
| `(1,5,1)` | 5→25 | 3, 51 | 2, 10 | PASS | PASS `2/2` |
| `(1,3,2)` | 9→27 | 7, 55 | 3, 9 | PASS | PASS `3/3` |
| `(5,3,1)` | 15→45 | 17, 145 | 10, 30 | PASS | PASS `10/10` |
| `(2,3,2)` | 18→54 | 19, 163 | 6, 18 | PASS | PASS `6/6` |
| `(7,3,1)` | 21→63 | 33, 289 | 18, 54 | PASS | PASS `18/18` |

"onto" is tested as `rank_{F_p}` of the induced `ρ(M)×ρ(pM)` matrix between the two free ordinary
modules; a `Z/p^K`-linear map between free modules is surjective iff its reduction mod `p` is, so
this test is **exact and immune to truncation**.  This reproduces **Ohta99 Lemma (1.2.12)** (`02` §3)
numerically, and supplies uniqueness input (U2) of `01` §3.3.
Repeated at `K = 6, 8, 10, 12, 14` — identical every time.

Contrast recorded by the same runs: on the **full** (non-ordinary) space `ϖ_{1,*}` also happened to
be onto in all five cases, so ordinarity was not needed for surjectivity here; that is a fact about
these small levels, not a theorem, and `03` never uses it.

`π_r(e'_{r+1}) = e'_r` is exactly the check `(G2-e')` in the table, together with the fact that both
idempotents are produced by the *same* limiting procedure from `U'_p`, which `π_r` fixes.

## §4. `π_r` well-defined and surjective (`hpi_ring.py`, PART A/B)

### 4.1 The exact test, and why a rank identity is the right one
For monomials `m_1,…,m_T` in the generators let `V` have columns `vec(ev_{pM}(m_i))` and `W` have
columns `vec(ev_M(φ_r m_i))`.  Well-definedness is `ker(V) ⊆ ker(W)` over `Z_p`.  Kernels of integer
matrices over `Z_p` are **saturated**, so

    ker_{Z_p}(V) ⊆ ker_{Z_p}(W)  ⟺  ker_{Q_p}(V) ⊆ ker_{Q_p}(W)  ⟺  rank(V) = rank([V;W]).

That is a rank identity of **integer** matrices, hence testable exactly mod a large prime (twice,
independently).  Surjectivity is tested as `rank(W) = rank(W_own) = rank([W | W_own])`, where
`W_own` is built from level `M`'s *own* generator set — i.e. the image of `π_r` really is all of
`𝕋'_M`, not merely a subalgebra.

### 4.2 PART A — full Hecke rings, exact mod two primes

    python3 hpi_ring.py A 2,3,2,4 1,5,1,3 1,3,2,3 5,3,1,3 > hpi_ring_A2.log
    (superseded earlier run: python3 hpi_ring.py A 1,5,1,3 1,3,2,3 5,3,1,3 2,3,2,3 > hpi_ring_A.log)

| `(N_g,p,r)` | deg | #mons | rank `V` | rank `W` | rank `[V;W]` | rank `W_own` | (WD) | (SURJ) | (NI) | relations |
|---|---|---|---|---|---|---|---|---|---|---|
| `(1,5,1)` | 3 | 56 | 39 | 3 | 39 | 3 | PASS | PASS | PASS | 17 |
| `(1,3,2)` | 3 | 56 | 42 | 7 | 42 | 7 | PASS | PASS | PASS | 14 |
| `(5,3,1)` | 3 | 120 | 103 | 16 | 103 | 16 | PASS | PASS | PASS | 17 |
| `(2,3,2)` | 4 | 210 | 111 | 17 | 111 | 17 | PASS | PASS | PASS | 99 |

Identical at both primes.  The last column is `#mons − rank V` = the number of independent relations
that actually hold at level `pM` and must be shown to survive at level `M`: the test is
**non-vacuous** in every case.  (At degree 3 the case `(2,3,2)` gave `rank V = 210 = #mons`, i.e. no
relations at all — a vacuous test; that is why it is run at degree 4.  This is recorded rather than
hidden.)  `rank W < rank [V;W]` in every case, so `π_r` is surjective and **not** injective, exactly
as `01` §3.4 predicts.

### 4.3 PART B — ordinary Hecke rings, mod `p^K`

Same test on the ordinary blocks.  All `(WD-ord)` **PASS**, with `#mons − rank V` = 46, 47, 83, 66,
69 independent relations respectively — non-vacuous everywhere.  Ranks:

| `(N_g,p,r)` | rank `R_{pM}` | rank `R_M` | rank `[V;W]` | (WD-ord) |
|---|---|---|---|---|
| `(1,5,1)` | 10 | 2 | 10 | PASS |
| `(1,3,2)` | 9 | 3 | 9 | PASS |
| `(5,3,1)` | 37 (`K≤12`) / 36 (`K=14`) | 11 | same as rank `V` | PASS |
| `(2,3,2)` | 18 | 6 | 18 | PASS |
| `(7,3,1)` | 51 | 18 | 51 | PASS |

**Declared limitation.**  For the two largest cases the `p`-adic rank routine reports its maximum
pivot valuation equal to `K−1`, i.e. the *tail* of the elimination is at the truncation boundary, and
the reported rank for `(5,3,1)` drifts `37 → 36` between `K=12` and `K=14`.  So the absolute rank
values for `(5,3,1)` and `(7,3,1)` carry a `±1` uncertainty.  The **verdict** does not: (i) `[V;W]`
has the same columns as `V` and strictly more rows, so any truncation artefact can only *inflate*
`rank[V;W]` relative to `rank V` — observing equality is therefore evidence in the safe direction,
never a false PASS produced by truncation; (ii) the equality `rank V = rank[V;W]` is stable across
`K = 6, 10, 12, 14`; and (iii) **`(WD-ord)` is in any case a formal consequence of `(WD)` of §4.2 —
which is exact — together with `π_r(e') = e'` of §3**, because `R_s = e'𝕋'_s` is a quotient ring of
`𝕋'_s` (`03` §5).  PART B is confirmation, not the load-bearing test.

## §5. What the numerics do and do not establish

They establish, on the weight-2 Manin-symbol carrier, for `(N_g,p,r) ∈ {(1,5,1),(1,3,2),(5,3,1),
(2,3,2),(7,3,1),(3,5,1)}` — including `p = 3`, which KLZ17's `p ≥ 5` hypothesis excludes:

* (G1)–(G4) for `ϖ_{1,*}`, with **all** diamonds, not a sample;
* injectivity and full primed-equivariance of `ϖ_2^*`, and the failure of both for `ϖ_1^*`/`U'_p`;
* `ϖ_{1,*}ϖ_1^* = p^2`, and `ϖ_2^* = Wϖ_1^*W`;
* `e'ϖ_{1,*}` surjective on ordinary parts (Ohta99 (1.2.12) reproduced);
* `π_r` well defined and surjective on the full rings (exact, two primes) and on the ordinary rings.

They do **not** establish the theorem: they are five levels, one weight, and a Betti (not étale)
carrier.  The theorem is `03`; `04` is its falsification attempt, and it failed to falsify —
including the three deliberately-chosen negative controls, all of which fired.
