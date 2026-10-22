# Sources and scope

1. Álvaro Lozano-Robledo, [The day I almost made $1M with math](https://www.youtube.com/watch?v=i1hiPIQbt0M), September 3, 2026. User-supplied primary account. Title/author/date read from YouTube; full auto-generated English transcript read through the browser transcript export. Relevant diagnosis: 1:53–2:31. Transcript is hashed in INPUT_BINDINGS.json but is not republished in this package. The speaker's computation has not been independently reproduced.
2. Magma Handbook, [Mordell–Weil Groups and Descent Methods](https://docs.magma-maths.org/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), especially Rank/RankBounds and return-status documentation. Read October 4, 2026. Rank returns a lower bound and an exactness flag; the displayed contract supports the reported diagnosis.
3. Magma Handbook, [Curves over the Rationals](https://docs.magma-maths.org/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/intro-2.html), AnalyticRank and ConjecturalRegulator. Read October 4, 2026. The former is heuristic; the latter assumes BSD. Neither is a standalone counterexample certificate.
4. Andrew Wiles, [The Birch and Swinnerton-Dyer Conjecture](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf), official Clay statement. Distinguishes rank equality from its refined leading-term formula. No prize-eligibility conclusion is made here.
5. Project research release at commit `8414aea58180f3a18bcee7fba23475c8cac90996`: claims A.1, R.1–R.7 and O.1–O.3; underlying PARI/eclib descent outputs, analytic certificate, and regulator certificate identified in INPUT_BINDINGS.json. Existing evidence grades are retained; this pass does not upgrade them.

All new computation in this packet is exact interval arithmetic with Python fractions. It checks the elementary implication from retained bounds, not the production of those bounds. Hashes identify files; they do not certify their mathematics.

