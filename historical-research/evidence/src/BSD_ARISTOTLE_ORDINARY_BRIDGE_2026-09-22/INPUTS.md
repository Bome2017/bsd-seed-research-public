# INPUTS — retained facts. These are inputs, not things to re-derive.

Everything here is either proved in the project record, certified by computation, or source-checked. Do not spend the
run re-establishing any of it. §7 lists what is **not** yet source-read — those you must check yourself.

---

## 1. The curve

    E / Q :   y^2 = x^3 - 22735 x^2 + 106272484 x
    N = 2^3 * 3 * 2243 * 4547^2 * 5843 = 6503188012738584
    E(Q) = <(0,0)> + Z P_1 + Z P_2,    P_1 = (4547, 327384),  P_2 = (5184, 281520)
    rank E(Q) = 2                                     [PROVED]
    analytic rank r_an = 2                            [PROVED, rigorous Arb intervals]
    L''/2 in [35.929604, 35.941023]

**Non-CM**, by two independent arguments: `j = 1322372123614064 / 689197281363` is **not an integer** (a CM
`j`-invariant is an algebraic integer); and `v_q(j) < 0` exactly at `q = 3, 2243, 5843`, so `E` has potentially
multiplicative reduction there, while a CM curve over `Q` has potentially good reduction everywhere.

Valuations: `Delta = 2^8 * 3^2 * 2243 * 4547^3 * 5843^2`. Multiplicative at `3, 2243, 5843` (`v_p(N) = 1`);
additive at `2` (`v = 3`) and `4547` (`v = 2`).

## 2. The definite field

    K = Q(sqrt -7),    N^- = 3 * 2243 * 5843,    N^+ = 2^3 * 4547^2

`N^-` is squarefree with an **odd** number of prime factors, so the quaternion algebra is **definite**. Splitting in
`K`, computed: `3, 2243, 5843` **inert**; `2, 4547` **split** (`-7 = 1 mod 8`, `(-7/4547) = +1`).
`2` and `4547` cannot lie in `N^-` since they are not Steinberg (`v = 3` and `v = 2`).

`h(-7) = 1`, so any hypothesis `p does not divide h_K` is **vacuous**.

## 3. The certified twist input  (CERTIFICATE, 2026-09-22)

    L(E^{-7}, 1)  in  [9.054319, 9.054421]        zero excluded, positive, margin 1.79e5

`w(E^{-7}) = +1` — from `chi_D(N) = (-1)^{|N^-|} = -1` and `w(E^D) = -chi_D(N)` — so this is the **central value**
and the analytic rank of `E^{-7}` is **0**. By the retained Gross–Zagier–Kolyvagin theorem at analytic rank zero:

    rank E^{-7}(Q) = 0        Sha(E^{-7}/Q)  finite

Hence the Mordell–Weil rank decomposition is

    (r^+, r^-) = (2, 0),      rank E(K) = 2.

Full artifact and validation record: `evidence/D7_CERTIFICATE_RESULT.md`.

**WITHDRAWN — do not use:** the earlier project statement that `w(E^{-7}) = +1` forces the **Mordell–Weil** rank
`r^-` to be even. The root number gives **analytic** rank parity only; algebraic parity needs a parity theorem that
is not installed here. It is not needed: GZK gives `rank E^{-7}(Q) = 0` unconditionally from `L != 0`.

## 4. A0 — object normalization (RESOLVED, do not reopen)

The finite theta elements are on the **square-root** side. The retained branch stabilizes

    theta_n^alpha = theta_{n+1} - alpha^{-1} nu(theta_n)

and its `c_2` is the mod-`p` `I^2/I^3` coefficient of that stabilized Gross-point theta element. (Line-level source in
`evidence/BRANCH_THETA.md` §§1–3.) At infinite level, with `calL_p` the square-root anticyclotomic `p`-adic
`L`-function and

    L_p = calL_p * calL_p^iota,

the involution `iota` sends `T -> -T/(1+T)`, preserving `I` and preserving order, so **`ord_I L_p = 2 ord_I calL_p`
is always even**, and the leading coefficient of `L_p` is `±` the square of that of `calL_p` (so one is a unit
exactly when the other is). Therefore

    [c_2] != 0  ==>  calL_p in I^2 \ I^3  ==>  L_p in I^4 \ I^5,  unit normalized leading coefficient.

