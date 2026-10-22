# F4 — Hostile literature hunt: exact rationality of L″(E,1)/(2·Ω_E·Reg(E)) (seed (2243,12))

Auditor: independent hostile referee (fresh context). Started 2026-09-18 18:25 PDT.
Target under attack: node **G26 / SRAT** of `../FULL_BSD_SEED_DAG.md` (sha256 `3e1c96b0…0985d20`), labelled OPEN, and
Lane 3's `C_frontier/C2_STATE_OF_THE_ART_2026.md` §(b) (sha256 `4efe1309…0a676501`), labelled OUT_OF_REACH.
Rules honoured: read-only outside `fable_audits/F4_*`; no ledger, memory, seal or report edited; no computation on the
seed; network used for literature only; nothing merged; no outward communication.

Status of this file: **COMPLETE (2026-09-18 21:01 PDT). RETURN = NOT_FOUND.** Read the section "FINAL VERDICT" at the end first;
CP-0 … CP-10 above it are the append-only evidence ledger (CP-2 was a provisional verdict written before the usage cap hit).
Working state: `F4_work/RESUME.md`, `F4_work/QUERY_LOG.md`, `F4_work/agents/*.md`.

## 0. The claim being hunted

Seed: E: y² = x³ − 22735x² + 106272484x, N = 2³·3·2243·4547²·5843, w = +1, E(Q) = Z/2 × Z², r_an = 2,
∏c_p = 16, #tors = 2. Certified numerics: L″(E,1)/(2·Ω·Reg) = 36 to ≈ 10⁻¹⁵ relative.
Wanted: a theorem that makes this an exact equality — (A) rationality/algebraicity, (B) a denominator bound,
(C) an arithmetic-cycle formula, (D) a p-adic comparison implying the complex identity, or (E) a special-case formula.

Logical note fixed before the hunt (so that candidates are graded correctly):
- (A) alone does **not** suffice. A rational number within 10⁻¹⁵ of 36 need not be 36; exactness needs (A) **and** (B)
  with denominator D < ≈ 10¹⁴ (so that 1/D exceeds the certified error), or an exact formula (C)/(E) whose right side
  is exactly computable.
- Any first-derivative formula is blind to the seed: if ord_{s=1} L(E,s) = 2 then every product L(E,s)·L(other,s) has
  vanishing first derivative, so Gross–Zagier-type identities read 0 = 0 (Heegner points torsion).

(checkpoints follow)

## CP-0. Set-up and custody (2026-09-18 18:31 PDT)

- Inputs hashed in `F4_work/input_hashes.txt` (DAG `3e1c96b0…`, NEXT_3_TARGETS `7383b841…`, prompts `3130ce0b…`,
  Lane 3 C2 `4efe1309…`).
- Prior state attacked: Lane 3 C2(b) answered "no" after 22 web queries (its `sources/QUERY_LOG.md`, entries 3, 11–14, 24
  bear on rationality). That log covers Yun–Zhang, the Kudla programme and BKS24 only at headline level; it does not
  touch Gross–Kohnen–Zagier, YZZ, arithmetic GGP, Beilinson/GL₂, Beilinson–Flach, Bertolini–Darmon, Darmon–Rotger, BSV,
  ETNC, Mazur–Tate, or a dated 2025–26 sweep. Those are the gaps this hunt fills.
- Five search agents launched (clusters A–E; prompts in `F4_work/agents/PROMPTS.md`; outputs `F4_work/agents/*.md`,
  append-only). Every candidate they return is re-checked by me at the primary-text level before it is graded here.
- Independent re-check of Lane 3's one load-bearing quote (done by me, local text
  `…LANE3…/C_frontier/sources/YunZhang_Taylor_published.txt`, sha256 `f1db69c6…955dd4`, l. 73–96): Yun–Zhang,
  Annals 186 (2017) §1: "In the number field case, the analogous spaces only exist (at least for the time being) when
  r ≤ 1" and "due to the lack of the analog of Sht^r_G for arbitrary r in the number field case, we could not formulate
  a precise conjecture." **VERIFIED as quoted.** Note what it does and does not say: it records the absence of a
  *conjecture*, in 2017, by those authors; it is not a statement that nothing can exist.

## 1. What would suffice — logic fixed before grading candidates

Write q := L″(E,1)/(2·Ω_E·Reg(E)). Lane 3 certified |q − 36| ≤ ε with ε = 4 × 7.5·10⁻¹⁶ = 3·10⁻¹⁵ (its Sha_an = q/4;
the observed agreement is ≈ 4·10⁻¹⁸, but only ε is certified).

1. **Rationality alone (A) is not enough.** q ∈ Q and |q − 36| ≤ ε do not give q = 36.
2. **(A) + (B) is enough, with room to spare.** If D·q ∈ Z for an explicit integer D < 1/ε ≈ 3.3·10¹⁴, then
   |Dq − 36D| ≤ Dε < 1 forces q = 36. A larger D only costs a longer certified evaluation of L″(E,1).
3. **Per-prime information cannot replace (B).** A theorem giving ord_p(q) for one p, or for finitely many p, leaves
   the denominator unbounded at all other primes. (B) needs a statement uniform in p: either an identity with explicit
   constants (Gross–Zagier type), or integrality at every prime outside an explicit finite set.
4. **First-derivative formulas are blind to the seed.** For every auxiliary L-function M(s), (L(E,s)·M(s))′ vanishes
   at s = 1 when ord L(E,s) = 2. So Gross–Zagier, YZZ, arithmetic inner product and arithmetic GGP identities
   specialise to 0 = 0 (Heegner/special cycles with torsion or null-height f-components). Only a formula of genuine
   order 2 can see L″(E,1).
5. **"(1,1)-type rank 2" is not the seed's situation.** L(E/K,s) = L(E,s)·L(E^K,s) with both factors of order 1 gives
   L″(E/K,1)/2 = L′(E,1)·L′(E^K,1), i.e. Gross–Zagier twice. The seed has a single primitive degree-2 L-function with
   a double zero; it does not factor.
6. **Independence from the algebraic side.** Even a proof of Sha(E/Q) ≅ (Z/3)² would not give q = 36, and q = 36 would
   not give finiteness of Sha: q is a complex-analytic number, and the only bridge between the two sides is the BSD
   formula itself.

## CP-1. Class (D) anchor re-verified by me in the published text (18:37 PDT)

Source: Burns–Kurihara–Sano, "On derivatives of Kato's Euler system for elliptic curves", J. Math. Soc. Japan 76 (2024)
855–919; local text `~/BSD_ABC_REVIEW_2026-09-17/sources/BKS24_jmsj76.txt` (sha256 `c8fc6dcc…81db5dc`). Numbering below is
the **published** one (the arXiv v2 numbering used by agent D is shifted by one: its Cor. 1.10 / Thm 1.13).

- **Cor. 1.11 (= Cor. 6.7), l. 333–346.** "The Generalized Perrin-Riou Conjecture (Conjecture 1.6) implies the following
  'p-adic Beilinson formula': (1 − 1/α)⁻¹(1 − 1/β)·L^{(r)}_{S,p} = [L_S^{(r)}(E,1)/(Ω⁺·R_∞)]·R_p" (good or non-split
  multiplicative p). This is the only statement in print that ties the complex r-th derivative to a p-adic one for
  r ≥ 2 — and it is an implication **from a conjecture**.
- **Thm 1.14 (= Thm 7.6), l. 373–392.** Hypotheses: Sha(E/Q) finite; r_an = r; IMC; Conj. 1.6; R^Boc_ω ≠ 0. Conclusion:
  L^{(r)}(E,1)/(Ω⁺R_∞) = u·#Sha·Tam/#tors² with u ∈ Z_p^×. Two of the user's exclusions apply at once (assumes finite
  Sha; assumes an open conjecture).
- **What is proved:** Thm 1.3 (order-of-vanishing containment only, itself under finiteness of Sha[p^∞]); Thm 1.5
  (Conj. 1.1 holds in analytic rank **one**); Thm 1.9 (generalized Rubin formula — purely p-adic).
- **How the complex number enters (l. 607):** "We fix an embedding R ↪ C_p". The real number L*_S(E,1)/(Ω⁺R_∞) is
  transported into C_p; no rationality is proved or used. *Remark (mine):* if Conj. 1.6 held for r = 2 at one prime p
  with R^Boc ≠ 0 and for every such embedding, then q would be fixed by all embeddings, hence q ∈ Q. So the conjecture
  at a single p would give (A). It would give only ord_p of q, not (B): by §1.3 that is still not enough for q = 36.
- Seed check: 3 is non-split multiplicative and 5 is good ordinary, so the formula's shape is available at both — but
  Conj. 1.6 is open for every curve with r ≥ 2. Grade: **FALSE_POSITIVE (conjectural; conditional on finite Sha)**.
  The DAG's sentence "BKS24 Cor. 1.11 is conditional" is CORRECT as written.

