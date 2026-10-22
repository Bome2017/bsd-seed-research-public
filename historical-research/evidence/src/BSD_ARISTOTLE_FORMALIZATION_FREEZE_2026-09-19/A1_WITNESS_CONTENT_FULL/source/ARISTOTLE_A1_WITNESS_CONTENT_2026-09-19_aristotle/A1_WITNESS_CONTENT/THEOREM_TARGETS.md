# THEOREM_TARGETS — A1 (all statements frozen in `WitnessContent/Spec.lean`)

Notation used below:
- `I = augIdeal R G` is the augmentation ideal of `MonoidAlgebra R G`, with `R` a commutative ring and `G` a commutative group.
- `gr R G r = I^r / I^(r+1)`.
- `PDvd p j t ⟺ ∃ y, p^j • y = t`.
- `depth p t = sSup {j | PDvd p j t}`.
- `hInf t p = ⨅_{S, t p S ≠ 0} depth p (t p S)`, valued in ℕ∞.
- `vInf p a = v_p(a)`, with value ⊤ when a = 0.
- `JE t P = {a | ∀ p ∈ P, hInf t p ≤ vInf p a}`.
- `primesOutside S0 = {p prime, p ∉ S0}`.

## CORE (required for A1_CORE)

| # | Lean theorem | statement (informal) | source | hint |
|---|---|---|---|---|
| T1 | `lemmaA_comm` | g^e = 1 for all g ∈ G, r ≥ 1, x ∈ I^r ⇒ e•x ∈ I^(r+1) | Codex ALGEBRAIC_REDUCTION_LEMMAS §A; FORMALIZABLE_GAPS A1 | (1) I = R-span of {of g − 1}. (2) With x = of g − 1: (1+x)^e = of(g^e) = 1, so e•x = −Σ_{k≥2} C(e,k)x^k ∈ I². (3) e•I ≤ I², then e•I^r = (e•I)·I^(r−1) ≤ I^(r+1) |
| T2 | `gr_killed_by_exponent` | every y ∈ I^r/I^(r+1) (r ≥ 1) satisfies e•y = 0 | consequence of §A | `Submodule.Quotient.mk_eq_zero`, T1 |
| T5 | `depth_spec` | p prime, p^a • M = 0, t ≠ 0 ⇒ PDvd p (depth t) t ∧ ¬PDvd p (depth t + 1) t ∧ depth t < a | WC §1 ("finite, since p^j M eventually vanishes") | {j \| PDvd p j t} is downward closed and bounded by a − 1 |
| T5b | `zero_infinitely_divisible` | PDvd p j 0 for all j | WC §1 ("Do not assign a finite truncated depth to the zero element") | y = 0 |
| T6 | `hInf_lt_top_iff` | hInf t p < ⊤ ⟺ ∃ S, t p S ≠ 0 | WC §1 (h_p = ∞ iff no nonzero witness) | `iInf_lt_iff`, `ENat.coe_lt_top` |
| T6b | `hInf_le_iff` | p prime, bounded exponent for every S at p ⇒ (hInf t p ≤ d ⟺ ∃ S, ¬PDvd p (d+1) (t p S)) | WC §1–§2 ("Each finite h_p is attained"; "the attaining t is not in pM") | the infimum in ℕ∞ is attained (well-founded); use T5 and T5b |
| T6c | `JE_bounds` | A ≠ 0, A ∈ JE t P ⇒ hInf t p ≤ v_p(A) for all p ∈ P, and hInf t p = 0 when p ∤ A | WC §1 definition of J_E; §2 proof | `padicValInt.eq_zero_of_not_dvd` |
| T7 | `WC_abstract` | **Theorem WC** in abstract witness form: conclusions (1), (2), (3) of WC under the tagged hypotheses | WC §2 (Theorem WC and proof) | (1) from T6c, T6 and the Selmer/5.17 hypotheses; (2) from T6b + Ota 1.5 + "Sha[p] = 0 ⇒ Sha[p^∞] = 0"; (3) primary assembly (torsion ⇒ every x is a finite sum of primary components) |
| T9a | `CM_uniform_denominator` | witnesses p² ∈ ZMod(p³) (images of 1 under n ↦ p²n) are nonzero at every prime, yet J = {0} | WC §4 "Uniform symbol denominators" | depth p (p²) = 2: p² = p²·1, and p³•y = 0 ≠ p²; for a ≠ 0 pick a prime p ∤ a |
| T9b | `CM_nonzero_everywhere` | refutes "nonzero finite witnesses of bounded exponent at every prime ⇒ ∃ A ≠ 0 in J_E" | Codex stop rules 7 and 8; the user's instruction | instantiate with T9a's system |
| T12 | `WC_abstract_nonvacuous` | the hypotheses of T7 are jointly satisfiable with 1 ∈ J_E and a nonzero witness at every good prime | package hygiene (guards against contradictory hypotheses) | Sha = PUnit, W = Unit, M p _ = ZMod p, t = 1, r = 2 |

