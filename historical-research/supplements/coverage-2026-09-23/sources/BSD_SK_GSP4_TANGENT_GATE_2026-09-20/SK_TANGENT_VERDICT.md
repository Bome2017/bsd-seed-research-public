# SAITO-KUROKAWA GSp_4 TANGENT GATE — final output

Date 2026-09-20. Seed E: `y^2 = x^3 - 22735 x^2 + 106272484 x`, rank 2, `E(Q) = Z/2 + Z P_1 + Z P_2`.
`p >= 5` symbolic good prime. `V = E[p]`, `det V = chibar_p`, `Rbar = 1 + V + chibar_p` in `GSp_4(F_p)`, similitude `chibar_p`.
Source/algebra audit only. No automorphy theorem attempted, no arithmetic run, no long computation.

## RETURN: `SK_TANGENT_OPEN_AT_R_EQUALS_T`

A and B compute cleanly. C's stated identity is **false as written** and is corrected below; the direction the candidate
actually needs survives the correction. D is the wall, and it is worse than "genuinely new mathematics": four independent
findings say the located machinery runs the wrong way, and one of them is the **same** obstruction that killed the GL(3)
predecessor, transferring by an exact computation.

**Recommendation: do not fund a successor.** The Galois-side computation is recorded below because it is clean and reusable.

---

## 0. Polarization check, and the collision check verified independently

`Rbar^vee (x) chibar = (1 + V^vee + chibar^{-1}) (x) chibar = chibar + V^vee(1) + 1 = chibar + V + 1 = Rbar`, using the Weil
pairing `V^vee(1) ~ V`. So `Rbar` is genuinely `GSp_4`-polarized with similitude `chibar`. In Saito-Kurokawa numerology this
is `k = 2`: the spin representation of a genus-2 SK lift of weight `k` from `f` of weight `2k-2` is
`rho_f + chi^{k-1} + chi^{k-2}` with similitude `chi^{2k-3}`, which at `k = 2` is `rho_f + chi + 1`, similitude `chi`. Correct.

Collision check re-run independently over `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19`, all `BSD_FABLE_*` and `BSD_ARISTOTLE_*`:
`GSp` 0 files, `Klingen` 0, `Saito` 0, `Kurokawa` 0, `paramodular` 0, `genus 2` 0 (`Siegel` matches 1 file, unrelated usage).
**The route is genuinely unrecorded**, as claimed.

**But the master carries a standing instruction that is directly on point.**
`provenance/eisenstein_register_before_integration.md:44`:

> "Do not launch a repair or successor from this GL(3) scout. **Changing the group, theorem name, weight, or derived
> terminology does not by itself change the failed arrow.**"

and line 40 records that the scout already considered "GL(3) datum **and nonclassical standard-representation alternatives**".
This does not automatically dispose of the proposal — the proposed arrow (upper bound) genuinely differs from the failed one
(class production) — but it raises the bar, and §D shows the new arrow has no located carrier while the old failure mode
transfers.

## A. `sp_4` as a `G_Q`-module — exact decomposition

For a symplectic form with similitude `nu`, the map `X |-> B_X(v,w) = <Xv,w>` gives `sp(W) ~ Sym^2(W^vee) (x) nu`, and
`W^vee ~ W (x) nu^{-1}`, so `sp(W) ~ Sym^2(W) (x) chibar^{-1}`. With `W = 1 + V + chibar`:

    Sym^2(W) = 1 + V + chibar + Sym^2 V + V(1) + chibar^2            (dims 1+2+1+3+2+1 = 10)

Twisting by `chibar^{-1}` and using `det V = chibar` (so `ad^0 V = Sym^2 V (x) chibar^{-1}` and `V^vee = V (x) chibar^{-1}`):

    **sp_4  ~  1  +  chibar  +  chibar^{-1}  +  ad^0 V  +  V  +  V^vee**        (1 + 1 + 1 + 3 + 2 + 2 = 10)

Block reading, with `W = A + B + C`, `A = 1`, `B = V`, `C = chibar`, `A` paired to `C` and `B` to itself:

| summand | block | dim |
|---|---|---|
| `1` | the `A<->C` torus direction | 1 |
| `chibar` | `Hom(A,C)` | 1 |
| `chibar^{-1}` | `Hom(C,A)` | 1 |
| `ad^0 V` | `Hom(B,B) ∩ sp` | 3 |
| `V` | `Hom(A,B)`, linked by polarization to `Hom(B,C)` | 2 |
| `V^vee` | `Hom(B,A)`, linked to `Hom(C,B)` | 2 |

