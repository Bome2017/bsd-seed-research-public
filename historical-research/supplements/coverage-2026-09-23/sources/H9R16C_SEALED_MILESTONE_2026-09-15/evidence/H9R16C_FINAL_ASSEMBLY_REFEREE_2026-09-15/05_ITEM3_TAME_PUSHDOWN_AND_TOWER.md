# 05 — ITEM 3: the tame push-down, and the typed tower relation

Continues 03, 04. Inputs: A1 (MPC, d_r = 1), A2, A3, A5 (tame transport), A6/Theorem 2 (Hom-valued D4),
B1, B2, B5, B6, §C, 02a. Prohibited items (BCPV (4.9), Hida's w-tower, all downstream inputs) are not used.

## §1. Which tame push-down does BCPV's construction use? (02a §1)

**What is printed.**
* BCPV define `ϖ_1` **only** in the p-direction: `X_1(Np^r) → X_1(Np^{r−1})`, `(A,P) ↦ (A,pP)`
  (BCPV.tex l.1198–1200).
* For the tame direction they **reuse the symbol** without a new definition:
  `definition_big_diagonal_Hida_families` l.1457 (`ϖ_{1,*}⊗ϖ_{1,*}⊗ϖ_{1,*}: H^1_ord(Y_1(Np^∞))^{⊗3} →
  H^1_ord(Y_1(N_fp^∞))⊗H^1_ord(Y_1(N_gp^∞))⊗H^1_ord(Y_1(N_hp^∞))`), and `pr_h` in (4.16), l.1486–1487
  ("for a cuspidal newform `h` of level `Γ_1(N_hp^r)` with `N_h | N`, the map `pr_h` is induced from the
  pushforward map `H^1_ét(X̄_1(Np^r),Z_p)(1) --ϖ_{1,*}--> H^1_ét(X̄_1(N_hp^r),Z_p)(1)` composed with
  projection to the `h`-isotypical Hecke eigenspace").
* So 02 §D P4/§E were right about the **symbol** and 02a is right that the **forgetful reading is an
  interpretation**. Classification: `NOT_PRINTED` (not FALSE, not ambiguous in the sources they inherit).

**What justifies the forgetful reading.** BCPV take their degeneracy/Hecke conventions from DR22 §1.3 and
KLZ17 §2.4–2.5 (they say so at l.1196: "We will follow Section 2 in op. cit., and stick to the notation
therein"). In both sources the **index 1** always denotes the map that is the *identity on the upper
half-plane*:
* DR22 l.1149–1154: `ϖ_1` "corresponds to the map `(A,P) ↦ (A,pP)`, and to the map `τ ↦ τ`"; `ϖ_2`
  "corresponds to `(A,P) ↦ (A/⟨p^rP⟩, P+⟨p^rP⟩)`, which on the upper half plane sends `τ` to `pτ`".
* KLZ17 `sect:degeneracy` l.544–551 defines, **for an arbitrary integer `A`** (not only `A = p`),
  `pr_1(E,e_1,e_2) = (E,e_1,Ae_2)` and `pr_2(E,e_1,e_2) = (E/⟨Ae_2⟩, …)`, and states: "`pr_1` and `hpr_1`
  correspond to the identity map on `(Z/MZ)^* × H` …, while `pr_2` and `hpr_2` correspond to
  `(x,z) ↦ (x,Az)`". With `A = t = N/N_h` this is exactly `pr^t_1(A,P) = (A,tP)` (forgetful) vs
  `pr^t_2(A,P) = (A/⟨N_hp^sP⟩, P mod)`.
* KLZ17 l.800 uses precisely the common→native step in the same convention: "if `N` is any common multiple
  of `N_f` and `N_g`, there is a natural degeneracy morphism `Y_1(N)^2 → Y_1(N_f)×Y_1(N_g)`. Pushforward
  along this degeneracy morphism defines a projection map `pr_{f,g}`" — the *natural* (index-1, forgetful)
  morphism, and BCPV's `pr_h` is the one-factor version of exactly this map.

**Decision recorded.** `pd^t = pr^t_1` (forgetful), `pd^{t_f} = pr^{t_f}_1`, justified by the inherited
KLZ17/DR22 index convention and by KLZ17 l.800, **not** by a printed BCPV definition. Because this is a
reading and not a theorem, §4 below also proves that **the tower relation and its constant are the same for
`pr^t_2`**, so the verdict does not depend on the choice. (What the choice *does* change is which point is
constructed — see §5 — a normalization question for the next gate, not for H9R16-C.)

## §2. How L5-T5 transports it, and the one composite identity that matters

A5 (L5-T5), at every `s`, with `ζ_{Np^s}^t = ζ_{N_gp^s}`:

    pr^t_{1,*} W_{Np^s} = W_{N_gp^s} pr^t_{2,*},      pr^t_{2,*} W_{Np^s} = W_{N_gp^s} pr^t_{1,*}.

Consequence (the composite actually used, since `Δ_r^{ord}` carries `W_{Np^r}` *at common level* while `A_r`
carries `W_{N_gp^r}` *at native level*; weight 2, `W^{-1} = W`, `WU'_pW = U_p`):

    A_r ∘ pr^t_{1,*} ∘ W_{Np^r} = W_{N_gp^r}(U'_p)^r W_{N_gp^r} pr^t_{2,*} = (U_p)^r ∘ pr^t_{2,*} .   (★)

So the mixed-level composite is an *operator identity with no scalar and no diamond*: pushing the
`W_{Np^r}`-twisted class down by the forgetful map and then applying `A_r` is the same as applying `(U_p)^r`
to the push-down by the other map. This is exactly why the level mixing flagged by Lane 2's "level caveat"
(B2) and Lane 4 `03` §2 ("the push-down `N → N_g` does not intertwine `W_{Np^r}` with `W_{N_gp^r}` without
degeneracy/Atkin–Lehner factors") is **closed, not merely deferred**: the intertwiner exists and is the
interchange of the two tame degeneracy maps.

**Numerical confirmation (this referee, new).** `_verify/msym_tame_check.py` (imports Lane 5's
`msym_check.py` unmodified, adds the tame operators; command line and log below) checks, on full weight-2
modular symbols mod two primes:
`(T5-a)`, `(T5-b)` (A5 itself), `(C-U)` `pr^t_{i,*}U'_p = U'_ppr^t_{i,*}`, `(C-D)` diamond compatibility,
`(C-W)` `pr^t_{i,*}ϖ_{1,*} = ϖ_{1,*}pr^t_{i,*}` (tame vs p-direction), and the composite `(★)`.

    cd _verify && python3 msym_tame_check.py 3,3,2,1 5,3,2,1 5,2,3,1      (log: _verify/tame_check.log)
    cases (N_g,t,p,r) = (3,3,2,1), (5,3,2,1), (5,2,3,1); primes 1000003 and 999983;
    levels: common 18/36, 30/60, 30/90; native 6/12, 10/20, 15/45.   91 checks, ALL PASS, 0 FAIL.

A5 was previously **not exercised numerically** (02 §A5 says so); it now is, together with the two
commutations that the tower proof needs.

## §3. The chain, written with its types

Fix `b = [t_2⊗t_3] ∈ B^bal_{r+1}` (native-level Hecke operators; Lemma C of 04). Write
`res^bal_{r+1,r}: B^bal_{r+1} → B^bal_r` for the map induced by `π_r` (standing input `H_π`: the ring map
with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}`; it is part of the *statement* of the target relation, B6, and is used as
such, not proved here).

**(3.1) Transport of the contraction across one level (uses A1 at the NATIVE tame level).**
For all `y_1⊗y_2⊗y_3 ∈ S_{r+1}^{⊗3}(2)`:

    ϖ^{(f)}_{1,*}( Contr_{r+1}^{A_{r+1}}([t_2⊗N_{r+1,r}t_3])(y) )
       = pd^{t_f}_*ϖ_{1,*}y_1 · ⟨ pd^t_*y_2 , ρ(t_2)A_{r+1}N_{r+1,r}t_3 pd^t_*y_3 ⟩_{N_gp^{r+1}}
       = pd^{t_f}_*ϖ_{1,*}y_1 · ⟨ ϖ_{1,*}pd^t_*y_2 , ρ(π_rt_2)A_r π_r(t_3) ϖ_{1,*}pd^t_*y_3 ⟩_{N_gp^r}
       = Contr_r^{A_r}( res^bal_{r+1,r} b )( ϖ_{1,*}^{⊗3} y ).

Line 2 uses: the commutations `pd^t_*ϖ_{1,*} = ϖ_{1,*}pd^t_*` and `pd^{t_f}_*ϖ_{1,*} = ϖ_{1,*}pd^{t_f}_*`
(independent prime directions; §2 `(C-W)`), then **A1 at tame level `M = N_g`** applied to
`y = pd^t_*y_2`, `z = pd^t_*y_3`: `⟨ϖ_{1,*}y, A_rϖ_{1,*}z⟩_r = ⟨y, A_{r+1}N_{r+1,r}z⟩_{r+1}` — legitimate
because A1 holds **on all of `H^1(X_1(N_gp^{r+1}))`**, not only on an image or on the ordinary part; and
`ϖ_{1,*}t = π_r(t)ϖ_{1,*}` to move `t_2,t_3` (with `ρ∘π_r = π_r∘ρ` on generators).
Here `N_{r+1,r} = Σ_{d ≡ 1 mod N_gp^r}⟨d⟩ ∈ Z_p[(Z/N_gp^{r+1})^×]` is the **native-level** norm element (A2).

**(3.2) The cycle tower (BCPV, printed).** `cor_DR_lemma_2_5_dual` (l.1421–1425), `Z_j = Δ^ét_j[a,b,c]`
with the Teichmüller-lifted index of 03 §4, whose level-`(r+1)` representative maps to the level-`r` one:

    ϖ_{1,*}^{⊗3} Δ^ét_{r+1}[e] = (U'_p)^{⊗3} Δ^ét_r[e].

**(3.3) Absorbing `(U'_p)^{⊗3}` (no constant, no rank factor).** With `U_pA_r = U_pW(U'_p)^r =
W(U'_p)^{r+1} = A_rU'_p` (from `WU'_p = U_pW`, BCPV (1.8)–(1.9); numerically (vi-c) in Lane 5's log), and
`pd^t_*U'_p = U'_ppd^t_*` (§2 `(C-U)`):

    Contr_r^{A_r}(b')( (U'_p)^{⊗3}y ) = U'_{p,(1)} · Contr_r^{A_r}( [t_2 ⊗ (U'_p)^2 t_3] )( y ).

One `U'_p` lands on the output factor; the other two combine on the carrier's third slot as `(U'_p)^2`
(the factor-2 one is transposed to `U_p` by the pairing and converted by `U_pA_r = A_rU'_p`).

