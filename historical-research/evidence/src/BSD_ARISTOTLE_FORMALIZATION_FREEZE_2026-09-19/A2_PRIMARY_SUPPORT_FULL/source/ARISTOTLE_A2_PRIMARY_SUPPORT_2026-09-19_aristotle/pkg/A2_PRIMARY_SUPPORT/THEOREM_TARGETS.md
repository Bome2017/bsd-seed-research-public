# THEOREM_TARGETS — A2 (all statements frozen in `PrimarySupport/Spec.lean`)

Notation used below:
- `primaryPart G p = {x | ∃ k, p^k • x = 0}`.
- `vInf p a = v_p(a)`, with v_p(0) = ⊤.
- `JOf P h = {a : ℤ | ∀ p ∈ P, h p ≤ vInf p a}`.
- `posSupport P h = {p ∈ P | h p ≠ 0}`.
- `content z = gcd` of the coordinates of z ∈ ℤⁿ (normalized, ≥ 0).
- `reduceMod m z` = z mod m.

## CORE (required for A2_CORE)
| # | Lean theorem | statement (informal) | source | hint |
|---|---|---|---|---|
| P1 | `primary_zero_of_torsionfree` | p prime, no p-torsion ⇒ G[p^∞] = 0 | WC §2 proof of (2) | induction on k |
| P2 | `torsion_decomposition` | in a torsion group every x is a finite sum of elements of primary parts (over primes) | standard (Codex: "Sha is a torsion group, thus the direct sum of its primary groups") | if n•x = 0, write 1 = Σ_q u_q·(n/q^{v_q n}) (Bezout / CRT) |
| P3 | `assembly` | torsion ∧ (p ∉ T ⇒ G[p^∞] = 0) ∧ (p ∈ T ⇒ G[p^∞] finite) ⇒ G finite | FORMALIZABLE_GAPS B3 | image of ∏_{p∈T} G[p^∞] under the sum map |
| P4 | `assembly_WC_shape` | the WC (3) shape: zero at good p ∤ A, finite at good p, finite on S0 ⇒ finite | WC §2 (3) | P3 with T = S0 ∪ primeFactors(A) |
| J1 | `JOf_ideal` | J(P,h) is an ideal of ℤ (P ⊆ primes) | WC §1 | v_p(a+b) ≥ min, v_p(ca) ≥ v_p(a) |
| J2 | `JOf_ne_zero_iff` | J(P,h) ≠ 0 ⟺ every h p < ⊤ and posSupport is finite | WC §1 ("nonzero exactly when…") | (⇐) take a = ∏ p^{h p} |
| J4 | `positive_depth_divides` | A ≠ 0, A ∈ J ⇒ positive depth only at p ∣ A; finite support; h p < ⊤ | WC §1–§2 | v_p(A) ≥ 1 ⇒ p ∣ A |
| L1 | `content_dvd_iff` | z ∈ m·ℤⁿ ⟺ m ∣ content z | FORMALIZABLE_GAPS A3 | `Finset.dvd_gcd_iff`; handle m = 0 separately |
| L5 | `content_padic` | z ≠ 0: z ∈ p^j ℤⁿ ⟺ j ≤ v_p(content z) | FORMALIZABLE_GAPS A3 | L1 + `padicValInt_dvd_iff` |
| CM1 | `CM_each_local_finite` | ⨁_p ZMod p: torsion, every primary part finite, infinitely many nonzero, infinite | WC §4 (profinite example, torsion form); required separation | the primary part at p is the p-coordinate |
| CM1′ | `CM_finite_support` | ℕ →₀ ZMod 2: torsion, finite prime support {2}, infinite | required separation | odd p acts invertibly |
| CM2 | `CM_nonzero_everywhere` | p² ∈ ZMod(p³) is nonzero and divisible by p at every prime; the constant depth 2 gives J = {0} | WC §4; stop rules 7 and 8 | for a ≠ 0 pick a prime p ∤ a |
| CM3 | `CM_profinite_perfectness` | v = 0 at {2, 5}, else 2: every local cokernel finite, the product infinite, and no nonzero integer in every local ideal | WC §4 "Finite generation over the profinite integers" | Lemma B |

