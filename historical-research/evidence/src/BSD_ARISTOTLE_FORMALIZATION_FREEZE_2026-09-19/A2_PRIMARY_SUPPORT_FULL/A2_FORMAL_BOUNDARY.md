# A2_FORMAL_BOUNDARY — what the machine-checked A2 theorems do and do not establish

```
PRIMARY SUPPORT / CONTENT / ASSEMBLY = LEAN MACHINE-CHECKED
LEVEL = A2_FULL (+ 3/3 STRETCH)
FIN STATUS = UNCHANGED
FORMULA STATUS = UNCHANGED
#Sha = 9 t^2 is formally checked ONLY as the abstract theorem order_nine_t_sq under its exact hypotheses
```

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced. This package is the support/assembly infrastructure used by WC,
> and the same caveat applies.

## 1. What is machine-checked
The Lean library `PrimarySupport` checks 28 theorems. Each has exactly its frozen type `PrimarySupport.Spec.<Name>`; the frozen
statements are in `source/.../pkg/A2_PRIMARY_SUPPORT/PrimarySupport/Spec.lean`, sha256 `80d452c2…`. Everything is abstract group
theory or elementary number theory, and no elliptic curve appears.

| block | theorems | content |
|---|---|---|
| primary assembly | P1 `primary_zero_of_torsionfree`, P2 `torsion_decomposition`, P3 `assembly`, P4 `assembly_WC_shape`, P5 `finite_iff_local_and_support` | torsion group: finite ⟺ (every primary part finite) ∧ (finitely many nonzero); WC-(3)-shaped assembly |
| finite prime support | J1 `JOf_ideal`, J2 `JOf_ne_zero_iff`, J3 `JOf_generator`, J4 `positive_depth_divides` | J(P,h) is an ideal; it is nonzero ⟺ all h(p) < ∞ and the positive support is finite; generator ∏ p^{h(p)}; positive depth only at p ∣ A |
| lattice content | L1–L7 (`content_dvd_iff`, `content_basic`, `content_unimodular`, `exists_primitive`, `content_padic`, `content_mod_pk`, `content_bounds_J`) | gcd-content divisibility (integral, p-adic, mod p^k with truncation), GLₙ(ℤ)-invariance, primitive factorisation, descent to ℤ |
| Lemma B | B1 `lemmaB_valuation`, B2 `lemmaB_cokernel` | a nonzero integer lies in all local ideals ⟺ finite support ⟺ finite product of local cokernels (exact valuation model) |
| order consequence | H0 `card_eq_prod_primary`, H2 `order_nine_t_sq` | finite G with \|G[2^∞]\| = 1, \|G[3^∞]\| = 9, \|G[5^∞]\| = 1 and square odd-primary orders ⇒ **\|G\| = 9t², gcd(t,30) = 1** |
| countermodels | CM1 `CM_each_local_finite`, CM1′ `CM_finite_support`, CM2 `CM_nonzero_everywhere`, CM3 `CM_profinite_perfectness`, CM4 `CM_order_441` | the false stronger statements are refuted (see §3) |
| stretch | S1 `alternating_square`, S2 `CM_noncyclic_target`, S3 `CM_codex_torsion_example` | square order for a nondegenerate alternating pairing into a **cyclic** ZMod N; the non-cyclic counterexample; Codex's exact torsion example |

## 2. Boundary audit of the seven required points (read against the frozen Spec and the proofs)
1. **`finite_iff_local_and_support` needs BOTH conditions.** `Finite G ↔ (∀ p prime, G[p^∞] finite) ∧ {p | G[p^∞] ≠ ⊥}.Finite`.
   - The proof is `Primary.finite_iff_local_and_support_aux`: (⇒) support ⊆ primeFactors(\|G\|); (⇐) assembly.
   - Neither conjunct suffices alone: CM1 (⨁_p ZMod p) and CM1′ (ℕ →₀ ZMod 2) are proved.
2. **`assembly_WC_shape` keeps exceptional-prime finiteness explicit.** `Primary.finite_of_primary_WC_shape` takes
   `hS0 : ∀ p ∈ S0, p.Prime → G[p^∞] finite` as a hypothesis and uses it for the S0-part of T = (S0 ∪ primeFactors A) ∩ primes.
3. **`JOf_ne_zero_iff` does not manufacture a nonzero J from pointwise data.** Its right side demands all h(p) < ∞ AND a finite
   positive support. CM2 proves that J = {0} although every local witness p² ∈ ZMod(p³) is nonzero.
4. **`content_bounds_J` keeps the comparison hypotheses.** A fixed nonzero lattice vector z, the depth bound
   h(p) ≤ v_p(content z) outside B, and h(p) < ∞ on B are all hypotheses of `Descent.exists_ne_zero_mem_JOf_of_content_bound`.
   Nothing constructs z or the comparison.
5. **`order_nine_t_sq` concludes only `∃ t, #G = 9·t² ∧ Nat.Coprime t 30`**, via H0 and "primary orders are p-powers".
   It never concludes #G = 9.
6. **`CM_order_441` proves that G = (ZMod 3)² × (ZMod 7)² satisfies every hypothesis of H2** (\|G[2^∞]\| = 1, \|G[3^∞]\| = 9,
   \|G[5^∞]\| = 1, and square odd-primary orders 9, 49, 1), and that `Nat.card G = 441`. The lemmas are `primaryPart_G441_*`.
7. **`alternating_square` has target `ZMod N` (cyclic) in its frozen type.**
   - The proof (`Symplectic.isSquare_card`) splits off hyperbolic planes by induction on the order.
   - The false non-cyclic generalisation is REFUTED in the same library: `CM_noncyclic_target`, the cross product on
     (ZMod 2)³, has order 8 and is nondegenerate and alternating.

**No elliptic-curve input is derived internally.** Sha, Selmer groups, Cassels–Tate and Ota appear nowhere in the library.
The square-order and 2/3/5-primary data enter H2 only as hypotheses. The source scan found no axiom, no instance declarations,
and no `set_option`.

## 3. What this does NOT establish
- **Not FIN.** Not "Sha(E/Q) finite" for the seed or any curve.
- **Not #Sha = 9.** H2 is an abstract theorem *under* `[Finite G]` and the square/primary hypotheses. Its conclusion is 9t²,
  and CM4 shows that t = 7 is consistent with all of those hypotheses. "FIN ⇒ #Sha = 9" is NOT proved and is not provable from them.
- **Not J_E ≠ 0**, not a uniform witness-content antecedent, and not uniform prime support for the seed.
  - J2 and L7 are "iff" / "if" statements about abstract depth functions and comparisons. They supply none of their antecedents.
- **Not FORMULA and not BSD.**
- **Not that WC is easier than FIN.** Codex's Theorem O1 (`BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md`)
  shows that on the good ordinary tail, depth-zero witness existence ⟺ primary Sha vanishing.
- **The formalization closes proof-engineering uncertainty only; it does not reduce the arithmetic difficulty.**

## 4. Mismatch with the Codex sources
**None.** The statements follow Codex's FORMALIZABLE_GAPS B3/A3, WITNESS_CONTENT_THEOREM §1/§4 and ALGEBRAIC_REDUCTION_LEMMAS
§B/§H, as packaged and audited before the run.

The only form changes were recorded before the run:
- Lemma B uses the valuation model.
- The square-order input is a hypothesis.
- The abstract Cassels–Tate step is scoped to a cyclic target (discovery D5), because the non-cyclic generalisation is false.