Both `A` and `C` are isotropic lines, so there are **two** Klingen filtrations. The nilpotent radical for the ordinary one
(`1` sub, weights increasing) is `n ~ V^vee + chibar^{-1}`; for the opposite one it is `V + chibar`. Since `Rbar` is a direct
sum, no filtration is canonical, and the correct object is the pseudo-deformation ring, whose tangent space sees
**both** `V` and `V^vee`. This is the first substantive point: **you cannot isolate `V` without also carrying `V^vee`.**

## B. The deformation problem and its tangent space

Conditions as specified: similitude fixed to `chi_p`; the three diagonal JH constituents frozen; minimal ramification away
from `p`; Bloch-Kato finite/crystalline at `p`; polarized. Freezing the diagonal removes the `ad^0 V` and torus directions.
Hence

    t_D  ⊆  H^1_f(Q, chibar) + H^1_f(Q, chibar^{-1}) + H^1_f(Q, V) + H^1_f(Q, V^vee).

Two of these die unconditionally:
* `H^1_f(Q, F_p) = 0` — `Q` has no everywhere-unramified abelian extensions.
* `H^1_f(Q, chibar) = H^1_f(Q, F_p(1)) = 0` for `p` odd — `H^1_f(Q, Z_p(1)) = Z^x (x) Z_p = 0` since `Z^x = {±1}` and `Cl(Q) = 1`.

and `H^1_f(Q, chibar^{-1}) = H^1_f(Q, F_p(-1))` vanishes for `p` outside an explicit Herbrand-Ribet-type eigenspace condition
(`H^1_f(Q, Q_p(-1)) = 0` by Soulé; the mod-`p` statement is a `p`-divisibility condition), so it is generically but not always 0.

**Answer to (★), in the exact form asked.** `sp_4` contains `V` with multiplicity one as a `G_Q`-module direct summand, so the
projection `pr_V` is **canonical**, and `pr_V(t_D) ⊆ H^1_f(Q, V) = Sel_p(E)` is a canonical quotient — not merely an injection
into Selmer. Equality holds iff the deformation conditions impose nothing beyond the Bloch-Kato conditions on that summand,
which is what "minimal away from `p`, crystalline at `p`" is designed to give. **So (★) holds in the canonical-summand sense.**
It does **not** hold in the sense of `t_D` *being* `Sel_p(E)`.

## C. The rank-two plane, and the correction

`E(Q) = Z/2 + Z P_1 + Z P_2`, so for odd `p`, `E(Q)/p E(Q)` has dimension exactly 2 and
`delta(P_1), delta(P_2)` are two independent classes in `H^1_f(Q,V)`. With
`0 -> E(Q)/p -> Sel_p(E) -> Sha[p] -> 0`,

    dim Sel_p(E) = 2 + dim Sha[p],    and    dim Sel_p(E) <= 2  <=>  Sha[p] = 0  =>  Sha[p^inf] = 0.

**The stated target `dim t^std_D = 2 + dim Sha[p]` is false as written.** By §B the correct statement is

    **dim t_D = 2 + dim Sha[p] + dim H^1_f(Q, V^vee) + dim H^1_f(Q, F_p(-1)),**

where `V^vee = V(-1)`, whose `H^1_f` is the Selmer group of a **non-critical twist** (conjecturally 0, since `L(E,2) != 0`,
but that is itself an unproved Bloch-Kato case). **The correction does not damage the useful direction**: an automorphic upper
bound `dim t_D <= 2` still implies `dim Sel_p(E) <= 2` and hence `Sha[p] = 0`. It does mean any such bound must
simultaneously force `H^1_f(Q, V(-1)) = 0`, i.e. prove a second Bloch-Kato vanishing for free.

So A-C succeed, with that one correction. The gate is entirely in D.

## D. The automorphic side — four findings

**D1. Every located SK/GSp_4 result runs in the wrong direction.** Brown (*Saito-Kurokawa lifts and applications to the
Bloch-Kato conjecture*, Compositio; arXiv:math/0512279) proves: if `p` divides the algebraic part of `L(k,f)` then `p`
divides the order of the Selmer group — an L-value divisibility **producing** a Selmer class. The Glasgow result on
congruences of SK lifts and denominators of central spinor L-values is the same calibration. This is structurally identical
to the failure the master already records for the GL(3) route: `FIXED_VISIBILITY_AUDIT.md` line 46, "Selected automorphic
extensions map into Selmer | **No upper bound on all excess classes**". The candidate needs the converse, and no located
result supplies it.

