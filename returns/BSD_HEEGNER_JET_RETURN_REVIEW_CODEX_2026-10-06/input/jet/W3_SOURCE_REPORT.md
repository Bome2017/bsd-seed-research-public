# W3 source construction at p = 31: sparse attempt, certificates and exact residual

**Status: SPECIFIC_OBSTRUCTION** for the sparse construction attempted here. It comes with two subordinate partial results:
- a seed-specific order-0 dual certificate, with explicit multipliers;
- a conditional reduction identifying which global quantities remain.

**No seed source value was produced.** SEED_SOURCE_VALUE_EXACT, SEED_PRIMARY_BOUND and ORDINARY_UNIFORM_BOUND are **not** claimed.

Grades used below:
- DERIVED: proved in this note or in code that a reader can re-run.
- IMPORTED_WITH_HYPOTHESES: depends on a retained input.
- LEAN: machine-checked.

Everything runnable is in `w3_source/`. The Lean file is `RequestProject/QuadraticJetForcing.lean`.

## 0. Corrections adopted

1. **Congruence-freeness.** A dual certificate for one functional `v` does **not** need global congruence-freeness. It only needs `v - c nu` to vanish on every solution of the chosen rows, and a congruent eigensystem may be invisible to a particular `v`. I withdraw my earlier remark suggesting otherwise.
2. **The cusps a/31.** When `gcd(31,N)=1`, the cusp `a/31` is `Gamma_0(N)`-equivalent to `0`, **not** to infinity. At level `31N` its denominator satisfies `gcd(31,31N)=31`. The code never uses cusp equivalence: every path `{infinity, a/31}` is decomposed by continued fractions into explicit Manin cosets, each with an explicit `gamma` in `Gamma_0(31N)`.
3. **Full-space cost.** The size of the full presentation (`|P^1(Z/31N)| = 416552442899890176`) is **not** a lower bound for sparse methods. It is not used as one here.
4. **Provenance of multipliers.** The earlier elimination returned only a yes/no flag. The new elimination (`ProvElim` in `cert_seed.py`) keeps the row provenance and so returns explicit multipliers `lambda_r`. Every reported identity is then rebuilt from scratch and re-checked column by column.

The small-level calibration in `sparse_cert.py` / `SMALL_LEVEL_BALL_RESULTS.json` still uses the older yes/no membership test. It is orientation only.

## 1. The presentation actually used (DERIVED; validated)

**Level and coset generators.** The level is `31N = 201598828394896104`. The coset generators are `D_k = g_k{0,infinity}`, where `g_k` in `SL_2(Z)` lifts the canonical Manin symbol `k`, written per prime power of `31N`.

**Gamma-equivariance.** The classical integral `int g(z)(X - zY)^w dz` forces

    Xi(gamma D) = sigma(gamma)_* Xi(D),   sigma([[a,b],[c,d]]) = [[d,b],[c,a]],

where the pushforward is along `(x,y) -> (x,y) sigma(gamma)`. Specialising at `<x>^w` gives

    <dx+cy>^w = omega(d)^(-w) (dx+cy)^w.

So the weight-`w` fibre carries nebentypus `omega^(-w)`:
- weight 5: `omega^(-3)`, of order 10 and conductor 31;
- weight 6: `omega^(-4)`, of order 15 and conductor 31.

Both characters are nontrivial, and they are kept throughout. `sigma(gamma)` lies in `Sigma_0(31)`, which is where the ten-slot jet action of `original/jet_module.py` is defined.

**Hecke operators.** These are given by

    (T_q Xi)(D) = sum_beta sigma(adj beta)_* Xi(beta D),

with `beta = [[1,j],[0,q]]` and also `[[q,0],[0,1]]` (the latter only when `q` does not divide `31N`). `U_31` uses `beta = [[1,j],[0,31]]`. Each path `beta D` is decomposed back into cosets.

**Validation** (`validate_presentation.py`). This is a calibration on a genuine symbol, not on the seed.
- Setup: the 31-stabilised plus eigensymbol of 389a1, at level `389*31`, built from exact Manin relations.
- Checks: the S, tau, `T_5` and `U_31` rows (with `alpha` mod `31^4`) hold on 40 random cosets.
- Countercontrol: a deliberately wrong eigenvalue is rejected.

## 2. Target functionals with exact coset identifiers

