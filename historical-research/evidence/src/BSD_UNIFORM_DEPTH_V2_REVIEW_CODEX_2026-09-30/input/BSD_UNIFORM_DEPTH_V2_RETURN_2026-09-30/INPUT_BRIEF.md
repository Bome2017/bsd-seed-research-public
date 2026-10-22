# Brief v2 (2026-09-30): a uniform depth bound for the Mazur–Tate elements of one rank-2 elliptic curve

(v2 replaces the 09-29 reviewed brief. The new state is in §3 (items B.20–B.22) and the new target is at the top of §5.)

## 1. The curve
E/Q: minimal model [0, −1, 0, −66020924, −65074271436], conductor N = 2³·3·2243·4547²·5843, non-CM,
rank E(Q) = 2, E(Q) ≅ Z² ⊕ Z/2 with basis P₁ = (−3031, 327384), P₂ = (−2394, 281520) (saturated; certified
2-descent). Reduction: 2 additive (c₂ = 2), 3 nonsplit multiplicative I₂ (a₃ = −1, c₃ = 2), 2243 split I₁ (c = 1),
4547 additive (c = 2), 5843 nonsplit I₂ (c = 2); Tam = 16. Two real components (Δ > 0), c∞ = 2. ρ̄_p is
surjective onto GL₂(F_p) for every odd p; ρ₃ is surjective onto GL₂(Z₃). Analytic rank 2 (certified),
q := L″(E,1)/(2·Ω·Reg) satisfies the certified interval 35.99427 < q < 36.00573; the much narrower estimate near 36 is evidence only, where Ω = ∫_{E(R)}|ω_E| = c∞·ω₁ = 2ω₁ and Reg is the determinant of the
Néron–Tate pairing in the BSD normalization. Ш(E/Q)[p^∞] = 0 is proved for all p ≤ 47 except p = 3, where
Ш[3^∞] ≅ (Z/3)². Whether Ш is finite is open.

## 2. Definitions (fix these conventions)
- Modular symbols: [r]⁺ := Re(λ_f(r))/ω₁, λ_f(r) = 2πi∫_{i∞}^{r} f(z)dz, ω₁ the least positive real period of the Néron lattice of the minimal model;
  [r]⁺ ∈ (1/1024)·Z for r ∈ Q.
- Auxiliary primes: for a prime p ∉ B* := {2, 3, 19, 59, 487, 2243, 4547, 5843}, let ℓ be a prime with ℓ ∤ pN,
  ℓ ≡ 1 (mod p), v_p(ℓ − 1) = 1, p ∤ #E(F_ℓ). Let g be the least primitive root mod ℓ and ind_g the discrete log.
- Depth-2 coefficient: C2(p,ℓ) := Σ_{a=1}^{ℓ−1} binom(ind_g(a) mod p, 2)·[a/ℓ]⁺ ∈ F_p. (It is the image of the
  Mazur–Tate element θ_ℓ = Σ_a [a/ℓ]⁺σ_a in I²/I³ of the order-p quotient of (Z/ℓ)^×, via σ_g − 1 ↦ T. On the
  domain of Ota's criterion, θ_ℓ ∈ I² follows from rank 2 and Ota's augmentation theorem, not from L(E,1) = 0 alone.)
- Tame height at ℓ: for Q ∈ E(Q) lying in the identity component at every bad prime and Q ≡ O (mod ℓ), write
  x(Q) = a/d², y(Q) = b/d³ in lowest terms; h_ℓ(Q) := ind_g(−a/b mod ℓ) mod p. With M := (exponent of the component
  groups)·(exponent of E(F_ℓ)) (prime to p), the pairing ⟨P,Q⟩_ℓ := (h_ℓ(P+Q) − h_ℓ(P) − h_ℓ(Q))/2 on M·E(Q) is
  bilinear mod p in the production normalization. The audited G2 comparison identifies the canonical biextension pairing with ±2 times this production form; keep that normalization when comparing constants. Tame regulator: R_{p,ℓ} := M^{−4}·det(⟨MP_i, MP_j⟩_ℓ) ∈ F_p.
- Scalar: w_{p,ℓ} := C2(p,ℓ) / ((a_ℓ − 2)·R_{p,ℓ}) ∈ F_p, defined when R_{p,ℓ} ≠ 0 and a_ℓ ≢ 2 (mod p).

