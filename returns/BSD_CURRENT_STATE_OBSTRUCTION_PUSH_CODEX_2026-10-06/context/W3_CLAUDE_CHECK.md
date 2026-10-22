# Independent check of the W3 p = 17/19 and Heegner-ν return (Claude, Opus 5.5, 2026-10-06)

**Archive.** `9a3a411e-…-aristotle.tar.gz`: sha256 f8f84f1a…, 251 entries, runs be7a0018 and 4e7dc730.

**Integrity.**
- `MANIFEST.sha256`: 166 of 167 entries verify. The one mismatch is `README.md`, which differs only by Aristotle's citation banner; with the banner stripped, the hash matches.
- The bundled executables were **not run**.

**Independent compile.** Read-only, Lean v4.28.0, Mathlib 8f9d9cff.
- All five files exit 0 with no errors and no `sorry`: KolyvaginVanishingOrder 49 s, Seed17Symbols 19 s, Seed19Symbols 25 s, QuadraticJetForcing 8 s, Main 6 s.
- `#print axioms` for all 15 declarations shows a subset of {propext, Classical.choice, Quot.sound}; `alpha_inv` uses none. There is no `Lean.ofReduceBool`, so no `native_decide`.

**Claim audit against the record.**
- **p = 17.** ℓ₀..ℓ₄ ≡ 0, 0, 0, 0, 13, so λ = 4. This agrees with the 10-06 seed-admission finding Reg_γ = 17·13 + O(17²): a 17-divisible normalized regulator, while Ш[17] = 0 is settled. It is a negative calibration for the ℓ₂ route, not a Ш alarm.
- **p = 19.** ℓ₂ ≡ 18, so λ = 2. With the imports (Kato divisibility, control, the Schneider / Perrin-Riou leading term, the main-conjecture identification), Ш[19^∞] = 0. p = 19 was already settled by Ota (ℓ = 191).
- **Local data.** c₃ = c₅₈₄₃ = 2 and c₂₂₄₃ = 1 are consistent with Tamagawa product 16. Surjectivity holds at 17, 19 and 53 by Serre's criterion.
- **L′(E^{(−23)},1) = 39.8472780641** in floating point. This is consistent with the record's certified partial sum 39.847278312318874 ± 4.3·10⁻¹⁶ (tail ≤ 0.335), and the record's certificate is the stronger one.
- **Heegner ν.** ν_p ≤ 2 ⟺ ν_p = 1 ⟺ Ш[p] = 0 cofinitely. This agrees with the record's closed lane NU_LE_TWO_RESTATES_SELMER.
- **Heuristic warning (kept as HEURISTIC).** If ℓ₂ mod p behaves like a random residue, ℓ₂ ≢ 0 should fail at infinitely many p. So a FIN mechanism must see #Ш separately from the regulator.

**Endpoint effect: none.** FIN, ORDER9 and Q36 are unchanged.