## CP-2. PROVISIONAL VERDICT (written early at 18:39 PDT because the usage cap may hit; superseded by any later verdict section)

**Provisional return: NOT_FOUND** — not found in the sources checked so far; this is *not* a claim of impossibility.

Evidence on disk at this checkpoint (primary-text unless marked):
- Yun–Zhang I/II: function fields only; authors "could not formulate a precise conjecture" over number fields
  (re-verified by me, CP-0). Follow-ups (Bieker 2607.07531, Z. Wang 2607.25237, Liu–Wang 2504.00275, Howard–Shnidman,
  Shnidman) are all function-field (agent A, `F4_work/agents/A_higher_GZ.md` S1–S9).
- Burns–Kurihara–Sano 2024: the only printed link between the complex L^{(r)}(E,1) and a p-adic derivative for r ≥ 2
  is Cor. 1.11, an implication from an open conjecture; Thm 1.14 assumes finite Sha (re-verified by me, CP-1).
- BKS II (Mazur–Tate): the Mazur–Tate leading term is the *algebraic* BSD constant times a Mazur–Tate regulator; the
  complex L″ does not occur in it; proved only conditionally on BSD + GPR, unconditional evidence only for r_an = 1
  (agent D, D9).
- Bley–Macias Castillo I, III; Burns–Macias Castillo–Wuthrich; Burns–Macias Castillo (Mem. AMS): despite "higher
  derivatives" in the titles, every statement is an equivalence with / consequence of eTNC or BSD; rank-2 rationality is
  checked only numerically (agent D, D5–D8).
- C.-H. Kim 2203.12161 ("higher Gross–Zagier formula"): purely algebraic comparison of Kolyvagin-system indices with
  Kurihara numbers; no complex second derivative (agent D, D2; agent A, S11).
- Banwait 2609.08431 (8 Sep 2026): p-adic, CM, per-p; nothing on complex L″ (checked by me, QUERY_LOG W4).
- Van Order 2510.10303 / 2510.10277: first central derivatives (abstract only).
- Goldfeld / Diamantis: integral and cohomological representations of derivatives, no comparison with Ω·Reg (abstract only).

**Smallest missing theorem (provisional wording):** an identity of genuine order 2 over Q,
L″(E,1) = c·Ω_E·det(⟨z_i,z_j⟩) with z₁∧z₂ ∈ ∧²E(Q) constructed and c ∈ Q^× explicit — or, more weakly, any theorem
giving D·L″(E,1)/(2ΩReg) ∈ Z for one explicit integer D (D < 3.3·10¹⁴ suffices at the present certified precision).
Rationality without a denominator bound would not suffice (§1.1–1.3).

Still running at this checkpoint: agents B (Kudla programme / AGGP), C (p-adic rank 2, Beilinson, BSV), E (2024–26 arXiv
sweep + special structure); agents A and D are writing their verdicts. Their files are append-only and readable as is.

## CP-3. Candidate ledger, part 1 — clusters A and D folded in (18:41 PDT)

Format per candidate: statement · domain · order covered · hypotheses · seed? · implication for q · status · grade.
"PT" = theorem statement read in the primary text (file and line numbers are in the agent file named); "AB" = abstract only.

### A. Higher Gross–Zagier; Yun–Zhang and follow-ups (agent file `F4_work/agents/A_higher_GZ.md`)

| # | candidate | what it says (exact shape) | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| A1 | Yun–Zhang I, Thm 1.2 (arXiv 1512.02683; Annals 186, 2017) PT | (1/(2(log q)^r))·\|ω_X\|·L^{(r)}(π_{F′},1/2) = self-intersection of the Heegner–Drinfeld cycle on Sht^r_G; π everywhere unramified, r even | **function field** k(X) | any even r | no (E is over Q) | none | published | FALSE_POSITIVE (function field) |
| A2 | Yun–Zhang II, Thm 1.3 / Cor. 1.4 (arXiv 1712.08026; Annals 189, 2019) PT | L^{(r₁)}(π,1/2)·L^{(r−r₁)}(π⊗η,1/2) = intersection number; Cor. 1.4 is the r-th derivative of a **single** L(π,s) times L(π⊗η,1/2) — exactly the shape wanted | **function field**, square-free level | any r of the right parity | no (number field; also not semistable) | none. Even there it is not a Néron–Tate regulator formula: §1.3.2 "It is not clear though how to relate the ambient space … to powers of E′" | published | FALSE_POSITIVE (function field) |
| A3 | Bieker, arXiv 2607.07531 (Jul 2026) PT; Z. Wang, arXiv 2607.25237 (Sep 2026) PT; Liu–Wang, arXiv 2504.00275 (v3 Apr 2026) PT; Howard–Shnidman (Adv. Math. 2019) PT; Shnidman (JEMS) PT; Yun ICM 2018 PT | deeper level / adjoint L-functions / higher period integrals / higher GKZ / Manin–Drinfeld cycles — all r-th derivative formulas on shtukas | **function field** | any r | no | none. Wang's number-field remark is conjectural and r = 1 only (§1.2.3) | preprints / published | FALSE_POSITIVE (function field) |
| A4 | W. Zhang ICM 2018 (arXiv 1712.08844) PT; W. Zhang survey arXiv 2402.17656 (Feb 2024) PT | no theorem; number fields have only r = 0 (automorphic quotient) and r = 1 (Shimura varieties); higher derivatives filed under "function field analogs" | number field (survey) | r ≤ 1 | — | none | survey | OPEN-STATUS witness |
| A5 | Gross–Kohnen–Zagier, Math. Ann. 278 (1987), Thm C PT | f-components of all Heegner divisors span a space of dimension 1 if L′(f,1) ≠ 0 and **0 if L′(f,1) = 0**; ⟨y_f,y_f⟩ = L′(f,1)/(4π‖f‖²) | Q | first derivative, root number −1 | no (w = +1; ord = 2) | none — degenerates to 0 = 0 | published | FALSE_POSITIVE (first derivative) |
| A6 | Bruinier–Yang (Invent. 177, 2009) Thm 1.5 PT; Bruinier–Ono (Annals 172, 2010) Thm 1.1 PT; Bruinier–Kudla–Yang AB | ⟨Z(f),Z(f)⟩_NT = (2√N/(π‖g‖²))·L′(G,1); L′(G,χ_Δ,1) = 0 ⇔ c_g⁺(Δ) algebraic (prime level) | Q | first derivative, odd functional equation | no | none | published | FALSE_POSITIVE (first derivative) |
| A7 | C.-H. Kim, "A higher Gross–Zagier formula and the structure of Selmer groups", arXiv 2203.12161v7, Thm 2.3 PT (read by agents A and D independently) | ord(κ^Heeg) + 1 = max{ord δ̃(E), ord δ̃(E^K)} = max of Selmer coranks; (2.1) equates index differences with length of Sel(K,E[p^∞])_{/div} | p-adic / algebraic | any Selmer corank | hypotheses partly available, but moot | none: "Kolyvagin derivatives of certain Mazur–Tate elements are involved instead of derivatives of Rankin–Selberg L-functions" (l. 76–78) | preprint | FALSE_POSITIVE (no complex L″; "higher GZ" in name only) |
| A8 | Kontsevich–Zagier, "Periods" (2001) §3.5, Problem 4 PT | Thm: Ω·R ∈ 𝒫 (periods). Problem 4: show L^{(r)}(f,k/2) ∈ 𝒫̂; done for r = 0, 1. If solved, BSD becomes an "accessible identity" between periods | Q | r ≥ 2 **open** (Diamantis–Rolen 2017, l. 82–85: "this conjecture is still open") | — | none. Even a solution would not be a rationality theorem: equality of two periods is decidable only via the (open) period conjecture, with no algorithm | problem / conjecture | NOT A ROUTE (pointer only) |
| A9 | Goldfeld 1995; Diamantis 1999/2001; Diamantis–Rolen; Diamantis–Strömberg (AB / PT for D–R) | Eichler-cohomology cocycles and integral formulas for derivatives of L-functions | Q | any | — | none (representation of L^{(k)}; nothing compared with Ω·Reg) | published | FALSE_POSITIVE (no arithmetic comparison) |

