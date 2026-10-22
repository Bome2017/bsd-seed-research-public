# W3 under the one-sided detector screen: ℓ₂ and the weight-direction residual

Claude (Opus 5.5), 2026-10-06. Paper only, $0. The assignment is Pro's redirect: test the W3 quantities under Aristotle's one-sided detector framework, with the weight-direction residuals as the main interest. An independent adversarial review (PASS_WITH_CORRECTIONS) has been applied; see §8. This note corrects one statement in the seed-admission return (§6).

**Verdict: `BRIDGE_IN_HAND__GLOBAL_CONTROL_OPEN`, ordinary primes only.**
- **Λ₁ is forced.** Under the retained low-jet input (LJ1), Λ₁ = 0, so the only weight-direction unknown is Λ₂.
- **The detector.** The W3 detector is the pair (Λ₂(p), ℓ₂(p)). It is a valid one-sided detector at good ordinary p ∤ D, under the retained W3 imports.
- **What is missing.** No integer I_E controlling its alarm set has been identified here.
- **Not ruled out.** Nothing examined rules W3 out. It is the only surviving lane with a one-sided bridge.
- **Coverage gap.** W3 does not cover the supersingular primes, which are infinitely many (Elkies), so it can give at most the ordinary part of U.

## 0. The screen (Aristotle, Lean-checked; recompiled here)

**Source.** `Coinvariant/Frontier.lean` (return 69562e6c) and `RequestProject/Continuation/MiddleGround.lean` (return eb3e82a5, REVISION_4). The recompile record is in `checks/ARISTOTLE_RECOMPILE.txt`: `bad_primes_dvd_fixed_integer`, `finite_of_detector`, `nu_collapses` and `congruence_without_bridge_insufficient` use only propext, Classical.choice and Quot.sound.

**The finite-support template.** For a candidate Λ_p and a fixed integer I_E ≠ 0, outside a finite set:
1. **Bridge:** Ш[p] ≠ 0 ⇒ p ∣ Λ_p (one-sided; false alarms allowed);
2. **Control:** Λ_p ≡ I_E·u_p (mod p) with u_p a p-unit;
3. **Non-circularity:** I_E is built without Ш.

If all three hold, the bad primes lie among the prime factors of I_E.

**Remark (elementary).** With free units, condition 2 holds for some I_E if and only if the alarm set A = {p : p ∣ Λ_p} is finite. One direction: take I_E = ∏_{p∈A} p. The other: the alarm set of I_E·u_p is the prime support of I_E. Under the bridge, A ⊇ (bad primes) ∪ (false alarms), so proving A finite proves U on the domain covered **and** finiteness of the false alarms. The route is easier than U only if the finiteness comes from an independently constructed I_E whose prime support visibly contains A.

## 1. The W3 quantities (from the retained sources)

**Node values and jet.** By formula (F) of `original/FINITE_MOMENT_MODULE.md`, V_(w,s) = α_w·F_p(t_w, t_s) (mod p⁴), with t_w = (1+p)^w − 1 ∈ pℤ_p and nodes (w,s) ∈ {(3,2), (3,3), (4,3), (4,4)}. Here F_p is the two-variable p-adic L-function of the integral Hida family through the seed at p. The quadratic jet is a T² + b TS + c S², with b = −c. Lean `W3.quadratic_jet_forcing`: if all four nodes vanish mod p³, then p divides a, b and c. **c = unit·ℓ₂(p)** (imported).

**Λ₁ is forced to vanish.** Λ_p(T) = ∫(1+T)^u dΞ_p({∞}−{0}) is the total mass at one divisor.
- Formula (F) at s = 0, together with the U_p identity Σ_a m_(n,0)(Ξ({∞, a/p})) = (α₀−1)Λ_n + Σ_{r≥1} α_r Λ_{n−r}, gives as power series

      α(T)·F_p(T, 0) = ∓(α(T) − 1)·Λ(T).

- Λ₀ = 0 (rank ≥ 2). The T-coefficient of F_p(T,0) is ∓(1 − 1/α₀)Λ₁. Here 1 − 1/α₀ is a p-unit, because α₀ ≡ a_p ≢ 1 (mod p): the seed has no anomalous primes.
- The retained input (LJ1), F_p ∈ (T,S)² (`ARITHMETIC_LOW_JETS.md`, grade WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS: the two rational points force a double zero), therefore gives **Λ₁ = 0**.
- Then **a = ∓(1 − 1/α₀)Λ₂ ≐ Λ₂**. α₁ occurs only as α₁Λ₁ and α₂ only as α₂Λ₀, so both drop out.

**Hence:** at good ordinary p ∤ D, W3 raises an alarm at p ⟺ **p ∣ Λ₂ and p ∣ ℓ₂**.

