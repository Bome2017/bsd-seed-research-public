# 14 — Whole-map assembly and missing-input audit (2026-09-16)

Operator prompt: `~/Downloads/BSD_WHOLE_MAP_ASSEMBLY_CONFIRMATION_PROMPT_2026-09-16.md` (Pro 6's architecture proposal).
Method: filesystem evidence only. No theorem proved, nothing sealed, no agent launched, no new H9R label.
Read: 00/01/04/05/07/08/09/12/13 of this directory; `H41_BSD_MASTER_STATUS_AND_DEPENDENCY_MAP_2026-09-13.md` (Downloads);
`H41_KAPPA_PARITY_2026-09-14/KAPPA_PARITY_PROOF.md`; `H41_VERTEX_IDENTIFICATION_KILL_GATE_2026-09-15/{00,06,07,09}`;
`run013-62a1-bsd2-2026-08-22/{STATUS,BSD_CHAIN}.md`; `66B1_CONVENTIONAL_FREEZE_001/{THEOREM_STATEMENT,LITERATURE_DEPENDENT_STRONG_BSD_COROLLARY}.md`;
`POST_FS_BSD2_COMPOSITION_FREEZE_001/THEOREM_B_...md`; Banwait–Huang 2601.16044v3 (local re-extracted text, Thm 2.13 l.336, Thm 2.18 l.520);
Zhai 1409.0231 (Thm 1.5 l.156, Thm 1.7 l.204); Wan 1411.6352 (Example 9.4); `BSD_H5_H6_H6A_H6B_checkpoint_2026-09-14.md` (H7/H8 sections);
Castella–Hsieh (lane copy, sec 6 l.1462-1546, Cor B l.182); H9R16C sealed milestone; H9R19 lane files 00-24; three memory notes.
One exact computation: `scratchpad` rational-arithmetic check of the four vertex models (recorded in sec C6).
NOT retrieved: Pro 6's Brauer note/programs (not in Downloads); the H1-H4 map (no local file found; H5-H8 only); the Google Drive
H5-H9R16-C checkpoint (local `.md` truncated at H9R2, `.docx` truncated mid-word — 12 sec B); BD05 Cor. 3 (cited by CH, not in corpus).

## A. Headline verdict
WHOLE_MAP_RECONSTRUCTION = CONFIRMED WITH CORRECTIONS. Pro 6's three-layer reading is right: two logically disjoint programs (H41 twist
BSD(2)/strong BSD; H5-H9 generalized-Kato Mordell–Weil bridge — `05` "Relationship: none, logically") plus reusable verified mathematics.
The two corrections that change the execution order:
 (1) Pro's "First" operation — assemble one certified-base family through descent + nonvanishing -> BSD(2) -> BH Thm 2.13 -> strong BSD —
     is ALREADY EXECUTED in the record, twice: Run013 (62a1 family F_62: `STATUS.md` STRONG_BSD_ASSEMBLY = PASS, BH 2.13 hypotheses
     discharged row by row in `BSD_CHAIN.md` sec 6) and 66b1 (`LITERATURE_DEPENDENT_STRONG_BSD_COROLLARY.md`). What was implicit is the
     three-predicate ledger; it is made explicit in sec C2 and every inclusion is already proved in the record.
 (2) For the H9 endpoint, the record's own source (CH sec 6, l.1468-1476) asserts INSTANCE-level Sha(E/K)[p^inf]-finiteness for its
     tabulated rank-2 curves via Bertolini–Darmon [BD05, Cor. 3] from exact-order-2 vanishing of the theta element, and then kappa != 0 in
     the 2-dimensional Selmer group by Cor B. With rank 2 known, that makes the instance-level Kummer statement a printed consequence
     (sec C8). This softens H9R19 lane 08's clause "no printed theorem proves Sha[p^inf] finite for any rank >= 2 curve": no printed
     UNIFORM theorem does; the instance criterion is p-adic-analytic (ord_{T=0} Theta_{E/K} = 2), checked per curve. BD05 Cor 3 itself
     was not verified here.