### D. Refined BSD, eTNC, Mazur–Tate, Burns–Kurihara–Sano (agent file `F4_work/agents/D_refined_bsd.md`)

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| D1 | BKS, JMSJ 76 (2024): Conj. 1.1/1.6, Thm 1.3, Thm 1.5, Thm 1.9, **Cor. 1.11**, **Thm 1.14** PT (re-verified by me, CP-1) | GPR conjecture ⇒ p-adic Beilinson formula linking L_S^{(r)}(E,1)/(Ω⁺R_∞) to L^{(r)}_{S,p} and R_p; Thm 1.14 gives the p-part of BSD under 5 hypotheses | E/Q, p odd | any r | no: Sha finiteness unknown; Conj. 1.6 open for r ≥ 2 | would give q ∈ Q and ord_p q **if** the conjecture held; not (B) | published; the link is conjectural | FALSE_POSITIVE (conjectural + assumes finite Sha) |
| D2 | BKS II, arXiv 2103.11535, Conj. 2.3, Thm 1.1, Cor. 1.2 PT | Mazur–Tate: θ_{F,S} ∈ I^r and θ ≡ ±L^alg·R_F in I^r/I^{r+1} with L^alg = #Sha·Tam/#tors² | Q | any r | — | **none even if proved**: the complex L^{(r)} does not occur; θ interpolates *values* L(E,χ,1)/Ω⁺ | Thm 1.1 conditional on BSD + GPR; unconditional only for r_an = 1 | FALSE_POSITIVE |
| D3 | Bley–Macias Castillo I (Crelle 722, 2017), Thm 2.6/2.8/2.9 PT; III (arXiv 1912.11260) Thm 2.1 PT | eTNC ⇔ explicit congruences between normalised derivatives; rationality C(A,Q[G]) is a conjecture assumed after l. 454; rank-2 curves (389a1, 433a1, 446d1) treated **numerically** ("very close to −46/37") | number fields | any | — | none | published | FALSE_POSITIVE (equivalences with eTNC; assumes rationality) |
| D4 | Burns–Macias Castillo–Wuthrich (Crelle 734) Thm 1.1 PT | eTNC_p for dihedral F/Q when L(A/K,s) has a **simple** zero, Sha(A_F) finite, Heegner point not p-divisible | number fields | first derivative | no | none | published | FALSE_POSITIVE (first derivative; assumes finite Sha) |
| D5 | Burns–Macias Castillo, Mem. AMS (arXiv 1909.03959) Conj. 3.3 PT | refined BSD for Hasse–Weil–Artin L-series; evidence proved only for order 0 (Kato/modular symbols) and first derivatives (Zhang/GZ) | number fields | conj. any; proved ≤ 1 | — | none | published | FALSE_POSITIVE (conjectural) |
| D6 | C.-H. Kim arXiv 2203.12159v6 (to appear AJM) Thm 1.1 PT; Kim arXiv 2609.15328 (14 Sep 2026) Thm 1.1 PT | Kurihara numbers determine Sel(Q,E[p^∞]); criterion for finiteness of Sha[p^∞] via derived Heegner points | p-adic / algebraic | any corank | partly (p ordinary) | none: "no regulator is involved in our approach" (l. 572–574); the L^{(r)}↔Sha relation appears only as Question 1.16 | preprints | IRRELEVANT to q (algebraic side only) |

Open-status sentences collected so far (all read in the primary text by an agent; K–Z and BKS24 context re-read by me):
- Kontsevich–Zagier 2001, §3.5: "We emphasize that so far there is not a single elliptic curve of rank r ≥ 2 for which (15) is known exactly, though many cases have been checked numerically to high precision."
- Yun–Zhang 2017, §1: "…we could not formulate a precise conjecture."
- Diamantis–Rolen 2017: "Apart from the cases r = 0 … and r = 1 (thanks to Gross–Zagier and others), this conjecture is still open."
- W. Zhang ICM 2018: "…one is led to the tantalizing question of finding Shtukas over number fields."
- BKS II 2021: "if r > 0, then the leading-term component of the conjecture has remained stubbornly mysterious … the only supporting numerical evidence is for the case r = 1".
- Shnidman 2022: "For r ≥ 2, our formula has no known analogue over number fields."
- C.-H. Kim, Jan 2024: "When the rank is larger than one, the situation becomes extremely puzzled. … It seems that no similar result for the number field case is addressed yet."
- Liu–Wang, v3 2 Apr 2026: "Over number fields, the geometric meaning of higher derivatives of L-functions remains mysterious even for elliptic curves, and is far out of reach in higher rank."

## CP-4. Candidate ledger, part 2 — cluster C folded in (18:42 PDT)

Self-correction recorded: my first pass over Banwait 2609.08431 used a grep that missed the key sentence (extraction
prints "L′′ (E, 1)" with a space). Grep-negative was not absence. The sentence is quoted below; I re-read it in my copy
(`F4_work/sources/coord/banwait_2609.08431.txt` l. 2377–2380).

