# Fatal trace error and fixed-field lifting obstructions

Status: **proved mathematical obstructions**, not a kernel-checked formal proof.
Source under audit: Destrempes–Malinin, arXiv:1703.02215v2.
Endpoint: audit of the claimed uniform FIN compression. These obstructions do not prove FIN or determine the seed's Sha.

## 1. First fatal inference located

Theorem 6, Step 2, printed pages 29–30, equations (135)–(137), has an integral element α₀ in one prime ideal 𝔓 above the rational prime p. It concludes that Tr(Lₙ/Q)(α₀) belongs to pZ. The local/global trace diagram (136) is valid, but the claimed divisibility at **every** prime 𝔓′ above p does not follow from divisibility at just 𝔓.

Explicit counterexample: L = Q(i), p = 17, α₀ = 4+i, and 𝔓 = (4+i). The ideal 𝔓 has norm 17, α₀ belongs to 𝔓, and

    Tr(L/Q)(α₀) = 8, not divisible by 17.

Equivalently, the two embeddings into Q₁₇ give residues 0 and 8. Only the first summand of the global trace vanishes. The correct global divisibility would follow, for example, from α₀ ∈ pO_L; that stronger premise is absent.

The paper's α₀ is not arbitrary, so this elementary example by itself diagnoses the invalid inference, rather than proving that every instance of its equation (137) is false. Sections 2 and 3 below independently disprove the uniform lifting statements that the paper needs.

**The same failure inside the paper's torsion-field setting.** Fix ell ≥ 5 with full residual image, and put L = Q(E[ell]) and D = [L:Q]. Its Galois group acts transitively on the nonzero ell-torsion points. Since α(P) is the rational expression (133) in P and [2]P, the integer T = Tr(L/Q)(α(P)) is the same for every such P. Choose a good rational prime p splitting completely in L, avoiding ell(ell−1)(ell+1)Δ′. Such primes exist by Chebotarev, and p does not divide D.

All ell²−1 nonzero ell-torsion points now reduce to distinct points of E(F_p). If (137) held for all of them, it would give

    ell² y(P)² T = Δ′ ell⁵ D in F_p

for all those reduced points. The right side is nonzero. If T is zero modulo p, the equation fails immediately. Otherwise it forces y(P)² to have one fixed value for all ell²−1 points. An affine cubic y²=x³+Ax+B has at most six geometric points with one specified nonzero y². Since ell²−1>6, this is impossible. Thus (137) fails for admissible torsion points in the actual full-image setting; no special property of their α₀ rescues the claimed universal congruence. This argument grants the upstream integrality identity and does not use Proposition 2 or the interpretation of C.

## 2. No finite collection of algebraic points lifts all reduced ell-primary points

**Theorem.** Let E/Q be an elliptic curve, let ell be a prime, and let S be any finite subset of E(Qbar). There are infinitely many primes p of good reduction, p ≠ ell, for which some nonzero point of E(F_p)[ell^∞] is not the reduction of any point of S (under any one fixed embedding into Qbar_p).

**Proof.** Choose n with ell^(2n) − ell^(2n−2) > |S|. By Chebotarev there are infinitely many good primes p splitting completely in Q(E[ell^n]); omit the finitely many primes needed for integral reductions of S and any other fixed finite excluded set. Prime-to-p torsion reduces injectively, so E(F_p) contains ell^(2n) − ell^(2n−2) points of exact order ell^n. The reductions of S have cardinality at most |S|. At least one of these nonzero torsion points is missing. ∎

**Application to Theorem 6 as used in §3.5.** A fixed bound 1 ≤ |a|, |b| ≤ C allows at most 4 floor(C)^2 rational values a/b. On y² = x³+Ax+B there are at most six geometric points with a prescribed nonzero y². Thus all proposed lifts form a set of cardinality at most 24 floor(C)^2. The theorem above contradicts their coverage assertion. Theorem 6's displayed statement says C is independent of n; §3.5 and Remark 4 explicitly use C depending only on E and ell, and independent of the auxiliary prime p. It is this uniform assertion needed to build their fixed K′ that is disproved here.

## 3. No fixed number field covers all local quotients

**Theorem.** For every elliptic curve E/Q, prime ell, and finite extension F/Q, there are infinitely many good primes p ≠ ell splitting completely in the normal closure of F such that, for every embedding ξ: F → Q_p,

    ξ(E(F)) ⊆ ell E(Q_p),
    E(Q_p)/ell E(Q_p) ≅ (Z/ell Z)^2.

