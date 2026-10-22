# Ordinary anticyclotomic bridge — hostile source audit

Scope: good-ordinary primes only, for the fixed curve of the project record, `K = Q(sqrt -7)`,
`N^- = 3·2243·5843` (definite), conditional on `[c_2] ≠ 0`.  Supersingular primes, the anomalous
prime problem, the proof of `[c_2] ≠ 0` and the numerical `D = -7` certificate are out of scope and
are not reopened.

Sources actually read at source for this audit:

* **BLV** = M. Bertolini, M. Longo, R. Venerucci, *Iwasawa main conjectures for the anticyclotomic
  `Z_p`-extension* (arXiv:2306.17784, revision of 5 Feb 2026 = the Math. Ann. version); read from the
  authors' LaTeX source.  References below are to the numbered statements of that file
  (Hypothesis 1.1 = `thehy`, Definition 1.3 = `def:exceptional`, Theorem A, Hypothesis `controlass`,
  §`selsec`, §`locsec`, Lemma `control nminus`, Lemma `control nplus`, Proposition `global control`,
  Theorem `BSD0`, §`def:definite_char` = Theorem `Adef`).
* **BD-DH** = M. Bertolini, H. Darmon, *Derived p-adic heights*, Amer. J. Math. **117** (1995),
  1517–1554 (both the authors' preprint file and the published version were read; the wording of
  Remark 2.21 is identical in the two).
* **BD05** = M. Bertolini, H. Darmon, Annals 2005, Corollary 3 — retained as a source-checked input
  per `INPUTS.md` §5; not re-derived here.

Labels used throughout, as required by `GATE.md` K4:

* **[T]** proved theorem, with citation;
* **[A]** standard algebraic identification that I verified myself, with the argument given;
* **[C]** conditional consequence of `[c_2] ≠ 0`;
* **[?]** conjecture / assertion without proof in the source;
* **[X]** unsupported inference.

---

## 0. Notation fixed for the audit

`Λ = Z_p[[G_∞]]`, `G_∞ = Gal(K_∞/K)`, `γ` a topological generator, `I = (γ-1)Λ` the augmentation
ideal, `ι` the Iwasawa involution `g ↦ g^{-1}`.

`S = S_p(E/K) = lim_n Sel_{p^n}(E/K)` (BD-DH Definition 2.15.1), with
`0 → E(K) ⊗ Z_p → S → T_p Ш(E/K) → 0`, and `s^± = rank_{Z_p} S^±` for the idempotents
`e^± = (1±τ)/2`, `τ` a complex conjugation.

`X_∞ = Hom(Sel_{p^∞}(E/K_∞), Q_p/Z_p)` (BD-DH §2.5), `σ = ord_I char(X_∞)`,
`ρ_p = Σ_{k=1}^{p} rank_{Z_p} S̄_p^{(k)}` (BD-DH §2.4, after Definition 2.19).

`𝔛_p^∅(f) = ` Pontryagin dual of `Sel_∅(K, **A**_f)` and `Char_p^∅(f) = char(𝔛_p^∅(f))`
(BLV §`def:definite_char`).

---

## TASK 1 — the BLV side

**1. The module.**  BLV §`def:definite_char`: *"Let `𝔛_p^ε(f)` be the Pontryagin dual of
`Sel_ε(K, **A**_f)`, which is a compact torsion `Λ`-module by Theorem `BSD0`.  Denote
`Char_p^ε(f)` the characteristic power series of `𝔛_p^ε(f)`."*  So the module is the Pontryagin
dual (`Hom(-, Q_p/Z_p)`, no further twist at this point) of the **discrete** Selmer group
`Sel_ε(K, **A**_f) = Sel^1_ε(K, **A**_f)` of §`Sec.DCSelmer` with `S = 1`, `L = 1`, `𝔓 = 0`,
`𝒪 = Z_p`.  In the ordinary case `ε = ∅` by the convention of §`locsec`.  **[T]**

**2. All local conditions** (BLV §`Sec.DCSelmer`, verbatim): classes in `H^1(K, **A**_f)` which are

* `ε`-finite at primes dividing `p`.  For `ε = ∅` this is
  `H^1_fin(K_{∞,𝔭}, A_f) = E(K_{∞,𝔭}) ⊗ Q_p/Z_p` (§`subsec-p`), i.e. the classical Kummer
  condition — *not* a Greenberg "strict" condition (the identification of the two in the ordinary
  case is BLV equation (`eq:ord1`), quoting Greenberg, Proposition 2.4 of [Gr-1]);
* **ordinary** at primes dividing `L N^-`, i.e. (with `L = 1`) at `ℓ | N^-`:
  `H^1_ord(K_ℓ, **A**) = Im(H^1(K_ℓ, **A**^{(ℓ)}) → H^1(K_ℓ, **A**))` where `**A**^{(ℓ)}` is the
  sub-object coming from the Tate-curve filtration `0 → T^{(ℓ)}(≅ Z_p(1)) → T → T^{[ℓ]}(≅ Z_p) → 0`
  (§`subsec-N^-`);
