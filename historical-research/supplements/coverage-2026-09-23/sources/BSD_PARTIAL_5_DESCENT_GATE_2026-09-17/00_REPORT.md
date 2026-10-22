# PARTIAL_FULL_5_DESCENT_GATE_001 — report (2026-09-17)

**Return: NO_PARTIAL_DESCENT_IN_STATED_CLASS.**

No construction from a smaller algebra, resolvent or subfield can bound Sel₅(E/Q) for the (2243, 12) seed, whatever its coefficients:
- If its coefficient module is −I-even, it induces the zero map on H¹(Q, E[5]). These are the already-closed norm, extension and conjugation channels.
- If its coefficient module is −I-odd, the field it needs has degree ≥ 24 over Q, so it is not smaller.
- The minimum, 24, is attained exactly by the four twisted point fields.

**Scope.**
- Source reading and finite-group computation only: GAP, 6.5 CPU-s.
- No FiveDescent, no degree-24 class group, no bnfcertify, no relation search.
- The hyperelliptic partial-descent theorem is not claimed to apply.

## Phase A — Fisher's full descent and the exact object behind "dim Sel₅ ≤ 2"

**Source.** T. Fisher, *Explicit 5-descent on elliptic curves*, ANTS X, Open Book Series 1 (2013), §6. The text is archived in `src/` (sha256 `f08838ad…`).

What §6 establishes, in paraphrase:
- For E/Q with no rational 5-isogeny, put L = Q(T), with T ∈ E[5] nonzero and [L:Q] = 24, and let σ₂ be the automorphism with σ₂(T) = 2T.
- There is an injective homomorphism H¹(Q, E[5]) → L*/L*⁵ whose image lies in the eigenspace {x : σ₂(x) ≡ x² mod L*⁵} (his equation (8)).
- If the Tamagawa numbers are prime to 5, the 5-Selmer group lies in L(S, 5), where S is the set of primes of L above 5.
- In his example (6727a1) he takes the class group and units of L from PARI's heuristic output, calling L too large for an unconditional computation. He closes by naming class groups and units as the main difficulty for further examples.

**Magma contract.** The handbook pages return HTTP 401 from this environment. The operator's statement that Magma implements n = 5 descent is recorded as **operator-supplied, not independently checked**.

**Applied to (2243, 12).**
- The Tamagawa product is 16, prime to 5. So Sel₅ ⊂ L(S, 5)^{(2)} with S = {𝔭 | 5}.
- There are two such primes, with (e, f) = (4, 1) and (5, 4). σ must fix each, since their (e, f) differ. So the S-part contributes only to eigenvalue 1, and:

      dim L(S,5)^{(2)} = 3 + c,    3 = the χ-rank of O_L*/5 (Herbrand; retained),   c = dim Cl(L)[5]^{(2)}.

  This reproduces the retained bound dim Sel₅ ≤ 3 + c.

The three categories the task asked to separate:
- **(i) Full class group and units:** not needed.
- **(ii) 5-primary data only:** an upper bound on one faithful χ-component suffices.
  - c = 0 gives Sel₅ ≤ 3, and parity then gives exactly 2.
  - Alternatively, b ≤ 2 on the dual component.
  - c ≤ 1 would also need explicit χ-units (t₅ ≥ 2).
  - These are exactly the recorded certificate rows.
- **(iii) Local conditions:** they cannot replace (ii).
  - At 5, the Kummer image is a line inside the 2-dimensional H¹(Q₅, E[5]), so it removes at most one dimension.
  - The exact description Sha[5] = ker(loc₃₁, loc₁₈₁) still presupposes the global group L(S, 5)^{(2)}.

**So:** the least that must be certified is an upper bound on a faithful 5-primary χ-component of a degree-24 class group.

## Phase B — partial-descent techniques and why they do not transfer

**Source.** S. Siksek, M. Stoll, *Partial descent on hyperelliptic curves and the generalized Fermat equation x³+y⁴+z⁵=0*, Bull. LMS 2012, arXiv:1103.1979. The text is archived in `src/` (sha256 `001a9170…`). The operator's CiteSeerX link redirects to an archive host that this environment cannot fetch. The description matches this paper: degree-30 fields avoided by factoring over quintic fields K.

