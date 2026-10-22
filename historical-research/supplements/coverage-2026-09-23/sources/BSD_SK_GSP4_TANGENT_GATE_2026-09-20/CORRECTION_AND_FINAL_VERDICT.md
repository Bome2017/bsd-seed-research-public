# SK GSp_4 GATE — CORRECTION AND FINAL VERDICT

Date 2026-09-20. **Additive**: `SK_TANGENT_VERDICT.md` is not edited. Where the two conflict, **this file governs**.

    SK_TANGENT = KILLED_AT_DIRECTION.        (supersedes SK_TANGENT_OPEN_AT_R_EQUALS_T)
    Endpoint effect NONE. Do not open a successor.

Source obtained and read in this run: **Berger-Betina, "On Siegel eigenvarieties at Saito-Kurokawa points",
Ann. Inst. Fourier 72 (2022)** (Numdam, `10.5802/aif.3482`, 3289 extracted lines). All quotations below are verbatim from it.

---

## 1. My D4 was wrong: the weight-2 carrier exists

`SK_TANGENT_VERDICT.md` §D4 claimed the irregular weights `{0,0,1,1}` transfer the GL(3) obstruction "verbatim" as a carrier
obstruction. **That is false and is withdrawn.** Berger-Betina study precisely this point: their introduction states they treat
"the case of the **non-cohomological weight (2,2)**", constructing the local pseudocharacter / GMA on a 2-dimensional Siegel
eigenvariety `E_Delta` of paramodular tame level at the Saito-Kurokawa point. The classical-cohomology obstruction does not
kill the eigenvariety formulation.

This was a miss on my part in the stronger sense: `arXiv:1902.05885` appeared in my own search output during the run and I did
not follow it.

**Durable positive finding, retained:**

> `1 + E[p] + chi_p` has a real weight-2 `GSp_4` eigenvariety carrier (Berger-Betina, AIF 2022).

## 2. A-C overclaimed, and the overclaim is withdrawn

Two specific withdrawals from `SK_TANGENT_VERDICT.md`:

* §B asserted that `(★)` "holds in the canonical-summand sense" and then that equality holds because the deformation
  conditions "impose nothing beyond Bloch-Kato on that summand". **Multiplicity one gives only
  `pr_V(t_D) ⊆ H^1_f(Q,V)`; surjectivity onto `Sel_p(E)` was not proved and does not follow.** Withdrawn.
* §C's displayed identity
  `dim t_D = 2 + dim Sha[p] + dim H^1_f(Q,V(-1)) + dim H^1_f(Q,F_p(-1))`
  **does not follow from the inclusion established in §B.** Withdrawn; it is at best an upper bound on `dim t_D`.

The structural reason, which I should have stated: `End(1 + V + chibar)` contains the three block projectors, so it is
**non-scalar**. The unframed representation-deformation functor is therefore not representable. A framed ring adds framing
directions; the pseudo-deformation / GMA object instead sees off-diagonal extensions through reducibility modules. **That is
exactly why this literature naturally produces injections of automorphic extension modules into Selmer, rather than
surjectivity of an automorphic tangent space onto all Selmer classes.**

## 3. The exact kill: the published carrier's inequality runs the wrong way

**Corollary 7.8 (verbatim):** "Assume (BK), (Reg), (St) and when `k = 2` also assume that `L_p(f_alpha, omega_p^{-1}, T = p)
!= 0`. Then we have

    2 <= dim t_{pi_alpha} <= 1 + ( dim H^1_{f,unr}(Q, rho_f(k-1)) )^2

and `dim t^0_{pi_alpha} <= ( dim H^1_{f,unr}(Q, rho_f(k-1)) )^2`."

Read the direction. **The Selmer dimension bounds the tangent space**, not the reverse. The only lower bound available is the
trivial `2 <= dim t`. So even a perfect determination `dim t_{pi_alpha} = 2` cannot be inverted to give
`dim H^1_{f,unr} <= 2`, let alone `dim Sel_p(E) <= 2`. The same direction shows in their Theorem 4.3 and in the injections
`Hom(T_{1,2}/T'_{1,2}, L) --> H^1_{f,unr}(Q, rho_f(k-1))`.

This is the identical failure the master already records for the GL(3) scout
(`audits/fixed_visibility_2026-09-19/FIXED_VISIBILITY_AUDIT.md:46`: "Selected automorphic extensions map into Selmer | **No
upper bound on all excess classes**"). An `R = T` theorem would not reverse it: `R = T` identifies two rings, it does not
prove that the deformation problem captures **every** residual `E[p]`-Selmer class. That surjectivity is the missing arrow,
and it is missing for the structural reason in §2.

Note also the shape of their strong results: **Theorem 6.8** assumes `dim H^1_{f,unr}(Q, rho_f(k-1)) = 1`, and the `k = 2`
statement at line 1897 assumes `dim Sel_{Q,f_alpha} = 0`. Both assume the Selmer information we would be trying to derive.

## 4. Seed-specific applicability, independently checked

Their hypothesis **(St) (verbatim):** "For any prime `l | N`, `rho_f|I_l` is special and the sign `eps_l(f)` in the functional
equation of `f` at `l` is always equal to 1 ... Moreover, if `f` satisfies (St), then the integer `N` is necessarily
squarefree." Their standing setup also takes `sign_f = -1`.

For the seed, all three fail:
* **Sign.** Analytic rank 2, so the global root number is `+1`, not `-1`.
* **Squarefree `N`.** `N = 2^3 * 3 * 2243 * 4547^2 * 5843` is not squarefree.
* **(St) directly**, by an independent check that does not rely on the squarefree remark: `p^2 | N` forces `a_p(f) = 0` at
  `p = 2` and `p = 4547`, whereas a Steinberg (special) local component gives `a_p = ±1`. So `rho_f|I_p` is **not** special at
  those primes; at `4547` the local component is supercuspidal/type III.

## 5. One further gap that would survive even a perfect result

Their eigenvariety tangent space is a **characteristic-zero** object controlled by a `p`-adic Bloch-Kato Selmer group. A
dimension statement there principally controls **corank**. Finite `Sha[p]` is invisible after tensoring with `Q_p`. FIN needs
residual/integral information strong enough to kill finite `p`-torsion, which this interface does not carry.

## 6. Final record

    SK_TANGENT = KILLED_AT_DIRECTION.

Not killed for "no carrier" (there is one, §1), not for "weight two impossible" (§1), and not by the D1-D4 package as I
stated it. Killed because **there is no surjective or integral Selmer-control map**: the published interface runs
automorphic-extension `-->` Selmer, an `R = T` theorem would not reverse it, and the residual representation's non-scalar
endomorphism ring is the structural reason the reverse arrow is unavailable.

Retained: the weight-2 `GSp_4` eigenvariety carrier for `1 + E[p] + chi_p` (§1), and the `sp_4` decomposition
`1 + chibar + chibar^{-1} + ad^0 V + V + V^vee` with `V` of multiplicity one (§A of the superseded file, which stands).

Do not spend another run on Saito-Kurokawa. Endpoint effect **NONE**; FIN and FORMULA unchanged; master untouched; nothing
merged; no novelty claim.
