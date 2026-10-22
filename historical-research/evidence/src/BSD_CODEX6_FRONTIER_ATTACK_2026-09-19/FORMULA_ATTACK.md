# FORMULA: minimum-strength attack

Write q=L''(E,1)/(2 Omega Reg). The target is q=4 #Sha, with FIN presupposed. Whenever this file uses the target q=36, it explicitly assumes **FIN and #Sha=9**. FIN alone does not supply the order.

## A numerical node is now closed

The bounded reconnaissance located the older Lane 3 interval regulator implementation. An independent directed-rounding implementation, with an exact rational tail bound, now proves

    q in [35.99427,36.00573].

See REGULATOR_CERTIFICATE.md. Therefore the following implication has no outstanding numerical premise:

    q rational AND den(q)<=174 -> q=36.

The antecedent remains unproved. A larger proved denominator bound could be accommodated by more certified analytic precision, but no such bound was obtained here, so more L'' computation is not useful now.

## Corrected node classification

| Node | Classification | Exact scope |
|---|---|---|
| Rank equality at two | PROVED_COMPUTER_ASSISTED | Retained rank theorem and Arb L'' nonvanishing |
| Exact Tamagawa/torsion factors | PROVED | 16 and 2; target multiplier is 4 |
| Omega enclosure | PROVED_COMPUTER_ASSISTED | Retained Arb; independent AGM here agrees |
| Reg and Omega*Reg enclosure | PROVED_COMPUTER_ASSISTED | New standalone certificate |
| D<=174 reconstruction implication | PROVED | Elementary integer-spacing proof; its premises are now numerically certified |
| q in Q | NEW_LEMMA_REQUIRED | No proof located or derived |
| Explicit usable denominator bound | NEW_LEMMA_REQUIRED | Separate arithmetic information, even after rationality |
| q=36 conditional on those arithmetic inputs | CONDITIONAL | Proven implication |
| FIN implies #Sha=9 | ROUTE_BLOCKED | Invalid inference; FIN allows extra square factors |
| Arithmetic determinant lattice under FIN | PROVED under that hypothesis | Contains no automatic identification with L'' |
| BKS Lemma U | PROVED under its recorded hypotheses | Existing local lattice theorem; not an exact unit comparison |
| GPR_an / exact p-adic scalar comparison in rank two | MAJOR_NEW_THEORY_REQUIRED | Grade of this proposed route, not a necessity theorem |
| Alternate bounded algebraicity route | UNKNOWN | Algebraic Lemma E gives a proved sufficient criterion; its antecedent is open |
| General FORMULA | UNKNOWN | No executable proof route established |

## 1. Does an existing determinant theorem give rationality after FIN?

The rational line and its integral arithmetic lattice become available, with the recorded local hypotheses. Choose a rational basis b and a real comparison sending b to Omega Reg. The real zeta vector is q b. Saying it belongs to the rational line is exactly saying q is rational. The lattice's existence supplies no such membership.

This is not just a missing normalization: replacing q by any positive real number changes none of the algebraic lattice statements. It is an abstract independence test of the proposed inference, not a claim that E's actual L-value is freely variable. The FIN-assumed audit already had this distinction; the master handoff should cite it.

## 2. One p-adic realization and weaker algebraicity

An exact identity iota(q)=m_p with m_p in Q would suffice by injectivity, and m_p algebraic over Q would at least prove algebraicity of q. But m_p in Q_p is not that statement: Q_p contains numbers transcendental over Q. Lemma U supplies a Z_p-unit ambiguity, not rationality.

If an identity has the same p-adic right-hand side for **every Q-embedding of C into C_p**, then q is fixed by every automorphism of C and is rational. This is a valid conditional field-theoretic argument, not a consequence of a theorem formulated for one fixed embedding. If embeddings are required to agree on Q-bar, the corresponding fixed-field argument gives only algebraicity, not rationality. The permitted embeddings and independence of the right-hand side must be proved, not suppressed.

No one-prime algebraicity theorem for the required rank-two scalar was found in the retained BKS statements. The p=5 digit u5=1 mod 5 remains consistency evidence. Its exact identification with the BKS height normalization was not needed and was not assumed.

