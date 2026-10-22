# MODULAR-DEGREE-AT-7 GATE — verdict: `V7_MODULAR_DEGREE_UNRESOLVED`

Date 2026-09-22. The CNS reduction is real and lands **better** than the generic statement for this curve. But the
new unknown `val_7(deg φ)` is not reachable by either available computational route, for a reason independent of
feasibility. §3 is the load-bearing finding.

---

## 1. CNS Theorem 1.2, source-checked verbatim (arXiv:1911.09446, = their Thm 7.2)

> **Theorem 1.2 (Theorem 7.2).** For an elliptic curve `E` over `Q` of conductor `N`, and for a level `Γ` with
> `Γ_1(N) ⊂ Γ ⊂ Γ_0(N)`, every surjection `φ : (X_Γ)_Q ↠ E` satisfies
>
>     c_φ | 6 · deg(φ),
>
> and if `N` is cube-free (that is, if `8 ∤ N` and `27 ∤ N`), then even `c_φ | deg(φ)`. More precisely, under these
> assumptions, for every prime `p` we have
>
>     val_p(c_φ) <= val_p(deg(φ)) + { 1  if p = 2 with val_2(N) >= 3 and there is no p' | N with p' = 3 mod 4,
>                                     1  if p = 3 with val_3(N) >= 3 and there is no p' | N with p' = 2 mod 3,
>                                     0  otherwise }

There is **no** exclusion at `p = 7`, none for additive reduction, and none for Kodaira type `I_0^*`. The user's
reading is confirmed.

## 2. For this curve it is better than the generic statement — both exceptions fail to fire

`N_{-7} = 2^3 · 3 · 7^2 · 2243 · 4547^2 · 5843` is **not** cube-free (`8 | N`), so the headline `c_φ | deg(φ)` does
not apply generically. But the per-prime version's `+1` terms are conditional, and neither condition holds here:

| exception | requirement | status |
|---|---|---|
| at `p = 2` | `val_2(N) >= 3` **and** no `p' | N` with `p' ≡ 3 (mod 4)` | `val_2(N) = 3` ✓, but **`3, 7, 2243, 4547, 5843` are all `≡ 3 mod 4`** ⟹ **does not fire** |
| at `p = 3` | `val_3(N) >= 3` | `val_3(N) = 1` ⟹ **does not fire** |

    => val_p(c_phi) <= val_p(deg phi) for EVERY prime p, i.e. c_phi | deg(phi),
       despite N not being cube-free.   In particular:  val_7(c) <= val_7(deg phi).

## 3. THE FINDING: neither computational route can bound `val_7(c)` above

**PARI `ellmoddegree` — honest, but the wrong quantity.** Its own help, verbatim: *"compute the modular degree of `e`
**divided by the square of the Manin constant**."* So it returns `R = deg(φ)/c²`. With `k = val_7(c)`,
`m = val_7(deg φ)`, `v = val_7(R) = m − 2k`, CNS gives

    k <= m = v + 2k   =>   0 <= v + k   =>   k >= -v

a **lower** bound on `k`. An upper bound is exactly what we need.

* `v >= 0` ⟹ `k >= -v` is vacuous (`k >= 0` anyway): **no information**.
* `v < 0` ⟹ `k >= |v| > 0`, i.e. `7 | c`: bad news, still no upper bound.

**So even a successful `ellmoddegree` run does not answer the question.** This is a logical obstruction, not a
resource one, and it is why no further effort was spent on the resource budget.

**Sage `modular_degree` — gives `deg(φ)` itself, but circularly.** Docstring, verbatim: *"The correctness of this
function when called with algorithm "sympow" is subject to the following three hypothesis: — **Manin's conjecture:
the Manin constant is 1** — Steven's conjecture … — The modular degree fits in a machine double."* And: *"computing a
certain value of an `L`-function 'uses a **heuristic** method… **For rigour, you would need to bound the tail**…"*

Using it to bound `val_7(c)` assumes `c = 1`, which is the conjecture the whole chain is trying to avoid.