* **trivial** (`res_w = 0`) at primes dividing `S N^+`, i.e. at `w | N^+`;
* finite (= unramified, `H^1(G_w/I_w, M^{I_w})`) outside `S L N p` (§`subsec-outside`).

**[T]**

**3. The ordinary case of Theorem A.**  Theorem A reads
`(L_p^ε(f)) ⊆ (Char_p^ε(f))`, *with equality in the non-exceptional case*; in the definite case
this is Theorem `Adef`, deduced from Theorem `BSD0` by the Mazur–Rubin/Howard limit argument.
The convention `ε = ∅` in the ordinary case is fixed in the Introduction ("we adopt the convention
that `ε = ∅` in the ordinary case … then in particular `L_p(f) = L_p^ε(f)`").  **[T]**

**4. Is the ordinary case always non-exceptional?**  Definition 1.3: *"`(E,K,p,ε)` is exceptional if
`E` has supersingular reduction at `p`, `p` is inert in `K` and `ε = +`."*  The three conditions are
conjunctive and the first already fails at good-ordinary `p`.  **Yes — at ordinary `p` the
exceptional case cannot occur, for `p` split or inert.**  **[T]**

**5. Equality of principal ideals.**  Consequently, for our curve at any `p` satisfying
Hypothesis 1.1, Theorem A gives the **equality** `(L_p(f)) = (Char_p^∅(f))` of principal ideals of
`Λ`.  No divisibility substitution is needed.  **[T]**

**Normalisations.**  BLV's definite ordinary `p`-adic `L`-function is built (§`goodord`) from the
`α`-stabilised Gross-point theta elements
`𝓛_{g,n} = α_p(g)^{-n} Σ_{σ∈G_n} ( ψ_g(σ P_{n-1}) − α_p(g)·ψ_g(σ P_n) ) σ`,
`𝓛_g = lim_n 𝓛_{g,n} ∈ Λ`, and then
`L_p(g) = 𝓛_g · 𝓛_g^ι`.
This is exactly the square-root normalisation recorded in A0; the branch's
`θ_n^α = θ_{n+1} − α^{-1}ν(θ_n)` differs from BLV's stabilised element by the unit factor
`α^{-(n+1)}` and an index shift, i.e. by a unit of `Λ` and a relabelling of the tower, and not in a
way that moves the `I`-adic order or the normalised leading coefficient.  **No incompatibility with
A0 was found, so A0 is not reopened.**  Since `gr_I Λ ≅ Z_p[T]` is a domain, orders add and leading
coefficients multiply; `ι` preserves `I` and acts on `I^k/I^{k+1}` by `(-1)^k`.  Hence

> **[C]** `[c_2] ≠ 0 ⟹ 𝓛_p ∈ I^2 \ I^3 ⟹ L_p ∈ I^4 \ I^5` with unit leading coefficient
> `⟹ (Theorem A) ord_I Char_p^∅(f) = 4` with unit normalised `I^4/I^5` coefficient.

The parity check of `GATE.md` K5 is satisfied: `ord_I L_p = 2·ord_I 𝓛_p` is even at every step.

**TASK 1 verdict: the BLV side delivers `σ_alg = 4` with unit leading coefficient, conditional on
`[c_2] ≠ 0` — provided the module of §`def:definite_char` is the module BD-DH's theorem is about.
That is Task 2.**

---

## TASK 2 — module identification

BD-DH §2.5 uses `X_∞ = Hom(Sel_{p^∞}(E/K_∞), Q_p/Z_p)` where `Sel_m(E/L)` is the **classical**
Selmer group of §1.2.1: `{s ∈ H^1(L, E_m) : res_w(s) ∈ E(L_w)/mE(L_w) for all w}` — the Kummer
condition at *every* place, no strict/relaxed modification, no imprimitivity.

Comparison, item by item, as required by `GATE.md` K3.

**(a) Global condition.**  Both are subgroups of `H^1(K_∞, A_f)` cut out by local conditions only;
BLV's `H^1(K, **A**_f)` is identified with `H^1(K_∞, A_f)` by Shapiro (BLV §`subsec-p`, used
throughout), and BLV's `Sel_ε(K, **A**_{f})` with `𝔓 = 0` is the analogue over the whole tower, with
the `[𝔓]`-control statement Proposition `global control` at finite level.  No difference.  **[T]/[A]**

**(b) Primes above `p`.**  Both impose `E(K_{∞,𝔭}) ⊗ Q_p/Z_p` (BLV §`subsec-p` for `ε = ∅`;
BD-DH §1.2.1 in the limit).  Identical; in particular BLV do **not** use the strict Greenberg
condition here — they prove it agrees with the Kummer condition (BLV (`eq:ord1`), quoting
Greenberg).  No difference.  **[T]**

**(c) Primes `w | N^+`.**  BLV impose the *strict* condition `res_w = 0`, BD-DH the Kummer
condition.  These agree because **both are the zero subgroup of the zero group**: BLV Lemma
`control nplus` proves `H^j(K_w, A_{h,𝒪}(𝔓)) = 0` for all `j` and all `w | N^+`, for every ideal
`𝔓` generated by a regular sequence (including `𝔓 = 0`), using Hypothesis `controlass`(5)
(`H^0(G_{Q_q}, E_p) = 0` and `ρ̄` ramified at `q`) and local Tate duality.  `INPUTS.md` §6 records
that `controlass`(5) holds for this curve at **every** `p ≥ 5` (both places `2` and `4547` are
additive with integral `j`, so `E_0/E_1` is a `q`-group and `c_q ≤ 4`).  So the two local conditions
literally coincide.  **[T]**