## B. The three layers, with tiers (tiers as in 01: L, A, A-ref, T, E, D, O)
| Layer | Established (tier) | Still to supply |
|---|---|---|
| H41 formal core | E_q(Q)/2E_q(Q) = C_2, rank 0, Finite E_q(Q) on H41, both branches (L, receipts) | nothing; do not re-enter (08 items 1-3) |
| H41 conventional | Sel_2 = C_2, rank 0, Sha[2^inf] = 0 (A/T, two audits) — NOT Lean | nothing |
| Certified-base families | F_62: BSD(2) PROVED (Zhai 1.5), strong BSD PASS qualified (BH 2.13); 66b1: BSD(2) PROVED (Zhai 1.7, full-real-period), strong BSD literature-dependent corollary; eight exact lambda certificates (E) | external-dependency/publication status; 66b1 priority (Wan 1411.6352 Ex. 9.4 lists 62a1 and 66b1 twist families as full-BSD examples "see [81]"; Nam 2018 Thm 4.9); nothing mathematical |
| Uniform H41 analytic | kappa odd, Thms A/B/C, graph lemma G (A-ref); Input 1, K1 PROVED; Thms D/D' conditional on E_0 in {E,B} + K2-K5; E_0 = E_1 uniform (A); Manin c = +-1 (T) | Target W; K2 numbering; K5 sealing; F/G; positive branch; a > 0 transfers |
| Same-sheet geometric (H9R16-C) | one-direction Jacobian-tower point system, SEALED narrowly; E(Q)-specialization a sealed NON-CLAIM | not the cross-sheet target; no transverse family (lane 20) |
| Live generalized-Kato | line-IV strict-Selmer family; Artin correspondence explicit; terminal equivalence q_Sha(kappa)=0 <=> rank 2 (Castella Thm A) | a Mordell–Weil contribution; uniformly: unprinted; per instance: CH sec 6 + BD05 Cor 3 (sec C8) |
| Checkers | Brauer identity (16) + sup(n-a_n)=inf; (TC); finite congruence (F4); Artin coevaluation (G2); strict-line criterion | witnesses |
The historical slogan F_ff -> S_dyadic -> saturation -> delta -> P04c is NOT the DAG: `dependency_graph.json` (35 edges) has no edge
touching F_ff; the formal chain is Run013 definitions -> S_dyadic, delta -> P01 -> P03 -> P04c -> GateR_rank -> GateRFinite, with F_ff a
separate leaf feeding ordinarity/v_2(N_q) in Composition Theorem B. CONFIRMED.

## C. The ten claims
C1 CONFIRM. Track A complete at tier L (point-group theorems only; no H^1/Sel/Sha/BSD object, 01 boundary). Conventional Sel_2 = C_2 and
   Sha[2^inf] = 0 at A/T, not exported Lean theorems. DAG as in sec B (F_ff not an ancestor of P04c/GateR).
C2 CONFIRM, and ADD: already closed. F_62 = {q prime: q = 5 mod 8, (q/31) = -1}: Sel^phi = {1,-31,q,-31q}, dual {1}, Sel_2 = C_2, rank 0,
   Sha[2^inf] = 0 (A/T; explicit realization at L), BSD(E_q,2) via Zhai 1.5 (62a1 optimal, Manin 1, Delta < 0, L/Omega_R = 1/4), strong BSD
   via BH 2.13 with all seven hypotheses discharged (BSD_CHAIN sec 6), scope PUBLIC_PREPRINT_QUALIFIED. 66b1 family {q = 5 mod 8, (q/3) = -1,
   (q/11) = +1}: Sel^phi = {1,33,q,33q}, BSD(2) in the full-real-period convention (Omega_R = 2 Omega^+, base 1/4, Zhai 1.7 gives
   v_2(L_Z^alg(E_q)) = 1 hence v_2(L/Omega_R) = 0; c = 2, tau = 1), strong BSD literature-dependent (BH 2.13; BSTW 10.12 and BH case (3) do NOT apply).
   Three predicates, explicit: Q_alg = the family (descent). Q_transfer(62a1) = Zhai 1.5: q odd, (q,62) = 1, M = q = 1 mod 4, ord_2(N_q) = 2;
   Q_transfer(66b1) = Zhai 1.7: q = 1 mod 4, (q,66) = 1, ord_2(N_q) = 1 - (-1) = 2. Q_odd = BH (i) (q,3N) = 1 and (vii) ordinary at q.
   Inclusions Q_alg subset Q_transfer cap Q_odd are PROVED in the record: Run013 Prop A (q = 5 mod 8, (q/31) = -1 => v_2 #E(F_q) = 2,
   a_q = 2 mod 8 != 0) and the 66b1 finite-field criterion ((33/q) = (-2/q) = -1 => N_q = 4 mod 8, a_q = 2 mod 8); q = 5 mod 8 excludes 2, 3, 11, 31.
   So the intersection (C) IS the family. No uniform all-base seed is used. Uniform H41 remains a separate obligation (sec C4-C5).
