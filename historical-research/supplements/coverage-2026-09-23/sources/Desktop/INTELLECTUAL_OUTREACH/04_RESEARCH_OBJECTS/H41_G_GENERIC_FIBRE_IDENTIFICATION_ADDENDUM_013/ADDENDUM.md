# Thirteenth addendum — G: the generic-fibre identification `(C) ⟺ T_p = q̂(S₀^B)`, repaired after audit

**Tier: PROOF — OPERATOR-AUDITED, REPAIRED AS SPECIFIED; NOT VERIFIED.** The operator audited the draft preserved
byte-for-byte in `01_audited_draft/` and returned *AUDIT VERDICT: REVISE BEFORE SEAL — MATHEMATICAL CORE OF G:
PASS WITH REPAIRS*, with recommended status *G = MATHEMATICALLY SOUND AFTER LOCAL REPAIRS*, "not yet VERIFIED".
Every repair in the operator's table is applied below (ledger, §11). **This repaired text has not itself been
re-audited.** No research object launched, no Codex or Aristotle run; the only computations are exact integer
lattice checks and mechanical text extraction. Prior objects unmodified and byte-identical: `ac82f3ad…`,
`d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`,
`b7ebbf00…`, `8af7a2a5…`, `afae7941…`, `a2667972…`, `7f7c8a9d…`.

## 0. Scope

G is the first stage of the operator's architecture **G → M → R**. It establishes `(C) ⟺ (C_gen)` on the generic
fibre over `ℂ`. It does not touch `(D3)`, M, R, characteristic 2, any integral model, or uniform optimality
`E₀ = E`. It obeys `ADDENDUM_012`: it uses none of `ω̄_f`, `Ω`, `ω` or an unspecified special fibre (holomorphic
1-forms are written `Hol(X)`, a form `ψ`); it never defines anything through `S₀ ∈ E₀(ℚ)[2]`; and it treats
`(C) ⟺ (C′)` as unproved, proving instead `(C) ⟺ (C_gen)`. As the operator directed, the corrected statement and
its point carry new names, `(C_gen)` and `S₀^B`.

Recorded from the operator, unchanged: as sealed there is no well-formed implication `(D3) ⟹ (C)`; the eventual
R-stage theorem may need `(D3)` plus specialization/component data; and the conservative dependency envelope for
`(D3)` is `(B) + (D1) + (D2) + (D) +` special-fibre description, `(D)` being the ARS application.

## 1. The two maps — crosswalk (the seal-blocking repair)

The audit found that the draft used one symbol `π` for two maps. The mechanical inventory
(`computation/inventory_pi_uses.sh`, `receipts/PI_USAGE_INVENTORY.txt`) shows the **sealed record does the same —
including inside a single report.** Stage II *defines* `π` on the curve:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 52-52
```text
**THEOREM — verified deduction.** Let E0 be the actual connected optimal quotient of J0(N), π its quotient map composed with the infinity-based Abel–Jacobi map, τ complex conjugation, and
```

but *applies* it to a subgroup of the Jacobian in its §4:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 161-165
```text
**THEOREM — source data survive.** Let C0=⟨[0]−[∞]⟩ and K=ker π. Frozen Stage I's checked Chua–Ling specialization at N=2p gives \(\#C_0=(p^2-1)/8\), with \(\#C_0[2^\infty]=2^m\). Its checked Yoo eta-divisor specialization at N=6p gives \(\#C_0=p^2-1\), with 2-part 8. These exact source calculations are compatible with all withheld results. They yield

\[
t=\#\pi(C_0)=\#C_0/\#(C_0\cap K),
\]
```

Stage I defines `π` on the Jacobian, normalized from the cusp `∞`, and pushes curve cycles forward along it:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/01_stage_I/STAGE_I_RECONSTRUCTION.md` lines 113-113
```text
**THEOREM — exact identity.** Let \(\pi:J_0(N)\to E_0\) be the actual optimal quotient, normalized from the infinity cusp, and let \(\nu_0\) be its Manin constant. Set
```

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/01_stage_I/STAGE_I_RECONSTRUCTION.md` lines 157-160
```text
\[
\eta_\ell=\sum_{j=1}^{(\ell-1)/2}\{0,j/\ell\}\in H_1(X_0(N),\mathbb Z),\qquad
u_\ell=[\pi_*\eta_\ell]\in U_0.
\]
```