`TARGET_FUNCTIONALS.json` writes each `V_(w,s)`, for the four retained nodes, as an exact row mod `31^4`.
- Its support is 74 cosets of `Gamma_0(31N)`, with 10 jet slots each.
- The rows follow formula (F) of `FINITE_MOMENT_MODULE.md`.
- `D_a = {infinity}-{a/31}` is oriented as the path from `a/31` to infinity.
- The weight variable is `T = (1+31)^w - 1`, not `T/p`.
- sha256: `3698f14f…a3a8`.

`FIRST_ORDER_RHS.json` gives the actual S row and `T_5` row at coset `(1:0)^6`. Their first-order parts are

    sum_k B_k^(1<-1) Xi_1(D_k) - a_(5,0) Xi_1 - b_5 Xi_0 = - sum_k B_k^(1<-0) Xi_0(D_k).

Here `b_5 = a_(5,1)` is kept as an unknown. The right-hand side needs 20 base evaluations, each a coset paired with a slot.

## 3. Certificates and residuals (`cert_seed.py`, `CERT_SEED_RESULTS.json`)

The seed data used are:
- `a_5 = a_7 = -2`;
- `alpha_0 = 57776` mod `31^4`, which is 23 mod 31.

### 3.1 Order 0, mod 31: closed by one row (DERIVED; recombination verified on 74 columns)

`lambda` is the single `U_31` row at the coset of `{0,infinity}`. It gives

    V_32 == 9 X,  V_33 == 22 X,  V_43 == 22 X,  V_44 == 9 X   (mod 31),
    X = Xi_0({infinity,0}),  22 = alpha_0 - 1 (mod 31).

The multipliers are in `CERT_ORDER0_MULTIPLIERS.json`.

Next, `X = 0` (IMPORTED_WITH_HYPOTHESES):
- Under the source identification and Hida control at `T = 0`, the weight-two specialisation of `Xi` is a unit times the stabilised symbol `phi_(f,alpha)`.
- Its value on `{infinity}-{0}` is a unit times `L(E,1)/Omega^+`.
- `L(E,1) = 0` holds unconditionally, because `E(Q)` has rank at least 2. By Kolyvagin/Kato, `L(E,1) != 0` would force rank 0.

Hence all four `V` vanish mod 31. This is a sparse, seed-specific proof of the first forced digit. It does not supply a bound.

### 3.2 Order 1 (slot `(1,0)`): one global column remains

The rows were:
- `U_31` at `{0,infinity}`;
- S, tau, `T_5` and `U_31` at all 74 target cosets;
- the base z-moment rows at those cosets.

That is 2072 rows. After elimination, exactly **one** order-one column survives: `Xi_1` slot `(1,0)` at the coset of `{0,infinity}`. In addition there are:
- 120 base columns (`Xi_0` slots), which are weight-two data;
- the symbol `a_(31,1) * m_(0,0)` at that coset.

That base value is the `X` of 3.1, which is 0. So **the eigenvalue derivative `a_(31,1)` drops out at first order.** `b_5` does not survive. The explicit identity is in `CERT_ORDER1_RESIDUAL.json`.

### 3.3 Order 2 (slot `(2,0)`)

Exactly one order-two column survives: `Xi_2` `(2,0)` at the coset of `{0,infinity}`. Also remaining are:
- `a_(31,2) * m_(0,0)`, which is 0;
- `a_(31,1) * m_(1,0)`;
- 115 `Xi_1` columns and 176 `Xi_0` columns, kept as the right-hand side.

The identity is in `CERT_ORDER2_RESIDUAL.json`.

### 3.4 The same identity in divisor coordinates (DERIVED; checked)

The pushes `[[1,-a],[0,31]]` fix every slot functional `e_(n,0)`. The `(n,0)`-coefficient of `V_(w,s)` divided by `31^n` is `(-1)^s w^n` mod 31, uniformly in `a`. Both facts are checked in `CERT_SEED_RESULTS.json`. Hence

    sum_{a=1}^{30} m_(n,0)(Xi({infinity,a/31})) = (alpha_0 - 1) Lam_n + sum_{r>=1} alpha_r Lam_(n-r),
    Lam(T) = sum Lam_n T^n = int (1+T)^u dXi({infinity,0}).

`Lam(T)` is the total-mass function of the family symbol at the **single divisor** `{infinity}-{0}`. At classical weights it is the `X^w`-coefficient of the normalised symbol of `g_w`, which is proportional to `L(g_w,1)`.

## 4. Exact first failure of this construction (SPECIFIC_OBSTRUCTION)

The `U_31` row turns the uniform part of every order into `Lam_n` together with weight-two data.

**No row within radius 0 of the targets removes `Lam_1` or `Lam_2`.** The order-1 and order-2 residuals in 3.2–3.3 are the exact remaining equations.