**(d) Primes `ℓ | N^-`.**  BLV impose `H^1_ord`, BD-DH the Kummer condition.  These coincide:
`ℓ` is inert in `K` and splits completely in `K_∞/K` (BLV §`subsec-N^-`), so at each place above `ℓ`
the completion is `K_ℓ`, and `E/K_ℓ` is a Tate curve, `E(K_ℓ) = K_ℓ^*/q_ℓ^Z`.  The Tate
uniformisation identifies the connecting map of `0 → μ_{p^n} → E[p^n] → Z/p^n → 0` with the Kummer
map of `G_m`, so
`Im(H^1(K_ℓ, μ_{p^∞}) → H^1(K_ℓ, A)) = Im((K_ℓ^* ⊗ Q_p/Z_p) → H^1(K_ℓ, A))`,
and since `K_ℓ^* ↠ E(K_ℓ)` and `- ⊗ Q_p/Z_p` is right exact, that image equals
`Im(E(K_ℓ) ⊗ Q_p/Z_p → H^1(K_ℓ, A))`.  The left-hand side is precisely BLV's `H^1_ord` (their
`A^{(ℓ)}` is the Kummer dual of `T^{[ℓ]}`, i.e. the `μ`-part), the right-hand side is BD-DH's
condition.  **[A]** (argument given; no appeal to "standard equivalence").

**(e) Primes of good reduction outside `p`.**  BLV impose the unramified condition, BD-DH the
Kummer condition; for `E` with good reduction at `w ∤ p` these coincide (the classical local
computation: the Kummer image is `H^1_ur(K_w, A)`; see Rubin, *Euler Systems*, Lemma I.3.5 /
Prop. I.6.1).  The tower is unramified at such `w` (it is ramified only above `p`, since
`p ∤ h_K`), so the identification passes to the limit.  **[T]/[A]**

**(f) Pontryagin dual conventions.**  Both `Hom(-, Q_p/Z_p)`.  No difference.  **[T]**

**(g) Twist / involution.**  BLV work with `**A**_f = Hom_cont(**T**_f^ι, μ_{p^∞})`,
`**T**_f = T_f ⊗ Λ(ε_∞^{-1})`; after Shapiro the underlying group is `Sel_{p^∞}(E/K_∞)` but the
`Λ`-action may differ from BD-DH's by `ι`.  This is harmless for everything the bridge uses:
`char(M^ι) = char(M)^ι`, `ι(I) = I`, `ι` acts on `I^k/I^{k+1}` as `(-1)^k`, hence `ord_I` is
preserved and the normalised leading coefficient changes by the unit `(-1)^σ`.  **[A]**

**(h) Finite / pseudo-null corrections, imprimitive Euler factors.**  None: by (b)–(e) the two
Selmer groups are *equal* as subgroups of `H^1(K_∞, A_f)`, not merely isogenous, and BLV's
`S = L = 1` specialisation carries no imprimitivity.  Hence the duals are isomorphic and the
characteristic ideals are equal on the nose.  **[A]**

