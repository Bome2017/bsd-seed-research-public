# SOURCE_EXCERPTS — A1_WITNESS_CONTENT

Every theorem this package copies from the Codex reports is listed below with:
- source filename;
- heading / theorem label;
- exact assumptions;
- exact conclusion;
- the **verbatim** source text.

The Codex and handoff files are the project's own files, so they are copied byte-exactly. Ota's paper is third-party, so it
is restated rather than copied. SHA-256 values are of the source files at packaging time (2026-09-19). Where the
packaged Lean statement differs in form from the prose, `THEOREM_TARGETS.md` says so explicitly.

## Codex frontier attack and handoff (verbatim)

### §1 Unconditional objects — objects of WC (S0, P, S-family, M(p,S), t(p,S), depth, h_p, J_E)
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e`)
- **heading / label:** §1 Unconditional objects
- **exact assumptions:** E/Q of rank two; S0 contains every prime excluded by Ota 5.17 and 6.4 (seed: {2,3,5,2243,4547,5843}); S-family as displayed
- **exact conclusion:** definitions only; J_E is an ideal of Z, nonzero iff every h_p finite and only finitely many positive (proved in package A2)

```text
## 1. Unconditional objects

Fix an elliptic curve E/Q of rank two. Let S0 be a finite set containing every prime excluded by Ota's Theorems 5.17 and 6.4, and put P = {primes outside S0}. For the fixed seed we may use

    S0 = {2, 3, 5, 2243, 4547, 5843}.

This uses the retained all-odd residual-image theorem, its p-adic lifting for p >= 5, Tamagawa product 16, and the absence of anomalous good primes. The latter follows from rational 2-torsion and Hasse: for p >= 7, a positive even multiple of p exceeds p+1+2 sqrt(p). We also put 5 in S0 so that its already sealed vanishing theorem is used directly; no new tame witness at 5 is required. The Ota hypotheses would also hold at 5, where the group order is 8.

For p in P, let S range over squarefree products of good primes ell not dividing pN, with ell = 1 mod p and E(F_ell)[p] cyclic. Write

    M(p,S) = I_S^2 / I_S^3 over Z_p,
    t(p,S) = the degree-two image of theta_S in M(p,S).

Ota supplies membership theta_S in I_S^2 without Sha-finiteness. M(p,S) is a finite p-primary module. We use the full leading term; choosing core pairs or a cyclic multilinear projection is optional.

For a nonzero element t of a finite p-primary Z_p-module M define

    depth_M(t) = max {j >= 0 : t belongs to p^j M}.

This is finite, since p^j M eventually vanishes. Do not assign a finite truncated depth to the zero element. Define

    h_p = min {depth_M(p,S)(t(p,S)) : t(p,S) != 0},

with h_p = infinity if the displayed set is empty. Each finite h_p is attained, by well-ordering of the nonnegative integers. Set

    J_E = {a in Z : v_p(a) >= h_p for every p in P},

where v_p(0)=infinity. This is an ideal of Z, possibly the zero ideal: the valuation inequality is preserved under addition and multiplication by integers. Its definition uses modular symbols and finite augmentation quotients, not #Sha or the BKS Mordell-Weil realization. It is nonzero exactly when every h_p is finite and only finitely many are positive. In that case its positive generator is the finite product of p^h_p. These assertions follow directly from prime factorization of a nonzero integer; they impose no coherence on unit parts.
```

### §2 The theorem — THEOREM WC and its proof
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e`)
- **heading / label:** §2 The theorem
- **exact assumptions:** J_E contains a nonzero integer A (the ANTECEDENT); Ota 5.17 and 6.4 (Thm 1.5) at p ∈ P; Selmer cofinite generation and corank; Sha torsion
- **exact conclusion:** (1) Sha[p^∞] finite ∀p ∈ P; (2) Sha[p^∞] = 0 for p ∈ P, p ∤ A; (3) Sha finite if the S0-primary groups are finite

