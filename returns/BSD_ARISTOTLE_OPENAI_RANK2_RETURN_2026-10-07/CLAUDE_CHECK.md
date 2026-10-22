# Independent check of the OpenAI rank-two return (Claude, Opus 5.5, 2026-10-07)


- **Package version.** Revision 1: the delta hash is 4233a966…, which is the revision-1 project.
- **Integrity.** MANIFEST: 51 of 52 entries verify. The only mismatch is the README banner; with it stripped the hash matches. New files: `research_return/EXCESS_OBSTRUCTION_RETURN.md`, `RequestProject/Continuation/ExcessObstruction.lean` and `ARISTOTLE_SUMMARY.md`. Nothing else changed.
- **Lean.** Compiles read-only in 56 s, exit 0, with no errors or warnings and no `sorry`, `native_decide` or `axiom`. All 27 declarations use subsets of {propext, Classical.choice, Quot.sound}; `dimChange` uses none.
- **Verdict: `EXCESS_OBSTRUCTION_PROVED`, with Stage B first failing at `GENERIC_RANK1_ONLY`. Confirmed.** Audit:
  - **Hostile audit of OpenAI (correct, and useful):**
    - `vertical:obstruction-span` FAILS as stated at χ = 1. The paired representations are isomorphic via the Weil pairing, so the commutator changes are symmetric forms and cannot span rectangular matrices (Lean).
    - Its commutator identity and `vertical:lift-test` transport to χ = 1.
    - `vertical:tests` (corank one, generic), `rd:det-switch`, `rd:away-two` and `rd:outer-bound` all need generic rank one or a simple zero.
  - **Stage A, Theorem A:** ker(S_p⁰ → Hom(𝒟_p^ℓ,𝔽_p)) = ℓ_p for p ∉ B*, supersingular p included. I checked:
    - **(A1)** via commutator differences over J_L. Points are p-divisible over L_p = ℚ(M_E[p]), so y(v) = y(w′) = 0.
    - **(A2)** via B(x,x) = −2e(x(v),x(w′)) ≠ 0, using Kummer disjointness and surjectivity onto E[p].
    - **The universal identity** ker(S → Hom(𝒟^W)) = W + ker 𝒪, which I re-derived through 𝒟^W = 𝒪(W)^⊥. It shows the fork always resolves *for* restriction: Stage A ⟺ ker 𝒪 ⊆ W.
    - **R4,** the kernel of restriction to ℚ(M_E[p]) is W, by inflation–restriction with a full Kummer block. This matches my corrected pre-check 3.
  - **Agreement with Codex (bb6ed896) on two levels.** The same commutator mechanism and the same symmetric-form output (Codex's (C)).
    - This run's 𝒪 is the `vertical:lift-test` invariant, a *necessary* lifting condition.
    - Codex's Morgan–Smith argument identifies it (up to k^×) with the full Cassels–Tate obstruction, whose left radical is exactly the liftable classes. So the two together give Stage A in the full deformation sense, subject to the Morgan–Smith audit targets.
  - **"Reformulation of the receiver kernel; no bound"** is accepted. It agrees with Codex and with lanes A–D (Lane C Lemma 5 shape).
  - **Stage B:**
    - Lemma B1: keeping generic H¹ = W forces loc_γ(W) = 0, so the unit-volume mechanism of `rd:det-switch` has nothing to act on.
    - Lemma B2: for one plane, the Jordan exponents of a self-adjoint φ give a dimension drop of #{a<0} − #{a>0} and a Δ_W shift of |Σa|. So a drop by 2 forces |Δv| ≥ 2. Both lemmas are linear algebra and checked.
    - The two-plane escape, with exponents (1,1,1,−3), is correct arithmetic, but no classes are supplied.
    - "No DVR carrier" is HEURISTIC: over ℤ_p it needs FIN at p and the local planes are torsion (Hasse); the cyclotomic family has generic H¹ = 0 and is wild; tame families have generic rank ≤ 1 per `vertical:tests`.
  - **Pre-checks:**
    - PRE-CHECK 3 is corrected: primes split in L_p are not admissible (Frob = 1, so the local complex is not acyclic).
    - PRE-CHECK 4 (TAME_LAW_G1) was not tested.
    - Supersingular p is covered by Stage A.

FIN, ORDER9 and Q36 are unchanged.