**D2. The nearest upper-bound-shaped technology has the wrong shape for rank 2.** Berger-Klosin (Math. Ann., *On deformation
rings of residually reducible Galois representations and R = T theorems*) and the three-JH-factor sequel (arXiv:2308.02708)
conclude, under hypotheses, that **the universal deformation ring is a DVR** — i.e. tangent dimension **1**. Our seed needs
tangent dimension `>= 2`, since `E(Q)/p` alone is 2-dimensional. The engine is principality of the reducibility ideal
(after Bellaiche-Chenevier), which produces *cyclic* quotients. **A machine whose output is "cyclic" is calibrated to Selmer
dimension 1 and cannot, unmodified, deliver the bound a rank-2 curve needs.**

**D3. Even the closest theorem's hypothesis class excludes the stated starting point.** arXiv:2308.02708 assumes the residual
representation is **non-semisimple** with three mutually non-isomorphic absolutely irreducible JH factors. `Rbar = 1 + V + chibar`
as proposed is a **direct sum**, i.e. semisimple. Its stated Selmer hypotheses are "conditions regarding the orders of certain
Selmer groups", and Bloch-Kato is assumed in the applications — both on the rejection list given.

**D4. The weight obstruction transfers verbatim, by exact computation.** HT weights: `1` gives `{0}`, `chibar` gives `{1}`,
`V` gives `{0,1}`. So

    **HT(Rbar) = {0, 0, 1, 1} — irregular.**

The master's recorded reason the GL(3) route died is exactly this: `MASTER_BSD_DAG.md:290`, "`1 + rho_E` has Hodge-Tate
weights `{0,0,1}` ... a finite-dimensional algebraic coefficient requires the regular character `lambda + rho_3`. Common
twists and finite spectral-parameter jets do not repair this classical cohomology obstruction." Genus-2 Siegel weight `k = 2`
is precisely the non-cohomological limit case; Brown-type results need `k >= 3`. The proposal's claim to differ from the
GL(3) failure holds for the *arrow* (upper bound vs class production) but **not** for the *weight*, which is the master's
stated killer and which the master explicitly warned would not be repaired by changing the group.

**What is not claimed:** none of D1-D4 is a nonexistence theorem. Weight-2 genus-2 Siegel Galois representations do exist via
`p`-adic limits (arXiv:2003.11822 treats exactly limits of SK type reducing to `1 + rhobar + chi`, crystalline and
Siegel-ordinary), so D4 blocks the classical cohomological carrier, not the object. D1-D3 are statements about what was
located, not about what exists.

## E. Verdict and recommendation

    SK_TANGENT_OPEN_AT_R_EQUALS_T

* **A: succeeds.** `sp_4 = 1 + chibar + chibar^{-1} + ad^0 V + V + V^vee`, with `V` of multiplicity one.
* **B: succeeds.** `pr_V` is canonical; `pr_V(t_D) ⊆ Sel_p(E)` is a canonical quotient, not an injection. `H^1_f(Q,F_p)` and
  `H^1_f(Q,chibar)` vanish unconditionally.
* **C: corrected.** `dim t_D = 2 + dim Sha[p] + dim H^1_f(Q,V(-1)) + dim H^1_f(Q,F_p(-1))`. The needed inequality survives.
* **D: open, and unpromising.** No located mechanism gives an upper bound; the nearest one gives tangent dimension 1, which
  is the wrong shape for rank 2; its hypothesis class excludes a semisimple residual representation; and the weight
  obstruction that killed the predecessor transfers by exact computation.

**Recommendation: do not open a successor.** The proposal's genuinely new idea is the *direction* of the arrow, and that idea
survives §A-C intact — but after the audit it has no carrier, and it inherits the master's recorded weight obstruction, which
`eisenstein_register_before_integration.md:44` anticipated for exactly this kind of group substitution. If it is ever revived,
the entry condition should be a located or constructed automorphic local ring with **tangent dimension `>= 2` at a reducible
point** — that single requirement is what all of D1-D3 fail.

Endpoint effect: **NONE**. FIN and FORMULA unchanged. Nothing merged, no novelty claim, master untouched.
