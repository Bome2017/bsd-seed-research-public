# Hostile source audit — good-ordinary definite anticyclotomic bridge

Scope: ordinary primes only. Everything downstream of `[c_2] != 0` is conditional, without exception.

Sources actually read at source for this audit (not project summaries):

* **[BLV]** M. Bertolini, M. Longo, R. Venerucci, *The anticyclotomic main conjectures for elliptic curves*,
  arXiv:2306.17784v2 (5 Feb 2026) — Hypotheses 1.1, Def. 1.3, Thm A, §4.2, §5 (5.2.1–5.2.5), §7.3 (Thm 7.1, Thm 7.3).
* **[BD-D]** M. Bertolini, H. Darmon, *Derived p-adic heights*, Amer. J. Math. **117** (1995) — §1.1 (assumptions 1–4,
  Prop. 1.1), §1.2 (Prop. 1.2, 1.3), Thm 2.7, Def. 2.15, Def. 2.16, Prop. 2.17, Thm 2.18, Def. 2.19, Def. 2.20,
  Rmk 2.21, Prop. 2.22, Thm 2.23, Cor. 2.24, Lemmas 2.25–2.27, §3 (Lemma 3.1, Conj. 3.3–3.9).

Labels used below, per the gate: **[THM]** proved theorem with citation; **[ALG]** standard algebraic identification
proved here, with the proof; **[COND]** conditional consequence of `[c_2] != 0`; **[CONJ]** conjecture;
**[UNSUP]** unsupported inference.

---

## TASK 1 — the BLV side

**1. The module.** [THM, BLV §7.3] In the definite case BLV set `X^eps_p(f) := Pontryagin dual of Sel^eps(K, A_f)`,
a compact torsion `Λ`-module by Theorem 7.1, and `Char^eps_p(f) :=` its characteristic power series. Here (BLV §5.2)

        T_f = T_f ⊗_{Z_p} Λ(eps_∞^{-1}),     A_f = Hom_cont(T_f, μ_{p^∞})^ι ,

`eps_∞ : G_K → Λ^*` the tautological character and `ι` Iwasawa's main involution. So `Sel(K, A_f)` is the Λ-adic
(Shapiro) avatar of a Selmer group of `E` over `K_∞`, with an `ι`-twisted Λ-structure.

**2. The local conditions** (BLV §5.2.5, with the parameters relevant to us: `k = ∞`, `L = 1`, `S = 1`, `g = f`,
`O = Z_p`, `P = 0`, `eps = ∅`). A class in `H^1(K, A_f)` lies in `Sel(K, A_f)` iff it is

* `∅`-finite at `p|p`: by BLV §5.2.1 with `eps = ∅`, `H^1_fin(K_{∞,p}, A_f) = E(K_{∞,p}) ⊗ Q_p/Z_p` under the Kummer
  map — i.e. **the classical Kummer condition**, not a Greenberg/strict/relaxed substitute;
* ordinary at `ℓ | N^-` (`L = 1`): `H^1_ord = Im(H^1(K_ℓ, A^{(ℓ)}_f) → H^1(K_ℓ, A_f))`, `A^{(ℓ)}_f` the `μ`-part of
  the Tate-curve filtration;
* **trivial** at `q | N^+`;
* finite (= unramified) outside `Np`.

**3. Ordinary case of Theorem A.** [THM] BLV adopt `eps = ∅` in the ordinary case (Introduction, "Conventions"), so
`L^∅_p(f) = L_p(f)` and `Char^∅_p(f) = Char_p(f)`. Theorem A (= Theorem 7.3 in the definite case) reads
`(L^eps_p(f)) ⊆ (Char^eps_p(f))`, **with equality in the non-exceptional case**.

**4. Non-exceptionality.** [THM] Definition 1.3: `(E,K,p,eps)` is exceptional iff `E` is **supersingular** at `p`,
`p` is **inert**, and `eps = +`. Good ordinary `p` is therefore never exceptional. So under Hypothesis 1.1 the
ordinary case always gives the **equality of principal ideals**

        (L_p(f)) = (Char_p(f))                                                     [THM]

— no divisibility is being substituted for equality.

**5. Normalizations.** [THM, BLV §4.2] BLV's ordinary definite construction is

        L_{g,n} = α_p(g)^{-n} Σ_{σ ∈ G_n} ( ψ_g(σ P_{n-1}) − α_p(g)·ψ_g(σ P_n) )·σ,
        L_g = lim_n L_{g,n},      L_p(g) = L_g · L_g^ι .

