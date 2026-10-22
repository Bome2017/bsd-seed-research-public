# STAGE II — audit of the prior ordinary-bridge runs and of the saturation-defect bound

Opened only after `AUDIT_STAGE_I.md` was written and committed (gate K0 respected: the Stage I
verdict was frozen in commit `Stage I hostile audit …` before `STAGE_II_ONLY/` was read).

    STAGE_II  = PRIOR_BOUND_CONFIRMED
                (the saturation-defect bound is justified in its exponent form; the
                 order-times-torsion form is a correct but slack consequence; the torsion factor
                 is vacuous on this curve; the shared "equivalently" is an error, as the
                 reconciliation says, and I give an explicit counterexample to the converse)

    CHANGED_STAGE_I_AFTER_READING_STAGE_II = no

    ADDITIONAL FINDING (not in either run nor in the reconciliation):
        the resulting bridge statement is TRUE-BUT-INEFFECTIVE.  Its side condition
        `p ∤ #Ш(E^{-7}/Q)` cannot at present be verified at ANY single prime (Stage I), so
        "the bridge closes for all but finitely many admissible p" currently does not license
        the conclusion at one named prime.  The finiteness of the exceptional set comes from
        finiteness of `Ш`, i.e. from an existence statement, and nothing in the record makes it
        explicit.

## 1. Is `A₂ ≤ v_p(exp Ш(E^{-7}/Q)[p^∞])` justified?  Yes — and I checked the dangerous step

Reconstructed argument (run B's form; run A's is the same argument with the exponent replaced
by the order):

1. Finite-layer Lemma 3.1: `⟨x, y⟩_{1,n} = 0` for `x, y` in the same `τ`-eigenspace of
   `Sel_{p^n}(E/K)`, `p` odd. **Accepted** — both runs re-derive it off the Chapter-3
   finiteness assumption, which is the right move; I could not re-read the source here.
2. `Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^{-7}/Q)` (odd-`p` twist decomposition), so the minus part is
   killed by `p^c`, `p^c` the exponent of `Ш(E^{-7}/Q)[p^∞]` (for `p ≥ 5` the Mordell–Weil
   contribution is trivial, since `E^{-7}(Q)_tors ≅ Z/2` — re-verified independently in Stage I,
   `TwistSha.torsion_divides_two`).
3. For `z = x + y` with `x ∈ Sel^+`, `y ∈ Sel^-`: `⟨p^c z, z'⟩_{1,n} = ⟨p^c x, y'⟩ + ⟨p^c y, x'⟩
   = ⟨x, p^c y'⟩ + 0 = 0`. So `p^c · Sel_{p^n}(E/K)` lies in the null space of `⟨,⟩_{1,n}`.
   (Run B writes this out only for `s ∈ Sel^+`; the minus case is trivial because `p^c` kills
   `Sel^-` outright. The gap is cosmetic.)
4. **The step that could have sunk it, and does not.** The null space of the *limit* pairing
   `⟨⟨,⟩⟩_1` is the **saturated** module `S̄^{(2)}`, not `S^{(2)}`; had the argument been run
   directly in the limit it would have produced `p^c S ⊆ S̄^{(2)}`, which says **nothing** about
   the index `[S̄^{(2)} : S^{(2)}]` and would have been worthless. Both runs instead argue at
   finite level, where `Sel_n^{(2)}` *is* the null space, and then take limits:
   `p^c S ⊆ lim_n (p^c Sel_n) ⊆ lim_n Sel_n^{(2)} = S^{(2)}` (inverse limits are left exact).
   This is the one place where the bound is fragile and both runs are on the right side of it.
   Residual source-dependency I could not discharge here: that `Def. 2.15/2.16` really defines
   `S^{(k)} = lim_n Sel_n^{(k)}` with the transition maps respecting the filtration.
5. Then, since `S̄^{(2)} ⊆ S`, the inclusion `p^c S ⊆ S^{(2)}` kills `S̄^{(2)}/S^{(2)}`, i.e.
   `A₂ ≤ c`. **Valid.**

**Verdict on the two forms.**

* Run B: `A₂ ≤ c` with `p^c = exp Ш(E^{-7}/Q)[p^∞]` — this is exactly what the argument gives.
  Justified.
* Run A: `A₂ ≤ v_p(#Ш(E^{-7}/Q) · #E^{-7}(Q)_tors)` — correct, since
  `exp | #` and the extra factor only weakens it. Not overstated; merely slack.
* The torsion factor is **vacuous here**, for the reason the reconciliation gives, and I confirm
  it by an independent route: `gcd(#E(F_5), #E(F_11), #E(F_13), #E(F_17)) = 2`
  (`TwistSha.torsion_divides_two`), so `#E^{-7}(Q)_tors = 2` and no `p ≥ 5` divides it.
* Consequently the two bounds have the same support, `{p : p | #Ш(E^{-7}/Q)}`, as claimed.