C3 CONFIRM with tiers. kappa odd (Thm C), Thms A/B, graph lemma Thm G: A-ref (two fresh referees, no-repair; graph lemma rev 1 FAILED on a
   Mazur–Rapoport citation outside its 6 ∤ N convention, rev 2 PASSED). Input 1 and (K1): PROVED by Thm G(ii)-(iv). (K2): imported
   (SGA 7 I IX 11.5 / Conrad–Stein); content operator-verified via Conrad–Stein Def 4.2, numbering UNCONFIRMED (12 A2). (K3): Lemma 4.2 with PARI
   receipts m = 3,5,7,9,11. (K4): t | 4 at E, t | 2 at B, from ICR / W sec 1 table (retained audit). (K5): row equivalences from the UNSEALED
   `H41_W_MECHANISM_AUDIT.md` (12 A1, C5). Bypass of R-X/R-ID: CONFIRM (04 sec 1-2; R-X stopped 2026-09-13; W route is PATH 1). Thms D/D' are
   conditional on E_0 in {E,B} and K2-K5; never unconditional (addendum sec 4).
C4 CONFIRM. Not an AND-list (01 sec B.4.3; 07 MOVE 5). What the component-group detector cannot see: at F and G, n_F = n_G = m - 2 is odd so
   Phi[2^inf] = 0 and the cusp image lies in the identity component; F needs w_3 = 2 mod 4, a mod-4 statement; Ribet/Edixhoven's Eisenstein
   action forces a_l = l+1 mod 4 at E, mod 2 at B, nothing at F/G (vertex gate 09). Alternatives: exclude F/G (kill gate: NO_PRIMARY_SOURCE_
   EXCLUSION_FOUND; needs a bound [Lambda_f : L(E)] | 2 not through Phi[2^inf]); handle G (identity-component / unit-part data) and F (integral
   mod-4 winding lift) plus their transfer conditions; or a direct twist theorem not routed through the optimal-curve seed.
C5 CONFIRM. E_0 = E_1 uniformly on negative H41 (tier A: Ling–Oesterle Thm 1 => |Sigma(2p)| = 2^{m+1} - 1 odd; Vatsal Rmk 1.8; no odd isogenies).
   It does not select E/B/F/G; the residue is the 2-power etale isogeny E = E* -> E_0 = E_1, Target W: [Lambda_f : L(E)] | 2 (L(E_0) = Lambda_f
   exactly, Cesnavicius Thm 1.2 c = +-1). Period parameter a (09-13 master table): negative E,B,G a = 0, negative F a = 1; positive E a = 0,
   positive B a = 1, F,G a = 2. Zhai 1.5 (Delta < 0) / 1.7 (Delta > 0) require an optimal curve with odd Manin constant, E[2](Q) != 0,
   L(E,1) != 0, least-positive-real-period normalization. Positive branch (8 lambda = 2 mod 4) is a separate, BLOCKED obligation.