## FULL (additionally required for A1_FULL)

| # | Lean theorem | statement (informal) | source | hint |
|---|---|---|---|---|
| T3 | `gr_p_primary` | p prime, e > 0, g^e = 1, prime-to-p naturals are units in R ⇒ p^(v_p e) kills I^r/I^(r+1) | WC §1 ("M(p,S) is a finite p-primary module"; only the bounded exponent is used) | e = p^v·u with p ∤ u; u acts invertibly through `algebraMap R (MonoidAlgebra R G)` |
| T4 | `bridge_517` | θ ∈ I^(min r p), r ≥ 2, p ≥ 3 ⇒ θ ∈ I² ∧ (r ≥ 3 ⇒ cls2 θ = 0) | WC §1 ("Ota supplies membership θ_S ∈ I_S²"); §2 ("Ota 5.17 would place θ_S in I_S^{min(corank,p)}, a submodule of I_S³") | `Ideal.pow_le_pow_right`, `dif_pos`, `Submodule.Quotient.mk_eq_zero` |
| T4b | `cls2_zero_iff` | θ ∈ I² ⇒ (cls2 θ = 0 ⟺ θ ∈ I³) | definitional support | as for T4 |
| T8 | `WC_groupRing` | **Theorem WC** with Ota 5.17 in its group-ring form θ_S ∈ I^(min(r_{p^∞}, p)) ⊆ Z_p[G_S] | WC §2, with the Ota input exactly as printed (Thm 5.17) | derive T7's hypotheses: bounded exponent from T3; witness form from T4 (p ≥ 3 because 2 ∈ S0); then apply T7 |
| T10 | `padicInt_units` | p prime, p ∤ u ⇒ (u : ℤ_[p]) is a unit | instantiation: T8's coefficient hypothesis holds for Z_p | `PadicInt.isUnit_iff`, `padicNorm` of a prime-to-p natural is 1 |
| T11 | `units_exponent` | for S ≠ 0, (ZMod S)ˣ has positive order and g^|G| = 1 | instantiation: G_S ≅ (Z/SZ)^× | `pow_card_eq_one'` |

## STRETCH (optional)

| # | Lean theorem | statement | source |
|---|---|---|---|
| S1 | `lemmaA_general` | Lemma A for an arbitrary (non-commutative) group, with I the augmentation ℤ-submodule of ℤ[G] and ℤ-submodule powers | §A ("No commutativity of G is needed") |
| S2 | `gr_finite_Z` | G finite abelian, r ≥ 1 ⇒ I^r/I^(r+1) over ℤ is finite | §A ("the graded quotient is a finite abelian group") |
| S3 | `gr_rational_trivial` | … and ℚ ⊗_ℤ I^r/I^(r+1) = 0 | §A ("its rationalization is zero") |

## Scope decisions (recorded; they do not change any claim)
1. **Lemma A is required in its commutative form (T1)**, because Ota's G_S is abelian and WC uses only that case. The general
   form, which Codex states for any finite group, is S1. This is a scoping choice and not a weakening of any claim: T1 is a
   special case of S1.
2. **Ota 5.17 enters in two forms.**
   - T7 takes the *witness form* ("corank ≥ 3 ⇒ t = 0"), which is the form Codex's proof uses.
   - T8 takes the *group-ring form as printed* ("θ_S ∈ I^(min(r_{p^∞}, p))"), and T4 proves that the group-ring form implies
     the witness form.
3. **M(p,S) = I²/I³ ⊗ Z_p is modelled as `gr (Rp p) (G p S) 2`**, where the abstract commutative ring `Rp p` carries only the
   property "prime-to-p naturals are units". T10 proves that ℤ_[p] has this property. Finiteness of M(p,S) is not needed
   (only bounded exponent is); it is stretch S2 for ℤ-coefficients.
4. **Ota Thm 1.5's condition "θ̃_S ≢ 0 mod p·(I²/I³)" is modelled as `¬ PDvd p 1 (cls2 θ)`**, i.e. the class is not in p·M.
   The base change from Ota's R ⊂ Q to Z_p is recorded in `ASSUMPTIONS.md` as a FORMAL_ASSUMPTION.
5. **Not in this package:**
   - Codex's integral lattice content (FORMALIZABLE_GAPS A3), which is in sibling package A2;
   - the rank-two contraction (FORMALIZABLE_GAPS A2);
   - the FORMULA-side lemmas (Package B: B1, B2, B4);
   - the implication LINE ⇒ WC.
