# Bounded review: central involution, lower-degree obstruction, external fields (2026-09-17)

Verdict: **CENTRAL_INVOLUTION_STRENGTHENING_VERIFIED**.

Inputs, all under `src/` (bundle `C1_NORM_INDEPENDENT_REVIEW_2026-09-17.zip`, sha256
65dba1e1c59354174c5daffc4162cf01d5cfd1f924b1b693fa7b151cc09fc34c; its `SHA256SUMS.txt` verifies all entries):
`PROOF_CENTRAL_INVOLUTION.md`, `PROPOSED_ADDENDUM.md`, `verify_central_obstruction.py`, `INDEPENDENT_RECEIPT.json`,
`OPUS_BOUNDED_REVIEW.md`, and the retained input archive `C1_ULTRA_PARALLEL_NORM_RELATIONS_001/`.

This work is in a **new private directory**. No shared file, ledger, seal or memory entry was changed; the addendum below is a
proposal, not a merge. No number field, class group, Selmer group or Sha order was computed. The 43-composition solve, the subgroup-lattice
enumeration of GL_2(F_5), the generic-radical analysis and any PARI certification were not rerun, as instructed.

## 1. Their checker

`verify_central_obstruction.py` runs here in 0.12 CPU-seconds and its receipt matches the supplied `INDEPENDENT_RECEIPT.json` **field for
field** (no key differs except elapsed CPU): status `PASS_CENTRAL_INVOLUTION_AND_HECKE_SPAN`, projector coordinates (4,2,3,1,0), Hecke
dimension 5, orbit sizes (1,1,1,1,20), target projector rank 6, central action −1, separating functional (1,2,3,4,0) with value 1 on the
projector, seven index-24 candidates with exactly one succeeding, dim End(target) = 1.

## 2. What I verified independently (my own code, `runs/`)

| claim | how I checked it | result |
|---|---|---|
| **Lemma 2.1** (J ≤ GL_2(F_5), −I ∉ J ⟹ |J| ≤ 20) | exhaustively: built the **entire subgroup lattice of SL_2(F_5)** (76 subgroups) | every odd-order subgroup has order 1, 3 or 5; every even-order subgroup contains −I; with det-index ≤ 4 this gives |J| ≤ 20 |
| its stated ingredients | direct enumeration | −I is the unique nonidentity involution of SL_2; GL_2(F_5) element orders are {1,2,3,4,5,6,8,10,12,20,24}, so no order 15; the centralizer of a transvection has order 20; \|H\| = 20 and −I ∉ H |
| P = F_5[G/H], double cosets | construction from scratch | index 24; double-coset sizes (1,1,1,1,20); z permutes them fixing the 20-orbit and swapping the two pairs of singletons |
| left z = right σ² on G/H | permutation comparison | holds |
| e = 4·1 + 2R + R² + 3R³ | matrices over F_5 | e² = e, Re = 2e, rank e = 6; dim P⁻ = 12 |
| **the "central-even" span is 3-dimensional** | dimension of {T ∈ End_G(P) : T·e₋ = 0} | **3**, matching the z-invariants of the double-coset basis |
| Λ = (1,2,3,4,0) | arithmetic in the orbit basis | kills (1,0,0,1,0), (0,1,1,0,0), (0,0,0,0,1) and Λ(e) = 1 |
| dim End_G(M) = 1 | rank of e·(Hecke)·e | 1 |
| **index-24 sharpness** | for each of the seven order-4 subgroups of B/U, the actual multiplicity of θ* in F_5[(G/J)^U], computed over **C** with fourth roots of unity | multiplicity 1 for the subgroup giving J = H, and 0 for the other six |
| §7 repair 2 (eigenvector convention) | built Ω^U and the R_σ action | with successive R_σ-orbit labels the λ-eigenvector is Σ_k λ^{−k}; with covector labels [2^k] and the action β ↦ 3β it is Σ_k λ^{k}. The two labelings run in opposite directions, so the supplied display was inconsistent with its own stated action and the executable is right. Display-only: e, its rank, Λ and everything downstream are unchanged. |

My first attempt at the "central-even" dimension conjugated the Hecke basis by L_z and found 5 and 0. That was the wrong notion:
L_z is itself a G-endomorphism of P and commutes with every Hecke operator, so conjugation is vacuous. The correct object is one-sided
(operators killing P⁻), which gives 3. Both runs are kept in `runs/`.

## 3. The arguments I checked by hand

- **§3 (both Hom spaces vanish).** z ∈ J whenever [G:J] < 24, so z acts trivially on R[G/J]; it acts by −1 on P⁻. For f: P⁻ → R[G/J],
  equivariance gives f(x) = f(zx) = z f(x) = f(x) with f(zx) = −f(x), so 2f = 0 and f = 0 when 2 is invertible; likewise the other side.
  This is genuinely stronger than a separating functional on compositions, and it holds over Z_5, Q_5 and Q, not only mod 5.
