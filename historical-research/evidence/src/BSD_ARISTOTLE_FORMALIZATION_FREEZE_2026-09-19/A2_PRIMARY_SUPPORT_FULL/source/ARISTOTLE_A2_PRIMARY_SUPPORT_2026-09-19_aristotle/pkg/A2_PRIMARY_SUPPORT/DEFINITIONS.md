# DEFINITIONS — A2 (frozen in `PrimarySupport/Defs.lean`)

| Lean name | definition | meaning / source | traps |
|---|---|---|---|
| `primaryPart G p` | `{x \| ∃ k, p^k • x = 0}` as an AddSubgroup | G[p^∞] | only meaningful for primes; every target restricts to primes where it matters |
| `primesOutside S0` | `{p \| p.Prime ∧ p ∉ S0}` | Codex's P | — |
| `vInf p a` | `if a = 0 then ⊤ else padicValInt p a` | v_p with v_p(0) = ∞ | `padicValInt` is junk for non-primes, so every J-target assumes P ⊆ primes |
| `JOf P h` | `{a : ℤ \| ∀ p ∈ P, h p ≤ vInf p a}` | Codex's J_E with h = h_p (WC §1) | 0 ∈ JOf always |
| `posSupport P h` | `{p \| p ∈ P ∧ h p ≠ 0}` | primes of positive depth | — |
| `content z` | `Finset.univ.gcd z` for z : Fin n → ℤ | gcd of coordinates, normalized ≥ 0 (FORMALIZABLE_GAPS A3) | content 0 = 0; for n = 0 the only vector is 0 |
| `reduceMod m z` | `fun i => (z i : ZMod m)` | reduction of a lattice vector mod m | ZMod 0 = ℤ; ZMod 1 is trivial |

**Relation to package A1.** A1's `JE t P` is by definition `JOf P (hInf t)`, with `hInf` the witness depth. So J1–J4 here
characterise A1's J_E. The packages do not import each other.