**Feasibility, measured anyway (step 1 of the brief), with a strict budget.** `ellmoddegree`: `N = 11` → 4 ms,
`N = 37` → 3 ms, `N = 5077` → 142 ms, `N = 234446` → **PARI stack overflow at the default 8 MB**. A scaling run over
twists with `parisizemax = 8 GB` **produced no output and exited 0** — another gp scripting artifact (the same
line-by-line/semicolon trap that silently killed an earlier script), not a timeout. Not chased, because §3 makes the
scaling law moot. **No `O(N)`-scale construction was attempted and none is warranted.**

## 4. The one valid remaining route, and the inversion trap (step 2)

Every prime dividing `deg φ` is a congruence prime. The **contrapositive is valid and is the usable direction**:

    7 is NOT a congruence prime for f   =>   7 ∤ deg(φ)   =>   (CNS)   7 ∤ c.

**Do not invert it.** "`7` is a congruence prime ⟹ `7 | deg φ`" needs extra hypotheses and is delicate precisely when
`p² | N` — which is exactly our `7²` situation (ARS, *Modular degree, congruence primes and multiplicity one*). The
brief's warning is recorded and respected.

Deciding whether `7` is a congruence prime for `f` means asking about mod-7 congruences to other newforms of level
`N = 318,656,212,624,190,616`. That is the same order of infeasibility as everything else at this level, so this route
is *logically* open but not *computationally* open.

**And per step 4 of the brief: surjectivity is not evidence.** `ρ̄_{E^{-7},7}` **is** surjective (Sage:
`non_surjective() = [2]`), but a surjective mod-7 representation does not preclude a mod-7 congruence to another
newform of the same level. That inference is not made here.

## 5. What would close it — and the blocker is the bound, not the precision

Any **unconditional** upper bound `deg(φ) <= N^A` gives `val_7(deg φ) <= A·log_7(N)` and hence, by CNS,
`val_7(c) <= A·log_7(N)`. With `log_7(N_{-7}) = 20.71`:

| `A` | `k = A·log_7 N` | needed halfwidth(`L`) | segments | cost |
|---:|---:|---:|---:|---:|
| 1 | 21 | 6.46e−22 | 340 | ~12 min |
| 1.5 | 32 | 3.27e−31 | 460 | ~17 min |
| 2 | 42 | 1.16e−39 | 560 | ~21 min |
| 3 | 63 | 2.07e−57 | 780 | ~29 min |

So **any unconditional polynomial bound with `A <= 3` is closable by a rerun of at most ~800 of the 3281 segments.**
The obstruction is obtaining such a bound, not the `L`-value precision. (Known results run the wrong way: Watkins
gives a *lower* bound `deg φ ≫ N^{7/6−ε}`.)

## 6. Verdict and corrected frontier

    V7_MODULAR_DEGREE_UNRESOLVED

    Supp_odd(c)               ⊆ {7}                          [ARS Cor 3.7 + Edi89 Thm 4.6.3 at 4547]
    val_7(c) <= val_7(deg φ)  PROVED for this curve           [CNS Thm 1.2; both +1 exceptions fail to fire]
    c_φ | deg(φ)              PROVED for this curve           [same, despite N not cube-free]
    val_7(deg φ)              THE CONCRETE UNKNOWN
      via PARI ellmoddegree   IMPOSSIBLE IN PRINCIPLE - returns deg/c^2, gives only a LOWER bound on val_7(c)
      via Sage modular_degree CIRCULAR - assumes the Manin constant is 1; also heuristic
      via congruence primes   VALID DIRECTION ONLY (7 not congruence => 7 ∤ deg φ); infeasible at this level;
                              the inverse is NOT available and is delicate exactly because 7^2 | N
      via deg φ <= N^A        WOULD CLOSE IT, and cheaply (<= ~800 segments). No such unconditional bound located.
    MORE_L_DIGITS             STILL NOT JUSTIFIED - blocked on the bound, not the precision
    ORDINARY_BRIDGE           NOT CLOSED