### C. p-adic rank-2 constructions; Beilinson–Flach; Bertolini–Darmon; Darmon–Rotger; BSV (agent file `F4_work/agents/C_padic_rank2.md`)

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| C1 | Castella–Hsieh, Forum Math. Sigma 10 (2022), arXiv 1809.09066: Thm A, Cor. B, Cor. 5.1 PT | κ_{α,α⁻¹} ≠ 0 ⇔ dim Sel_str = 1; Cor. 5.1: κ = C·(Euler)·θ̄_{f/K}/h^{(ρ)}(P,Q)·(P⊗log_p Q − Q⊗log_p P), with θ̄ the leading coefficient of the **anticyclotomic** BD theta element and h^{(ρ)} a derived **p-adic** height | Q, p-adic | Selmer rank 2 | N⁻ square-free etc.; moot | none: the complex L″ never appears; only complex *values* L(E^K,1), L(E/K,χ²,1) ≠ 0 enter; Remark 1.3 leaves "(3) ⇔ (4) … the rank 2 case of BSD" open | published | FALSE_POSITIVE (p-adic; no link to complex L″) |
| C2 | Darmon–Rotger, "Elliptic curves of rank two and generalised Kato classes" (RMS 2016) Thm 3.4, Cor. 3.6, Conj. 3.8, 3.12 PT; Darmon–Rotger JAMS 30 (2017) Thms A, B, D PT | p-adic L-values L_p^{g_α}(f,g*,h) "should rather be viewed as different p-adic avatars of L″(f,g,h,1)" — *heuristic wording, no comparison theorem*; Thm B: L(E,ρ,1) = 0 and L_p^{g_α} ≠ 0 ⇒ dim Sel_p(E,ρ) ≥ 2 | number field, p-adic, ρ = ρ₁⊗ρ₂ Artin | order ≥ 2 of L(E,ρ,s) | for E/Q itself (h = ḡ) DLR predict the p-adic values **vanish** and the classes "never generate the Selmer group or Mordell–Weil group of E" (JAMS l. 393–399) | none | published / conjectures | FALSE_POSITIVE (p-adic avatar without comparison; Selmer lower bound only) |
| C3 | Darmon–Lauder–Rotger, Forum Math. Pi 3 (2015), Conjecture ES PT | p-adic iterated integral = det of a 2×2 matrix of **p-adic logarithms** of points / log_p(u); proved only when p splits in K under a Heegner hypothesis | number field, p-adic | proved case is **(1,1)-type** (BDP p-adic GZ twice) | no | none | conjecture; proved only (1,1) | FALSE_POSITIVE |
| C4 | BSV, Astérisque 434 (2022) Thm A, **Cor. B** PT | Cor. B: d²/ds² L(f⊗g⊗h,s)\|_{s=1} ≠ 0 ⇔ log_{ββ}(res_p κ_{αα}) ≠ 0. **Names the complex second derivative** — but L(f⊗g⊗h,s) = L(A/K,φ,s)·L(A/K,ψ,s), both of sign −1 | number field, p-adic, exceptional zero | **(1,1)-type** | no: the seed's L(E,s) is primitive with a double zero | none beyond GZ–Zhang for each factor; a non-vanishing equivalence only | published | FALSE_POSITIVE ((1,1)-type — the textbook instance) |
| C5 | BSV, "On p-adic analogues of the BSD conjecture for Garrett L-functions" (Ann. Inst. Fourier, online first 2026) Conj. 1.1, Thm 3.2 PT | Conj.: leading term of the Garrett–Hida p-adic L-function = p-adic regulator in I^r/I^{r+1} mod Q(ρ)^{*2}; Thm 3.2: Rubin-type formula, p-adic height of the diagonal class vs first-order term of the p-adic L-function | p-adic | any r (conj.) | — | none (complex leading term does not enter) | conjecture + p-adic theorem | FALSE_POSITIVE |
| C6 | Bertolini–Darmon, Invent. 168 (2007) Thm 1 PT | d²/dk² L_p(f_∞;k,k/2)\|_{k=2} = ℓ·log_E(P)², ℓ ∈ Q^×; P of infinite order ⇔ L′(E,1) ≠ 0 | Q, p ∥ N, **weight direction**, sign −1 | rank **one** | no: w = +1, where L_p(f_∞;k,k/2) vanishes identically | none | published | FALSE_POSITIVE (p-adic, weight variable, rank 1) |
| C7 | Stein–Wuthrich, Math. Comp. 82 (2013) Thm 6.1 + Kato PT | ord_p of the leading term of the characteristic series = ord_p(ε_p·∏c_v·#Sha(p)·Reg_γ/#tors²) when the p-adic height is non-degenerate and Sha(p) finite; with Kato gives upper bounds for #Sha(p) | Q, p-adic | any rank | yes at good ordinary / multiplicative p (this is how Sha[5^∞] = 0 was obtained) | none: compares the p-adic analytic side with the **algebraic** side; the complex L″ is never compared | published | not a route to q (algebraic side only) |
| C8 | Büyükboduk–Pollack–Sasaki (arXiv 1811.08216) Thms 1.1.4, 1.1.5 PT; Perrin-Riou; Kobayashi; Bertolini–Darmon–Venerucci; Venerucci (AB) | Perrin-Riou's conjecture and the p-adic Beilinson formula in analytic rank **one**; the bridge to the complex side is the complex Gross–Zagier formula | Q | rank 1 | no | none. Shows *why* (D) works for r = 1: one Heegner point feeds both the complex and the p-adic formula. No such object is known for r = 2 | published | FALSE_POSITIVE (rank 1) |
| C9 | Banwait, arXiv 2609.08431 (8 Sep 2026) Thms A, B PT (read by agents C, E and by me) | normalised second Taylor coefficient of the MTT **p-adic** L-function is a unit ⇔ Reg_γ unit and Sha[p^∞] = 0; "the analytic rank itself, that is L″(E,1) ≠ 0, is not assumed" | Q, **CM** only, p split | p-adic order 2 | no (seed non-CM; §16: "Nothing in §§3–6 survives the removal of complex multiplication") | none | preprint | FALSE_POSITIVE (p-adic second derivative; CM) |
| C10 | Castella, arXiv 2204.09608v3 (CM rank 2) Thms B, C PT; Castella–Sano arXiv 2601.14504 Thms A, B PT; Castella arXiv 2312.01481 AB; Gatti–Guitart–Masdeu–Rotger, Gatti–Rotger, Rivero, Darmon–Rotger 2207.01310 AB | Selmer-dimension and Kurihara-number statements; rank 0 or first-derivative p-adic formulas | p-adic | — | — | none | preprints / published | FALSE_POSITIVE / IRRELEVANT |

Answer to the class-(D) key question (agent C, confirmed by CP-1): the statement
"(1−1/α)⁻¹(1−1/β)·L_p^{(r)} = [L^{(r)}(E,1)/(Ω⁺R_∞)]·R_p" is a **theorem only for r = 1** (Perrin-Riou ordinary,
Kobayashi supersingular; BKS24 Remark 6.8) and for r = 0 with an exceptional zero (Greenberg–Stevens). For r = 2 it is
a consequence of an open conjecture. No theorem in this cluster contains the value of the complex L″(E,1).

New dated open-status sentence (re-read by me): Banwait, arXiv 2609.08431v1, 8 Sep 2026, §13:
"**No construction is known that attaches an algebraic number to L″(E,1).**" Same paragraph: "the plectic points of
Fornea–Gehrmann [21, §1] are conjectural and degenerate to rank one over Q."

## CP-5. Candidate ledger, part 3 — cluster B folded in (18:43 PDT)

### B. Kudla programme; arithmetic Siegel–Weil; Li–Zhang; Chen; arithmetic inner product; arithmetic GGP (agent file `F4_work/agents/B_kudla_program.md`, 18 primary-text blocks)

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| B1 | Kudla–Rapoport–Yang, Ann. Math. Studies 161 (2006): Thm 1.0.6, Cor. 1.0.7, Thm 1.0.9 PT | ⟨θ̂(f),θ̂(f)⟩ = C(0)·L′(1,F)·⟨f,f⟩; ⟨Z(t₁)(F),Z(t₂)(F)⟩ = C(0)·L′(1,F)·a_{t₁}(f)a_{t₂}(f)/⟨f,f⟩ ("the analogue … of Gross–Kohnen–Zagier, Theorem C") | Q | **first** derivative, ε(1,F) = −1 | no: w = +1; level must be a square-free D(B); ord = 2 | none: θ̂(f) = 0 when L′(1,F) = 0. Agent's inference (not a quote): Thm 1.0.6 is an identity in s, but for ε = +1 some C_p vanishes doubly at s = 0, so its second s-derivative is again 0 = 0 | published | FALSE_POSITIVE (first derivative) |
| B2 | Kudla, "Special cycles and derivatives of Eisenstein series" (2003) PT; Bruinier–Zuffetti lecture notes arXiv 2607.06285 (Jul 2026) PT | arithmetic generating series = **central derivative of an incoherent Siegel Eisenstein series**; incoherence forces an odd functional equation | Q | first derivative **of Eisenstein series** | — | none (no L(E,s) statement at all) | conj. / partly proved | FALSE_POSITIVE (Eisenstein derivatives) |
| B3 | Li–Zhang, JAMS 35 (2022) (Kudla–Rapoport conjecture) PT; Li–Zhang, Invent. (GSpin) arXiv 2106.15038 PT; R. Chen, co-rank 1 arithmetic Siegel–Weil I (arXiv 2405.01426) PT, II–IV AB; Y. Luo arXiv 2504.18528 PT | arithmetic intersection numbers of special cycles = **derivatives of local densities / Fourier coefficients of Eisenstein series**; Faltings heights | number fields (unitary F/F₀, GSpin over Q) | first derivative of Eisenstein series | — | none: these are not L(E,s) | published / preprints | FALSE_POSITIVE (Eisenstein derivatives; first order) |
| B4 | Li–Liu, Annals 194 (2021) and Forum Pi (2022); C. Li survey arXiv 2402.12159v2 (PSPM 112.3, 2025) Thm 4.5.2, Thm 4.5.4 PT | arithmetic inner product formula ⟨Θ_{φ₁},Θ_{φ₂}⟩_X = L′(1/2,π)/b_{2n}(0)·∏Z_v; ord_{s=1/2}L(s,π) = 1 ⇒ rank CH^n(X)⁰_{m_π} ≥ 1 | unitary groups, **F₀ ≠ Q**, ε(π) = −1 required | first derivative; analytic rank 1 | no (ε = +1; F₀ ≠ Q; GL₂/Q is not in scope) | none: for ε = +1 the coherent Rallis formula reads 0 = 0 at L(1/2,π) = 0; the survey's Table 2 has no row for L″ | published | FALSE_POSITIVE (first derivative) |
| B5 | Arithmetic GGP: W. Zhang AFL (arXiv 1909.02697) PT; W. Zhang survey (2024) PT; Disegni–W. Zhang arXiv 2410.08401v2 (Mar 2026) PT; Disegni–Liu arXiv 2204.09239 PT | first central derivative of Rankin–Selberg L-functions ↔ heights of GGP cycles; p-adic versions relate the first derivative of a **p-adic** L-function to p-adic heights | unitary groups, F₀ ≠ Q | first derivative | no | none | published / preprints / conj. | FALSE_POSITIVE (first derivative; p-adic without complex comparison) |
| B6 | Liu–Tian–Xiao–Zhang–Zhu, Invent. (2022), arXiv 1912.11942 PT (pp. 1–12) | Beilinson–Bloch–Kato for Rankin–Selberg motives: Selmer rank 0 when L ≠ 0, rank 1 under a non-vanishing cycle-class hypothesis | number fields | rank 0/1 | no | none (Selmer bounds, not L-value formulas) | published | FALSE_POSITIVE (rank 0/1) |
| B7 | Feng–Yun–Zhang, higher Siegel–Weil (Invent. 2024; arXiv 2103.11514) PT; Feng–Howard–Mkrtchyan II (arXiv 2507.13473) PT; Feng–Yun–Zhang, "Modularity of higher theta series III" (arXiv 2608.07173v2) PT | r-th derivative of Siegel Eisenstein series ↔ special cycles on Hermitian shtukas with r legs; "higher arithmetic inner product formula" | **function field** | any r | no | none | published / preprints | FALSE_POSITIVE (function field **and** Eisenstein derivatives) |

Two dated expert statements, both re-read by me in the agent's downloaded texts:
- Chao Li, "Geometric and arithmetic theta correspondences", arXiv 2402.12159v2 (8 Mar 2025; PSPM 112.3), Remark 4.4.4
  (txt l. 1072–1077; pdf sha256 `7cded393…`): "**Over number fields, however, no analogue of such a higher Siegel–Weil
  formula is currently known when r > 1.**"
- Feng–Yun–Zhang, arXiv 2608.07173v2 (v2 16 Sep 2026 per arXiv listing; pdf sha256 `86de9426…`), §1.1: "While the r = 0
  and r = 1 cases of this story have parallels over number fields, **the existence of a story for higher derivatives is
  a distinctive feature of the function field setting.**" These are the authors of the higher Gross–Zagier formula,
  writing two days before this audit.

## CP-6. Session resumed after the usage cap; ledger part 4 — YZZ and the plectic circle (20:54 PDT)

Process note. The cap hit at ≈ 18:44 PDT and killed all five search agents **before any of them wrote a `## VERDICT`
section**. Their append-only notes survived (A 348 lines, B 382, C 187, D 171, E 188). I did not relaunch them: the
remaining work is folded and finished by me below, one checkpoint per step. Agent blocks are quoted with their own
line references into the downloaded texts in `F4_work/sources/{A..E}/`.

### A (continued). Yuan–Zhang–Zhang; plectic constructions (agent file `A_higher_GZ.md` S18–S23)

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| A10 | Yuan–Zhang–Zhang, "Triple product L-series and Gross–Kudla–Schoen cycles" (version 14 Nov 2023) Conj. 1.3.1, Thm 1.3.3 PT | ⟨P_L(f),P_L(f̃)⟩ = (16ζ_F(2)²/L(1,π_L,ad))·L′(1/2,π_L)·α(f,f̃), up to Σ c_p log p in general; exact when π is unramified | totally real F | **first** derivative of the degree-8 triple product, sign −1 | no | none: L(s,E×E×E) = L(Sym³E,s)·L(E,s−1)² has central order ≥ 4 for the seed, so L′ = 0 | preprint (long-running) | FALSE_POSITIVE (first derivative; other L-function) |
| A11 | YZZ, "The Gross–Zagier formula on Shimura curves" (Ann. Math. Studies 184, 2013) — **not open-access, NOT READ**; known through secondary quotes (Kim 2024: "when the rank is at most one") | L′(1/2,π,χ) ↔ height of a CM point | totally real F | first derivative | no | none (0 = 0 at order 2) | published | FALSE_POSITIVE (first derivative) — **UNVERIFIED at primary level** |
| A12 | YZZ, "The Gross–Kohnen–Zagier theorem over totally real fields" (Compositio 145, 2009) AB; S. Zhang, "Gross–Schoen cycles and dualising sheaves" (Invent. 179, 2010) Conj. 1.5.1 PT | modularity of Kudla's generating series; Beilinson–Bloch conjecture restated | totally real F | — | — | none (no derivative formula / conjecture only) | published | IRRELEVANT |
| A13 | Nekovář–Scholl, "Introduction to plectic cohomology" (Contemp. Math. 664, 2016) §12, §17, Questions 18.1–18.2 PT | "formulae for leading terms of L-functions at points where they have a derivative of order r": this is L^{(r)}(f,0) for Hilbert forms over F of degree r — **s = 0, non-central**, zero forced by Γ-factors, conditional on plectic Conj. 6.1; the central case is Question 18.2 (order a ≤ r = [F:Q]) | totally real F, [F:Q] = r > 1 | r-th derivative, conjectural | no: for F = Q, r = 1 | none | conjectural / speculative | FALSE_POSITIVE (conjectural; non-central; base change) |
| A14 | Fornea–Gehrmann, "Plectic Stark–Heegner points" (Adv. Math. 2023; arXiv 2104.12575) Thm A = Thm 5.13, Conj. 1.3, 1.5 PT | 2^r·χ(d^r L^S_ε(A/E)_c) = d rec_S(Q^χ_A) in I^r/I^{r+1}: r-th derivative of an **anticyclotomic p-adic** L-function = p-adic plectic invariant (exceptional zeros from r inert multiplicative primes) | totally real F, p-adic | r = #S; over Q r ≤ 1 | no | none; the complex L^{(r)} is not involved | theorem is p-adic; algebraicity of points conjectural | FALSE_POSITIVE |
| A15 | Darmon–Fornea, "Mock plectic points" (arXiv 2310.16758) Thms 3.4, 3.8, 3.9; Conj. 3.12, 3.13 PT | invariants "expected to lie in the alternating square of the Mordell–Weil group of certain elliptic curves of rank two over Q"; theorems are p-adic (first derivative of L_p(E,K,s)); the rank-2 statements are conjectures; authors note the invariant "can sometimes vanish for trivial reasons (for example, when E(Q) has rank two)" | Q, p ∥ N inert in K, p-adic | Selmer rank 2 (conj.) | constructible at 3, 2243, 5843, but only a conjectural p-adic statement would result | none | preprint; conjectural | FALSE_POSITIVE (p-adic; conjectural) |
| A16 | Fornea–Gehrmann, "Iwasawa theory and mock plectic points" (arXiv 2311.03100v2, Dec 2024) Thm 1.3 PT | L(E/K,1) = 0 and Q_K ≠ 0 ⇒ r_p(E/K) = 2 | Q, p-adic | p-Selmer rank | — | none (Selmer-rank statement; "we do not yet know how to check the non-vanishing of Q_K numerically") | preprint | FALSE_POSITIVE |
| A17 | Fornea, "Plectic Heegner classes" (arXiv 2603.28327v2, Apr 2026) Conj. 1.9, 1.10 PT | κ^χ_{A,S} Selmer ⇔ r_an ≥ r; κ = det(w) for some w ∈ ∧^r A(L_c)^χ | totally real F, p-adic | conjectural | no | none: not even a conjecture relating the classes to the complex L^{(r)} | preprint | FALSE_POSITIVE |

Open-status sentences from this block (agent-quoted from primary text):
- Fornea–Gehrmann 2021/2023: "A long-standing open problem in the arithmetic of elliptic curves consists in discovering a
  modular construction of an element P ∈ ∧^r A(E) such that P is non-torsion exactly when the algebraic rank … equals r."
- Darmon–Fornea 2023 on Nekovář–Scholl: "At the moment, no precise numerical recipe is available to compute them, placing
  the conjectures of loc. cit. somewhat outside the scope of experimental verification."

## CP-7. Ledger part 5 — Beilinson for GL₂, p-adic Beilinson formulas, p-adic BSD formulations (20:55 PDT)

### C (continued) (agent file `C_padic_rank2.md` C-15 … C-18)

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| C11 | Beilinson's theorem for GL₂ as presented in Brunault's thesis (arXiv math/0602186) Thm 4 PT; Brunault, "Regulators of Siegel units" (arXiv 1504.08127) Thm 27 PT | L(f,2)·L(f,χ,1) = (Nπi/φ(N))·τ(χ)·⟨r_N{u_{ψχ},u_χ}, f⟩; m(x+1/x+y+1/y+12) = 2L′(E,0) | Q | **non-central** value L(f,2) ∼ L′(f,0) (simple zero forced by the Γ-factor); K₂-regulator, not a height regulator | — | none: the central point enters only as a critical *value* L(f,χ,1) chosen ≠ 0 | published | FALSE_POSITIVE (non-central) |
| C12 | Bertolini–Darmon, "Kato's Euler system and rational points on elliptic curves I: a p-adic Beilinson formula" (Israel J. Math. 199, 2014) PT (abstract + structure) | syntomic regulators of K-theory elements = values of the Mazur–Swinnerton-Dyer p-adic L-function at integers **≥ 2**; application: Perrin-Riou's rank-**one** conjecture | Q, p-adic | non-central; rank ≤ 1 | no | none. (Terminology clash: this "p-adic Beilinson formula" is not BKS's leading-term formula at s = 1.) | published | FALSE_POSITIVE |
| C13 | Perrin-Riou, Ann. Inst. Fourier 43 (1993) §3.3.4 "FORMULE (non démontrée)", §3.3.7 "CONJECTURE BSD(V)" PT (OCR) | p-adic BSD in rank r: r-th derivative of L_{p,MSD} = #Sha·Tam·(p-adic regulator)/…: stated with the **algebraic** BSD quantities | Q, p-adic | any r, **conjecture** | — | none: the complex L^{(r)}(E,1) does not appear for r ≥ 2 | conjectural | FALSE_POSITIVE |
| C14 | Disegni, "On the p-adic BSD conjecture for elliptic curves over number fields" (arXiv 1609.02528) Hyp. (BSD_∞), Conj. (BSD_p), Thms A, B PT | Conj. (BSD_p): d^{r̃}L_p(A,1) = ∏ẽ_p(1)·R̃(A)·**\|Sha(A)\|_an**·∏c_v, where \|Sha\|_an := L^{(r)}(A,1)/(r!·…·R_NT·Ω_A·∏c_v) and its rationality is **Hypothesis (BSD_∞)-2** | number fields, p-adic | conj. any r; **Thm A: r_an ≤ 1** | no (r_an = 2) | none: the comparison with the complex leading term *presupposes* rationality instead of proving it | published theorems are r_an ≤ 1 | FALSE_POSITIVE |

