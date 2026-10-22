# Fresh review of the BSD seed release v0.2.0-private-review

**Date:** 23 September 2026  
**Object reviewed:** the uploaded ZIP, not the live GitHub tag or the author's original folders.  
**ZIP SHA-256:** `c52c77c569bfdc63ad774e58056dd0fa57c831af99e75241d72072c2b9124052`  
**Manuscript:** `paper/seed_bsd.pdf`, 32 pages.  
**Review type:** mathematical reading, selected primary-source checks, exact independent arithmetic, selected executable replays. This is not human peer review, a novelty determination, or a complete reimplementation of every calculation.

## 1. Verdict

The revision materially addresses the central omissions identified in the included first Pro report. The lattice estimate, A3 module argument, coefficient-witness soundness argument, and restricted custody reconciliation are now accessible arguments rather than unsupported assurances.

I found **no new counterexample to the algebraic rank-two result, no contradiction in the displayed lattice estimate, and no demonstrated failure of the A3 implication**. I found three specific corrections: an incorrect bibliography binding, an incorrect theorem label, and an inward-rounded displayed numerical radius. None changes the stated outer L-value interval or supplies a counterexample to a principal mathematical result.

The right outcome of this review is **substantive revision supported, with the three local corrections below**, not an unconditional certification of the entire research package. The newly displayed proofs still use substantial imported mathematics. Original large-computation receipts remain trusted rather than freshly regenerated. Those are boundaries of this review and of the release's declared evidence chain, not newly demonstrated mathematical gaps.

The paper remains a partial BSD dossier. In particular, a sufficient implication involving M2 is not a proved nonvanishing result, and the numerical enclosure for q is not a proof of q = 36.

## 2. Executions and independent checks

| Check | Result | What it establishes |
|---|---|---|
| Uploaded archive root manifest | 3,472/3,472 entries match; no missing or unexpected files apart from the manifest itself | Integrity of this uploaded snapshot |
| `python -B tools/verify_release.py` | 18/18 checks pass | Precisely the portable checks the release contains |
| Fresh standard-library exact arithmetic | Pass | Family specialization, invariants, displayed point relation, selected traces, residual irreducibility witnesses, exact decoding of the retained Arb ball |
| Provided regulator/period evaluator, 100 decimal digits and 30 terms | Pass | Reproduction of the published regulator enclosure from the small included calculation |
| Same evaluator, 120 digits and 34 terms | Pass; narrower compatible regulator enclosure | Additional precision/term-count consistency; not an independent implementation |
| Actual legacy and repaired C executables | 12/12 expected outcomes | Known bad witness accepted only by legacy; genuine control accepted by both; truncation, trailing bytes, bad record count and wrong prime rejected |
| Fresh large Fourier/cyclotomic run | Not performed | Original numerical-series computations remain imported |
| Fresh Sage/eclib saturation run | Not performed | Source and retained unconditional index-bound output inspected |
| Fresh Lean build | Not performed | Complete capstone signature inspected; retained build evidence not re-executed |

The C runs used GCC on Linux, with a small CommonCrypto-to-OpenSSL SHA-256 API shim and undefined-behavior sanitization. The group arithmetic and witness predicate were not modified. This is a local cross-platform test, not a reproduction of the original macOS compiler binary.

The full portable suite also replays the symbol-to-coefficient sums, the witness receipt/custody joins, the 2243 height calculation, the finite-field rank calculation, and the existing first Pro arithmetic script. It includes evidence/index/manifest checks and deliberately failing controls. **Eighteen passing checks are not eighteen independently established theorems.**

## 3. Three corrections to make

### C1. The odd-prime Manin support citation names the wrong ARS paper

**Location:** Appendix D.1; `paper/sections/F_lattice_proof.tex`, first paragraph on odd-prime support; bibliography key `ars`.

The text cites `Cor. 3.7` of `ars`. The bibliography makes `ars` the 2012 paper *The modular degree, congruence primes, and multiplicity one*. That paper has a **Remark 3.7**, not the asserted Manin-support corollary.

