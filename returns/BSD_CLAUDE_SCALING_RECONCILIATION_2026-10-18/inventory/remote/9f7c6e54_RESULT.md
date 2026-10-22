# RESULT: Kato's determinant element before the Mordell–Weil realization

## Outcome: **NEW_COMPARISON_OR_LEMMA**

**The new lemma: Theorem K.** It is Sha-free, and it covers Ota witnesses at p-torsion-free auxiliaries. The bound the
task proposed — h_p ≤ v_p(C) + v_p(content_L(z)) with z the Kato element — **fails for this candidate**, at an
explicitly identified map. That is a SCOPED_FAILURE of the proposed construction. It is not a theorem about other
constructions.

**Nothing is promoted to an endpoint.** No new vanishing of Sha, finite-support result, FIN, ORDER9 or Q36 is
obtained.

- **Input:** commit `4a04423` (staged handoff bundle; `input/STAGING.md`).
- **Derivation:** `DERIVATION.md`.
- **Countercheck:** `checks/`.

## The single question, answered

**Question.** Can an integral construction starting from the Kato determinant classes bound the divisibility of their
specializations to Ota witnesses, uniformly in p, without the Mordell–Weil identification and without Sha finiteness?

**Answer for this candidate: no.** The reason is exact.
- By BKS II Cor. 5.3, which uses Hyp. 2.2 only, the witness factors as θ_{F,S} = x_F·δ_F (Lemma K1).
  - x_F is the coordinate of the determinantal zeta element: the "Kato content".
  - δ_F is the characteristic element of the Bloch–Kato Selmer complex over F: purely algebraic and independent of
    Kato's element.
- The leading term of δ_F is computed exactly by an elementary lemma, K3, together with the descent K4. This gives
  **Theorem K.** For every p ∉ B_K = S₀ ∪ {19, 59, 487}, ordinary or supersingular, and every squarefree S of primes
  l ≡ 1 (mod p) with p ∤ #E(F_l):
  - if Sha(E/Q)[p^∞] is infinite, the witness t(p, S) is 0;
  - otherwise t(p, S) = η·x_Q·#Sha(E/Q)[p^∞]·det(B_S) in Z_p ⊗ I²/I³, with η a unit and B_S the Bockstein matrix.
- So the specialization map from the determinant line to the witness is **multiplication by #Sha(E/Q)[p^∞]**, times
  the Bockstein. This is the task's "n ↦ p·n" loss, made exact.
- The Kato content does satisfy the proposed content bound. At good ordinary p, v_p(x_Q) = 0 (Cor. K-c; IMC at
  recorded grade), i.e. C = 1.
- **The failure lies wholly in the algebraic factor #H²_f(Q, T_p)_tors.** No property of the Kato element can control
  it, because δ_F does not involve that element.

## What is new relative to the supplied records

1. **The factorization θ_{F,S} = x_F·δ_F under Hyp. 2.2 alone.** The records reached the tame leading term only
   through BKS Prop. 5.4 and the maps (11)/(13), which require T_pSha = 0 (LINE audit Items 1–2; E10 Prop. D).
2. **Theorem K**, the exact Sha-free witness law. It holds at every depth k, for multi-prime S, and at supersingular
   p ∉ B_K.