**Meaning of Λ₂.** Since Λ_p(p) = Λ₂p² + O(p³), we have **Λ₂ ≡ u·p⁻²Λ_p(p) (mod p)**: the first undetermined (p²-)digit of the critical value of the weight-3 member g_1^{(p)} (level Np, nebentypus ω_p^{−1}).
- This is consistent with the global-period return's retained b_p ≥ 2.
- Its M_p = L(g,2)/Θ, divided by p², tracks the same digit if η_p is a unit, since F(p,0) ≡ F(p,p) ≡ ap² (mod p³) by b = −c.

**Residuals at p = 31** (counts verified by the reviewer):
- order 1: 120 weight-two columns (59 + 59 + 1 + 1), the Λ₁ slot, and α₁m₀₀;
- order 2: 176 weight-two columns, 115 order-1 family columns (not weight-two data), the Λ₂ slot, α₁m₁₀ and α₂m₀₀.

Both residuals are the §3.4 U_p identity. Under LJ1 the open weight-direction quantity is Λ₂.

## 2. The screen applied

| Quantity | 1. Bridge | 2. Control ⟺ finite alarm set | 3. Independent I_E | Status |
|---|---|---|---|---|
| ℓ₂(p) (cyclotomic) | Yes, at retained grade: the contrapositive of the per-prime criterion "ℓ₂ ≢ 0 ⇒ Ш[p^∞] = 0", at good ordinary p under the standing hypotheses. | **Open.** False alarms include the cyclotomic-regulator-degenerate primes. At p = 17, Reg_γ = 17·13 + O(17²) while Ш[17^∞] = 0, so **ℓ₂ is not an every-prime detector**. (c ∝ ℓ₂ is imported, and 17 ∤ D is unverified.) Finiteness of all its false alarms: heuristically infinite (Σ 1/p), neither proved nor disproved. | none identified | not ruled out; heuristically disfavored alone |
| Λ₂(p) alone | Not separately: it enters through a. | the same Fermat-quotient-type heuristic | none identified | not a detector alone |
| **The W3 pair (Λ₂, ℓ₂)**, i.e. the jet | **Yes, conditionally:** contrapositive of the W3 index theorem with `quadratic_jet_forcing`, on the cofinite Hida domain p ∤ D, at good ordinary p. Imports: source identification, Hida control (written; D not computed), LJ1, b = −c. | **Open.** An alarm needs p ∣ Λ₂ and p ∣ ℓ₂. Heuristically rare (Σ 1/p², **assuming the two behave independently**). No mechanism is known. | none identified | **bridge in hand, control open; ordinary primes only** |
| q = L″(E,1)/(2ΩReg) | **Missing** (needs a rank-2 GZ–Kolyvagin/TNC link). | Automatic once q is a nonzero rational. | yes, if Q36 | control (given Q36) without bridge |

Pro's complementarity, made exact: **W3 has a bridge without control; q has control without a bridge.**

## 3. Candidate sources of an independent I_E