```text
## 2. The theorem

**Theorem WC.** If J_E contains a nonzero integer A, then:

1. Sha(E/Q)[p^infinity] is finite for every p in P;
2. Sha(E/Q)[p^infinity] = 0 for p in P with p not dividing A;
3. if the primary groups at the finitely many primes in S0 are finite, Sha(E/Q) is finite.

**Proof.** For p in P, h_p <= v_p(A) < infinity supplies an S with t(p,S) nonzero. If the p-primary Sha group were infinite, its Z_p-corank would be positive: the p-primary Selmer group is cofinitely generated, and a cofinitely generated p-primary group of corank zero is finite. Hence the Selmer corank would exceed rank E(Q)=2. Ota 5.17 would place theta_S in I_S^{min(corank,p)}, a submodule of I_S^3, contradicting t(p,S) != 0. This proves (1).

If p does not divide A, h_p=0. The attaining t is not in pM, so its reduction in M/pM is nonzero. Ota 6.4 gives Sha[p]=0. Any nonzero p-primary torsion element has a nonzero multiple of order p, so the entire p-primary group vanishes. This proves (2).

Sha is a torsion group, thus the direct sum of its primary groups. All but finitely many vanish by (2); those left are finite by (1) and the S0 hypothesis. Their direct sum is finite. QED.

The imported Ota assertions are read in the retained primary text, lines 2069–2078 and 2146–2156, and checked against [Ota's paper](https://arxiv.org/abs/1509.00682). The proof above is our deduction. No converse is asserted.
```

### §4 Uniform symbol denominators — countermodel (regression test T9a)
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e`)
- **heading / label:** §4 Uniform symbol denominators
- **exact assumptions:** fixed lattice Z with element 1; integral maps n ↦ p²n into Z_p (here: ZMod p³)
- **exact conclusion:** the source has no denominator yet the image is divisible by p at every prime: uniform denominators do not bound h_p

```text
### Uniform symbol denominators

The project bounds denominators by a power of 2. That gives integrality at every odd p. It does not bound h_p. Counterexample: the fixed lattice Z with element 1, evaluated by the integral maps n -> p^2 n in Z_p. The source has no denominator at all, yet the image is divisible by p at every prime. The actual logarithmic and localization maps must supply additional arithmetic information.
```

### §5 Exact stop — status lines
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e`)
- **heading / label:** §5 Exact stop
- **exact assumptions:** —
- **exact conclusion:** WC_IMPLICATION = PROVED; WC_ANTECEDENT_FOR_SEED = UNKNOWN; SEED_FIN = OPEN

```text
## 5. Exact stop

    WC_IMPLICATION = PROVED
    LINE_IMPLIES_WC = PROVED using the retained core-pair normalization/existence
    WC_ANTECEDENT_FOR_SEED = UNKNOWN
    NONZERO_ELEMENT_OF_J_E = NOT CONSTRUCTED
    EXCEPTIONAL_PRIMARY_FIN = OPEN at 2243, 4547, 5843
    SEED_FIN = OPEN

The seed's sealed p=5 cyclotomic symbol certificate is not silently relabelled as a tame Ota witness: 5 is excluded and its known vanishing is used directly. The p=3 group also lies in S0. No value of h_p has been newly computed. Neither the 20 p=5 symbols nor any finite set of primes can establish J_E != 0.

The next theorem attempt should address integral descent and bounded witness content directly. The reduction makes the target smaller than LINE, but does not supply an executable proof of its antecedent.
```

### §A Finite augmentation quotients — LEMMA A (targets T1, T2, S1–S3)
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md` (sha256 `8dcd44af28fef1648a0a0e37085eda632f80bca2aa214585df6935c797d3f8b6`)
- **heading / label:** §A Finite augmentation quotients
- **exact assumptions:** finite group G of exponent dividing e; R = Z[G]; I = augmentation ideal; r ≥ 1
- **exact conclusion:** e·I^r ⊆ I^(r+1); I^r/I^(r+1) finitely generated, killed by e, finite; rationalization zero

```text
## A. Finite augmentation quotients do not survive direct rationalization

Let G be a finite group of exponent e, R=Z[G], and I its augmentation ideal. For every r>=1,

    e I^r is contained in I^(r+1).

Indeed, for g of order dividing e, write g=1+x. Expanding (1+x)^e=1 gives ex in I^2. The elements g-1 generate I as an abelian group, hence eI is contained in I^2. Multiply by I^(r-1). Therefore I^r/I^(r+1) is finitely generated and killed by e, and is finite. After tensoring with Q it vanishes. Equivalently, the rational augmentation ideal is idempotent: in Q[G], 1-|G|^(-1) sum_g g is an idempotent generator.

