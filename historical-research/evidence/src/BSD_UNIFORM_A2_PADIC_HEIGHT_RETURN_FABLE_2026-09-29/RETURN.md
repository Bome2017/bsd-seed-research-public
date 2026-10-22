# RETURN — Lane A2: p-adic height nondegeneracy / L_p″ ≠ 0 for almost all p (Fable 5.1, 2026-09-29)

## STATUS: NO_SOURCE_FOR_THESE
Scoped to the sources listed below (theorem level vs secondary vs abstract kept separate). This records that
no theorem of type (a) or (b) was found in this bounded screen. It is not a claim that none exists.

## Kill test K-A2 (run first, after the collision check in NOTES.md §0)
Question: is there ANY unconditional theorem of type (a) or (b) for ANY non-CM curve of rank ≥ 2?
Answer: none found. The first failing condition for each candidate, quoted from source:

| file | source (grade) | first failing condition (verbatim / exact) |
|---|---|---|
| S08 | Schneider 1982, Invent. 69 (THEOREM, scan) | posed as open: "Problem. Is the bilinear form ... nondegenerate?" |
| S07 | Schneider 1985, Invent. 79 (THEOREM, scan) | a hypothesis: "Hypotheses (H): ... << , >>_κ is nondegenerate"; "any future proof of the nondegeneracy" |
| S01 | Mazur–Stein–Tate 2006 (THEOREM) | "Conjecture 1.1. The cyclotomic height pairing ( , )p is nondegenerate" |
| S10 | Perrin-Riou 1993, AIF 43 (THEOREM) | "3.3.7. CONJECTURE BSD(V) ... B) i) La forme ... est non dégénérée" |
| S05 | Stein–Wuthrich 2013 (THEOREM) | "Conjecture 4.1" and "Conjecture 4.4"; "Apart from ... [Ber82] ... complex multiplication of rank 1, there are hardly any results" |
| S02 | Balakrishnan–Müller–Stein 1210.2739 (THEOREM) | "this is not known in general" |
| S06 | Wuthrich 2004, JLMS 70 (THEOREM) | Thm 3: "Let p be an odd prime" (FIXED p; the curve varies) and "either constant 0 or ..."; almost-all-p appears only as Conjectures 1–2 |
| S04 | Burungale–Disegni 1803.09268 (THEOREM) | "Let B be a simple CM abelian variety"; root number −1; nondegeneracy "is not known in any cases of rank higher than 1" |
| S03 | Banwait 2609.08431 (PREPRINT, THEOREM) | "complex multiplication by the maximal order"; one split p per statement; §15: "In rank at least two no theorem gives the determinant nonzero at a single prime of a single curve" |
| S09 | Adachi–Katagiri–Shii 2609.35626 (PREPRINT, THEOREM) | conclusion is "either < , >_Nα or < , >_Nβ is non-trivial": non-triviality, not det ≠ 0, and not specified for the unit-root splitting |

Type (b) (L_p″ or ord-r coefficient ≠ 0 for all large p, rank ≥ 2): no statement was found in any screened
source, CM or non-CM. The only rank-2 L_p″ theorems (S03, Thm A/B) are CM, one split p at a time, and are
equivalences with (nondegenerate regulator with v_p = 0, and Sha[p^∞] = 0).

## Exact boundary of what is known (type (c)), as found
1. **Rank ≥ 2, any curve.** No theorem gives det⟨P_i,P_j⟩_p ≠ 0 even at one prime (S04 PUBLISHED 2020;
   S03 PREPRINT). Per-prime NUMERIC or computer-assisted nonvanishing exists: SW data; S03 Part 2; the
   project's p = 3, 5, 17; and checks/ here (good ordinary 5 ≤ p ≤ 47, PARI, not certified).
2. **CM, rank 1 (one point).** Bertrand: E CM, p ordinary, P ∈ E(Q) non-torsion ⇒ (P,P)_p ≠ 0.
   Primary text not obtained; verbatim attribution in S10 §3.4.4 (also S03, S04, S06). This is the only
   located theorem that holds at all ordinary p of a fixed curve, and its content is one height.
3. **CM abelian varieties, root number −1.** S04 Thm 1.1: non-vanishing for almost all anticyclotomic
   characters χ (isotypic pieces), not nondegeneracy.
