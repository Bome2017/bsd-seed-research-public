# First-pass hostile review of seed_bsd.pdf, version 0.1.1

Review date: 23 September 2026.
Manuscript SHA-256: `11599b2b022ce9d21ad7cf5a79b8232c7f67c429501212c88abda95166b7e2ab`.

## Scope and recommendation

This is a review of the actual 25-page PDF, with selected primary-source checks and a small independent exact-arithmetic script. It is not an audit of the full evidence repository, an end-to-end numerical replay, a Lean rebuild, a novelty determination, or human peer review. A matching seed-BSD repository could not be located through the connected GitHub searches. The PDF contains repository-relative paths but no repository URL or release commit.

Recommendation: **major revision before presenting the document as a complete proof paper for its advertised main results.** It can be circulated as an explicitly provisional technical dossier for targeted expert consultation. The central problem is not that it claims full BSD—it explicitly does not—but that it alternates between proof-paper and project-ledger standards. Several consequential assertions cannot be checked from the manuscript as supplied.

No independent contradiction to the algebraic rank-two claim was found. The first-pass checks positively verify the exact specialization of Zywina's theorem; full basis saturation and the analytic certificates require separate evidence.

## Reproducible checks actually performed

Run `python3 independent_checks.py`. The program uses only Python's standard library and writes `independent_checks.json`.

It checks the displayed c4, c6, discriminant, j-invariant, coordinate translation, points, relation G = -P1-P2+T, conductor factor product, small-prime traces, the full supersingular list below 2000, the multiplicative split/nonsplit tests, the numerical coefficient in the displayed D5 determinant, the interval arithmetic relating the printed L''/2 and Omega*Reg bounds, the Eichler mass formula, and Frobenius irreducibility witnesses.

It does NOT independently determine the conductor by Tate's algorithm, prove global saturation, evaluate the original L-series or heights, prove the Manin bound, verify the coefficient corpus, or compile Lean. The interval check is a consistency check on supplied bounds, not a new analytic certificate.

## I1 — Main proof obligation: Theorem 2.4 (page 5)

**Classification:** missing load-bearing derivation in the supplied manuscript; not a demonstrated false theorem.

Theorem 2.4 asserts c0 = 2^a with a <= 8, an appropriate parametrization constant cE dividing 512, and a 1/1024 lattice for the unitary-cusp symbols. The explanation says that the numerical bound is derived from Pasten section 10, CNS 6.12(c), and ARS 3.6(a), but does not present that derivation.

The exponent bound, not merely odd-prime support, is indispensable to exact real reconstruction. Source labels cannot replace the calculation that produces the integer 8. Pasten's general boundedness statement is not on its own the numerical inequality a <= 8, and the cited rational-singularity result is not on its own such an inequality either.

**Required repair:** insert a proposition with the full inequality chain and its constants, check every hypothesis, name the optimal curve and exact chosen parametrization, show transfer across the degree-two isogeny, and then prove the symbol lattice from rational unitary cusps and torsion. 'The modular parametrization' is ambiguous: composition with multiplication by an integer changes its Manin constant. State which normalized map is being bounded.

Do not downgrade all numerical results automatically: the proof may be in the repository. But a main theorem of this importance must have an accessible, exact supporting argument.

## I2 — Main proof obligation: Theorem 7.3 (page 12)

**Classification:** inadequately presented new proof; formalization scope must remain explicit.

The three-step outline is not enough to assess the principal new bridge. BLV supplies imported results, but the equivariant comparison and resulting rank balance are added mathematics. Their equations and maps should appear in the paper or a precisely linked proof appendix.

**Required repair:** give named lemmas for (a) exact specialization and elimination of the finite Z_p-torsion subgroup; (b) the equivariant residual presentation, with kernel/cokernel eigenspaces and the sign-twisted resolution; (c) the final rank-two surjection and kernel vanishing. State all four arithmetic inputs and all structural module inputs mathematically. Associate each with the exact source theorem or proof supplied in the paper, and each Lean theorem with its complete hypothesis list.

Important: the rendered PDF correctly uses the reduction `bar(F^-)` in defining d. Its distinction between residual order and ordinary Iwasawa lambda should NOT be marked as an error. Lean verification is conditional on the imported inputs; a clean build is not a verification of those inputs.

## I3 — Verifier repair and the retained corpus (Appendix B, page 22)

**Classification:** consequential evidence-reconciliation obligation.

The disclosure that the old verifier accepted a false coefficient at q=4099 is a soundness issue, not merely a regression-test anecdote. The separate distinct-factor/overflow scan might rehabilitate the retained runs without redoing every group calculation, but that requires a precise compositional argument.

