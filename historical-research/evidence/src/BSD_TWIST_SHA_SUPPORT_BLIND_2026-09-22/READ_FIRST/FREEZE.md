# CANONICAL FREEZE — ordinary lane, after the two ordinary-bridge audits

Date 2026-09-22. This supersedes the ordinary-bridge packet as the active statement of where the branch stands.
That packet becomes history. Hostile reconciliation, not a summary: §3 records what both runs got wrong.

---

## 1. What is now established

**Certified computation** (`~/BSD_TWIST_D7_CERTIFICATE_2026-09-22/`):

    L(E^{-7}, 1) in [9.054319, 9.054421]     zero excluded, margin 1.79e5
    => analytic rank of E^{-7} is 0
    => (Gross-Zagier-Kolyvagin)  rank E^{-7}(Q) = 0  and  Sha(E^{-7}/Q) FINITE
    => (r^+, r^-) = (2, 0),  rank E(K) = 2,   K = Q(sqrt -7)

**Proved by two independent audits**, both source-reading BLV and Bertolini–Darmon, both returning
`LEADING_TERM_STEP_FAILS`:

    MODULE_IDENTIFICATION    BLV Char_p = char ideal of the BD X_inf; Selmer groups literally equal
    BD_ORDER_INEQUALITY      sigma >= rank S + rank S^(2) >= 2 max(s^+, s^-)
    TWIST_MINUS_EIGENSPACE   S^- = S_p(E^{-7}/Q), for Selmer and T_p Sha, not merely for E(K)
    A2a_DIVISIBLE_SHA        Div Sha(E/K)[p^inf] = 0, conditional on [c_2] != 0

Both independently noticed that **BD Lemma 3.1 sits in a chapter that assumes `Sha` finite**, and both re-derived it
without that assumption. Since finiteness was simultaneously the forbidden hypothesis and the target, a run that had
missed this would have returned a circular proof. That is the strongest evidence the A2a result is sound.

**Verified here, independently of both runs.** The Task-6 core does not even need the `2 max` formula:

    s^- = 0  =>  S = S^+  =>  the first anticyclotomic height vanishes identically on S (it already vanishes
    on S^+ x S^+)  =>  S^(2) = S  =>  sigma >= rank S + rank S^(2) = 2 rank S  =>  rank S <= 2.
    And rank S = rank E(K) + d = 2 + d.  Hence d = 0.

**Consequence worth separating out, because it needs no leading-term step at all:** `d = 0` includes `d^+ = 0`, so

    conditional on [c_2] != 0 only:   Sha(E/Q)[p^inf] is FINITE
    at EVERY admissible good-ordinary p, including the exceptional ones of §3.

## 2. What fails, and why it is not a gap

Task 7 fails. The needed statement is `v_p(R_der) >= 0`. BD Thm 2.23 places the leading term in
`(I^4/I^5 ⊗ Q)/Z_p^x`; Thm 2.18(5) allows denominators `p^{A_k}` from the saturation defect; Cor 2.24(2) makes only
the **product** `#(Sha/Div Sha) · R_der` integral — exactly the quantity being split. Remark 2.21 asserts placement
in `I^rho/I^{rho+1}` without proving integrality.

**`A_2 = 0` is SUFFICIENT, not equivalent.** Both runs wrote "equivalently". A positive saturation defect does not
force the determinant regulator to have negative valuation; cancellation or extra divisibility can occur. This is a
**shared error across two agreeing runs** — recorded because agreement is otherwise the evidence being relied on.

**Universal `Sha(E/K)[p^inf] = 0` is FALSE, not unproved**, at any `p | #Sha(E^{-7}/Q)`, since
`Sha(E/K)[p^inf]^- = Sha(E^{-7}/Q)[p^inf]`. Run B states this itself. So `A_2 = 0` universally is provably the wrong
target and must not be pursued.