Since `Σ_{σ ∈ G_n} ψ_g(σ P_{n-1})σ = ν(θ_{n-1})` (the Gross point `P_{n-1}` is rational over `K_{n-1}`), one has
`L_{g,n} = −α_p^{-(n-1)}·( θ_n − α_p^{-1} ν(θ_{n-1}) )`, i.e. **BLV's square-root object is the retained branch's
α-stabilised theta element up to the unit `α_p^{-(n-1)}` and an index shift**, and BLV's `L_p(f)` is exactly the
project's `L_p = 𝓛_p·𝓛_p^ι`. A0 is therefore compatible with the BLV conventions; I did not need to reopen it.

**Consequence.** `Λ = Z_p[[T]]` is a domain and `I = (T)` is prime, so `ord_I` is additive on products, and
`ι : T ↦ −T/(1+T)` preserves `I` and acts on `I^k/I^{k+1} ≅ Z_p` by `(−1)^k`. If `[c_2] ≠ 0`, i.e. the `I^2/I^3`
coefficient of `𝓛_p` is a **unit**, then `L_p(f) ∈ I^4 \ I^5` with leading coefficient `(unit)^2 ∈ Z_p^×`, hence by
Theorem A

        ord_I Char_p(f) = 4,   with unit leading coefficient in I^4/I^5.          [COND]

Parity check (K5): `ord_I L_p = 2 ord_I 𝓛_p` is even. ✓

**Hypotheses, for this curve.** Hypothesis 1.1 additionally requires `p ∤ disc(K)`, i.e. **`p ≠ 7`** is excluded
along with the anomalous primes; `p ∤ h_K` is vacuous (`h(−7) = 1`); `ρ̄_{E,p}` surjective excludes finitely many `p`
(Serre, non-CM). Conditions (6), (7) hold for all `p ≥ 5` by the packet's checks, which I did not re-derive.

---

## TASK 2 — module identification

BD's object is [BD-D §2.5] `X_∞ = Hom_{Z_p}(Sel_{p^∞}(E/K_∞), Q_p/Z_p)` with `Sel_{p^n}(E/L)` the **classical**
Selmer group, defined in §1.2.1 by the local conditions `res_w(s) ∈ E(L_w)/p^n E(L_w)` at **every** place.
So the two modules must be compared **place by place**; "standardly equivalent" is not admissible (K3). Below,
`w` runs over places of `K_∞`; recall `K_∞/K` is ramified only above `p`.

**(a) Global condition.** Both are subgroups of `H^1(K_∞, E[p^∞])` cut out by local conditions only; no auxiliary
global constraint on either side. Note `Sel_{p^∞}(E/K_∞) = colim_n Sel_{p^∞}(E/K_n)`, whose local condition at `w` is
`Im(E(K_{∞,w}) ⊗ Q_p/Z_p)`. ✓ same shape.

**(b) At `v | p`.** BLV (`eps = ∅`) *define* the finite subgroup to be `E(K_{∞,p}) ⊗ Q_p/Z_p` under the Kummer map
(§5.2.1). This is literally the classical condition. **No Coates–Greenberg comparison is needed**, and no
Greenberg/strict/relaxed discrepancy arises. ✓ identical.

**(c) At `q | N^+`.** BLV impose the **trivial** condition. Classically the condition is `Im(E(K_{∞,w})⊗Q_p/Z_p)`,
and for `w ∤ p` one has `E(K_{∞,w}) ⊗ Q_p/Z_p = 0` (`E(K_{∞,w})` is an extension of a finite group by a pro-`q`
group, and both are killed by `⊗ Q_p/Z_p` for `p ≠ q`). ✓ identical. [ALG]

**(d) Outside `Np`.** BLV impose the unramified condition `H^1(G_w/I_w, A^{I_w})`. At a place of good reduction with
`w ∤ p`, `H^1_{unr}(K_w, E[p^n]) = E(K_w)/p^n E(K_w)`, hence in the limit
`H^1_{unr}(K_w, E[p^∞]) = colim_n E(K_w)/p^n = E(K_w) ⊗ Q_p/Z_p = 0`, which is again the classical condition; the
same computation applies at each place of `K_∞` above `w` (the tower is unramified there). ✓ identical. [ALG]

**(e) At `ℓ | N^-`** — the only place where a real discrepancy could hide, and the one to check by hand. `ℓ` is
inert in `K`, so `K_ℓ/Q_ℓ` is the unramified quadratic extension and `E/K_ℓ` is a **split** Tate curve, with
`0 → μ_{p^∞} → E[p^∞] → Q_p/Z_p → 0`; also `ℓ` splits completely in `K_∞/K`, so `K_{∞,λ} = K_λ`. Then

