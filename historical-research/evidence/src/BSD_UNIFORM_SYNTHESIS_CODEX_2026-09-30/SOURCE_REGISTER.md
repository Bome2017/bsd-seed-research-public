# Source register and limits

Accessed 2026-09-30. PDF bytes and extracted text are saved under `sources/`; exact hashes are in `SOURCE_BINDINGS.json` and the manifest. Mutable author URLs are pinned by the saved bytes. Deep theorems are imported, not reproved.

## Decisive sources

1. **Castella–Liu–Wan, current author revision**, dated September 21, 2026, 45 pages: <https://web.math.ucsb.edu/~castella/CLW2.pdf>.
   - Theorem A (printed p.3); standing large-image hypothesis on p.2; section 1.5 on p.7.
   - Sections 2.1, 2.4, and 2.5, especially Lemma 2.10, integral normalization, Conjecture 2.19 and Remark 2.20.
   - Section 5.6, (5.18), (5.21)–(5.22), for the explicitly cited Castella–Sano determinant equivalence. The rank-zero application (5.23) is not used.
   - This is the new substantive source input to the seed application.

2. **Castella–Liu–Wan, older arXiv v1**, August 29, 2026: <https://arxiv.org/pdf/2608.29470v1>.
   - Compared Theorem A and its squarefree-level requirement. This version is kept to document what changed, not used as the theorem covering the seed.
   - Author index: <https://web.math.ucsb.edu/~castella/>. Its note about newer author versions was checked directly.

3. **Castella–Sano**, arXiv 2601.14504v1: <https://arxiv.org/html/2601.14504v1>.
   - Sections 1.1.1–1.1.4: definitions, parity, Theorem A, Corollary A, ordinary clause of Theorem B.
   - Section 2.2: the Euler product, determinant Conjecture 2.2.2 and equivalence Proposition 2.2.3.
   - The author copy <https://web.math.ucsb.edu/~castella/Kurihara.pdf> was also checked. It is dated January 20 rather than the arXiv text's January 22; the decisive statements agree. The application cites the pinned arXiv version.

4. **Chan-Ho Kim**, arXiv 2203.12159v6: <https://arxiv.org/html/2203.12159v6>.
   - Theorem 1.8, especially the higher Fitting ideals and paired structure. This separates nonzero p-adic order, unit index, corank, and finite torsion.
   - Local PDF and text copied from the earlier geometric-source screen, with hashes newly recorded. No output from its earlier checks is treated as a theorem proof.

5. **Bullach–Honnor**, arXiv 2511.07203v1: <https://arxiv.org/html/2511.07203v1>.
   - Hypothesis 1.2, Theorem 1.4(b), Definition 2.2; classical Selmer Fitting membership and the full projected theta element.
   - Uses the retained September 27 normalization/restriction audit. The low-depth extension in `DEPTH_TARGET.md` is derived here. No extra finite-Sha assumption is attached to the classical-group conclusion.

6. **Kriz–Nordentoft**, arXiv 2310.20678v3: <https://arxiv.org/html/2310.20678v3>.
   - Definitions 5.11–5.12, Corollaries 5.16 and 5.20, and the discussion distinguishing the required Kurihara length from an output valuation bound.
   - Saved PDF labels the adjacent strict-corank discussion Remark 5.2. Use section/content anchors rather than transferring remark numbers between renderings.
   - These results propagate a supplied unit-witness length. They do not give an independent bound of two for the seed.

## Adjacent sources checked for an upper-bound mechanism

- **Kriz–Nordentoft, horizontal moments**, <https://arxiv.org/html/2507.01836v1>. The inspected moment formulas involve horizontal invariants; they do not supply an independent bound below four for this seed. This source was already in A1; no novelty is claimed for noticing it again.
- **Burungale–Castella–Grossi–Skinner**, <https://arxiv.org/html/2312.09301v2>, Theorem C / Corollary C. A nonzero Kato-system order and a residual unit-witness order must not be conflated. The precise Kim structure theorem governs the deduction in this return.
- **Keliher–Park, distribution in prime cyclic extensions**, <https://arxiv.org/html/2607.01126>, Theorems 1.1, 5.1 and the proof of Theorem 1.1. The fixed-p, ERH-conditional distribution uses twisted/relative Selmer structures to control rank growth in extensions. No bound for the original curve's p-Selmer group follows from its stated result. This is a scoped nonapplication, not a claim that arithmetic statistics can never help.
- **Residual modular-symbol distribution and central anticyclotomic nonvanishing:** prior A1 source reports were checked for the previously identified object mismatch. Individual-symbol distribution, a different twist family, or complex nonvanishing is insufficient without a map to the required low-depth coefficient. No full repeat of that literature screen was undertaken.

## Scope of verification

No all-p image proof, prime certificate corpus, Lean development, Route K implementation, or foundational Euler-system theorem was rerun. The exact local discriminant check is the only fresh seed arithmetic. Algebraic consequences in `DEPTH_TARGET.md` are written deductions, not machine-formalized theorems. No theorem of uniform depth below four was located or proved.
