# Independent check of the rev2 Aristotle return, and of the critique of it

Date: 2026-09-22. Additive file; nothing existing was modified.

Object checked: `~/Downloads/863950d0-2212-4024-943a-eb69fa4ef59f-aristotle.tar.gz`
(sha256 `71c6285221a8f5dfacaf5dad6d2c258156204125555071d1947787e0cb056253`), containing
`C2_WITNESS_REPORT.md`, `ARISTOTLE_SUMMARY.md`, `RequestProject/C2Witness.lean` (469 lines), and an embedded copy of
the input packet.

## What I did

1. **Packet identity.** Extracted the embedded `C2_WITNESS_2026-09-22_rev2.tar.gz` and compared it file by file with
   `~/BSD_C2_WITNESS_2026-09-22/`: all 8 files identical by sha256. The return was produced against rev2.
2. **Lean, textually.** No `sorry`, no `admit`, no `axiom`, no `native_decide`. All 24 theorem names cited in the
   report's table exist in the file. **Not compiled here** (Mathlib build), so "builds against Mathlib" and the axiom
   list are unverified, exactly as in the critique.
3. **The algebra, independently.** Re-derived and numerically verified the central identities for p = 5, 7, 11, 13,
   23, 31, 53 over 200 random packets each, without using the Lean file:
   - `2c₂ = M₁ − M₂` with `M_k = Σ_j j^k v_j`;
   - `Σ_x x² v(x) = −c_{p−3}` for the Lagrange interpolant `v(x) = Σ_i c_i x^i`;
   - granting `M₁ = 0`: `c₂ = −M₂/2 = c_{p−3}/2`;
   - packets of degree ≤ p−4 give `M₂ = 0`;
   - `γ ↦ γ^a` scales `M₂` by `a^{−2}`.
   All hold. The critique's display `c₂ = −½Σ j²v_j = ½b_{p−3}` is correct.
4. **Bertolini–Darmon, primary source.** Fetched *Derived p-adic heights* and read Definition 2.20, Theorem 2.23 and
   Corollary 2.24 directly.

## Verdict on the critique, point by point

| # | critique's point | my finding |
|---|---|---|
| 1a | M3's `Ш(E/K)[p^∞] = 0` conflicts with the project's own Cassels–Tate shortcut | **correct** |
| 1b | `ρ_p = 4` controls the order, not the regulator's valuation | **correct, and confirmed against BD** |
| 2 | "equivalently λ = 2" clauses omit `μ = 0` | **correct but narrow** |
| 3a | the identity does not exclude a weighted-correlation theorem | **correct, and the report already says so** |
| 3b | "o(p) errors are invisible mod p" is wrong | **correct: a wording error in the report** |
| 4 | the computational primitive is not shown to be necessary | **correct** |
| 5 | the 4547 twist aside is already resolved: type III, not I₀* | **correct** |
| 6 | the formalization proves polynomial relations, not an explicit isomorphism | **correct** |

### Details

**1b is the substantive one, and BD settles it.** Definition 2.20 defines `R_der` as the product of the partial
regulators `R^{(k)} = det((( , ))_k)` when `(( , ))_{p−1}` is nondegenerate, living in `(I^{ρ_p}/I^{ρ_p+1} ⊗ Q)/Z_p^×`;
`ρ_p = Σ_k k·ρ^{(k)}` is called the *order of vanishing* of `R_der`. Theorem 2.23 gives the leading coefficient as
`#Div(Ш(E/K)_{p^∞}) · R_der`, and Corollary 2.24(1) says nondegeneracy gives *order* equality `ν_p = ρ_p`, while
2.24(2) only bounds the denominator (`p^B·R_der` is integral, `p^B = #(Ш/Div Ш)`). So:
- nondegeneracy ⟹ the order is `ρ_p`; it says nothing about the valuation of `R_der`;
- `c₂ ∈ Z_p^×` needs the *leading coefficient* to be a unit, i.e. `Div(Ш)` trivial **and** `R_der ∈ Z_p^×`.
The critique's `[[0,p],[−p,0]]` (nondegenerate alternating, determinant `p²`) is exactly a legitimate `R^{(k)}` of
valuation 2. **M3 as written is missing the unit condition on the derived regulator**, and the packet's own
`INPUTS.md` §2 ("the extra input is exactly `ρ_p = 4`") carries the same gap, so this correction lands on the packet
as well as on the return.