**Scope caveat the runs do not state.** `A₂ = 0` is the relevant condition only because, in the
configuration forced here (`ρ_p = 4`, `rank S = 2`, `d_1 = 0`, `d_2 = 2`), the derived regulator
is the determinant of `⟨⟨,⟩⟩_2` on `S̄^{(2)} = S` alone. In any other filtration configuration
one needs `A_k = 0` for every `k` with `d_k > 0`, and the bound above only controls `k = 2`.
The claim as stated is therefore configuration-dependent, and the configuration is itself
conditional on `[c_2] ≠ 0`.

## 2. "`v_p(R_der) ≥ 0`, equivalently `A₂ = 0`" — adjudicated

The reconciliation's demotion is **upheld**, and it is stronger than "not proved": the converse
is false as linear algebra, so no repair of the argument can recover an equivalence.

* *Sufficiency* is sound. Thm 2.18(5) makes `p^{A₂}⟨⟨,⟩⟩_2` integral; with `A₂ = 0` the Gram
  matrix of `⟨⟨,⟩⟩_2` in a `Z_p`-basis of the saturated (hence free, direct-summand) module
  `S̄^{(2)}` has entries in `Z_p`, so its determinant lies in `Z_p`.
* *Necessity* fails. A symmetric `2 × 2` matrix all of whose entries have valuation `-1` can
  have unit determinant. Explicit witness, machine-checked in Lean:
  `defectGram = !![1/5, 2/5; 2/5, 29/5]`, symmetric (`TwistSha.defectGram_symm`), every entry of
  denominator `5` (`TwistSha.defectGram_entries_nonintegral`), determinant `1`
  (`TwistSha.defectGram_det_unit`). So `v_p(R_der) ≥ 0` is compatible with `A₂ = 1`; the word
  "equivalently" in both runs is an error, not shorthand, and `A₂ = 0` must be recorded as a
  **sufficient structural criterion** only.
* Note the asymmetry this creates: at a prime with `p | #Ш(E^{-7}/Q)` the runs' scenario
  `v_p(R_der) = -B < 0` is *consistent* with everything BD prove, but it is not forced either;
  BD Thm 2.23 plus `Ш(E/K)[p^∞]^- ≠ 0` does force `v_p(R_der) < 0` there. That is the only place
  the equivalence direction is actually available, and it is available for the trivial reason
  that the conclusion is known independently.

## 3. Is the exceptional set the right one?

Yes as a set, with two corrections of emphasis.

* **Correct.** `{p : p | #Ш(E^{-7}/Q)}` (intersected with the admissible lane) is exactly where
  the argument stops, and run B is right that at such `p` the target `Ш(E/K)[p^∞] = 0` is
  **false**, not merely unproved.
* **Correction 1 — effectivity.** The ledger rows read as though the exceptional set were merely
  unlisted. Stage I establishes something sharper: with present theory it is **not listable**.
  No prime `p ≥ 5` is currently proved to lie outside it (Stage I §5), because the only routes
  to `p ∤ #Ш(E^{-7}/Q)` at analytic rank zero (Kato; Kobayashi at supersingular `p`) consume the
  *exact rational* `L(E^{-7},1)/Ω`, and the package certifies only a real interval, which — as
  proved in `TwistSha.certified_interval_does_not_pin_valuation` — fails to determine
  `v_p(L/Ω)` at any prime. So `ORDINARY_VANISHING_OFF_TWIST_SHA` is conditional on `[c_2] ≠ 0`
  **and** on an arithmetic input that is presently unavailable at every prime, not just on
  `[c_2] ≠ 0` with a small unknown finite exclusion.
* **Correction 2 — the good news, stated without using the prediction.** All three primes at
  which Stage I finds the twist-`Ш` question *structurally* out of reach (`7` additive and
  dividing `disc K`; `4547` additive; `5843` split multiplicative, exceptional zero) are already
  outside the admissible ordinary lane: `conductor(E^{-7}) = 49N` with `gcd(7,N) = 1` gives
  `N = 2³·3·2243·4547²·5843`, so `4547` and `5843` are bad for the seed, and BLV Hypothesis 1.1
  excludes `p | 7N` anyway. Therefore:

      IF the exact rational L(E^{-7},1)/Ω is certified and its numerator's prime divisors ≥ 5
      are all bad-or-additive primes of E^{-7}, THEN Kato (good ordinary) and Kobayashi (good
      supersingular) — whose remaining hypotheses are all verified in Stage I: ρ̄_p irreducible
      for every p ≥ 5, p ∤ #tors, p ∤ ∏c_v — give Ш(E^{-7}/Q)[p^∞] = 0 at every admissible p,
      and the bridge's exceptional set is EMPTY.

  This is a conditional roadmap, labelled as such. It is *not* the prediction: it does not
  assert what the numerator is, and it becomes a theorem only when the exactness certificate
  of Stage I §5 exists.