`ADDENDUM_004` and `ADDENDUM_005` use `π` for the Jacobian quotient and `π̂` for its dual, the polarization left
unspecified:

**Verbatim** — `H41_ETA_EXTERNAL_CHECK_ADDENDUM_004/ADDENDUM.md` lines 53-56
```text
The correct comparison is obtained by dualizing. With `π : J₀(N) → E₀` the connected optimal quotient,
connectedness of the kernel gives a surjection on integral homology, so

    π* : H¹(E₀,ℤ) ↪ H¹(X₀(N),ℤ)   is saturated,
```

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/ADDENDUM.md` lines 62-64
```text
equivalently, in the Jacobian, with `J = J₀(2p)`, `T_p = ((p²−1)/16)·([0]−[∞]) ∈ J(ℚ)[2]` the class cut
out by `√F_p`, `π : J → E₀` the connected optimal quotient, `π̂ : E₀ ↪ J` its dual embedding, and
`S₀ ∈ E₀(ℚ)[2]∖{0}` the class of the primitive character `α_p mod 2`:
```

and `α_p` is defined by pullback along the curve-level pushforward:

**Verbatim** — `H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002/01_attempt/PROOF_ATTEMPT.md` lines 94-96
```text
Let alpha_p be the pullback, to integral homology of X_0(N), of the primitive
integer functional on the actual U_0 lattice. Then
alpha_p({0,1/3})=w_3.
```

**This addendum renames nothing that is sealed.** For G only, it introduces

    q     : J → E₀            the optimal quotient — surjective, with connected kernel
    AJ_∞  : X → J             the Abel–Jacobi map based at the cusp ∞
    φ     := q ∘ AJ_∞ : X → E₀
    q̂     := λ_J⁻¹ ∘ q^∨ ∘ λ_{E₀} : E₀ → J        with λ_J, λ_{E₀} the principal polarizations

**Crosswalk.** `(AJ_∞)_* : H₁(X,ℤ) → H₁(J,ℤ)` is an isomorphism, so `φ_* = q_* ∘ (AJ_∞)_*` on `H₁` and
`φ^* = (AJ_∞)^* ∘ q^*` on `H¹`.

| sealed use of `π` (line numbers from the inventory receipt) | reading in G | effect |
|---|---|---|
| `π_*` on cycles of `X₀(N)` — Stage I ll.159, 335; Stage II ll.102, 151 | `φ_*` | unaffected |
| `π*` on integral cohomology — `ADDENDUM_004` ll.56, 59 | `q^*`, equal to `φ^*` under `AJ_∞` | unaffected |
| `π` as the map `X → E₀` — Stage II l.52, its definition | `φ` | unaffected; no kernel or dual applies to it |
| `π` as `J → E₀`, its kernel, its restriction to `C₀`, `π([0]−[∞])` — Stage I ll.71, 113, 125, 289, 296, 351; Stage II ll.161, 164, 167; `ADDENDUM_004` l.53; `ADDENDUM_005` ll.63, 83 | `q` | unaffected |
| `π̂`, "its dual embedding" — `ADDENDUM_005` ll.63, 66, 177; `ADDENDUM_008` l.139; `ADDENDUM_009` l.132; `ADDENDUM_010` ll.25, 133; `ADDENDUM_011` l.122; `ADDENDUM_012` §§3, 6.1, 7; READMEs of 005, 008, 009, 012 | `q̂`, **with principal polarizations fixed here** | the seal never specified the polarization; G requires it to be principal (§6) |

`ADDENDUM_012`'s inventory lines are its verbatim quotations of the passages above plus its own uses of `π̂`, and
carry the same readings. Connected kernel, dualization, `q^∨` and `q̂` make sense **only** for `q`. No sealed
statement changes its intended meaning; what changes is that G never writes `π`.

*Notation.* This `q` is unrelated to the `q`-expansion parameter and to the family prime `q` of `E_q`; G uses
neither.

## 2. Setting and conventions

* `X = X₀(2p)(ℂ)`, compact. `F = F_p` is holomorphic and nonvanishing on `X` away from `S := supp(div F) = {[0],[∞]}`,
  with `div F = k([0]−[∞])`, `k = (p²−1)/8`, `v₂(k) = m ≥ 3` (frozen).
* `J = Hol(X)^∨ / Λ`, `Λ = {ψ ↦ ∫_x ψ : x ∈ H₁(X,ℤ)}`, with canonical principal polarization `λ_J`. For a degree-0
  divisor `D`, `AJ(D) = [ψ ↦ ∫_c ψ]` for any 1-chain `c` with `∂c = D`.
* `E₀` the Γ₀-optimal quotient with principal polarization `λ_{E₀}`; `H₀ = H₁(E₀(ℂ),ℤ)`; `τ` complex conjugation;
  `U₀ = H₀/ker(1+τ)`; `λ₀` the primitive integer functional on `U₀`, so that `α_p(x) = λ₀([φ_* x])`.
* `x·y` denotes the intersection forms on `H₁(X,ℤ)` and on `H₀`, unimodular and alternating. **Only their reductions
  mod 2 are used, and all sign conventions for them agree mod 2.**
* `ι_X : H₁(X,ℤ)/2 → J[2](ℂ)`, `ι_X(x̄) = [½∫_x]`, is a bijection independent of orientation, because
  `½∫_x − (−½∫_x) = ∫_x ∈ Λ`; likewise `ι_{E₀}`. Throughout `F₂ ≅ μ₂` by `a ↦ (−1)^a`.

## 3. Statements

    T_p  := [D] ∈ J[2](ℂ),    D := (k/2)·([0] − [∞]),   2D = div F              (k is even)
    S₀^B := ι_{E₀}(v̄),       v a primitive generator of H₀^{τ=−1} = ker(1+τ)    (sign of v irrelevant)

    (C_gen)    T_p = q̂(S₀^B)    in  J[2](ℂ)

**Theorem G.** For every `x ∈ H₁(X,ℤ)`:

    (G1)  (−1)^{χ_p(x)} = e_J(T_p, ι_X(x̄))
    (G2)  (−1)^{α_p(x)} = e_J(q̂ S₀^B, ι_X(x̄))
    (G3)  (C)  ⟺  (C_gen)
    (G4)  (C_gen)  ⟹  S₀^B ∈ E₀(ℚ)[2]

## 4. Proof of (G1) — Kummer–monodromy, through a literal branch cut

**Lemma 1 (a literal branch cut).** Choose `κ ∈ ℂ^×` so that no critical value of `κF` lies in the open ray
`(0,∞)`. This is possible because `κF` has finitely many critical values, and it changes neither `div F`, nor
`dF/F`, nor the monodromy of `√F`. Let `K` be the closure of `(κF)⁻¹((0,∞))`, each arc oriented from its pole end
to its zero end. Then:

1. `∂K = div F`;
2. for every loop `γ` in `X∖S` meeting `K` transversally, `w(γ) := (1/2πi)∫_γ dF/F = ±(γ·K)`, with one global sign
   fixed by the conventions;
3. `∫_K ψ = 0` for every `ψ ∈ Hol(X)`.

*Proof.* Over `(0,∞)` the map `κF` is an unramified covering of degree `deg F`, so `K` consists of `deg F` embedded
arcs, disjoint except at endpoints in `S`. Near a zero of order `m`, `κF` has local form `z^m`, so exactly `m` arcs
end there; near a pole of order `m`, exactly `m` arcs begin there. With the stated orientation
`∂K = Σ_P ord_P(F)·P = div F`, which is (1). On `X∖K` the function `κF` takes values in `ℂ∖[0,∞]`, where the branch
`Log` with argument in `(0,2π)` is holomorphic; so `L := Log∘(κF)` is holomorphic on `X∖(K∪S)` and jumps by `2πi`
across each arc. On each subarc of a transverse loop `γ` between crossings, `dL = dF/F`, so `∫_γ dF/F` is minus
the sum of the jumps at the crossings, which is (2). For holomorphic `ψ`, `d(Lψ) = (d(κF)/(κF))∧ψ = 0`, both
factors being `(1,0)`-forms. Stokes' theorem on `X` minus `ε`-discs about `S` and a thin neighbourhood of `K` gives
`0 = ±2πi∫_K ψ + O(ε|log ε|)`, the error coming from the `ε`-circles, where `L` has at most logarithmic growth.
Letting `ε → 0` gives (3). ∎

This is the inverse image of a ray with the `2πi` jump of `log F` made explicit, following McMullen's proofs of
the principal-divisor direction of Abel's theorem (cited by the operator; not in the corpus, not re-read here). It
is self-contained given Stokes' theorem, and it **replaces** the audited draft's Lemmas 1.1–1.2, which produced
`K` as an abstract Lefschetz-dual class. Lefschetz duality is no longer used.

**Proof of (G1).** Choose a 1-chain `c` with `∂c = D`, possible since `deg D = 0`. Then `K − 2c` has boundary
`div F − 2D = 0`; let `β ∈ H₁(X,ℤ)` be its class. Replacing `c` by `c + z` for a cycle `z` replaces `β` by
`β − 2z`, so `β̄` does not depend on `c`.

* *Jacobian side.* Lemma 1(3) gives `2∫_c ψ + ∫_β ψ = 0` for all `ψ`, so `AJ(D) = [∫_c] = [−½∫_β] = ι_X(β̄)`.
  Hence **`T_p = ι_X(β̄)`**.
* *Monodromy side.* Every `x ∈ H₁(X,ℤ)` is represented by a loop `γ` in `X∖S` transverse to `K` and `c`. Continuing
  `√F = exp(½ log F)` along `γ` multiplies it by `(−1)^{w(γ)}`, and by Lemma 1(2),
  `w(γ) ≡ γ·K = 2(γ·c) + γ·(K−2c) ≡ x·β (mod 2)`. So `(−1)^{χ_p(x)} = (−1)^{x·β}`.
* *Pairing.* By [F1], `e_J(ι_X(ā), ι_X(b̄)) = (−1)^{a·b}`; so `e_J(T_p, ι_X(x̄)) = (−1)^{β·x} = (−1)^{χ_p(x)}`. ∎

*Remarks.* Every sign convention — orientation, the sign in Lemma 1(2), the sign of the half-period, the sign of
`AJ` — enters only through a parity or through an equation `= 0`, so none can change (G1). The evenness of the cusp
orders is used exactly once, to write `div F = 2D`.

*Remark — the draft's Lemma 0, demoted; not used by any proof.* `Γ₀(2p)` has no elliptic points (`ε₂ = ε₃ = 0`,
since `p ≡ 3 (mod 4)` and `(−3/2) = −1`), so the sealed computation `χ_p(γ) = W(γ) mod 2` (`ADDENDUM_003` l.76) is the
winding of `F` along the projected loop with no orbifold correction. Echoed in `receipts/LATTICE_LEMMA_CHECK.txt`.

## 5. Proof of (G2) — the Betti point `S₀^B`

**Lemma 2 (uniform lattice lemma).** Let `H ≅ ℤ²` carry a unimodular alternating form `(a,b) ↦ a·b`, and let `τ` be
an involution of `H` with `τa·τb = −a·b`. Put `L⁺ = ker(τ−1)` and `L⁻ = ker(τ+1)`. Then `L⁺ = ℤu` and `L⁻ = ℤv`
with `u, v` primitive, and:

* **(a)** `[H : L⁺ + L⁻] = |v·u| ∈ {1, 2}`;
* **(b)** the integer functionals vanishing on `L⁻` are exactly the integer multiples of `f := v·(–)`; `f` is primitive
  and `τ`-invariant and induces `H/L⁻ ≅ ℤ`, so the primitive functionals on `U₀ = H/L⁻`, pulled back to `H`, are `±f`;
* **(c)** mod 2, the unique `s̄` with `f(y) ≡ s̄·ȳ` for all `ȳ` is `s̄ = v̄`;
* **(d)** the functional vanishing on `L⁻` normalized to `±1` on `u` is `f/f(u)`, integral iff `[H : L⁺+L⁻] = 1`;
* **(e)** `ū = v̄` iff `[H : L⁺+L⁻] = 2`.

*Proof.* `τ` reverses the form, so `det τ = −1`, and an involution of `ℤ²` with determinant `−1` has eigenvalues
`+1` and `−1` once each; so `L⁺`, `L⁻` have rank one. Take `u, v` primitive. (a) `H/L⁻ ≅ ℤ` because `v` is
primitive, so `H/(L⁺+L⁻)` is cyclic; for every `h`, `2h = (h+τh) + (h−τh)` with `h+τh ∈ L⁺` and `h−τh ∈ L⁻`, so that
cyclic group is killed by 2 and has order 1 or 2. The index of `ℤu + ℤv` is `|det(u,v)| = |v·u|`, the form being
unimodular. (b) Functionals vanishing on `ℤv` form `Hom(H/ℤv, ℤ) ≅ ℤ`; `f` vanishes on `v` and is primitive because
`v` is, so it generates; and `v·τy = −(τv)·(τ²y) = −(−v)·y = v·y`. (c) The mod-2 form is nondegenerate.
(d) `f(u) = v·u`. (e) `ū` and `v̄` are nonzero, and they coincide iff `det(u,v)` is even, iff the index is 2. ∎

The exact check (`computation/check_lattice_lemma.py`, `receipts/LATTICE_LEMMA_CHECK.txt`) corroborates (a)–(e) on
all 84 integral involutions of `ℤ²` with `det = −1` and entries in `[−6,6]` — 42 of index 1, 42 of index 2 — and all
three of its negative controls are caught. **It certifies only those finite cases; the universal statement is
Lemma 2.** It replaces the audited draft's check, whose comment A4 described a finite-box test as a universal
certificate.

*Lattice types.* Index 1 is the rectangular case `H = L⁺ ⊕ L⁻`, index 2 the non-rectangular one. For a real elliptic
curve, positive discriminant corresponds to the rectangular, two-component case and negative discriminant to the
non-rectangular, one-component case (classical; confirmed by the operator's external check). By (e), in the index-2
case the plus and minus lines coincide mod 2 — the same characteristic-2 collapse met before — and by (d) that is
exactly where normalizing on the plus line fails to be integral.

**The Betti point.** Apply Lemma 2 to `H = H₀`. By [F1] and Lemma 2(b),(c), `S₀^B = ι_{E₀}(v̄)` satisfies
`e_{E₀}(S₀^B, ι_{E₀}(ȳ)) = (−1)^{v·y} = (−1)^{λ₀([y])}` for every `y ∈ H₀`. It is nonzero, and real: complex
conjugation acts on `H₀` as `τ` and commutes with `ι_{E₀}` [F10], and `τv̄ = −v̄ = v̄`. **`S₀^B` is half a primitive
anti-invariant cycle.**

**Lemma 3 (functoriality through the quotient).** For `s ∈ E₀[2]` and `t ∈ J[2]`, `e_J(q̂s, t) = e_{E₀}(s, qt)`, and
no degree factor occurs.

*Proof.* With `e_n : A[n] × A^∨[n] → μ_n` the canonical pairing and `e^λ(x,x') := e_n(x, λx')`,

    e^{λ_J}(t, q̂s) = e_n^J(t, λ_J λ_J⁻¹ q^∨ λ_{E₀} s) = e_n^J(t, q^∨(λ_{E₀} s))
                    = e_n^{E₀}(qt, λ_{E₀} s) = e^{λ_{E₀}}(qt, s),

by the adjunction `e(a, q^∨ b) = e(qa, b)`, and for `n = 2` skew-symmetry allows the arguments to be reordered [F2]. ∎

Moreover `q(ι_X(x̄)) = ι_{E₀}(φ_* x̄)`: `q` is the homomorphism with `q ∘ AJ_∞ = φ`, so its analytic representation
sends `ℓ ∈ Hol(X)^∨` to `ℓ ∘ φ^*`, and for `ℓ = ½∫_x` this is `ψ' ↦ ½∫_x φ^*ψ' = ½∫_{φ_*x} ψ'`.

