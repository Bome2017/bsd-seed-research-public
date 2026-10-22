# Frontier: what has and has not been ruled out

## The precise statement (supersedes any wording that suggests "nothing is easier than FIN")

> **We have not yet found a target that is both substantially easier than FIN and still strong
> enough to control the infinite prime tail.**

Many things are easier than FIN: `Ш[p^∞] = 0` for one fixed `p`, producing the receiver `B_p`,
checking a Kolyvagin prime at `p = 53` (done here for `ℓ = 3391`), evaluating one W3
coefficient at one `p`, and the rank-two and twist bookkeeping. The difficulty only appears when
one statement has to handle essentially every prime.

## Candidates eliminated so far (each is about that target only)

| Candidate | What it turned out to be | Where |
|---|---|---|
| Receiver `B_p` | `B_p ≅ Ш[p]` (fixed theorem). A uniform bound on `B_p` is the missing problem | fixed input |
| Coinvariant `h_p` | strict Selmer dimension. `h_p ≤ 2 ⟺ Ш[p] = 0` with parity, and `h_p ≤ 1 ⟺ Ш[p] = 0` when `λ_p = 1` | `REDUCED_TARGET.md`, `Coinvariant/ReducedTarget.lean` |
| Heegner `ν_p` | cofinitely `ν_p = 1 + dim Ш[p]` (given the twist condition), so a cofinite `ν_p ≤ 2` is cofinite `Ш[p] = 0` | `HEEGNER_NU.md`, `Coinvariant/KolyvaginOrder.lean`, `Frontier.nu_collapses` |
| W3 `ℓ₂` | fails at `p = 17` even though `Ш[17] = 0`, so it does not characterize `Ш[p]` | user-supplied; not recomputed here |

None of this shows that an easier intermediate object cannot exist.

## The shape of the wanted intermediate theorem (checked in Lean)

`Coinvariant/Frontier.lean` builds with no `sorry` and uses only the standard axioms. Write
`Z p` for `Ш(E/ℚ)[p] = 0`.

* `cofinite_iff_of_collapse`: if `T p ↔ Z p` for all but finitely many `p`, then a cofinite theorem
  for `T` is exactly a cofinite theorem for `Z`. This is the formal meaning of "collapses to FIN".
* `nu_collapses`: if cofinitely `ν_p = 1 + dim Ш[p]` and `dim Ш[p]` is even, then `ν_p ≤ 2`
  collapses to `Ш[p] = 0`.
* `not_iff_of_false_alarm`: one prime with `Ш[p] = 0` where the target fails shows that the target
  does not characterize `Ш[p]`.
* `finite_of_detector`: a **one-sided** detector is enough. If `Ш[p] ≠ 0 ⇒ D(p)` and only finitely
  many `p` satisfy `D`, then the bad primes are finite. False alarms are allowed.
* `bad_primes_dvd_fixed_integer`: suppose
  1. `Λ_p ≡ I_E · u_p (mod p)` for all primes `p`, with `I_E ∈ ℤ∖{0}` fixed;
  2. `u_p` is a `p`-unit;
  3. **(detection bridge)** `Ш[p] ≠ 0 ⇒ p ∣ Λ_p`.

  Then every prime with `Ш[p] ≠ 0` divides `I_E`, so the bad primes lie in the finite set
  `primeFactors(I_E)`.
* `congruence_without_bridge_insufficient`: hypotheses 1 and 2 alone do not give the conclusion.
  The bridge 3 has to be proved separately for whichever `Λ` is used.

### Two consequences for the `Λ₁, Λ₂` test

1. **The bridge is part of the target.** A cross-prime pattern `Λ_p ≡ I_E u_p` only becomes the
   implication `Ш[p] ≠ 0 ⇒ p ∣ I_E` once `Ш[p] ≠ 0 ⇒ p ∣ Λ_p` is known. That bridge is one-sided:
   it does not need `p ∤ Λ_p ⇒ Ш[p] = 0`. This is why it can be strictly easier than FIN: it never
   has to certify vanishing prime by prime.
2. **The `p = 17` behaviour of `ℓ₂` is not by itself disqualifying.** By `finite_of_detector`, a
   false alarm at `p = 17` just means 17 would have to divide the controlling integer. It does
   show that `ℓ₂` is not a characterization. What would rule `ℓ₂` out as a detector is either
   infinitely many false alarms, no global control of the form `ℓ₂(p) ≡ I'·u_p`, or failure of
   the bridge `Ш[p] ≠ 0 ⇒ p ∣ ℓ₂(p)`. None of these has been established here. The same three
   checks apply to `Λ₁` and `Λ₂`.

## The Q36 route

This route has the same logical shape. It needs a rank-two Gross–Zagier/Kolyvagin/TNC mechanism
that turns the fixed leading term `q ≈ 36` into the bridge "`Ш[p] ≠ 0 ⇒ p` divides a fixed
nonzero integer built from `q`". That bridge is currently missing. Nothing here supplies it or
rules it out.

## Status

* Frontier: **find a global object whose finite arithmetic controls the family `Ш[p]` without
  already being `Ш`.** No such object has been found, and its existence has not been ruled out.
* Not done here: the `Λ₁, Λ₂` cross-prime computation, and the W3 `ℓ₂` recomputation at `p = 17`.
  The W3 evaluator and corpus are not in this project.