Consequences: a fixed conductor S, or any finite list of conductors, can have higher augmentation information only at finitely many primes. Simply rationalizing each finite group ring cannot recover the desired characteristic-zero leading term.

**Scope correction.** This does not show that inverse limits contain no characteristic-zero information. For a procyclic pro-p tower, the completed augmentation quotient is Z_p and becomes Q_p on rationalization. Nor does it exclude geometric or derived lifts. It identifies why rationalization cannot be interchanged with completion. Statements that a product of finite groups has “no rational line” should be replaced by this precise finite-stage assertion.
```

### Package A — Codex formalization proposal (A1 augmentation annihilation; A2 contraction; A3 integral content)
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FORMALIZABLE_GAPS.md` (sha256 `2f19d86fe01191d76f34c12038ce4d56b25c5e50b964d61a82fdc52b6d7bd699`)
- **heading / label:** Package A
- **exact assumptions:** as displayed
- **exact conclusion:** as displayed (A2 contraction and A3 content are NOT in this package: see THEOREM_TARGETS.md §Scope)

```text
## Package A — finite algebra and determinant types

**A1. FORMALIZABLE_NOW: augmentation annihilation.** Input: a finite group G, positive integer e with g^e=1 for every g, its integral group ring, augmentation ideal I, and r>=1. Output: e I^r is contained in I^(r+1); hence the graded quotient is a finite abelian group and its rationalization is zero. Proof: expand (1+(g-1))^e; sum on the additive generators; multiply by I^(r-1). Separate the finite generation and annihilation lemmas. No commutativity of G is needed. Source proof: Algebraic Lemma A.

**A2. FORMALIZABLE_NOW: rank-two contraction.** Input: a field K, a K-vector space V of dimension two, a nonzero linear functional ell. Output: exterior-square contraction is an isomorphism onto ker ell, with inverse kappa -> (v wedge kappa)/ell(v) for any v with ell(v)!=0. Prove independence of v. This is pure linear algebra; instantiate ell=log_p only outside the core theorem. Source proof: Algebraic Lemma C.

**A3. FORMALIZABLE_NOW: integral content.** Input: a finite free Z-module M, basis, and nonzero z. Let c be the positive gcd of the coordinates. Output: for every prime p and j>=0, z is in p^j(M tensor Z_p) iff j<=v_p(c); c is independent of unimodular basis change. An initial finite algebra version over Z/p^k is sufficient for the witness projection application, with j<k and zero/truncation cases treated explicitly. Do not assign zero a finite valuation.

**Acceptance:** exact hypotheses; authored modules explicitly built; no sorry/admit; theorem types and axiom inventory reported; conditional arithmetic imports outside the pure algebra files. One clean replay of the chosen source bytes, not repeated default builds.
```

### Not formalizable as a solved arithmetic gap
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FORMALIZABLE_GAPS.md` (sha256 `2f19d86fe01191d76f34c12038ce4d56b25c5e50b964d61a82fdc52b6d7bd699`)
- **heading / label:** Not formalizable as a solved arithmetic gap
- **exact assumptions:** —
- **exact conclusion:** J_E ≠ 0 for this curve: no construction or proof (never a target here)

```text
## Not formalizable as a solved arithmetic gap

- J_E != 0 for this curve: no construction or proof.
- Existence of the desired integral determinant/zeta object before FIN: no construction.
- Uniform primitive comparison with Ota witnesses: no proof.
- q in Q, or the proposed bounded algebraicity: no proof.
- An archimedean GPR/ETNC comparison: not reduced to a finite algebraic lemma.
- Exact order nine from FIN alone: false inference.

The two packages are suitable for parallel sessions later if the user chooses to run them. Their value is checking reusable deductions and eliminating ambiguity, not resolving the two open arithmetic branches by automation.
```

### Weakest sufficient statement, with scope stated
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FIN_ATTACK.md` (sha256 `0fb5b18c5c773978dff0770c1e04178860d0f12ac619e132b71b7bdb3e681dfc`)
- **heading / label:** Weakest sufficient statement, with scope stated
- **exact assumptions:** —
- **exact conclusion:** WC is the weakest explicit sufficient condition isolated in the bounded attack; not an absolute minimality theorem

