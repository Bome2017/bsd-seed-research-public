# Primary-source register and reproduction

Primary sources inspected for this Stage-I reconstruction:

1. Shuai Zhai, Non-vanishing Theorems for Quadratic Twists of Elliptic Curves, arXiv:1409.0231, inspected PDF v2. Definition on printed p. 2; Theorem 1.7 and adjoining discussion on printed p. 5.
2. John E. Cremona, Algorithms for Modular Elliptic Curves, 2nd edition: Chapter 2 section 2.8 (printed p. 30, real-period definition); Table 4 (printed pp. 313-314, exact base ratio, row 66B(E)); Chapter 3 section 3.2 (printed p. 67, multiplicative and I0* steps of Tate's algorithm). Author-hosted full text.
3. John Cremona's Elliptic Curve Data documentation, optimality and Manin constant section, and coefficient data for 66b1.
4. Cai-Li-Zhai, On the 2-part of the Birch and Swinnerton-Dyer conjecture for quadratic twists of elliptic curves, arXiv:1712.01271: explicit full-real-period definition, Theorem 1.1, Remark 1.3 and Theorem 1.5.
5. Banwait-Huang, On the identification of elliptic curves that admit infinitely many twists satisfying the Birch-Swinnerton-Dyer conjecture, arXiv:2601.16044v3 (4 June 2026): Definitions 2.1-2.7, Theorems 2.13 and 2.14, normalization discussion after 2.14, and Remark 2.11 on unpublished inputs.
6. Burungale-Skinner-Tian-Wan, arXiv:2409.01350, inspected 103-page PDF: Theorem 1.7 on printed p. 4, period discussion including Remark 2.3, Theorem 10.12 on printed p. 89, and Example 1 on printed p. 90. The literal a3=0 requirement and the broader introductory statement are recorded separately, without a silent correction.
7. Jungbae Nam, Critical L-values of Primitive Forms Twisted by Dirichlet Characters, Concordia PhD thesis, 2018; repository filename Nam_PhD_S2019.pdf. Theorem 4.9, printed p. 81.
8. Shu-Zhai, arXiv:2102.11808: condition (Tor) and Theorems 1.2 and 1.4.
9. Kriz-Li, arXiv:1710.00294: Theorem 1.4 (no rational cyclic 4-isogeny hypothesis).

No packet point-count script/output or 62a1 mechanism capsule was used to derive the mathematics or independent numerical results.

## Reproduction

The program verify_stage1.py requires Python 3 and sympy. Run:

    python verify_stage1.py

It overwrites independent_checks.json in the same directory. It verifies coordinate identities, isogeny identities including both coordinates of composition, invariants and the halving quartic, and then counts points for all odd good primes below 10000 without importing packet computations. It compares the independently counted values against the derived character criterion. It is not a formal proof of uniform local solubility; that proof is supplied in the reconstruction.

The original packet is not modified or repackaged in this archive. Its SHA-256 is recorded in CHECKSUMS.sha256 along with the frozen files. A changed frozen record must be a separately identified version, not an unrecorded overwrite.
