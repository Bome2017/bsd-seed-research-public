# c_2(p) witness package — STAGING NOTES. Not the package.

Date 2026-09-22. **Blocked on Codex's final replay report** (BLV<->BD module ID, BD 2.18/2.23/Lemma 3.1, odd-p Selmer
decomposition, full A_2 <= c argument, I_3(13) reconciliation). The package is built only after that report, since an
audit finding in the bridge would change the theorem statement and point 2 below. These two points do not depend on it.

## 1. Direct enumeration of the Gross set is infeasible — computation in general is NOT ruled out

phi_E lives on the definite Shimura set of the quaternion algebra ramified at N^- = 3·2243·5843 and infinity, Eichler
level N^+ = 2^3·4547^2. Eichler mass = (1/12)·26195528·248157072 = 5.42e14.

    DIRECT_GROSS_SET_ENUMERATION = INFEASIBLE

That is all the mass proves. It does **not** show that no compressed Brandt-module, Hecke-eigenspace, trace-formula,
quotient or congruence computation can reach the functional c_2(p). (An earlier draft said "no value of c_2(p) is
computable, not even at p = 5" — withdrawn: an impossibility claim resting on the failure of one method.)
Requirement for the package: **any proposed computational route must show how it avoids materializing the full
Shimura set.**

## 2. The bridge equivalence, and what it does and does not forbid

Once Codex validates the bridge (BLV equality, BD 2.23, Cor 2.24(1)):

    c_2(p) in Z_p^x   <=>   Sha(E/K)[p^inf] finite  and  #Sha(E/K)[p^inf] · R_der(p) in Z_p^x

(<=): R_der != 0 makes the second derived height nondegenerate, so sigma = rho_p = 4 by Cor 2.24(1); a unit leading
coefficient of Char_p transfers by BLV equality to L_p, whose leading coefficient is ±c_2(p)^2.

What this forbids is **tautology, not a category**. Proving the right-hand side with the same BLV/BD leading-term
machinery merely repackages the target. An algebraic route whose **decisive input is logically independent of that
bridge** — an independent integral-height calculation, a congruence theorem, an explicit Selmer construction — is
admissible. (An earlier draft said "the only non-circular route is analytic" — withdrawn: it constrained against
unforeseen mathematics rather than against tautologies.)

Caveat unchanged: the equivalence rests on exactly the bridge pieces Codex is auditing.

## 3. That analytic problem was already located this morning — beyond published theory

It is DIAGONAL_CROSS_PRIME_GROSS_POINT_NONVANISHING. Source check 2026-09-22 (see
~/BSD_OUTREACH_ASSESSMENT_2026-09-22/SOURCE_CHECK_AND_FRONTIER_UPDATE.md):

| | published (BHKO 2408.13932, BHTY 2508.19706) | needed here |
|---|---|---|
| automorphic input | self-dual Hecke character (CM) | non-CM phi_E |
| tower prime p | fixed | varies |
| reduction prime l | fixed (BHKO also treats l = p) | l = p |
| quantifier | all but finitely many characters | all but finitely many primes p |

The package carries this table so the run starts from it — **without** framing it as a prediction that the answer
is "published analytic nonvanishing is missing". The table shows the known mismatch; it must not predetermine the
search.

## 4. Package plan (after Codex)

READ_FIRST: ORDINARY_LANE_FREEZE.md; the section-2 equivalence; DIRECT_GROSS_SET_ENUMERATION = INFEASIBLE; the
section-3 mismatch table; Codex's replay report, each bridge piece marked source-replayed vs double-Aristotle-audited.

**Admissible route classes:**

| class | content |
|---|---|
| A. analytic / horizontal nonvanishing | Gross-point equidistribution, toric-period mod-p methods |
| B. algebraic, independent | congruences, integral heights, Euler/Kolyvagin input logically independent of the BLV/BD bridge |
| C. compressed computation | Brandt / Hecke quotient that provably avoids the 5.42e14 enumeration |
| D. impossibility / first missing theorem | exactly why A–C stop |

**Global prohibition:** no route may use a statement already equivalent to `c_2(p) in Z_p^x`.
**Also prohibited** unless an actual dependency error is found: twist-Sha, Manin constants, anomalous primes, A2a/A2b.

**Quantifier discipline** — the target is the family `c_2(p)`, p ordinary, not one number. Distinguish:
one prime / positive density of ordinary p / all but finitely many ordinary p / every admissible ordinary p. Only the
last closes the ordinary contribution to FIN outright; cofinite closes it modulo a finite-exception treatment;
positive density does not reach FIN at all.

**Verdicts:** `UNIFORM_C2_UNIT_PROVED` · `COFINITE_C2_UNIT_ONLY` · `POSITIVE_DENSITY_C2_UNIT_ONLY` ·
`FIXED_P_C2_UNIT_ONLY` · `COMPRESSED_COMPUTATION_ROUTE` · `FIRST_MISSING_THEOREM: <exact statement>` ·
`BRIDGE_DEPENDENCY_ERROR`.
(`POSITIVE_DENSITY` added to the proposed set: it is in the quantifier list, so a run proving it needs a verdict.)

**Kept OUT of the prompt:** my own expectation that the likeliest output is a first-missing-theorem verdict. That is
calibration for the user, not an input to the run — the same anchoring the blind/aware split was built to prevent.

NOT sent: the rest of the BSD corpus.

---
*Revised 2026-09-22 after external review:* §1 narrowed from "incomputable at any prime" to "direct enumeration
infeasible"; §2 narrowed from "only analytic routes are non-circular" to "no route through the same bridge"; §4 moved
from one question to four route classes, a global anti-tautology prohibition, quantifier levels and a verdict set.

---
**Withdrawn after external audit (rev 2):** §2's converse ("<=: R_der != 0 makes the second derived height
nondegenerate") is WRONG — R_der is the product over every filtration step, so R_der != 0 gives sigma = rho_p, not
rho_p = 4; a converse needs rho_p = 4 explicitly. Also every "conductor-p Gross points" here is wrong: BLV's layer K_n
uses traced Gross points of conductor p^{n+1}, so the first layer K_1 is conductor p^2. See INPUTS.md §2, §4.