**Proof of (G2).** By Lemma 2(b), `α_p(x) = λ₀([φ_* x]) = ±(v·φ_* x)`, so

    (−1)^{α_p(x)} = e_{E₀}(S₀^B, ι_{E₀}(φ_* x̄)) = e_{E₀}(S₀^B, q(ι_X x̄)) = e_J(q̂ S₀^B, ι_X(x̄)).   ∎

## 6. Where the anticipated mismatches actually live

* **Sign.** Enters only through parities and through equations `= 0`; cannot affect G.
* **Plus/minus eigenspace — real, located in the definition of `α_p`, not in G.** Lemma 2(d),(e): the plus-line
  normalization fails to be integral exactly in the non-rectangular case. The displayed negative-branch base has
  `Δ < 0`; `E₀ = E` is recorded at `n = 5,7,13,17` (`ADDENDUM_007`) but not uniformly. G uses the sealed `U₀`
  definition, which is why that definition is load-bearing.
* **Polarization — real, located in `q̂`.** With principal `λ_J`, `λ_{E₀}`, Lemma 3 holds with no factor. Replacing
  `λ_{E₀}` by `d·λ_{E₀}` gives `e^{dλ} = (e^λ)^d`, identically trivial mod 2 for even `d`, so an even-degree
  polarization in the definition of the dual map would silently break (G2). §1 fixes principal polarizations.
