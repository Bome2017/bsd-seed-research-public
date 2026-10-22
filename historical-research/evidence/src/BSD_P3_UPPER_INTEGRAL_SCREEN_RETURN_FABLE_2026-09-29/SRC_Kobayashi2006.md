# SRC — S. Kobayashi, "An elementary proof of the Mazur–Tate–Teitelbaum conjecture for elliptic
# curves", Doc. Math. Extra Vol. Coates (2006) 567–575. Copy read: arXiv:math/0610164v1 (only version;
# sources/Kobayashi2006_math0610164.pdf, sha256 dc66dd36…; "Kob l.N" = the .txt). Grade of copy: PREPRINT
# text of a published paper (journal PDF not fetched: Bielefeld URL 404). Read: ALL (9 pp.).
## What it proves (quoted)
- §3 standing hypothesis (Kob l.199-201): "In this section we assume that E is the Tate curve
  E_q : y² + xy = x³ + a4(q)x + a6(q) where q = q_E ∈ Q_p^× satisfying |q|_p < 1".
- Col : lim H¹(k_n, T*(1)) → Λ = Z_p[[Γ]] (l.250-255), built from d_n ∈ Ĝ_m(m_n) via φ̂ : Ĝ_m ≅ Ê
  over Z_p (l.227-235). This is INTEGRAL (target Λ).
- l.301-325: with z^Kato (Kato Thm 12.5 cited for the interpolation, Ω⁺_E), Col(z^Kato)(X) = L_{p,γ}(E,X).
- Thm 4.1 (l.433-438): derivative of Col(z) at X = 0. Cor 4.2 (l.439-457): "if E/Q has split
  multiplicative reduction at p" then L'_{p,γ}(E,0) = (1/log_p κ(γ))·(log_p q_E/ord_p q_E)·L(E,1)/Ω⁺_E.
## What it does NOT contain
- No Selmer group, no characteristic ideal, no divisibility or inclusion of ideals anywhere (read in
  full). The paper's theorem is the MTT derivative formula (Greenberg–Stevens), not a main-conjecture
  statement. Its only Λ-level output is the identity Col(z^Kato) = L_{p,γ} for the Tate curve.
## K-R24a (applicability to the seed, p = 3, nonsplit)
- p = 3 allowed: no restriction stated (p odd is implicit in Kato's element; nothing excludes 3).
- **FIRST FAILING: nonsplit multiplicative.** §3 assumes E is the Tate curve over Q_p (split). The
  construction uses φ̂ : Ĝ_m ≅ Ê over Z_p (l.227), which fails over Z_p for the nonsplit twist
  (Ê ≅ Ĝ_m only over Z_{p²}, twisted by the unramified quadratic character). Cor 4.2 says "split".
- Integral: the Coleman map is integral, but no inclusion is stated, so "integral T-INT" does not arise.
- p-adic L attached: yes (via Col). Image / level hypotheses: none stated (the interpolation input
  is imported from Kato 12.5 as a citation).
## K-R24b (proof support): N/A — the paper states no divisibility, so it cannot support SW 7.3's
  divisibility in ANY reduction type; SW cite it for the "exceptional case" (SW l.1197-1199), i.e. for
  the trivial zero (T | d(T)), which is the split case only.
## Grade: THEOREM (read at source) for the Tate-curve Coleman identity and Cor 4.2; IRRELEVANT to
  T-INT at nonsplit p. Consequence for item 1: SW 7.3's cited support for the multiplicative case
  covers only the split trivial zero, and only its analytic side.
## Useful by-product (UNCHECKED as a written deduction; no source): the method's analogue for the
  nonsplit twist would use the height-one formal group Ê over Z_p with T_pÊ = Z_p(1)⊗η (η unramified
  quadratic). Since η is nontrivial on G_{Q_p(μ_p∞)}, no trivial zero occurs. Not printed here.
