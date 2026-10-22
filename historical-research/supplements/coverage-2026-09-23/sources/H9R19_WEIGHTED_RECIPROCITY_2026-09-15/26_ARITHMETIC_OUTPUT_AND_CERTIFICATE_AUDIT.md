# 26 — ARITHMETIC-OUTPUT AUDIT + CERTIFICATE AUDIT of Pro's H9 arithmetic-gate note (2026-09-16)
Read-only. No new H9R number. No agent launched. Nothing built. H41 untouched (frozen).

Input: `25_SRC_pro_H9_arithmetic_gate_and_finite_certificate_2026-09-16.md` (byte copy; sha256 41ded167685996154305bdfd77450b898916d9a0f1137419baaa317aa2635e89),
relayed by the operator with this instruction: "Do a read-only arithmetic-output audit before further H9 construction. Fix the exact target as
E(Q)⊗Q_p, and test whether the descended tower output is confined to one rational direction; if it is, record the resulting strict-localization
obstruction. Do not try to obtain independence merely by varying auxiliary generalized Kato classes. Then select one genuinely new arithmetic
source [...]. Choose explicitly between one benchmark, a narrower family and the current universal target. Build only after identifying the new
arithmetic obligation and its failure test."
Also attached: PROOF.md, sha256 71024db1ca0893acf7cd20bd271fc80be5a6faf209feb15635b3a8d24201f2e3 = sealed H41 rev 3 (byte-identical to
~/H41_MOD4_SUCCESSOR_PROOF_2026-09-16/PROOF.md). Context only; nothing in it is used or changed.

## Sources (local line numbers)
[C]    Castella, "Nonvanishing of generalised Kato classes and Iwasawa main conjectures" = lane file 22: Thm A l.88-102; Remarks l.103-114;
       Choice 5.2.1 l.839-846; Thm 5.2.3 l.861-866; p-parity [Nek01] in the proof l.1012; Sel(Q) = Sel(K) l.1016; Rem 5.4.1 l.1020-1026.
[CH]   Castella–Hsieh arXiv 1809.09066, ~/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15/sources/CastellaHsieh_1809.09066.txt (sha256 8302d020...):
       Thm A l.155-161; Cor B l.182-184; names l.185-187; Cor C l.188-189; filtration (5.1)-(5.2), S = S^+, odd layers trivial, S^(inf) = 0 [CV05]
       l.1388-1400; ord_J L_p = 2r l.1417; (5.5) l.1420; leading coefficient l.1422; BD05 divisibility 2rho >= e_1 + 2e_2 + ... l.1441;
       Cor 5.1 l.1448; sec 6 l.1457-1476 (BD05 Cor 3 at l.1469; Cor B at l.1476).
[CHpub] Castella–Hsieh, Forum Math. Sigma 10 (2022) e12, doi 10.1017/fms.2021.85, publisher page read through a web summary (NOT verbatim):
       Theorem B = hypotheses of Theorem A plus rank_Z E(Q) > 0; conclusion ord_T Theta_{f/K} = 2 => kappa_{alpha,alpha^{-1}} != 0. Proof not read.
       The published version numbers differently from [CH]; never mix the two numberings.
[SW]   Stein–Wuthrich, "Algorithms for the arithmetic of elliptic curves using Iwasawa theory", wstein.org/papers/shark/shark.pdf
       (PDF sha256 217cc596a2784e7b1f086edbf2260b101f94175ecb627158191d2dc64dad7032; text = lane file 27): Thm 1.1 l.74-77; l.139-140;
       Thm 6.1 (Schneider, Perrin-Riou, Jones) l.1078-1088; Kato's Thm 7.3 l.1192-1194; Kato's Thm 7.4 l.1202-1203; sec 7.1 l.1224-1237.
[B26]  Banwait arXiv:2609.08431v1, abstract only (web): rank-two CM curves; rank two is an input. Matches Pro's screening. Not load-bearing.
Sealed tower: ~/H9R16C_SEALED_MILESTONE_2026-09-15: 00 theorem block; 01 sec 6, sec 8; 05 l.5-10, l.41, l.58-60.

## 1. The note, section by section
N1 (Castella Thm A transcription). CONFIRMED against [C] l.88-102: (1) kappa_p(E) != 0 => dim Sel(Q,V_pE) = 2; (2) if dim Sel = 2 then
   kappa_p(E) != 0 iff loc_p != 0 on Sel, and then kappa_p(E) spans ker(loc_p). Hypotheses (i)-(iii) and Choice 5.2.1 as the note states.