## FULL (additionally required for A2_FULL)
| # | Lean theorem | statement | source |
|---|---|---|---|
| P5 | `finite_iff_local_and_support` | torsion G: finite ⟺ (every primary part finite) ∧ (finitely many nonzero) | exact separation (user requirement) |
| J3 | `JOf_generator` | J(P,h) = (∏_{posSupport} p^{h p}) when finite | WC §1 ("its positive generator is the finite product of p^h_p") |
| L2 | `content_basic` | content ≥ 0; content = 0 ⟺ z = 0 | A3 |
| L3 | `content_unimodular` | content(U z) = content z for det U a unit | A3 ("c is independent of unimodular basis change") |
| L4 | `exists_primitive` | z ≠ 0 ⇒ z = content(z)·z₀ with content z₀ = 1 | WC §4 ("Smith normal form gives z = c z₀ with z₀ primitive") |
| L6 | `content_mod_pk` | reduceMod p^k z ∈ p^j·(ZMod p^k)ⁿ ⟺ p^{min j k} ∣ content z | A3 ("finite algebra version over Z/p^k … truncation cases treated explicitly") |
| L7 | `content_bounds_J` | depth ≤ v_p(content z) outside a finite B, and finite on B ⇒ ∃ A ≠ 0 in J | WC §4 "Descent to Z with a primitive comparison" |
| B1 | `lemmaB_valuation` | ∃ A ≠ 0 with p^{v p} ∣ A ∀p ⟺ finitely many v p ≠ 0 | ALGEBRAIC_REDUCTION_LEMMAS §B (1)⟺(2) |
| B2 | `lemmaB_cokernel` | ∏_p ZMod(p^{v p}) finite ⟺ finitely many v p ≠ 0 | §B (1)⟺(3) |
| H0 | `card_eq_prod_primary` | a finite abelian group has order ∏_{p ∣ \|G\|} \|G[p^∞]\| | standard; needed for H2 |
| H2 | `order_nine_t_sq` | \|G[2^∞]\| = 1, \|G[3^∞]\| = 9, \|G[5^∞]\| = 1, odd primary orders squares ⇒ \|G\| = 9t², gcd(t, 30) = 1 | ALGEBRAIC_REDUCTION_LEMMAS §H |
| CM4 | `CM_order_441` | (ZMod 3)² × (ZMod 7)² satisfies H2's hypotheses and has order 441 | §H countermodel |

## STRETCH (optional)
| # | Lean theorem | statement | source |
|---|---|---|---|
| S1 | `alternating_square` | a finite abelian group with a nondegenerate alternating pairing into a CYCLIC group ZMod N has square order | §H ("the alternating Cassels–Tate pairing makes the odd-primary orders squares"), in abstract form |
| S2 | `CM_noncyclic_target` | trap: with target (ZMod 2)³, the cross product gives a nondegenerate alternating pairing on a group of order 8 | package hygiene: shows why S1 needs a cyclic target |
| S3 | `CM_codex_torsion_example` | Codex's exact example ⨁_{p≠2,5}(ZMod p)² | WC §4 |

## Scope decisions (recorded; they do not change any claim)
1. **Lemma B in the valuation model.** Codex states it for d ∈ ∏_p Z_p. Since d_p Z_p = p^{v_p(d_p)} Z_p for d_p ≠ 0, each of the
   four equivalent conditions depends only on v = (v_p(d_p)). The model is therefore exact for (1)–(3), and (4) is not
   separately formalized. Genuine ℤ_[p] is not required.
2. **H2 takes "odd-primary orders are squares" as a hypothesis**, which is the IMPORTED Cassels–Tate input. Its abstract
   group-theoretic source (S1) is stretch. The countermodel CM4 is required because it is what kills "FIN ⇒ #Sha = 9".
3. **Codex's torsion countermodel** ⨁(ZMod p)² with its pairings is stretch S3. The simpler CM1 (⨁ ZMod p) already
   separates the two conditions.
4. **Not here:**
   - the WC implication, Lemma A and the depth/witness layer (package A1);
   - the FORMULA-side B1/B2/B4 of Codex's proposal;
   - the rank-two contraction.
