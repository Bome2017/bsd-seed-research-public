# COLLISION CHECK

All paths are relative to `project/reading_set/BSD_SEED_ARISTOTLE_2026-10-05/`.

**What was searched.**

* All 44 cards of `guide/03_WALL_ATLAS.md`, read in full.
* `guide/01`, `guide/04` and `guide/05`.
* `sources/HISTORICAL_STOPS_AND_CORRECTIONS.md` (3,353 entries), searched with `grep` for:
  Kolyvagin, Heegner, Bertolini, derived height, Gross–Zagier, p-adic height, Schneider,
  Perrin-Riou, residual image, surjectiv, Mazur–Tate, Iwasawa, p-adic L-function, genus 2,
  hyperelliptic, receiver, and the bad primes.
* `sources/governing/{RECEIVER_DESCENT,RECEIVER_LOCAL,RECEIVER_ARITHMETIC,FOUR_LANES}.md`.
* `working_set/BSD_ADDITIVE_SUPPORT_REVIEW_CODEX_2026-10-03/context/FORWARD_RECEIVER_RETAINED.md`.
* `sources/governing/RELEASE.json` (claims A.3, R.1, B.1, B.10, B.18, B.20, B.23).
* `sources/FULL_COMPENDIUM_2026-10-01.md` §00.5.

The search was keyword- and card-based. It is **not** a claim of exhaustive novelty: the
283,307-object external archive was not available.

---

## A. Theorem BFR / Lemma L (the result actually returned)

**Applicable cards:** W13 (receiver construction), W14 (exact local splitting), W21
(receiver bookkeeping), W01 (pointwise vs. support), W02/B.20 (bad primes not covered),
W39/W40 (bad-prime criterion B.18).

**Closest prior construction.** The forward class-group receiver,
`working_set/BSD_ADDITIVE_SUPPORT_REVIEW_CODEX_2026-10-03/context/FORWARD_RECEIVER_RETAINED.md`
§1–§4. It is confirmed in `sources/governing/FOUR_LANES.md` and summarized in W13. Its
Proposition is stated **only for good p ≥ 5**. B.20 states explicitly that "the bad primes
2243, 4547 and 5843 … are not covered". The compendium §00.5 lists F-bad as open.

**First implication of the prior construction that fails to transfer to the bad primes.**
This is §2 of that file: "Because p does not divide #E(F_p), reduction shows
E(Q_p)/p = E_1(Q_p)/pE_1(Q_p) … Equation (3) therefore shows that R_p generates that local
Kummer line."

* At bad `p` the hypothesis has no meaning.
* At `p = 4547` the conclusion is **false**. There
  `[E(ℚ_p):E₁(ℚ_p)] = 2·4547` and `E₁ = pE₀`, so `R_p ∈ pE(ℚ_p)` (Lemma L(iii)).
* §3's proof that `r ≠ 0` (by localization of `R_p` at `p`) is also unavailable at 4547.

**New arithmetic input that changes it:**

1. The bad-prime local index computation `c_p·#Ẽ_ns(𝔽_p) ∈ {2242, 2·4547, 2·5844}`. It is
   re-checked here by exact singular-point/tangent-cone computation, plus kernel-checked
   divisibilities. With it, the local Kummer line at 2243 and 5843 is spanned by `R_p`.
2. An exact local certificate at 4547, checked independently in Lean (kernel) and in Python.
   It shows that `P2` topologically generates `E₀(ℚ_4547)` and spans `E(ℚ_4547)/p`.
3. A Γ-structure argument for `ker(res) = W` that does not need `r ≠ 0`.

**Precise effect.**

* FIN: unchanged.
* Exceptional primary obligations at 2243, 4547 and 5843: still open. They acquire the
  receiver sufficient criterion `dim B_p ≤ 1` (or `p⁴ ∤ #Cl(O_{L_p}[1/p])`) for full primary
  vanishing. As a result the receiver route's residual set after a hypothetical cofinite bound
  no longer automatically contains them.
