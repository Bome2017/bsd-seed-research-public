# Review of Aristotle tail-compression run 1

2026-09-22. Returned archive `returned_run1.tar.gz`, sha256
`d4922574de8b1cb89abefd995c37711601d69dc8dbb0eea6738894f3177cf7db`, 19 860 bytes. Lean 4.28.0,
`RequestProject/Main.lean`, 170 lines, **0 occurrences of `sorry`**.

## Recorded verdict

    NEW_LEMMA_ONLY.        ENDPOINT EFFECT: NONE.

Aristotle's own return was `NEW_LEMMA_ONLY`, and it obeyed the wording mandate correctly: it states
explicitly that it did not construct a `p`-free model, that it does **not** claim none exists, that this is
case (iii) of the mandate, and it delimits the class `C` in prose. That part of the gate worked.

## Retained — four items

1. **TWIST_SUPPORT_FINITE.** `Sha(E^{-23}/Q)` is finite by Gross-Zagier-Kolyvagin from the certified analytic
   rank one, so `{p : Sha(E^{-23}/Q)[p] != 0}` is finite. Formalized as `torsionPrimes_finite` /
   `twistSupport_finite` via `p | #A`. Elementary given the finiteness input, and correct.
2. **SEED_ONLY_OFF_FINITE_TWIST_SET.** Conditional on the retained comparison plus the idempotent splitting:
   outside that finite twist-support set, `I_3(p) != F_p <=> Sha(E/Q)[p] != 0`. This is the genuine
   sharpening — the auxiliary twist cannot generate an infinite false-positive tail, so asymptotically the
   unresolved `I_3` condition really is detecting the seed. `seed_only_criterion_off_finite_set`.
3. **FINITE-LANE ASSEMBLY.** Finitely many lanes, each with its own fixed support integer, plus finite-exception
   coverage, give one finite support set. `tail_finite_support_of_covering_lanes`. Fine and elementary; does not
   alter the frontier.
4. **FIXED-INTEGER <=> FINITE-SUPPORT**, retained **as an elementary diagnostic only** — see below.

The comparison is carried as an explicit hypothesis (`TailCompression.Comparison`), never axiomatized. That is
the right structure and worth noting.

## Downgraded — the headline claim

`ARISTOTLE_SUMMARY.md` line 10 and `VERDICT.md` line 44 say a `p`-free model of `I_3` "is not a strictly easier
intermediate object — constructing one *is* proving the lane tail theorem, and conversely", and the summary's
first-arrow paragraph says the arrow "is equivalent to constructing a `p`-free model of `I_3` in class `C`".
**The Lean theorem does not establish that.** What `fixed_integer_iff_finite_seed_support` proves is

    ( ∃ C != 0, ∀ p in lane: ¬I_3(p) => p | C )  <=>  { p in lane : Sha(E/Q)[p] != 0 } is finite

assuming the comparison and finite twist support — i.e. the elementary fact *a set of primes is finite iff its
elements all divide some nonzero integer*. Verified directly against the source:

* **No integral-model object appears in `Main.lean` at all.** Grep for `Fitting`, `determinant`,
  `SelmerComplex`, `IntegralModel`, `tensor`, `⊗` returns exactly one hit, at line 112, and it is inside a
  **docstring**. The formalized content is `ℕ`, `Finset`, `AddCommGroup`, and four abstract predicates
  `Lane`, `I3unit`, `ShaQnz`, `ShaTwnz`. The class `C` never enters Lean.
* So there is no formalized ideal, determinant, Fitting object, Selmer complex, or reduction comparison
  `X ⊗ F_p ≅ I_3(p)` anywhere. **`fixed support integer` is not equivalent to `existence of a p-free integral
  model`** on the strength of what was proved. A model with a suitable nonzero invariant might yield such a
  `C`, but that implication needs arithmetic algebra Aristotle did not supply; and finite support certainly does
  not manufacture a model.

## Effectivity — a second distinction

The converse direction is non-constructive. Its proof is `classical`, then
`set S : Finset ℕ := hseed.toFinset ∪ htw.toFinset`, then `C := ∏ q ∈ S, q`. So it proves **existence of some
`C`** via `Set.Finite.toFinset` and choice. It does **not** produce the explicit, effectively known `C_1` the
task demanded. "Explicit fixed integer" must not be advertised as equivalent to mere finiteness of the lane
support.

## The first unproved arithmetic arrow, restated

Aristotle's wording folds the model into the integer. The correct statement:

> Construct a genuinely `p`-independent arithmetic object `X` with a **proved** specialization/comparison to
> `I_3(p)`, and extract from `X` a nonzero, **effectively known** `C_1` whose prime divisors contain every lane
> failure.

Completely open.

## Grading criterion for run 2

* If it proves another version of "finite support iff some integer contains the bad primes", it has **collided
  with run 1** and gives nothing new.
* If it **constructs or obstructs the specialization map** from a fixed integral object to the `p`-dependent
  `I_3`, it has addressed the real Q1.

Run 2 should be allowed to finish; this review supplies the distinction to grade it by.
