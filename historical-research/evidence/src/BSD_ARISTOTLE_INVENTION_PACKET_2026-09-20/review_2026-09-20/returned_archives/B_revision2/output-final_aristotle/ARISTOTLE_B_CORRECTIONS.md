# Corrections to `ARISTOTLE_B_REPORT.md`

Return code, unchanged: **`ARISTOTLE_NEW_LEMMA_ONLY`.**  Nothing here closes or reduces
finiteness of Ш, the order-9 target, or q = 36.  The corrections below act on the three
errors identified in the review, keep the bad-place corollary and the abstract intersection
lemma, and scope both precisely.  The broad arithmetic no-go claims of the earlier report
are withdrawn and are **not** to be entered on any no-resurrection register.

## 0. What survives, verbatim

* The Tate-algorithm bookkeeping: Kodaira types `I_1*, I_2, I_1, III, I_2` and Tamagawa
  numbers `2, 2, 1, 2, 2` at `2, 3, 2243, 4547, 5843`, reproducing
  `N = 2^3 · 3 · 2243 · 4547^2 · 5843` (`scripts/tate.py`).
* The bad-place cohomology corollary, in the corrected form

  > `p ≥ 5`, `p ∉ {19, 59, 487, 2243, 4547, 5843}` ⟹ `H^1(Q_ℓ, E[p]) = 0` at every bad
  > place `ℓ`,

  whose two ingredients are: the finite reduction quotient `E(Q_ℓ)/E_1(Q_ℓ)`, of order
  `m_ℓ = c_ℓ · #Ẽ_ns(F_ℓ)`, has no `p`-torsion; and the formal group contributes none for
  `p ≠ ℓ`; local duality plus the local Euler characteristic then force the `H^1` to vanish.
  The exclusions `2243, 5843` are the residue characteristics where the formal-group step is
  unavailable; `19, 59, 487, 4547` are the primes dividing some `m_ℓ`.

  *Formal status.*  `RequestProject/SeedBadPlacePrimes.lean` machine-checks exactly the
  divisibility bookkeeping — which primes divide `4, 8, 2242, 9094, 11688`.  The
  elliptic-curve interpretation, local duality and the Euler-characteristic step are written
  mathematics outside that formal theorem.  The file now says so.

* The abstract intersection lemma, as elementary linear algebra — but in the quadratic, not
  the symplectic, setting (§1).

## 1. The pairing is symmetric, not alternating

For odd `p` the local pairing on `H^1(Q_v, E[p])` induced by the Weil pairing together with
the cup product is **symmetric**: the degree-one cup-product sign cancels the alternating
sign of the Weil pairing (Poonen–Rains, §4.1).  The relevant structure on `⨁_v H^1(Q_v,E[p])`
is therefore a quadratic space, and "maximal isotropic" means isotropic for a quadratic form.
The earlier file `SelmerDualityCountermodel.lean` formalized `ω((x,y),(x',y')) = xy' - yx'`;
Lean checks that statement correctly, but it does not model the arithmetic.

**Repair.** `RequestProject/QuadraticSelmerModel.lean` redoes the construction for the split
quadratic form `Q(v) = ∑_i x_i y_i` on `F^{2N}`, isotropy meaning vanishing of `Q`:

* `QuadSelmer.exists_maximal_isotropic_pair_inter` — for every `k ≤ N` there are totally
  isotropic `G, L` of dimension `N` with `dim (G ⊓ L) = k`, where `L` is the fixed product of
  local conditions (one isotropic line per place);
* `QuadSelmer.exists_config_with_known_plane` — the same with a fixed 2-plane inside
  `G ⊓ L`;
* `QuadSelmer.finrank_inter_le` — **the bound that does hold**: in fixed ambient dimension
  `2N`, `dim (G ⊓ L) ≤ N`.

Scope, stated in the file: the axioms "nondegenerate symmetric pairing, two maximal isotropic
subspaces, `N` places" give exactly the bound `N` and nothing sharper.  The unboundedness in
`QuadSelmer.inter_unbounded` comes from letting `N` grow, not from the axioms defeating a
bound in fixed dimension.  The earlier claim that this excludes duality/reciprocity
mechanisms generally is withdrawn.  `SelmerDualityCountermodel.lean` is retained with a
correction notice; its theorems remain valid linear algebra.