* **Degree.** No degree factor occurs in the adjunction. Any induced-polarization degree occurs elsewhere and is not
  needed by G.

## 7. Proof of (G3) and (G4)

**(G3).** `ι_X` is onto `J[2](ℂ)`. By (G1) and (G2), `(C)` holds iff `e_J(T_p, t) = e_J(q̂S₀^B, t)` for all
`t ∈ J[2]`, iff `e_J(T_p − q̂S₀^B, t) = 1` for all `t`, iff `T_p = q̂S₀^B` by nondegeneracy [F5]. ∎

**(G4).** Suppose `T_p = q̂(S₀^B)`. Its divisor is supported on the `ℚ`-rational cusps `0` and `∞`, and `X` has the
rational point `∞`, so `T_p ∈ J(ℚ)`, the analytic class realizing the algebraic one through `Jac(X) ≅ Pic⁰(X)` [F9].
`q`, `λ_J`, `λ_{E₀}` and `q^∨` are defined over `ℚ`, so `q̂` is; since `ker q` is connected, `q^∨`, hence `q̂`, is a
closed immersion, injective on geometric points [F6]. Fix `ℚ̄ ⊂ ℂ`; all 2-torsion is `ℚ̄`-rational. For `σ ∈ G_ℚ`,

    q̂(σS₀^B) = σ·q̂(S₀^B) = σT_p = T_p = q̂(S₀^B),

