# MATHEMATICAL_SPEC — A1: Codex's Theorem WC and the finite algebra under it

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

## 1. Context (not part of the formal task)
Codex's frontier attack (2026-09-19; verdict `BSD_FRONTIER_UNKNOWN`) studies an elliptic curve E/Q of rank two. It isolates a
sufficient condition for finiteness of Sha(E/Q) away from a finite exceptional set: **Theorem WC**.
- The implication is proved from published inputs (Ota 2015/2018; Selmer-group basics).
- Its **antecedent**, the existence of a nonzero integer in the witness ideal J_E, is **UNKNOWN**. No construction of it exists.

A cross-family review (Opus) added a caveat, which is recorded in the project handoff:
- WC is weaker than the older LINE hypothesis.
- That does *not* make its antecedent easier than FIN.
- At good ordinary primes, a Kurihara/Kim-type converse would turn Sha[p^∞] = 0 into exactly the witness condition, so on
  that tail the antecedent may be FIN restated in Ota's coordinates.
- This package formalizes only the implication, which remains valid either way.

## 2. Objects (Codex WC §1)
- **P.** S0 is a finite set of excluded primes (for the seed, {2,3,5,2243,4547,5843}); P is the set of primes not in S0.
- **Witnesses.** For p ∈ P, S runs over admissible conductors (squarefree products of good ℓ ∤ pN, ℓ ≡ 1 mod p,
  E(F_ℓ)[p] cyclic).
  - G_S = Gal(Q(μ_S)/Q), and I_S is the augmentation ideal of Z_p[G_S].
  - M(p,S) = I_S²/I_S³ is a finite p-primary module.
  - t(p,S) is the class of the Mazur–Tate element θ_S. Ota's theorem gives θ_S ∈ I_S² without any finiteness of Sha.
- **Depth.** For a nonzero t in a finite p-primary module M, depth_M(t) = max{j ≥ 0 : t ∈ p^j M}. Zero has no finite depth.
- **h_p** = min{depth(t(p,S)) : t(p,S) ≠ 0}, and ∞ if there is no nonzero witness.
- **J_E** = {a ∈ Z : v_p(a) ≥ h_p for every p ∈ P}, with v_p(0) = ∞. It is an ideal of Z. It is nonzero iff every h_p is finite
  and only finitely many are positive (package A2 formalizes this characterisation).

## 3. Theorem WC (Codex WC §2)
If J_E contains a nonzero integer A, then:
1. Sha[p^∞] is finite for every p ∈ P;
2. Sha[p^∞] = 0 for every p ∈ P with p ∤ A;
3. if the primary groups at the primes of S0 are finite, Sha is finite.

**Inputs of the proof:**
- (a) Ota Thm 5.17: θ_S ∈ I_S^{min(r_{p^∞}, p)}.
- (b) Selmer basics: infinite Sha[p^∞] ⇒ r_{p^∞} ≥ 3, because the rank is 2.
- (c) Ota Thm 1.5 (special case of 6.4): if t(p,S) ∉ p·M(p,S), then Sha[p] = 0.
- (d) Sha is torsion.

**Proof** (Codex):
- **(1)** h_p ≤ v_p(A) < ∞ gives an S with t(p,S) ≠ 0. If Sha[p^∞] were infinite, then r_{p^∞} ≥ 3 and min(r, p) ≥ 3 (as p ≥ 7).
  So θ_S ∈ I³, hence t(p,S) = 0, a contradiction.
- **(2)** p ∤ A gives h_p = 0. The attaining witness is not in pM, so (c) gives Sha[p] = 0. Every nonzero p-primary element has
  a nonzero multiple of order p, so Sha[p^∞] = 0.
- **(3)** Sha is the direct sum of its primary parts. All but finitely many of them vanish by (2), and the rest are finite. ∎

## 4. Lemma A (Codex ALGEBRAIC_REDUCTION_LEMMAS §A)
**Statement.** Let G be a group with g^e = 1 for all g, and let I be the augmentation ideal of R[G]. Then e·I^r ⊆ I^(r+1)
for r ≥ 1. Consequently:
- I^r/I^(r+1) is killed by e;
- over ℤ with G finite, it is finite and its rationalisation vanishes.

**Proof.**
- For g ∈ G put x = g − 1. Then (1 + x)^e = g^e = 1, so e·x = −Σ_{k≥2} C(e,k) x^k ∈ I².
- The elements g − 1 generate I, so e·I ⊆ I².
- Multiplying by I^(r−1) gives the claim.

Over Z_p with e = p^v·u (p ∤ u, so u is a unit), I^r/I^(r+1) is killed by p^v. This is target T3, the bounded exponent that
makes depths well defined.

## 5. Formal model (how the Lean statements encode §2–§4)
**T7 (abstract witness form).**
- M(p,S) is an abstract abelian group of bounded p-power exponent, and t(p,S) is an abstract element.
- The inputs (a)+(b), (c), (d) and the antecedent are hypotheses, with (a) in witness form: "r ≥ 3 ⇒ t = 0".

**T8 (group-ring form).**
- M(p,S) = `gr (Rp p) (G p S) 2`, where Rp p models Z_p and G p S models G_S.
- t(p,S) = `cls2 (θ p S)`.
- Input (a) appears exactly as printed: θ ∈ I^(min(r,p)).
- T3, T4, T10 and T11 connect the model to the abstract theorem T7.

## 6. False shortcuts (regression targets)
- **Uniform denominators do not bound witness content (T9a).** The source ℤ ∋ 1 has no denominator. The integral maps
  n ↦ p²n into ZMod(p³) produce nonzero witnesses of depth 2 at every prime, so h_p = 2 for all p and J = {0}.
- **"A nonzero witness at every p ⇒ finite support / J_E ≠ 0" is false (T9b).**
- **Non-vacuity (T12).** The hypotheses of T7 are jointly satisfiable, so T7 cannot be proved by exploiting contradictory
  hypotheses.