## 2. The finite-place model dropped the localization kernel

For a finite set `S` of places containing the bad places, `p` and `∞`, the correct relation
is

    0 → ker(loc_S) → Sel_p(E) → im(loc_S) ⊓ L_S → 0,

so the finite intersection computes the **image** of Selmer; identifying it with Selmer needs
injectivity of `loc_S` (Poonen–Rains, Remark 4.15).  The earlier report placed the
Mordell–Weil plane directly inside the finite intersection, which is not licensed.

**The kernel is visibly nonzero here.** `11 ∤ N`, and the reduction of
`y² = x³ - 22735x² + 106272484x` mod `11` has `14` points (machine-checked:
`LocKer.seed_affine_card_F11`, `LocKer.seed_card_F11`, `LocKer.eleven_not_dvd_seed_card`).
Since `11 ∤ 14` and the formal group of `E/Q_11` is torsion free (`e = 1 < p-1`),
`E(Q_11)[11] = 0`, so the local Kummer image at `11` is 1-dimensional; the bad-place
corollary kills the remaining finite-place contributions.  Hence the finite localization
image has dimension `≤ 1`, while the two retained rational points give
`dim_{F_11} Sel_11(E) ≥ 2`.

**Formalized general form.** `RequestProject/LocalizationKernel.lean`:

* `LocKer.finrank_comap_eq` : for `f : V → W` linear, `L ≤ W`, and `Sel := f⁻¹(L)`,
  `dim Sel = dim ker f + dim (im f ⊓ L)`;
* `LocKer.finrank_ker_pos`, `LocKer.ker_ne_bot` : if `dim Sel ≥ 2` and `dim (im f ⊓ L) ≤ 1`
  then `ker f ≠ 0`.

The arithmetic inputs (`dim Sel_11 ≥ 2` from the rational points; the local dimension counts)
are written mathematics; the counting identity and the mod-11 point count are formal.

## 3. The "transposition principle" is invalid

From `dim Sel_rel = dim Sel_str + 1 + d` one may *not* convert an upper bound into a lower
bound on the dual group.  With `x = y + C`: `x ≤ B ⟺ y ≤ B - C`; an upper bound transfers to
an upper bound, and only a lower bound gives a lower bound.  Recorded formally, with the
statement that the identity alone bounds neither side, in
`RequestProject/RelaxedStrictIdentity.lean` (`RelStr.le_of_le`, `RelStr.le_of_le'`,
`RelStr.lower_from_lower`, `RelStr.no_bound`).

Consequently the earlier report's "exact remaining arrow" is not justified by that identity.
Auxiliary classes can contribute to an upper bound only through an additional orthogonality
or annihilation argument, which the dimension identity does not supply.

## 4. Narrowing of the remaining negative claims

| Earlier claim | Corrected form |
|---|---|
| Duality/reciprocity mechanisms are excluded | In fixed ambient dimension `2N` the bound `dim(G ⊓ L) ≤ N` does hold (`QuadSelmer.finrank_inter_le`); the construction only shows these axioms cannot improve on it. Unboundedness comes from varying `N`. |
| Bad-place vacuity makes bad-reduction geometry useless | It kills only constructions whose output factors through the vanishing groups `H^1(Q_ℓ, E[p])`. |
| Ш is supported on the exceptional prime set | Not established. A nonzero global class may restrict to zero in all those (zero) bad-place groups. |
| `#Sel_p ≥ p²` rules out a Selmer target | It rules out a *constant* cardinality bound only. A uniform dimension bound, or an independently proved `#Sel_p ≤ C·p²`, is untouched. |
| Mordell–Weil plane sits inside the finite local intersection | False as stated; localization has a nonzero kernel at `p = 11` (§2). |

## 5. Status of the endpoint