so `σS₀^B = S₀^B`, and `S₀^B ∈ E₀(ℚ)[2]`. ∎

    Rationality of S₀^B is a consequence of (C_gen), not an input.

## 8. Consequences

* `(C) ⟺ (C_gen)`. What `ADDENDUM_005` called `(C′)`, with its unjustified `S₀ ∈ E₀(ℚ)[2]`, is replaced by `(C_gen)`,
  in which rationality is derived.
* `(C)` says precisely: **the cuspidal point `T_p` is the image, under the dual map built from principal
  polarizations, of the real 2-torsion point of `E₀` that is half a primitive anti-invariant cycle.**
* **For R:** `(C)` is an equality of two named geometric 2-torsion points, `T_p = q̂(S₀^B)`. A repaired `(D3)` route
  must recover it, including the real/étale position of `S₀^B`, which a differential may not see.
* **Level-specific items — dependencies only; not covered by the operator's audit.** (i) `ADDENDUM_003` and
  `ADDENDUM_004` report `χ_p = α_p mod 2` on full homology at `N = 62, 254`; granted G, `T_p = q̂(S₀^B)` there. This
  adds no evidence, and `N = 62` remains forced. (ii) At `n = 5,7,13,17`, where `ADDENDUM_007` records `E₀ = E` on
  Cremona's ecdata (an external authority) and `E` has `Δ < 0`, `E(ℝ)[2] = {O, (0,0)}`; since `S₀^B` is real and
  nonzero, `S₀^B = (0,0)` there. Both rest on those earlier sealed results and were not re-audited.

