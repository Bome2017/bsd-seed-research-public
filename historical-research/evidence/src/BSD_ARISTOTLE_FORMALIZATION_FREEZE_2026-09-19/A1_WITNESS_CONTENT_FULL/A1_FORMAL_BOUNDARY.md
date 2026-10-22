# A1_FORMAL_BOUNDARY — what the machine-checked A1 theorems do and do not establish

```
A1 WC FINITE-ALGEBRA FORMALIZATION = MACHINE-CHECKED
STATUS = CONDITIONAL
LEVEL = A1_FULL
ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED
FIN STATUS = UNCHANGED
```

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced.

## 1. What is machine-checked
The Lean library `WitnessContent` checks 20 theorems. Each has exactly its frozen type `WitnessContent.Spec.<Name>`; the frozen
statements are in `source/.../A1_WITNESS_CONTENT/WitnessContent/Spec.lean`, sha256 `7ff05537…`.

**Mathematical content.** All of it is abstract algebra; every arithmetic input is a hypothesis:
- **Lemma A** (commutative case, T1). In the general non-commutative ℤ-submodule form it is S1.
- **Graded pieces.** They are killed by the exponent (T2), are `p`-primary of bounded exponent when prime-to-p integers are
  units (T3), and over ℤ they are finite (S2) with rationalisation zero (S3).
- **The bridge (T4).** It turns Ota Thm 5.17's group-ring form `θ ∈ I^{min(r,p)}` into the witness form. T4b gives `cls2`.
- **Depth, h_p and J_E** (T5, T5b, T6, T6b, T6c).
- **Theorem WC** in abstract form (T7) and with Ota 5.17 as printed (T8).
- **Regression countermodels (T9a, T9b)** refute "nonzero witness at every prime ⇒ J_E ≠ 0 / finite support".
- **Non-vacuity (T12).** The hypotheses of T7 are jointly satisfiable.
- **Instantiation checks (T10, T11).** ℤ_[p] satisfies the unit hypothesis, and (ZMod S)ˣ has positive exponent.

## 2. The formal boundary: hypotheses of T7 `WC_abstract` / T8 `WC_groupRing` (unchanged from the frozen Spec)
| hypothesis | tag | status after this run |
|---|---|---|
| `A ≠ 0 ∧ A ∈ J_E` | NOT_PART_OF_THIS_TASK (the open antecedent) | **NOT PROVED** — an explicit hypothesis |
| Ota Thm 5.17: `θ_S ∈ I^{min(r_{p^∞},p)}` (T8), or its witness form (T7) | IMPORTED_ARITHMETIC_THEOREM | a hypothesis, never discharged |
| Ota Thm 1.5: witness ∉ p·M ⇒ Sha[p] = 0 | IMPORTED_ARITHMETIC_THEOREM | a hypothesis |
| Selmer: infinite Sha[p^∞] ⇒ corank ≥ 3; corank ≥ 2 | IMPORTED_ARITHMETIC_THEOREM | hypotheses |
| Sha torsion | IMPORTED_ARITHMETIC_THEOREM | a hypothesis |
| finiteness of the primary groups at S0 | NOT_PART_OF_THIS_TASK | a hypothesis of conclusion (3) only |
| 2 ∈ S0; G_S has exponent e > 0; prime-to-p integers are units in `Rp p`; bounded p-power exponent (T7) | FORMAL_ASSUMPTION | the last three are discharged in-package for the concrete model (T3, T10, T11) |

**Conclusions** (for every p ∈ P = primes ∉ S0):
1. Sha[p^∞] is finite.
2. Sha[p^∞] = 0 when p ∤ A.
3. Sha is finite, *if* the primary groups at S0 are finite.