3. **Corollary K-a.** Over this family, depth t(p, S) ≥ v_p(#Sha(E/Q)[p^∞]) + v_p(x_Q). So bounded-depth witnesses from
   this family exist only if v_p(#Sha[p^∞]) is bounded.
4. **Corollary K-b.** At the G2 auxiliaries: t ≠ 0 ⟺ p ∤ x_Q and Sha(E/Q)[p^∞] = 0.
5. **Corollary K-c.** At good ordinary p:
   - x_Q is a unit;
   - depth t(p, {l}) = min(k, v_p(#Sha[p^∞]) + v_p(det B̄_l)). This is the valuation-level Mazur–Tate leading term at
     these layers, proved from the IMC without first assuming Sha finite.
6. **E10's multiplier M_p, split as zero patterns.** p | M_p ⟺ (p | x_Q or Sha[p^∞] ≠ 0). No exact p-adic identity is
   claimed.
7. **Lemma K5.** The level-one Kato class vanishes (z_Q = 0) at every p ∉ B_K. So the determinantal element is p-adic
   in origin, and the construction supplies no Z-lattice. This is a consistency point.

No novelty is claimed relative to the literature. Descent formulas of this shape are standard.

## The candidate and the maps examined

    Δ_F = det⁻¹_{Z_p[G]} RΓ(O_{F,Σ}, T)  ∋ 𝔷_F = x_F·b_F
      │ φ_F  (acyclic local terms at ℓ | SN; E₁(F_p)* ≅ Z_p[G] via c_F)
      ▼
    det⁻¹ RΓ_f(F, T) ──π_{F,f} = det(ψ_f)──▶ Z_p[G] ∋ θ_{F,S} = x_F·δ_F ──▶ Z_p ⊗ I²/I³ ∋ t(p, S)
      │ ν (base change)
      ▼
    Δ_Q = det⁻¹_{Z_p} RΓ(Z_Σ, T) ∋ 𝔷_Q = x_Q·b_Q          [the lattice L_p; content v_p(x_Q)]

**Coefficient rings and Euler factors.**
- The coefficient rings are Z_p[G_S], its augmentation ideal I, and Z_p ⊗ I²/I³ ≅ Z/p^k for singletons.
- The auxiliary Euler factors #E(F_ℓ)/ℓ are units, because the local complexes at ℓ are acyclic.
- Eul_{F/Q,N} is a unit (BKS Remark 2.7).
- The p-factor enters only through c_F. Lemma 5.5's cancellation is not used.

## Imported theorems and unmet hypotheses

**Hypothesis 2.2 of BKS II** was read in the primary text. It has four parts: m squarefree; (m, N) = 1;
p ∤ 6mN·#tors·Tam·∏_{ℓ|pmN}#E^{ns}(F_ℓ); and E[p] surjective. **There is no ordinarity condition.** It holds for the
seed at every p ∉ B_K and every p-torsion-free S (Lemma H).

**Imported, not re-proved:**
- Kataoka's Lemma 4.2 and Ann(z_{F∞}) = 0, and the Burns–Sano and Burns–Sakamoto–Sano theorems behind them. The source
  only sketches these.
- BKS Prop. 5.1, Prop. 5.2 and Cor. 5.3 (proofs read), and the §5.3 base change.
- Poitou–Tate duality for Selmer complexes [Dual].
- The Bockstein = Mazur–Tate identification [MC] (Burns–Macias Castillo Th. 10.3; not re-read). It is used only when
  Sha[p^∞] is finite.
- G2 and its §4 comparison, at audited grade.
- The IMC at good ordinary p, at recorded grade. It is used only for K-c, through a DERIVED determinant translation.
- A DERIVED Euler-factor step: v_p(x_Q) is independent of S. It is used only in K-a's uniformity.
- The retained seed inputs.

**Not supplied:** a supersingular main conjecture for this non-semistable curve. So at the infinitely many
supersingular p, x_Q is only known to be integral.

## Prime scope

| statement | primes covered |
|---|---|
| Theorem K, K-a, K-b | all p ∉ B_K, ordinary and supersingular |
| K-c | good ordinary p ∉ B_K under the recorded IMC hypotheses |

**Exceptional primes.** Nothing here applies at p ∈ B_K.
- 2, 3, 5 and 19 have separate recorded results.
- 59 and 487 are excluded by BKS Hyp. 2.2(iii) and have no recorded primary result.
- 2243, 4547 and 5843 are open.

FIN is not claimed. Even the missing step below, supplied outside a finite set, would give finite support only.

## Countercheck

`checks/leading_term_check.py`, output in `checks/leading_term_check.json`. It ran in 1.1 CPU-seconds in total, with
exact arithmetic.
- **Lemma K3 and the factorization bookkeeping:** 78/78 exact matches on random instances. These cover (Z/p^N)[C_{p^k}]
  for (p, k) = (5, 1), (7, 1), (5, 2), ranks a = 2 and 3, and torsion M ∈ {0, Z/p, (Z/p)², Z/p²}.
- **Decisive implications:**
  - T1: torsion kills or lowers the witness even with unit Kato content and a nondegenerate Bockstein (36/36);
  - T2: with M = 0 the witness is nonzero (12/12);
  - T3: with rank 3 the witness is 0 in I²/I³ (6/6).
- **Product-of-Z_p countermodel:** perfect complexes with unit content, identity Bockstein and M ≅ (Z/p)² give a zero
  witness at p = 7, 11 and 13. So all p-local properties used are compatible with infinite support. This is an
  abstract model, not a claim about the seed.
- **A checker bug was found and fixed.** The first version of the checker had a normalization bug: it dropped the unit
  parts of the Smith pivots. The fix is recorded in `checks/CPU_LOG.md`, and it does not change any statement.

## First remaining step (named, not started)

A prime-independent bound on #H²_f(Q, T_p)_tors, the torsion of the descended Bloch–Kato Selmer complex, which is
≅ Sha(E/Q)[p^∞]^∨ when finite. It is needed for all p outside an explicit finite set. At supersingular p, a bound on
v_p(x_Q) is also needed.

**The limit of this negative statement.**
- Theorem K shows that no tame specialization at p-torsion-free layers of this same determinantal element can supply
  that bound, since all of them carry the factor #Sha[p^∞].
- It does not exclude witnesses at Kolyvagin-type auxiliaries (E(F_l)[p] ≅ Z/p), which lie outside BKS Hyp. 2.2.
- Nor does it exclude any other Kato, motivic, Galois or finite-support construction.

No other mechanism was begun. No successor was launched. Nothing was sent anywhere. The session stops here.