* classical condition: `E(K_λ) ⊗ Q_p/Z_p = 0` (as in (c)) — the trivial subgroup;
* BLV condition: `H^1_ord = Im(H^1(K_λ, μ_{p^∞}) → H^1(K_λ, E[p^∞]))`. Kummer theory gives
  `H^1(K_λ, μ_{p^∞}) = K_λ^× ⊗ Q_p/Z_p ≅ Q_p/Z_p` (units contribute `0` since `p ≠ ℓ`; the valuation survives), and
  the connecting map `H^0(K_λ, Q_p/Z_p) = Q_p/Z_p → K_λ^× ⊗ Q_p/Z_p` is cup product with the Tate period, i.e.
  multiplication by `v_λ(q_ℓ) = v_ℓ(Δ)` under the valuation identification. For our curve
  `v_ℓ(Δ) = 2, 1, 2` at `ℓ = 3, 2243, 5843`, a **`p`-adic unit for `p ≥ 5`**, so the connecting map is onto and
  `H^1_ord(K_λ, E[p^∞]) = 0`.

  ✓ identical **given `p ∤ v_ℓ(Δ)` for `ℓ | N^-`** — which holds here for every `p ≥ 5`, but is a genuine
  hypothesis of the comparison and should be carried. (The Λ-adic statement is the same computation: `G_{K_λ}` acts
  trivially on the Λ-factor because `ℓ` splits completely in `K_∞`.) [ALG]

**(f) Imprimitive Euler factors.** None are present in the instance we use: BLV's imprimitivity parameters are
`S` (extra trivial conditions) and `L` (level-raising primes), and the object entering `Char_p(f)` is the case
`S = 1`, `L = 1`, `g = f`. ✓

**(g) Duals and twists.** Both sides take the Pontryagin dual. The only structural difference is the `ι`-twist built
into `A_f = Hom_cont(T_f ⊗ Λ(eps_∞^{-1}), μ_{p^∞})^ι`: Shapiro's lemma identifies `Sel(K, A_f)` with
`Sel_{p^∞}(E/K_∞)` as groups, with the Λ-action composed with `ι`. Hence

        X^∅_p(f) = (X_∞)^ι,       Char_p(f) = ι( char(X_∞) ).

`ι` is a ring automorphism of `Λ` preserving `I`, so `ord_I Char_p(f) = ord_I char(X_∞)`, and on `I^4/I^5` it acts by
`(−1)^4 = +1`, so the normalized leading coefficients agree exactly. ✓ completely controlled.

**(h) Finite / pseudo-null corrections.** None enter: the comparison (b)–(e) is an equality of local conditions at
every place, hence an equality of Selmer groups, not merely up to finite index. The control statement BD need is
their own Lemma 2.26 Step 1 (`X_∞/J_n X_∞ = Sel_{p^n}(E/K_n)^dual`, using `E[p](K_∞) = 0`, which holds since
`Q(E[p])/Q` has group `GL_2(F_p)`, nonsolvable for `p ≥ 5`, while `K_∞/Q` is dihedral).

**(i) Standing hypotheses of BD vs BLV.** BD-D §1.1 requires: (1) `p ∤ 2·#(E/E^0)` over `O_K`; (2) good reduction
above `p`; (3) the image of `ρ_p` contains a Cartan subgroup; (4) surjectivity of the local norm maps
`E((K_n)_v) → E(K_v)` for all `v`, all `n`. For our data: (1) holds for `p ≥ 5` (component groups over `O_K` have
order dividing `v_ℓ(Δ) ∈ {1,2}` at `ℓ | N^-` and `≤ 4` at the additive places `2`, `4547`, which are split so
`K_w = Q_w`); (2) is `p ∤ N`; (3) follows from surjectivity of `ρ̄_{E,p}` (BLV Hyp. 1.1(3)); (4) follows from
BD-D Prop. 1.1, whose hypothesis is that at the primes ramified in `K_∞/K` — i.e. exactly `v | p` — `E` is ordinary
and `p ∤ #E(F_v)`. Since `#E(F_{p^2}) ≡ 1 − a_p^2` and `#E(F_p) ≡ 1 − a_p (mod p)`, this is **verbatim BLV
Hypothesis 1.1(5)**, the non-anomalous condition. So BD's assumptions cost **no primes beyond those BLV already
excludes**. [ALG]

**Verdict for Task 2: `MODULE_IDENTIFICATION_PROVED`** — BLV's characteristic module is the `ι`-twist of BD's
`X_∞`, the twist being an automorphism of `Λ` that preserves `I`, `ord_I` and (in degree 4) the normalized leading
coefficient. Carried hypotheses: `p ≥ 5`, `p ∤ N`, `p ∤ v_ℓ(Δ)` for `ℓ | N^-`, `E[p](K_∞) = 0`, plus BLV
Hypothesis 1.1.

---

## TASK 3 — the derived-height order inequality