C6 CONFIRM, with the model check EXECUTED. Exact rational arithmetic (r = 8, 32, 2048; D = 1 - 4r): Pro's displayed E: y^2 = x^3 + (1-2r)x^2 + r^2 x,
   F: y^2 = x^3 + (-2-8r)x^2 + D^2 x, G: y^2 = x^3 + (-2+16r)x^2 + x are exactly the three curves 2-isogenous to B: y^2 = x(x-1)(x-D) (Velu
   images through the roots 0, 1, D; four distinct j-invariants). f'(0) = r^2, D^2, 1 are rational squares, so BH Thm 2.18(8b) ("none of
   f'(x_0), -f'(x_0), -Delta_E are squares") excludes E, F, G; B has full rational 2-torsion, outside (8a)/(8b). Thm 2.13 (verbatim l.336-347)
   consumes (i) (D,3N) = 1, (ii) L(E_d,1) != 0, (iii) BSD(E_d,2), (iv) a_3 in {-2..2}, (v) no rational 3/5/7-isogeny, (vi) ramified
   multiplicative witnesses, (vii) ordinary at p | d — and has NO optimality hypothesis. Optimality enters only through Zhai (Q_transfer).
   The assembly (A) is valid and, for the two certified bases, already done (C2).
C7 CONFIRM (H9R19 lane file 20; sealed 01 sec 6, 05 l.41).
C8 CONFIRM the logic (H9R19 lane 08 terminal block, both directions). Target: a QUANTIFIED FAMILY — every (E, p, K, chi) satisfying CH Thm A /
   Castella Thm A hypotheses; no model is fixed anywhere in the H5-H9 record. Instances in CH sec 6 (Theta_{E/K} vanishing to exact order 2,
   computed mod p^2 or p^3): 389a1 (p=11, K=Q(sqrt-2)), 433a1 (11, -7), 446c1 (7, -3), 563a1 (5, -1), 643a1 (5, -1), 571b1 (5, -1),
   1913a1 (7, -3), 2027a1 (13, -1), 1621a1 (11, -2). CH l.1468-1476: for these, "by the work of Bertolini–Darmon [BD95, BD05] ... (see [BD05,
   Cor. 3]) it follows that Sha(E/K)[p^inf] is finite", and by Cor B kappa_{E,K} is a nonzero class in the 2-dimensional Sel(Q, V_pE). With
   rank E(Q) = 2 known (Cremona generators), M = S and kappa is Kummer for each instance — a printed consequence, no new construction.
   BD05 Cor 3 NOT verified here. Uniformly: the exact order of Theta is a per-curve p-adic computation; no uniform theorem.
   Available global point sources: specified curve — Cremona/LMFDB Mordell–Weil generators with a positive canonical-height determinant;
   uniform — none printed (Heegner: rank 1; Chow–Heegner: line I, zero at the target; polyquadratic plectic: invariant forced to 0 in the
   tested configuration per Pro; Stark–Heegner / DR 3.12 / Darmon–Fornea 3.13: conjectural).