## 3. Differentiate or regularize critical-value algebraicity

Attempt: use algebraicity of the normalized central value and differentiate at its double zero. Algebraic Lemma G disproves this inference using c(s-1)^2 for arbitrary c. A value theorem at a discrete critical integer is not an identity of algebraic families in the complex variable s. Dividing by (s-1)^2 and taking a limit simply reintroduces the unknown leading coefficient.

Deligne/Beilinson-style rational structures are legitimate candidate languages. For this central double zero, identifying the leading term with the real regulator is the unproved comparison. Separating integrality from rationality is useful, but does not make that comparison an already-proved theorem.

## 4. Auxiliary Rankin–Selberg family and first derivatives

For a holomorphic auxiliary L-factor M, the product's first derivative at 1 is zero, while its second derivative contains L''(E,1)M(1). Two simple-zero factors over a quadratic field are a different situation from this primitive double zero.

A varying-family argument was also tested. If F(s,t) has a first-derivative formula in s for varying t, differentiating it gives F_st, whereas the requested value is F_ss at the fixed curve. A comparison between these derivatives, plus a differentiable arithmetic realization of the height side, is required. A p-adic interpolation supplies a p-adic derivative and does not by itself identify this real derivative. Thus the naive twice-specialized Gross–Zagier route fails at a specific operation; a genuinely new two-variable comparison is not ruled out.

## 5. Second Kronecker-limit / Eisenstein derivatives

Introducing a pole can lower the formal derivative order, but the relevant regularized cuspidal projection and its identification with the Neron–Tate determinant must then be proved. Existing Eisenstein/unit formulas do not supply that map merely by being differentiated again. The retained F4 dossier contains no theorem instantiating these operations for this curve. This bounded audit found no missing ready-made source formula, and makes no global nonexistence claim.

## 6. ETNC rationality separated from integrality

Yes, these can be separated. In the rational determinant line, the assertion that the real zeta vector is rational is the rational part. Local integral-generation conditions are additional. In the present fixed basis, the first assertion is RAT itself. Even RAT plus integrality away from a finite set is not a usable denominator bound without exponent bounds at that set; powers of a fixed prime give arbitrarily fine rational approximations.

An ideal can control denominators if its relation to the **analytic** vector is proved. An arithmetic ideal alone cannot identify that vector. Conversely, a full ETNC theorem is stronger than this session needs; we do not declare all of ETNC necessary.

## 7. Real, p-adic and determinant regulator comparison

The canonical MW pairing defines Reg_infinity; local p-adic pairings define Reg_p; BKS compares appropriate p-adic objects through a Bockstein map. The missing step is a comparison that actually contains the complex leading term. Normalizing a determinant basis does not provide it.

Given iota(q)=m_p, an exact identity m_p=4 #Sha would indeed solve FORMULA at one prime. In that setting it is equivalent to FORMULA and must not be introduced as an independent “small lemma.” Equality of generated Z_p-lattices gives only equality up to a unit. The source reading of BKS Theorem 7.8 confirms precisely this local limitation.

## 8. A p-adic value plus a height/denominator bound

An a priori denominator bound for a **known rational number** enables rational reconstruction. It does not prove that a real number is rational or that it maps to the computed p-adic scalar. Algebraic Lemma F gives explicit distinct rationals compatible with arbitrarily small real error and any finite number of p-adic digits if the denominator is unbounded.

A weaker alternative worth retaining is bounded algebraicity: if q has a primitive minimal polynomial whose other conjugate distances give B<1/epsilon, Lemma E forces q=36 without first establishing rationality. No theorem proving that algebraicity and bound was obtained. Calling every such option “full GPR” would overstate what is logically necessary.

## Exact first unproved arrow

For the minimum route:

    current curve/theorem data -> q rational with usable denominator control.

RAT is its first unproved component. The numerical enclosure is complete. For the BKS candidate route, the first open comparison is the actual archimedean-to-p-adic identity, with its embedding and normalization specified; it is not the only possible formulation.

Under FIN without the additional order-nine hypothesis, q=36 still does not prove FORMULA. One must also exclude the remaining Sha factors, or use a common theorem that bounds them. This requirement stays inside FIN/FORMULA and is not a fourth top-level obligation.
