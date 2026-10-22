# First-review coverage by claim

All 76 claim statements and their manuscript treatment were reviewed for consistency and scope. The table below gives the stronger work, where any, and explicitly limits it. A statement review is not a complete proof audit. See `FIRST_REVIEW.md` for the executable checks.

| Claim | Review performed and boundary |
|---|---|
| A.1 — Arithmetic data of the curve | Exact curve/invariant/point-count replay; detailed Tate classifications retained rather than independently rederived in this review. |
| A.2 — E has no complex multiplication | Nonintegral j recomputed exactly; standard rational-CM implication read. |
| A.3 — Residual images are full at every odd prime | Statement and retained image-theorem attribution checked; all residual-image proofs not replayed. |
| A.4 — Manin constant and the symbol lattice | Proof-scope review; restricted to rational unitary cusps; missing-lattice versus rounding distinction corrected. Published Manin imports remain at recorded reading grades. |
| R.1 — The Mordell-Weil group | Primary preprint scope checked. Recovered and replayed global Sage/eclib saturation index one and exact basis change. Separate enumeration proof restored, not rerun. |
| R.2 — L(E,1) = L'(E,1) = 0 | Logical dependence on rank and published rank-zero/one results checked; those source proofs not rederived. |
| R.3 — Certified second derivative: analytic rank exactly two | Statement and trust base reviewed; supplemental witness checks passed; original Arb enclosure not regenerated. |
| R.4 — RANK | Dependency consistency checked; rank/basis replay as R.1 and analytic certificate retained as R.3. |
| R.5 — Periods and regulator | Normalization checked in manuscript; full real interval computation not rerun. Floating Sage output is not a replacement for the retained rigorous bounds. |
| R.6 — The BSD quotient interval | Consistency of stated quotient interval reviewed; no fresh full analytic/regulator interval run. |
| R.7 — The exact endpoint of full BSD for E | Elementary endpoint equivalence checked with retained torsion/Tamagawa constants. |
| S.2 — The 2-primary component vanishes | Retained preprint input and statement checked; descent not independently rerun. |
| S.3 — The 3-primary component is (Z/3)^2 | Exact coefficient replay, restored independent formal-height replay for valuation two, and finiteness-first proof order checked. Skinner/Jones imports retained. |
| S.5 — The 5-primary component vanishes | Exact residue recomputed from retained symbol tables; downstream theorem hypotheses and interval certificate remain at imported grades. |
| S.7 — The 7-primary component vanishes | Exact residue recomputed from retained symbol tables; downstream theorem hypotheses and interval certificate remain at imported grades. |
| S.11 — The 11-primary component vanishes | Exact residue recomputed from retained symbol tables; downstream theorem hypotheses and interval certificate remain at imported grades. |
| S.13 — The 13-primary component vanishes | Exact residue recomputed from retained symbol tables; downstream theorem hypotheses and interval certificate remain at imported grades. |
| S.P — The primary components at 2, 3, 5, 7, 11, 13 | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| S.FIN — What FIN would give: the square-order constraint and the 2601 threshold | Conditional finite-group threshold/square-order deduction checked; FIN not supplied. |
| S.U — A uniform torsion bound is equivalent to the Sha half of the endpoint | Corrected to equivalence with FIN plus conditional ORDER9, not conditional ORDER9 alone. |
| S.K — FIN decomposes by primes, at full depth | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| Q.1 — Bounded rationality forces q = 36 | Statement, normalization and endpoint implication reviewed; no arithmeticity or q=36 supplied. |
| Q.2 — Bounded algebraicity forces q = 36 | Statement, normalization and endpoint implication reviewed; no arithmeticity or q=36 supplied. |
| Q.3 — A common scalar would settle both endpoints | Statement, normalization and endpoint implication reviewed; no arithmeticity or q=36 supplied. |
| Q.4 — The weighted Mellin period | Statement, normalization and endpoint implication reviewed; no arithmeticity or q=36 supplied. |
| K.1 — The twist by -23 has analytic and algebraic rank one | Twist formula, sign and claimed consequence reviewed; large Arb certificate and coefficient stream not regenerated. |
| K.2 — The twist by -7 has analytic and algebraic rank zero | Twist formula, sign and claimed consequence reviewed; large Arb certificate and coefficient stream not regenerated. |
| B.1 — Cyclotomic depth-two criterion at good ordinary primes | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| B.2 — Criterion SS at good supersingular primes | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| B.3 — Anticyclotomic forward bridge at good ordinary primes (K = Q(sqrt(-7))) | Statement/module-dependency qualifications reviewed; no fresh BLV/BD source replay. |
| B.4 — Anticyclotomic forward bridge at good supersingular primes (A3) | Pinned Lean replay passed; finite mod-p order wording corrected; arithmetic black boxes and modeling steps remain imports. |
| B.5 — One forward architecture for every good prime p >= 5, p not dividing 7N | Scope checked; ordinary and supersingular forward implications do not evaluate M2 at any prime. |
| B.6 — The split multiplicative prime 2243: a sufficient certificate, not computed | D5 exact generator/verifier replay; local normalization checked; cubic coefficient uncomputed and F4 remains open. |
| B.7 — The nonsplit multiplicative prime 5843: a sufficient certificate, not computed | Retained nonsplit sufficient criterion checked for scope; no expensive certificate or fresh source proof replay. |
| B.8 — The additive prime 4547: only a semi-decision, and the route is blocked | Corrected overbroad impossibility wording; retained Kim sufficient witness remains, with no feasible evaluation supplied. |
| B.9 — Ordinary-tail equivalence O1 | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| B.10 — Division-field reduction | Statement and finite exceptional set scope checked; full descent theorem not rederived. |
| B.11 — LINE and witness content (conditional algebra) | Equivalence versus difficulty reduction distinguished; no new integral witness. |
| B.12 — Local structure of the Selmer groups at settled primes | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| B.13 — Heegner-Stark Fitting identities over Q(sqrt(-23)) | Preserved unproved ideal evaluation and twist-primary qualification; no 13-unit promotion. |
| B.14 — An effective constant from any fixed integral model (Lean) | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| B.15 — The ordinary stabilization correction is invisible in the witness quotient | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.1 — Integral sources do not bound prime support | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.2 — Localization determinants of the known points do not see the quotient | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.3 — The Destrempes-Malinin lifting mechanism is false | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.4 — Eisenstein congruences give selected subspaces only | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.5 — Finite logarithmic realizations of the Mellin period are excluded in the stated class | Preserved obstruction scope; no universal exclusion of all arithmetic realizations. |
| X.6 — Both single-vertex Eisenstein completions miss the Mellin period (certified residuals) | Interval and scope checked; raw residual enclosures not regenerated. |
| X.7 — Further midpoint analyses (trace, Mellin, Green kernel, secondary descent) | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.8 — Broad curvature orthogonality | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.9 — Visibility gives no horizontal gain | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.10 — Torus and vector extensions retain exactly the unknown Sha | Corrected split torus versus split extension; scoped written argument reviewed. |
| X.11 — Finite local data and first-derivative formulas do not reach the second derivative | Scoped first-derivative conclusion to tested routes; a bare factorization is not a universal impossibility theorem. |
| X.12 — A fixed rank-three ambient model is equivalent to finite lane support | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.13 — No unit-root stabilization at supersingular primes | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.14 — The prime-by-prime ladder was stopped at 13 | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| X.15 — No Manin/Hecke/Atkin-Lehner compression of the 2243 certificate | Finite rank computation and Atkin-Lehner checks replayed; no general computational lower bound inferred. |
| X.16 — The 2243 and 5843 certificates are unaffordable at the authorized budget | Resource/budget stop preserved; computation not launched or newly timed. |
| X.17 — Procedural and unsuccessful stops | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| O.1 — FIN | Open endpoint/frontier label retained. No proof or witness supplied. |
| O.2 — ORDER9 | Open endpoint/frontier label retained. No proof or witness supplied. |
| O.3 — Q36 | Open endpoint/frontier label retained. No proof or witness supplied. |
| O.4 — The prime-uniform integral witness (frontier question) | Open endpoint/frontier label retained. No proof or witness supplied. |
| H.1 — Run013: a qualified full-BSD twist family of 62a1 | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| H.2 — The 66b1 family | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| H.3 — H41 mod-4 successor | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| H.4 — Gate-R: Lean point-group bridge for E_{r,q} | Restored the retained Params/H41 hypotheses; no new family/BSD proof asserted. |
| H.5 — H9R16-C geometric milestone | Statement/scope and dependency metadata reviewed; detailed source proof and any underlying computation not independently replayed in this first review. |
| W.1 — WITHDRAWN: "C_1 != 0 is forced by the unit specialization at p = 13" | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.2 — WITHDRAWN: the arrow-orientation rule ("must map out of Selmer, not into it") | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.3 — SUPERSEDED: C13 = 7 or 8 | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.4 — CORRECTED: exact theta order, "A_2 = 0 equivalently", and "rho_p = 4 suffices" | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.5 — CORRECTED: "cbar_2 = -c_{p-3}" and "5843 obstructs the twist Sha support" | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.6 — SUPERSEDED: older 2243/5843 cost figures and the "compute only" framing | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.7 — WITHDRAWN: "v2.3 isolates crashed and restarted runs" | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
| W.8 — Earlier register | Withdrawal/supersession checked for consistency with the release; historical source preserved rather than overwritten. |