**Parity is a hard check: `ord_I L_p` can never be odd.** Any identification implying an odd order is wrong on its
face.

## 5. BD Corollary 3 (SOURCE-CHECKED)

Bertolini–Darmon, Annals 2005. Theorem 1's setup is `N^-` squarefree with an **odd** number of prime factors — the
**definite** case, ours. With `rho = max(r^+, r^-)` and `delta^± = 0` at good ordinary `p`, Corollary 3 gives

    ord_I L_p >= 2 max(r^+, r^-).

For the certified `(2,0)` ranks this lower bound is **4**.

## 6. BLV hypotheses, and which are free for us

Bertolini–Longo–Venerucci, arXiv:2306.17784, Math. Ann. 395 (2026). Hypothesis 1.1: `p >= 5`, `p ∤ N`, `p ∤ h_K`,
`p ∤ disc(K)`, `rho-bar_{E,p}` **surjective**, `N^-` squarefree, an anomalous condition, and ramification conditions.
`p` may be **split or inert**; reduction may be **ordinary or supersingular**. Theorem A:
`(L_p^eps) subset (Char_p^eps)` with **equality in the non-exceptional case**; Definition 1.3 marks exceptional as
supersingular **and** `p` inert **and** `eps = +`. **At ordinary `p` the exceptional case cannot occur.**

Surjectivity of `rho-bar` *forces* non-CM, so BLV is built for this kind of curve.

Checked here, for this curve:

* **(Ram)** `rho-bar_p` ramified at every `l | N`, for **every `p >= 5`**. At the multiplicative places the
  Tate-curve criterion needs `p ∤ v_l(Delta)` and `v_l(Delta) = 2, 1, 2` at `l = 3, 2243, 5843`. At the additive
  places `2` and `4547`, `j` is integral, so the reduction is potentially good, inertia acts through a group of order
  `e | 24`, and `p >= 5` gives `p ∤ 24`.
* **`H^0(G_{Q_q}, E[p]) = 0` for `q | N^+`**, for **every `p >= 5`**: both places are additive with `j` integral, so
  the formal group is pro-`q`, `E_0/E_1 = (F_q,+)` is a `q`-group, and `c_q <= 4` for every additive Kodaira type.
  **Zero primes excluded.**
* **`p ∤ h_K`** vacuous, `h(-7) = 1`.
* **(Im)** surjective for all but finitely many `p` (Serre, non-CM).
* **Anomalous condition** (`a_p ≢ ±1 mod p` inert, `a_p ≢ 1 mod p` split): **no prime `5 <= p < 30000` has
  `a_p = ±1`** for this curve. Not proved finite — Lang–Trotter predicts infinitely many (density 0) — and not proved
  infinite either. **This is interface B and is OUT OF SCOPE here** (see `GATE.md`).

## 7. NOT source-read here — you must check these yourself

* **BD Theorems 2.7, 2.18, 2.23 and Remark 2.21.** Their characterization in this project was accepted as given and
  has never been read at source. Task 3 and Task 7 depend on them. Treat this packet's descriptions of them as
  *unverified hypotheses about the literature*.
* **The module identification** (BLV `Char_p` vs BD `X_inf`). Task 2. Open.
* **The `tau`-eigenspace bridge for pro-`p` Selmer and `T_p Sha`** (as opposed to for `E(K)`). Task 4. Open.

## 8. Live configurations before the certificate

With `d^± = corank Div Sha(E/K)[p^inf]^±`, `s^+ = 2 + d^+`, `s^- = r^- + d^-`, and `sigma = 4 >= 2 max(s^+,s^-)`:
`d^+ = 0` is forced (rank-two `E(Q)` already fills `s^+`), but `d^- in {0,1,2}` **survives**. The certificate is what
removes those rows — see Task 5.

## 9. Project status this audit must not contradict

`RANK` closed. **`FIN` open. `FORMULA` open.** `#Sha[30030^inf] = 9` with `Sha[3^inf] = (Z/3)^2` and
`Sha[p^inf] = 0` for `p = 2,5,7,11,13`. Conditional threshold: `#Sha < 2601 ==> #Sha = 9`; cite the master record for
that value, **never copy a number for it into a new artifact** — a stale `1089` propagated once through exactly that
mistake.