Calibration at small prime levels (389 and 3023) gave the same picture: ball certificates appeared only once the support covered essentially the whole coset space (389 of 390, and 3024 of 3024). This is evidence about **this** construction, not a theorem about all sparse methods.

**Missing authenticated inputs, stated exactly:**
1. **Weight-two values.** These are the values of the seed's primitive plus eigensymbol on 3608 Manin symbols of level `N`, from the 960 paths `{infinity, a/31}` and `{infinity, a/961}` and their negatives (`seed_pilot31.py`). They determine all `Xi_0` columns and `ell_2` below.
   - Acquisition was attempted but not achieved. Linear algebra over the full space is out of reach, and so is the period-integral route at denominator 961 (`ESTIMATE` of about `7.7e10` terms per path).
   - These are resource statements only.
   - No value was inserted.
2. **`Lam_2` mod 31.** No construction tried here produces it. Equivalently it is the value at `T = zeta_31 - 1`, modulo `pi^3`, coming from the weight-two specialisation with a wild character of order 31. That is again a classical form, but not `f`.

## 5. Conditional reduction of the mod-`p^3` test

**Imports**, all explicit:
- the source identification of `F` with `Xi`;
- `p` in the cofinite Hida domain. **This is unverified at 31**: it needs 31 not to divide the unenumerated integer `D`;
- the retained low-jet input `F in (T,S)^2`;
- the functional equation `b = -c`.

Write the quadratic jet of `F` as `a T^2 + b TS + c S^2`.

- **(LEAN, `W3.quadratic_jet_forcing`)** If all four node values vanish modulo `p^3`, then `p` divides `a`, `b` and `c`. This holds for every prime and needs no condition on `p`: after the row operation `4 r_44 - 7 r_33`, the node matrix has a determinant-1 minor.
- **(IMPORTED_WITH_HYPOTHESES)** `c` equals a unit times `ell_2`, the `S^2`-coefficient of the seed's weight-two Mazur–Tate–Teitelbaum p-adic L-function. The only extra ingredient is the reflection `x -> -x` that absorbs the factor `(-1)^s` (on the plus part).
  - `ell_2 mod p` is an exact finite sum over the level-`p^2` measure (`weight2_jet.py`).
  - This formula is calibrated on 11a1, 37a1 and 389a1. For 389a1 (rank 2), `ell_0 = ell_1 = 0` at all 8 ordinary primes tested; the level-2 and level-3 computations agree; and non-global assignments are rejected.
  - Therefore, if `ell_2` is not divisible by 31, some node value is nonzero mod `31^3`, and W3 holds at 31 under the imports above.
- **(DERIVED from 3.4)** The coordinate `a` is tied to `Lam_2` through the `U_31` identity: in the uniform part, `(alpha_0 - 1) Lam_2` appears together with `alpha_1 Lam_1`. With `b = -c`, the mod-`p^3` test therefore depends only on `ell_2` and on the one-divisor quantities `Lam_1` and `Lam_2`.

**Arithmetic step removed.** The weights-5/6 Hida symbols are no longer needed to evaluate the mod-`p^3` layer at 31. What remains is:
- weight-two seed data;
- the coefficients of one Lambda-adic value, `Lam(T)`, at the single divisor `{infinity}-{0}`.

No uniform-in-`p` control of `ell_2` or `Lam_2` was obtained. Uniform nonvanishing of `ell_2` mod `p` is a p-adic-regulator-type question, and nothing here settles it. FIN, ORDER9 and Q36 are unchanged.

## 6. Files

**Lean.** `RequestProject/QuadraticJetForcing.lean` contains:
- `W3.quadratic_jet_forcing`;
- `W3.exists_node_ne_zero_of_not_dvd_c`;
- `W3.padic_node_congr` (the congruence `t_n ≡ n p (mod p^2)` in `Z_p`).

**Python** (`w3_source/`):
- `seed_sparse.py`: the presentation and the target functionals.
- `validate_presentation.py`: the 389a1 calibration of the presentation code.
- `cert_seed.py`: the seed certificates and residuals.
- `weight2_jet.py` and `modsym2.py`: the exact weight-two tools.
- `seed_pilot31.py`: arithmetic bindings and the support of the weight-two route.
- `sparse_cert.py`: the small-level ball calibration (yes/no only).

**Outputs:** `*_RESULTS.json`, `TARGET_FUNCTIONALS.json`, `FIRST_ORDER_RHS.json`, `CERT_ORDER*_*.json`.
