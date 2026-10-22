# MATHEMATICAL_SPEC — A2: primary support, finite support, lattice content, order consequence

> **WARNING.** Formalizing WC proves only the implication from the stated witness-content antecedent.
> It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

## 1. Primary assembly
**Primary parts.** Let G be a torsion abelian group and G[p^∞] = {x : p^k x = 0 for some k}.
- **Decomposition (P2).** If n•x = 0 with n = ∏ q^{a_q}, choose integers u_q with Σ_q u_q·(n/q^{a_q}) = 1. Then
  x = Σ_q u_q(n/q^{a_q})•x, and each summand lies in G[q^∞].
- **Assembly (P3).** If G[p^∞] = 0 for primes p outside a finite set T, and G[p^∞] is finite for p ∈ T, then G is the image of
  the finite set ∏_{p∈T} G[p^∞] under summation, hence finite.

**Separation (P5, CM1, CM1′).** For torsion G:
- finite ⟺ (every primary part finite) ∧ (only finitely many nonzero);
- neither conjunct suffices:
  - ⨁_p ZMod p has every primary part finite and is infinite (CM1);
  - ℕ →₀ ZMod 2 has finite support {2} and is infinite (CM1′).

**Use in WC.** In WC (3) the vanishing outside S0 ∪ {p | A} comes from WC (2), and the finiteness comes from WC (1) and the
S0 hypothesis. P4 is exactly this assembly.

## 2. The depth ideal and finite prime support (Codex WC §1)
Let P be a set of primes and h : P → ℕ ∪ {∞}. Define J(P, h) = {a : v_p(a) ≥ h(p) ∀ p ∈ P}.
- J is an ideal (J1).
- J ≠ 0 iff every h(p) < ∞ and {p : h(p) > 0} is finite (J2).
- In that case J = (∏ p^{h(p)}) (J3).
- A fixed A ≠ 0 in J forces h(p) = 0 for p ∤ A: only primes dividing A exhibit positive depth (J4).

**Countermodel CM2.** The witness p² ∈ ZMod(p³) is nonzero at every p, but divisible by p, with depth 2. The constant depth 2
gives J = {0}. So a nonzero witness at every prime does NOT give finite support.

## 3. Lattice content (Codex FORMALIZABLE_GAPS A3; WC §4)
For z ∈ ℤⁿ let c = gcd of the coordinates (normalized, ≥ 0).
- z ∈ mℤⁿ ⟺ m ∣ c (L1). For z ≠ 0: z ∈ p^jℤⁿ ⟺ j ≤ v_p(c) (L5).
- c is invariant under GLₙ(ℤ) (L3), and z = c·z₀ with z₀ primitive (L4).
- **Finite version (L6).** The image of z in (ℤ/p^k)ⁿ lies in p^j(ℤ/p^k)ⁿ ⟺ p^{min(j,k)} ∣ c. The truncation case j > k is
  explicit.
- **Descent to ℤ (L7, Codex WC §4).** Suppose an arithmetic construction produced, outside a finite set B, witnesses of depth
  at most v_p(c) for a fixed nonzero z, and finite-depth witnesses on B. Then J ≠ 0.
  - The package proves only this implication.
  - Codex: "The missing input is the comparison with that primitive integral lattice."

## 4. Lemma B in the valuation model (Codex ALGEBRAIC_REDUCTION_LEMMAS §B)
For d ∈ ∏_p Z_p with each d_p ≠ 0, put v_p = v_p(d_p). Then d_p Z_p = p^{v_p} Z_p, so the following conditions depend only on
v, and they are equivalent:
- (1) v_p = 0 for almost all p;
- (2) some A ≠ 0 lies in every d_p Z_p (B1);
- (3) ∏_p Z_p/d_p Z_p ≅ ∏_p ZMod(p^{v_p}) is finite (B2).

**Countermodel CM3** (Codex's example: v = 0 at 2 and 5, v = 2 at 3, v = 2 for p ≥ 7). Every local cokernel is finite, the
product is infinite, and no nonzero integer lies in every local ideal. So perfectness and finite local defects over a
profinite product do not give finite support.

## 5. FIN does not determine the order (Codex ALGEBRAIC_REDUCTION_LEMMAS §H)
**H2.** Let G be finite abelian with |G[2^∞]| = 1, |G[3^∞]| = 9, |G[5^∞]| = 1, and every odd primary order a square. Then
|G| = 9t² with gcd(t, 30) = 1.
- The proof uses H0 (|G| = ∏ |G[p^∞]|) and the fact that |G[p^∞]| is a power of p.

**CM4.** (ZMod 3)² × (ZMod 7)² satisfies every hypothesis of H2 and has order 441. So "FIN ⇒ #Sha = 9" is a false inference.
Codex's abstract countermodel is (Z/3)² ⊕ (Z/7)².

**S1 (stretch).** A nondegenerate alternating pairing G × G → ZMod N forces |G| to be a square. The target must be cyclic:
S2 shows that the cross product on (ZMod 2)³ is nondegenerate and alternating on a group of order 8.
