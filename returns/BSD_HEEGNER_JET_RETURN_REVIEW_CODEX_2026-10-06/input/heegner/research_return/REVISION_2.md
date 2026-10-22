# REVISION 2 — Heegner lane, after the 2026-10-06 direction review

This file responds to the direction review of 2026-10-06 for the Heegner lane only (the
receiver, coinvariant and jet lanes are other runs). It records which claims of `PROOF.md`,
`RESULT.md`, `SEED_DELTA.md` and `HANDOFF.md` are withdrawn or narrowed, what was newly
checked, and what is still missing. **FIN, ORDER9 and Q36 are unchanged. No derived Heegner
point was computed. No prime is newly settled.**

Grades as before: **[L]** kernel-checked (`RequestProject/Continuation/TraceCongruence.lean`,
new), **[W]** written proof, **[I]** imported theorem, **[R]** citation supplied by the reviewer
and not re-read in this run, **[C]** exact Python computation (`checks/`).

## 1. Corrections accepted

1. **Domain of Lemma 3 (narrowed).** The residual-dimension statement Lemma 3 relies on is
   attributed by the reviewer to W. Zhang, *Selmer groups and the indivisibility of Heegner
   points*, §8.2, Lemma 8.4 [R]. That lemma carries the paper's standing hypotheses,
   including **good ordinary reduction at `p`** and Hypothesis ♥. I did not have the printed
   text in this run. Lemma 3 is therefore **restricted to good ordinary `p`**, and is
   conditional on matching every standing hypothesis (§3 below does this for `p = 53`, as far
   as the seed data allow). The earlier sentence "covers ordinary and supersingular `p`
   alike" is **withdrawn** for Lemma 3. It remains true for Lemma 2, which is only about
   Frobenius classes. Kim's Theorem 1.1 does not cover the supersingular case here, because
   that case assumes semistability and the seed has additive places at 2 and 4547.
   * Concrete consequence [L]: `a_29 = 0` (`affCount_29`), so `p = 29` is supersingular. The
     earlier coverage list (28 primes) **overstated** the authenticated domain: `29` must be
     removed. All other listed primes are ordinary ([C], `finite_batch_auxiliaries.out.json`,
     key `a_p_of_covered_primes`).
2. **Exact `a_ℓ = 0` is not needed for the trace term (corrected).** `PROOF.md` §5 said the
   choice `a_ℓ = 0` "is exactly what makes Lemma 1 exact". That was wrong in its effect. With
   `M_ℓ = gcd(a_ℓ, ℓ + 1)`, the norm relation `Tr y_ℓ = a_ℓ y_1` gives
   `(σ − 1)D_ℓ y_ℓ = (ℓ + 1)y_ℓ − a_ℓ y_1 ≡ 0 (mod M_ℓ E(H_ℓ))`. This is the standard
   Kolyvagin-prime congruence. It is now kernel-checked in the abstract form
   (`derived_invariance_trace`, `derived_invariance_mod_common`, `derived_invariance_mod_gcd`,
   [L]). One derived point therefore serves every eligible prime factor of `M_ℓ` at once.
   `a_ℓ = 0` only maximizes `M_ℓ` (to `ℓ + 1`).
3. **Coverage obstacle (B) removed for any fixed finite batch.** `RESULT.md` §3(B) said a
   cofinite theorem would need, for every large `p`, an inert `ℓ` with `a_ℓ = 0` and
   `p ∣ ℓ + 1`, and called this open. With correction 2 that requirement is unnecessary.
   [W] Let `M` be any squarefree product of eligible primes (`p ≥ 5`, `p ≠ 23`). Apply
   Chebotarev in `K(E[M])/ℚ` to the conjugacy class of complex conjugation `τ`. It gives
   infinitely many `ℓ ∤ 23NM` with `Frob_ℓ ~ τ`. For each such `ℓ`: `ℓ` is inert in `K`,
   `a_ℓ ≡ tr ρ̄_M(τ) = 0` and `ℓ ≡ det ρ̄_M(τ) = −1 (mod M)`. No independence of the mod-`p`
   images is needed, since `τ` itself lies in the full Galois group. This supplies the
   auxiliary primes for the batch. It does **not** control any derived point. The open
   Lang–Trotter-type question concerns only exact `a_ℓ = 0` with a prescribed large factor, and
   that is no longer on the critical path.
   * Seed instances ([C], with inertness [L]): the earlier table missed `37` and `41`.
     `ℓ = 21089` is inert (`inert_21089` [L]), has `a_ℓ = −74` [C] and
     `M_ℓ = gcd(−74, 21090) = 74 = 2·37` (`common_modulus_21089` [L]). So it is a Kolyvagin
     prime for `37`. For `41`: `ℓ = 100613` (`a_ℓ = 0` [C], just above the earlier `10⁵`
     limit) and `ℓ = 127591` (`a_ℓ = 164 = 4·41` [C]).
   * A warning case [C]: `ℓ = 60679` has `37·41 ∣ ℓ + 1` but `a_ℓ = −74`, so
     `M_ℓ = 74` and `ℓ` serves **only** `37`. When `a_ℓ ≠ 0`, the eligible primes are the
     factors of `M_ℓ`, not of `ℓ + 1`.