Reading of C14 that matters for class (D): wherever the literature writes a p-adic leading-term formula with the complex
L^{(r)}(E,1) on the right-hand side for r ≥ 2 (Disegni 2016; BKS 2024), rationality of L^{(r)}(E,1)/(Ω·R) is either a
hypothesis of the formulation or a consequence of the conjecture — never an output of a theorem. Disegni, 8 Sep 2016
(l. 302–306): "The results are of course concentrated in the cases where something is known for the classical conjecture
(BSD_∞), namely … the archimedean analytic rank is at most 1."

## CP-8. Ledger part 6 — Mazur–Tate (Ota), higher-rank Euler systems, periods, ETNC survey, databases (20:55 PDT)

### D (continued) (agent file `D_refined_bsd.md` D10–D18). Database, Sage and Kontsevich quotes re-read by me in `F4_work/sources/D/`.

| # | candidate | what it says | domain | order | seed satisfies? | implication for q | status | grade |
|---|---|---|---|---|---|---|---|---|
| D7 | Ota, "Kato's Euler system and the Mazur–Tate refined conjecture of BSD type" (arXiv 1509.00682; AJM 2018) Thm 1.2 PT | θ_S ∈ I_S^{r_E} — the **rank part** of Mazur–Tate, unconditional ("does not require the validity of any conjecture") | Q | any rank | yes, plausibly | none: an order-of-vanishing statement for elements that interpolate twisted *values*; the leading-term part is not addressed; no L″ | published | IRRELEVANT to q |
| D8 | Burns–Sakamoto–Sano III (arXiv 1902.07002) Thm 6.11, 6.14 PT; I, II, IV AB | Fitting-ideal equalities and TNC, **if** BSD_p(E/Q) holds and Perrin-Riou's conjecture holds; (iii): e_χ z^Kato ≠ 0 ⇔ rk_χ ≤ 1 | Q / abelian F | rk_χ ≤ 1 for formulas | no | none. Shows why BKS needed a *conjectural* derivative formalism: Kato's element itself dies in rank ≥ 2 | published | FALSE_POSITIVE (assumes BSD_p) |
| D9 | Sakamoto (arXiv 2106.03370) AB; Kim–Kurihara (IMRN 2021), Kurihara (2014) — **not read in primary text** | Selmer structure / Fitting ideals from modular symbols (Kurihara numbers) | Q, p-adic | any | — | none (algebraic side) | published | IRRELEVANT; UNVERIFIED at primary level |
| D10 | Flach, "The equivariant Tamagawa number conjecture: a survey" (Contemp. Math. 358, 2004) Conj. 2, §5.4 PT | Rationality is **Conjecture 2** (Deligne critical case / Beilinson general case); proved ETNC cases for elliptic curves: CM with rank 0 (Colwell), CM non-central j ≥ 2 (Kings) | number fields | — | — | none | survey | OPEN-STATUS witness: "progress … in the case ord_{s=1}L(E,s) ≤ 1 (but none for higher vanishing order)" |
| D11 | Kontsevich–Zagier "Periods" (2001) §3.5 Problem 4 PT; Kontsevich, "Periods" short text (6 Oct 2006) §7 PT (re-read by me, l. 363–384); Van Order arXiv 2510.10303v2 Cor. 7.9 PT | Ω·R is a period (theorem); L^{(r)}(f,k/2) ∈ 𝒫̂ is a theorem for r ≤ 1 and **Problem 4** for r ≥ 2; Van Order proves Λ′(E/k,1) ∈ 𝒫 (first derivative) and restates the r ≥ 2 case as a conjecture | Q | r ≥ 2 open | — | none. Doubly open as a route: (i) L″(E,1) is not known to be a period; (ii) equality of two periods has no decision procedure | problem | NOT A ROUTE (same as A8) |

