# RETURN — Lane A1 (row F2): mod-p nonvanishing of depth-2 Mazur–Tate coefficients, uniformly in p (Opus 5.5, 2026-09-29)

## STATUS: NO_SOURCE_FOR_THESE
Scoped to the sources listed below: 17 read at theorem level, 1 via its author's survey, 1 partial, 17 triage rows.
None states a theorem meeting K-A1 (i) mod p AND (ii) uniform in p for the F2 object (order-p twists at the
trivial-character jet, depth 2). This records a bounded screen. It is not a claim that no such theorem exists.

## Exact boundary of what is known (among the sources read; quotes in SRC_*.md, verdicts in K_A1_TABLE.md)
1. Order-p twists of prime conductor l == 1 (mod p), mod p, all large p, E fixed: known at DEPTH 0 when L(E,1) != 0
   (FKK Thm 3.9, "for all but a finite number of primes l"), from the congruence L_alg(f,1,psi) ==
   (a_l - 2) L_alg(f,1) mod l-bar (Thm 3.5). For the seed, that congruence says exactly C0 == 0.
2. The same twists at depth r >= 1: known ONE p AT A TIME. Kriz–Nordentoft 2310.20678 Thm 1.4/Cor 5.20 give
   v_p(L(E,chi,1)/Omega) <= r/(p-1) (i.e. v_pi <= r) for many order-p chi of conductor l*q_1...q_r, from a nonzero
   length-r Kurihara number at that p. Their Cor 1.5 covers "100% of primes p" but concludes only L(E,chi,1) != 0,
   with r(p) not controlled. BCGS Thm C/Cor C (their input at ordinary p) fixes the order at a Z_p-corank r_str.
3. Uniform in p, mod p, E fixed: known for characters of order PRIME to p. These are quadratic twists (Ono–Skinner
   Cor 1), class-group characters with p ∤ h_K (Burungale–Hida–Tian Thm 1.1, about X(E/H_K)^chi), and l-power
   anticyclotomic characters with the reduction prime varying (Chida–Hsieh Thm D; Brakočević Thm 1.1).
   These concern twists or other isotypic parts, not Sha(E/Q)[p].
4. Character order = reduction prime at a FIXED p: mu = 0 (Ferrero–Washington, Vatsal 2003 via survey, Chida–Hsieh
   Thm C, Hamieh); residual equidistribution of single symbols (Lee–Sun Thm E; Constantinescu–Nordentoft Thm 1.1);
   per-p Kurihara criteria and moments (Kim–Kim–Sun; Kriz–Nordentoft 2507.01836).
5. Archimedean only: Petridis–Risager, Bettin–Drappeau, Nordentoft (x2), Chinta via Dasgupta–Khan; Mazur–Rubin (conj.).
Net: uniform in p at depth 0 in analytic rank 0 (FKK); at depth r one p at a time, given a per-p witness
(Kriz–Nordentoft); nothing found at depth 2, uniformly in p, for a curve with L(E,1) = 0.

## Why REDUCED is not returned
Reading Thms 3.7 + 3.9, FKK's uniformity comes from ONE nonzero rational, L_alg(E,1): excluded primes divide it, and
conductors come from a Chebotarev choice of l with a_l != 2. The depth-2 analogue of their Thm 3.5 would read
C2(p,l) == (a_l - 2) * iota(Z) * R_{p,l} (mod p), with one Sha-free rational Z != 0. That is row F1 / target T2
(B_PART3). It is already on record, together with its route to F2 via G2 (K288_UNIFORMITY_ANALYSIS §3(a)).
No source read gives a congruence of this type at depth >= 1, so the screen adds no new reduction.
Kriz–Nordentoft give v_pi <= 2 (at conductors l*q_1*q_2) from length-2 Kurihara witnesses. At good ordinary p such
a witness is already equivalent to Sha[p^inf] = 0 (FIN_FRONTIER, "Exact form of the open tail", flagged there for
referee): FIN-b support itself, not a statement sharper than F2 that reduces it.

## What was read
- THEOREM level (17): SRC_01-05, 07-12, 14-19 (16 arXiv items + Ono–Skinner, Annals 1998, from the author-hosted
  PDF). Survey level (1): SRC_06 (Vatsal 2003, via Vatsal's ICM survey). Partial (1): SRC_13 (K-A1 (i) only).
  TRIAGE, UNCHECKED, not exclusions (17 rows): SRC_20 (classical items seen only in restatements, plus 5 abstracts).
- arXiv: 25 abs pages opened without version suffix; latest versions noted; no withdrawal notice. Web: ~10 searches,
  arXiv API queries, author pages (Ono, Vatsal, Sun); no accounts or forms.

## What this changes
- Registers these sources as screened and not supplying F2. None appears in the inputs' screened lists.
- Records a published correction. Hamieh (Manuscripta 2014) says the inequalities in Vatsal 2003 were "mistakenly
  given as equalities". So Vatsal's ICM Thm 2.7 "=" should be read as a bound (SRC_06, SRC_08).
- WATCH: the Kriz–Nordentoft horizontal framework (2310.20678, 2507.01836) is the closest to F2. It has order-p
  twists with conductor prime to p, Kato–Kolyvagin derivatives, and augmentation rank. A successor giving
  single-prime depth-2 control, or bounding r(p) uniformly in p, would bear on F2 or FIN-b. The supersingular
  primes would stay separate (DNR 46).
- Authors' remarks (quotes, not project claims): Vatsal ICM Rem 2.10, "no general notion" of a derivative being
  nonzero mod p; Lee–Sun Rem 4.6, "no notable analogous progress" for modular L-values with Dirichlet twists.

## Discipline
Collision check first (NOTES.md §1): no overlap. K-A1 was run per candidate. Kill verdicts state only what the
cited statements say; no necessity or impossibility claims, no odds. At most 2 processes (sequential curl/pdftotext,
text greps). No subagents, paid compute, pushes or messages. Writes only here; downloads in the session scratchpad.

FIN, ORDER9 and Q36 are unchanged.