## 3. What is proved
- (Ota, Thm 6.4; one-way) If p ∤ 6N·#E(F_p)·Tam, the p-adic image of ρ_p is all of GL₂(Z_p), p ≥ rank E(Q), and ℓ ≡ 1
  (mod p) is a good prime with E(F_ℓ)[p] cyclic, then C2(p,ℓ) ≠ 0 ⟹ Ш(E/Q)[p^∞] = 0. (For this E, every good p ≥ 7
  has p ∤ #E(F_p), since #E(F_p) is even and less than 2p.) Contrapositive: if Ш[p] ≠ 0 then C2(p,ℓ) = 0 for every such ℓ.
- (G2) For every p ∉ S₀ := {2, 3, 5, 2243, 4547, 5843} there are infinitely many ℓ with ℓ ≡ 1 + p (mod p²), ρ̄_p(Frob_ℓ) = −I (so a_ℓ ≡ −2, hence
  a_ℓ − 2 ≢ 0) and R_{p,ℓ} ≠ 0.
- (Theorem W; written proof, audited) For p ∉ B* and any two admissible ℓ, ℓ′: w_{p,ℓ} = w_{p,ℓ′} in F_p. Write w_p for
  the common value. No finiteness of Ш is assumed. If Ш[p] ≠ 0 then w_p = 0.
- (Candidate only; written, unaudited) a level-p^k construction has been proposed to yield compatible values w_p^∞. Do not use that arithmetic compatibility as a proved input. An arbitrary p-adic lift of w_p exists but has no such content.
- (B.20; imported preprints, independently reviewed) For EVERY good p ≥ 5, supersingular included (and 19, 59, 487),
  some Kurihara quantity δ_n is nonzero mod p. Sources: Castella–Liu–Wan, author-hosted revision of 2026-09-21,
  Theorem A (its condition (ram) holds via ℓ = 2243 ∥ N, since v_2243(Δ) = 1; no squarefree-level hypothesis);
  Castella–Sano arXiv:2601.14504, Theorems A and B and Corollary A.
- (B.21; derived) Let r_p = min{ν(n) : δ_n ≢ 0 mod p}. Then r_p = dim_{F_p} Sel_p(E/Q), which is even and ≥ 2, and
  r_p = 2 ⟺ Ш[p^∞] = 0. This uses Kim arXiv:2203.12159 Thm 1.8 (its Ш-independent clauses only), parity, and the
  split dual Kummer sequence with Nakayama.
- (B.22; derived at import grade) For a good prime p≥5, if K/Q is real cyclic of degree p with actual conductor m prime to pN (composite allowed), and χ is faithful,
  then v_{ζ_p−1}(χ(θ_K^MT)) < 4 ⟹ Ш[p^∞] = 0. Here θ_K^MT is the full Bullach–Honnor-normalized element
  (arXiv:2511.07203, Thm 1.4(b) and Def 2.2; total real period Ω⁺ = 2ω₁). The inequality must be strict: "≤ 4" fails.
- Consequence: w_p ≠ 0 ⟹ Ш[p^∞] = 0. So Ш[p^∞] = 0 for all p outside a finite set FOLLOWS FROM: there is a nonzero
  rational Z=a/b≠0 in lowest terms, with w_p = Z mod p outside a proved finite set S_Z. Exclude S_Z, B*∪{5}, every prime dividing ab, and any additional theorem-hypothesis exceptions. Denominator primes must be excluded to define reduction. This gives eventual primary vanishing, not finiteness at the remaining primes.

## 4. What is observed (not proved)
- w_p ≡ 288 (mod p) for p = 17, 19, 23, 29, 31, 37, 41, 43, 47 (the retained certificate row S.17-47 supplies one listed auxiliary ℓ for each p; any additional probes must be cited separately; 19 lies in B*, so
  there the ℓ-independence is observed, not proved).
- The conjectural value, from the refined Mazur–Tate conjecture (Burns–Kurihara–Sano Conj 2.3 form, which assumes Ш
  finite): w_p ≡ K_E := 4·c∞·#Ш·Tam/(#E(Q)_tors)² = 32·#Ш; with #Ш = 9 this is 288. The same formula gives 24 on a
  second rank-2 curve, y² = x(x² − 5tx + 4t(t+9)) at t = −36/5 (N = 2900, Tam = 12, tors 2, #Ш_an = 1), where the
  direct computation gives w_p = 24 for p = 7, …, 23.
- Elementary: if w_p = Z mod p for all p in the list above and Z ∈ Q, then either Z = 288 or the height of Z exceeds
  3.7·10⁹ (7.08·10¹⁰ if p = 19 is included).
- The two conjectural formulas for Z are: 32·#Ш (needs Ш finite to make sense: circular for the purpose here) and
  8q (using it as a rational constant requires a proof that this seed's q is rational, followed by the independent residue comparison). No universal literature nonexistence claim is intended.

## 5. The question
**The target (v2, corrected).** Prove that there is one finite set S containing {2,3,2243,4547,5843} such that, for every p outside S, at least one of the following holds:
- (i) a real cyclic degree-p field K/Q, at its actual conductor m prime to pN, and a faithful character χ satisfy v_{ζ_p−1}(χ(θ_K^MT))<4, with the full BH normalization. Composite conductors and p-dependent choices are allowed;
- (ii) for two distinct Kato primes q_1,q_2 (q_i∤Np, q_i≡1 mod p, a_{q_i}≡2 mod p), the mod-p Kurihara quantity δ_(q_1q_2) is a unit;
- (iii) an independent bound dim_{F_p} Sel_p(E/Q)≤3 holds.
For (ii), use Castella–Sano's total-real-period symbol Re(λ_f(a/n))/Ω_E^+ and δ_n=Σ_(a,n)=1 [a/n]^+∏_(q|n)ind_(g_q)(a) mod p. This symbol is half the production symbol in §2. Kato primes have trace +2 mod p; they are not the G2 trace −2 auxiliaries.

Under B.21, (ii) and (iii) are equivalent to each other and to Sha[p^∞]=0. B.22 proves (i) is sufficient; the records do not prove its converse. Different valid mechanisms may cover different prime subsets, provided their union leaves only a proved finite exceptional set.

Existence at unspecified length is already B.20. A bound in terms of the unknown minimum unit length is not an independent upper bound. Nonzero complex L-values alone supply no normalized valuation bound.

**Countermodel to an inference from primitivity alone:** the compact dual module X=Z_p²⊕(Z/p)² has four generators and Fitt₂=(p²), Fitt₃=(p), Fitt₄=Z_p, compatible with M_∞=0 and first unit index four. It is not Sel_p itself or an asserted elliptic-curve example. For the weaker character threshold ≤4, the group-ring model in the accepted review contains θ=t⁴ in its Fitting ideal while still requiring four base generators.

**Alternative architecture** (still admissible, not required):
Find a construction, or a theorem, that produces a single rational number Z ≠ 0 (or any p-independent object whose
p-adic image is w_p) with w_p ≡ Z (mod p) for all p outside an explicit finite set, WITHOUT assuming Ш finite and
WITHOUT assuming q ∈ Q. (A single nonzero rational constant is one sufficient mechanism, not a necessary one. A
uniform upper bound, or a direct theorem that the witnesses C2(p,ℓ) are nonzero for all p outside one finite set,
would serve equally well. "Without assuming" means exactly that: an independent PROOF of a statement equivalent to
finiteness of Ш, or of q ∈ Q, is admissible.) Any of the following would be progress:
- (a) a global object Y (defined once, not per prime) and an identity C2(p,ℓ) ≡ (a_ℓ − 2)·n_Y·R_{p,ℓ} (mod p) for
  all large p and admissible ℓ, with n_Y computed from Y;
- (b) first prove the arithmetic compatibility of the proposed w_p^∞ from §3, then prove that these values are the images of one nonzero rational number, by any mechanism (archimedean bound
  on a canonical lift, a global functional equation, an Euler-system norm relation across different p, …);
- (c) a structural obstruction: a proof that every identity of the form (a) whose right side is computed from
  modular symbols, tame data and E(Q) alone must have n_Y = 32·#Ш. That would be a theorem too. (Scope: such a
  constant is NOT equivalent to finiteness of Ш. A nonzero constant n gives Ш[p^∞] = 0 only for p ∉ S ∪ S₀ ∪ supp(n), with S
  the finite set in (a); it gives no finiteness at the excluded primes (59, 487, 2243, 4547, 5843 for this E). Conversely, finiteness of Ш alone
  does not produce the constant; that also needs the residue law x_{Q,p}·u_p ≡ n (mod p) for almost all p. A formula involving #Ш must state its finiteness hypothesis or independently prove finiteness; it cannot be used as an unconditional obstruction while that cardinality is undefined.)

**The most useful answer now** is a concrete mechanism for (i), (ii) or (iii) under the tests of §7:
p-dependent constructions are allowed, and so is the proved 3-primary input; it need not produce 288 or settle q.
It must show how excess Selmer torsion is excluded, and which infinite set of primes it covers. The closest framework
on record is the horizontal p-adic measures of Kriz–Nordentoft (arXiv:2310.20678, Thm 1.4 and Cor 5.20). Its
valuation bound depends on the length of a supplied mod-p unit Kurihara witness. The minimum such length is r_p, which
B.21 identifies with dim Sel_p, so Kriz–Nordentoft as printed cannot close the gap without a new input bounding r_p.

## 6. Previously screened approaches and their specific missing steps
Reopening rule: identify the earlier first failed mathematical step and the new input, map or inequality proposed to change it. The records below are scoped searches, not universal impossibility theorems.
- The screened uniform nonvanishing argument of Fearnley–Kisilevsky–Kuwata uses a nonzero normalized rank-zero L-value. That hypothesis fails here. The retained Kriz–Nordentoft implication transfers a supplied mod-p unit-witness length into a valuation bound; it does not bound the minimum length independently.
- The screened cyclotomic-height results did not supply the required almost-all-p nondegeneracy theorem for this seed. This is not a claim that no rank-two nondegeneracy theorem exists at any prime. Retained computations at 3,5,17 are finite-prime inputs.
- The tested elliptic-surface specialization and composite-modulus versions of Theorem W did not provide an independent upper bound. The Yun–Zhang formula concerns its function-field moduli problem; no applicable comparison for this seed was located in that screen. The screened plectic and auxiliary-cycle constructions likewise lacked the required comparison.
- In a first-derivative proposal whose L-function is L(E,s)H(s) with H holomorphic at 1, the rank-two zero makes that derivative vanish. This does not exclude derivatives in another variable, corrected quotients with justified cancellation, or other cycle constructions. Ordinary Heegner-point arguments must be stated under their actual Heegner and sign hypotheses; no assertion is made about every imaginary quadratic field.
- The screened Kato, Kurihara, derived-Heegner and higher-rank Euler-system routes did not supply the independent upper bound. Being indexed by p is not itself a defect, and does not justify asserting that every uniform consequence would require Sha finite.

## 7. Tests any proposed answer must pass, in this order
- K-S (paired-state test; apply it first, to the claimed ENDPOINT mechanism): a relation that holds equally with and
  without excess p-primary Selmer torsion cannot by itself force vanishing. A useful intermediate lemma may have no
  standalone FIN consequence; if so, state exactly what new input it supplies to the proposed complete proof.
- K-P (uniformity): for a proposed common rational scalar or common integral object, the object must be defined
  independently of p. For a DIRECT uniform theorem, p-dependent objects and auxiliary choices are allowed: prove that
  the construction and every needed estimate work for all p outside ONE fixed finite set (as G2 does). A fixed-prime
  or density-one theorem alone does not give finite support.
- K-F (no assumed conclusions): do not assume finiteness or the order of unknown primary parts of Ш, the desired
  witness nonvanishing, or q ∈ Q. Independently PROVED finite arithmetic is allowed, including the certified
  Ш[3^∞] ≅ (Z/3)² and the settled primes ≤ 47, as is an independently proved equivalent criterion. Identify the new
  arrow from these inputs to uniform control; inserting the number 9 into a proposed constant is not such an arrow.
- K-C: it must not reduce to one of the items in §6 without a new input that changes that item's stated reason.
- K-num (numerical compatibility): a proposed specialization identity must agree with every certified residue at the
  primes in its claimed domain (on E, and on the N = 2900 curve where it applies). The exact values 288 on E and 24 on
  the N = 2900 curve are conjectural normalization benchmarks (the refined Mazur–Tate constant); the finite
  observations do not force them. A rational candidate that differs from them is not rejected for that reason alone:
  it must pass the residue checks, and any exact-value exclusion needs an independent height bound or theorem. State
  separately whether the candidate constructs the predicted refined Mazur–Tate constant, or only another sufficient
  finite-support mechanism. An independent proof of a Ш-equivalent statement, or of rationality, is admissible;
  neither may be assumed.

## 8. Format requested
State every claim as THEOREM (with the printed source and its hypotheses), DERIVED (with the derivation), or
CONJECTURE. Give the first failing test for any candidate you reject. Do not estimate likelihoods.