**(3.4) Hom-valued D4 at both levels (04 Theorem 2) and Kummer injectivity.** Apply Theorem 2 at level
`r+1` to `Φ̄^mod_{r+1}`, push forward by `ϖ^{(1)}_{1,*}` (B1 F1: `Kum∘ϖ_{1,*} = H^1(T_pϖ_{1,*})∘Kum`, valid
because `ϖ_{1,*}: J^{(1)}_{r+1} → J^{(1)}_r` is a `Q`-rational homomorphism of abelian varieties), use
(3.1)–(3.3), then Theorem 2 at level `r`:

    Kum_{F'_{r+1}}( ϖ^{(1)}_{1,*} Φ̄^mod_{r+1}(b) ∘ (1⊗N) − U'_{p,(1)} Φ̄^mod_r( res^bal b )∘(1⊗(U'_p)^2) ) = 0 .

`Kum` is injective on `Ĵ^{(1)}_r(F'_{r+1})` (B1 F2), and the two sides are evaluated at the same
`b ∈ B^bal_{r+1}`, so the **point identity** holds in `Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`:

    (T)   ϖ^{(1)}_{1,*} ∘ Φ̄^mod_{r+1} ∘ (1⊗N_{r+1,r}) = U'_{p,(1)} ∘ Φ̄^mod_r ∘ res^bal_{r+1,r} ∘ (1⊗(U'_p)^2).

No class over `K_0` and no twisted `H^1` is needed for this step: injectivity is used over `F'_{r+1}`,
evaluationwise. (That both sides lie in the ⋆-invariants, i.e. in the ambient module
`Hom(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})^⋆` of B5/L1, is then automatic and is checked in 07.)

**(3.5) Normalization ⇒ the charter's relation.** With Lane 2's normalized point (B6 T3)
`Q_s := (U'_p)^{-s}_{(1)} ∘ Φ̄^mod_s ∘ (U'_p)^{-2s}_{carrier}` (`U'_p` invertible on `e'_ord`-parts),
`τ_r^MW(x) := ϖ^{(1)}_{1,*}∘x`, `π_r^*(x) := x∘res^bal_{r+1,r}`, and using centrality of `N_{r+1,r}` and
`U'_p`, `π_r(U'_p) = U'_p`, `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`:

    τ_r^MW(Q_{r+1}) ∘ (1⊗N_{r+1,r})
      = (U'_p)^{-(r+1)}_{(1)}[ϖ_{1,*}Φ̄^mod_{r+1}(1⊗N)](U'_p)^{-2(r+1)}
      = (U'_p)^{-(r+1)}_{(1)}U'_{p,(1)}Φ̄^mod_r ∘ res^bal ∘ (U'_p)^{2-2(r+1)}
      = (U'_p)^{-r}_{(1)} Φ̄^mod_r ∘ res^bal ∘ (U'_p)^{-2r}
      = π_r^* Q_r .

**Constant: exactly 1** (`δ♮_r = d_r = 1`), integrally, with the group-ring element `N_{r+1,r}` — not the
scalar `p` — on the carrier.

## §4. Independence of the choice of tame push-down (what 02a §1 asks for)

Let `pd^t ∈ {pr^t_1, pr^t_2}` and `pd^{t_f} ∈ {pr^{t_f}_1, pr^{t_f}_2}`, chosen once and used at **every**
level `s`. Every step of §3 used only:
(i) `pd^t_* ϖ_{1,*} = ϖ_{1,*} pd^t_*` and `pd^{t_f}_*ϖ_{1,*} = ϖ_{1,*}pd^{t_f}_*`;
(ii) `pd^t_* U'_p = U'_p pd^t_*`;
(iii) `pd^t_*⟨d⟩ = ⟨d mod N_gp^s⟩pd^t_*`;
(iv) A1 at the native tame level, applied to arbitrary classes.
Statements (i)–(iii) hold for **both** indices: the p-direction and tame-direction degeneracies are
independent prime directions (on points, `P ↦ pP` and `P ↦ tP` or the two quotients commute verbatim;
verified numerically for both indices, §2 `(C-W)`, `(C-U)`, `(C-D)`). Hence **(T), (3.5) and the constant 1
are unchanged by the choice**, and the verdict on item 3 does not depend on resolving 02a §1. Only the
*identity of the constructed point* depends on it (§5).

## §5. What the choice does change (recorded, not used)

By (★), with `pd^t = pr^t_1` the contracted functional is built from `(U_p)^r pr^t_{2,*}` applied to the
pre-`W` diagonal class, while with `pd^t = pr^t_2` it is built from `(U_p)^r pr^t_{1,*}`. The two points
differ by the tame-degeneracy interchange, which on an `h`-isotypic quotient (`h` new of level `N_hp^r`) is
multiplication by a tame Hecke scalar at the primes dividing `t`. That scalar is a *normalization*
constant of the eventual `f`/`g`-branch specialization; it is invisible to H9R16-C and must be fixed before
any statement that names `λ_{N_gp^r}(g)` or `a_p(g)^{±r}` (BCPV l.1561, l.1721–1728). It is carried into
the next gate (08), not resolved here.

## §6. Precision finding on the normalization exponents (correction to B5 (T♮_r) / Lane 5 `05` §4 wording)

The constant is 1 **only with the carrier normalization `(U'_p)^{-2s}` included**. With the factor-1
normalization alone — the literal form of B5's `(T♮_r)`:
`ϖ^{(1)}_{1,*}(U'_p)^{-(r+1)}Φ̄^mod_{r+1} = δ♮_r (U'_p)^{-r}Φ̄^mod_r∘res^bal` — the leftover is
`(1⊗(U'_p)^2)` on the carrier (3.3), i.e. `δ♮_r ≠ 1` for that normalization; the missing factor is exactly
BCPV's `a_p(g)^{-2r}` (`lemma_2023_11_14_1442`, l.1490: `a_p(f)^{-r}a_p(g)^{-2r}`) against their
`a_p(f)^{-r}` on the `f`-factor. The charter's own statement (item 3) uses Lane 2's `Q_r` (B6 T3), which
carries `(U'_p)^{-2r}` on the carrier and is therefore the correct normalization; **with it, `δ♮_r = 1`.**
Classification: wording defect in B5/Lane 5 `05` §4, not in the charter's target; no mathematical loss.

## §7. Verdict for item 3

**ITEM 3 = PROVED.**

> `τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^* Q_r` in `Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`,
> integrally, with constant 1, for either tame push-down used uniformly in `r`, `N_{r+1,r}` the native-level
> norm element; Kummer injectivity applied over `F'_{r+1}` evaluationwise.

Carried, not defects: the tame push-down is `NOT_PRINTED` in BCPV and is fixed here by the inherited
KLZ17/DR22 index convention (§1), with independence proved (§4); `H_π` is a standing input of the statement;
§5's tame Hecke scalar is a normalization for the next gate; §6 corrects the wording of B5's `(T♮_r)`.

ITEM3_STATUS = PROVED (constant 1; tame push-down decided and shown immaterial; A5 numerically confirmed)