**Their mechanism, in paraphrase.**
- Choose a Galois-invariant family Y of subsets of the root set.
- The Y-Selmer set belongs to an intermediate covering whose group is the quotient J[2]/Γ_Y.
- It gives only a necessary condition: if it is empty, then C(Q) = ∅. It is **not** an injection of a Selmer group, and is "usually weaker".
- Computing it needs class groups and units of the fields in the algebra L_Y only, namely subfields of the field K over which f factors.
- The authors note that no intermediate covering exists in the generic case where Gal(f) is the full symmetric group.

**The two ingredients, and how each fails for E[5] over Q:**
1. **A proper Galois-stable subgroup** (their Γ_Y) is needed.
   - E[5] is **absolutely irreducible** under GL₂(F₅) (C2), and GL₂(F₅) is **transitive** on E[5]∖0 (C1).
   - So the descent algebra over Q is a single field L of degree 24, with no proper factor algebra.
2. **Coefficients that allow Kummer theory over the small field.** Their descent is a 2-descent, and μ₂ = Z/2 is a trivial Galois module, so K*/K*² suffices.
   - For p = 5, over any base K′ where E[5] becomes reducible (up to conjugacy K′ ⊇ F₀, the field of the Borel), the sub and quotient are the characters ψ and ψ* = ωψ⁻¹. Neither is trivial or ω.
   - So Kummer theory or class field theory must pass to the fields those characters cut out. Over F₀ these are L and L_d, of degree 24.

**The exact degree-24 bridge.** 5-isogeny descent over F₀ is exact: restriction to F₀ is injective because 6 is prime to 5. Its isogeny Selmer groups are governed by the χ-components of Cl(L) and Cl(L_d), i.e. c and b, which are already recorded. So it is an exact bridge with **no computable gain**, and it lies outside the stated "smaller" class.

## Phase C — finite-group kill test (`runs/phaseC_kill_test.g`, GAP 4.15.1, exact)

| check | result |
|---|---|
| C0 | \|GL₂(F₅)\| = 480; −I is central |
| C1 | transitive on the 24 nonzero vectors, so the descent algebra over Q is one field of degree 24 |
| C2 | V = E[5] is irreducible and absolutely irreducible, so there is no Galois-stable subgroup and no Siksek–Stoll intermediate covering over Q |
| C3 | 48 subgroup classes; 13 avoid −I, with **minimal index 24**; all 15 classes of index < 24 contain −I |
| C4 | exactly **4** classes of index 24 avoid −I, all C₅ ⋊ C₄. They are the vector stabilisers of V ⊗ detʲ, j = 0, 1, 2, 3 (the four twisted point fields). The Gassmann pairs are {j=0, j=1} (= {L, L_d}, matching ζ_L = ζ_{L_d}) and {j=2, j=3} |
| C5 | over **every** subgroup H′ of index < 24, i.e. every base field of degree < 24: every composition factor W of E[5] has −I ∉ ker(H′ → GL(W)). The field cut out by W has degree ≥ 24, and exactly 24 only for the Borel characters (indices seen: 24, 48 and 480) |
| C6 | vector stabiliser of order 20 with N_G(H)/H ≅ C₄ = Aut(L), generated by the scalar-2 automorphism σ₂ |

**Kill statement.**
- Let the construction pass through a Galois module M over a base field K′.
- Its information about H¹(Q, E[5]) enters through a nonzero map from, to, or pairing with E[5].
- It therefore factors through a subquotient of E[5] on which −I acts as −1.
- The kernel of the action on that subquotient avoids −I, so by C3 and C5 its field has degree ≥ 24 over Q. If instead the Galois image of K′ misses −I, then K′ itself already has degree ≥ 24.
- A construction confined to fields of degree < 24 therefore sees only −I-even data and induces the zero map on Sel₅.
- Such a map can inject Sel₅/⟨δP₁, δP₂⟩ only if that quotient is already 0, which is the thing to be proved.

## Return

    NO_PARTIAL_DESCENT_IN_STATED_CLASS
      every certificate for dim Sel_5 <= 2 must do arithmetic in a field of degree >= 24 cut out by a -I-odd subquotient of E[5];
      the minimal such fields are the four twisted point fields (index-24 classes C5:C4, j = 0..3; Gassmann pairs {0,1}, {2,3})
      Fisher's full descent needs only the 5-primary faithful component: c = 0 (or b <= 2) — not the full class group, not units
      Siksek-Stoll partial descent needs a proper Galois-stable subgroup and trivial Kummer coefficients: E[5] has neither over Q,
        and over any base of degree < 24 its composition factors are -I-odd characters cut out in degree >= 24

