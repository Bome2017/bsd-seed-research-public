# Cross-connections: what the whole record shows that no single record states

This file is the builder's synthesis, written after the claim index. Items marked **[record]** restate something that is already in the cited records. Items marked **[builder]** are observations made while consolidating; they are written as checkable statements, and none is promoted into the claim index as a theorem. The auditor should test the [builder] items first.

## 1. Shared dependencies: apparently separate results resting on one input

| shared input | results that depend on it | consequence |
|---|---|---|
| **Skinner 2016, Theorem A, as published** (internal SU provenance open at the Euler-removal interface) | the second route to S.3 (its primary support is route K, S.3K), B.6 (2243 route), B.7 (5843 route) | **[builder]** Both multiplicative bad-prime routes, and the second route to the one component carrying all of Sha's known content, rest on the same imported theorem. An actual defect in the imported theorem would affect these chains together. The project's unreconstructed internal interface is not evidence of a defect in the published theorem. The good-prime results S.5–S.13 do not use it: they rest on Kato's divisibility, which excludes p \| N. The bad-prime feasibility record already notes that "the R2-type seam recurs" at p \| N **[record]**. |
| **Kato's divisibility + SW Thm 6.1, good ordinary clause (Schneider, Perrin-Riou)** | S.5, S.7, S.11, S.13, B.1 | **[builder]** An independent trust base from the one above. The good-prime vanishing results would survive a problem in Skinner's multiplicative theorem. |
| **The certified coefficient corpus** (producer + independent integer verifier `wverify`) **and the Arb engine lineage** (`arbcore`) | R.3, S.3–S.13, K.1, K.2, X.6, and the future B.6 / B.7 | **[builder]** Every analytic certificate evaluates an exponentially weighted twisted L-series from overlapping coefficient corpora using one verifier lineage. The independent replays share the raw a_p bytes (for example the K.2 small-T replay). **So a correctness review of `wverify.c` and its witness scheme is the single highest-leverage audit item on the computational side.** |
| **The proved symbol lattice (1/1024)Z at the rational unitary cusps used here** (A.4) | S.3, S.5, S.7, S.11, S.13, B.6 | Interval uniqueness is not a check of lattice membership. A wrong denominator, including a power of 2, can silently produce a wrong result. The Manin and cusp arguments are load-bearing. |
| **Rank and the full Mordell-Weil basis** (R.1) | the real regulator; point-basis height calculations | Zywina supplies the rank/2-descent input, not the full integral basis. The separate Lane 3 global saturation certificate has now been restored and replayed. Its computed index bound is 2; saturation has index 1. |


## 2. One result supplying another argument's hypothesis

* **D5 + D2 + the ℒ-invariant complete the theory side of the 2243 route [builder, from records].**
  * Master §3 (2026-09-21) lists the split case as needing "its stated nonzero ℒ-invariant input". That input is now supplied twice, independently:
    * ℓ_γ ≡ 1799 (mod 2243), computed in the D5 certificate's §3 without PARI;
    * the same value in the cross-family check's `LOCAL_L_INVARIANT.json`.
  * D2 is discharged at source level, and D5 was certified on 2026-09-23.
  * The 2243 implication now has the same logical shape as the retained p = 3 proof: finiteness first, an independent nondegenerate height, then Jones's forward theorem.
  * What remains is imported theorems (D1, D3, D6, D7), the engine (D8, with defect F4 open), and the uncomputed coefficient.
* **The A3 argument bypasses the ordinary lane's unreplayed steps [record; builder emphasis].**
  * The frozen ordinary bridge (B.3) rests on steps the project has not replayed: the BLV↔BD module identification, BD 2.18(5)/2.23/Lemma 3.1, and the odd-p descent.
  * The A3 argument (B.4) runs verbatim at ordinary p with ε = ∅, uses none of those steps (nor the D=-7 certificate), and has a Lean-checked algebraic core.
  * **[builder]** Promoting the A3 route to the canonical ordinary proof would remove the least-verified links from B.3. The records leave this substitution to the user (K.6).
* **The compression attempt supplies a free check for any future 2243 run [record].**
  * c₁ ≡ 0 (mod 2243) is forced by the order ≥ 3 of the p-adic L-function (D1, D2, D7), but not by the Atkin–Lehner pairing.
  * An output with c₁ ≢ 0 would expose an error. No error-detection probability follows without a distribution model for incorrect output.

## 3. Which sufficient witnesses can actually be evaluated on this curve