4. **Height obstruction (narrowed).** Proposition 4 shows exactly this: the specific test
   `ĥ(P_ℓ)/p² < (minimum positive height on E(H_ℓ))` can never certify indivisibility, because
   the derivative makes the left side at least the minimum. The sentence in `PROOF.md` §4 that
   this "rules out the whole family Gross–Zagier heights + Lehmer/Lang/Silverman minimum", and
   that divisibility is "invisible to archimedean heights", **is withdrawn as stated**. Other
   uses of heights are not excluded: for example, a height bound combined with an
   authenticated Mordell–Weil lattice for `E(H_ℓ)` (saturation), or with a rigorously bounded
   search. No feasible seed-scale version of these is supplied here.
5. **FIN versus ORDER9 (corrected).** `SEED_DELTA.md` §3 said that cofinite vanishing "together
   with the finite remainder" gives "FIN, then ORDER9". Cofinite vanishing of `Sha[p]` plus
   finiteness of the finitely many exceptional primary parts gives **FIN only**. ORDER9 needs,
   in addition, the exact order of each exceptional primary part: trivial for `p ≥ 5`, with the
   record's 2- and 3-primary certificates.
6. **Division of `ℓ + 1` by bad primes.** The reviewer warns that dividing `ℓ + 1` by a squarefree
   product of bad primes is unsafe when those primes occur to higher powers. This lane's
   scripts never do that. They fully factor `ℓ + 1` (and now `M_ℓ`) by trial division and keep
   multiplicities. The warning is recorded for any reuse.

## 2. Reviewer's reduced target for the coinvariant lane (bookkeeping only)

The reviewer derives `h_p = 2 + dim Sha[p] − dim loc_p Sel_p`, with the last term in `{0, 1}`,
and hence, by even parity, `h_p ≤ 2 ⟺ Sha[p] = 0`. The final arithmetic step is checked
(`reduced_target_iff` [L]: `h + t = 2 + s`, `t ≤ 1`, `s` even ⟹ `(h ≤ 2 ↔ s = 0)`). The
identification giving `h_p` is the coinvariant return's and is not re-checked here.

## 3. Theorem-application check at a concrete admissible prime: `p = 53`, `ℓ = 3391`

`p = 53` is the first prime the record has not settled that is relevant to ORDER9.
`ℓ = 3391` is inert (`inert_3391` [L]), with `a_ℓ = 0` [C, independently re-verified by the
reviewer] and `3392 = 2⁶·53` (`residues_mod_53` [L]). The table matches the standing
conditions as far as I can identify them without the printed text. The reviewer should
compare it with Hypothesis ♥ and Lemma 8.4 as printed.