```text
## Weakest sufficient statement, with scope stated

There is no canonical “weakest theorem” among all possible proof languages. Within the currently usable Ota architecture, WC is the weakest explicit sufficient condition isolated here: **nonzero J_E**, plus finiteness at its finite excluded set. For tail vanishing alone, it suffices that h_p=0 outside an explicitly finite set; finite-depth witnesses at the remaining good primes give their finiteness.

For the seed, the excluded 2-,3-,5-parts are retained as solved; 2243,4547,5843 remain open under this route. They remain subnodes of FIN. A genuinely global theorem may absorb them.

Next premium work: construct and test an integral descent/comparison map that forces nonzero witness content before assuming local FIN. Require the map, its coefficient ring, its primitive lattice, and its exact Ota specialization before calling it a mechanism. The formal reductions themselves need no premium mathematical search. No numerical LINE test, p=7 launch, or p=23/29 run is justified by this session.
```

### DO_NOT_RESURRECT_ADDENDUM item 7
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/DO_NOT_RESURRECT_ADDENDUM.md` (sha256 `1f18ad4173268857aaa139e6111b28cb8ecf99efa4435edfbc043fad030f3aaf`)
- **heading / label:** DO_NOT_RESURRECT_ADDENDUM item 7
- **exact assumptions:** —
- **exact conclusion:** stop rule (verbatim)

```text
7. Do not confuse an arbitrary profinite determinant ideal with a nonzero ideal of Z. Perfectness and finite defects at each p do not ensure finite support.
```

### DO_NOT_RESURRECT_ADDENDUM item 8
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/DO_NOT_RESURRECT_ADDENDUM.md` (sha256 `1f18ad4173268857aaa139e6111b28cb8ecf99efa4435edfbc043fad030f3aaf`)
- **heading / label:** DO_NOT_RESURRECT_ADDENDUM item 8
- **exact assumptions:** —
- **exact conclusion:** stop rule (verbatim)

```text
8. Do not demand cross-prime unit equality when only witness content is needed for FIN. Conversely, defining J_E does not prove it nonzero.
```

### DO_NOT_RESURRECT_ADDENDUM item 9
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/DO_NOT_RESURRECT_ADDENDUM.md` (sha256 `1f18ad4173268857aaa139e6111b28cb8ecf99efa4435edfbc043fad030f3aaf`)
- **heading / label:** DO_NOT_RESURRECT_ADDENDUM item 9
- **exact assumptions:** —
- **exact conclusion:** stop rule (verbatim)

```text
9. Do not rationalize finite augmentation quotients and expect their leading terms to survive. Do not use that failure to forbid completed or derived lifts.
```

### DO_NOT_RESURRECT_ADDENDUM item 15
- **source file:** `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/DO_NOT_RESURRECT_ADDENDUM.md` (sha256 `1f18ad4173268857aaa139e6111b28cb8ecf99efa4435edfbc043fad030f3aaf`)
- **heading / label:** DO_NOT_RESURRECT_ADDENDUM item 15
- **exact assumptions:** —
- **exact conclusion:** stop rule (verbatim)

```text
15. Do not treat the conditional WC proof, the numerical certificate, or a later Lean proof of a reduction as proof of FIN or FORMULA. No new nonzero witness, uniform integer A, rational q, denominator bound, or common zeta element was constructed.
```

### Handoff FIN_FRONTIER §5 — WC is a clean interface, NOT a reduction in difficulty (the package warning)
- **source file:** `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/FIN_FRONTIER.md` (sha256 `60b82cd136fc082ec33c816ef0e7275d9cd36de9e962c7f26155b0cd65511ada`)
- **heading / label:** Handoff FIN_FRONTIER §5
- **exact assumptions:** —
- **exact conclusion:** WC weaker than LINE ≠ antecedent easier than FIN; a compiled WC proves only the implication

```text
## 5. WC — Codex's witness-content criterion (cross-family, 2026-09-19): a clean interface, NOT a reduction in difficulty
Sources: `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa5…`); Opus cross-check `~/BSD_SEED_2243_12_FIN_ASSUMED_FORMULA_AUDIT_2026-09-19/ADDENDUM_CROSS_FAMILY_2026-09-19.md`.