**Thm 2.7** [BD-D]. For `1 ≤ k ≤ p−1` there are canonical pairings `⟨,⟩_k : Sel^{(k)} × Sel^{(k)} → I^k/I^{k+1}` on
`Sel = Sel_{p^n}(E/K)` with `Sel^{(k)} = Sel ∩ (γ−1)^{k−1} Sel_{p^n}(E/K_n)`; `(−1)^{k+1}`-symmetric; `Sel^{(k+1)}` is
the null-space of `⟨,⟩_k`; the norm space lies in every null-space.

**Def. 2.15 / 2.16, Prop. 2.17, Thm 2.18** [BD-D]. `S_p(E/K) = lim_n Sel_{p^n}(E/K)`, `S_p^{(k)} = lim_n Sel_n^{(k)}`,
`S̄_p^{(k)} = ` its `p`-adic saturation in `S_p(E/K)`; the derived heights `⟨⟨,⟩⟩_k : S̄_p^{(k)} × S̄_p^{(k)} →
I^k/I^{k+1} ⊗ Q` satisfy: `(−1)^{k+1}`-symmetry; `S̄_p^{(k+1)}` **is** the null-space of `⟨⟨,⟩⟩_k`; universal norms lie
in all null-spaces; `⟨⟨,⟩⟩_1|_{E(K)_p}` is the Mazur–Tate/Schneider height; and **(5)** `p^{A_k}⟨⟨,⟩⟩_k` is integral,
where `p^{A_k}` is the exponent of the finite group `S̄_p^{(k)}/S_p^{(k)}`. Note item (5): the derived heights are
**`Q`-valued in general**, with denominators bounded only by the saturation index. This is the fact that will
decide Task 7.

**Thm 2.23** [BD-D]. With `X_∞` Λ-torsion, `σ_p := ord_I char(X_∞)`, `ρ_p := Σ_{k=1}^{p} rank_{Z_p} S̄_p^{(k)}`:
`σ_p ≥ ρ_p` and, in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`,
`L̄_∞ = #( Ш(E/K)_{p^∞} / Div Ш(E/K)_{p^∞} )·R_der`.
(The printed statement says "greater than"; the proof establishes `≥`, and the symbol `σ_p` is reused inside the
proof for the filtration sum `d_1 + 2d_2 + ⋯ + p d_p = Σ_k rank S̄_p^{(k)}`. This is a notational collision in the
source, not a mathematical gap.) The inequality is proved by exhibiting
`det(⟨x'_i, y'_j⟩) ∈ I_n^{Σ_k k d_k}` at every finite layer, via Lemmas 2.25/2.26 (Fitting ideal = characteristic
ideal, and control `μ_n(char X_∞) = Fitt_{Λ_n}(Sel_{p^n}(E/K_n)^dual)`). It requires only BD §1.1 (1)–(4) and
`X_∞` Λ-torsion. ✓

**Item 1 — the first height pairs only opposite `τ`-eigenspaces.** [THM, BD-D Lemma 3.1]
`⟨⟨τs_1, τs_2⟩⟩_k = (−1)^k ⟨⟨s_1, s_2⟩⟩_k`, proved from Galois equivariance of the local Tate pairing and the fact
that `*` acts on `I^k/I^{k+1}⊗Q` by `(−1)^k`. **Hostile caveat:** Lemma 3.1 sits in Chapter 3, whose opening
paragraph assumes `Ш(E/K)_{p^∞}` finite — a *forbidden* hypothesis here. Its proof does not use that assumption
(it uses only equivariance of the Tate pairing and the definition of `⟨⟨,⟩⟩_k`), and the same one-line argument
applies verbatim at each finite layer to `⟨,⟩_{k,n}`. So it is usable, but must be re-derived rather than cited
blindly. [ALG, re-derived]

Consequently, for odd `p`, `⟨⟨,⟩⟩_1 ≡ 0 on S^+ × S^+` and on `S^- × S^-`.

