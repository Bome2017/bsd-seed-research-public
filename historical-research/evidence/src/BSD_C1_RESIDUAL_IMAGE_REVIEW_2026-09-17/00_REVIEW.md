# Review of the positive residual-image theorem (2026-09-17)

Verdict: **ALL_ODD_RESIDUAL_IMAGE_VERIFIED**.

Input: `src/C1_ODD_RESIDUAL_IMAGE_2026-09-17/` (zip sha256 c76da9a88579fa832539a8e9206a08219199a99df8558acaaeaf277e248d1d4c), containing
`PROOF.md`, `verify.py`, `EXACT_CHECK_RECEIPT.json`, `SOURCES.md`, `ACCEPTED_REVIEW_NOTE.md`, and the preserved `input/00_REVIEW.md`
(byte-identical to my central-involution review, ede65808…).

Private directory; this review writes no shared file. No number field, class group, Selmer group or Sha order was computed. No field
construction, no calibration, no K33 work. Resources: about 0.2 CPU-seconds of the 60 allowed, one process.

## 1. The statement

For positive m, n with m, A = m+16n², B = m+25n² all prime and ≡ 11 (mod 24), and E: y² = x³ − 5Ax² + 4ABx, the mod-ℓ image is
GL₂(F_ℓ) for **every odd prime ℓ**. (ℓ = 2 is necessarily excluded: (0,0) is a rational 2-torsion point.)

## 2. Reconstructed before replay — each step checked

| step | check | result |
|---|---|---|
| **hypotheses are Zywina's own** | read Theorem 1.2 in the local source `34_SRC_zywina_2502.01957v1.txt` | verbatim: "m, m+16n² and m+25n² are primes congruent to 11 modulo 24", concluding E(Q) ≅ Z/2Z × Z². No mod-7 condition, no 840/420. The paper also lists the fibres I₁, III, I₂, I₀* at 0, −16, −25, ∞, matching our generic-surface work. |
| 12 \| n and A > 163 | 24 \| 25n² ⇒ 24 \| n²; residues checked | n ≡ 0 (mod 12) is the only possibility; A ≥ 11 + 16·144 = 2315 > 163 |
| invariants | symbolic | c₄ = 16A(13m+100n²) and Δ = 2⁸3²mA³B² both hold identically |
| multiplicative primes | reductions of c₄ | c₄ ≡ 25600n⁴ (mod m), ≡ 32400n⁴ (mod B), and 13m+100n² ≡ −108n² (mod A); with m ≥ 11, B ≥ 3611, A ≥ 2315 and m,B,A ∤ n these are nonzero, giving I₁ at m, I₂ at B, v_A(c₄) = 1, v_A(Δ) = 3 |
| observed types | PARI `elllocalred` on (3011,420) **and** (3491,60) | m → I₁ (c=1), A → III (c=2), B → I₂ (c=2), 3 → I₂ (c=2), 2 → I₁* (c=2); Tamagawa product 16 in both cases |
| **the local model at A** | symbolic | x = u²X, y = u³Y with u⁴ = A gives exactly Y² = X³ − 5u²X² + 4BX; its discriminant is Δ/u¹² with no factor of u, hence a unit; the special fibre is Y² = X³ + 4B̄X with B̄ ≡ 9n², discriminant −2985984n⁶ ≠ 0, so good reduction and j = 1728 |
| the descent automorphism | symbolic | (X,Y) ↦ (−X, iY) preserves Y² = X³+4B̄X and squares to (X,−Y) = [−1] |
| **T² = −I with det T = 1 ⇒ non-scalar** | algebra | a scalar square root of −I has determinant −1, so T is non-scalar with eigenvalues ±i in F̄_ℓ, for every odd ℓ including ℓ = 3 |
| **F swaps the eigenlines** | exhaustive, ℓ = 3,5,7,11,13 | for T with T² = −I, det T = 1 and **every** F ∈ GL₂(F_ℓ) with FTF⁻¹ = T⁻¹, the number of lines stable under both is **0** in all five cases |
| transvection | Tate curve at m (or B when ℓ = m), v(Δ) = 1 or 2 not divisible by odd ℓ | argument is the standard one; the unramified quadratic twist in the nonsplit case does not touch inertia |
| **group lemma** | closure, ℓ = 3,5,7,11,13 | ⟨upper, lower transvection⟩ has order 24, 120, 336, 1320, 2184 = \|SL₂(F_ℓ)\| exactly. The prime-field step (powers of one transvection give all u(a)) is used and is flagged in the proof |
| ℓ = A | Mazur's prime-isogeny bound + A > 163 | irreducibility, then the transvection at m ≠ A completes it |
| C1 ⊂ C60 | congruences | m ≡ 491 (mod 840) ⇒ m ≡ 11 (mod 120); 420 \| n ⇒ 60 \| n. And C60 ⇒ m, A, B ≡ 11 (mod 24), so Zywina applies |
| p = 5 data on C60 | m ≡ 1 (mod 5), 5 \| n | reduction y² = x³+4x, #E(F₅) = 8, a₅ = −2: good, ordinary, non-anomalous, E(Q₅)[5] = 0 — confirmed on both members |
| the example | PARI `isprime` (a proof, not a pseudoprime test) | (3491,60): m = 3491, A = 61091, B = 93491 all prime; m ≡ 11 (mod 120) but m ≢ 491 (mod 840), so it is in C60 and not in C1; odd conductor part 3mA²B = 3654225778448609283, against 318222060510286953256323 for (3011,420), ratio 87083.3 |

