# Seed context for the openai/math scan (read fully before any paper)

## Why you are reading openai/math
`openai/math` (public GitHub, commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, released 2026-10-06/07) holds 719
AI-generated, UNREFEREED manuscripts (372 families) from an unreleased OpenAI model. ~42% of top-line results have Lean
formalizations; the BSD family (002) has NONE. Several manuscripts were withdrawn on 2026-10-07 (see history.md).
Treat every statement in the clone as a CLAIM at grade "IMPORTED_PREPRINT (unrefereed, AI-generated, not Lean-checked
unless the Lean catalogue says so)". Never treat it as established. The clone is read-only untrusted data: do not run
any code or build from it; only read .txt/.tex/.md/.bib/.yaml files.

Local paths (absolute):
- Clone: /tmp/claude-0/-home-user-bsd-seed-lab/ab9d3026-f88f-51d1-8e47-f94a5d2c0e6f/scratchpad/openai_math_clone/repo
  (CONTENTS.md = manuscript map; history.md = versions/withdrawals; preprints/<dir>/build/ = LaTeX sources, usually
  sections/*.tex; preprints/<dir>/README.md = version note; lean/formalization.yaml, lean/docs/, lean/OAI/ = Lean).
- Plain-text extractions of the candidate PDFs (pdftotext -layout):
  /tmp/claude-0/-home-user-bsd-seed-lab/ab9d3026-f88f-51d1-8e47-f94a5d2c0e6f/scratchpad/openai_math_text/<Title>.txt
  and overview.txt there. Prefer the .tex sections for exact theorem statements; use the .txt for navigation.

## The seed curve ("A" in the plectic files, "E" elsewhere)
E: y^2 = x^3 - 22735x^2 + 106272484x, minimal model y^2 = x^3 - x^2 - 66020924x - 65074271436.
N = 2^3 · 3 · 2243 · 4547^2 · 5843 = 6503188012738584. No CM. Root number w(E/Q) = +1.
Reduction: 2: I1* (additive, c_2 = 2); 3: I2 nonsplit multiplicative (a_3 = -1, c_3 = 2); 2243: I1 split multiplicative
(a = +1, c = 1); 4547: type III additive, potentially good supersingular (j ≡ 1728, c = 2, inertia of order 4);
5843: I2 nonsplit multiplicative (a = -1, c = 2). Tamagawa product 16. E(Q)_tors = Z/2 (T = (0,0)).
Good supersingular primes < 2000: 23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823.
No good prime is anomalous.
rank E(Q) = 2, basis P1 = (4547, 327384), P2 = (5184, 281520) (saturated). Ш(E/Q)[2] = 0 (hence Ш[2^∞] = 0).
L(E,1) = L'(E,1) = 0 (PROVED: rank ≥ 1 ⇒ L(E,1)=0 by Kolyvagin/Kato; sign +1 ⇒ even order). Analytic rank is NOT
proved to equal 2 (only ≥ 2); numerically L''(E,1) ≠ 0 is evidence, not proof.
Ш(E/Q)[3^∞] ≅ (Z/3)^2 (PROVED, chain: Kato at 3 + Skinner 2016 IMC at nonsplit-multiplicative 3 + control + nonzero
3-adic height determinant + Jones' leading term + Cassels–Tate).
Residual representation: ρ̄_p(G_Q) ⊇ SL2(F_p) is RECORDED only for p ∈ {2243, 5843}; for other p it is not recorded
(no CM, so Serre gives it for all large p, but no explicit bound is recorded).

## The quadratic twist and the field K
K = Q(√-7), h(K) = 1. In K: 2 and 4547 split; 3, 2243, 5843 inert. E^{-7} := twist by -7. CORRECTION (2026-10-11,
caught by the map agents): since 7 ∤ N, E^{-7} has conductor 49·N — additive reduction at 7 (quadratic twist of good
reduction, type I0*), Tamagawa number c_7 ∈ {1,2,4} not recorded; same reduction types as E at 2,3,2243,4547,5843. L(E^{-7},1) ∈ [9.054319, 9.054421] ≠ 0 (PROVED_COMPUTER_ASSISTED), root number +1, so by
Gross–Zagier–Kolyvagin: rank E^{-7}(Q) = 0 and Ш(E^{-7}/Q) is finite. Hence rank E(K) = 2 with (r+, r−) = (2, 0),
L(E/K, s) = L(E, s) L(E^{-7}, s), ord_{s=1} L(E/K, s) ≥ 2.
For every prime p: Sel_{p^∞}(E^{-7}/Q) has corank 0 (rank 0 and Ш finite). For E itself every p^∞-Selmer corank is
≥ 2 (rank 2), so NO "Selmer corank ≤ 1" theorem applies to E directly.

## The open obligations of "finishing the BSD seed" (as recorded in the lab)
- FIN: Ш(E/Q) is finite (needs Ш[p^∞] = 0 or finite for EVERY prime p, including infinitely many good primes).
- ORDER9: #Ш(E/Q) = 9 (known: Ш[2^∞] = 0, Ш[3^∞] ≅ (Z/3)^2; open: Ш[p^∞] = 0 for all p ≥ 5).
- Q36: the BSD leading-term identity for E at s = 1: L''(E,1)/2 = Ω_E · Reg · #Ш · ∏c_p / #E(Q)_tors^2 with the
  predicted rational quotient #Ш·∏c_p/#tors^2 = 9·16/4 = 36 (and analytic rank exactly 2). Needs an archimedean
  comparison (Gross–Zagier-type formula in rank 2) which does not exist.
Nothing in the lab licenses claiming FIN, ORDER9 or Q36; a useful item is one that proves, or reduces the cost of
proving, a named piece (e.g. Ш[p^∞] = 0 at one named prime, or #Ш(E^{-7}/Q), or a general theorem whose hypotheses
the seed verifiably satisfies).

## The lab's existing routes (what an openai/math result would have to improve on)
- Good primes p ≥ 5: Kurihara witnesses (Mazur–Tate elements / production symbols): r_p := minimal length of a
  mod-p unit Kurihara witness = dim Sel_p(E/Q); r_p = 2 ⟺ Ш[p^∞] = 0. Also the K-route (TASK.md): a Gross-packet
  second moment M_2(p) ≠ 0 ⇒ Ш[p^∞] = 0 (via Bertolini–Darmon / BLV anticyclotomic main conjecture + derived heights),
  whose cost is a seed-scale definite-quaternion (Brandt / Shimura-set) enumeration (class set ~5·10^14) — UNAFFORDABLE.
- Bad primes 2243, 4547, 5843: B.18 (Bullach–Honnor-type criterion with production symbols [a/l]^+, l ≡ 1 mod p):
  C_0 ≡ C_1 ≡ 0, C_2 ≢ 0 mod p ⇒ Ш[p^∞] = 0; conditional on an unperformed computation (~31.6k–74k core-hours).
- p = 5843 (plectic route, work/plectic_step2_return_2026-09-30/): Fornea–Gehrmann (arXiv 2311.03100v2) Thm 3.4:
  L(E/K,1) = 0 and mock plectic invariant Q_K ≠ 0 ⇒ corank Sel_{p^∞}(E/K) = 2 ⇒ (with E^{-7} corank 0) Ш(E/Q)[5843^∞]
  finite. Q_K ≠ 0 was reduced to lemma TH: nonvanishing mod p^k of the first derivative at the trivial character of a
  level-raised anticyclotomic theta element (bipartite Euler system, FG25 Def 3.14). FG25 Remark 3.5 names the
  obstacle to the converse of Thm 3.4: the full Heegner-point main conjecture at a multiplicative prime p inert in K
  (exceptional zero of the anticyclotomic p-adic L-function at the trivial character).
- p = 3: done (see above); p = 2: done (Ш[2] = 0).

## What counts as "usable" (answer these for every candidate item)
1. Exact statement (verbatim, with section/theorem number and file path) and ALL hypotheses.
2. Which seed obligation it serves: FIN / ORDER9 / Q36 / Ш[p^∞] at a named p / #Ш(E^{-7}) / lemma TH / cost reduction
   of an existing lab computation / a general theorem replacing a hypothesis in an existing lab chain.
3. Hypothesis check against the seed data above, prime by prime (2, 3, 2243, 4547, 5843, good ordinary, good
   supersingular). Note where the seed does NOT satisfy a hypothesis (e.g. Selmer corank ≤ 1, squarefree conductor,
   semistability, ρ̄ surjective, p ∤ N, p ≥ 5, no additive reduction, rational torsion conditions).
4. Whether the manuscript proves it or imports it (name the imported published theorem) — and whether it depends on
   another OAI manuscript (which one; was that one withdrawn/revised per history.md).
5. What the lab would still have to do (computation, verification of the manuscript, grading).
Kill tests: K-A (never assume a conjecture, Ш finite, rank-2 Gross–Zagier, or the desired conclusion); K-RANK2 (a
result needing Selmer corank ≤ 1 cannot apply to E; it may apply to E^{-7}); K-GRADE (an unrefereed AI manuscript is
never better than IMPORTED_PREPRINT; a Lean-checked statement is LEAN_CHECKED only for the exact formal statement).

## LATEST LAB STATE (added 2026-10-11 from branch research/state-sync-2026-10-04 @ 9793ff7b) — READ THIS TOO
Primary results now settled (grade: source-audited published theorem + certified computation, not Lean): Ш[2^∞] = 0;
Ш[3^∞] ≅ (Z/3)^2; Ш[p^∞] = 0 for every good prime 5 ≤ p ≤ 47 (singleton Ota witnesses c_2(θ_ℓ) ≢ 0 mod p at
p = 17, 19, 23, 29, 31, 37, 41, 43, 47; smaller p from the v0.2.6 record). Consequently (CURRENT_STATE.md):
- FIN: open. "Uniform part" (cofinitely many p) has NO theorem. Named finite remainder: 59, 487, 2243, 4547, 5843.
- ORDER9: under FIN, #Ш = 9 or #Ш ≥ 25,281 (= 9·53²); vanishing at all p ≥ 53 would suffice.
- Q36: rationality of q_E with reduced denominator ≤ 174 plus the retained interval would force q_E = 36; neither is
  supplied. The lab's live analytic endpoint is written as L''(E,1)/(2 Ω_E Reg(E)) = 36.
- Current derivative target (Kato route, good p ≥ 5 outside {19,59,487}): δ_p = A_p κ(P1) + B_p κ(P2) ≠ 0 and
  m_p − w_p ≤ 1 ⇒ Ш[p^∞] = 0 (written conditional proof, desk-reviewed). Missing: cofinite nonvanishing and the
  "excess-content" estimate m_p − w_p ≤ 1 outside a finite set. Another sufficient route: a proved tame identity
  C2(p,ℓ) = 288(a_ℓ − 2)R_(p,ℓ) at G2-detecting auxiliaries for cofinitely many p (the six control curves use
  curve-dependent constants 8,4,16,8,16,32, not 288; untested on the seed).
- Retained inputs you may cite as "retained" (with their recorded grades): rank-two basis, analytic rank ≥ 2,
  residual-image statement A.3 (large image at the relevant primes), Tamagawa 16, Manin lattice A.4.

THREE PRIOR SCREENS OF openai/math ALREADY EXIST — your job is the DELTA, not a repeat:
1. Claude audit 2026-10-06: <S>/lab_latest/work/returns/BSD_OPENAI_RELEASE_AUDIT_CLAUDE_2026-10-06/OPENAI_RELEASE_AUDIT.md
   and .../BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06/GATE4_CHECK.md. Conclusions: release supplies "transport
   machinery" (obstruction span, Bockstein alternation, determinant switches, missing-vertex group-ring transfer) but
   no rank-two global anchor; Exact-BSD §1/§5/§10 read: its rational anchor is rank ≤ 1 in three places (X_p needs
   Q_E ∈ Q; tame Gross–Zagier spectral identity; a(E)+a(E^D) = 1 at the center). GATE4 fails with the known anchor.
2. Codex screen 2026-10-11: <S>/lab_latest/work/returns/BSD_OPENAI_MATH_SCREEN_CODEX_2026-10-11/{REPORT.md,
   WHAT_TO_REUSE.md, notes/DIRECT_BSD_AUDIT.md, notes/ADJACENT_ARITHMETIC.md, notes/GLOBAL_CYCLE_SCOPE.md,
   notes/FORMALIZATION_SCOPE.md}. Conclusions: headline corank ≤ 1 theorems cannot apply to E (Kummer injection
   gives corank ≥ 2 at every q); reusable pieces = (a) pointwise-2-converse `co:kummer`/`co:theta-bridge`/
   `co:weighted-comparison` finite-field Kummer detector + weighted theta coefficient formula (but its plus-detector
   is incompatible with the seed's Frobenius −I G2 primes; rank-one Heegner sum, not a two-point determinant);
   (b) Exact-BSD `models:series-division` (03-models.tex:538-590), an integrality lemma, NOT a valuation bound (exact
   countercontrol L = u + p^a, B = L²); (c) Exact-BSD §8–9 `extraction:theta-implication`/`unit:simultaneous-jumps`
   (analytic horizontal zeros ⇒ Selmer jumps) whose arithmetic step uses central acyclicity from ONE point-generated
   Selmer line (`vertical:parity`, 04-vertical.tex:252-266) — fails for the seed's two-point plane; (d) Milne-rationality
   §2 intersection-ratio normalization (technique only); (e) Lean: pinned formal-log / formal-group modules reusable
   for local formalizations; no main-result Lean for any screened arithmetic family. "Do not repeat": corank-one
   headline application; rank-two missing-vertex/switch unchanged; first-order obstruction / order-3 point-lift
   campaign; rank-one twist identities as the seed identity; Goldfeld density for this curve.
3. Codex CM comparison push 2026-10-11: <S>/lab_latest/work/returns/BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11/
   REPORT.md: used Exact-BSD §3,4,6,8,9,10 + the 2-converse coefficients section to build an explicit degree-corrected
   CM map (2T_5 − T_13 + 2 acts as 2) and repair a finite-modulus assembly; no CM nonvanishing or bound.
Also: the lab's "Aristotle" returns (Oct 6–7) tested rank-two anchor / derived-Gross / 1-motive / OpenAI rank-two
mechanisms: all PRECISE_OBSTRUCTION or NO_CANONICAL_GENERATOR; see <S>/lab_latest/work/returns/README.md.
(<S> = /tmp/claude-0/-home-user-bsd-seed-lab/ab9d3026-f88f-51d1-8e47-f94a5d2c0e6f/scratchpad)

WHAT IS STILL UNASSESSED BY THOSE SCREENS (assess these; mark each as NEW or ALREADY-COVERED):
U1 The twist E^{-7}: s_q(E^{-7}) = 0 for all q, so Exact-BSD thm:main (if correct) gives the full BSD formula and
   #Ш(E^{-7}/Q)[p^∞] at EVERY p including 2, 3, 2243, 4547, 5843 — new relative to GZK (which gives finiteness only).
   Does any lab route (K-route bound v_p#Ш(E/K)[p^∞] ≤ 2c; plectic route at 5843; Q36 via L(E/K) = L(E)L(E^{-7}))
   actually consume #Ш(E^{-7})[p^∞] or the BSD formula of E^{-7}?
U2 Rank-independent intermediate theorems at the seed's BAD primes 2243, 4547, 5843 (and 59, 487): IMC / control /
   Euler-system / Kato-normalization statements proved for all curves at multiplicative or additive primes — can any
   replace a hypothesis in a Skinner-2016-type chain (IMC + control + p-adic height nondegeneracy + leading term) or
   in B.18 at those primes? The Selmer-converse paper handles the additive prime 3 for cubic twists: is there a
   general additive-prime theorem?
U3 Anticyclotomic / Heegner-point main conjecture content in the Selmer-converse, Exact-BSD and two-primary papers
   (they cite Bertolini–Darmon, Perrin-Riou, level raising): anything at p | N multiplicative, p inert in K — the FG25
   Remark 3.5 obstacle for the plectic route at 5843 (lemma TH: nonvanishing of c_1(λ_ℓ)).
U4 The uniform (cofinite) problem: any statement controlling Selmer/Ш at all but finitely many p for a fixed curve
   of rank 2 (expected none; confirm with locations). Any cofinite "excess content" or Kato-divisibility estimate.
U5 Cost reduction for the lab's actual computations (singleton Ota witnesses c_2(θ_ℓ) at p = 59, 487; B.18 production
   symbols at 2243, 4547, 5843; lemma TH's c_1(λ_ℓ) at 5843; Shii's theta/Fitting comparison at inert supersingular p).

## UPDATE 2026-10-11 (later): lab branch head is now 4a251748 (Codex return BSD_SHII_THETA_PERIOD_PUSH_CODEX_2026-10-11,
exported to <S>/lab_latest/work/returns/BSD_SHII_THETA_PERIOD_PUSH_CODEX_2026-10-11/REPORT.md). Status there:
SIGNED_SOURCE_AND_TWO_LAYER_EXTRACTION_DERIVED; LOCAL_PERIOD_COMPARISON_REPAIRED; NO_NEW_SEED_BOUND. Content: on good
supersingular p inert in K (p ≠ 7) the signed quadratic jets of Shii's theta source are two residues from layers of
conductor p² and p³ (formulas for β_p^±); Shii's Fitting theorem gives Θ_n ι(Θ_n) ∈ Fitt(Sel_{p^∞}(E/K_n)^∨) — the
PRODUCT, so a unit quadratic coefficient alone does NOT bound Ш (abstract control M_a with arbitrarily large finite
length); a local Lubin–Tate period comparison is repaired on a rank-one CM coefficient line. Missing: an integral
arithmetic map from those source classes to the seed's controlled quotient / actual Kato derivative. Consequence for
this scan: any openai/math item that only supplies "a nonzero theta/derivative coefficient" is NOT a seed bound; it
must supply the map or an independent bound. FIN, ORDER9, Q36 unchanged.

## TWIST E^{-7} — what the lab ALREADY records (for grading candidate twist-E-7; from the Oct-4 compendium on branch
## research/state-sync-2026-10-04, file work/returns/BSD_ARISTOTLE_RESEARCH_CONTINUATION_2026-10-06/submission/
## BSD_ARISTOTLE_CONTINUATION_2026-10-06/FULL_COMPENDIUM.md lines 947-949, 1123, 1137, 1147-1155)
- PARI record: E^{-7} Tamagawa product 32 (c_2=2, c_3=2, c_7=2, c_2243=1, c_4547=2, c_5843=2), torsion Z/2, Kodaira at
  2,3,7,4547: I1*, I2, I0*, III; total real period Ω^tot_{E^{-7}} = 0.0230978825323144454978352...; "Under BSD,
  B = 392 predicts #Sha(E^{-7}) = 392·4/32 = 49 = 7² (sanity check only; explicitly outside the audit's conclusion)".
  Independent pure-Python replay in this session (scratchpad/checks/twist_bsd_quotient.py): Ω_E = 0.056089803039 (matches
  the lab's AGM value), Ω_{E^{-7}} = 0.023097882532, Tamagawa 32, predicted #Sha ∈ [48.99972, 49.00028] from the K.2
  interval; torsion ≤ 2 by point counts over F_5..F_41. So "#Sha(E^{-7}/Q) = 49" is a RECORDED PREDICTION, not new.
- Aristotle twist-Sha run (line 947-949): "For no p ≥ 5 is Sha(E^{-7}/Q)[p^∞] = 0 unconditionally proved; support
  finite (Kolyvagin) with no explicit set. ... Best achievable even with exact L: vanishing outside {7, 4547, 5843}."
  Kato bound with #Sha_an = 49 gives ord_p #Sha(E^{-7}) ≤ 0 for p ≥ 5 ∉ {7, 4547}, conditional on Manin constant ≤ 2
  and a DISPUTED coverage of 5843 (line 1123). The certified L-interval does not pin the exact rational L/Ω at any p.
- "CASSELS_TATE_SHORTCUT.md: twist Sha support moved off the critical path for the seed" (line 1133).
Consequence for grading twist-E-7: family 002 (if its chain were correct) would turn the recorded prediction into
#Sha(E^{-7}/Q) = 49 exactly and Sha(E^{-7})[p^∞] = 0 for every p ≠ 7 INCLUDING 2, 3, 4547, 5843 — beyond what the
lab's own attempts reached — but at grade IMPORTED_PREPRINT (unrefereed AI chain, no Lean) and for a quantity the lab
has moved off the critical path. State both halves.