**Item 2 — `rank S̄^{(2)} ≥ |s^+ − s^-|`.** [THM] BD state exactly this immediately after Lemma 3.1 ("the null-space
of `⟨⟨,⟩⟩_1` has rank at least `|r^+ − r^-|`"), with `r^±` there denoting the ranks of `S_p(E/K)^±` — the *Selmer*
ranks, i.e. our `s^±`, not Mordell–Weil ranks. ✓

**Item 3 — the order formula counts the filtration ranks.** ✓ `ρ_p = Σ_{k=1}^{p} rank S̄_p^{(k)} = Σ_k k d_k`, and
`σ_p ≥ ρ_p ≥ rank S + rank S̄^{(2)}`.

**Item 4 — omitted higher terms.** They can only *increase* `ρ_p`; dropping `k ≥ 3` weakens the inequality in the
safe direction. ✓

**Item 5 — truncation at `p`.** The pairings exist for `k ≤ p−1` and the filtration is indexed `k ≤ p`. We use only
`k = 1, 2`, and `p ≥ 5`. ✓

**Verdict for Task 3.** The chain

        σ ≥ rank_{Z_p} S + rank_{Z_p} S̄^{(2)} ≥ (s^+ + s^-) + |s^+ − s^-| = 2 max(s^+, s^-)

**is exactly what the source proves**, given (i) `X_∞` Λ-torsion, (ii) BD §1.1 (1)–(4), (iii) Lemma 3.1 re-derived
without the Chapter-3 finiteness assumption. `BD_ORDER_INEQUALITY = PROVED` (with `X_∞` torsion supplied
conditionally by `[c_2] ≠ 0` + Task 1 + Task 2). Note this is *not* BD Conjecture 3.7, which asserts the
corresponding **equality** and is conjectural; only the `≥` direction is used, and that is a theorem.

---

## TASK 4 — the `τ`-eigenspace bridge for pro-`p` Selmer and `T_p Ш`

Let `Δ = Gal(K/Q) = {1, τ}`, `p` odd, `χ` the quadratic character of `K`, `D = −7`, `E^D = E^{-7}`.

**Step 1 (Galois cohomology).** For any `Z_p[Δ]`-module, `e^± = (1 ± τ)/2` are idempotents and `M = M^+ ⊕ M^-`.
`H^i(Δ, −)` is killed by `2` and, on `p`-primary modules, by `p^n`; hence it vanishes. Inflation–restriction gives
`H^1(Q, E[p^n]) ≅ H^1(K, E[p^n])^Δ = H^1(K, E[p^n])^+`. Over `Q`, `E^D[p^n] ≅ E[p^n] ⊗ χ`, and restriction to `K`
kills `χ`; the transported `Δ`-action differs by `χ(τ) = −1`, so
`H^1(Q, E^D[p^n]) ≅ H^1(K, E[p^n])^-`.

**Step 2 (local conditions).** The same vanishing applies place by place. For `v` split in `K`,
`⊕_{w|v} E(K_w)/p^n = E(Q_v)/p^n ⊕ E(Q_v)/p^n` with `τ` swapping the summands, so each eigenspace is
`E(Q_v)/p^n = E^D(Q_v)/p^n` (`D` is a square in `Q_v`). For `v` inert or ramified, `K_w/Q_v` is quadratic and, `p`
being odd, `(E(K_w)/p^n)^+ = E(Q_v)/p^n` and `(E(K_w)/p^n)^- = E^D(Q_v)/p^n`, using
`E^D(Q_v) ⊗ Z_p = {P ∈ E(K_w) : P^τ = −P} ⊗ Z_p`. Hence the eigen-decomposition of Step 1 matches the Selmer
conditions, and

        Sel_{p^n}(E/K)^+ ≅ Sel_{p^n}(E/Q),        Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^D/Q),

compatibly with the maps `m_p` used to form the inverse limit. [ALG]

**Step 3 (pro-`p` Selmer and `T_p Ш`).** Taking `lim_n` (exact on the finite groups involved, and `e^±` commute
with the transition maps):

        S := S_p(E/K),   S^- ≅ S_p(E^D/Q) = lim_n Sel_{p^n}(E^D/Q),
        0 → E^D(Q) ⊗ Z_p → S_p(E^D/Q) → T_p Ш(E^D/Q) → 0 .

This is the statement about the **Selmer / `T_pШ`** objects that the task demands; it is not the Mordell–Weil
decomposition, although the latter is its `E(K) ⊗ Z_p` sub-quotient.

**Step 4 (input of the certificate).** `L(E^{-7},1) ≠ 0` gives, by the retained analytic-rank-zero
Gross–Zagier–Kolyvagin theorem, `rank E^{-7}(Q) = 0` and `Ш(E^{-7}/Q)` **finite**. Therefore
`E^D(Q) ⊗ Z_p` has rank `0` and `T_p Ш(E^D/Q) = 0` (the Tate module of a finite group). Since `E(K)[p] = 0`
(`ρ̄_{E,p}` surjective) the module `S` is `Z_p`-free, so a rank-zero direct summand is zero:

        s^- = rank_{Z_p} S^- = 0,   and in fact  S^- = 0.                          [ALG + certificate]

Also `Ш(E/K)[p^∞]^- ≅ Ш(E^{-7}/Q)[p^∞]` and `Ш(E/K)[p^∞]^+ ≅ Ш(E/Q)[p^∞]` by the same comparison applied to the
descent sequence. **Record this: it will be decisive in Task 7.**

`TWIST_MINUS_EIGENSPACE = PROVED` (standard identification, proved here; uses the certificate as input, nothing
else).

---

