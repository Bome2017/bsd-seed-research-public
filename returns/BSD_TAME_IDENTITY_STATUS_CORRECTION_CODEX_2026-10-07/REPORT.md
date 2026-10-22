# Tame identity, endpoint, and pending-check status correction

October 7, 2026. **RECORD_REFINEMENT_CORRECTED; NO_NEW_ARITHMETIC_RESULT.**

This checks the supplied refinement against the actual exactness report, stored residue table, retained G2/normalization statements, endpoint ledger, and RUN_NOW entries. It does not perform either pending independent audit or certify the antecedent mathematical chain. FIN, ORDER9 and Q36 are unchanged.

## 1. What the six-curve experiment supports

The six control constants are curve-dependent:

| Curve | Reported K_E |
|---|---:|
| 389a1 | 8 |
| 433a1 | 4 |
| 664a1 | 16 |
| 655a1 | 8 |
| 1615a1 | 16 |
| 194040co6 | 32 |

The experiment reports 104 clean depth rows modulo p^2 or p^3 and 275 defined odd-prime-power rows agreeing with C2 = K_E(a_ell-2)R. These counts describe overlapping sets, not 379 independent observations. They concern tested levels and defined regulator components of I^2/I^3. The 63 undefined-regulator rows do not test that equality.

**It did not establish the seed law with 288 on six curves.** The seed is absent from this panel; its higher-depth version is explicitly untested. The original report's §6 language about an integral per-level identity must be read as an inference/conjectural target from the tested rows, as qualified by its §7, not a theorem for all levels. Its references to seed Sha=9 are target/analytic-order language, not an established actual order.

This audit independently rechecks the displayed congruence from the stored C2 and R values. It does not recompute either producer. The co6 symbols include numerical identifications under a retained denominator bound; these are not upgraded to independently certified exact modular symbols. Precomputation seal chronology remains custodian-attested. The independent reimplementation remains pending.

See [source report](context/EXACTNESS_REPORT.md), [stored table](context/EXACTNESS_EVALUATION.json), and [check output](checks/RESULTS.json).

## 2. The proposed identity has a precise seed payoff

The proposed seed law is

    C2(p,ell) = 288 (a_ell-2) R_(p,ell) mod p,

in the retained source, period, and discrete-log conventions. Since 288=2^5*3^2, its reduction is a unit for p>=5. Retained G2 supplies, outside its stated finite set, auxiliary primes with residual Frobenius -I and R nonzero. Thus a_ell-2=-4 mod p is also nonzero. With the retained Ota hypotheses and matching, the law at such a prime implies Sha[p^infinity]=0.

The common conservative G2/W/tame-comparison domain in the current source is outside

    {2,3,5,19,59,487,2243,4547,5843},

with any additional source-normalization conditions retained. This is not an ordinary-only assertion in the retained record. The existence theorem does not provide a cheap auxiliary-prime search bound.

A FIN-free proof of this law would be an actual route through the infinite-prime obligation. Constructing a detector alone does not provide the law. Nor may 288 be introduced by assuming #Sha=9 or Q36. The six-curve table takes K_E from a formula using analytic Sha data; fitting that table is evidence, not a construction of the required seed scalar.

**Narrowest sufficient target:** for cofinitely many eligible p, prove the nonzero identity at a G2-detecting auxiliary ell. A theorem at every admissible ell is stronger and would suffice, but is not necessary for that implication. A different independently constructed fixed nonzero rational scalar also suffices for cofinite support after excluding its numerator and denominator primes. The value 288 is the specific predicted normalization.

See the retained [G2 statement](context/G2_PROOF.md) and [normalization and sufficient tame comparison](context/TAME_COMPARISON.md). Their imported/written-proof grades are preserved.

## 3. Identity priority is not an exclusion of estimates

It is reasonable to prioritize the exact tame identity as the current construction target. It is not correct to replace the missing arithmetic with the assertion that only an identity can work.

The supported derivative criterion remains: for the actual specified nonzero class, m_p-w_p<=1 implies primary vanishing, under its retained hypotheses. An independent cofinite estimate for that exact excess content would still solve the stated tail. No such estimate is supplied here. The source normalization document explicitly leaves that possibility open.

The present review does not verify a blanket character-sum obstruction. The tame construction itself uses ell different from p, with ell congruent to 1 modulo p. An obstruction stated for a particular character-sum problem at ell=p cannot by itself exclude all upper-bound mechanisms. The rank-one Gross-Zagier analogy supplies no rank-two comparison theorem here.

## 4. Endpoint ledger and supersingular scope

- **FIN:** after an appropriate cofinite theorem, the recorded outstanding named exceptions are 59, 487, 2243, 4547, and 5843. Additional exceptions introduced by the actual uniform theorem or source normalization must be retained until settled. Under the retained primary certificates, the smaller primes need no new work here.
- **Supersingular primes:** these are an infinite coverage issue, not another finite leftover. The recent cohomological content criterion includes them on its good-prime domain; some ordinary numerical comparisons do not. A matching tame law on the full retained G2/Ota domain would not require a separate supersingular construction merely because of supersingularity. None of these conditional statements proves their vanishing yet.
- **ORDER9:** given FIN and the retained small-primary results, actual vanishing at every p>=53 would suffice. Equivalently an independent support or size argument excluding #Sha>=9*53^2=25,281 would suffice; a separate computation at every such prime is not required.
- **Q36:** independent. The retained interval is 35.99427<q_E<36.00573. If q_E is rational with reduced denominator <=174 then q_E=36, since 1/174>0.00573. Denominator 175 permits 36+1/175 inside the interval. A suitable number-field height formula is one possible route, not the only logical form of a proof.

These are endpoint dependencies, not new certificates. See [retained endpoint excerpts](context/ENDPOINT_EXCERPTS.md).

## 5. Running versus pending

RUN_NOW records the redirection to the actual bottom-layer CM-divisor/localization construction. This audit confirms the recorded assignment, not live execution of a session titled “Exact BD constant.” Its best stated outcome is a geometrically defined detector with justified maps; the fixed scalar law would still require proof.

Two prompts are present in the inspected record:

1. Independent reimplementation of selected exactness-test rows, including producer conventions.
2. Independent check of Exit 1 §11.2/§12's claimed exact derivative-content formula and its integral/source hypotheses.

No completion receipt for either was established in this check. They remain **recorded pending checks**, not accepted new conclusions. In particular, the exact equality m_p-w_p = length Sha[p^infinity] + a Bockstein valuation (after the claimed unit comparison) is not promoted from the Exit 1 report or RUN_NOW summary. The weaker supported content bound remains separate.

See [RUN_NOW excerpts](context/RUN_NOW_EXCERPTS.md) and [Exit 1's submitted formula and audit request](context/EXIT1_PENDING_FORMULA.md). Archived prompts are source material, not launch instructions.

## 6. Checks and publication scope

All 49 ordinary manifest entries of the exactness package match. Its remaining manifest entry is a special aggregate hash, not a literal filename: the concatenation of 171 symbol files in filename order matches that digest. A conventional sha256sum invocation needs that line handled separately. The source files were not changed.

Eight source bindings, copied files/excerpts, a standalone stored-data check, and endpoint arithmetic are retained. Hash agreement is custody; stored congruence agreement is not producer replay. This return updates only the lab's current status/navigation and adds this sealed record. It does not promote research main, recertify all historical mathematics, or report progress through the seed's missing arithmetic theorem.