**Reference implementations and databases (all re-read by me in the saved pages):**
- LMFDB knowl `ec.analytic_sha_order` (reviewed; last edited by J. Cremona 2024-03-08): "For curves of rank 2 and above,
  **there is no such theorem**, and the values computed are floating point approximate values which are very close to
  integers. In the LMFDB we store and display the rounded values in this case."
- LMFDB knowl `ec.q.analytic_sha_value`: "For curves of rank at least 2 **it is not known to be rational** …"
- LMFDB knowl `rcs.rigor.ec.q`: "For curves of rank greater than 1, the quantity predicted by the BSD conjecture to be the
  order of Ш **is not even known to be rational** and can only be computed as a floating point approximation."
- SageMath `sha_tate.py`, `an()`: "…as a provably correct integer, unless the analytic rank is > 1, in which case this
  function returns a numerical value."
- Kontsevich, "Periods" (2006) §7: "In the case r ≥ 2 …, there is no example in which we can prove the identity predicted
  by the BSD conjecture. The problem is that the natural integral representation for higher derivatives
  (d/ds)^r L(s)|_{s=1} can not be reduced using all tricks known today to an integral of an algebraic function. It is a
  great challenge for number theorists to pass the barrier r ≤ 1."

## CP-9. Ledger part 7 — the 2024–2026 sweep and the seed's special structure (20:57 PDT)

### E1. Dated sweep (agent file `E_sweep_special.md`: 27 arXiv-API queries q01–q27, 2024-01 … 2026-09, raw XML in `sources/E/`; completed by me with a 45-paper abstract batch, QUERY_LOG W13)

Queries covered: "rank two" / "rank 2" (92 math.NT hits), "second derivative", "higher derivative(s)", "leading
term/coefficient", "analytic rank two", "Gross-Zagier" (29), Tate–Shafarevich + rank two, "Swinnerton-Dyer" (58), "order of
vanishing", "Beilinson–Bloch", "height pairing(s)", "Bloch–Kato" (45), "Tamagawa number conjecture", Zywina, "Mahler
measure", Heegner (55), Kolyvagin (26), plectic (59), Kato classes / zeta elements, "p-adic L-function" + derivative,
"Mazur–Tate", derived heights, regulator + L-value, "central derivative(s)".

| # | item | content | grade |
|---|---|---|---|
| E1 | Banwait 2609.08431 (8 Sep 2026) PT | see C9 | FALSE_POSITIVE (p-adic, CM) |
| E2 | C.-H. Kim 2609.15328 (14 Sep 2026) PT | criterion for finiteness of Sha[p^∞] in Selmer corank ≥ 2 via derived Heegner points; no complex leading term | IRRELEVANT to q |
| E3 | Castella–Sano 2601.14504 (Jan 2026) PT | Kurihara numbers ↔ IMC; ord_p #(Sel/div) from modular symbols | algebraic side only |
| E4 | Wei–Zhai 2605.09251 (May 2026) PT (intro + Thm 1.1) | non-vanishing of Taylor coefficients in quadratic-twist families under GRH | FALSE_POSITIVE (analytic; no arithmetic content) |
| E5 | Burungale–Skinner–Tian–Wan 2409.01350v2 PT (abstract + intro) | zeta elements; BSD applications for semistable curves | FALSE_POSITIVE (rank 0/1) |
| E6 | Sweeting 2503.19226v2; Loeffler–Zerbes 2110.13102v3; Y. Liu 1511.08176 PT (abstract + statements) | Bloch–Kato / BSD for other motives | FALSE_POSITIVE (rank 0/1; Selmer bounds) |
| E7 | Van Order 2510.10303, 2510.10277; Du 2412.00688; Du–Peng 2603.15795; Lilienfeldt–Shnidman 2408.04375; Howard 2609.13435 (AB except Van Order Cor. 7.9 PT) | "central derivative(s)" = **first** derivatives; arithmetic Siegel–Weil for the spherical Hecke algebra | FALSE_POSITIVE (first derivative / Eisenstein) |
| E8 | Bullach–Honnor 2511.07203 (Nov 2025) AB; Llerena-Córdova 2412.17703 AB; Kim–Pollack 2505.09121 AB; Macias Castillo–Sano 2603.23978 AB; Bullach–Burns 2509.13894 AB | Mazur–Tate conjectures proved in "substantial part" via the **rank-zero component** of eTNC; numerical study finds discrepancies in some original MT statements; refined Selmer formulas via Kolyvagin derivatives "insensitive to … analytic rank"; derived p-adic heights | algebraic / p-adic side; by D2 the MT leading term does not contain L″. AB only — not load-bearing |
| E9 | Banerjee 2509.24645 AB; H. Li 2608.11969 AB; Barrios–Mok 2510.00926 AB; Gunri–Jha–Majumdar 2607.26774 AB; Burungale–Tian 2609.14893 AB | results "provided that the BSD is known", or in analytic rank ≤ 1 | FALSE_POSITIVE (assume BSD / rank ≤ 1) |
| E10 | Balakrishnan–Çiperiani–Mazur–Rubin 2409.00891 AB | shadow lines for Mordell–Weil rank 2, anticyclotomic, "subject to the Shafarevich–Tate conjecture" | p-adic; conjectural; no L″ |
| E11 | Braunling 2510.10816 AB ("Without real vector spaces all regulators are rational") | determinant functors on LCA groups | title-only hit; IRRELEVANT |
| E12 | Feng–Yun–Zhang 2601.18557; Z. Wang 2509.05526; FHM 2507.13473 | shtukas | FALSE_POSITIVE (function field) |

Result of the sweep: **no 2024–2026 preprint found whose abstract or (where read) text asserts a complex leading-term
identity, rationality, or denominator bound for a central zero of order ≥ 2 of a primitive GL₂ L-function over a number
field.** Limits: the arXiv API matches title/abstract tokens only; 29 of the 45 follow-ups were read at abstract level.

### E2. The seed's special structure (class E of the brief)