## TASK 5 — replay of the live-configuration enumeration

With `d^± = corank_{Z_p} Div Ш(E/K)[p^∞]^± = rank_{Z_p} T_pШ(E/K)^±`, and `rank (E(K)⊗Z_p)^+ = rank E(Q) = 2`:

        s^+ = 2 + d^+,      s^- = r^- + d^- .

Given `σ = 4` and `σ ≥ 2 max(s^+, s^-)` one gets `s^+ ≤ 2` and `s^- ≤ 2`, hence `d^+ = 0` **forced**, and exactly the
six rows of the packet's table survive:

| `d^+` | `r^-` | `d^-` | `s^+` | `s^-` | `2max` | `Div Ш` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 2 | 0 | 4 | 0 |
| 0 | 0 | 1 | 2 | 1 | 4 | ≠ 0 |
| 0 | 0 | 2 | 2 | 2 | 4 | ≠ 0 |
| 0 | 1 | 0 | 2 | 1 | 4 | 0 |
| 0 | 1 | 1 | 2 | 2 | 4 | ≠ 0 |
| 0 | 2 | 0 | 2 | 2 | 4 | 0 |

Independently confirmed: **`τ`-equivariance plus `σ = 4` alone does not give `Div Ш = 0`** — rows 2, 3, 5 survive it.
The minus-side input is genuinely needed, and it is the certificate (Task 4) that supplies `s^- = 0`, deleting every
row but the first. Any verdict reaching finiteness from `σ = 4` alone would be invalid; this audit does not.

---

## TASK 6 — A2a: does certificate + order 4 kill the divisible part?

Assume `[c_2] ≠ 0`, Task 2, hence `σ = ord_I char(X_∞) = 4` with unit leading coefficient; assume the Task-3
inequality; and use `s^- = 0` from Task 4.

Since `S = S^+` (Task 4, Step 4) and `⟨⟨,⟩⟩_1` vanishes on `S^+ × S^+` (Lemma 3.1, `p` odd), `⟨⟨,⟩⟩_1 ≡ 0` on `S`;
by Thm 2.18(2) the null-space is all of `S`, so `S̄^{(2)} = S` and

        4 = σ ≥ rank S + rank S̄^{(2)} = 2 s^+ = 2(2 + d^+)   ⟹   d^+ = 0 .

With `d^- = 0` from the certificate, `T_p Ш(E/K) = T_pШ^+ ⊕ T_pШ^- = 0`, i.e.

        Div Ш(E/K)[p^∞] = 0,   equivalently  Ш(E/K)[p^∞] is FINITE.               [COND]

No forbidden input was used: finiteness of `Ш(E/K)[p^∞]` is the *output*; no height non-degeneracy was assumed
(indeed `⟨⟨,⟩⟩_1 ≡ 0` here); no `T_pШ = 0` assumption, no BSD, no rank-two Heegner index.

Theorems that make it work: **BLV Thm A (ordinary, non-exceptional) + Task-2 comparison** for `σ = 4`;
**BD-D Thm 2.23 (`σ_p ≥ ρ_p`) + Thm 2.18(2) + Lemma 3.1** for the inequality; **the twist identification of Task 4 +
the `D = −7` certificate + GZK at analytic rank 0** for `s^- = 0`. `A2a_DIVISIBLE_SHA = PROVED (conditional on
[c_2] ≠ 0)`.

---

## TASK 7 — A2b: from the unit leading coefficient to `Ш(E/K)[p^∞] = 0`

**The exact source statement** (BD-D Thm 2.23), in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`:

        L̄_∞ = # ( Ш(E/K)_{p^∞} / Div Ш(E/K)_{p^∞} ) · R_der ,

with `R_der = R^{(1)}···R^{(p−1)}` (Def. 2.20), `R^{(k)} = det(⟨⟨s_i,s_j⟩⟩_k)` on a filtration-compatible basis of
`S̄^{(k)}/S̄^{(k+1)}`; `R_der := 0` if `⟨⟨,⟩⟩_{p−1}` is degenerate. Cor. 2.24: (1) if `⟨⟨,⟩⟩_{p−1}` is non-degenerate
then `σ_p = ρ_p`; (2) `p^B R_der` is integral, where `p^B = #(Ш/Div Ш)`. Rmk 2.21: *if `Ш(E/K)_{p^∞}` is finite*,
using an integral Mordell–Weil basis and the change-of-basis matrix `M`, `R_der := det(M)^{-2}R^{(1)}···R^{(p−1)}`
"is well-defined in `I^{ρ_p}/I^{ρ_p+1}` (not just up to a `p`-adic unit) and does not depend on the choice of `M`".

