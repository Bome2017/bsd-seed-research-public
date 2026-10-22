# RESUME — MCS source-application check

STATUS: DONE. GOVERNING FILE: `RETRACTION_AND_CORRECTED_VERDICT.md`. RETURN: **NO_CHANGED_ARROW** (outcome unchanged;
three of the four stated reasons RETRACTED). `MCS_APPLICATION_VERDICT.md` is preserved unmodified as evidence, not as
mathematical authority. Stopping rule fired.

Do not return another reformulation of the same Selmer problem. No follow-up search, next-prime run, or formalization
is authorized by this operation.

Two things to carry forward:
1. RETRACTED. The Heegner-torsion argument is an INVALID inference: Theorem 3.9 uses the tower element y_infinity and
   produces a Lambda-basis (Remark 3.11), which stays a basis after specialization. A family can be nonzero while one
   specialization vanishes. The generalization to "every anticyclotomic Heegner construction" is withdrawn in full and
   must not enter the no-resurrection register.
   The REAL obstruction is Hypothesis 3.6(iii): N square-free, which the seed fails. Applicability, not impossibility.
2. CANONICAL THRESHOLD IS NOW **1521** (gcd(t,2310)=1), not 1089 — P11 proved Sha[11^inf]=0 on 2026-09-20.
   The 2026-09-20 Aristotle packet says 1089 and must not be reissued as-is.

## 2026-09-21 addendum — join audit
`JOIN_AUDIT_AND_NEXT_QUESTION.md`. The nonsquarefree join's structure is CONFIRMED: Hyp 3.6(iii) is consumed only to
import BCK21; Prop 3.7 and Lemma 3.8 do not use it; the other "square-free" hits are the auxiliary Kolyvagin index sets.
KaSa24 citation cleared. Residual-image argument checked. BCK Hypothesis (spade) deliberately not re-audited -- named as
the single inherited dependency.

Next question has a named object: the augmentation depth of y_infinity, measured by the derived p-adic heights of
MCS Sec 4 / Theorem 1.8 (BD filtration S_p^(k), values in Q_k = I^k/I^{k+1}, identified with Nekovar's).
Proposed refinement to K: also require ord L(E^K,1) = 1, so Kolyvagin pins rank E(K) = 3 and (J) has a determined
Mordell-Weil contribution; restriction then transfers a K-bound to Q for odd p.

## 2026-09-21 addendum 2 — derived-height proposal REFUTED, correction accepted
`DERIVED_HEIGHT_CORRECTION_ACCEPTED.md` supersedes section 5 of the join audit. Two errors: Q_k is the height's OUTPUT
not its input; and v_infinity still lifts through the tower, so it is a genuine cocycle (da = 0) and every derived
Bockstein kills it (MCS App. A.1). Dividing by t^e removes exactly what could have been seen. Scope: kills only that
proposal, NOT derived heights on other Selmer directions.

Target now named: Fitt^i(Sha(E/K)[p^n]^*) = I_{i+3}(eps^Hg_{n,0}) for a certified suitable K, and
I_3(eps^Hg_{1,0}) = F_p => Sha(E/Q)[p^inf] = 0. Remaining: certified twist + independent evaluation of the ideal.
No replacement mechanism proposed.

## 2026-09-21 addendum 3 — twist/ideal corrections accepted
`TWIST_IDEAL_CORRECTIONS_ACCEPTED.md` supersedes A.3/A.4/B.2 of the attempt.
- Cost was wrong by 18x AND wrong in kind: 8,444,396 = primes VERIFIED, not the cutoff; cutoff was 1.5e8, so D=-23
  needs 3.45e9. But C11 already extends to T = 39,141,244,927 (2333 segments of 2^24), so the needed 206 segments
  EXIST and are hash-verified, 11.3x headroom. No new coefficient production for the cheapest twist.
  Still open: twisted derivative, certified error bound, runtime, and whether 3.45e9 is an adequate cutoff.
- Coverage summary overreached (3rd instance of this pattern): correct scope is any FIXED FINITE collection leaves
  infinitely many primes uncovered; says nothing about K varying with p.
- "I_3 from the Heegner index" REFUTED by explicit counterexample; full Selmer-complex data matters.