| Candidate | Finding | Status |
|---|---|---|
| Λ₁ | A trivial carrier: Λ₁ = 0 at every prime in the domain (LJ1). Useless for FIN. | trivial |
| Hida families at different p as "one object" | No map relating their Λ₂-coefficients is known. They live over different weight spaces ℤ_p⟦T⟧. | none known |
| The weight-3 forms g_1^{(p)} | No global identity relating their critical values across p is known. Congruence to f fixes only the vanishing digits. | none known |
| The domain integer D = 2·N·φ(N)·D₀ (D₀ includes the auxiliary primes q_h; `COFINITE_HIDA_CONTROL.md` §2) | Controls the Hida algebra's structure, not Λ₂'s values. η_f is a p-unit for p ∤ D. | domain condition only |
| η_f / L(ad⁰f, 1) | "Ш[p] ≠ 0 ⇒ p ∣ η" is false in general (10-01 test bank). | no |
| Beilinson–Flach/KLZ classes; Ochiai's big Kato class | They reproduce the same F_p, with no new global control. | no new carrier |
| Kato's bottom class for f | It vanishes in rank 2. | no |
| Big Heegner points | They specialize to torsion at the seed (y_K torsion). | no |
| Known weight-derivative theorems (Greenberg–Stevens, local at p) | Split multiplicative primes only. The seed's W3 primes are good ordinary. | not applicable |
| Two-variable leading term (jet ≐ #Ш·form) | Conjectural; its only p-independent factor is #Ш, which is circular. | circular |
| Aristotle's CRT / rational-reconstruction test | The right probe once Λ₂ residues exist at many primes in one fixed normalization. **No seed Λ₂ value exists at any prime.** | cannot run yet |

## 4. Scoped statements, with grades

1. **(Proved, elementary.)** Control ⟺ a finite alarm set. Under the bridge this implies U on the covered domain, plus finitely many false alarms (§0 Remark).
2. **(Written derivation under retained imports.)** Λ₁ = 0, a ≐ Λ₂, and the W3 alarm at ordinary p ∤ D is "p ∣ Λ₂ and p ∣ ℓ₂".
3. **(Seed data plus imports.)** ℓ₂ is not an every-prime detector (p = 17). Whether its false alarms are finite is unestablished.
4. **(Heuristic, labelled.)** Single coefficients behave like Fermat quotients and are expected to vanish infinitely often. The pair (Λ₂, ℓ₂) is expected to vanish jointly only finitely often, if independent.
5. **(Logical shape under the conjectural leading term.)** If jet ≐ #Ш·form, W3 holds at p iff p ∤ #Ш and the form is nonzero mod p. So cofinite W3 success **implies** cofinite mod-p nonvanishing of the form, but is not equivalent to it.
6. **(State of the art, for scale.)** Infinitely many non-Wieferich primes for a fixed base is known only under abc (Silverman 1988). Nondegeneracy of p-adic height regulators is open in rank ≥ 2.

**Missing ingredient, stated exactly:** cofinite nonvanishing of the pair (Λ₂(p), ℓ₂(p)) mod p at good ordinary p, obtained from an independently constructed I_E. **Plus** a separate route for the infinitely many supersingular primes.

**Recommendation.** Keep W3 as the lane with a one-sided bridge, and do not run more primewise ℓ₂ values. It remains a per-prime **route** at regulator-degenerate primes such as 17, where Λ₂ would have to carry the test (no prime has been certified this way). Its uniform input is a global identity for the pair.

## 5. Where W3 and Q36 meet

They meet at a global rank-2 object Z of the following kind (**none known**):
- (i) an archimedean height formula relating ⟨Z,Z⟩_∞ to L″(E,1);
- (ii) a Kolyvagin-type descent bounding Ш[p] by Z's index for all p.

If such a Z existed:
- Z's index would be an independent I_E for the bridge on the q side, and W3's p-adic alarm-set problem would no longer be needed for U.
- From (i), the rationality of q (RAT) would follow if ⟨Z,Z⟩_∞ is a rational multiple of Reg_∞. DEN ≤ 174 would also need the explicit constants and Z's index.

Without such a Z, no link between W3 (p-adic completions) and Q36 (the real completion) is known. A Q36 proof by bounded algebraicity or a common scalar would not by itself give FIN. Aristotle's FRONTIER.md states the same logical shape for the Q36 route.

## 6. Correction to the seed-admission return (lab commits 73ec5bf / 5bd0305)

That return said ℓ₂ was "dead as I_E" and that "the seed defeats it as a uniform detector at p = 17". **This was too strong.** The false alarm at 17 shows ℓ₂ is not a characterization, and not an every-prime detector. As a one-sided detector it fails only if its false alarms are infinite, its control fails, or its bridge fails. The bridge holds, and the rest is open. Everything else in that return stands:
- the Heegner collapse;
- q as the only prime-independent candidate identified there;
- p = 31 already settled.

## 7. Checks of the two Aristotle returns supplied 10-06

| Return | Check | Result |
|---|---|---|
| 69562e6c (FRONTIER, coinvariant, Heegner ν) | recompiled 6 Lean modules (v4.28.0, Mathlib 8f9d9cff) | all compile. The Frontier theorems use standard axioms only. `KolyvaginPrime3391.affine_count_3391` also uses `Lean.ofReduceBool` and `Lean.trustCompiler` (compiler-checked, as stated). |
| 69562e6c | PARI cross-check of the ℓ = 3391 Kolyvagin data | a_3391 = 0; (−23/3391) = −1; 53 ∣ 3392; a_53 = −6. Confirmed. |
| 69562e6c | `MANIFEST.sha256` | 62/63 OK (`STATE.json` stale) |
| eb3e82a5 (Heegner continuation, REVISION_4) | read the frontier and the cross-prime test | consistent. Its self-test uses synthetic controls only. |

## 8. Independent review applied (adversarial reviewer, PASS_WITH_CORRECTIONS)

1. **Λ₁ = 0 under LJ1**, with a ≐ Λ₂ and α₁, α₂ dropping out (major): applied in §1, §2 and §4.
2. **Λ₂, not Λ₁, is the first undetermined digit**, consistent with b_p ≥ 2 (major): applied in §1.
3. **Grades:** "proved" became written-derivation or imported where due; LJ1 is a trivial n = 1 carrier. Applied in §3 and §4.
4. **"Fails cofinite detection at 17"** became "not an every-prime detector": applied in §2 and §6.
5. **"Equivalent" became "implies"**; supersingular coverage added; the independence assumption labelled. Applied in the verdict, §2 and §4.
6. **Adjoint L-invariant row** removed (α₁ drops out; the tie is Hida's theorem, IMRN 2004); Greenberg–Stevens stated as local at p. Applied in §3.
7. **Unscoped phrases** scoped ("none known / identified here"); "certificate" became "route"; "Q.1 would follow" became "RAT would follow". Applied throughout.

The reviewer's carrier search found **no carrier for Λ₂** (§3 rows on BF/KLZ, Ochiai, Kato's bottom class and big Heegner points).

FIN, ORDER9 and Q36 are unchanged.