My first pass at three of these checks was malformed — I substituted for m inside expressions where A and B are themselves defined through m,
which is circular. Corrected in `runs/fixed_reductions.gp`; both runs are kept.

## 3. Assessment of the proof

The argument is correct as written, and the local computation at A is the substantive new step: it replaces "type III, so inertia has
order 4" with an explicit good model over Q_A^{nr}(A^{1/4}), an explicit descent automorphism, and the tame relation F T F⁻¹ = T^A = T⁻¹
using A ≡ 3 (mod 4). That is what makes the local representation absolutely irreducible at **every** odd ℓ ≠ A simultaneously, which a
single Frobenius test at 7 cannot do. The eigenline-swap step is the crux and I verified it exhaustively for the first five odd primes as
well as by the general argument.

Two observations that do not affect the verdict:

1. The theorem gives each mod-ℓ image separately. It says nothing about the adelic image or independence across ℓ, and the proof does not
   claim otherwise.
2. C60 is exactly "Zywina's family ∩ {m ≡ 1 (mod 5), 5 | n}": m ≡ 11 (mod 120) ⟺ m ≡ 11 (mod 24) and m ≡ 1 (mod 5), while 12 | n is
   automatic, so n ≡ 0 (mod 60) adds only 5 | n. The mod-7 conditions in C1 were carrying the old Frobenius irreducibility test and
   nothing else. That is worth stating plainly in the addendum.

## 4. Dependencies I did not re-derive

- Mazur's rational prime-isogeny theorem (used for ℓ = A only). The proof's own source qualification — read in Banwait Thm 1.2 and
  cross-checked in Michaud-Jacobs, original paywalled text not retrieved — should be preserved.
- Tate uniformization and the standard description of ℓ-torsion inertia for multiplicative reduction.
- The Serre–Tate fact that for potentially good reduction the inertia action on prime-to-q torsion factors through Aut of the reduced curve.
- Tao–Ziegler Theorem 1.3 for the C60 infinitude. The shape of the application is the same one already audited for C1: the polynomials
  16(60u)² and 25(60u)² vanish at 0 and are divisible by 120, so the residue class 11 (mod 120) is preserved. I checked that divisibility
  (57600 = 480·120, 90000 = 750·120) but did not re-read the theorem this cycle.
- Tamagawa numbers on C60: both members give the same types and product 16, and the types at 2 and 3 depend only on m mod 24 and 12 | n,
  but I did not write out the Tate-algorithm case analysis for the whole family.

## 5. Proposed author-side addendum (not merged; this review writes nothing shared)

> **Uniform odd-prime residual surjectivity (reviewed).** For every m, n with m, A = m+16n², B = m+25n² prime and ≡ 11 (mod 24) — that is,
> on Zywina's whole parent family — the mod-ℓ Galois image of E: y² = x³ − 5Ax² + 4ABx is GL₂(F_ℓ) for every odd prime ℓ. The proof is
> local: at A the curve acquires good reduction over the tame quartic extension, the inertia matrix satisfies T² = −I with determinant 1,
> and Frobenius inverts it because A ≡ 3 (mod 4), so it exchanges the two eigenlines and no local line is stable; a Tate-curve transvection
> at m (at B when ℓ = m) plus the prime-field lemma then gives SL₂(F_ℓ), and the cyclotomic determinant gives GL₂(F_ℓ). The single
> coefficient prime ℓ = A is handled by Mazur's prime-isogeny bound, since A ≥ 2315 > 163.
>
> Consequently **C1's mod-7 congruences were sufficient but not necessary** for residual surjectivity: they were carrying the old
> Frobenius-at-7 irreducibility test. C1's definition is unchanged. For discussion only, C60 (m ≡ 11 mod 120, n ≡ 0 mod 60, m, A, B prime)
> is the parent family intersected with the p = 5 conditions m ≡ 1 (mod 5) and 5 | n; it contains C1, retains rank 2, the two sections,
> Sha[2^∞] = 0, good ordinary non-anomalous reduction at 5 with a₅ = −2, and prime-to-5 Tamagawa numbers, and is infinite by the same
> Tao–Ziegler application. One member outside C1 is (m,n) = (3491,60).
>
> This is a Galois-image theorem only. It is not a Sha bound, not a class-component bound, not an evaluated arithmetic witness, and not a
> statement about the adelic image. Smaller conductors do not make any degree-24 computation feasible, and the central norm-channel
> obstruction and generic-radical saturation are untouched. The remaining target is unchanged: b ≤ 2 (or an equally sufficient certificate)
> in actual specialization fields.

## 6. Escalation

None. No disputed inference was isolated, so Fable is not called.