N2 (equivalence with the strictness argument). CONFIRMED. Same argument as the TERMINAL EQUIVALENCE block of 08 (cases r = 2 and r <= 1).
   The alternatives (0,2), (1,1), (2,0) and the refusal to use Mordell–Weil parity are right; Castella's own proof uses only Selmer p-parity
   ([C] l.1012).
   ACCEPTED CORRECTION C1. Castella's hypotheses give analytic rank >= 2 only ([C] l.96). So the 08 WAY-FORWARD label
   "NAME_OF_THE_WALL = rank-2 converse to Gross–Zagier–Kolyvagin" is a misnomer. By Castella–Hsieh's own names ([CH] l.185-189), Cor B
   (rank 2 + Sha finite => kappa != 0) is the rank-2 analogue of Skinner's converse and Cor C (kappa != 0 => dim Sel = 2) the rank-2
   analogue of Kolyvagin's theorem. The wall is neither. Corrected label: SELMER-CORANK-2 SHA FINITENESS, i.e.
   dim_Qp Sel(Q,V_pE) = 2 => rank E(Q) = 2 (equivalently Sha(E/Q)[p^inf] finite). It is purely algebraic.
N3 (Prop 3.1 and the vector). CONFIRMED; it is the r <= 1 case of the 08 corollary. The vector log_p(Q)delta(P) - log_p(P)delta(Q) is Castella
   Remark (2) ([C] l.107-114) and CH Cor 5.1 ([CH] l.1448), already in the record.
   Cor 3.2 (support-rank test). CONFIRMED as stated, and ADOPTED as gate G-SUPPORT. Scope added here: it constrains constructions whose outputs
   are elements of E(Q)⊗Q_p after trace, descent and projection, together with p-adic limits of their span. It does not reach derived classes
   obtained by dividing a norm-compatible family by an augmentation element (Kolyvagin, Bertolini–Darmon or Rivero type), which are not limits
   of descended outputs; those stay under file 20 and the first-derivative observation of the 08 WAY-FORWARD block.
N4 (auxiliary classes proportional). CONFIRMED: ker(loc_p) depends only on (E, p), and by [C] Thm A(2) every nonzero kappa_p(E), for every
   admissible (K, chi), spans it. [CH] Cor 5.1 already gives independence of chi for fixed K; Thm A(2) extends proportionality across K.
   ADOPTED as gate G-AUX.
N5 (inverse-limit linking). CONFIRMED (O is a domain; a compatible system x_n defines x with (alpha - beta)x = 0, so x = 0). This is gate 19,
   whose record uses d_0 = v_p(alpha - beta) for the two p-stabilizations of theta_chi. The "v_2" in the 2026-09-16 chat summary was a chat
   slip; neither 19 nor 08 contains it. No record change.
N6 (certificates). Logic CONFIRMED; the finite form of Certificate B is clause (d) of the 08 terminal block. Two refinements follow.
   R1. KAPPA IS DOWNSTREAM AT INSTANCE LEVEL. Every printed criterion for kappa != 0 consumes or implies dim Sel <= 2:
     - [CH] Thm A: kappa != 0 iff dim Sel_str = 1 (l.155-161). Input: a Selmer statement.
     - [CH] Cor B: input rank 2 and Sha[p^inf] finite (l.182-184).
     - [CH] sec 6 and [CHpub] Thm B: input exact theta order rho = 2. That input IS a Selmer bound. Odd derived layers vanish because S = S^+
       and (5.2) (l.1394-1400); S^(inf) = 0 by Cornut–Vatsal (l.1400); the Bertolini–Darmon divisibility gives 2rho >= sum_i i e_i
       (l.1441). With rho = 2: 4 >= 2(e_2 + e_4 + ...) = 2 dim S, so dim Sel(K,V_pE) = dim Sel(Q,V_pE) <= 2 ([C] l.1016 for the equality).
     - [C] Thm A(2): input dim Sel = 2.
     Consequence: Certificate A never supplies information that Certificate B lacks. Whatever certifies kappa != 0 carries dim Sel <= 2, and
     that bound plus two independent points already gives W = S, rank 2 and Sha[p^inf] finite, with kappa never used.
   R2. A KAPPA-FREE CYCLOTOMIC CERTIFICATE IS PRINTED AND MASS-COMPUTED. [SW] Thm 6.1: ord_{T=0} f_E >= r, with equality iff the p-adic height
     is nondegenerate and Sha(E/Q)(p) is finite. Kato ([SW] Thm 7.3): f_E divides L_p(E,T) for E semistable at p with rho_p surjective; Thm 7.4
     gives f_E | p^m L_p otherwise. So two independent points plus a finite computation showing ord_T L_p(E,T) <= 2 give ord f_E = 2 = r, hence
     Sha(E/Q)(p) finite. No auxiliary (K, chi), no kappa, no Choice 5.2.1. [SW] sec 7.1 carries this out for a rank-2 curve at p = 5.
     [SW] Thm 1.1 proves Sha(E/Q)[p] = 0 for 1,534,422 pairs (E non-CM, rank >= 2, conductor <= 30000, 5 <= p < 1000 good ordinary,
     mod-p representation surjective). [SW] l.139-140: the full Sha is not known finite for any curve with analytic rank >= 2.
   Consequence of R1 and R2: at instance level, the H9 objects (towers, kappa) add no arithmetic information.