**(i) Hypotheses of BD-DH §1.1 for our data** (needed for the derived heights to exist at all; the
audit must check them, they are not implied by BLV's list):

1. `p ∤ 2·#(E/E^0)` over `Spec O_K`: at the inert multiplicative places `3, 2243, 5843` the
   component group has order dividing `v_ℓ(Δ) = 2, 1, 2`; at the additive places `2, 4547` the
   component group has order `≤ 4`.  So every `p ≥ 5` is fine.  **[A]**
2. good reduction above `p`: part of Hypothesis 1.1(1).  **[T]**
3. `ρ_p(G_K)` contains a Cartan subgroup of `GL_2(F_p)`: Hypothesis 1.1(3) gives
   `ρ̄(G_Q) = GL_2(F_p)`, and `ρ̄(G_K) = GL_2(F_p)` unless `K ⊆ Q(E_p)`; the only quadratic subfield
   of `Q(E_p)` is `Q(sqrt(p*))`, and `Q(sqrt -7) = Q(sqrt(p*))` only for `p = 7`, which is excluded
   by Hypothesis 1.1(2) (`p ∤ disc K`).  **[A]**
4. surjectivity of the local norm maps: BD-DH Proposition 1.1 gives this once, for every `v`
   ramified in `K_∞/K` (i.e. `v | p`, as `p ∤ h_K`), `E` is ordinary at `v` and `p ∤ #E(F_v)`.  For
   `p` inert, `#E(F_{p^2}) ≡ (1-a_p)(1+a_p) (mod p)`; for `p` split, `#E(F_p) ≡ 1-a_p (mod p)`.  So
   this is **exactly** BLV Hypothesis 1.1(5), the non-anomalous condition already in force.  **[A]**

### Return

`MODULE_IDENTIFICATION_PROVED` — with the explicit content: for every `p` satisfying BLV
Hypothesis 1.1 (hence `p ≥ 5`, `p ≠ 7`, non-anomalous, `ρ̄` surjective) and good ordinary for this
curve,
`Sel_∅(K, **A**_f) = Sel_{p^∞}(E/K_∞)` as subgroups of `H^1(K_∞, A_f)`, hence
`𝔛_p^∅(f) ≅ X_∞^{(ι)}` and `Char_p^∅(f) = char(X_∞)^{(ι)}`, and in particular
`ord_I Char_p^∅(f) = ord_I char(X_∞) = σ` with the same normalised leading coefficient up to a unit.

No mismatch was found.  I flag, honestly, that (d), (e), (g), (h) and (i.1)/(i.3)/(i.4) are my own
comparisons rather than quoted theorems; each is written out above rather than asserted.

---

## TASK 3 — the derived-height order inequality, at source

**BD-DH Theorem 2.7** (finite layer `L/K`, `Sel = Sel_{p^n}(E/K)`, filtration
`Sel^{(k)} = Sel ∩ (γ-1)^{k-1} Sel_{p^n}(E/L)`): for `1 ≤ k ≤ p-1` there are canonical pairings
`⟨ , ⟩_k : Sel^{(k)} × Sel^{(k)} → I^k/I^{k+1}` with (1) `⟨s_1,s_2⟩_k = (-1)^{k+1}⟨s_2,s_1⟩_k`,
(2) **`Sel^{(k+1)}` is the null-space of `⟨ , ⟩_k`**, (3) the norm space is in the null-space of all
of them.  Integral values.  **[T]**

**BD-DH Theorem 2.18**: for `1 ≤ k ≤ p-1` there are canonical pairings
`⟪ , ⟫_k : S̄_p^{(k)} × S̄_p^{(k)} → I^k/I^{k+1} ⊗ Q` with (1) symmetry/alternation by parity of `k`,
(2) **`S̄_p^{(k+1)}` is the null-space of `⟪ , ⟫_k`**, (3) universal norms lie in every null-space,
(4) `⟪ , ⟫_1` restricted to `E(K)_p` is the Mazur–Tate/Schneider `p`-adic height, and
(5) `p^{A_k} ⟪ , ⟫_k` takes values in `I^k/I^{k+1}`, where `p^{A_k}` is the exponent of the finite
group `S̄_p^{(k)}/S_p^{(k)}`.  Here `S̄_p^{(k)}` is the `p`-adic **saturation** of `S_p^{(k)}` in
`S_p(E/K)` (Definition 2.16).  **[T]**

**BD-DH Theorem 2.23**: with `ρ_p = Σ_{k=1}^{p} rank_{Z_p} S̄_p^{(k)}` (equivalently
`ρ_p = d_1 + 2d_2 + ⋯ + p·d_p`, `d_k = rank S̄^{(k)}/S̄^{(k+1)}`), the order of vanishing `σ` of
`char(X_∞)` satisfies `σ ≥ ρ_p`, and
`L̄_∞ = #( Ш(E/K)_{p^∞} / Div Ш(E/K)_{p^∞} ) · R_der` in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`.
The inequality `σ ≥ ρ_p` is established in the proof *unconditionally* (the displayed estimate
`det(⟨x'_i, y'_j⟩) ∈ I_n^{Σ_k k d_k}` at each layer, via Lemma 2.25 and Lemma 2.26), i.e. it does
**not** presuppose non-degeneracy of any derived height.  **[T]**

**BD-DH Lemma 3.1**: `⟪τ s_1, τ s_2⟫_k = (-1)^k ⟪s_1, s_2⟫_k` for all `s_1, s_2 ∈ S̄_p^{(k)}`.  The
proof uses only Galois equivariance of the local Tate pairing and the fact that the involution `*`
acts on `I^k/I^{k+1} ⊗ Q` by `(-1)^k`; it does **not** use the standing assumption of Chapter 3 that
`Ш(E/K)_{p^∞}` be finite, and it is stated for `S̄_p^{(k)}`, i.e. for the pro-`p` Selmer group and
not only for `E(K)_p`.  BD-DH then record explicitly: *"the `p`-adic height pairing `⟪ , ⟫_1` is
trivial when restricted to `S_p(E/K)^+ × S_p(E/K)^+` and `S_p(E/K)^- × S_p(E/K)^-`.  Hence the
null-space of `⟪ , ⟫_1` has rank at least `|r^+ − r^-|`"* — with their `r^±` being precisely our
`s^±`.  **[T]**

### The chain

1. first anticyclotomic height pairs only opposite `τ`-eigenspaces: **[T]** (Lemma 3.1 with `k = 1`,
   plus `p` odd so `e^± = (1±τ)/2` are integral idempotents and `S ⊗ Q = S^+⊗Q ⊕ S^-⊗Q`);
2. `rank S̄^{(2)} ≥ |s^+ − s^-|`: **[T]** (BD-DH, sentence after Lemma 3.1, using Theorem 2.18(2));
3. the characteristic-order formula counts the filtration ranks in the required way: **[T]**
   (Theorem 2.23, `σ ≥ ρ_p = Σ_k rank S̄^{(k)}`);
4. no omitted higher filtration term can invalidate it: **[T]** — all terms of `ρ_p` are
   non-negative, so dropping `k ≥ 3` only weakens the bound;
5. truncation at level `p`: the pairings exist for `1 ≤ k ≤ p-1` and the filtration is indexed
   `1 ≤ k ≤ p`; we use only `k = 1, 2` (and `rank S̄^{(3)}` as a non-negative term), so `p ≥ 5` is
   ample and `σ = 4 < p` is never in conflict.  **[T]**

Hence

> `σ ≥ ρ_p ≥ rank_{Z_p} S + rank_{Z_p} S̄^{(2)} ≥ (s^+ + s^-) + |s^+ − s^-| = 2·max(s^+, s^-)`.

**TASK 3 verdict: the inequality is exactly what the source proves** (with the one pedantic
correction that the middle term must be read with the *saturations* `S̄^{(k)}`, which is how BD-DH
define `ρ_p`; the ranks are unaffected).  `BD_ORDER_INEQUALITY = HOLDS`.

---

## TASK 4 — the `τ`-eigenspaces and the certified twist

Let `p` be odd, `D = -7`, `χ_D` the quadratic character of `K/Q`.

**(1) Selmer decomposition.**  `Res: H^1(Q, E[p^n]) → H^1(K, E[p^n])^{Gal(K/Q)}` is an isomorphism
(inflation–restriction; kernel and cokernel are killed by `2` and by `p^n`, and `p` is odd).  As
`G_Q`-modules `E^D[p^n] ≅ E[p^n] ⊗ χ_D`, and `Res_K` kills `χ_D`, so restriction also embeds
`H^1(Q, E^D[p^n])`.  Since `τ` acts on `H^1(K, E[p^n])` and `p` is odd, `e^± = (1±τ)/2` split it,
and the two images above are the `+` and `−` eigenspaces:
`H^1(K, E[p^n])^+ = Res H^1(Q, E[p^n])`, `H^1(K, E[p^n])^- = Res H^1(Q, E^D[p^n])`.  **[A]**

**(2) Local conditions.**  For a place `w` of `K` over a place `v` of `Q`, the local Kummer
condition `E(K_w) ⊗ Z/p^n` is `τ`-stable, and `(E(K_w) ⊗ Z/p^n)^±` corresponds to
`E(Q_v) ⊗ Z/p^n`, resp. `E^D(Q_v) ⊗ Z/p^n`, by the same argument applied locally (again `p` odd
kills the `Gal(K_w/Q_v)`-cohomology).  Therefore
`Sel_{p^n}(E/K)^+ ≅ Sel_{p^n}(E/Q)` and `Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^{D}/Q)`.  **[A]**
(This is the standard `p`-odd twist decomposition; the point demanded by Task 4 is that it is a
statement about the *Selmer* groups, and the argument above is at that level, not at the level of
`E(K)`.)

**(3) Passage to the inverse limit and to `T_p Ш`.**  The isomorphisms of (2) are compatible with
the multiplication-by-`p` transition maps used in BD-DH Definition 2.15, so
`S_p(E/K)^+ ≅ S_p(E/Q)`, `S_p(E/K)^- ≅ S_p(E^{D}/Q)`, and the exact sequences
`0 → E(F) ⊗ Z_p → S_p(E/F) → T_p Ш(E/F) → 0` are compatible with the splitting; in particular
`T_p Ш(E/K)^- ≅ T_p Ш(E^{D}/Q)` and `Div Ш(E/K)_{p^∞}^- ≅ Div Ш(E^{D}/Q)_{p^∞}`.  **[A]**

**(4) Conclusion from the certificate.**  The certificate gives `rank E^{-7}(Q) = 0` and
`Ш(E^{-7}/Q)` finite.  Hence `S_p(E^{-7}/Q)` has `Z_p`-rank `0 + corank Div Ш(E^{-7}/Q)_{p^∞} = 0`,
so

> `s^- = 0`, and a fortiori `r^- = 0` and `d^- = 0`.  **[T from the certificate + A]**

`TWIST_MINUS_EIGENSPACE = HOLDS`.  (Note this is genuinely stronger than the `E(K)`-decomposition:
it is finiteness of `Ш(E^{-7}/Q)`, not just the rank, that kills `d^-`.)

---

## TASK 5 — replay of the live configurations

With `s^+ = 2 + d^+`, `s^- = r^- + d^-`, `σ = 4` and `σ ≥ 2·max(s^+, s^-)`:

* `2(2 + d^+) ≤ 4` forces `d^+ = 0` — free from the inequality, because the known `rank E(Q) = 2`
  already fills `s^+`;
* `r^- + d^- ≤ 2` leaves exactly the six rows `(d^+, r^-, d^-) ∈ {(0,0,0), (0,0,1), (0,0,2),
  (0,1,0), (0,1,1), (0,2,0)}`, of which three have `d^- ≠ 0`.

So `τ`-equivariance **alone** does not give `Div Ш = 0`; the minus-side input is load-bearing.  The
certificate (Task 4) forces `r^- = d^- = 0` and leaves only the first row.  I reproduce the
enumeration independently, and it is machine-checked in
`RequestProject/LiveConfigurations.lean`
(`OrdinaryBridge.live_configurations`, `OrdinaryBridge.live_configurations_sharp`,
`OrdinaryBridge.divisible_part_vanishes`; the file builds with no `sorry`).  These are the
*arithmetic* bookkeeping statements only — they formalise the counting step of Tasks 5 and 6, not
the arithmetic-geometric inputs.

No step of this audit reaches finiteness from `σ = 4` alone; `GATE.md` K6 is respected.

---

## TASK 6 — A2a: does certificate + order 4 kill the divisible part?

Assume `[c_2] ≠ 0` **[C]**, module identification (Task 2), hence `σ = 4` with unit leading
coefficient, the Task-3 inequality, and `s^- = 0` (Task 4).

1. `s^- = 0` and Lemma 3.1 (`k = 1`) give `⟪ , ⟫_1 ≡ 0` on `S̄^{(1)}`: the pairing kills
   `S^+ × S^+`, its target is a `Q_p`-vector space, and `S^-` has rank `0`, so every value vanishes.
2. Theorem 2.18(2): `S̄^{(2)} = ` null-space of `⟪ , ⟫_1 = S̄^{(1)} = S`.
3. Theorem 2.23: `4 = σ ≥ ρ_p ≥ rank S̄^{(1)} + rank S̄^{(2)} = 2·rank_{Z_p} S`, so `rank S ≤ 2`.
4. `rank S ≥ rank_{Z_p}(E(K) ⊗ Z_p) = rank E(K) = 2` (rank `E(Q) = 2` from the project record and
   `rank E^{-7}(Q) = 0` from the certificate).  Hence `rank S = 2` and `rank T_p Ш(E/K) = 0`.
5. `rank_{Z_p} T_p Ш(E/K) = corank Div Ш(E/K)_{p^∞} = d^+ + d^-`, so `d^+ = d^- = 0`, i.e.

> **`Div Ш(E/K)[p^∞] = 0`, hence `Ш(E/K)[p^∞]` is finite.**  **[C]**

Theorems doing the work: **BD-DH Theorem 2.23** (the inequality `σ ≥ ρ_p`), **BD-DH Theorem 2.18(2)**
(identification of the null-spaces with the filtration), **BD-DH Lemma 3.1** (`τ`-equivariance),
**BLV Theorem A** in the ordinary/non-exceptional case (to convert `[c_2] ≠ 0` into `σ = 4`), the
Task-2 identification, and the `D = -7` certificate through Task 4.

Forbidden assumptions check: finiteness of `Ш(E/K)[p^∞]` is *derived* in step 5, never used; no
`T_p Ш = 0` input; **no non-degeneracy of any height is assumed** — on the contrary, the first
derived height is here identically zero, and the non-degeneracy of `⟪ , ⟫_2` is *forced* below
rather than assumed; no BSD, no FIN, no rank-two Heegner index.

`A2a_DIVISIBLE_SHA = HOLDS (conditionally on [c_2] ≠ 0)`.

---

## TASK 7 — A2b: from the unit leading coefficient to `Ш[p^∞] = 0`

**Exact source statements.**

*Definition 2.19/2.20*: with a basis of `S_p(E/K)` compatible with the filtration,
`R^{(k)} = det(⟪s_i, s_j⟫_k)` over the `d_k` basis vectors spanning `S̄^{(k)}/S̄^{(k+1)}`, well
defined up to `Z_p^×`; if `⟪ , ⟫_{p-1}` is non-degenerate then
`R_der = R^{(1)}⋯R^{(p-1)} ∈ (I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`, otherwise `R_der = 0`.

*Theorem 2.23*: `σ ≥ ρ_p` and
`L̄_∞ = #( Ш(E/K)_{p^∞} / Div Ш(E/K)_{p^∞} ) · R_der`  **in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`**.

*Corollary 2.24*: (1) if `⟪ , ⟫_{p-1}` is non-degenerate then `σ = ρ_p`; (2) if `p^B` is the order
of `Ш/Div Ш` then `p^B·R_der ∈ (I^{ρ_p}/I^{ρ_p+1})/Z_p^×`.

*Remark 2.21*: if `Ш(E/K)_{p^∞}` is finite, then with `M` carrying an integral Mordell–Weil basis to
a filtration-compatible basis, `R_der := det(M)^{-2} R^{(1)}⋯R^{(p-1)}`; *"This is well-defined in
`I^{ρ_p}/I^{ρ_p+1}` (not just up to a `p`-adic unit) and does not depend on the choice of `M`."*
**No proof is given for this sentence, in either the preprint or the published version.**

**Our configuration.**  From Task 6: `rank S = 2`, `S̄^{(2)} = S̄^{(1)}`, so `d_1 = 0` and
`ρ_p = 2 + 2 + rank S̄^{(3)} + ⋯ ≤ σ = 4` forces `rank S̄^{(3)} = 0`, i.e. `d_2 = 2`, `ρ_p = σ = 4`,
and **`⟪ , ⟫_2` is non-degenerate — derived, not assumed**, with all later pairings trivially
non-degenerate on the zero module, so `R_der ≠ 0` and Theorem 2.23 applies with equality of ideals.
Since `Div Ш = 0` (Task 6), `Ш(E/K)[p^∞]` is finite and Remark 2.21 applies; with the Mordell–Weil
basis `P_1, P_2` the filtration is trivial, so `M` may be taken to be the identity and
`R_der = det( ⟪P_i, P_j⟫_2 ) = ⟪P_1, P_2⟫_2^2` (an alternating `2×2` determinant).

The target identity is then, in `I^4/I^5 ⊗ Q` modulo `Z_p^×`,

> `unit = #Ш(E/K)[p^∞] · ⟪P_1, P_2⟫_2^2`,  i.e.  `v_p(#Ш(E/K)[p^∞]) = −2·v_p(⟪P_1,P_2⟫_2)`.

Answering the six checks of Task 7:

1. **What contains `R_der`?**  Theorem 2.23 and Definition 2.20 place it in
   `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`, i.e. *a priori with denominators*; Theorem 2.18(5) bounds those
   denominators by `p^{A_k}`, the exponent of `S̄^{(k)}/S^{(k)}` — the saturation defect, which is
   not controlled by the finiteness of `Ш`.
2. **When is `R_der` integral?**  The source proves integrality only of the **product**: Corollary
   2.24(2) says `p^B R_der` is integral, where `p^B = #(Ш/Div Ш)`.  This is exactly the quantity
   one wants to bound, so Corollary 2.24(2) cannot be used to bound it.  Remark 2.21 asserts
   integrality of `R_der` alone, but gives no proof, and it is not proved elsewhere in §2.  **[?]**
3. **Does vanishing of the divisible part make `Ш[p^∞]` finite?**  Yes: `Ш[p^∞]` is cofinitely
   generated, so `Ш[p^∞] ≅ (Q_p/Z_p)^d ⊕ (finite)` with `d = corank Div Ш = 0`.  **[A]**
4. **Do both factors have non-negative valuation?**  `v_p(#Ш) ≥ 0` trivially; `v_p(R_der) ≥ 0` is
   precisely the unproved point.  All the source gives is
   `v_p(R_der) ≥ −2·A_2`, with `p^{A_2}` the exponent of `S̄^{(2)}/S^{(2)}` (Theorem 2.18(5)).
5. **Does a unit leading coefficient force `v_p(#Ш) = 0`?**  **Not from the cited results.**  The
   identity `unit = #Ш · R_der` is compatible with `#Ш = p^B` and `v_p(R_der) = −B` for any
   `0 ≤ B ≤ 2A_2`; Corollary 2.24(2) is satisfied identically in that scenario.  Concluding `B = 0`
   from the unit product is the step that is missing, and doing it by invoking Remark 2.21 means
   importing an unproved assertion.  **[X]** if asserted.
6. **Hence `Ш(E/K)[p^∞] = 0`?**  Not established.

**Strongest correct replacement.**  What the sources *do* give, conditional on `[c_2] ≠ 0`, is

> `Ш(E/K)[p^∞]` is **finite**, and `#Ш(E/K)[p^∞]` divides `p^{2A_2}`, where `p^{A_2}` is the
> exponent of `S̄_p^{(2)}/S_p^{(2)}`; in particular `Ш(E/K)[p^∞] = 0` **iff** `R_der` is a `p`-adic
> unit, e.g. as soon as `S_p^{(2)} = S̄_p^{(2)}`.

I can add one step here that the packet does not contain, and that narrows the gap (my own argument,
label **[A]**, offered as a replacement statement and not as a closure of the bridge).  At finite
level, the pairing `⟨ , ⟩_{1,n}` on `Sel_{p^n}(E/K)` satisfies the same `τ`-rule as Lemma 3.1
(the proof of Lemma 3.1 is a statement about the `Λ_n`-valued pairing of §2.3, and `*` acts by `-1`
on `I_n/I_n^2 ≅ G_n ⊗ Z/p^n`), so it vanishes on `Sel^+ × Sel^+` and `Sel^- × Sel^-`.  Writing
`e` for the exponent of `Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^{-7}/Q)`, one gets for all
`z = x + y, z' = x' + y'` (with `x, x' ∈ Sel^+`, `y, y' ∈ Sel^-`)
`⟨e z, z'⟩_{1,n} = ⟨x, e y'⟩ + ⟨e y, x'⟩ = 0`,
so `e · Sel_{p^n}(E/K) ⊆ Sel_{p^n}^{(2)}` by Theorem 2.7(2).  Since
`0 → E^{-7}(Q) ⊗ Z/p^n → Sel_{p^n}(E^{-7}/Q) → Ш(E^{-7}/Q)[p^n] → 0` and `E^{-7}(Q)` is finite with
`Ш(E^{-7}/Q)` finite (certificate), `e` divides the `n`-independent integer
`e_0 = exp(E^{-7}(Q)[p^∞]) · exp(Ш(E^{-7}/Q)[p^∞])`.  Passing to the limit, `e_0 · S ⊆ S^{(2)}`, so
`A_2 ≤ v_p(e_0)` and therefore

> **[A]+[C]** `#Ш(E/K)[p^∞]` divides `p^{2 v_p(e_0)}`; in particular, if
> `p ∤ #Ш(E^{-7}/Q) · #E^{-7}(Q)_tors` then `A_2 = 0`, `R_der` is a unit, and
> `Ш(E/K)[p^∞] = 0`.

So the bridge closes for **all but finitely many** good-ordinary `p` — but the excluded finite set
is `{p : p | #Ш(E^{-7}/Q)·#E^{-7}(Q)_tors}`, which the `D = -7` certificate (an `L`-value
non-vanishing statement) does **not** identify.  The audit's question was posed for *every*
good-ordinary `p` satisfying the hypotheses, and for that the step fails.

---

## PRINCIPAL VERDICT

### `LEADING_TERM_STEP_FAILS`

Tasks 1–6 go through: conditional on `[c_2] ≠ 0`, BLV Theorem A (ordinary ⇒ non-exceptional ⇒
equality of ideals) plus the module identification of Task 2 give `σ = 4` with unit normalised
`I^4/I^5` coefficient; BD-DH Theorem 2.23 + Theorem 2.18(2) + Lemma 3.1 give
`σ ≥ ρ_p ≥ 2·max(s^+, s^-)`; the `D = -7` certificate, through the odd-`p` twist decomposition of
the *Selmer* groups, gives `s^- = 0`; and these together force `Div Ш(E/K)[p^∞] = 0`, hence
`Ш(E/K)[p^∞]` finite.  The chain then stops.

**First missing implication** (state it, not its downstream consequences):

> **Missing theorem.**  Let `p ≥ 5` be good ordinary for `E`, satisfying BLV Hypothesis 1.1 and
> BD-DH §1.1, with `Ш(E/K)[p^∞]` finite and with derived filtration
> `S_p(E/K) = S̄^{(1)} = S̄^{(2)} ⊋ S̄^{(3)} = 0`.  Then the second derived height `⟪ , ⟫_2` takes
> values in `I^2/I^3` (not merely in `I^2/I^3 ⊗ Q`) on `E(K) ⊗ Z_p`; equivalently
> `S_p^{(2)} = S̄_p^{(2)}`, i.e. `A_2 = 0`; equivalently `v_p(R_der) ≥ 0`.

Bertolini–Darmon prove only `v_p(#(Ш/Div Ш)) + v_p(R_der) = 0` (Theorem 2.23) and
`v_p(#(Ш/Div Ш)) + v_p(R_der) ≥ 0` (Corollary 2.24(2)); Theorem 2.18(5) explicitly allows
`⟪ , ⟫_k` to have denominators `p^{A_k}` coming from the saturation defect `S̄^{(k)}/S^{(k)}`, and the
finiteness of `Ш(E/K)[p^∞]` does not control that defect.  Remark 2.21's sentence *"This is
well-defined in `I^{ρ_p}/I^{ρ_p+1}`"* is, in context, an assertion that the `Z_p^×`-ambiguity is
removed; read as an integrality claim it is unproved in the paper.  Any argument that cancels
`R_der` against the unit leading coefficient without proving `v_p(R_der) ≥ 0` is `GATE.md`-forbidden
regulator cancellation.

The gap is narrow and explicitly localisable: by the argument in Task 7 it suffices to know
`p ∤ #Ш(E^{-7}/Q) · #E^{-7}(Q)_tors` — an input about the **order** of the twist's
Shafarevich–Tate group, which is strictly more than the certified non-vanishing of `L(E^{-7}, 1)`.

Nothing above is promoted to a certified project result.  Everything downstream of `[c_2] ≠ 0` is
conditional; `FIN` and `FORMULA` remain open; nothing is claimed for supersingular `p` or for the
anomalous primes.

---

## Ledger

    MODULE_IDENTIFICATION   = PROVED           (BLV Sel_∅(K,A_f) = classical Sel_{p^∞}(E/K_∞);
                                                N^+ by BLV Lemma `control nplus`, N^- by the Tate-curve
                                                identification, good primes by the standard
                                                unramified = Kummer comparison, ι-twist harmless)
    BD_ORDER_INEQUALITY     = HOLDS            (BD-DH Thm 2.23 σ ≥ ρ_p, Thm 2.18(2), Lemma 3.1;
                                                σ ≥ rank S + rank S̄^(2) ≥ 2·max(s⁺,s⁻); p ≥ 5 ample)
    TWIST_MINUS_EIGENSPACE  = HOLDS            (odd-p Selmer twist decomposition, proved here, plus
                                                the certificate: s⁻ = 0, hence r⁻ = d⁻ = 0)
    A2a_DIVISIBLE_SHA       = HOLDS [C]        (Div Ш(E/K)[p^∞] = 0, conditional on [c_2] ≠ 0;
                                                needs the certificate — σ = 4 alone leaves d⁻ ∈ {0,1,2})
    A2b_LEADING_TERM        = FAILS            (Thm 2.23/Cor 2.24 give only integrality of the product;
                                                Rmk 2.21's integrality of R_der is unproved.
                                                Replacement: #Ш(E/K)[p^∞] | p^{2A_2}, = 0 iff R_der is a unit)
    ORDINARY_BRIDGE         = LEADING_TERM_STEP_FAILS
