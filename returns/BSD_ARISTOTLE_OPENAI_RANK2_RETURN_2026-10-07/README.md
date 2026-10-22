# Aristotle OpenAI rank-two mechanism run (revision 1): canonical return (2026-10-07)

**Status: `EXCESS_OBSTRUCTION_PROVED`. Stage B first fails at `GENERIC_RANK1_ONLY`. Stage C was not entered.**

**Stage A (PROVED; Lean skeleton).** For p ∉ B*, supersingular p included, tame commutator-difference directions at Frobenius-acyclic primes γ ≡ 1 (mod p) obstruct exactly the strict classes outside ℓ_p = W_p ∩ S_p⁰.
- It is a reformulation of the receiver kernel. It gives no bound on Ш[p].
- It agrees with Codex's independent Stage-A derivation (lab bb6ed896). Codex's Morgan–Smith step makes this run's lift-test invariant the full obstruction.

**Hostile audit of the OpenAI lemmas.**
- `vertical:obstruction-span` fails as stated at the untwisted point: the Weil pairing makes the paired representations isomorphic, so only symmetric forms arise.
- `vertical:tests`, `rd:det-switch`, `rd:away-two` and `rd:outer-bound` need generic rank one or a simple zero.

**Stage B.**
- A single-prime switch cannot both drop the special fibre by two and preserve Δ_W = (P₁∧P₂)⊗(P₁^∨∧P₂^∨). This is Lean linear algebra.
- A two-plane switch with Jordan exponents (1,1,1,−3) escapes, but no classes realizing it are supplied.
- No DVR family carrying generic H¹ = ⟨P₁,P₂⟩ is known (HEURISTIC).

**Files.**
- `EXCESS_OBSTRUCTION_RETURN.md`: the full return.
- `RequestProject/Continuation/ExcessObstruction.lean`: 27 declarations on the standard axioms.
- `ARISTOTLE_SUMMARY.md`.
- `CLAUDE_CHECK.md`.

The banner is excluded. The archive is `../archives/ed24e1f2-00e9-49d9-b79d-7054609c8a8d-aristotle.tar.gz`.

FIN, ORDER9 and Q36 are unchanged.