## 9. Classical facts used — sources not in the corpus

None of these sources is present in the corpus as a source text (`receipts/REFERENCE_PRESENCE.txt`). The one
author-pattern match, `stein_watkins_v1.txt` — Stein–Watkins, *Modular parametrizations of Neumann–Setzer elliptic
curves* — is a different work with no Proposition 3.3, and is recorded as such. Locations supplied by the operator
in the audit are recorded as operator citations, not re-read here.

* **[F1]** The polarized Weil pairing over `ℂ` is the Riemann form on integral homology, up to sign; for a Jacobian
  that form is the intersection form. *Operator cites Milne, Abelian Varieties, Example 13.3.*
* **[F2]** The adjunction `e(a, q^∨ b) = e(qa, b)` and skew-symmetry of the polarized pairing. *Operator cites Milne,
  Proposition 13.2.*
* **[F5]** Nondegeneracy of the Weil pairing.
* **[F6]** The dual of an optimal quotient (connected kernel) is a closed immersion. *Operator cites Stein,
  Proposition 3.3;* also asserted in the seal at `ADDENDUM_005` l.83.
* **[F9]** `Jac(X) ≅ Pic⁰(X)` for a compact Riemann surface. *Operator cites McMullen.*
* **[F10]** Complex conjugation on `E₀(ℂ)` acts on `H₁` as `τ` and commutes with the half-period map.
* **[F8]** Elliptic-point counts — used only by the demoted remark.

