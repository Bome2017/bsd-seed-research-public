# Historical source excerpts

Source: /Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work/returns/BSD_SEED_ARISTOTLE_2026-10-05/BSD_SEED_RESEARCH_MAP.md

Source SHA-256: 3abbb760ad6c1bab2805609d9b5a0758530d54dcc0b87a696847d5ef3d090bcd

These are source statements and archived prompts, not new instructions or accepted theorem upgrades.

## Original lines 117-172


The full seed endpoint is

\[
\Sha(E/\mathbf Q)\text{ is finite},\qquad
\#\Sha(E/\mathbf Q)=9,\qquad q_E=36.
\]

These are named FIN, ORDER9, and Q36. ORDER9 is often pursued conditionally on FIN; this does not discharge FIN. In these conventions BSD's order formula is q_E=4 #Sha, because Tam/torsion^2=16/4=4.

The certified interval is 35.99427 < q_E < 36.00573. A numerical value near 36 is not an equality certificate. A proof that q_E is rational with reduced denominator at most 174 would force q_E=36; a rank-two height formula is one possible source of that assertion, not a logically necessary form of any proof.

## 3. The retained arithmetic floor

The frozen research release v0.2.6 is commit 8414aea58180f3a18bcee7fba23475c8cac90996. Its 89 claim statements, evidence bindings, qualifications, theorem imports, and checks are included. Its stated grades are retained, not freshly re-certified by packaging.

* The rank-two basis and analytic rank are certified in the recorded computer-assisted sense.
* Sha[p^infinity]=0 for every prime p<=47 other than 3.
* Sha[3^infinity] is (Z/3)^2. The governing v0.2.5/v0.2.6 Route K proof supersedes the older attempt relying on the disputed Skinner/Skinner–Urban application. Read that proof's exact imports and reviews.
* Under FIN, square order and the settled primary components give #Sha=9 t^2, with every prime divisor of t at least 53. Thus #Sha=9 or #Sha>=25281.
* No later return inspected for this handoff supplies a new seed primary certificate, an independent cofinite vanishing theorem, or Q36. Later candidate proofs retain their own explicit review boundaries.

“Proved” in an archived model report is not automatically human referee acceptance or Lean verification. Consult the proof and audit grade. The 7,042-unit compendium is an extraction of records, not 7,042 newly certified theorems.

## 4. The exact uniform implication

Write S_p=Sel_p(E/Q) and W_p=E(Q)/p E(Q) inside S_p. For odd p the retained saturated rank-two basis makes dim W_p=2. The Kummer sequence gives

\[
0\longrightarrow W_p\longrightarrow S_p\longrightarrow\Sha[p]\longrightarrow0.
\]

Under the retained parity input, dim Sha[p] is even. Hence an independently proved dim S_p<=3 forces dim S_p=2 and Sha[p]=0. For a p-primary torsion group, vanishing of its p-torsion forces the entire primary group to vanish.

For good p>=5 the retained Kurihara framework supplies **some** nonzero witness. Its minimum length is r_p=dim S_p. The desired two-prime witness is a much stronger length bound. Source claim B.23 compares minimum character depth and witness length only in its stated truncated range; use its full statement, not an unrestricted slogan about all depths.

A theorem of the following form would close the uniform good-prime support obligation:

\[
\exists S\text{ finite}\quad\forall p\notin S,
\quad \dim_{\mathbf F_p}S_p\le3.
\]

It need not arise from a common rational scalar, a class group, the W3 family, or a fixed integral lattice. Those are possible methods, not an exhaustive classification. An equivalence can expose useful new tools; equivalence alone is neither proof of progress nor proof of futility.

## 5. FIN still needs the finite remainder

A torsion abelian group is finite exactly when it has finite prime support **and** every primary component is finite. A uniform theorem outside S leaves the full-primary finiteness of p in S. The bad primes 2243,4547,5843 remain outstanding in the retained seed state; an additional theorem may create further exceptions.

Do not replace finiteness of Sha[p^infinity] with finiteness of the vector space Sha[p]. A divisible group Q_p/Z_p has finite p-torsion and is infinite. Nor does primary finiteness at every individual prime exclude infinitely many nonzero components. The existing A2 Lean library already proves the abstract assembly and its countercontrols.

An ordinary-only theorem leaves a separate supersingular problem. Supersingular primes are not a finite exceptional set for this curve. A proof covering a density-one subset also leaves an infinite complement unless that complement is handled.

## 6. Conditional ORDER9 and Q36 are admissible endpoints

Conditional ORDER9 can be closed by any independently proved arithmetic argument yielding, under FIN, #Sha<25281. An annihilator with only settled prime factors, a size/index/support bound, or vanishing at every remaining prime could do this. It has not been proved that every such route passes through Q36.