**1a.** `CASSELS_TATE_SHORTCUT.md` §2 concludes `A = Ш(E/Q)[p^∞] = 0` "with no condition on the twist's Sha support",
via `v_p(#Ш(E/K)) ≤ 2c` and `#B ≥ p^{2c}`. Under that bridge `Ш(E/K)[p^∞] ≅ A ⊕ B` need not vanish. M3's
`Ш(E/K)[p^∞] = 0` is therefore strictly stronger than what the project's own forward bridge supports. The report does
label M3 *conditional*, so this corrects a conditional claim, not a proved one.

**2.** The report's principal statements do include `μ = 0` (VERDICT, item 11, and M2's first clause). The omissions
are in the trailing clauses "equivalently `λ(L_p) = 2r`" (VERDICT), "equivalently `λ(L_p) = 4`" (M2) and
"equivalently `λ(𝓛) = 2`" (§5). The Lean theorem `isUnit_c2_iff_order_eq_two` is stated as the order of the mod-`p`
reduction, which is correct. The critique's `F = pT²` (μ = 1, λ = 2, quadratic coefficient `p`) is a valid witness to
the gap.

**3b.** The report's §3A says equidistribution errors "are `o(p)` … and are *invisible mod p*". As written that is
false — a constant error 1 is `o(p)` and nonzero mod `p`. The defensible statement is the converse one: an
archimedean or ℓ-adic bound of size `o(p)` gives *no control at all* of the class mod `p`. The conclusion survives;
the sentence does not.

**3a, 4.** Both are logical-scope points and both are right. The report itself labels §3A/§3B inferences
"unsupported" and §3D says no impossibility is claimed, so 3a agrees with the report's own caveats rather than
contradicting it. For 4, nothing in the report shows that per-value evaluation of `ψ̄` is *necessary*: the target is
the single scalar `Σ_j j²ψ̄(γ^jP₁) mod p`, and a method computing that sum directly would do.

**5.** `TWIST_NORM_INTERIM.md` §3 records the seed at 4547 as Kodaira **III**, `v_4547(j) = 0`, potentially
supersingular, robust across the isogeny class. The report's `I₀*` speculation is dead. Its own words ("the Kodaira
type at 4547 is not in the packet") are accurate about the packet, and it flags the aside as unsupported; the project
simply already has the answer.

**6.** `grep` for `RingEquiv|AlgEquiv|MulEquiv` in `C2Witness.lean`: zero hits. Item 4's `𝔽_p[G₁]/I³ ≅ 𝔽_p[t]/(t³)`
is carried by `one_add_X_pow_char` ((1+X)^p − 1 = X^p) and `X_pow_mem_span_X_pow_three` (X^p ∈ (X³)), i.e. the two
relations that would make such an isomorphism work, not the isomorphism itself. The report's own §1 is explicit that
the arithmetic inputs are abstracted and that BLV, Ш and the bridge are not formalized.

## What stands

- The reduction `c₂ ≡ −½ Σ_j j² v_j` under the retained lower-order vanishing, and its sharp form
  `c₂ ∈ Z_p^× ⟺ c_{p−3} ≠ 0`: **verified here independently of Lean**, for many primes.
- Generator-independence of the witness: verified.
- The annihilation of packets of degree ≤ p−4: verified.
- The verdict itself ("none of quantifier levels 1–4"; no new nonvanishing) is what the report claims; the critique's
  opening sentence restates it rather than correcting it.

## Recommended edits before this becomes project authority

1. Restate M3 as: `c₂(p) ∈ Z_p^×` ⟺ `ρ_p = 4` **and** the leading coefficient `#Div(Ш(E/K)[p^∞])·R_der` is a
   p-adic unit — i.e. divisible part trivial **and** `R_der ∈ Z_p^×`. Note that this is stronger than the forward
   bridge's `Ш(E/Q)[p^∞] = 0`. Correct `INPUTS.md` §2's "the extra input is exactly `ρ_p = 4`" the same way.
2. Add `μ = 0` to the three trailing "equivalently λ = …" clauses.
3. Replace "invisible mod p" with "not controlled mod p".
4. Restate the computational primitive as sufficient, not necessary; record that evaluating the weighted sum directly
   would also suffice.
5. Drop the 4547/I₀* aside, citing `TWIST_NORM_INTERIM.md` §3 (type III).
6. Say "the two relations underlying `𝔽_p[G₁]/I³ ≅ 𝔽_p[t]/(t³)`", not "the isomorphism", unless an explicit
   `RingEquiv` is added.

Not checked here: the Lean build and axiom list; BLV's ordinary equality; the forward bridge (frozen, not re-audited).