| # | structure | what exists | grade |
|---|---|---|---|
| S1 | rational 2-isogeny E → E′ | Cassels (1965): the BSD quotient is isogeny-invariant (assuming finite Sha); L(E,s) = L(E′,s). Lane 3 already has C′ = C and Sha(E′) ≅ Sha(E). This transports the *conjecture*, it supplies no formula | nothing new |
| S2 | Zywina's family, arXiv 2502.01957 (read in full by agent E, PT): Thm 1.2 gives E(Q) ≅ Z/2 × Z² by 2-isogeny descent; the seed's equation was re-derived from (m,n) = (2243,12) | **no L-function content at all** (grep: only root number / parity remarks, l. 87–102). None of the 8 papers citing it (Semantic Scholar list, abstracts) makes an analytic statement | NOT FOUND in the primary text |
| S3 | curves y² = x(x² + ax + b); conductor 2³·3·2243·4547²·5843 with additive, potentially supersingular reduction at 4547 (j ≡ 1728) | Tunnell/Waldspurger-type formulas are for central *values* (rank 0); no derivative formula attached to this shape found. The non-semistable conductor *excludes* the seed from several theorems (KRY square-free level; Yun–Zhang II square-free level — function field anyway; BSTW semistable) but nothing of order 2 exists to be excluded from | nothing found |
| S4 | exact formulas for L″(E,1) itself | Mellin/Rankin–Selberg representations (Goldfeld, Diamantis) are integrals with no arithmetic comparison (A9). Mahler-measure and K₂ results concern L(E,2) ∼ L′(E,0) and, over totally real F of degree n, L^{(n)}(E/F,0) = rational × n×n determinant of Mahler measures for CM curves (Samart–Tao 2409.14714, AB) — **non-central** zeros forced by Γ-factors. Kontsevich 2006: the integral for (∂/∂s)^r L(s)\|_{s=1} "can not be reduced using all tricks known today to an integral of an algebraic function" | FALSE_POSITIVE (non-central) / none |
| S5 | Bloch–Kato / Tamagawa number conjecture for a rank-2 motive over Q | Flach's survey: progress only for ord ≤ 1 "(but none for higher vanishing order)"; nothing newer found in the sweep (Sano 2510.01601, Diamond–Flach–Guo 2512.02348 concern other motives / adjoint) | none found |
| S6 | Buhler–Gross–Zagier, Math. Comp. 44 (1985), rank-3 curve 5077a | Gross–Zagier proves L′(E,1) = 0 exactly, hence a triple zero; L‴(E,1)/3! agrees with Ω·R to 28 decimals — **numerical agreement only**, forty years ago and still the template (K–Z 2001; LMFDB 2024) | illustration of what GZ can and cannot do |

Analogy kept on record (QUERY_LOG W9–W11): leading-term theorems of order ≥ 2 **do** exist over number fields — Stark's
conjecture for rational characters (Tate), Borel's theorem for ζ_F at s = 1 − m, Samart–Tao's determinants of Mahler
measures — but each is at a non-central point, where the zero is forced by Γ-factors and the regulator lives in units
or K-theory, and each is proved through a class-number-formula-type identity. For a central zero of L(E,s) the
corresponding identity is BSD itself.

## CP-10. Ledger part 8 — Beilinson–Flach proper and Bertolini–Darmon derived heights (20:58 PDT; abstracts only — agent C was cut off before reaching them)

| # | candidate | what it says | domain | order | implication for q | grade |
|---|---|---|---|---|---|---|
| C15 | Kings–Loeffler–Zerbes, "Rankin–Eisenstein classes and explicit reciprocity laws" (arXiv 1503.02888) AB; Bertolini–Darmon–Rotger, Beilinson–Flach I/II (known to me from Darmon–Rotger JAMS Thm A, PT in C2) | explicit reciprocity law to **critical values**; finiteness of Selmer for E twisted by an odd 2-dim Artin ρ when L(E,ρ,1) ≠ 0 | number field, p-adic | **rank 0** (twisted) | none | FALSE_POSITIVE (rank 0) |
| C16 | Rivero–Rotger, "Derived Beilinson–Flach elements and the arithmetic of the adjoint of a modular form" (arXiv 1806.10022) AB; Rivero 2103.00990 AB | derived classes at weights (1,1,0) ↔ units and p-units; 𝓛-invariant of the adjoint | p-adic | — | none (not L(E,s)) | FALSE_POSITIVE |
| C17 | Bertolini–Darmon, "Derived heights and generalized Mazur–Tate regulators" (Duke 1994), "Derived p-adic heights" (AJM 1995) — **not on arXiv, NOT READ**; Howard, "Derived p-adic heights and p-adic L-functions" (arXiv 1202.6343) AB; used in Castella–Hsieh Cor. 5.1 (PT, C1) | derived heights ↔ higher derivatives of **p-adic** (anticyclotomic / cohomologically defined) L-functions | p-adic, algebraic | any | none: no complex L-function in the statements | FALSE_POSITIVE (p-adic) — BD 1994/95 UNVERIFIED at primary level |

---

# FINAL VERDICT (21:00 PDT, 2026-09-18) — supersedes CP-2

## RETURN: **NOT_FOUND**

Not found in the sources checked (listed in CP-3 … CP-10 and in `F4_work/QUERY_LOG.md` + `F4_work/agents/*.md`). This is
a statement about the literature searched, **not** a statement of impossibility.

