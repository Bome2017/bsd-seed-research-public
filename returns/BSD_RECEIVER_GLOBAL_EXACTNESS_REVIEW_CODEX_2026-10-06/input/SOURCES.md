# Sources and scope

## Private repository sources inspected through the GitHub connector

Repository: Bome2017/bsd-seed-lab.
Pinned commit: 6c1cb9398ce6d4791fc7988ee18893cd74bc1cdf.

1. work/returns/BSD_ARISTOTLE_UPPER_CONTROL_REVIEW_2026-10-06/REPORT.md
   Git blob SHA-1: 5bf8fe09d4dc32b785943b3c47fd551eb85f882d.
   Inspected accepted statement, delta, corrections, checks, and scope.
2. work/returns/BSD_ARISTOTLE_UPPER_CONTROL_REVIEW_2026-10-06/CORRECTED_PROOF.md
   Git blob SHA-1: efe25155f20704aec4941122fde816832817f6c3.
   Section 1 retains the P_2 local generator. Section 3 supplies global descent.
   Sections 4-5 isolate the sole possible defect at p=4547. Section 6 contains
   the same reciprocity operation used at other coefficient primes. Section 7
   leaves a global defect at 4547; PROOF.md here removes it.
3. work/returns/BSD_ARISTOTLE_UPPER_CONTROL_REVIEW_2026-10-06/CORRECTIONS.md
   Git blob SHA-1: 53af99cd33f580ce2ccc7c4c684b7977b851bcb5.
   C1 supplies the properly scoped global/local distinction. All its other
   corrections remain in force.
4. work/returns/BSD_ARISTOTLE_BFR_REVIEW_2026-10-06/MATHEMATICAL_RECONSTRUCTION.md
   Git blob SHA-1: 38d98caa6eef3c93556bad10faf2bfd19d87e9f9.
   Section A proves that P_2 generates E(Q_4547)/4547. Sections B-C are prior
   forward receiver inputs; section D distinguishes multiplicity from total
   class-group size and states the retained parity use.

These are source identifiers returned by the connector, not hashes of copies
bundled in this addendum. The full remote source files are not redistributed.
The uploaded BFR review archive was also inspected locally. Its SHA-256 is in
SOURCE_BINDINGS.json. The full third return was not downloaded or replayed.

## Published primary inputs inspected

- B. Poonen and E. Rains, Random maximal isotropic subspaces and Selmer groups,
  arXiv:1009.0287, https://arxiv.org/pdf/1009.0287.
  Section 4.1, odd-degree case; Proposition 4.10 and proof, PDF pp. 17-18;
  Theorem 4.13 and its Brauer reciprocity proof, PDF p. 19.
  Apply the statements to E with its principal polarization and the self-dual
  isogeny [p]. No distributional conjecture or heuristic from this paper is used.

- R. Pannekoek, On p-torsion of p-adic elliptic curves with additive reduction,
  arXiv:1211.5833, https://arxiv.org/pdf/1211.5833.
  Theorem 1, PDF p. 1, and the reduction-filtration discussion on p. 2.
  The translated seed has all a_i in p Z_p and p=4547 is outside the four
  small-prime exceptional cases. The component number 2 remains a seed import.

- H. Darmon, F. Diamond, R. Taylor, Fermat's Last Theorem,
  https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf.
  Theorems 2.17-2.19, printed pp. 60-62, give finite-module local and global
  duality. Used as a check on the existing comparison. The new short proof
  needs only local self-annihilation and global reciprocity, not the full
  Selmer-cardinality formula or an application of a modularity theorem.

- N. Dainobu, Ideal class groups of division fields of elliptic curves and
  everywhere unramified rational points, arXiv:2304.05035, https://arxiv.org/pdf/2304.05035.
  Proposition 2.8 and preceding Remark 2.5, PDF p. 8, checked for the retained
  away-from-p finite/unramified convention. This paper does not provide the
  new 4547 global deduction or a seed upper bound.

Relevant formula pages were visually inspected in addition to their parsed
text. Published inputs are used at their stated hypotheses. Source checking
here is targeted, not an exhaustive verification of the project's imports.
