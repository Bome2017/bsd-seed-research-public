# Primary-source ledger

All sources below were inspected via the web in this reconstruction. Page numbers
are printed page numbers unless stated otherwise. No packet literature extraction
was treated as final authority on period conventions.

* Shuai Zhai, Non-vanishing theorems for quadratic twists of elliptic curves,
  arXiv:1409.0231, p.2: Lalg uses the least positive real period of the minimal
  Neron differential. P.5, Theorem 1.7: positive-discriminant analytic input.
* Robert L. Miller, Proving the Birch and Swinnerton-Dyer conjecture for specific
  elliptic curves of analytic rank zero and one, arXiv:1010.2431v3, p.1:
  Omega is the integral over ALL real points. P.16, Theorem 7.1: base BSD(2)
  for conductor less than 5000. This is not a uniform theorem for all 66b1 twists.
* Cai--Li--Zhai, arXiv:1712.01271v2, pp.1-2: real Tamagawa/period convention,
  with Omega=Omega+ or 2 Omega+. Theorems 1.1/1.5 require a different
  base valuation and a prime point-count condition of valuation one.
* Banwait--Huang, arXiv:2601.16044v3, p.3 Definition 2.1 and Definition 2.7;
  p.7 Theorem 2.14; p.8 proof remark (2): explicitly follows the CLZ period
  convention and subtracts the valuation of the number of real components.
  P.6 Theorem 2.13 is a separate conditional strong-BSD transfer criterion;
  p.13 section 2.7 addresses the conductor-150 list, including 66b1.
  The older v1, p.5 section 2.4, also explicitly records base full-period
  valuation -2 for 66b1. Current applicability tests use v3, not v1.
* Burungale--Skinner--Tian--Wan, arXiv:2409.01350v2, p.2 Conjecture 1.1
  calls Omega a Neron period but does not explicitly give the real-component
  integral. P.89 Theorem 10.12 has a_3(E)=0 and assumes BSD(2) of the twist.
  The p.4 Theorem 1.7/p.90 Example 1 printed inclusion of 66b1 is not a
  source-complete proof of the missing 2-primary input through the cited chain.
  Exact component-factor convention: NOT CERTIFIED in this reconstruction.
* Christopher Skinner, arXiv:1407.1093, p.25 section 3.3, defines the Neron
  period by integrating over a generator of H_1(E(C),Z)^+. This is primitive
  real-period normalization. The cited results are at odd primes; they cannot
  distinguish a factor of two.
* H. Nam, Concordia doctoral thesis (repository file Nam_PhD_S2019.pdf;
  repository record 984957), p.81 Theorem 4.9: condition (a) requires 2 split
  or good reduction at 2. This fails on the proposed 66b1 family. The displayed
  conclusion is algebraic rank zero, not full BSD or Sha[2] vanishing.
  P.89 Table 5 includes numerical 66b1 data; that table is not a replacement
  for the theorem's hypotheses. PDF-page screenshots of the theorem failed,
  but its parsed primary text was available; the table image was inspected.
* Shu--Zhai, arXiv:2102.11808, p.2 condition (Tor), requires order-two rational
  2-torsion on both the curve and its quotient, which fails for this quotient.
* Barrios--Mok, arXiv:2510.00926, p.5 Theorem 1.4/Corollary 1.5: BSD modulo
  rational squares, not an exact 2-adic valuation formula.
* Barrios--Roy--Sahajpal--Tallana--Tobin--Wiersema, arXiv:2501.03209v2,
  p.14 Table 4: ramified good reduction becomes I_0^*, c=1+#roots; unramified
  multiplicative twists remain I_n. The Table 4 image was inspected.
  P.18 Table 5 parsed text gives the 2-adic I_n twist rule; attempts to render
  that page failed. The c_2=2 assertion is also derived independently through
  unramified twisting of the split I_4 geometric component group.
* LMFDB conductor-66 listing, EllipticCurve/Q/66/: matches 66b1=66.b4,
  coefficients, discriminant, rank, torsion, semistability, Manin constant,
  and the isogenous center's full rational 2-torsion. Curve-detail/API URLs
  did not load. Optimality is used as explicitly established input from the
  target packet, not claimed as a newly proved modular-parametrization result.

## Boundary of the search

NOT_FOUND means no source-complete prior uniform BSD(2) theorem for the exact
specified prime family was established from the primary sources above. It is
not a novelty claim or a proof that no such theorem exists elsewhere.