The result exists in a different paper by the same authors: Agashe–Ribet–Stein, *The Manin Constant*, Pure and Applied Mathematics Quarterly 2 (2006), 617–636, **Corollary 3.7**. For an optimal newform quotient it says that a prime dividing the Manin constant is either 2 or has square dividing the level. For elliptic curves, its Theorem 2.3 also suffices.

**Repair:** add a separate bibliography key for the 2006 Manin paper and change this one citation. Preserve the existing 2012 key for Theorem 3.6(a), which is the appropriate modular-exponent divisibility result.

**Effect:** a real source-binding error, but a repairable one. The required published theorem exists with the required content.

### C2. CNS 5.15 is a theorem, not a corollary

**Location:** Appendix D.2, `paper/sections/F_lattice_proof.tex`.

Replace “Their Corollary 5.15” with “Their Theorem 5.15.” The integrality assertion about the differential of a normalized newform is present in the source.

**Effect:** reference-label correction, not a mathematical failure.

### C3. The printed L-value radius is rounded inward

**Location:** the discussion after Theorem 3.3, `paper/sections/03_rank.tex`.

The manuscript prints a resulting ball with radius `5.709 * 10^-3`. Exact decoding of the retained Arb dump

`8fbdc2e36e453517571bc5e5f9400837 -7a 17625463 -24`

gives radius

`0.005709008823032490909099578857421875`,

which is strictly greater than `0.005709`. Thus the shorter displayed ball is not an outward-rounded representation of the actual certified ball.

The decoded endpoints are approximately

`35.9296047439286684010299311348317953429`

and

`35.9410227615747333828481302925466390929`.

Both are inside the theorem's stated outer interval `[35.929604, 35.941023]`. Consequently the theorem and the ensuing q-interval are not invalidated by this display issue.

**Repair:** write an outward-rounded radius, for example `5.70901 * 10^-3`, and call the display an outward-rounded enclosure rather than the exact resulting ball. This replacement also accommodates truncation of the displayed midpoint.

**Effect:** a genuine rigorous-numerics presentation error, with no change to the theorem's claimed outer enclosure.

A proposed patch containing only C1–C3 is supplied separately. The reviewed release and its historical evidence have not been edited.

## 4. Rank, basis, analytic rank, and regulator are separate claims

### Algebraic rank

The specialization is exact: m = 2243, n = 12, m + 16 n^2 = 4547, and m + 25 n^2 = 5843. All three integers are prime and congruent to 11 modulo 24. The resulting equation is exactly

`y^2 = x^3 - 22735 x^2 + 106272484 x`.

Zywina's Theorem 1.2 gives the abstract Mordell–Weil group Z/2 × Z^2. The surrounding descent also supplies Sha[2] = 0. This part does not depend on the new lattice proof, the A3 bridge, or a large L-series computation.

### Integral basis

The theorem does not itself prove that the displayed P1 and P2 form a full integral basis. The retained Sage/eclib output does contain the stronger certificate claimed by the revision: a computed saturation index bound of 2, a successful 2-saturation, and returned index 1. The independently checked exact relation is

`G = -P1 - P2 + T`, with G = (5843, 210348).

The determinant-one change of basis is valid. I inspected, but did not freshly execute, the eclib calculation or the alternative ratpoints enumeration. This is different from relying on a fixed-prime saturation search alone.

Relevant record: `evidence/src/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/out/s04a_sage.out`.

### Analytic rank

The logical chain is sound: positive algebraic rank and the rank-zero theorem imply L(E,1) = 0; root number +1 then implies L'(E,1) = 0; a valid positive enclosure for L''(E,1)/2 gives analytic rank exactly two.

The large partial sum itself was not recomputed in this audit. Its certificate, formula, tail argument, and repaired coefficient-verifier composition were examined. Decoding its stored Arb ball independently confirms the announced outer enclosure, conditional on the original computation producing that ball correctly.

### Regulator and real period

The small standalone directed-rounding evaluator ran successfully. At 120 digits and 34 terms it gives

`17.7965174724903402988155284169665 < Reg(P1,P2)`

`Reg(P1,P2) < 17.7965174724903402995344445612474`.

This is compatible with, and narrower than, the published enclosure. Its AGM real-period calculation gives

`Omega_E = 0.05608980303887280889661880361586076834227...`.