- **§4 (repair of the N_H corollary).** The old step is indeed unavailable: π∘ι = |H|·id_P = 20·id_P = 0 in characteristic 5, so factoring
  ι∘π is not a splitting. The replacement is valid and universal: z N_J = N_J for every J of index < 24, z is central so every term
  a N_J b is z-fixed, while z N_H ≠ N_H because H and zH are disjoint. Hence no relation N_H = Σ a_i N_{J_i} b_i over any nonzero
  coefficient ring — which closes the "clear a denominator divisible by 5" escape.
- **§5.1 (outside fields, module form).** [G : q(J')] ≤ [G':J'] < 24, so z ∈ q(J'), so some j' ∈ J' acts as −1 on the inflated P⁻; hence
  (P⁻)^{J'} = 0 and Hom_{RJ'}(P⁻,R) = 0, and Frobenius reciprocity (induction = coinduction) gives both vanishing Hom spaces. No averaging
  over the kernel of q is used, so 5 | |ker q| is harmless.
- **§5.2 (outside fields, arithmetic form).** [K ∩ A : Q] < 24 puts z in Gal(K/(K∩A)); z extends to τ ∈ Aut(KA/A) of order 2; τ stabilises
  each conjugate D_g because z is central, and acts there as the central involution. Then T_out ∘ z = T_out and z ∘ T_in = T_in follow from
  invariance of the ideal norm under an automorphism fixing the target and compatibility of extension with automorphisms, so on 5-primary
  parts T_out kills the minus component and e₋T_in = 0. This is a vanishing statement about the actual class-group maps, not a
  contraposition of Etienne's implication — which is the substantive improvement.
- **§6.** j and N with Nj = 2, jN = 1 + z identify Cl(Q)⊗Z_5 with A_D^+ and ker N with A_D^-; the faithful component is one of the two
  quartic parts of that relative kernel. The conclusion — smaller-field class data give the plus part and no bound on the minus part —
  is exactly right and is the honest limitation of the whole central argument.

## 4. Dependency boundaries

- I did not re-read Etienne (arXiv:2411.13124) or Biasse–Fieker–Hofmann–Page (arXiv:2002.12332) this cycle. §5.2's direct proof is what I
  checked; the citations are context, and the note itself avoids relying on a converse of Etienne's Proposition 3.5.
- "Iterated Mackey composites reduce to double-coset operators with the same endpoints" is standard but was not verified from a source
  here; §5.1 supplies an independent route that I did check.
- The original archive's GAP/Python runs were read, not rerun (per instruction 4).
- Nothing here bounds b, c, any class group, any Selmer group or Sha. The remaining arithmetic target is unchanged.

## 5. Proposed addendum (not merged)

Their `PROPOSED_ADDENDUM.md` is accurate as written. I propose adopting it with two wording changes and one addition:

1. Replace "every subgroup J ≤ GL_2(F_5) with [G:J] < 24 contains −I. Proof: …" with the same statement plus the note that it was
   **verified exhaustively** against the full subgroup lattice of SL_2(F_5) in this review, independently of the ingredient checks.
2. In the sentence on the Brauer eigenvector, say explicitly that the two conventions (covector labels [2^k] with β ↦ 3β, versus
   successive R_σ-orbit labels) run in **opposite directions**, so the coefficients λ^k and λ^{−k} each belong to one of them; the
   executable uses the second and is unaffected.
3. Add, after the exclusion sentence: *the exclusion concerns ordinary ideal extension, norm and conjugation channels only; it says nothing
   about the size of the target component, which is known to be nonzero (b ≥ 1), and a vanishing-channel statement never bounds it.*

Every non-exclusion in §5.3 should be preserved verbatim: arithmetic elements or relations specific to D; non-splitting inequalities;
fields of degree ≥ 24; different twisted coefficient constructions; a direct one-sided or component-only coverage proof; evaluated
Euler/Stark/Iwasawa inputs. Degree is not an operation count.

Proposed status lines, unchanged from theirs:

```
CENTRAL_ODD_TARGET_HAS_NO_LOWER_DEGREE_NORM_CHANNEL   (new, reviewed here)
GENERIC_RADICAL_SATURATION_VERIFIED                   (unchanged)
SPECIALIZATION_ARITHMETIC_OPEN                        (unchanged)
ARITHMETIC_INPUT_NOT_IDENTIFIED                       (unchanged)
```

## 6. Escalation

None is warranted: no unresolved arithmetic inference with an exact line and counterexample was found, so Fable is not called.

## 7. Resources

Their checker 0.12 s; my exhaustive lattice check 3.15 s; two smaller checks 0.12 s together. Aggregate ≈ 3.4 CPU-seconds of the 60
allowed, one process, well under 1 GiB.