| target class | result | closest thing in print | why it does not count |
|---|---|---|---|
| (A) rationality / algebraicity of L″(E,1)/(Ω·Reg) | NOT_FOUND | BKS24 Conj. 1.6 would imply it at one p (my remark, CP-1); Disegni's (BSD_∞)-2 *assumes* it; K–Z Problem 4 asks only for "period" | conjecture / hypothesis / problem. LMFDB (reviewed 2024): "For curves of rank 2 and above, there is no such theorem" |
| (B) explicit denominator bound | NOT_FOUND | none, not even conjecturally in isolation (it is BSD's integrality #Sha·∏c_p/#tors² ∈ (1/#tors²)Z) | — |
| (C) arithmetic-cycle formula | NOT_FOUND over number fields | Yun–Zhang II Cor. 1.4 has exactly the right shape (r-th derivative of a single L(π,s)) — over **function fields**; every number-field formula (GZ, GKZ, YZZ, KRY, Li–Liu AIPF, AGGP) is a **first** derivative and needs root number −1 | function field / first derivative (reads 0 = 0 on the seed). Feng–Yun–Zhang, 16 Sep 2026: "the existence of a story for higher derivatives is a distinctive feature of the function field setting" |
| (D) p-adic comparison implying the complex identity | NOT_FOUND as a theorem | BKS24 Cor. 1.11 ("p-adic Beilinson formula") — proved for r = 1 (Perrin-Riou, Kobayashi), where one Heegner point feeds both the complex and the p-adic Gross–Zagier formula; conjectural for r = 2 | conjectural; Thm 1.14 also assumes finite Sha. Every rank-2 p-adic theorem found (Castella–Hsieh, Darmon–Rotger, BSV, Fornea–Gehrmann, Banwait, Stein–Wuthrich) compares p-adic objects with the algebraic side or with other p-adic objects; BSV Cor. B names the complex second derivative but in the (1,1)-factorised case |
| (E) special-case formula (2-isogeny, Zywina family, conductor) | NOT_FOUND | Cassels' isogeny invariance (transports the conjecture only) | Zywina's paper has no L-function content; nothing attaches a derivative formula to y² = x(x² + ax + b) |

**FOUND_CONDITIONAL_RATIONALITY: no.** Every conditional statement found is conditional on BSD itself, on finiteness of
Sha, or on an open conjecture that no finite computation can check (BKS Conj. 1.6 for r = 2 equates a transcendental-
looking complex number with a p-adic Euler-system derivative). These are the brief's own exclusions.

**FOUND_ALTERNATE_EXACT_ROUTE: no.** The only curve-by-curve route in print that avoids BSD/eTNC is Kontsevich–Zagier's:
(i) show L″(E,1) is a period (their Problem 4; stated as still open for r ≥ 2 by Diamantis–Rolen 2017 and restated as a
conjecture by Van Order 2026), then (ii) prove the resulting identity of periods by the elementary rules (their Conjecture
1 predicts this is possible and gives no algorithm). Both steps are open; Kontsevich (2006) explains why (i) fails with
"all tricks known today". It is a pointer, not a route.

## What the certified computation does prove today

With q := L″(E,1)/(2Ω_E·Reg(E)) and Lane 3's certified |q − 36| ≤ ε = 3·10⁻¹⁵ (not re-audited here):

> q = 36, **or** q is irrational, **or** q is a rational number whose denominator exceeds 1/ε ≈ 3.3·10¹⁴.

That trichotomy is rigorous. Nothing in the literature removes the second and third branches.

## Smallest missing theorem

**T★.** *An explicit integer D ≥ 1 with D·L″(E,1)/(Ω_E·Reg(E)) ∈ Z* — for the seed, or for a class containing it.
Any D < 1.6·10¹⁴ finishes SRAT at the present precision (2D·ε < 1), and a larger D only costs more certified digits.

The natural shape of such a theorem, by analogy with r = 1, is an **order-2 Gross–Zagier identity over Q**:

    L″(E,1) = c · Ω_E · det( ⟨z_i , z_j⟩ )_{i,j=1,2} ,   c ∈ Q^× explicit,  z₁ ∧ z₂ ∈ ∧²E(Q) constructed and computable,

after which q = (c/2)·[E(Q)/tors : ⟨z₁,z₂⟩]² has denominator dividing that of c/2. What is missing is the object
z₁ ∧ z₂ ("a modular construction of an element P ∈ ∧^r A(E)" — Fornea–Gehrmann call it "a long-standing open problem")
together with a complex-analytic formula for it. Over function fields the object exists (Heegner–Drinfeld cycles on
shtukas with two legs); over number fields there is no space for it to live on (Yun–Zhang 2017; W. Zhang 2018).

Strictly weaker statements do **not** suffice (§1): rationality alone; BKS Conj. 1.6 for r = 2 at one prime, or at
finitely many (gives q ∈ Q and ord_p q only); K–Z Problem 4; BSD_p at finitely many p. Strictly stronger than needed:
the full BSD formula.

## Mandatory search list — coverage

| topic (brief) | ledger rows | level | outcome |
|---|---|---|---|
| higher Gross–Zagier formulas | A1–A4 | PT (A1 re-read by me) | function field only |
| Gross–Kohnen–Zagier | A5, A6, B1 (KRY Thm 1.0.9 "analogue of GKZ") | PT | first derivative; dimension 0 when L′ = 0 |
| Yuan–Zhang–Zhang | A10 PT; A11 **not read (book)**; A12 AB | mixed | first derivative |
| Yun–Zhang + number-field follow-up | A1–A4, B7 | PT | no number-field follow-up exists; authors say so (2017, 2018, 2024, Sep 2026) |
| arithmetic Gan–Gross–Prasad | B5 | PT | first derivative, F₀ ≠ Q |
| Kudla–Rapoport–Yang | B1, B2 | PT | first derivative, ε = −1, square-free level |
| arithmetic Siegel–Weil | B2, B3, E7 (Howard 2026 AB) | PT | Eisenstein-series derivatives, first order; Li 2025: nothing known for r > 1 |
| Li–Zhang | B3 | PT | Eisenstein / local densities |
| Chen | B3 (I: PT; II–IV: AB) | mixed | Eisenstein, first order |
| Beilinson conjecture results for GL₂ | C11, C12; analogy W10–W11, S4 | PT / AB | non-central only |
| Beilinson–Flach / derived classes | C15–C17, C2 | AB (+PT for DR JAMS) | rank 0 twisted; p-adic |
| Bertolini–Darmon | C6 PT; C12 PT; C17 **BD 1994/95 not read** | mixed | p-adic; weight direction; rank 1 |
| Darmon–Rotger | C2, C3 | PT | p-adic "avatars", no comparison theorem; proved cases (1,1)-type |
| BSV | C4, C5 | PT | (1,1)-type; p-adic conjecture |
| Burns–Kurihara–Sano | D1 (re-read by me, published text), D2, D8 | PT | conjectural link; assumes finite Sha |
| ETNC / refined BSD | D3–D5, D10 | PT | equivalences with eTNC; rank-2 rationality numerical only |
| Mazur–Tate refined conjecture | D2, D7, E8 | PT / AB | the MT leading term is algebraic — contains no L″ even conjecturally |
| determinant / regulator rationality | D10 (Flach Conj. 2), A8/D11, W9–W11, S4, E11 | PT / search level | proved only at non-central points (Stark–Tate, Borel, Samart–Tao) |
| second-derivative algebraicity of automorphic L-functions | A8, A9, A13, D11, S4 | PT / AB | open at the centre; K–Z Problem 4 |
| p-adic Gross–Zagier of order 2 | A14, C1, C4–C6, C9, C17 | PT / AB | all p-adic ↔ p-adic or p-adic ↔ algebraic |
| 2025–2026 rank-two BSD papers | E1–E12, W12, W13 | PT for 10, AB for ≈ 35 | none claims a complex leading-term statement in order ≥ 2 |

## Findings against the audited files (labelled as the audit preamble asks; nothing was edited)

1. **COSMETIC — `NEXT_3_TARGETS.md` T3** says a denominator bound "D < about 10⁷" is needed with "36 ± 10⁻¹³". With Lane 3's
   certified ε = 3·10⁻¹⁵ any explicit D < 1.6·10¹⁴ (for L″/(ΩReg)) suffices. The target is easier to hit than stated —
   and equally absent.
2. **REPAIRABLE (wording) — `FULL_BSD_SEED_DAG.md` §G26**: "The Mazur–Tate refined conjecture (θ_n ∈ I² with a leading term
   in I²/I³) … is open for r = 2." The *rank part* θ_S ∈ I^{r} is a theorem (Ota, AJM 2018, Thm 1.2, unconditional under
   mild hypotheses on S — not checked for the seed here); only the leading-term part is open. More to the point, the MT
   leading term is L^alg·R_F with L^alg = #Sha·Tam/#tors² (BKS II Conj. 2.3): it lives on the **algebraic** side and could
   never deliver SRAT. It belongs under G23/G24, not G26. (Pointer for F2/F3, abstract only: Bullach–Honnor arXiv 2511.07203,
   Nov 2025, "prove a substantial part of conjectures of Mazur and Tate".)
3. **REPAIRABLE (wording) — same section / NEXT_3_TARGETS T3**: "Kudla-program arithmetic Siegel–Weil formulas concern
   Eisenstein-series derivatives, not L″(E,1)" is true but incomplete. The programme does have L-function theorems
   (KRY Cor. 1.0.7; Li–Liu arithmetic inner product formula); they are first-derivative, root-number −1 statements and
   read 0 = 0 on the seed. That is the accurate reason.
4. **COSMETIC — BKS numbering.** "BKS24 Cor. 1.11 / Thm 1.14" is the published numbering; arXiv v2 has Cor. 1.10 / Thm 1.13.
   The DAG's claim "Cor. 1.11 is conditional" is CORRECT.
5. **COSMETIC — my own §1.4** should read "for every auxiliary M(s) *holomorphic at s = 1*"; true of every case in the ledger.
6. **Process finding.** A WebSearch summariser fabricated a quotation ("rationality of L″(E,1) is [not] unconditionally
   known") out of a sentence about finiteness of Sha, and my own first grep missed the one sentence in the same paper that
   *is* about L″ (QUERY_LOG W1, W4). Both were caught only by reading the PDF text. No summariser output is cited anywhere
   in this file as a quotation.

Verdict on the audited labels (G26 = OPEN; Lane 3 C2(b) = OUT_OF_REACH): **PASS_WITH_CORRECTIONS.** The hostile hunt over 21
mandated topics — ≈ 90 full texts downloaded and text-extracted (89 per-source blocks in the agent files; not every text
was read end to end), ≈ 55 further items at abstract level, and a dated 2024–2026 sweep — found no
theorem, preprint or conditional result (outside the brief's exclusions) that touches L″(E,1)/(Ω·Reg) for a genuine
double zero.

## Limits of this hunt (UNVERIFIED items; none is load-bearing for NOT_FOUND, each is graded on secondary evidence)

- Not read (paywalled or not online): Yuan–Zhang–Zhang's book (Ann. Math. Studies 184); Bertolini–Darmon 1994 and 1995
  (derived heights); Goldfeld 1995; Diamantis 1999; Kurihara 2014; Kim–Kurihara 2021; Borcherds 1999; Jones 1989.
- Abstract only: Chen II–IV; Burns–Sakamoto–Sano I, II, IV; ≈ 35 of the sweep papers; all of CP-10; Van Order 2510.10277;
  Keller–Stoll; Borel / Kings / Stark (search-summary level, used only as analogies).
- All five search agents were killed by the usage cap before writing their own verdicts. Their notes are per-source and
  append-only, so nothing was lost, but no agent cross-checked another; the re-reads listed below are mine.
- Re-read by me in primary text: Yun–Zhang I §1; BKS24 (published) Cor. 1.11, Thm 1.14, l. 607; Banwait §1.1, §13, §14;
  C. Li Remark 4.4.4; Feng–Yun–Zhang III §1.1; LMFDB knowls ×3; Sage `sha_tate.py`; Kontsevich 2006 §7.
- Instruments: US web search and the arXiv API (title/abstract tokens). Journal-only, thesis and non-English literature
  is under-sampled. "Not found" means not found by these instruments.

**What would overturn NOT_FOUND:** a number-field space playing the role of shtukas with two legs, with its height pairing
compared to Néron–Tate; a proof of BKS Conj. 1.6 for r = 2 that is uniform in p; or K–Z Problem 4 for r = 2 together with
an explicit period identity for this curve. None was found, at any level of rigour, dated up to 2026-09-16.