C9 CONFIRM. Retained system (checkpoint sec 12, H8R2): the Castella–Do anticyclotomic Euler system for V_{f,chi} from diagonal classes after
   decomposing the two CM factors (ordinary–ordinary and relaxed–strict variants, exact tame/wild norm relations); its bottom class is a twist
   of kappa_1(f,g,h) (CD Remark 5.3.1); core rank 1 for the modified (relaxed-at-p / relaxed-strict) Selmer structure; controlled module = the
   corresponding modified Selmer/dual-Selmer module, compatible with dim Sel = 2 (used in Castella's proof). Missing arrow: the comparison of
   that controlled module's Fitting/characteristic-ideal information with the Bloch–Kato sequence containing V_pSha, i.e. whether the strict
   line is Kummer rather than Sha (H8R3 target). Under the terminal equivalence that arrow is Sha[p^inf]-finiteness for rank 2; CH's instance
   route (C8) is the only printed form of it.
C10 CONFIRM (H9R19 lane 23; sup(n - a_n) = inf retained; no-lift theorem scoped to coefficient functionals, not a non-Kummer theorem).

## D. Required assembly — fully quantified endpoints
D1 Fixed certified curve family (62a1). For every prime q = 5 mod 8 with (q/31) = -1: rank E_q(Q) = 0, Sha(E_q)[2^inf] = 0, BSD(E_q, 2)
   (A/T; Zhai 1.5), and BSD(E_q) (BH 2.13; qualified by BH v3 Remark 2.11 dependencies BSTW / Castella–Ciperiani–Skinner–Sprung / Keller–Yin;
   priority caveat Nam 2018 Thm 4.9, Wan 1411.6352 Ex. 9.4). Same shape for 66b1 with its family and full-real-period normalization. DONE.
D2 Infinite twist family of one certified base: D1 is that theorem (positive-density families, Run013 Prop B density 1/8 among primes). DONE.
D3 Uniform stated H41 family: negative branch: [E_0 in {E,B}] and [K2 confirmed, K5 sealed] => 4 lambda odd => (Thm B, a = 0 at E,B) BSD(E_q,2)
   for all negative H41 twists => (BH 2.13, a_3 = 0, local premises discharged) qualified strong BSD. OPEN at Target W. Positive branch: OPEN
   (seed 8 lambda = 2 mod 4 BLOCKED; a > 0 at positive B/F/G). No all-H41 claim is available.
D4 Generalized-Kato Kummer assertion: for all (E,p,K,chi) as in Castella Thm A with kappa_p(E) != 0: kappa_p(E) in Kum(E(Q) (x) Q_p)
   <=> rank E(Q) = 2 <=> Sha[p^inf] finite. Uniformly OPEN with no printed route; instance-level: printed via CH sec 6 + BD05 Cor 3 + Cor B.
D5 Broader H1-H8 rank / strong-BSD endpoints: H1-H4 NOT_IN_RECORD locally (no file found); H5-H8 frozen statuses as in 05 (H5 MW_RATIONALITY_
   STILL_INDEPENDENT; H6/H6A UNRESOLVED; H7 V_P_SHA_REMAINS_OBSTRUCTED; H8 SYSTEM_IDENTIFICATION_PRECEDES_PRIMITIVITY; H8R2 as in C9).
   After Kummer realization (given kappa != 0): rank 2 and Sha[p^inf] finite follow; NOT obtained: analytic rank 2, the leading-coefficient
   formula at p, other primes, and kappa != 0 itself.

## E. Return block
```
WHOLE_MAP_RECONSTRUCTION = CONFIRMED WITH CORRECTIONS (sec A (1)-(2))
CLAIMS = 1 CONFIRM; 2 CONFIRM+ADD(already closed for 62a1 and 66b1; predicates explicit, inclusions proved); 3 CONFIRM (tiers listed; K2 numbering
         unconfirmed, K5 unsealed); 4 CONFIRM; 5 CONFIRM; 6 CONFIRM (model check executed); 7 CONFIRM; 8 CONFIRM+ADD(quantified family; instance
         route printed via CH sec 6/BD05 Cor 3, unverified here); 9 CONFIRM; 10 CONFIRM
MISSING_OLDER_BRANCHES = H1-H4 map (NOT_IN_RECORD locally); H5-H9R16-C authoritative checkpoint (Drive only; local .md truncated at H9R2, .docx
         truncated mid-word); Pro 6's Brauer note/programs (not local); BD05 (cited by CH, not in corpus); K5's source unsealed; K2 numbering
ALREADY_COMPLETE_ENDPOINTS = Track A (L) and A' (A/T) on all H41; F_62 and 66b1 families: BSD(2) PROVED, strong BSD qualified; eight exact lambda
         certificates (E); E_0 = E_1 (A); kappa odd + Thms A-C + graph lemma (A-ref); Thms D/D' (conditional); H9R16-C sealed (narrow); H9R19
         reconstruction; terminal equivalence; Brauer checker
SHORTEST_VALID_H41_ASSEMBLY = certified bases: DONE (Run013 BSD_CHAIN sec 6; 66b1 corollary). Uniform negative: Target W -> Thms D/D' (with K2
         confirmed, K5 sealed) -> 4 lambda odd -> Thm B (a = 0 at E,B) -> BSD(2) -> BH 2.13 -> qualified strong BSD
EXACT_NEGATIVE_E_B_IMPLICATION = E_0 = E: Phi_E[2^inf] = Z/4, kappa odd + K1 => Phi(q)(sp_J c) of order 4 => 4 | t, K4 t | 4 => t = 4 <=>(K5)
         w_3 = 1 mod 2 <=> 4 lambda odd; E_0 = B: Phi_B[2^inf] = Z/2 => t = 2 <=> same bit. Tier A-ref, conditional on E_0 in {E,B}, K2-K5
UNIFORM_NEGATIVE_REMAINING_ALTERNATIVES = (exclude F/G: needs [Lambda_f : L(E)] | 2 by a mechanism not through Phi[2^inf]) OR (handle G via
         identity-component data and F via an integral mod-4 winding lift, plus F's a = 1 transfer) OR (a direct twist theorem not routed through
         the optimal-curve seed). Not an AND-list
POSITIVE_BRANCH_REMAINING_OBLIGATIONS = seed 8 lambda = 2 mod 4 (positive divisibility known only at 2^{max(a-1,0)}); a > 0 at positive B/F/G
         (transfer inapplicable); only positive E has a = 0
CURRENT_VERTEX_THEOREM = E_0 = E_1 on all negative H41 (A); c = +-1; L(E_0) = Lambda_f; E_0 = E verified at m+2 in {5,7,13,17}; Target W
         [Lambda_f : L(E)] | 2 <=> E_0 in {E,B}; PARKED (unparking condition 01 sec B.4.3); computation exhausted (next N = 1048574)
H9_ACTUAL_CURVE_OR_QUANTIFIED_FAMILY = QUANTIFIED FAMILY (Castella/CH Thm A hypotheses); no model fixed; CH sec 6 instances listed in C8
H9_AVAILABLE_GLOBAL_POINT_SOURCES = specified curve: Cremona/LMFDB generators + height determinant (executable); uniform: NONE printed
H7_H8_CONTROLLED_MODULE_AND_MISSING_SHA_ARROW = Castella–Do anticyclotomic Euler system (bottom class a twist of kappa_1(f,g,h)); core rank 1 for
         the modified Selmer structure; missing = comparison of its controlled dual-Selmer/Fitting data with the V_pSha quotient (strict line
         Kummer vs Sha) — equivalent to rank-2 Sha finiteness
OBLIGATIONS_REMAINING_AFTER_H9_KUMMER = kappa != 0 itself; analytic rank 2; leading-coefficient/regulator formula at p; other primes; H1-H4 endpoints
TRUE_SCOPED_NO_GO_RESULTS = Phi[2^inf] = 0 at F,G (kappa route blind); kappa != T_p; R-X socle stop; H9R23 no-lift (coefficient functionals only);
         congruence-linking (a_p = alpha vs beta); derived-point (no transverse direction); CM polarization hits Ind chi^2; Brauer witnesses
         have no source; Rivero's vanishing needs split-multiplicative f; endpoint <=> rank 2
OPEN_GAPS_WITH_REAL_SOURCE_OBJECTS = Target W (lattices Lambda_f, L(E), the etale 2-power isogeny E -> E_0); G (identity component of the Neron
         model at 2 / cusp image); F (integral winding element mod 4); positive seed (u_l in U_0); K2 numbering, K5 sealing (sources exist);
         H9 instance route (theta element exact order, BD05 Cor 3 — verify the citation)
CHECKERS_WITHOUT_WITNESSES = Brauer (16) + sup(n-a_n) = inf; (TC); finite congruence (F4); Artin coevaluation (G2); strict-line criterion
FIRST_EXECUTABLE_OPERATION = MOVE 3 of 07: confirm (K2)'s SGA 7 numbering and seal (K5) (restate the W-audit row equivalences inside a sealed object),
         then package the conditional negative-E/B family theorem (Thms D/D' + Thm B + BH 2.13) with hypotheses and predicates explicit.
         Bookkeeping with definite answers; no new idea required. (Pro's "First" is already done — do not redo it.)
EXPECTED_THEOREM_OUTPUT = "For every negative H41 base with E_0 in {E,B}, and every q in the H41 twist family, BSD(E_q,2) holds; under BH 2.13's
         disclosed dependencies, BSD(E_q)." Fully quantified, conditional, sealed inputs
EXACT_STOP_CONDITION = (K2) numbering cannot be matched to SGA 7 I IX 11.5 / Conrad–Stein, or a (K5) row equivalence fails re-derivation from
         W sec 2 — then Thms D/D' lose their stated tier and the package is not issued
ONE_IMMEDIATE_OPERATION = the FIRST_EXECUTABLE_OPERATION above
ONE_RESEARCH_OPERATION = Target W: bound [Lambda_f : L(E)] by 2 for negative H41 — source objects exist (modular-symbol lattice, Neron lattices,
         the etale isogeny); the missing input is a mechanism not measured by Phi[2^inf] (unparking condition). For H9 there is no research
         operation with a defined map; its missing input is a second rational point / Sha finiteness, and the only printed instance route is
         CH sec 6 + BD05 Cor 3 (verify BD05 before using it)
```

## F. Supersession (2026-09-16, later the same day): the vertex gate has a supplied proof
Operator packet (Downloads/PROOF.md + bsd_precontinuation_audit_2026-09-16.zip) supplies a proof that E_0 in {E,B} on every negative
H41 base: all-node residues (sealed Thm B) read in the toric character coordinates (sealed Thm C(i)) make every coordinate of q^* xi
odd; the length pairing then makes <X_J, q^* xi> even; Conrad–Stein Lemma 6.3 + Theorem 8.2 (verified verbatim, any DVR) give
n_0 = ord_2 Delta_min(E_0) even; n_F = n_G = m-2 is odd. First hostile audit PASS with remarks: ~/H41_VERTEX_EXCLUSION_AUDIT_2026-09-16/00.
Effect if a second fresh referee concurs: VERTEX_ROUTE PARKED -> CLOSED (negative); Thms D/D' lose the vertex hypothesis; negative seed
4 lambda odd for all negative H41 given Inputs 1-6; with Theorem B (a = 0 at E,B) BSD(E_q,2) on the H41 family; with BH 2.13 applied to
the ORIGINAL E (uniform (i),(iv)-(vii) per the packet, verified) qualified BSD(E_q). Sec E's FIRST_EXECUTABLE_OPERATION is superseded
by: second referee on PROOF.md; cite the length-pairing identification in the seal; seal K5; then package. Sec E's ONE_RESEARCH_
OPERATION (Target W) is discharged in its vertex form by this proof (Target W follows via kill-gate 07 sec 1). H9 rows unchanged; the
Drive-checkpoint reconciliation is in ~/H41_VERTEX_EXCLUSION_AUDIT_2026-09-16/01 (finite maps sealed; route hits the vanishing class).

## G. Positive branch (2026-09-16, later): kill test NOT KILLED — see ~/H41_POSITIVE_KILL_TEST_2026-09-16/00_RESULT.md
Slopes of the retained N = 6l unit are = 2 mod 4 uniformly (B - A = 3(l-1)); d log F = f (mod 4) at infinity is a Sturm-proved theorem at
N = 66, 258 (and = -f at 62, 254), depth exactly 4, uniform at good primes via the order-4 point. A mod-4 D3 (T1 + L1 + L2, with the
transfer by w_N since the w_2 step does not lift) would give positive E_0 = E and 8 lambda = 2 mod 4 together, hence positive BSD(2) and
qualified BSD via the existing machinery; the same mechanism gives negative E_0 = E. MOVE 6's "BLOCKED" is superseded by these named tasks.

## H. Positive branch, same day: T1 proved uniformly; L2 (mod-4 D3) proved from the inputs the sealed D3 uses, with w_N in place of w_2;
Cremona: the displayed H41 E is the proved optimal curve (Manin constant 1) at all ten H41 levels below 500000. Remaining before a
positive BSD(2) package: P1 (positive graph lemma), P2 (positive local form of F), L1 (integral residue/character citation), hardening,
referees. See ~/H41_POSITIVE_KILL_TEST_2026-09-16/02_T1_L2_POSITIVE_PROOF.md.

## I. H41 mod-4 successor proof: both independent referees accept (2026-09-16)
~/H41_MOD4_SUCCESSOR_PROOF_2026-09-16, PROOF.md revision 3 (sha256 71024db1ca0893ac...): two fresh no-repair referees, full reviews of rev 0/rev 1
and delta reviews of rev 2 and rev 3, all ACCEPT/PASS WITH REMARKS, 0 BLOCKING. Claims: positive H41 (E_0 = E, cusp order 2, 4 lambda odd, twist
BSD(2), BSD qualified by BH v3 Rem 2.11) and negative H41 (E_0 = E, cusp order 4, 4 lambda odd, same twist conclusions), relative to imports
I1-I13 and R9. Open non-blocking import: the Atkin–Lehner sign a_p = -epsilon_p (cross-route via Monsky 2-parity recorded in ERRATA_AFTER_REVIEW.md).
SEAL-READY (SEAL_READINESS.md); NOT sealed; operator decision. If sealed, sec E's H41 rows change: NEGATIVE/POSITIVE seeds CLOSED, vertex CLOSED
(E_0 = E both branches), twist BSD(2) CLOSED on the retained family, BSD qualified. H9 rows unchanged.

## J. SEALED 2026-09-16 (operator go-ahead): H41_MOD4_SUCCESSOR_ADDENDUM_018
    H41_MOD4_SUCCESSOR = SEALED_AREF_T   (04_RESEARCH_OBJECTS/H41_MOD4_SUCCESSOR_ADDENDUM_018, archive sha256 648120efb9780435df62e5be510bb66fcb238ad739ac83a5091ccc80b25c8415)
    POSITIVE_OPTIMAL_VERTEX = E                NEGATIVE_OPTIMAL_VERTEX = E
    POSITIVE_CUSP_ORDER = 2                    NEGATIVE_CUSP_ORDER = 4
    POSITIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
    NEGATIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
    H41_RETAINED_TWISTS_BSD2 = CLOSED
    H41_RETAINED_TWISTS_FULL_BSD = CLOSED_AT_EXTERNAL_LITERATURE_QUALIFIED_TIER (BH v3 Remark 2.11)
    OLD_VERTEX_COMPONENT_ONLY_ROUTE = HISTORICAL_FAILED_MECHANISM / SUPERSEDED
    OLD_H41_W_BLOCKED_STATUS = SUPERSEDED_BY_MOD4_INTEGRAL_CHARACTER_ROUTE
    H9_STATUS = UNCHANGED
Sections E-I of this file are superseded for the H41 rows accordingly; all H9 rows (D4, H7/H8, instance route, checkers) are unchanged.

## H41 FROZEN (operator, 2026-09-16) — custody addendum sealed
H41_W_AUDIT_IMPORT_ROWS_CUSTODY_ADDENDUM_019 (archive sha256 8cdf84fd89ff7672726982dee79b6930f4e08594dc8346b0a72ed63ebe9de831): ADDENDUM_018's imports I3-I5 are BOUND — I3 elementary given E_0 = E
(h = 1, a = 0, delta_0 = 2 or 1 by the sign of Delta); I4 (t | 2 positive E, t | 4 negative E) and I5 (z = nu0 delta0 lambda/h, reduced
denominator t) are verbatim statements of the sealed IDENTITY_COMPONENT_REVIEW.md (byte-identical to its member in CODEX_H41_SEED_RESEARCH_FREEZE_001.tar.gz).
The W audit is carried as a negative-result artifact; only its global BLOCKED status is superseded. No residual H41 custody item remains.
H41 = FROZEN: do-not-redo except an identified defect. Research frontier = the general H9 bridge (H9 rows unchanged).