**1. Our filtration.** By Task 6, `Ш(E/K)[p^∞]` is finite, so `S = E(K) ⊗ Z_p ≅ Z_p^2`, `S = S̄^{(1)} = S̄^{(2)}`
(as `⟨⟨,⟩⟩_1 ≡ 0`), so `d_1 = 0`, and `ρ_p ≥ 2 + 2 = 4 = σ ≥ ρ_p` forces `ρ_p = 4`, `rank S̄^{(3)} = 0`, hence
`S̄^{(3)} = 0` (a saturated submodule of a free module of rank 0). Thus `d_2 = 2`, all higher `d_k = 0`,
`⟨⟨,⟩⟩_{p−1}` is (vacuously) non-degenerate and `Cor. 2.24(1)` returns `σ_p = ρ_p = 4`, consistently. And
`R_der = R^{(2)} = ⟨⟨P_1, P_2⟩⟩_2^2` for an integral basis `P_1, P_2` of `E(K)/tors` (`M = Id`, since with `d_1 = 0`
every basis is filtration-compatible). So the formula specializes to

        unit  =  # Ш(E/K)[p^∞] · ⟨⟨P_1, P_2⟩⟩_2^2   in  (I^4/I^5 ⊗ Q)/Z_p^× .      [COND]

**2. Where `R_der` lives, and when it is integral.** `⟨⟨,⟩⟩_2` takes values in `I^2/I^3 ⊗ Q`; by **Thm 2.18(5)**
only `p^{A_2}⟨⟨,⟩⟩_2` is guaranteed integral, `p^{A_2}` being the exponent of `S̄^{(2)}/S_p^{(2)}`. Remark 2.21
*asserts* integrality in the `Ш`-finite case but **gives no proof**, and no other statement in the paper supplies
one in the degenerate regime: Cor. 2.24(2) only gives `#(Ш/DivŠ)·R_der` integral, which is precisely the product
we are trying to split. So the step "unit product ⟹ both factors are units" is **not licensed by the source as it
stands**.

