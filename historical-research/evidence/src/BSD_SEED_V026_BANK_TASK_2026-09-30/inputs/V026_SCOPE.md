# What v0.2.6 banks: the scope list (Claude, 2026-09-30)

Revised 2026-09-30 after the Fable coordinator's check (PASS with three wording fixes):
- the B.20 version caveat;
- the B.20 ordinary-coverage sentence;
- the frontier wording, where "equivalently in effect" became "each of which implies" and the converse of (i) is not
  claimed.

Revised again 2026-09-30 after Codex's check (CONFIRMED_WITH_CORRECTIONS; `inputs/CODEX_THREE_BRIEFS_REVIEW_REPORT.md`).
Codex's corrected copy was installed. The one change: the label placement follows the v0.2.5 precedent.

**Rules for every item.**
- Bind each governing file by path and sha256.
- The claim text never exceeds its grade.
- The review labels must be exact. Model readings are checks at their recorded grades, not a human referee and not a
  formal verification.

## Review label (verbatim in the claims verification record of B.20–B.22)

"Derived by Codex (OpenAI). Independent review by ChatGPT Pro (OpenAI): ACCEPT_AT_IMPORT_GRADE. The source statements
were checked by Claude Opus 5.5 and Claude Fable 5.1 (Anthropic); the Δ-component bridge by Claude Fable 5.1; the Part B
deductions by Claude Opus 5.5. The author-hosted CLW revision is byte-identical across three independent downloads
(sha256 0686fa41…d036fb98); arXiv v1 is a different file. Not a human review; not formalized."

The exact review label is supported by the recorded reports at their stated scopes. Bind the specific Fable source/Δ-bridge check and retrieval records if attributing those additional checks in the release; addenda reporting them are not a fresh replay here. Repeated byte-identical downloads verify source identity, not independent theorem proofs. Keep this exact label in the claim verification/evidence record.

In the paper and README, use the mathematical grades and source citations plus a one-line provenance clause, as S.3K
did in v0.2.5. For example: "derived by Codex (OpenAI) and independently reviewed by ChatGPT Pro (OpenAI), with source
and deduction checks by Claude models (Anthropic); not a human review; not formalized". This is consistent with
TASK.md.

The Fable source-statement and Δ-component bridge check (CLW l.983; at k = 2 the proved component ω^{k/2} = ω is the
cyclotomic one) is recorded in `~/BSD_BUILD_MAP/UNIFORM_STEP_REDUCTION_SHEET_2026-09-29.md` §9, with sha256
e92688976c4a51f6777a5bde4bb74c61979d9c5a99803304be05111746ec5707 on 2026-09-30. Claude's source-statement and Part B
checks are addenda 25 and 28 in inputs/.

## IN

### 1. NEW B.20: a unit Kurihara witness exists at every good p ≥ 5 (the maintainer may choose the id)
- **Statement.** For every prime p ≥ 5 of good reduction for E, including the supersingular primes and 19, 59 and 487,
  M_∞(δ) = 0. Hence some squarefree Kato conductor n, which may depend on p, has δ_n ≢ 0 (mod p).
  - The bad primes 2243, 4547 and 5843 and the primes p ≤ 3 are not covered.
- **Release grades:** PROVED_WRITTEN and IMPORTED_PREPRINT; kind THEOREM. "Derived" describes the application, not a new grade identifier.
- **Imports:**
  - Castella–Liu–Wan, "Kato's main conjecture for nonordinary modular forms", author-hosted revision dated
    2026-09-21 (sha256 0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98), Theorem A. Its (ram) holds
    via ℓ = 2243 (v(Δ) = 1); k = 2 < p; p-regular since a_p = 0 at supersingular p. The arXiv v1 required squarefree
    N; the revision does not.
  - Castella–Sano, arXiv 2601.14504v1: Theorem A and Corollary A (nonordinary) and Theorem B (ordinary).
  - The retained seed inputs: ρ̄_p surjective for odd p; ρ_p surjective for p ≥ 5; the Manin constant divides 2^9;
    Tam = 16.
- **Version caveat (must appear in the B.20 text).** The CLW revision is author-hosted and not on arXiv as of
  2026-09-30. arXiv 2608.29470 lists only v1, the squarefree-level version; this was checked live on 2026-09-30. The
  revision is pinned by the sha256 above. A later version could change the hypotheses of Theorem A.
- **Ordinary coverage (must appear in the B.20 text).**
  - The ordinary primes are covered by Castella–Sano Theorem B as printed. Its hypotheses are p > 3, (sur) and
    p ∤ c_φ, and its proof cites [Wan15, BCS25] for the ordinary main conjecture.
  - 19, 59 and 487 are ordinary for E (a_19 = 4, a_59 = −4, a_487 = −28). The worker re-derives these with PARI
    `ellap` and records the output. Theorem B has no hypothesis that excludes them.
  - The Euler factors at 2243 and 5843 are nonunits at these primes (2242 = 2·19·59, 5844 = 12·487). Both
    formulations retain these factors and neither cancels them, so they create no extra exception (Pro review
    PART_A_COVERAGE, A3).
  - The supersingular primes come from the CLW revision, because Theorem B's supersingular case requires squarefree N.
