# FIXED_E5_DEGREE2_TWIST_ATTACK_001 — report (2026-09-17)

**Return: UNKNOWN_NO_WITNESS.** Gate G is parked.

What the label means here:
- No witness was found.
- No proof excludes the whole degree-two class (genus 0 and genus 1 together).
- The **genus-0 half is closed by a theorem** (§2).
- The genus-1 half is cut down to explicit necessary conditions (§3). Those conditions still leave infinitely many candidate D, and there is no finite degree range for genus 1 (§1.4).
- No coefficient search was run in either phase.

**Scope.** Private directory. The shared ledger, seals and memory were not touched.

**Inputs.** The retained facts were not reopened:
- E₀ = 389a1.
- E: y² = x³ + a(t)x + b(t) is the Rubin–Silverberg family over Q(t), in Fable's transcription. The copy in `src/` has the same sha256, `7bfe18ef…`.
- The family is geometrically Shioda's S(5), with E(Q̄(t)) = E[5] ≅ (Z/5)².

**Compute.** Under 1 CPU-s of the 300 allowed, one process, one thread:
- `runs/gen_coeffs.py`: 0.8 s.
- `runs/phase0.gp`: under 0.1 s. Its output is in `runs/phase0.out`.

## 1. Phase 0 — geometry and bounds

**1.1 Base family** (recomputed, `[P0.1–P0.4]`).
- deg a = 20 and deg b = 30.
- Δ = −16(4a³ + 27b²) = const·g⁵, with **g irreducible over Q of degree 12**.
- Res(g, a) ≠ 0 and Res(g, b) ≠ 0, so the only bad fibres are the twelve I₅ fibres at the roots of g.
- deg Δ = 60 = 12χ, so the fibre at ∞ is smooth.
- j(E_0) = 1404928/389.

New fact used below: because g is irreducible, **G_Q acts transitively on the 12 cusps.**

**1.2 Exact minimal model of the twist.** For squarefree D ∈ Q[t], write X = Dx and Y = D²y:

    E^D :  Y² = X³ + a(t)D(t)²·X + b(t)D(t)³.