The factor two relative to the least positive real period is consistently included in the q calculation. The fresh q calculation still imports the original L-value interval, so it must not be described as a fresh computation of L''.

## 5. The lattice appendix now contains the missing argument

The proof has four distinct steps: fix the optimal parametrization and its possible degree-two transfer; eliminate odd factors of c0; bound the 2-primary differential-lattice denominator; pass from rational torsion cusp images to normalized period coordinates.

The odd support theorem, once C1 is corrected, leaves only 4547. Edixhoven's thesis Theorem 4.6.3 has the potentially supersingular branch used by the paper. Its restrictions p > 7, the additive-type exclusions, and absence of a rational degree-p isogeny fit the stated application to type III at 4547. I checked the theorem statement in the primary thesis, not the entire proof of that theorem.

For the 2-primary part, the displayed projected-lattice inequalities give

`v2(c0) + kappa <= v2(deg phi0) <= e' + kappa`,

hence v2(c0) <= e'. The modular-exponent divisibility is in the 2012 ARS paper. The use of the Néron differential lattice is supported by CNS's rational-singularity criterion and integrality theorem.

The integer eight is actually derived. With the four listed components and the imported intersection/genus premises,

`K*mu/12 <= (2*mu - 4*c') - 3*(mu/6 - c' + mu/4)`

`= 3*mu/4 - c'`,

so `K <= 9 - 12*c'/mu < 9`, and integrality gives K <= 8. The signs still work when the chosen infinity component has a positive vertical zero; one needs k_infinity <= 0, not an unjustified equality to zero.

CNS §5.9 does give the component multiplicity formula used here. At p = 2 and valuation three, all four displayed multiplicities equal one. Its discussion of regular local deformation rings and the supersingular Frobenius kernel supports other named inputs. I did not reconstruct all Katz–Mazur models, the genus/mass identities, and their functorial descent from first principles. Those remain the most useful focused arithmetic-geometry review target; their being imported is not itself a counterexample or a missing algebraic step.

Finally, c0 divides 2^8, the selected cE divides 2^9, and rational cusp images have torsion exponent dividing two. The rectangular period lattice then yields the stated 2^-10 symbol grid for the listed unitary cusps. There is no spare power-of-two margin. Uniqueness of a rounded grid point without this membership argument would not establish an exact symbol.

## 6. A3 is substantially more than the earlier outline

I checked the revised Appendix E, its retained signed-bridge proof, and the complete Lean capstone signature. The argument now exposes the components that matter:

1. Exact nonzero-character specialization lengths eliminate finite Z_p-torsion, not just pseudo-isomorphism ambiguity.
2. The residual equivariant presentation is compared with the sign-twisted resolution for u = gamma - gamma^-1. Because conjugation sends u to -u, omitting the sign twist would invalidate the comparison.
3. The character-by-character arithmetic comparison gives equal plus/minus ranks d, rather than only total rank 2d.
4. The plus part surjects onto the rank-two rational Mordell–Weil quotient. At d = 2 this is a surjection between free rank-two Z_p modules and has zero kernel.

This is a meaningful mechanism, not an assumption of the desired Sha vanishing under a different name. It is also not a conclusion from a characteristic ideal alone. Finite submodules and the separate conjugation eigenspaces are precisely where the stronger inputs are needed.

One tempting source objection does not work: BLV §7 allows a Z_p-algebra morphism from Lambda to a finite DVR. Theorem 7.1 is not confined to finite-order characters. This supports the use of the chosen nonzero specializations in the retained proof. BLV's equality is stated in the non-exceptional case; the signed-minus choice and the local hypotheses must remain part of the application.

The Lean signature explicitly assumes the exact length/cardinality comparison, the rank relation, the arithmetic comparison named `harith`, and the control/Kummer maps. It verifies deductions from these inputs; it does not formalize the full Selmer-theoretic construction. I did not perform a fresh Lean build and do not independently certify every arithmetic specialization and equivariant-control identification.

No contradiction was found in the displayed algebra. No M2(p) nonvanishing witness is produced by it. The revision is correct to say that this implication settles no new prime without such an evaluation (or another argument).

## 7. The verifier defect and repair