**Required repair:** state the witness format and the mathematical acceptance predicate; identify the defective and repaired code versions; prove that the repaired predicate equals the old valid group checks plus exactly the new conditions that were scanned; bind original acceptance receipts and the scan to the same complete witness bytes; document ranges, overlaps, completeness, and malformed-input handling. Explain why the supplied witnesses determine the group order, rather than just a possible divisor of it.

A scan on the missing conditions can be sufficient if those implications and bindings hold. It is not sufficient merely because all scanned hashes match. Conversely, lack of a new billion-record end-to-end run does not by itself refute the certificates.

## I4 — Unresolved C13 custody claim (Appendix D, page 23)

**Classification:** unsupported scope assurance.

The manuscript calls the custody discrepancy unresolved while asserting that it does not affect the mathematics. Those statements require reconciliation. The reader needs the exact altered paths, before/after hashes, affected claims, and the replacement or surviving evidence chain.

**Required repair:** either document why only non-input material changed, bind the theorem to a fully intact alternative certificate, or state precisely which reproducibility claim remains qualified. Do not silently refresh a manifest. Preserve the old evidence and describe the additive supersession.

## I5 — Residual surjectivity (Theorem 2.3, page 5)

**Classification:** proof omitted, with a concrete short repair available.

Listing inertia, a transvection and Mazur is not a proof covering every odd prime, especially when the proposed transvection prime equals the residual prime.

The exact script verifies these Frobenius witnesses excluding reducibility at the possible odd rational prime-isogeny degrees:

| residual primes ell | good q | a_q | discriminant a_q^2-4q |
|---|---:|---:|---:|
| 3,7,11,19,43,67,163 | 5 | -2 | -16 |
| 13,17,37 | 7 | -2 | -24 |
| 5 | 17 | -6 | -32 |

Every displayed discriminant is a nonsquare modulo the corresponding ell. After stating Mazur's prime-isogeny list, these exclude invariant lines. Use the Tate transvection at 2243 for ell != 2243, and the multiplicative prime 5843 with discriminant valuation 2 for ell = 2243. Give the elementary lemma that an irreducible subgroup of GL2(F_ell) containing a transvection contains SL2(F_ell), then use the cyclotomic determinant. Cite the standard integral lifting result separately for ell >= 5.

This is support for the stated result, not a claim that the result is false.

## I6 — Rank and saturation (Theorem 3.1, page 6)

**Classification:** applicability checks pass; saturation evidence still needs access.

Explicitly supply m=2243, n=12 in the manuscript. Then m+16n^2=4547 and m+25n^2=5843; all three are prime and 11 modulo 24. Zywina Theorem 1.2 directly supplies the abstract rank and torsion, and its descent supplies Sha[2]=0. This takes very little space and removes an avoidable lookup.

The manuscript correctly distinguishes this from proving the displayed points form a global integral basis. Include the actual global saturation bound, eclib version, command, and certified output. A bounded saturation search is not enough, and the manuscript correctly says so.

## I7 — Undefined theorem objects and scopes (§§9–10, pages 16–19)

**Classification:** statements not fully evaluable as written.

Examples: h_p's precise minimization domain; the module and local comparisons in Theorem 9.2; delta_n, rho_n and J_E in Theorem 9.3; class L3 in Obstruction 10.3; the normalized Eisenstein kernels and residuals in 10.4; the exact function class excluded in 10.5.

Saying that an obstruction has a limited scope is not enough if the scope is not defined. In particular a continuous Mellin representation alone does not, without additional precise uniqueness and convergence hypotheses, establish every broad exclusion of Dirichlet-series or Euler-product representations.

**Required repair:** define the objects, hypotheses and excluded class and provide the argument; otherwise convert these into explicitly unverified summaries of archived attempts and move them out of the theorem sequence. A private project codename is not a mathematical definition.

## I8 — Allegations about sources (§10.2 and Remark 8.3)

**Classification:** inadequate documentation and unnecessarily strong attribution.

Destrempes–Malinin is not identified in the bibliography. The counterexample alpha=4+i, P=(4+i), p=17 refutes the displayed unrestricted implication. It does not, on its own, establish which exact theorem in a named paper uses that implication under all of its actual hypotheses.

**Required repair:** give full source metadata, exact theorem/lemma/page, the relevant original hypotheses, the invalid step and the scope of the consequence. Until then replace 'A defective source' with a description of the precise inference ruled out.

Likewise the manuscript does not need a categorical finding that Jones lacks a converse. State that this proof uses only his forward implication, with finiteness and nondegeneracy independently supplied. An alleged gap in a published attribution should be a separately documented note, not an unsupported aside.

Published results can legitimately be imported. A failed internal reconstruction of Skinner–Urban does not by itself downgrade Skinner's stated theorem. Separate the import actually used from the history of an unsuccessful alternate proof.

## I9 — Concrete local corrections