Unchanged: no bound on `#Ш(E/Q)` below `1089`, no progress on order 9 or on q = 36.  The
retained deliverables are the bad-place corollary (with its formal divisibility core), the
quadratic intersection lemma with its `≤ N` companion bound, the localization-kernel identity
with the mod-11 witness, and the corrected transposition logic.

## 6. Files

| File | Contents | Build |
|---|---|---|
| `RequestProject/SeedBadPlacePrimes.lean` | divisibility core of the bad-place corollary; corrected scope in the docstring | clean, no `sorry` |
| `RequestProject/QuadraticSelmerModel.lean` | quadratic (symmetric) intersection countermodel and the `≤ N` bound | clean, no `sorry` |
| `RequestProject/LocalizationKernel.lean` | localization exact-sequence dimension identity; nonzero kernel criterion; `#Ẽ(F_11) = 14` | clean, no `sorry` |
| `RequestProject/RelaxedStrictIdentity.lean` | corrected transposition logic | clean, no `sorry` |
| `RequestProject/SelmerDualityCountermodel.lean` | superseded symplectic model, retained with a correction notice | clean, no `sorry` |

All theorems use only `propext`, `Classical.choice`, `Quot.sound`.

## 7. Response to the second assessment (returned archives)

The three errors flagged in the first review were corrected before this section was written;
the assessment of the *returned archive* describes the state prior to those corrections.  For
the record, the current state of this project is:

* **Symmetric vs alternating.**  Corrected in §1.  `RequestProject/QuadraticSelmerModel.lean`
  carries out the intersection example for the split *quadratic* form, and
  `SelmerDualityCountermodel.lean` retains only a correction notice on its arithmetic reading.
* **Localization kernel.**  Corrected in §2.  `RequestProject/LocalizationKernel.lean` proves
  `dim f⁻¹(L) = dim ker f + dim(im f ⊓ L)` and, with the machine-checked count
  `#Ẽ(F_11) = 14`, exhibits the nonzero kernel at `p = 11`.
* **Reversed inequality.**  Corrected in §3; `RequestProject/RelaxedStrictIdentity.lean`.

Three further points of the assessment are accepted and recorded here.

**(a) The Iwasawa/control-theorem step.**  The dual Kummer sequence

    0 → Ш(E/Q)[p^∞]^∨ → Sel_{p^∞}(E/Q)^∨ → Z_p^2 → 0

keeps the two Mordell–Weil directions in the object a control theorem produces, so that
object is infinite and a characteristic ideal with unit leading coefficient does not bound it.
The counterexample `X = (Λ/(T))^2` — characteristic ideal `(T^2)`, coinvariants `X/TX ≅ Z_p^2`
infinite — is now formalized in `RequestProject/IwasawaCoinvariants.lean`
(`IwCoinv.TX_eq_bot`, `IwCoinv.instInfiniteQuotient`), together with the abstract form
`IwCoinv.infinite_of_surjective_onto_pair`.  This refutes only the inference "unit leading
coefficient ⟹ bounded coinvariants"; a route through a precise leading-term theorem, primary
finiteness, height nondegeneracy and regulator integrality is untouched, and no claim is made
that a main conjecture is either necessary or sufficient.

**(b) Nothing here is a hopelessness result.**  No claim in this project asserts that the seed
lacks exploitable specificity, that an Euler system or a main conjecture is logically
necessary, or that any mechanism class is closed.  The negative statements retained are the
scoped linear-algebra ones of §1 and §3 and the qualified local corollary of §0; they are not
for any no-resurrection register.  The claims about a universal conductor/discriminant
identity and about the seed's specificity belong to the other archive and are not asserted
here.

**(c) Endpoint, unchanged.**  Neither a further Ш-prime, nor finiteness, nor any comparison of
the real leading term with the regulator is established.  The implication
`(∀ p ≥ 11, Ш(E/Q)[p] = 0) ⟹ #Ш(E/Q) = 9` is a consequence of the retained small-primary
data; its premise contains the outstanding arithmetic problem, and nothing in this project
proves an instance of it.

Files added in this round: `RequestProject/IwasawaCoinvariants.lean`.  All files build with no
`sorry`, on axioms `propext`, `Classical.choice`, `Quot.sound` only.