| Condition | Status for `p = 53` | Grade |
|---|---|---|
| `p ≥ 5`, `p ∤ N`, `p ≠ 23` (`p ∤ disc K`), `p ∤ h_K = 3` | holds | arithmetic |
| good **ordinary**: `a_53 = −6 ≢ 0` | holds (`affCount_53`, `ordinary_53`) | [L] |
| `ρ̄_{E,53}` surjective | retained import A.3 (all odd `p`) | [I] |
| `ρ̄` ramified at multiplicative `q ∥ N` (`q = 3, 2243, 5843`) | holds: `v_q(Δ_min) ∈ {2, 1, 2}` (`minimal_discriminant`), and `53 ∤ v_q`; Tate-curve criterion | [L] + [W] |
| primes `q ∥ N` with `q ≡ ±1 (mod 53)` | none: residues `3, 17, 13` (`residues_mod_53`), so this clause is vacuous | [L] |
| additive places `q = 2, 4547` (`q² ∣ N`) | `E(F)[53] = 0` for every finite unramified `F/ℚ_q`: component group of order ≤ 4, `E₀/E₁` an `F_q`-vector group, `E₁` pro-`q`. Local Euler characteristic and self-duality then give `H¹(ℚ_q, E[53]) = 0` | [W] |
| Tamagawa numbers, torsion, Manin constant prime to `53` | `c_q ≤ 4` at the additive places, `c_q ∣ v_q(Δ) ≤ 2` at the multiplicative places, `#E(ℚ)_tors = 2`, `c_E ∣ 2⁹` (record) | [W] + record |
| Heegner hypothesis for `K = ℚ(√−23)` | holds (`SeedFinite`) | [L] |
| `ℓ` a Kolyvagin prime for `53`: inert, `53 ∣ a_ℓ`, `53 ∣ ℓ + 1` | holds | [L] + [C] |

**Whether the N-square-full places are allowed.** I cannot confirm from memory whether the
paper's main setting restricts `N` (for example to squarefree `N`, or to `N` with conditions at
`q² ∣ N`). If it does, the additive places `2³` and `4547²` are outside the printed hypothesis.
The line above shows only that the local cohomology at those places vanishes for `p = 53`. That
is what such conditions are usually designed to guarantee, but a reviewer must make the actual
match. **The theorem application is therefore not authenticated**; this table reduces it to a
finite comparison with the printed text.

**Precise criterion, conditional on that match [W + R].** Write `c(ℓ) ∈ H¹(K, E[53])` for the
genuine Kolyvagin class of `P_3391`. `c(1) = 0`, because `y_K` is torsion of order prime to 53.
So the first nonzero level of the residual Kolyvagin system is `≥ 1`. If `c(3391) ≠ 0`, it
equals 1, and Lemma 8.4 gives the eigenspace dimensions `(2, ≤ 1)`. Since
`rank E(ℚ) = 2`, it follows that `Sha(E/ℚ)[53] = 0`.

**New structural fact about the derived class [W].** By Kolyvagin's local relation between
`∂_ℓ c(nℓ)` and `loc_ℓ c(n)` (as in Gross's exposition; numbering not re-verified),
`∂_ℓ c(ℓ) = φ_ℓ(loc_ℓ c(1)) = 0`. Hence `c(ℓ)` is unramified at `ℓ` as well, so
`c(ℓ) ∈ Sel_53(E/K)`, and, with the sign bookkeeping of `PROOF.md` Lemma 3 step 5 (still to be checked against the
printed convention), it lies in the eigenspace identified with `Sel_53(E/ℚ)`. In
particular, if `Sha[53] = 0` then `c(ℓ) = κ(aP₁ + bP₂)` for some `(a, b) ∈ 𝔽_53²`. An
"independent evaluation identity" for the derived point must therefore take this form: the
derived class written in coordinates against the Kummer classes of `P₁` and `P₂`. This is the
shape of a derived Gross–Zagier/Kolyvagin-type formula. Nothing of that kind is proved here,
and this remark does not bound `Sha`.

## 4. What remains (unchanged in substance)

* An authenticated application of the residual-dimension lemma at `p = 53` (or another
  concrete ordinary admissible `p`). §3 reduces this to a comparison with the printed
  hypotheses.
* Actual arithmetic information on the genuine derived point `P_ℓ` modulo `p`, or an
  independent evaluation identity for `c(ℓ)` in the coordinates of §3. No point was computed.
  Heegner points at level `N ≈ 6.5·10¹⁵` were not attempted.
* For a uniform statement: a mechanism controlling `P_ℓ mod p` for all eligible `p ∣ M_ℓ` and a
  cofinite set of `p`. Correction 3 removes only the auxiliary-prime supply problem.

## 5. Files

* New Lean: `RequestProject/Continuation/TraceCongruence.lean`. It builds, contains no `sorry`
  or `native_decide`, and its axiom audit is in `lean/AXIOM_AUDIT_REVISION_2.txt` (only
  `propext`, `Classical.choice`, `Quot.sound`).
* New computation: `checks/finite_batch_auxiliaries.py` and its output
  `checks/finite_batch_auxiliaries.out.json`.