4. **Non-CM, rank 1.**
   - Non-triviality of the unit-root cyclotomic height is open (S09 §1: "Even non-triviality ... remains
     open in general, including for elliptic curves over Q with good ordinary reduction at p").
   - At supersingular p, the D_p-valued height is nonzero (Bernardi–Perrin-Riou 1993; S04 fn 1, SECONDARY).
     By S05 Lemma 4.3 this is rank-1 content: in rank 2 it needs the fine regulator, which is Conj 4.4.
   - p-adic Gross–Zagier (Perrin-Riou; Kobayashi 2013) gives equivalences h_p ≠ 0 ⟺ L_p′ ≠ 0, not
     nonvanishing (S03 §14; SECONDARY).
   - Burungale–Skinner PAMS-B 2023: 3-adic nondegeneracy for a positive proportion of rank-1 twists, p = 3
     Eisenstein (ABSTRACT ONLY).
5. **"One of two splittings" at EVERY good p, any rank, non-CM.** S09 Cor 1.3 (PREPRINT), classical form
   S10 Rem. ii–iii: h_Nα(P) − h_Nβ(P) = c·log_E(P)², c ≠ 0. So for every non-torsion P, h_Nα(P) and
   h_Nβ(P) are not both 0. The hypotheses hold for the seed at every good p (S09 check). It does not give
   the unit-root pairing non-trivial at ordinary p, and it does not give det ≠ 0.
6. **Transcendence inputs.** None found beyond Bertrand. S03 §15: "One transcendence-theoretic result bears
   on the height pairing, and it is a rank-one result". No p-adic four/six-exponentials or Schanuel
   application to heights located (TRIAGE: searched, not exhaustive).
7. **HEURISTIC / CONJECTURE.**
   - Wuthrich Conj 1: h_p(P) ∈ p³Z_p for only finitely many p.
   - Wuthrich Conj 2: density-1 unit leading coefficient in rank r.
   - Schneider's Problem; MST Conj 1.1; SW Conj 4.1/4.4; PR 3.3.7.

## Bearing on rows F3-O3 and F4 (scoped; no necessity claims)
- **F3-O3** (R_p ≠ 0 for p outside a finite set): not supplied. The boundary above leaves it open even at a
  single prime as a theorem. The seed has per-prime numerics only (p = 3, 5, 17 on record; checks/ here).
- **F4** (ord L_{p,α} ≤ 2 at every non-Tate p): not supplied. At good ordinary p, S02 Thm 1.7 / S05 Thm 6.1
  (Schneider, Perrin-Riou) give: ord f_E = 2 ⟺ R_p ≠ 0 and Sha[p^∞] finite. With Kato (ord f_E ≤ ord L_p)
  and the IMC at the recorded grade, F4-at-p ⟺ (O3-at-p and finiteness of Sha[p^∞]). At supersingular p,
  S05 Thm 6.2 gives the same with the D_p-valued regulator (Conj 4.4 side). An independent analytic proof
  of L_p″ ≠ 0 would give both. None was found. Equivalence here is not circularity (B_CORRECTIONS 8).
- **REDUCED** is not claimed. No found theorem implies O3 or F4 from a named, narrower statement.
  - S06 Thm 3 varies the curve at fixed p.
  - S09 controls h_Nα − h_Nβ, not det of the unit-root pairing.
  - S03 Thm B is CM-only; its author states that nothing survives removing CM (S03 §16).

## What this changes
- H06 correction (scope): AKS Cor 1.3 is not limited to non-ordinary p. It applies at every good p of the
  seed, with conclusion "one of two splittings non-trivial". Only Cor 1.5 is non-ordinary. Still not
  applicable to O3/F4.
- Banwait 2609.08431 is upgraded from abstract level (LIT_SWEEP B1) to theorem level (S03).
- New to the record as screened, not applicable:
  - Wuthrich 2004 Thm 3;
  - Burungale–Disegni 2020;
  - Schneider I/II at source;
  - Perrin-Riou 1993 at source;
  - Burungale–Skinner 2023 (abstract only);
  - Kundu–Lei 2504.10761.
- Collision flagged: 1703.02215 is Destrempes–Malinin (DNR 18/44). It resurfaced in search; not used.
- Task-text note: the listed P₁, P₂ are coordinates on the MINIMAL model; they are not on the short model
  printed before them (PARI check in NOTES §2).

## Read-level ledger
- THEOREM level (full text, relevant sections): S01–S10.
- SECONDARY only (statement known through a quoted source): Bertrand 1982/84; Bernardi 1981;
  Bernardi–Perrin-Riou 1993; Kobayashi 2013; Büyükboduk–Pollack–Sasaki.
- ABSTRACT / TRIAGE only (UNCHECKED at theorem level): Burungale–Skinner PAMS-B 2023; Kundu–Lei (abstract
  and intro); 2311.01691; 2310.20678; 2001.00045; 2604.20662. See S11.
- arXiv ids checked on unsuffixed abs pages; none shows withdrawal:
  - 2609.35626 v1; 2609.08431 v1; 2504.10761 v1;
  - 1803.09268 v2; 1210.2739 v2; 2311.01691 v2; 1703.02215 v2; 2310.20678 v3; 2603.20886 v2.
- Searches: 11 web searches and about 11 arXiv API queries (abstract fields: "p-adic height"/"p-adic regulator"
  with non-degenerate / non-vanishing / Schneider / transcendence; rank-2 L_p order).

## Discipline
- Collision check first (NOTES §0). Web use: papers only.
- One process at a time: curl, pdftotext, and a single <1-min PARI run.
- No subagents, pushes, messages or paid compute.
- Writes only in this folder; downloads in the session scratchpad.

FIN, ORDER9 and Q36 are unchanged.