| witness | where it applies | evaluable now? |
|---|---|---|
| C_p = [T²]L_p (B.1) | good ordinary p ≥ 5 | **yes**, with the existing engine; it was used at 5, 7, 11, 13. The cost grows roughly with p²√N. **At p = 17 it is structurally zero**: the normalized regulator has valuation one, so depth three is needed **[record: D_primes §2]**; 17 was settled by the singleton coefficient instead (S.17-47). |
| C_2(p,l), singleton (S.17-47) | good p ≥ 5, ordinary or supersingular | **yes**, with the existing engine: used at 17, 19, 23, 29, 31, 37, 41, 43, 47, one auxiliary l each |
| Criterion SS coefficient (B.2) | good supersingular p | **yes, in principle**: about 270 / 460 CPU-hours at 23 / 29 (not run) |
| K for 2243, depth-two coefficient for 5843 (B.6, B.7) | the multiplicative bad primes | **not production-ready** (the recorded restart defect is open); modeled cost: about 1.1·10⁵ and 6.3·10⁵ CPU-hours (parked) |
| C_2(p,l), singleton at the bad primes (B.18) | 2243, 4547, 5843 | **not run**: modeled at about 2.4·10⁴–7.4·10⁴ core-hours, and the current evaluator's checkpoint files need 0.8–5.8 TB (X.16) |
| M₂(p), c₂(p) (B.3–B.5) | good p ≥ 5, p ∤ 7N | **[builder] no evaluator supplied by this project.** The eigenform φ_E lives on the definite Shimura set of the quaternion algebra ramified at {3, 2243, 5843, ∞}, with Eichler level N⁺ = 2³·4547². Its mass is ∏(q−1)·ψ(N⁺)/12 ≈ **5.4·10¹⁴**. Full enumeration is unaffordable here; no compressed evaluator is supplied. This is not a lower bound for all algorithms. The anticyclotomic bridges therefore settle **no individual prime** at present; they remain conditional single-prime tests as well as possible inputs to a uniform theorem. |
| h_p (B.9) | good ordinary p outside S0 | a witness of Kurihara-number type; it is equivalent to the vanishing, so it earns no reduction |
| I₃(p) over Q(√−23) (B.13) | regime (P) primes | no evaluation method **[record]** |
| 4547 witness (B.8) | 4547 | no: the smallest Kolyvagin pair is about 8.1·10¹⁵ **[record]**; see also B.18 |

**[builder]** Per-prime progress on this curve has come from the cyclotomic and singleton witnesses, and could come from the bad-prime certificates; each is finite and each is costly. Progress on FIN needs a uniform statement, and none of the evaluable witnesses is uniform. This is the frontier's PRIME_UNIFORM_INTEGRAL_WITNESS question (O.4), seen from the computational side.

## 4. Similar requirements, without an identified arithmetic comparison

* The Stark lane over Q(√−23) (rank 3; B.13, X.12) and the definite-theta lane over Q(√−7) (rank 2; B.3–B.5) both lack an evaluation of the designated witness. No theorem identifies these arithmetic objects. Neither has a prime-independent integral object whose reductions govern the p-adic witness.
* In analytic rank one the object is the Heegner index, which works because the Heegner point has conductor one. Over Q(√−23) the corresponding index is infinite, since rank E(K) = 3.
* The definite lane uses Gross points of conductor p², indexed by p by construction.
* **[builder]** The 2243 route has the same shape: a single depth-two coefficient at a single prime.

## 5. The endpoint arithmetic, assembled

* Given FIN, #Sha = 9t² with every prime factor of t at least 53; the next possible order is 25,281 = 9·53² (S.FIN, using S.17-47).
* Any nonzero bad-prime component contributes at least 2243² to the order, so it cannot hide under the threshold. It still has to be excluded for ORDER9.
* **[builder]** In the uniform-bound form (S.U), a single bound #Sha[n] < 2601 for all n would settle FIN and ORDER9 together, including all bad and supersingular primes. This is a logical equivalence with FIN and ORDER9; it supplies no independent difficulty reduction.
* The scalar side (q = 36) is disjoint from all of this except through the common-scalar formulation (Q.3). The finite local data tested in X.11 do not determine q without additional global arithmetic input.

## 6. Does this starting point offer an advantage? (for the manuscript's final section)

**Advantages [builder assessment]:**
* The rank and analytic rank are certified.
* There is an explicit basis with a certified regulator.
* q is certified within 0.006 of 36.
* The primary components at 2, 3, 5, 7, 11, 13 are settled, with the only nonzero one explicit, (Z/3)².
* Certified auxiliary quadratic fields exist in both rank regimes: rank 2 over Q(√−7) and rank 3 over Q(√−23).
* A Lean-checked conditional bridge covers every good prime p ≥ 5, p ∤ 7N.
* A large, documented set of scoped obstructions shows which mechanisms fail and where.

**Disadvantages [builder assessment]:**
* The conductor 6.5·10¹⁵ makes naive full modular-symbol or quaternionic spaces have scale 10¹⁴–10¹⁶.
* The conductor is not squarefree (2³, 4547²), which excludes several published theorems in their printed form.
* The additive, potentially supersingular prime 4547 has no executable retained certificate; the two-prime Kurihara sufficient implication remains.
* The split multiplicative prime 2243 carries an exceptional zero (handled, at computational cost).
* The one nonzero primary component rests on route K (S.3K), a written derivation read by model readers but not by a human referee; Skinner's theorem, with two steps not established for this curve, is its second route.

**Whether this balance makes the curve a good test case for rank-two BSD methods is a question for outside experts.** The package is organized so they can answer it.

## First-review dependency repair

The legacy coefficient verifier accepts repeated prime factors, and a concrete wrong point count was accepted. `review/repairs/wverify_distinct.c` repairs that check. A supplemental scan verified the omitted conditions on every retained witness file and matched retained hashes; it did not rerun the original group arithmetic. See `review/FIRST_REVIEW.md`.