**3. What can be proved.** I can bound the denominator. Let `p^c` be the exponent of `Sel_{p^∞}(E^{-7}/Q)`; by the
certificate `Sel_{p^∞}(E^{-7}/Q) = Ш(E^{-7}/Q)[p^∞]` is finite, so `c < ∞`, and by Task 4,
`Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^{-7}/Q)` is killed by `p^c` for every `n`. Let `s ∈ Sel_{p^n}(E/K)^+`. For
`t = t^+ + t^-`: `⟨s, t^+⟩_{1,n} = 0` by the finite-layer form of Lemma 3.1 (`p` odd), and
`⟨p^c s, t^-⟩_{1,n} = ⟨s, p^c t^-⟩_{1,n} = 0`. Hence `p^c Sel_n^+ ⊆ Sel_n^{(2)}` for all `n`, and in the limit
`p^c S ⊆ S_p^{(2)}`, i.e.

        A_2 ≤ c,   so   v_p(R_der) ≥ −2c,   and   v_p( # Ш(E/K)[p^∞] ) ≤ 2c .      [ALG]

In particular:

* **If `p ∤ # Ш(E^{-7}/Q)`** then `c = 0`, `S_p^{(2)} = S = S̄^{(2)}`, `⟨⟨,⟩⟩_2` is integral on `S`, `R_der` is
  integral, and the unit product forces `v_p(#Ш(E/K)[p^∞]) = 0`, i.e. — the group being a finite `p`-group —

        Ш(E/K)[p^∞] = 0 .                                                          [COND]

* **If `p | # Ш(E^{-7}/Q)`** the conclusion is not merely unproved, it is **false**: by Task 4,
  `Ш(E/K)[p^∞] ⊇ Ш(E/K)[p^∞]^- ≅ Ш(E^{-7}/Q)[p^∞] ≠ 0`. At such a prime the Thm 2.23 identity is still consistent,
  with `v_p(R_der) < 0` absorbing the `Ш`-factor — which is exactly the possibility Remark 2.21's unproved
  integrality assertion would exclude.

Since `Ш(E^{-7}/Q)` is finite (certificate), only finitely many primes are affected, but **no statement in the
record identifies them**, and the target was quantified over *every* good-ordinary `p` satisfying the hypotheses.

**Answers to the checklist.** (1) `R_der` lives in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×` — a **rational** line, not a
lattice; Rmk 2.21 asserts, without proof, integrality when `Ш` is finite. (2) Integrality is guaranteed by the
source only after multiplication by `p^{A_k}` (Thm 2.18(5)) or by `#(Ш/DivШ)` (Cor. 2.24(2)); here it holds outright
iff `A_2 = 0`, for which `p ∤ #Ш(E^{-7}/Q)` is a sufficient condition proved above. (3) Yes — vanishing of the
divisible part makes `Ш[p^∞]` finite (Task 6). (4) `#(Ш/Div Ш)` has non-negative valuation trivially; `R_der` does
**not** provably have non-negative valuation. (5) Therefore a unit leading coefficient does **not**, by itself,
force `v_p(#Ш(E/K)[p^∞]) = 0`. (6) Consequently `Ш(E/K)[p^∞] = 0` follows only under the extra hypothesis of (2).

---

## PRINCIPAL VERDICT

### `LEADING_TERM_STEP_FAILS`

Tasks 1–6 go through, conditionally on `[c_2] ≠ 0`: module identification holds, the order inequality is what the
source proves, the certified twist input rigorously gives `s^- = 0`, and `σ = 4` then forces
`Div Ш(E/K)[p^∞] = 0`, i.e. `Ш(E/K)[p^∞]` **finite**. The chain breaks at the passage from the unit leading
coefficient to vanishing.

**First missing implication** (state it exactly, nothing downstream):

> For the good-ordinary primes `p` under consideration, the derived regulator of Bertolini–Darmon,
> `R_der = ⟨⟨P_1,P_2⟩⟩_2^2 ∈ (I^4/I^5 ⊗ Q)/Z_p^×`, computed on an integral basis of `E(K)/tors` in the degenerate
> regime `⟨⟨,⟩⟩_1 ≡ 0`, satisfies `v_p(R_der) ≥ 0` — equivalently, `S_p^{(2)} = lim_n (Sel_{p^n}(E/K) ∩ (γ−1)
> Sel_{p^n}(E/K_n))` is `p`-saturated in `S_p(E/K)`, i.e. `A_2 = 0` in Thm 2.18(5).

This is asserted by BD Remark 2.21 without proof and is not delivered by Theorem 2.23, Theorem 2.18(5) or
Corollary 2.24(2).

**Strongest correct replacement, proved in this audit.** Conditional on `[c_2] ≠ 0` and BLV Hypothesis 1.1 (so
`p ≥ 5`, `p ∤ 7N`, `ρ̄_{E,p}` surjective, `a_p` non-anomalous), plus the certified `D = −7` input:

* `Ш(E/K)[p^∞]` is **finite** and `v_p(#Ш(E/K)[p^∞]) ≤ 2c`, `p^c` the exponent of `Ш(E^{-7}/Q)[p^∞]`;
* if moreover **`p ∤ # Ш(E^{-7}/Q)`**, then `Ш(E/K)[p^∞] = 0`;
* if `p | # Ш(E^{-7}/Q)`, then `Ш(E/K)[p^∞] ≠ 0`, so the unrestricted statement is not merely unproved but **false**
  at such `p`. The bridge must therefore be re-stated with the side condition `p ∤ # Ш(E^{-7}/Q)`, and the finite
  exceptional set determined (it is finite because the certificate makes `Ш(E^{-7}/Q)` finite).

Nothing here is certified: every item after `[c_2] ≠ 0` is conditional on it.

---

## LEDGER

        MODULE_IDENTIFICATION   = PROVED        (explicit place-by-place comparison; BLV Char_p(f) = ι(char X_∞);
                                                 carried hypotheses p >= 5, p ∤ N, p ∤ v_l(Δ) for l | N^-)
        BD_ORDER_INEQUALITY     = PROVED        (BD-D Thm 2.23 proof + Thm 2.18(2) + Lemma 3.1 re-derived without
                                                 the Chapter-3 Ш-finiteness assumption; needs X_∞ Λ-torsion,
                                                 supplied conditionally by [c_2] != 0)
        TWIST_MINUS_EIGENSPACE  = PROVED        (algebraic identification proved here for Sel, S_p and T_pШ;
                                                 with the certificate gives s^- = 0 and Div Ш^- = 0)
        A2a_DIVISIBLE_SHA       = PROVED        [CONDITIONAL on [c_2] != 0]  d^+ = d^- = 0, Div Ш(E/K)[p^∞] = 0,
                                                 hence Ш(E/K)[p^∞] finite; no forbidden hypothesis used
        A2b_LEADING_TERM        = FAILS         missing: v_p(R_der) >= 0 (BD Rmk 2.21 asserted, not proved).
                                                 Holds, with proof, when p ∤ #Ш(E^{-7}/Q); false when p | #Ш(E^{-7}/Q)
        ORDINARY_BRIDGE         = NOT PROVED    as universally quantified over good-ordinary p; proved conditionally
                                                 on [c_2] != 0 for all such p with p ∤ #Ш(E^{-7}/Q)

Out of scope and untouched: supersingular signed modules (A3), the anomalous-prime problem (B), the proof of
`[c_2] != 0`, the numerical `D = −7` certificate, `FIN`, `FORMULA`, full BSD.