No longer used after repair: Lefschetz duality (draft [F7]) and the abstract branch-cut form of Abel's theorem
(draft [F4]), both replaced by the self-contained Lemma 1; draft [F3] (skew-symmetry) is folded into [F2]. None of
the facts above is a characteristic-2 or bad-reduction statement; G uses no integral model.

## 10. What this addendum does not do

* It does **not** prove `(C)`. It proves `(C) ⟺ (C_gen)`, in a repaired text awaiting re-audit.
* It does not touch `(D3)`, M or R, and does not settle uniform optimality `E₀ = E`; the `B` vertex is live.
* It does not determine, uniformly, which rational 2-torsion point `S₀^B` is.
* The positive branch remains outside this architecture.

## 11. Repair ledger

| audit item | audit status | required action | applied as | where |
|---|---|---|---|---|
| `π` used for two maps | seal-blocking | split `q : J → E₀` from `φ = q∘AJ_∞ : X → E₀`; define `q̂`; state a crosswalk; rename nothing sealed | done; the inventory shows the sealed record, Stage II included, uses `π` both ways | §1, §3, §5, §7 |
| G1 Kummer/monodromy | pass with repair | literal geometric branch cut `F⁻¹(ray)` | Lemma 1; Lefschetz duality removed | §4 |
| G2 Betti point | pass | uniform lattice lemma instead of a bounded computation | Lemma 2 (a)–(e) | §5 |
| G2 functoriality | pass | split `q` from `φ` | Lemma 3 with `q̂`; `q(ι_X x̄) = ι_{E₀}(φ_* x̄)` | §5 |
| principal polarization | pass, load-bearing | keep the explicit definition of `q̂` | kept | §1, §6 |
| G3 | pass | none beyond G1/G2 | restated with `q̂` | §7 |
| G4 | pass | rewrite with `q`, not the sealed `π` | rewritten | §7 |
| 84-involution receipt | pass as finite check | narrow A4's certification claim | new check states its finite scope, labels C4 finite-box, adds three caught negative controls | `computation/check_lattice_lemma.py` |
| rectangular/rhombic trap | pass mathematically | insert the uniform index-{1,2} proof | Lemma 2(a),(d), with (e) | §5 |
| Lemma 0 | correct, nonessential | demote to a remark/receipt | demoted | §4 |
| §8 level-specific consequences | not re-audited | keep only as dependencies on earlier sealed `E₀ = E` results | so marked | §8 |
| §6 degree sentence | soften | say no degree factor occurs in the adjunction | done | §6 |

## 12. Custody

* `01_audited_draft/` holds the three files the operator audited, byte-identical to what was delivered
  (`receipts/AUDITED_DRAFT_CUSTODY.txt`). They are preserved unmodified and superseded by this text.
* `computation/verify_verbatim_blocks.py` is carried unmodified from `ADDENDUM_012` (`ad758846…`), where it was shown
  to catch five tampered inputs; it confirms every §1 quotation byte for byte (`receipts/VERBATIM_VERIFICATION.txt`).
* `receipts/`: `LATTICE_LEMMA_CHECK`, `PI_USAGE_INVENTORY`, `REFERENCE_PRESENCE`, `AUDITED_DRAFT_CUSTODY`,
  `CANONICAL_VERBATIM`, `VERBATIM_VERIFICATION`.

**The H41 seed remains unproved.**