- **At a root of D:**
  - v(aD²) = 2 + v(a), v(bD³) = 3 + v(b) and v(Δ') = 6, because D is coprime to Δ.
  - a and b do not both vanish there.
  - So the model is minimal and the fibre is **I₀\***.
- **At ∞:** smooth if deg D is even; I₀\* if deg D is odd.
- **At the cusps:** the twist is unramified, so the fibres stay I₅.

| case | deg D | branch points n_B | fibres | χ | e | b₂ | p_g | h^{1,1} |
|---|---|---|---|---|---|---|---|---|
| A (genus 0) | 1 or 2 | 2 | 12 I₅ + 2 I₀\* | 6 | 72 | 70 | 5 | 60 |
| B (genus 1) | 3 or 4 | 4 | 12 I₅ + 4 I₀\* | 7 | 84 | 82 | 6 | 70 |

These fibre types were checked on seven sample D (`[P0.5]`).

**1.3 Branch points at cusps are impossible over Q.** A root of D ∈ Q[t] with deg D ≤ 11 has degree at most 11 over Q. Every cusp has degree 12, because g is irreducible. Over Q̄, a branch point at a cusp would turn that I₅ (A₄) into I₅\* (D₉), instead of adding a separate I₀\* (D₄) at a smooth fibre. Each such point raises the trivial-lattice rank by one, leaving room for rank at most 1 (one cusp) or 0 (two cusps). This is the rank-budget lemma's "cusp ramification gives no free rank".

**1.4 Shioda–Tate, NS discriminant, heights.**

*Trivial lattice.* L = U ⊕ A₄¹² ⊕ D₄^{n_B}.
- Rank 58 (case A) or 66 (case B).
- Maximum geometric Mordell–Weil rank: 2 (A) or 4 (B).
- disc(L) = (Z/5)¹² ⊕ (Z/2)^{2n_B}, using det A₄ = 5 and det D₄ = 4 (`[P0.6]`).

*E^D(Q̄(t)) is torsion-free.*
- 2-torsion: the cubic stays irreducible over Q̄(t).
- 5-torsion: E^D[5] = E[5] ⊗ χ_D has no G_{Q̄(t)}-invariants.
- Order p ∉ {2, 5}: such a section meets only identity components and misses O. Its height would then be 2χ > 0, which is impossible for torsion.

So L is primitive in NS, and the gluing formalism applies.

*Case A: the lattice constraint is tight.*
- L^⊥ ⊂ H²(S, Z) has rank 70 − 58 = 12, which equals ℓ₅(disc L) = 12.
- The transcendental lattice T has rank 12 − r. Since NS is primitive in the unimodular H², ℓ₅(disc NS) = ℓ₅(disc T) ≤ 12 − r.
- Gluing along L gives ℓ₅(disc NS) ≥ 12 − ℓ₅(H), where H is the image of MW in disc(L). The 5-part of H is the image of the component map MW → ⊕_v Z/5.
- Hence ℓ₅(H) = r: **the component map MW/5 → (Z/5)¹² is injective.**
- §2 gives an independent proof of the same statement.

*Case B: no constraint.* rank L^⊥ − ℓ₅(disc L) = 16 − 12 = 4, and the lattice gives nothing (`[P0.7]`). The defect 4 = 4·genus(C) is the Hom(J_C[5], E₀[5]) term of §3.

*Heights.* With c_v ∈ Z/5 the component met at cusp v:

    h(P) = 2χ + 2(P·O) − Σ_cusps c_v(5 − c_v)/5 − #{I₀* fibres where P is off the identity component}.

For an integral section, X ∈ Q[t] with deg X ≤ 2χ and deg Y ≤ 3χ. Poles of X, and deg X > 2χ, add to P·O.
- **Case A:** no range is needed, because §2 proves that no Q-rational rank-2 pair exists.
- **Case B:** there are only lower bounds (§3). det(MW lattice) = |disc T| / (5¹²·4^{n_B}) is not constrained by anything available. So Phase-0 data gives no finite height or degree range, and **no coefficient search was started**, as the spec requires.

## 2. Phase 1 — genus 0: THEOREM (no degree-two genus-zero solution over Q)

**Lemma 1 (component injectivity).** Let D ∈ Q̄[t] be squarefree with deg D ∈ {1, 2} and no root at a cusp. Then the component map

    c : E^D(Q̄(t))/5 → ⊕_{12 cusps} Φ_v ⊗ F₅

is injective.

*Proof (Selmer).* Put K = Q̄(t) and M = E^D[5] = E[5] ⊗ χ_D.
- E[5] is constant, because all 25 points are sections of S(5). So M is unramified except at the two branch points t₁, t₂, where inertia acts by −1.
- Take P with c(P) = 0 and check its local Kummer classes δ(P)_v:
  - **Good places:** E^D(K_v) is 5-divisible. The residue field Q̄ is algebraically closed, and the formal group is uniquely divisible.
  - **Cusps:** χ_D is unramified at v and the residue field is algebraically closed, so E^D ≅ E over K_v, with split I₅ reduction. P lies in the identity component, which is 5-divisible. So δ(P)_v = 0.
  - **Branch points:** H¹(K_v, M) = M/(−2)M = 0.
- So δ(P) is unramified outside {t₁, t₂}. Therefore δ(P) ∈ H¹(π₁(P¹ ∖ {t₁, t₂}), M) = H¹(Ẑ(1), M) = M/(−2)M = 0.
- By Kummer injectivity, P ∈ 5·E^D(K). ∎

A second, independent proof is the discriminant-length argument of §1.4.

**Theorem 2.** For every squarefree D ∈ Q[t] with deg D ∈ {1, 2}:

    rank E^D(Q(t)) ≤ 1,   hence   rank E(Q(t, √D)) = rank E(Q(t)) + rank E^D(Q(t)) ≤ 1.

So no degree-two, genus-zero base change of the 389a1 Rubin–Silverberg family carries two independent Q-rational sections of the natural pulled-back family. This holds whether or not u² = D(t) has a rational point.

*Proof.*
1. Let M = E^D(Q̄(t)). It is torsion-free (§1.4), so M^{G_Q} = E^D(Q(t)) is saturated in M, and M^{G_Q}/5 ↪ M/5.
2. By §1.3, D has no root at a cusp. So Lemma 1 gives M/5 ↪ ⊕_v Φ_v ⊗ F₅.
3. The map c is G_Q-equivariant, because the Néron model is defined over Q. So c(P) is a G_Q-invariant vector for every P ∈ M^{G_Q}.
4. G_Q is transitive on the cusps (§1.1). An invariant vector is therefore determined by its coordinate at one cusp v₀, which lies in Φ_{v₀} ⊗ F₅ ≅ F₅.
5. Hence rank E^D(Q(t)) = dim M^{G_Q}/5 ≤ 1. ∎

**Refinement (rank 1 — not needed for the verdict, not evaluated).**
- Rank 1 requires G_{Q(v₀)} to fix a nonzero c_{v₀}(P). That means E^D is split multiplicative at v₀ over Q(v₀) = Q[t]/(g).
- Equivalently, −2a(v₀)b(v₀)D(v₀) ∈ Q(v₀)^{×2}. (The node is at x₀ = −3B/2A, with tangent-slope square 3x₀ ≡ −2AB mod squares.)
- Such a section meets components ±k, for one fixed k, at all 12 cusps. Its height is

      h = 12 + 2(P·O) − 12·k(5 − k)/5 − (0, 1 or 2).

- Even a rank-1 witness here could not be upgraded to rank 2 inside genus 0.

**Dependencies of Theorem 2.**
- g irreducible over Q (computed).
- E[5] constant over Q̄(t) (retained Shioda fact).
- The fibre types of §1.2.

It uses nothing else about a(t) and b(t). The Q-structure E[5] ≅ E₀[5] is not needed for genus 0.

## 3. Phase 2 — genus 1: kill-first reduction

Phase 2 was entered under condition (a): Phase 1 proved a complete negative theorem for deg D ≤ 2.

**Set-up.** Take deg D ∈ {3, 4}, C: u² = D(t) of genus 1, and M = E^D[5].
- By RS Thm 5.1, E[5] ≅ E₀[5] ⊗ Q(t). Using this, G_Q-equivariantly:

      H¹(P¹_Q̄, j_*M) = E₀[5] ⊗ H¹(C_Q̄, F₅) ≅ Hom(J_C[5], E₀[5])      (dimension 4 = 2n_B − 4).

- The proof of Lemma 1 now gives an exact sequence of G_Q-modules:

      0 → Hom(J_C[5], E₀[5]) → Sel₅(E^D/Q̄(t)) → ⊕_v Φ_v ⊗ F₅.

  Classes with zero component data are exactly the unramified ones. This is the same defect of 4 that the lattice shows in §1.4.

**Proposition 3.** For squarefree D ∈ Q[t] with deg D ∈ {3, 4}:

    rank E^D(Q(t)) ≤ 1 + dim Hom_{G_Q}(J_C[5], E₀[5]) ≤ 2.

*Why.* E^D(Q(t))/5 injects into Sel^{G_Q}. The invariants of the sub have dimension ≤ 1: ρ̄_{E₀,5} is surjective, so End_{G_Q} E₀[5] = F₅ and any nonzero G_Q-map J_C[5] → E₀[5] is an isomorphism. The invariants of the quotient also have dimension ≤ 1, since there is one cusp orbit.

**Rank 2 requires all of the following:**
1. J_C[5] ≅ E₀[5] as G_Q-modules. That is, J_C is 5-congruent to 389a1: in the Rubin–Silverberg family (symplectic) or in Fisher's X_{E₀}(5, 2) (anti-symplectic).
2. The twisted cusp fibre is split over Q(v₀): −2a(v₀)b(v₀)D(v₀) is a square in Q(v₀).
3. There is a Q-rational section P₀ ∉ 5·MW that passes through the identity component at all 12 cusps, whose Kummer class spans Hom_{G_Q}(J_C[5], E₀[5]). Its height is h(P₀) = 14 + 2(P₀·O) − k₀ ≥ 10.
4. There is a second Q-rational section P₁ that meets components ±k, for one fixed k ≠ 0, at all 12 cusps.
5. For Gate G itself, C(Q) must be infinite, so C ≅ J_C with positive rank.

**These conditions do not empty the class.**
- Example: C = 389a1 itself, with D₀(t) = 4t³ + 4t² − 8t + 1 (from (2y+1)² = 4x³ + 4x² − 8x + 1). It satisfies conditions 1 and 5.
- So does every positive-rank curve in the 5-congruence class, composed with any change of t by PGL₂(Q).

**What is left open.** Deciding conditions 3 and 4 is a Noether–Lefschetz question: does the Selmer class spanning Hom_{G_Q}(J_C[5], E₀[5]) die in Sha(E^D/Q̄(t)) ≅ Br? The candidate D form a 3-parameter family. The expected dimension is negative (p_g = 6 conditions per class). §1.4 gives no finite range. Any search would therefore be a blind ansatz, and none was run.

**Genus 1 is not closed.**

## 4. Candidate acceptance checklist

There is no candidate. The list (squarefree D, exact model, identities, non-torsion, height determinant, rational point on the cover, natural fibration) was not exercised.

## 5. Verdict and handling

    UNKNOWN_NO_WITNESS
      genus 0 (deg D in {1,2}): CLOSED BY THEOREM - rank E(Q(t,sqrt D)) <= 1 for every such D (Theorem 2)
      genus 1 (deg D in {3,4}): REDUCED, NOT CLOSED - rank <= 2; rank 2 needs J_C[5] ~ E0[5] as G_Q-modules
                                plus conditions 2-4 (Prop. 3); no finite height range; no search run
      no witness of rank 1 or 2

- **Gate G** is parked operationally. FIXED_E5_GATE_G stays OPERATIONALLY_OBSTRUCTED; NONEXISTENCE_OPEN.
- **Per the hard-stop rules:**
  - no escalation to base-change degree > 2, higher genus, wider ansätze or literature searches;
  - Gate S not entered;
  - next lane: specialization-specific 5-arithmetic.
- **Not examined:** whether the mechanism (constant E[5], one cusp orbit, Hom(J_C[5], E₀[5])) extends to higher-degree base changes. There, cusp orbits can split and torsion interferes. This is outside scope, and no claim is made.

**Proposed ledger block.** Not merged; it needs operator acceptance.

    FIXED-E[5] FAMILY, DEGREE-2 TWIST ATTACK (FIXED_E5_DEGREE2_TWIST_ATTACK_001, 2026-09-17)
    Return: UNKNOWN_NO_WITNESS; Gate G parked (OPERATIONALLY_OBSTRUCTED; NONEXISTENCE_OPEN unchanged).
    Proved (genus 0): the cusp polynomial g (deg 12) of the 389a1 Rubin-Silverberg family is irreducible over Q;
      for every squarefree D in Q[t] with deg D in {1,2}: rank E^D(Q(t)) <= 1, so rank E(Q(t,sqrt D)) <= 1.
      Mechanism: MW(E^D)/5 -> (+)_cusps Phi_v (x) F5 is injective (Selmer: H^1(pi_1(G_m), E[5] (x) chi_D) = 0;
      independently the NS discriminant length), and invariant component vectors span <= 1 dim (one cusp orbit).
    Reduced (genus 1, deg D in {3,4}): rank E^D(Q(t)) <= 1 + dim Hom_{G_Q}(J_C[5], E0[5]) <= 2; rank 2 needs
      J_C[5] ~ E0[5], split twisted cusp fibres, and a Q-rational section through the identity component at all
      12 cusps (height >= 10). No finite height range; no search run. NOT a negative theorem for genus 1.

**Files.**
- `src/rs_family_389a1_check.py`: Fable's transcription, sha256-identical copy.
- `runs/gen_coeffs.py` and `runs/coeffs.gp`: α_k and β_k specialised at J = 21952/10503.
- `runs/phase0.gp` and `runs/phase0.out`: all Phase-0 computations.
