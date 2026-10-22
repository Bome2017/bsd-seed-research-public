# Audit of the decisive step in the Cloud Néron review (b358f75)

**Verdict: `DECISIVE_STEP_AGREES`.** The result holds only at the import grades the review itself states. The step is b = 1 at 4547: `2·4547·ω_G` lies in the Néron lattice for the packet theta forms. No discrepancy was found.

## Scope

- **Audited:** from Lemma N1 through Theorem N4 of `work/neron_normalization_review/output/02_DENOMINATOR_LATTICE.md`. This follows the handoff rule: a supplied result has its decisive step audited, not rebuilt.
- **Source copy:** a fresh read-only clone of branch `claude/paired-kernel-construction-phivfw` at `b358f7507759dad4a1e016c519d6f486ffca37e1`, placed in the scratch folder.
- **Not touched:** the staging folder, the lab worktree and every sealed folder.
- **Not audited here:**
  - Phase 1 (the Kim–Ota / ARS chain, including the flagged weakest link, KO Remark 6.6(1));
  - the retained `c_E | 2^9` and `2^8 S ⊆ H`;
  - the prior numerical check of `03` Lemma 4.

## What was checked

1. **CNS Prop. 5.14 statement (offline v3 text, lines 2648–2663).** The review quotes (5.14.1) correctly:
   - `≥ −v_p(N)` at ℓ = 0;
   - `≥ −v_p(N/L) + 1/(p−1)` for 0 < ℓ < v_p(N);
   - `≥ 0` at ℓ = v_p(N).

   Each condition is checked at "some (equivalently, any)" cusp with the given ℓ.
   - Valuations are normalized so that `val_p(p) = 1` (CNS §1.4).
   - The expansions are those of `f|_2 γ` with γ ∈ SL₂(Z), expanded in `e(nz/w(c))`, with no width factor (CNS (4.2.2); Lemma 5.13).
   - This is the normalization Lemma N2 uses.
2. **Thresholds re-derived from (5.9.1) and (5.12.1).**
   - A cusp of denominator p^ℓ lies on the (ℓ, n−ℓ)-component.
   - For a, b ≥ 1, d/e = p^{m−1}(pb−b−1) / (p^{m−1}(p−1)) = b − 1/(p−1), with m = min(a, b), in both the a ≥ b and a ≤ b cases.
   - The case a = 0 gives d/e = n, and b = 0 gives 0.
3. **Lemma N2 inputs, derived by hand.**
   - Theta transformation prefactor: weight 2 gives (−i)² = −1; with c^{−2} and det^{−1/2} = N^{−1}, the prefactor is −1/(2Nc²) for Θ = θ/2.
   - Split case (Eichler order of level p^n, e ≤ n): the Gauss sum factors into a hyperbolic plane and a p^n-scaled plane. It is p^{3e}·(p^e-th root of unity) or 0.
   - Division case (maximal order, e = 1): reduce mod π and complete the square in F_{p²}. The result is −p³·(p-th root of unity) or 0.
   - Pairing l with −l cancels the 1/2 at p = 2.
4. **Own brute force** (`scripts/`, `out/`; 12/12 PASS, 10 s CPU, 75 MB).
   - Split case: (p, n, e) = (5,2,1), (7,2,1), (3,2,1), (2,3,1), (2,3,2), (2,3,3), (5,2,2).
   - Division case: p = 3.
   - The nonzero branch was forced at e = 2.
   - This is separate code from the cloud's `gauss_level_p2_check.py`.
5. **Rational singularities (CNS Thm 6.12, text lines 3016–3020).**
   - (a) holds at 2243, 4547 and 5843.
   - (b) holds at 3, since v₃(N) = 1.
   - (c) holds at 2, since 3 | N and 3 ≡ 3 (mod 4); 2243, 4547 and 5843 are also ≡ 3 (mod 4).
   - Prop. 6.2 with Ex. 6.3 then gives H⁰(X₀(N)_{Z_(p)}, Ω) = Néron lattice at every p.
6. **Theorem N4 algebra.**
   - π_E∘i_E = [ed].
   - T_l is Rosati-invariant for l ∤ N, so i_E^* kills f^⊥.
   - The pullback identity is i_E^*ω_G = λ_f(G)(ed/c_E)ω_E, which gives D0·c_E·K_E ∈ Z.
   - c_E is an integer dividing 2⁹, so B_θ = D0·2⁹ = 2¹⁰·4547.
7. **Arithmetic.**
   - 2¹⁰·4547 = 4,656,128 (log₂ = 22.15, 23 bits); 2¹⁷·4547 = 595,984,384.
   - 1/(2B) = 1.0739e-7 and 8.389e-10.
8. **Commit scope.** e5b4dd2..b358f75 changes only `work/neron_normalization_review/output/`: 10 files, +602 lines, no deletions.

## Observations

- **b = 1 at 4547 has slack.** After one factor of p, N2 gives ≥ 0 at the intermediate cusps against the threshold −1 + 1/4546. So b = 1 would survive a misreading of the 1/(p−1) term in either direction. It needs only N2 and the general shape of (5.14.1).
- **The sharper 2¹⁰ has no slack at 2.** With p = 2, 1/(p−1) = 1, so after one factor of 2, N2 gives exactly the threshold ℓ − 2 at ℓ = 1 and 2. The 2¹⁰ therefore depends on N2 being exact at 2, including the ±l cancellation of the 1/2 (checked). The join form 2¹⁷ does not use N2 at 2.
- **At ℓ = v_p(N)**, the check can be made at ∞ (integrality, N1). The e = n Gauss sums are not needed there.
- **Sharpness of b = 1 was not tested**, and the review says so. b = 0 would hold if and only if, at an intermediate 4547-cusp, each weighted coefficient sum is ≡ 0 mod (1 − ζ_p). That is a congruence on weighted local counts. It was not examined here and is not needed for the upper bound.

## Claims

No seed value, witness, M, FIN, ORDER9 or Q36 is claimed. Nothing was committed, pushed or sent.