1. **Page 6, Theorem 3.3:** 'no floating-point step anywhere in the enclosure' is false for Arb. Its balls use floating-point midpoints and radii with rigorous error propagation. Replace with 'no uncontrolled floating-point approximation is used'.
2. **Page 8, Theorem 4.4:** 'all 72+72 symbols at 81' needs correction. There are phi(81)=54 unit residues, so all plus and minus values at denominator 81 give 54+54=108 entries. 72 per sign could mean 18 at denominator 27 plus 54 at denominator 81, but that is a different inventory and should be stated explicitly.
3. **Page 8, Lemma 4.1:** Hasse plus parity excludes a_p congruent to 1 for p>=7, not by itself for p=5. Cross-reference the already verified a5=-2 (or #E(F5)=8).
4. **Pages 7 and 13:** distinguish L_{p,omega1} from the Stein–Wuthrich full-real-period normalization consistently; the displayed coefficient table uses the factor of two correctly. A unit-factor invariance does not remove the need to name the convention.
5. **Page 14, D8:** evaluator reliability is not a mathematical assumption of the implication K!=0 => Sha_p=0. Move it into the certificate-production section. K is defined independently of the implementation.
6. **Page 20:** FIN need not come from one theorem covering every prime. Cofinite vanishing plus finiteness of every remaining primary component suffices. Fixed bad primes can be handled separately. Preserve alternative routes rather than making M2 nonvanishing compulsory.
7. **Page 13:** replace the blanket 'Kato's divisibility excludes primes dividing the conductor' by the exact version/theorem being used and its excluded case.
8. **Notation:** separate rational basis P1,P2 from Gross point P1; distinguish the cyclotomic coefficient C_p from the class-group module also denoted C_p; define gamma/kappa and the two period conventions in one location.

## I10 — Repository access and release design

**Classification:** reproducibility cannot be assessed from the supplied release.

Add a repository URL, immutable release tag and full commit hash to the first page or data-availability section. Distinguish a quick replay of downstream sums from a full verification of the L-series certificates, and list the external data needed for each. State sizes, access or regeneration instructions, and expected resources.

`verify_release.py` checking hashes and replaying coefficient sums must not be described as a complete independent certification of every upstream theorem. Give a per-claim coverage matrix.

Second-pass priorities: proof of the Manin exponent bound; the exact A3 Lean hypotheses and theorem-to-source bindings; original/repaired coefficient verifier and corpus receipt reconciliation; C13 custody; global saturation; source/control chain for the 3-primary result; D5 exact arithmetic; clean-environment release commands.

## I11 — Scientific contribution and document structure

**Classification:** major presentation and positioning issue.

The paper is currently part theorem article, part evidence ledger, part research diary, and part collaboration prospectus. The novelty statement is too broad to identify a principal result. 'The results are new for this curve' is not enough to establish a methodological contribution.

Stein–Wuthrich already report rank>=2 primary-Sha computations for 1,534,422 eligible curve/prime pairs of conductor <=30000. Distinguish that established method from (i) the high-conductor certified implementation, (ii) any genuinely new conditional bridge, and (iii) elementary restatements and archived failed attempts.

A defensible main paper would foreground the arithmetic theorem, the precise new bridge and its full proof, and the certificate methodology. Move operational statuses, cloud prices, authorizations, most withdrawn claims, and unrelated-curve achievements to the repository. Maintain an immutable historical register there rather than requiring an expert to reconstruct the project chronology.

The high conductor establishes computational difficulty; explain separately why this particular curve is mathematically informative or why the method generalizes.

## Suggested immediate revision order

1. Expose complete proofs of Theorem 2.4 and the added arithmetic steps of Theorem 7.3.
2. Resolve verifier/corpus and C13 evidence reconciliation for the exact release.
3. Add the short Zywina specialization and surjectivity proof.
4. Correct the explicit counting, numerical-language, normalization and quantifier issues.
5. Define or demote the under-specified statements in §§9–10.
6. Publish a pinned evidence release and a small quick-start review path.

## Selected external sources checked

- D. Zywina, arXiv:2502.01957v1, Theorem 1.2 and its surrounding statements: https://arxiv.org/html/2502.01957v1
- H. Pasten, arXiv:1705.09251v4, section 10: https://arxiv.org/html/1705.09251v4
- K. Cesnavicius, M. Neururer, A. Saha, arXiv:1911.09446, Theorems 6.12 and 7.2: https://arxiv.org/pdf/1911.09446
- M. Bertolini, M. Longo, R. Venerucci, arXiv:2306.17784v2, relevant control and main-conjecture statements: https://arxiv.org/html/2306.17784v2
- W. Stein and C. Wuthrich, paper and author-hosted summary: https://wstein.org/papers/shark/
- FLINT/Arb representation documentation: https://flintlib.org/doc/index_arb.html and https://flintlib.org/doc/using.html

These source checks are not a full reproof of each imported theorem or all source compositions in the manuscript.