**Non-claims.**
- This says nothing about the feasibility of degree-24 computations; the projected-relations stop remains a resource decision.
- It says nothing about non-descent methods (Euler systems, p-adic L-functions) or other primes p.
- It does not claim that c or b is large.

## Proposed ledger block (not merged; needs operator acceptance)

```
PARTIAL_FULL_5_DESCENT_GATE_001 (seed (2243,12)) — NO_PARTIAL_DESCENT_IN_STATED_CLASS (2026-09-17)
  Fisher 2013 §6: H^1(Q,E[5]) -> L*/L*^5 (L = Q(T), degree 24) lands in the sigma_2-eigenspace x^{sigma_2} = x^2; with Tamagawa numbers
  prime to 5, Sel_5 lies in L({p|5},5). For (2243,12): dim L(S,5)^(2) = 3 + c (the S-part is sigma-fixed), so the object needed for
  dim Sel_5 <= 2 is an upper bound on the faithful 5-primary component: c = 0 (or b <= 2); not the full class group, not units.
  Siksek-Stoll partial descent (arXiv:1103.1979) needs a proper Galois-stable subgroup and trivial Kummer coefficients; E[5] is absolutely
  irreducible and transitive on E[5]\0 (the descent algebra is the single degree-24 field). GAP kill test on GL2(F5): 13 of 48 subgroup
  classes avoid -I, minimal index 24; exactly 4 of index 24 (C5:C4, the point fields of E[5] (x) det^j, Gassmann pairs {0,1}, {2,3}).
  Over every base of degree < 24 each composition factor of E[5] is -I-odd, cut out in degree >= 24. Hence no smaller
  algebra/resolvent/subfield certificate exists (-I-even channels give the zero map; -I-odd ones are not smaller).
  The 5-isogeny descent over F0 is an exact bridge with no computable gain (reproduces c, b). Magma handbook not retrievable (HTTP 401):
  the n = 5 implementation claim is operator-supplied. No descent, class group or relation search was run.
```

Files: `src/Fisher2013_Explicit5Descent_OBS1.{pdf,txt}`, `src/SiksekStoll2012_PartialDescent_arXiv1103.1979.pdf`, `src/SiksekStoll2012.txt`, `runs/phaseC_kill_test.g` (+ `phaseC_output.txt`, `phaseC_time.txt`), `MANIFEST.sha256`.

## Erratum (operator review, 2026-09-18) — the kill statement is narrowed; this section governs

**What was wrong.** The sentence "a construction confined to fields of degree < 24 sees only −I-even data and induces the zero map on
Sel₅" is **wider than the argument proves**. It is withdrawn. Two counterexamples to the literal wording:
- **Local restriction.** The fixed-prime localizations loc₃₁ and loc₁₈₁ are nonzero on H¹(Q, E[5]) and need no global field. The
  decomposition group at ℓ is a small subgroup that need not contain −I, and a local field has no "global degree" in the sense of C3–C5.
- **Cup products.** Take ξ ↦ inv_v(e₅(ξ ∪ κ)) with κ a fixed explicit class such as δ(P₁), through the Weil pairing
  E[5] ⊗ E[5] → μ₅ into H²(Q_v, μ₅) (a −I-even target). This gives nonzero linear functionals on H¹(Q, E[5]). Poitou–Tate and
  Cassels–Tate constructions are of this kind.

The error in the proof is the parenthetical "if instead the Galois image of K′ misses −I, then K′ itself already has degree ≥ 24".
That holds for number fields, not for completions, and the pairing clause did not track the auxiliary fixed class.

**What the argument does prove.** The C1–C6 computations stand. They yield:
- **NO_LINEAR_KUMMER/PERMUTATION/RESOLVENT_DESCENT_BELOW_DEGREE_24.**
  - Take any G_Q-linear descent map induced by a module map E[5] → Ind_{H′}^{G}(W′), with [G : H′] < 24 and −I acting trivially on W′
    (Kummer coefficients μ₅, permutation or resolvent modules). Such a map is zero.
  - Any −I-odd coefficient module over a number field needs a splitting field of degree ≥ 24. The minimum, 24, is attained exactly by
    the four twisted point fields.
  - This closes the Siksek–Stoll / intermediate-cover class over Q and over every base of degree < 24. That is a Selmer-SET
    obstruction attached to a factorization over smaller fields, not a Selmer-group upper-bound machine.

**Explicitly not excluded.** Local conditions; functionals from cup products with fixed explicit classes; Poitou–Tate or Cassels–Tate
constructions; non-descent methods (Iwasawa theory, Euler systems).
