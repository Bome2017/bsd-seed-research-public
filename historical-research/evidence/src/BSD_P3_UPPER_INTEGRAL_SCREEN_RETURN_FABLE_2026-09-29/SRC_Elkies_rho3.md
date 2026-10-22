# SRC — hypothesis check: is ρ₃ : G_Q → GL₂(Z₃) surjective for the seed? (needed by SW 7.3's
# hypothesis and by Kato 12.5(4)'s (12.5.2) read literally)
## Source: N. D. Elkies, "Elliptic curves with 3-adic Galois representation surjective mod 3 but not
## mod 9", arXiv:math/0612734v1. PREPRINT copy (sources/Elkies_math0612734.pdf). Read: abstract,
## §0 (El l.1-60), §2 end and §3 (page 5, read from the rendered page image, not only pdftotext).
- Abstract: X9 of genus 0 parametrizes E with ρ₃ "not surjective mod 9 but generically surjective
  mod 3"; "for every x ∈ P¹(Q), other than the two rational solutions of f(x) = 0, the elliptic curves
  with j-invariant f(x) have ρ₃ surjective mod 3 but not mod 9". §3 (p.5): if ρ₃ is surjective mod 3
  and j = f(x), the image mod 9 is (conjugate to) the proper subgroup G′.
- **The printed f(x) has a sign typo.** As printed: f(x) = −3⁷(x²−1)³(x⁶+3x⁵+6x⁴+x³−3x²+12x+16)³
  (2x³+3x²−3x−5)/(x³−3x−1)⁹ = 1728 − 3³A²B²(2x³−3x²+4)/(x³−3x−1)⁹. PARI: the two printed forms are
  NOT equal; with "+" in both places (f = +3⁷(…)/(…) = 1728 + 3³A²B²(…)/(…)) they are identically equal.
  Elkies's own examples (El l.39) j = 4374, 419904, −44789760 are hit by the "+" form (x = ∞, and two
  rational x) and by NONE of them with the printed "−" form. SEED_DATA's recalled formula carried the
  printed "−". Conclusion: use the "+" form. (Discrepancy reported; not an erratum claim.)
## Computation (checks_elkies_rho3.gp; PARI 2.17, run040 env, <0.1 s, 1 process)
- Seed j = 2⁴·3⁻²·43³·1013³·2243⁻¹·5843⁻² (matches SEED_DATA). For BOTH signs, numerator − j·denominator
  (degree 27) has no rational root (nfroots = []), and j ≠ f(∞) = ±4374. So j ∉ f(P¹(Q)).
- Also: j is not a cube; E has no rational 3-isogeny (isogeny class {1,2}); ρ̄₃ = GL₂(F₃) (SEED_DATA).
## Conclusion and grade
- Given ρ̄₃ surjective, if ρ₃ were not surjective its image mod 9 would be a proper subgroup surjecting
  onto GL₂(F₃), i.e. (up to conjugacy) inside Elkies's G′, so j ∈ f(P¹(Q)); contradiction. Hence ρ₃ is
  SURJECTIVE onto GL₂(Z₃), and ρ₃(G_{Q(μ3∞)}) = SL₂(Z₃) ⊇ SL₂(Z₃), i.e. Kato's (12.5.2) holds.
- Grade: COMPUTED, relative to (i) Elkies's X9 formula (read at source, sign corrected by two checks)
  and (ii) the completeness facts "mod 9 surjective ⇒ 3-adically surjective" and "every proper subgroup
  of GL₂(Z/9) with full det surjecting onto GL₂(F₃) lies in a conjugate of G′" — SECONDARY (Elkies §0
  attributes the setting to Serre; RSZB 2106.11141 Thm 1.1.6 is the general classification; its
  3-adic tables were not read). This upgrades SEED_DATA's "UNCHECKED at source" to this grade.
