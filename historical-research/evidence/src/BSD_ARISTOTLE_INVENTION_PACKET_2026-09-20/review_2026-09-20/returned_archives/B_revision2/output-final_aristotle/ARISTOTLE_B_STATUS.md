# Status after the latest review

**Return code, unchanged: `ARISTOTLE_NEW_LEMMA_ONLY`.**

## 1. The review's statement is accepted in full

> No additional `Ш`-prime is controlled, no global order bound is obtained, and no comparison
> proving `q = 36` is established. This neither supplies a demonstrated path to full BSD nor
> proves that such a path is unavailable.

That is exactly the state of this project, before and after this round. Concretely:

* `Ш(E/Q)[p^∞]` remains settled only for `p ∈ {2, 3, 5, 7}` (retained primary inputs, not
  proved here). Nothing in this project settles `p = 11` or any further prime.
* No upper bound on `#Ш(E/Q)`, on `#Ш(E/Q)[n]`, or on `dim_{F_p} Sel_p(E)` for any `p ∉ {2,3,5,7}`
  is proved here; in particular the threshold `#Ш < 1089` is untouched.
* Nothing here compares `L''(E,1)/(2 Ω_E Reg E)` with `36`.
* No claim in this project asserts that any mechanism class is closed, that the seed lacks
  exploitable specificity, or that an Euler system or a main conjecture is logically necessary.
  The negative results that are retained are the scoped linear-algebra ones of
  `ARISTOTLE_B_CORRECTIONS.md` §1 and §3 and the qualified local corollary of its §0. None of
  them is a hopelessness statement and none belongs on a no-resurrection register.

The implication retained from the supplied primary data, `(∀ p ≥ 11, Ш(E/Q)[p] = 0) ⟹ #Ш(E/Q) = 9`,
still has an unproved premise, and no instance of that premise is proved here.

## 2. What was added in this round

One new exact arithmetic fact about the seed curve, with its finite verification machine-checked
in `RequestProject/SeedIrreducibility.lean`.

**Theorem (seed).** `E : y² = x³ - 22735x² + 106272484x` admits no rational isogeny of prime
degree `p` for any prime `p ≥ 5`; equivalently, the `G_Q`-module `E[p]` is irreducible for every
prime `p ≥ 5`.

*Inputs used, both carried as explicit hypotheses in the Lean statement rather than asserted:*

1. Mazur's theorem on rational isogenies of prime degree: a rational `p`-isogeny forces
   `p ∈ {2, 3, 5, 7, 11, 13, 17, 19, 37, 43, 67, 163}`.
2. A Galois-stable line in `E[p]` makes `Frob_ℓ` act with an eigenvalue in `F_p` for every good
   `ℓ ≠ p`, i.e. `x² - a_ℓ x + ℓ` has a root mod `p`.

*Everything else is finite and formal:* the point counts `#Ẽ(F_5) = 8`, `#Ẽ(F_7) = 10`,
`#Ẽ(F_17) = 24`, hence `a_5 = a_7 = -2`, `a_17 = -6`; and for each prime on Mazur's list one of
`x² + 2x + 5`, `x² + 2x + 7`, `x² + 6x + 17` has **no** root modulo it:

| `p` | 5 | 7 | 11 | 13 | 17 | 19 | 37 | 43 | 67 | 163 |
|---|---|---|---|---|---|---|---|---|---|---|
| witness `ℓ` | 17 | 5 | 5 | 7 | 7 | 5 | 7 | 5 | 5 | 5 |

The conclusion is `SeedIrr.IsogenyInput.not_reducible`, proved with no `sorry` on the axioms
`propext`, `Classical.choice`, `Quot.sound`.

Also added, from the same point counts: `#Ẽ(F_11) = 14`, `#Ẽ(F_13) = 18`, and
`SeedIrr.torsion_card_dvd_two`, i.e. any order dividing both divides `gcd(14,18) = 2`. With the
standard injection of torsion into the reduction at an odd good prime and the rational point
`(0,0)`, this reproves `E(Q)_tors = Z/2` from a computation checked inside Lean.

## 3. What that does and does not buy

It **removes a hypothesis, uniformly in `p`**: irreducibility of `E[p]` is a standing assumption
in essentially every statement about `Sel_p(E)` for this seed, and it is now available for all
`p ≥ 5` without further computation and without a prime-by-prime check.

It **does not** control a `Ш`-prime, bound `dim Sel_p(E)`, bound `#Ш`, or touch `q = 36`. It is
an input, not a mechanism, and it is registered as such.

## 4. First remaining unproved arrow

Unchanged from the previous round: for a fixed prime `p ≥ 11`, produce an upper bound on
`dim_{F_p} Sel_p(E)` — equivalently exhibit enough annihilating conditions on the quotient
`Ш(E/Q)[p]` — without assuming finiteness of `Ш`, without a characteristic-zero statement that
loses the finite torsion, and without an unproved exhaustive exceptional-prime set. No argument
in this project reaches that arrow, and no argument here shows that it cannot be reached.