N7 (finite theta-coefficient lemma). CONFIRMED: for odd p and n >= M, the T and T^2 coefficients of (1+T)^{p^n} - 1 are p^n and p^n(p^n - 1)/2,
   both divisible by p^M, so O[Gamma/Gamma^{p^n}] -> (O/p^M)[T]/(T^3) is well defined and the formula follows. Requirements 1-4 are right.
   Normalization anchor: CH's leading coefficient is Theta mod J^{rho+1} with J the augmentation ideal ([CH] l.1422). The cyclotomic analogue
   of the lemma is the computation R2 needs.
N8 (next-operation contract). ADOPTED, as the admission gate of sec 3.
Chat claim withdrawn: "no unconditional method exists for any family" (2026-09-16 chat, never in the record) was unsupported. Correct form: no
printed uniform theorem; printed instance certificates exist (p-descent; [SW]; [CH] sec 6); a family theorem needs a new uniform Selmer bound.
Not verified here: [CHpub] verbatim and its proof; BD05 Cor 3; Kato 17.4 and the proofs behind [SW]; [B26] beyond its abstract.

## 2. Arithmetic-output audit of the sealed tower (target fixed: E(Q)⊗Q_p inside S = Sel(Q,V_pE))
(a) Output type. Q_r lies in Hom_{Z_p}(B^bal_r, Ĵ^(1)_r(F'_r)^ord)^{Gal(F'_r/K_0),⋆}, with J^(1)_r = Jac X_1(N_f p^r) and F'_r = Q(mu_{Np^r})
    (00 theorem block; 01 sec 8). These are Hom-valued Jacobian points over cyclotomic fields: raw outputs in the note's sense, not elements of
    E(Q)⊗Q_p.
(b) Descent. The only chain to the target is a sealed non-claim: "the chain P^nat_inf -> P^nat_{inf,p_g} -> (E(Q)⊗Q_p)⊗^R_{g,p_g} --lambda_g-->
    E(Q)⊗F_g | NOT PROVED, and does not follow from anything sealed here" (05 l.41). Also sealed: no statement about weight-one specialization
    or E(Q), and "No claim that the point tower is non-torsion" (05 l.58-60).
(c) Branches. The only proved weight-one specialization attached to this construction is the same-root class kappa_{alpha,beta^{-1}} = 0
    (08 top block; [CH] Thm A l.159). The live class kappa_{alpha,alpha^{-1}} is on the conjugate branch, and the point tower does not retarget
    there (08, supersession after file 09).
```
DESCENDED_OUTPUT_IN_E(Q)⊗Q_p    = NOT DEFINED in the sealed record (05 l.41)
SUPPORT_RANK_TEST (note Cor 3.2) = NO INPUT: it can neither pass nor kill the sealed tower
OUTPUT_ON_LIVE_BRANCH           = NONE (no retargeting); same-root branch output = 0, trivially confined, no new information
STRICT_LOCALIZATION_OBSTRUCTION = NOT RECORDED AS NEW (its hypothesis is unmet). Recorded instead as gate G-SUPPORT for any future
                                  definition of a descended output: its span must be able to reach two rational directions.
```

