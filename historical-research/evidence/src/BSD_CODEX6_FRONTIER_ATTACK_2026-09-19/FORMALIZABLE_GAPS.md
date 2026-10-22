# Exact formalization handoff

No Aristotle/Harmonic session or Lean build was launched. These are mathematical contracts and proofs ready for a later bounded formalization task. No guessed mathlib declaration names are asserted. Do not axiomatize an open BSD conclusion and report the resulting implication as a solution.

## Package A — finite algebra and determinant types

**A1. FORMALIZABLE_NOW: augmentation annihilation.** Input: a finite group G, positive integer e with g^e=1 for every g, its integral group ring, augmentation ideal I, and r>=1. Output: e I^r is contained in I^(r+1); hence the graded quotient is a finite abelian group and its rationalization is zero. Proof: expand (1+(g-1))^e; sum on the additive generators; multiply by I^(r-1). Separate the finite generation and annihilation lemmas. No commutativity of G is needed. Source proof: Algebraic Lemma A.

**A2. FORMALIZABLE_NOW: rank-two contraction.** Input: a field K, a K-vector space V of dimension two, a nonzero linear functional ell. Output: exterior-square contraction is an isomorphism onto ker ell, with inverse kappa -> (v wedge kappa)/ell(v) for any v with ell(v)!=0. Prove independence of v. This is pure linear algebra; instantiate ell=log_p only outside the core theorem. Source proof: Algebraic Lemma C.

**A3. FORMALIZABLE_NOW: integral content.** Input: a finite free Z-module M, basis, and nonzero z. Let c be the positive gcd of the coordinates. Output: for every prime p and j>=0, z is in p^j(M tensor Z_p) iff j<=v_p(c); c is independent of unimodular basis change. An initial finite algebra version over Z/p^k is sufficient for the witness projection application, with j<k and zero/truncation cases treated explicitly. Do not assign zero a finite valuation.

**Acceptance:** exact hypotheses; authored modules explicitly built; no sorry/admit; theorem types and axiom inventory reported; conditional arithmetic imports outside the pure algebra files. One clean replay of the chosen source bytes, not repeated default builds.

## Package B — uniqueness and conditional assembly

**B1. FORMALIZABLE_NOW: integer-spacing reconstruction.** Input: a rational q=a/b in lowest terms with b>0, integer m, positive integer D, nonnegative real epsilon, b<=D, |q-m|<=epsilon, and D*epsilon<1. Output: q=m. Instantiate m=36, D=174, epsilon=573/100000; the final inequality is exact rational arithmetic. Do not substitute “174q is integral” for a reduced-denominator bound.

**B2. FORMALIZABLE_NOW: polynomial separation.** Input: f in Z[X], real q with f(q)=0, f(36)!=0, and a proved bound |f(36)|<1. Output: contradiction. Add the factorization/conjugate-product bound as a separate lemma if desired. This avoids making formal algebraic-number or analytic-L-function infrastructure a prerequisite for the core argument. Source proof: Algebraic Lemma E.

**B3. FORMALIZABLE_NOW: abstract primary assembly.** Input: a torsion abelian group decomposed as the direct sum of its primary groups; finite exceptional set S; nonzero integer A; primary groups finite at S and primes dividing A, zero elsewhere. Output: the group is finite. An elliptic-curve instantiation must import Ota's implications and cofiniteness explicitly. Formalizing those imported hypotheses is not proving them.

**B4. FORMALIZABLE_NOW: one-sided common certificate arithmetic.** Input: positive rational B, all prime valuations nonnegative, q=4B, q in the certified compact interval, and the exact 3-primary order plus the abstract primary bounds from COMMON_OBJECT_ANALYSIS.md. Output: B=9, finite total order nine, q=4 times that order. Separate rational integrality, interval uniqueness, and group assembly.

**Acceptance:** theorem statements distinguish the real interval premise, rationality premise, and finite-primary premise. The Python interval result remains an external computer-assisted input unless a separate verified arithmetic checker is deliberately implemented. Do not label the analytic certificate kernel-proved after proving only B1.

## Not formalizable as a solved arithmetic gap

- J_E != 0 for this curve: no construction or proof.
- Existence of the desired integral determinant/zeta object before FIN: no construction.
- Uniform primitive comparison with Ota witnesses: no proof.
- q in Q, or the proposed bounded algebraicity: no proof.
- An archimedean GPR/ETNC comparison: not reduced to a finite algebraic lemma.
- Exact order nine from FIN alone: false inference.

The two packages are suitable for parallel sessions later if the user chooses to run them. Their value is checking reusable deductions and eliminating ambiguity, not resolving the two open arithmetic branches by automation.