Both runs bound the defect, differently:

    run A :  A_2 <= v_p( #Sha(E^{-7}/Q) * #E^{-7}(Q)_tors )
    run B :  A_2 <= c,  where p^c is the EXPONENT of Sha(E^{-7}/Q)[p^inf]

**Computed here: `#E^{-7}(Q)_tors = 2` exactly** — the twist's quadratic factor has discriminant
`4497724161 = 49 * 91790289`, not a square, and point counts give the order dividing 2. By Mazur the only primes
that could ever appear in torsion are `2, 3, 5`; BLV needs `p >= 5`; here none do. So run A's extra factor is
**vacuous** and both bounds have the same support, `{ p : p | #Sha(E^{-7}/Q) }`.

## 3. The hostile finding: BOTH runs aimed at a statement stronger than the project needs

This was not flagged by either run, and it changes the frontier.

`FIN` is about **`Sha(E/Q)`**. For odd `p` the idempotents `(1 ± tau)/2` give

    Sha(E/K)[p^inf]  =  Sha(E/Q)[p^inf]  (+)  Sha(E^{-7}/Q)[p^inf]
                        ^^^^^^^^^^^^^^^      ^^^^^^^^^^^^^^^^^^^^^^
                        the PLUS part        the MINUS part
                        what FIN needs       irrelevant to FIN

At `p | #Sha(E^{-7}/Q)` the **minus** part is nonzero, so `Sha(E/K)[p^inf] != 0`. **But `Sha(E/Q)[p^inf]` may still
be zero.** The failure at the exceptional primes lies entirely in the eigenspace `FIN` does not care about.

The runs proved things about the *whole* `Sha(E/K)` because BD Thm 2.23's leading term is the full order. So the
exceptional set `{p | #Sha(E^{-7}/Q)}` may be an **artifact of aiming at the `K`-statement** rather than a real
obstruction to `FIN`.

This opens a second, independent route, which is **not** known to work — under the anticyclotomic `Lambda`, `tau`
acts as the involution `iota` rather than commuting, so `Char_p` does **not** obviously split into eigenparts, and
no eigenspace-refined analogue of Thm 2.23 is in hand. It is an open question, not a repair.

## 4. Frozen ledger

    CERTIFIED  : L(E^{-7},1) != 0 ; rank E^{-7}(Q) = 0 ; Sha(E^{-7}/Q) finite ; #E^{-7}(Q)_tors = 2
    PROVED (conditional on [c_2] != 0, admissible good-ordinary p):
       Div Sha(E/K)[p^inf] = 0        i.e.  Sha(E/Q)[p^inf] FINITE at every such p
    PROVED (conditional on [c_2] != 0, and p not dividing #Sha(E^{-7}/Q)):
       Sha(E/K)[p^inf] = 0            hence Sha(E/Q)[p^inf] = 0
    FALSE      : Sha(E/K)[p^inf] = 0 at p | #Sha(E^{-7}/Q)   -- a fact, not a gap
    NEEDED     : v_p(R_der) >= 0 ;  A_2 = 0 sufficient, NOT equivalent
    OPEN, new  : (a) the p-support of #Sha(E^{-7}/Q)  -- finite, fixed-curve
    OPEN, new  : (b) an eigenspace-refined leading term isolating the PLUS part, which would make (a) moot
    OPEN       : [c_2] != 0, unchanged
    UNTOUCHED  : A3 supersingular (proved infinite) ; B anomalous a_p = +-1 (conjecturally infinite)
    OPEN       : FIN, FORMULA

**"Cofinite" is narrower than it reads.** Admissible excludes supersingular `p` (proved infinite, Elkies) and
anomalous `p` (conjecturally infinite, Lang–Trotter, none below 30000 here). So this is **not** finite support, and
not even finite support restricted to ordinary primes.

## 5. Fixed-curve data for the next question

    E^{-7} :  y^2 = x^3 + 159145 x^2 + 5207351716 x         (quadratic twist of the seed by D = -7)
    conductor 49 N = 318656212624190616 = 2^3 * 3 * 7^2 * 2243 * 4547^2 * 5843
    c4    = 155281214032 = 2^4 * 7^2 * 43 * 1013 * 4547
    c6    = -19291412299579840
    Delta = 1951401451332224483990307737856 = 2^8 * 3^2 * 7^6 * 2243 * 4547^3 * 5843^2
    j(E^{-7}) = j(E) = 1322372123614064 / 689197281363   (twists share j; NOT integral)
      v_q(j) < 0 exactly at q = 3, 2243, 5843  -> potentially multiplicative there
      j a unit at 2, 7, 4547                   -> potentially good there
    minimality: v(Delta) < 12 at every bad prime, so this model is minimal at all of them
    per-prime (v(c4), v(Delta), v(j)):
      2    (4, 8,  4)      3    (0, 2, -2)     7    (2, 6,  0)
      2243 (0, 1, -1)      4547 (1, 3,  0)     5843 (0, 2, -2)
    E^{-7}(Q)_tors = Z/2 exactly
    E^{-7}(R) has 2 components (cubic has 3 real roots: 0 > -46039.963 > -113105.04)
    2*pi / AGM(sqrt(e1-e3), sqrt(e1-e2)) = [WITHHELD until Stage I is frozen - see STAGE_II_ONLY/]   (period of dx/y; NOT the Neron period)
    L(E^{-7},1) in [9.054319, 9.054421]   CERTIFIED

**Deliberately not computed here: `prod_v c_v`.** It needs Tate's algorithm at `2, 3, 7, 2243, 4547, 5843`, and there
is **no PARI and no Sage on this host** (checked). So no `#Sha` is predicted in this freeze — by necessity, and also
by choice, so that the next audit is not anchored on a guess.