## 3. Admission gate for any further H9 proposal (note sec 8, refined)
G-DATUM   Name the new arithmetic datum: two rational directions, an independent Selmer or Sha bound, or a construction with a stated non-collapse test.
G-MECH    Name the mechanism that supplies it, independent of the conclusion targeted.
G-REUSE   When reusing a stopped route (same-sheet trace; line IV Q3; cross-sheet; approximants; CM model; congruence linking; derived point;
          Brauer splitting), name the exact hypothesis or equation that changes.
G-SUPPORT Descended outputs must be able to span two rational directions (note Cor 3.2).
G-AUX     Varying the auxiliary (K, chi) never supplies independence (note sec 4).
G-CYC     If the arithmetic source is a Selmer bound, state what it adds over the printed kappa-free certificates (R1, R2).
G-TEST    A bounded failure test runs before any construction.
This replaces the 2026-09-16 chat wording "every proposal must say where its second point comes from". The 08 WAY-FORWARD recommendation
("names its second point or its second-derivative-to-point mechanism") remains compatible.

## 4. Quantifier choice (the instruction's required explicit choice)
UNIVERSAL        This is the whole-map target (audit 14: H9 = quantified family over the Castella/CH hypotheses). Nothing in the record or in
                 the note meets G-DATUM and G-MECH for it. STATUS: no admissible mechanism.
BENCHMARK        Excluded by name under the operator's $1M-only rule (rule 3 lists "a benchmark"). It also adds no arithmetic: CH sec 6
                 tabulates rank-2 instances, [SW] Thm 1.1 covers 1,534,422 rank >= 2 pairs, and kappa is downstream (R1). Its failure test
                 cannot fail informatively.
NARROWER FAMILY  Excluded by name under rule 3 ("a special family") unless the operator overrides. If overridden, the obligation is a NEW
                 uniform Selmer bound on a family with two independent sections. By R2 the kappa-free tool would be uniform control of
                 ord_T L_p <= 2, e.g. through the cyclotomic lambda-invariant under mod-p congruences (Greenberg–Vatsal; not re-read).
                 First failure test: does a positive-dimensional family with constant E[p] and two independent sections exist?
                 NOT RUN. NOT A CANDIDATE.
```
QUANTIFIER_CHOICE = UNIVERSAL TARGET RETAINED
NEW_ARITHMETIC_SOURCE_SELECTED = NONE ADMISSIBLE
BUILD = NONE
LANE_STATUS = UNCHANGED: CLOSED AT THE RANK-2 (SELMER-CORANK-2) SHA-FINITENESS BOUNDARY
```

## SUPERSESSION (2026-09-16, after Pro's response; source = file 28, check = file 31) — the text above is kept unedited
- SC1 status words: "LANE_STATUS = UNCHANGED: CLOSED AT ..." in sec 4 reads as CURRENT_H9_CONSTRUCTION = STOPPED AT ITS RECORDED
  BOUNDARY; UNIFORM_H9_ARITHMETIC_TARGET = OPEN; NEW_ADMITTED_MECHANISM = NONE IDENTIFIED. "Closed" here never meant a proved theorem.
- SC2 N6 R1 "Certificate A never supplies information that Certificate B lacks" holds only for the inspected printed criteria, as logical
  redundancy. It is not a cost comparison. A new geometric proof of kappa != 0 or of kappa in W would be new information.
- SC3 N6 closing sentence REPLACED BY: "The inspected instance criteria already contain sufficient arithmetic bounds, so adding kappa as an
  intermediate conclusion is unnecessary for those finiteness deductions. No additional arithmetic contribution of the currently sealed
  tower has been established."
- SC4 N2 C1 label: valid under the full hypotheses of Castella's Theorem A, including the auxiliary choice, with kappa_p(E) != 0; for every
  Selmer-corank-2 curve it would be a strictly stronger target.
- SC5 N6 R2's Stein–Wuthrich l.139-140 is the authors' statement at the time of writing, not a 2026 literature survey.
- SC6 sec 3: G-CYC REPLACED BY G-WSHA (information about W, V_p Sha, or kappa in W; a further upper bound on S adds nothing when
  kappa != 0). NEW G-COEFF (no finite coefficient vector algebraic over Q can be the nonzero strict class, even up to a common p-adic
  scalar; Fuchs–Pham arXiv:1412.1248v2 Thm 2.2). Full statements: file 31 sec 4.