- **Governing files:**
  - `~/BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/` (REPORT, NEW_INPUT_APPLICATION, SOURCE_REGISTER, SOURCE_BINDINGS);
  - the Pro review in `~/BSD_UNIFORM_SYNTHESIS_REVIEW_CHECK_CODEX_2026-09-30/input/BSD_UNIFORM_SYNTHESIS_INDEPENDENT_REVIEW_2026-09-30/`
    (RETURN, PART_A_COVERAGE, SOURCE_AUDIT);
  - `~/BSD_UNIFORM_SYNTHESIS_REVIEW_CHECK_CODEX_2026-09-30/REPORT.md` and its FRESH_SOURCE.json;
  - Claude's check REPORT, addenda 25 and 28.

### 2. NEW B.21: the minimal unit-witness length equals the Selmer dimension
- **Statement.** With r_p := min{ν(n) : δ_n ≢ 0 (mod p)}, for every good p ≥ 5: r_p = dim_{F_p} Sel_p(E/Q). This is
  even and ≥ 2, and r_p = 2 ⟺ Sha(E/Q)[p^∞] = 0. It also excludes a hypothetical divisible part; no finiteness of
  Sha is assumed.
- **Release grades:** PROVED_WRITTEN and IMPORTED_PREPRINT; kind THEOREM. Retain every named import from B.20 and Kim.
- **Inputs:**
  - Kim, arXiv 2203.12159v6, Thm 1.8: ONLY its Sha-independent clauses (the corank and the higher Fitting ideals);
  - parity (root number +1);
  - the split dual Kummer sequence and Nakayama.
- **Governing:** the Pro review's PART_B_DEPTH.md §§B1–B3; addendum 28 (Claude's check).
- **Mandatory scope sentence:** "This is an identity, not an upper bound. The abstract dual module X = Z_p² ⊕ (Z/p)² needs four generators, with Fitt₂(X)=(p²), Fitt₃(X)=(p), and Fitt₄(X)=Z_p. It is compatible with M_∞=0 and first unit index four. This is a module countermodel to an inference from primitivity alone, not a claim about the seed at an uncomputed prime."

### 3. NEW B.22: the character-depth criterion
- **Statement.** Let p ≥ 5 be good, let K/Q be real cyclic of degree p with its actual conductor m prime to pN (composite allowed),
  and let χ be a faithful character. If v_{ζ_p−1}(χ(θ_K^MT)) < 4 for the full Bullach–Honnor-normalized Mazur–Tate
  element (Def. 2.2, total real period Ω⁺ = 2ω₁), then Sha(E/Q)[p^∞] = 0.
  - The inequality is STRICT. "≤ 4" is insufficient: the group-ring countermodel (R/(t))² ⊕ (R/(p,t))² contains t⁴
    in its Fitting ideal.
- **Release grades:** PROVED_WRITTEN and IMPORTED_PREPRINT; kind CONDITIONAL. The sufficient implication is derived from Bullach–Honnor, arXiv 2511.07203v1, Hyp 1.2 and Thm 1.4(b); plus
  B.21 and restriction (E(K)[p] = 0, because the image contains SL₂(F_p)).
- **Governing:** PART_B_DEPTH.md §§B4–B6; Codex's DEPTH_TARGET.md; addendum 28.

### 4. The frontier statement (paper §11, the README status, and the uniform-step open item)
- **State the open uniform target exactly:** "Find one finite set S containing {2,3,2243,4547,5843} and an independent argument that, for every p outside S, either a two-prime mod-p unit Kurihara witness exists or dim_{F_p} Sel_p(E/Q) ≤ 3. Under B.21 these two conditions are equivalent to each other and to Sha[p^∞]=0. A faithful value of the full BH-normalized element of a real cyclic degree-p field at its actual conductor prime to pN, with depth strictly below four, is another sufficient condition. No converse from Sha vanishing to existence of that character value is claimed. Fields, conductors and estimates may depend on p."
- **Wording rules:**
  - Say "current known frontier". Never "only/all that remains".
  - No claim that no method exists. Instead: "no applicable theorem was located in the screened sources".
- Mark only the V025 watch item about applicability of Castella–Liu–Wan at this nonsquarefree seed level RESOLVED. The uniform upper-bound task remains OPEN.

### 5. OPTIONAL: refresh O.1/O.2's stale wording ("p ≥ 17", "< 2601")
Bring them to the current thresholds (the primes ≤ 47 are settled; 25,281), without changing their grade. If the spec's
structure makes this non-trivial, leave it and list it in CHECK_REQUEST.

## OUT
- Any claim of a uniform bound, finite support, FIN, ORDER9 or Q36.
- Any identification with the historical E11/288 scalars (no normalization comparison has been done).
- U22 material.
- Third-party page renders (the source_checks PNGs). Bind them by path and sha256 only; do not copy them (the K2
  precedent).