**Setup.**
- S0 = {2, 3, 5, 2243, 4547, 5843}, and P = the primes outside S0.
- For p ∈ P, S runs over squarefree products of good primes ℓ ∤ pN with ℓ ≡ 1 (mod p) and E(F_ℓ)[p] cyclic.
- t(p,S) is the degree-two image of θ_S in M(p,S) = I_S²/I_S³ ⊗ Z_p, a finite p-primary module.
- depth(t) = max{j : t ∈ p^j M}, defined only for t ≠ 0.
- h_p = the minimum depth over the nonzero t(p,S), and ∞ if there are none.
- J_E = {a ∈ Z : v_p(a) ≥ h_p for every p ∈ P}.

**Theorem WC** (conditional; PROVED from Ota Thms 5.17/6.4 as quoted). If J_E contains a nonzero integer A, then:
1. Sha[p^∞] is finite for every p ∈ P;
2. Sha[p^∞] = 0 for every p ∈ P with p ∤ A;
3. Sha is finite, provided the primary groups at S0 are finite.

**Status.**
- The implication is PROVED: Codex wrote the proof, and Opus checked the logic. Ota's hypotheses for p ∈ P are as checked by Codex; Opus did not re-verify them.
- The antecedent J_E ≠ 0 is OPEN: nothing has been constructed.
- LINE ⇒ WC (Codex, using the retained core-pair inputs), so **WC is weaker than LINE**.

**What that does NOT mean.** "Weaker than LINE" does not mean "its antecedent is easier than FIN".
- **Opus caveat** (2026-09-19; the converse hypotheses were NOT checked for the seed). At a good ordinary p where the IMC holds, a Kurihara/Kim-type
  converse (non-vanishing / primitivity of Kato's Kolyvagin system and Kurihara's structure theorem) should turn Sha[p^∞] = 0 into a depth-0 Ota witness.
- If so, then on the ordinary tail J_E ≠ 0 is essentially FIN written in Ota coordinates. Its only content beyond the prime-by-prime FIN statements would be
  the uniformity packaging (one integer A).
- **WC is a clean interface and gives formal structure. It is not yet a reduction in mathematical difficulty.**
- A compiled (Lean/Aristotle) proof of WC proves only the implication from the stated antecedent. It establishes neither that the antecedent is easier
  than FIN nor that FIN has been reduced (DO_NOT_RESURRECT rows 37–38).