The defect is real. A fresh direct point count using a square-root multiplicity table gives a_4099 = 86. The malicious order-six witness proposes 68 and repeats factors to claim D = 576. The old executable accepts it. The repaired executable rejects it for duplicate factors. Both accept the genuine control; the repaired executable also rejects the malformed-input cases tested here.

The mathematical repair is coherent. For each prime factor, the nonvanishing scalar-multiplication check gives a lower bound on the corresponding valuation of the order of P. Only with distinct factors may those lower bounds be multiplied into D dividing ord(P). Hasse's interval then isolates the group order. The checked multiplication guard is appropriate to the retained range.

The supplementary scan can therefore repair the specifically identified defect compositionally: original valid group checks plus separately established distinctness and safe products imply the repaired predicate on the same well-formed records. A full rerun is not logically required merely because one missing condition can be checked independently.

However, the ZIP does not contain the billions of witness records. The 3,757-file/2,693,070,671-record scan is a retained result, including deliberate overlapping corpora. The receipt join can be replayed, but hashes and receipts are not proofs that a historical execution occurred. The release correctly preserves that trust boundary. This review is not a proof that no other implementation defect exists.

## 8. C13 custody

The portable checks reproduce the exact limited reconciliation: RESULT.json, STATE.json and RESUME.md differ from historical bindings; nine calculation-input artifacts match their recorded bindings. The old STATE value remains unrecovered.

The downstream coefficient calculation reads the intact symbol tables, not the three changed status files, and returns C13 = 2 in the least-real-period convention and 1 in the full-real-period convention. Thus the identified status changes do not alter that exact downstream arithmetic.

This does not establish that the entire C13 history was unmodified, and it does not rerun the original numerical evaluations that created the symbol tables. The revised wording correctly distinguishes these propositions.

## 9. Final boundary

The uploaded release is internally intact at its declared manifest and portable-check level. It contains substantive written repairs to the two principal mathematical omissions. The three corrections in this review are local and have explicit replacements.

The review does not validate the live GitHub tag, the original folders on the author's computer, the entire large coefficient corpus, every imported theorem composition, a new Lean build, or novelty. It also does not establish FIN, ORDER9 or Q36. Those facts should not be conflated with a finding that the rank-two or A3 claims are false.

The most useful next mathematical review is narrow: the four-component integral-model application in Appendix D, and the actual equivariant residual/control realization behind I3 in Appendix E. The next computational upgrade is a clean repaired-verifier/engine replay of a declared corpus, not another multiplication of passing manifest checks.

## Primary sources consulted

- David Zywina, *There are infinitely many elliptic curves over the rationals of rank 2*, arXiv:2502.01957v1, Theorem 1.2 and its following descent discussion. Source: `https://arxiv.org/pdf/2502.01957v1`.
- K. Cesnavicius, M. Neururer, A. Saha, *The Manin constant and the modular degree*, author PDF, §§5.8–5.10, Theorem 5.15, Proposition 6.2, Proposition 6.10, Theorem 6.12 and §7. Source: `https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf`.
- A. Agashe, K. Ribet, W. Stein, *The modular degree, congruence primes, and multiplicity one*, Theorem 3.6(a) and Remark 3.7. Source: `https://www.math.fsu.edu/~agashe/math/moddeg3.pdf`.
- A. Agashe, K. Ribet, W. Stein, *The Manin Constant*, 2006, Theorem 2.3 and Corollary 3.7. Source: `https://wstein.org/papers/ars-manin/agashe-ribet-stein-the_manin_constant.pdf`.
- S. J. Edixhoven, *Stable models of modular curves and applications*, 1989 thesis, Theorem 4.6.3, printed pp. 60–61. Source: `https://websites.math.leidenuniv.nl/edixhoven/publications/1989/phd-thesis.pdf`.
- M. Bertolini, M. Longo, R. Venerucci, *The anticyclotomic main conjectures for elliptic curves*, arXiv:2306.17784v2, hypotheses, §§5 and 7, especially Theorem 7.1. Source: `https://arxiv.org/pdf/2306.17784v2`.

Exact scripts and logs accompany this report. No part of the proposed correction patch has been applied to the reviewed snapshot.
