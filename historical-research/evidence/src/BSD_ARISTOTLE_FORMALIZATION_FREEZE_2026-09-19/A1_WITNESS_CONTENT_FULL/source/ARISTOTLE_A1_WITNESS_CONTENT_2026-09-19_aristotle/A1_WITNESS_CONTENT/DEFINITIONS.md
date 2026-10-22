# DEFINITIONS — A1 (frozen in `WitnessContent/Defs.lean`)

| Lean name | definition | mathematical meaning / Codex source | junk values and traps |
|---|---|---|---|
| `primaryPart G p` | AddSubgroup `{x : G \| ∃ k, p^k • x = 0}` | the p-primary part G[p^∞]; Sha[p^∞] when G = Sha | for p prime this is the usual p-primary component |
| `PDvd p j t` | `∃ y, p^j • y = t` | t ∈ p^j M | `PDvd p j 0` holds for every j (T5b) |
| `depth p t` | `sSup {j \| PDvd p j t}` in ℕ | Codex's depth_M(t) = max{j ≥ 0 : t ∈ p^j M} (WC §1) | meaningful only for t ≠ 0 with p^a • M = 0 (T5). For t = 0 the set is unbounded and `sSup = 0` is junk, so `depth` is never applied to 0 in `hInf` |
| `primesOutside S0` | `{p \| p.Prime ∧ p ∉ S0}` | Codex's P | — |
| `hInf t p` | `⨅ (S) (_ : t p S ≠ 0), (depth p (t p S) : ℕ∞)` | Codex's h_p = min{depth(t(p,S)) : t(p,S) ≠ 0}, and ∞ if there is none | equals ⊤ exactly when every witness at p vanishes (T6) |
| `vInf p a` | `if a = 0 then ⊤ else padicValInt p a` | v_p(a) with v_p(0) = ∞ | — |
| `JE t P` | `{a : ℤ \| ∀ p ∈ P, hInf t p ≤ vInf p a}` | Codex's J_E (WC §1). It is an ideal; its nonzero characterisation is in package A2 | 0 ∈ JE always. The antecedent is ∃ A ≠ 0 with A ∈ JE |
| `augHom R G` | `MonoidAlgebra.lift R R G 1` | augmentation R[G] → R, Σ a_g g ↦ Σ a_g | — |
| `augIdeal R G` | `RingHom.ker (augHom R G)` | augmentation ideal I (commutative G) | — |
| `gr R G r` | `↥(I^r) ⧸ comap (I^r).subtype (I^(r+1))` | graded piece I^r/I^(r+1) (a module over R[G]) | — |
| `cls2 θ` | class of θ in I²/I³ if θ ∈ I², else 0 | Codex's t(p,S), the degree-two image of θ_S | the `else 0` branch is junk. Under the imported Ota 5.17 input θ ∈ I² always holds (T4) |
| `augSubZ G` | kernel of the augmentation ℤ[G] → ℤ, as a ℤ-submodule | used only for stretch S1 (non-commutative G) | powers are products of ℤ-submodules of the ℤ-algebra ℤ[G] |

**Model of the arithmetic objects (T8).** Every arithmetic object is represented by an abstract datum:

| arithmetic object | abstract datum in T8 |
|---|---|
| G_S = Gal(Q(μ_S)/Q) | a commutative group `G p S` with exponent `e p S > 0` (T11: `(ZMod S)ˣ`) |
| Z_p | a commutative ring `Rp p` in which prime-to-p naturals are units (T10: `ℤ_[p]`) |
| θ_S ∈ Z_p[G_S] | an element `θ p S : MonoidAlgebra (Rp p) (G p S)` |
| r_{p^∞} = corank_{Z_p} Sel(Q, E[p^∞]) | a natural number `r p` |
| Sha(E/Q) | an abelian group `Sha` |
| the admissible conductors S at p | an index type `W p` |
