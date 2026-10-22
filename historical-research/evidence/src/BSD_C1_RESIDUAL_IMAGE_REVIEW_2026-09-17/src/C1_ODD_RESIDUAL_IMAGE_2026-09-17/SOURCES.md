# Source and execution register

Date: 2026-09-17. Only the source facts identified below are imported. The all-odd-prime assertion is the author-side deduction in PROOF.md, not a theorem claimed to be printed in any of these sources.

## Supplied project source

`input/00_REVIEW.md`: latest attached bounded central-involution review, preserved byte for byte. SHA-256 is recorded in EXACT_CHECK_RECEIPT.json. Read in full. The current turn does not independently rerun its checker or its exhaustive lattice computation, and does not verify its separate 50-entry manifest (not supplied as mounted bytes in this turn).

The source recommends adoption with its three wording adjustments and retains all the listed non-exclusions. It reports no class-group/Selmer/Sha computation and no shared-ledger or seal edit.

## Primary papers read

1. David Zywina, *There are infinitely many elliptic curves over the rationals of rank 2*, arXiv:2502.01957v1.
   https://arxiv.org/pdf/2502.01957
   Read: Theorem 1.2; statements about the two independent points and Sha[2]; invariant and bad-reduction passages; Lemma 4.1 and its argument recovering (m,n) from j. The theorem page was also checked as a page image. The paper supplies the rank/2-primary input; no claim of novelty is made for that input.

2. Terence Tao and Tamar Ziegler, *The primes contain arbitrarily long polynomial progressions*, arXiv:math/0610050v2.
   https://arxiv.org/pdf/math/0610050
   Read: Theorem 1.3 (positive relative upper density version). Its application to primes 11 modulo 120 and the three displayed polynomials is our deduction. Positive relative density of a coprime prime progression is the standard prime-number theorem for progressions; it is not merely inferred from infinitude of the progression. No effective bound for its first pattern is claimed.

3. Barinder S. Banwait, *Explicit isogenies of prime degree over quadratic fields*, arXiv:2101.02673v3.
   https://arxiv.org/pdf/2101.02673v3
   Read: Theorem 1.2, explicitly attributed there to Mazur's original Theorem 1. Page image checked. ONLY the unconditional rational prime-isogeny theorem is used, not the GRH-dependent quadratic-field algorithms in this paper.

## Standard local input checked

4. J. S. Milne, *Elliptic Curves*, second edition, author PDF.
   https://www.jmilne.org/math/Books/EC2.pdf
   Read relevant local-field/Tate-curve discussion around printed pp. 102-103 (PDF pp. 106-107): split multiplicative Tate uniformization and the discriminant valuation. Prime-to-residue good-reduction torsion and the Weil-pairing determinant are standard background used explicitly in the proof. The particular order-four descent action is computed in PROOF.md; it is not attributed as a printed C1 theorem to Milne.

## Cross-check and original-source limitation

5. Philippe Michaud-Jacobs, *Mazur's isogeny theorem*, arXiv:2209.03153v2, Theorem 1.
   https://arxiv.org/pdf/2209.03153v2
   Cross-checked the rational prime-isogeny list.

6. Barry Mazur, *Rational isogenies of prime degree*, Inventiones Mathematicae 44 (1978), 129-162.
   https://doi.org/10.1007/BF01390348
   Original publisher metadata checked. Original theorem PDF was not retrieved through the available public access. We do not claim to have read its original proof in this turn. The exact theorem statement used is available in item 3.

## Executed here

- Independent standard-library `verify.py`: exact sparse-polynomial identities, example primality by trial division, F5 point counts, congruence inclusions, prime-field elementary matrix groups for 3,5,7,11,13,17, model inertia/Frobenius matrices over F5, and odd-conductor arithmetic.
- One preliminary symbolic scaling-identity check with SymPy, independently recast in the standard-library checker.
- No number field, unit group, class group, Selmer group, Galois image, or Sha order computed.
- No theorem-status edit, manuscript, shared ledger, memory mutation, or agent launch.
- The finite examples do not prove the all-odd-prime theorem. Its proof requires the local and group arguments and Mazur's theorem.