* ORDER9: unchanged.
* Q36: unchanged.

**Admissibility as a uniform mechanism: NO.** The receiver's first failed implication for the
uniform problem is W13's "It is not an independently bounded target", together with W21's
"proving receiver exactness does not prove this selected kernel has no spurious directions".
Both are **unchanged**. BFR is therefore not offered as a FIN mechanism. It is a scoped
extension of the domain of an existing arithmetic map, with the new local input listed above.
It is not a renamed `C_p`, it is not an equivalent criterion presented as a bound, and it is
not a formal proof that assumes the bound.

**Scope of old negatives preserved.** Nothing here contradicts W13–W21. The record's
good-prime claims about `R_p` remain correct for good non-anomalous `p`. The 4547
observation restricts their scope and is not a correction of an error in them, since they
were stated only for good `p`.

---

## B. Uniform candidate M1: Heegner–Kolyvagin over an auxiliary K with rank E^K = 1

* **Closest prior.** `sources/HISTORICAL_STOPS_AND_CORRECTIONS.md` entry **E12a-158**
  ("Heegner/Gross-Zagier: base Heegner point torsion; rank-2 GZ only over function fields") and
  entry **E13-112** (Kim arXiv:2609.15328, Kolyvagin conjecture at good ordinary p). Card W02
  covers the analogous Kato/Kurihara version.
* **Exact first failed implication.** "A nonzero Kolyvagin system (Kolyvagin's conjecture,
  W. Zhang / Kim) bounds the first nonzero level ν_p at 1 for all p outside a finite set."
  E12a-158 records: "Derived Kolyvagin classes give fixed-prime finiteness criteria … no
  cross-prime index."
* **What would change it.** A cross-prime bound on ν_p. No such input was found.
* **Verdict:** inadmissible; not developed.

## C. Uniform candidate M2: order-two vanishing of the p-adic L-function

* **Closest prior.** Release claim **B.1** (cyclotomic depth-two criterion), cards W24/W25,
  and **E12a-138** bridge type B1 ("p-adic Beilinson without finiteness, R_p != 0 …
  Schneider-type").
* **Exact first failed implication.** "`[T²]L_p(E,T)` is a p-adic unit for all good ordinary
  `p` outside a finite set." This is a cross-p nonvanishing of p-adic regulators/L-values
  (W25: "Hida control at a fixed p is not cross-p rigidity"). It also leaves the supersingular
  complement untouched (guide/01 §5).
* **Verdict:** inadmissible; not developed.

## D. Uniform candidate M3: the genus-two source curve and its Jacobian splitting

* **Object.** `C: U² = 1 − T² − 66020924T⁴ − 65074271436T⁶`. Its quotient by
  `(T,U) ↦ (−T,−U)` is `E` via `(T⁻², U/T³)`, which is the record's fixed source of the
  points `R_p`. Its quotient by `T ↦ −T` is
  `E2: Y² = X³ − 66020924X² + 65074271436X + 65074271436²`. So `Jac(C) ~ E × E2`. The
  exact `j`-invariants differ (computed with exact rationals), so `E2` is not a twist of `E`.
* **Closest prior.** `FORWARD_RECEIVER_RETAINED.md` §2, last paragraph ("The existence of this
  fixed source does not give a bound on the class groups"), and §3, equation (5)
  ("Hom_(G0)(V*epsilon_p,V)=0").
* **Exact first failed implication.** "Constraints coming from the fixed source family
  constrain the V-isotypic receiver head B_p." The source points `R_T` are anti-invariant and
  live in the `Vε` summand. `Hom_{G₀}(Vε, V) = 0`, and `E2[p]` is not `V`. So the new object
  (the splitting and `E2`) leaves this implication unchanged.
* **Verdict:** inadmissible; not developed. The only use of the `R_p` construction that this
  return pursues is the local one in A.
