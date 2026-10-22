# Tame route after G2: is there a route to the Law that does not encode FIN? (Claude, Opus 5.5, 2026-10-06)

The question is Pro's (relayed 10-06): inspect `link_iff_fin_and_kato`, say where the equivalence comes from, and decide whether the Tame Law has an independent construction that does not use Ш-finiteness. This note is paper only and cost $0.

## 1. Where the equivalence in `link_iff_fin_and_kato` comes from

Sources: Aristotle 69562e6c (7), `Coinvariant/TameLink.lean` (`link_iff_finite_alarms`, `link_iff_fin_and_kato`) and `Coinvariant/DetectorRule.lean` (`exists_fixed_carrier_iff_finite_alarms`), all recompiled here with standard axioms.

- **Law ⇒ FIN-tail ∧ (K).**
  - The Law's alarms are the primes dividing W, which are finitely many. So x_p ≢ 0 (mod p) outside a finite set.
  - The BKS factorization x_p ≐ x_{ℚ,Σ}·#Ш[p^∞] identifies the zero set of x_p with {p : Ш[p] ≠ 0} ∪ {p : p ∣ x_{ℚ,Σ}}.
  - This is the direction the route exists for.
- **FIN-tail ∧ (K) ⇒ Law.**
  - This direction goes through `exists_fixed_carrier_iff_finite_alarms`. That lemma takes W to be the product of the finitely many alarm primes, sets u_p = x_p·W⁻¹ (mod p) at all other primes, and sets u_p = 1 at the alarm primes.
  - The W it produces is built from the Ш-support itself. It is the trivial direction.
- **Reading.** With free p-units the Law records only the zero pattern of x_p. It therefore says nothing beyond FIN-tail ∧ (K).
  - (K) is retained at good ordinary p: Codex K288 audit 2026-09-27, Kato plus Skinner–Urban.
  - So the existence form of the Law is FIN restated. It is not a weaker target.

## 2. The exact Law is strictly stronger than FIN

- **What it says.** In the exact Law, W and the unit are fixed in advance. Under the audited conventions u = 1, so it says s_p ≡ 288 at the eleven residues checked.
- **Why FIN cannot give it.** FIN fixes only which residues are zero, never their values. So FIN cannot prove the exact Law.
- **What any proof must do.** It must produce the residues s_p from a characteristic-zero identity, and it would then imply FIN through the ⇒ direction above.
- **The only kind of statement that would count.** A characteristic-zero identity whose tame realizations give C₂(p,ℓ) = m·(a_ℓ − 2)·R_{p,ℓ} with one rational m.

## 3. The candidate sources Pro named, checked against the record

| Candidate | What the record and the screened literature give | Supplies the exact Law without FIN/BSD? |
|---|---|---|
| The fixed scalar q (TAC, m = 8q) | Needs q ∈ ℚ, which is open for every rank-two curve, plus a tame–archimedean comparison | no |
| Height comparison / biextension identity | G2's fixed 1-motive gives the regulator side (a_ℓ − 2)·R_{p,ℓ} as Frobenius invariants. Record K5: nothing produces the modular-symbol side C₂ from it | no |
| Rank-two Gross–Zagier | No number-field version is known. Yun–Zhang covers function fields only (record A3/V6) | no |
| Published comparison (Tan, Ann. Inst. Fourier 45, 1995, Thms 3.12/3.14/3.16) | Proved from BSD for E over ℚ and over every intermediate field, and even then only up to a nonzero constant in F_p^× | no (BSD-conditional) |
| Characteristic-zero comparison Θ_E ↔ Z ↔ M_G2 (admission test, `~/BSD_COMPARISON_MAP_ADMISSION_2026-10-06/`) | Fails at the Θ_E arrow. The degree-2 class lies in a finite group at every level, so it has no ℚ-valued realization | no (NOT_ADMITTED) |

## 4. Is there a strictly weaker version of the Law that still gives finite support?

Pro asked this in a follow-up the same day. Statements about the family (x_p mod p) fall into two classes.

- **Zero-pattern statements** depend only on Z = {p ∉ B : p ∣ x_p}.
  - By the BKS factorization, Z = Supp Ш ∪ {p : p ∣ x_{ℚ,Σ}} outside B, and Supp Ш ⊆ Z.
  - A zero-pattern statement forces Supp Ш to be finite, whatever the split of Z, only if it forces Z minus the (K)-exceptions to be finite.
  - The (K)-exceptions are finite at good ordinary p (retained).
  - So the weakest sufficient zero-pattern statement is "Z is finite", which is FIN-tail ∧ (K). This is exactly the existence form of the Law (§1).
  - **No zero-pattern weakening escapes FIN-tail.** This is elementary logic given the factorization.
- **Residue statements** constrain the values of x_p mod p, not only whether they vanish. Examples:
  - the exact Law (one W, u = 1);
  - a bounded-unit law (x_p ≡ W·u with u in a fixed finite set U ⊂ ℚ^×);
  - a law with finitely many candidate constants.

  Each of these implies FIN-tail (x_p ≡ 0 only at primes dividing W·∏U) and is strictly stronger than it, because FIN never fixes residues. These are the only versions that could have a mechanism independent of FIN. Each needs a characteristic-zero identity that produces the residues. The record has none (§3), and its only residue data agree with the exact Law: eleven residues, all 288 under the audited conventions.

So the answer is no. No weakening of the Law is both sufficient for finite support and different in content from FIN-tail, except residue-level laws. Every residue-level law needs the same missing characteristic-zero identity. The tame route has reached a precise endpoint: an exact reformulation, not yet a mechanism. It opens only if a residue-level identity is found.

## 5. Verdict

- **The Law is the only remaining gate on the tame route.** G2 (fullness and auxiliary primes) is solved, as are Theorem W and the Ota detector.
- **The existence form of the Law is FIN restated.**
- **The exact form needs a characteristic-zero rank-two identity.** No such identity exists in the record or in the literature screened so far.
- **The tame route ends at the same missing object as the Heegner, W3 and Q36 routes.** That object is a rank-two Gross–Zagier-type identity tying modular-symbol data to the Mordell–Weil biextension with a rational constant.
- **Scope.** This is a scoped negative about known constructions, not an impossibility statement.
- **What would change it** (any one of these):
  - such an identity;
  - an unconditional version of Tan's comparison with an exact constant over the degree-p subfields of ℚ(μ_ℓ);
  - rationality of q together with TAC.

FIN, ORDER9 and Q36 are unchanged.