Consequently E(F) cannot surject onto E(Q_p)/ell E(Q_p) for all but finitely many p.

**Proof.** By Mordell–Weil choose a finite generating set P₁,…,P_r for E(F), including generators for its torsion subgroup. Choose Q_i ∈ E(Qbar) with ell Q_i = P_i. Let M/Q be a finite Galois extension containing F, E[ell], all Q_i, and their conjugates. Chebotarev supplies infinitely many good p ≠ ell splitting completely in M, outside any specified finite excluded set. Each embedding F → Q_p extends to M → Q_p. It follows that every ξ(P_i), hence every point of ξ(E(F)), is an ell multiple in E(Q_p).

At the same time all of E[ell] is rational over Q_p. The kernel of good reduction E(Q_p) → E(F_p) is uniquely ell-divisible, so the local quotient is E(F_p)/ell E(F_p). A finite abelian group has the same ell-rank in its quotient by ell as in its ell-torsion. Here its ell-torsion has dimension two. ∎

**Application.** Take F = the paper's fixed K′. Proposition 10, equation (184), claims precisely the local coverage that this theorem rules out, for every p outside a fixed finite set. In the constructed counterexamples p splits in K′, so its decomposition-fixed subfield is K′ itself. Thus Proposition 10 is false as a statement, not merely inadequately justified.

## 4. The obstruction also reaches nontrivial semisimple Frobenius types

**Theorem.** Let F/Q be finite Galois. Suppose the image of G_F on V = E[ell] contains an element s of order d prime to ell with V^s ≠ 0. There are infinitely many good rational primes p ≠ ell, splitting completely in F, and embeddings ξ: F → Q_p, such that

    ξ(E(F)) ⊆ ell E(Q_p),
    dim_Fell E(Q_p)/ell E(Q_p) = dim_Fell V^s > 0,

and the Frobenius action on V is conjugate to s.

**Proof.** Let M = F(E[ell], ell^(-1)E(F)), where it suffices to adjoin ell-preimages of a finite generating set of E(F). This is a finite Galois extension of Q: F/Q is Galois, E(F) is G_Q-stable, and adjoining V makes all choices of the preimages equivalent. The group K = Gal(M/F(E[ell])) embeds into a finite direct sum of copies of V, and hence is elementary abelian of exponent ell.

Lift s to h ∈ Gal(M/F). Then h^d ∈ K, so h^(d ell) = 1. Choose an integer a divisible by ell and congruent to 1 modulo d. The element t = h^a still projects to s and has order d. Chebotarev gives infinitely many unramified good p with a place of M having Frobenius t. Then p splits completely in F and M_w/Q_p is unramified of degree d.

For every P ∈ E(F), an ell-preimage Q belongs to E(M_w). Its trace T to E(Q_p) satisfies ell T = d ξ(P). Choose u,v ∈ Z with ud+vell = 1. Then

    ξ(P) = ell (uT + v ξ(P)).

Thus all F-rational points are locally ell-divisible. The ell-torsion of E(F_p) is V^s, and the good-reduction argument in Section 3 gives the asserted nonzero local quotient. ∎

**Application to Lemma 9(e)'s setting.** For F = K′, Lemma 9(e) supplies s = diag(λ₀,1) of order d₀ dividing ell−1. The local quotient in this theorem has dimension one, and p ≡ λ₀ (mod ell), so p is not congruent to 1 modulo ell. Consequently simply restricting Proposition 10 to this residual Frobenius type cannot fix it. This does not prove that every prime specially selected by Lemma 8 fails; Lemma 8 prescribes additional class-field data. Nor does it disprove a lifting statement restricted to actual global Selmer classes: that would require a separate arithmetic argument absent from this paper.

## 5. Exact dependency and scope

The proof chain is:

    false trace inference (135) → (137)
      → uniform bounded lifts (Theorem 6)
      → fixed K′ with universal local coverage (Proposition 10)
      → local-to-global Kummer replacement (Proposition 11)
      → Corollary 10
      → Proposition 12, Step 6 (I ⊆ I′)
      → Sah's theorem and prime-to-ell descent
      → claimed Theorem 5.

Sah's theorem and restriction–corestriction do not supply the missing universal local coverage. Letting K′ vary with p removes the fixed finite field used later; allowing infinitely many bounded-lift replacements removes finiteness. Neither is a repair of this proof. A new Selmer-specific comparison would require independent proof.

**Progress classification:** no-go compression for finite universal lift sets and fixed-field universal local Kummer coverage. No finiteness or exact-order statement for Sha follows. No assertion of literature novelty is made.