## 4. Do my Stage I findings change the exceptional set?

**Unchanged.** I proved nothing about `#Ш(E^{-7}/Q)`, in either direction, so I cannot shrink
`{p : p | #Ш(E^{-7}/Q)}`; and since that set is defined by the true order, my findings cannot
enlarge it either. What changes is its *epistemic status* (Correction 1) and the *route* to
emptying it (Correction 2).

Two smaller inputs Stage I contributes to the prior ledger:

* BLV Hypothesis 1.1 asks for `ρ̄_{E,p}` surjective. For the twist I proved `ρ̄_p` **irreducible
  for every `p ≥ 5`** and **surjective for `5 ≤ p ≤ 37`**, with explicit Frobenius certificates;
  since `ρ̄_{E^{-7},p} ≅ ρ̄_{E,p} ⊗ χ_{-7}`, both properties transfer to the seed for `p ≥ 5`:
  twisting by a character preserves irreducibility and does not change the projective image, and
  `det(ρ̄ ⊗ χ) = χ² · det(ρ̄) = det(ρ̄)` because `χ` is quadratic, so "contains `SL₂` and has
  surjective determinant" is twist-invariant. So the "non-Eisenstein / surjective" row of
  the hypothesis list is discharged unconditionally on this curve, and the ordinary **Eisenstein
  case** never arises — a hypothesis the prior runs carried but nobody had checked.
* The anomalous exclusion (`a_p = ±1`) is **vacuous on this curve**: `E^{-7}` has a rational
  `2`-torsion point `(0,0)`, so `#E^{-7}(F_p)` is even and `a_p(E^{-7}) ≡ p+1 ≡ 0 (mod 2)` at
  every odd good prime; and `a_p(E) = χ_{-7}(p)·a_p(E^{-7})` for `p ∤ 7`, so the seed's `a_p` is
  even too. Hence `a_p = ±1` is impossible at every odd good prime, for both curves. The
  reconciliation's table lists the anomalous primes as a possibly infinite excluded set
  ("conjecturally infinite, Lang–Trotter, none below 30000 here"). For this curve the set is
  **provably empty**, not merely empirically empty below 30000. That removes one of the two
  infinite sets the reconciliation says separate the result from `FIN` — the supersingular set
  (interface A3) remains, and it is genuinely infinite by Elkies.

That last point is the one place where Stage II work strictly improves the prior ledger.

## 5. Residual disagreements with the prior record

1. `FREEZE.md` §2 says run A's extra torsion factor is vacuous "by Mazur the only primes that
   could ever appear in torsion are `2, 3, 5`". Mazur's torsion theorem allows `p`-torsion for
   `p ∈ {2,3,5,7}` (`Z/7` occurs). The conclusion is right here because the torsion is exactly
   `Z/2`, but the reason as stated is wrong.
2. `BSD_QUOTIENT_PREDICTION.txt` selects the period normalisation by requiring the quotient to
   be a perfect square. That is BSD-circular (Stage I §1); the defensible reason is `Δ > 0 ⇒
   E(R)` has two components `⇒ Ω = ∫_{E(R)}|ω| = 2·ω₁`, which I verified by an independent AGM
   computation.
3. The reconciliation's §5 route 2 ("Kato + Skinner–Urban for good ordinary non-Eisenstein `p`")
   is the right route but misidentifies the blocker as the Eisenstein case and the missing
   Tamagawa data. On this curve there is no Eisenstein prime `≥ 5` and the Tamagawa product is
   irrelevant at `p ≥ 5` (it is `{2,3}`-smooth by Kodaira type alone). The blocker is the exact
   algebraic `L`-value; Skinner–Urban is in any case the wrong divisibility for a vanishing
   statement, and its squarefree-conductor-type hypotheses are not met here (`N` is not
   squarefree).

## 6. Ledger after this audit

    PRIOR_BOUND (exponent form, run B)        = CONFIRMED (argument reconstructed and checked;
                                                 the finite-level vs. limit hazard is handled)
    PRIOR_BOUND (order·torsion form, run A)   = CORRECT BUT SLACK; torsion factor vacuous here
    "A₂ = 0 equivalently v_p(R_der) ≥ 0"      = ERROR; sufficient only (explicit counterexample)
    A₂-only control                           = configuration-dependent (needs A_k = 0 for all
                                                 k with d_k > 0; here only k = 2 occurs)
    EXCEPTIONAL SET {p | #Ш(E^{-7}/Q)}        = correct, and currently NOT LISTABLE
    ANOMALOUS EXCLUSION                       = provably empty for this curve (a_p always even)
    EISENSTEIN EXCLUSION                      = provably empty for this curve (p ≥ 5)
    ORDINARY_VANISHING_OFF_TWIST_SHA          = conditional on [c_2] ≠ 0 AND on an input no
                                                 present theorem supplies at any prime