## 3. What this does NOT establish
- **Not FIN.** Sha(E/Q) is not shown finite for the seed or for any curve.
- **Not J_E ≠ 0**, and no nonzero integer in J_E is constructed.
- **Not uniform prime support** for the seed.
- **Not that WC's antecedent is easier than FIN.** The handoff's Q0 kill gate asked whether, on the good ordinary tail, the
  antecedent is FIN in Ota coordinates.
  - Codex has since answered it (`~/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md`, Theorem O1,
    sha256 `7a5ac582f42c8f7c…`; a written deduction from Kim Thm 1.10 and Castella–Sano Thm B with the seed hypotheses checked;
    not Lean-checked).
  - O1 says: at every good ordinary p ∉ S0, h_p = 0 ⟺ Sha[p^∞] = 0.
  - So on that tail the WC depth-zero condition is primary Sha vanishing restated. This formalization removes
    proof-engineering uncertainty only; it does not reduce the arithmetic difficulty.
  - The positive-depth transfer for the exact Ota-admissible set, and the supersingular primes, are not covered by O1.
- **Not the arithmetic facts themselves:** not Ota's theorems, not the Selmer facts, not the Ota hypotheses at the seed's primes.
- **Not the modelling identifications**, which are documented only:
  - the base change R ⊂ Q → Z_p;
  - p-integrality of θ_S;
  - G_S ≅ (ZMod S)ˣ;
  - the Ota S-class nuance D1.

## 4. Proof architecture as verified by reading `WC.lean` / `Primary.lean` / `Depth.lean`
**(1) Finite primary part.**
- From `A ≠ 0 ∧ A ∈ J_E`, `JE_bounds_aux` gives `hInf ≤ v_p(A) < ⊤`, so `hInf_lt_top_iff_aux` gives a nonzero witness t(p,S).
- If Sha[p^∞] were infinite, the Selmer hypothesis gives `r p ≥ 3`, and then the Ota-5.17 witness form gives t(p,S) = 0.
  This is a contradiction.
- Uses only the finite-support-free statement h_p < ∞ at the single prime p.

**(2) Zero primary part.**
- If `p ∤ A` then `hInf = 0`.
- `hInf_le_iff_aux` with d = 0, using the bounded exponent, gives a witness with `¬PDvd p 1`.
- Ota 1.5 gives Sha[p] = 0, and `primaryPart_eq_bot_of_ptorsion_trivial` (induction on k) gives Sha[p^∞] = 0.

**(3) Finite-support assembly.**
- T := (S0 ∩ primes) ∪ primeFactors(|A|). This is finite because A ≠ 0.
- The primary parts on T are finite: for p ∈ S0 by the explicit exceptional hypothesis, otherwise by (1).
- Each x ∈ Sha is torsion (hypothesis). It decomposes over the prime factors of its order (`exists_primary_decomposition`,
  via `Submodule.iSup_torsionBy_eq_torsionBy_prod`).
- Components at primes outside T vanish by (2).
- So Sha is covered by the finite product of the finite parts on T (`finite_of_covered_by_primary`).
- **The finite support comes from the prime factors of the fixed nonzero integer A.** It never comes from "a nonzero witness
  at every prime", and that false inference is refuted by T9a/T9b in the same library.
- Exceptional-prime finiteness is used only at p ∈ S0, and only inside conclusion (3).

**T8 → T7.**
- Bounded exponent comes from T3.
- The witness form of 5.17 comes from T4. It needs `p ≥ 3`, derived from `2 ∈ S0` and p prime.
- Everything else is passed through unchanged.

## 5. Mismatch with Codex's WC theorem (WITNESS_CONTENT_THEOREM.md §2)
**None in logical content.** Conclusions (1), (2), (3) and the proof steps match Codex's §2 proof one-to-one.

Formal differences, all recorded in the original package before the run:
- T7 takes Ota 5.17 in witness form, and T8 takes the printed form plus the proved bridge T4.
- "M(p,S) finite p-primary" is used only through "bounded exponent". Finiteness over ℤ is S2.
- The admissible family is an abstract index type. On the arithmetic side (provenance, not formalization), note D1:
  - Codex's family matches Ota's Thm 1.5 (introduction);
  - Ota's body Thm 6.4 as printed assumes the stricter S-class of Thm 6.1.
  - Under the stricter class J_E can only shrink, and the formal implication is unchanged.