**Kill gate before any premium effort on constructing J_E:** `CODEX_QUESTIONS.md` Q0.
```

## Ota, *Kato's Euler system and the Mazur–Tate refined conjecture of BSD type* (arXiv:1509.00682)

Third-party source. What follows is a **faithful mathematical restatement**, not a copy. The line numbers refer to
the project's local text extraction `~/BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F4_work/sources/D/ota_1509.00682.txt`
(sha256 `4bb177618ed9fded191bb06b59653767df0d9a58a00cd1d37fe7b1204b976f51`). Codex checked these statements against the arXiv PDF (`SOURCE_INDEX.md` S53).

**Setting (§1.2, lines ≈56–68; notation line ≈163).**
- E/Q has no complex multiplication and conductor N. m_ℓ := [E(Q_ℓ) : E_0(Q_ℓ)], and r_E := rank E(Q).
- R ⊂ Q is a subring in which every prime p is inverted that satisfies at least one of:
  - (i) p divides 6N·|E(F_p)|·∏_{ℓ|N} m_ℓ;
  - (ii) the p-adic Galois representation G_Q → Aut_{Z_p}(T_p E) is not surjective;
  - (iii) p < r_E.
- R is also chosen so that θ_S ∈ R[G_S] for all S (§1.1, lines ≈47–49).

**Notation (lines ≈38–53, 127, 168).**
- G_S := Gal(Q(μ_S)/Q), and I_S is the augmentation ideal of R[G_S].
- r_{p^∞} is the Z_p-corank of the discrete Selmer group Sel(Q, E[p^∞]).

**Definition 2.1 (lines ≈211–216).**
- θ_S := Σ_{a ∈ (Z/SZ)^×} ([a/S]⁺_E + [a/S]⁻_E)·δ_a ∈ Q[G_S], where δ_a ∈ G_S is the element with δ_a ζ_S = ζ_S^a.

**Theorem 5.17 (lines 2069–2078).**
- *Hypotheses:*
  - p ∤ 6N·|E(F_p)|·∏_{ℓ|N} m_ℓ;
  - G_Q → Aut_{Z_p}(T_p E) is surjective;
  - S is a squarefree product of good primes ℓ such that E(F_ℓ)[p] is Z/pZ or 0.
- *Conclusion:* θ_S ∈ I_{G_S}^{min{r_{p^∞}, p}} ⊆ Z_p[G_S]. In particular, if p ≥ r_E then θ_S ∈ I_{G_S}^{r_E}.
- The proof combines Cor. 5.15 (exponent min{r_{p^∞} − 1, p}) with the functional equation of θ_S and the p-parity theorem.

**Theorem 1.5 (introduction, lines 118–122; stated there as a special case of Theorem 6.4).**
- *Hypotheses:*
  - p is a prime not invertible in R;
  - S is a squarefree product of good primes ℓ with ℓ ≡ 1 mod p and E(F_ℓ)[p] cyclic.
- *Conclusion:* if the leading coefficient θ̃_S (the image of θ_S in I_S^{r_E}/I_S^{r_E+1}, lines 114–116) is ≢ 0 mod p·(I_S^{r_E}/I_S^{r_E+1}),
  then Sha(E/Q)[p] = 0 and p ∤ J_S.
  - Here J_S is the order of the cokernel of E(Q) → ⊕_{ℓ|S} E(F_ℓ) ⊕ ⊕_{ℓ|N} E(Q_ℓ)/E_0(Q_ℓ).

**Theorem 6.4 (lines 2146–2156, setting of §6.2).**
- *Setting:* S is as in Theorem 6.1: a squarefree product of good primes ℓ with E(F_ℓ)[p′] cyclic for EVERY prime p′ not invertible in R.
  - p is a prime not invertible in R, with p ∤ S.
  - S = S₁S₂, where S₁ is the product of the ℓ | S with ℓ ≡ 1 mod p.
- *Conclusion:* if the image θ̃_S^{(p)} of θ_S in Z/pZ ⊗_R I_S^{r_E}/I_S^{r_E+1} is nonzero, then
  - Sha[p] = 0;
  - p ∤ J_{S₁};
  - p ∤ ∏_{ℓ|S₂}(a_ℓ − 2).
- The proof, lines ≈2160–2250, works with p-local objects (Kato's Euler system, Kolyvagin derivatives, Corollary 4.19).

**Hostile note on the S-class (discovered while packaging; recorded, not resolved).**
- Codex's witness family is: ℓ ∤ pN, ℓ ≡ 1 (mod p), E(F_ℓ)[p] cyclic. This matches **Theorem 1.5 exactly**, which this package imports.
- Theorem 6.4 *as printed* assumes the stronger S-class of Theorem 6.1: cyclicity at every non-invertible prime, not only at p.
- If a referee insists on the printed Theorem 6.4, restrict the index type `W p` to that class.
  - The formal WC proof is unchanged, because `W p` is abstract.
  - Only the arithmetic meaning of h_p and J_E changes: J_E can only get smaller, so the antecedent gets harder.

**Normalisation notes.**
- §2 defines θ̃_S for Conjecture 2.4 as the image of ½θ_S on the "+" quotient. Theorems 1.5 and 6.4 use the image of θ_S in
  I_S^{r_E}/I_S^{r_E+1} (lines 114–116 and 2156–2158).
- For odd p, the factor ½ is a unit, so no depth changes.

**Base change (FORMAL_ASSUMPTION).** Ota works with I_S ⊂ R[G_S] for R ⊂ Q, while Codex's M(p,S) is I_S²/I_S³ over Z_p.
- Z_p is flat over R when p ∉ R^×, and R/p = F_p. Hence M_{Z_p} = Z_p ⊗_R M_R and M_{Z_p}/p = F_p ⊗_R M_R.
- So "θ̃ ∉ p·M" is the same condition over R and over Z_p.
- Standard commutative algebra, NOT formalized here.
