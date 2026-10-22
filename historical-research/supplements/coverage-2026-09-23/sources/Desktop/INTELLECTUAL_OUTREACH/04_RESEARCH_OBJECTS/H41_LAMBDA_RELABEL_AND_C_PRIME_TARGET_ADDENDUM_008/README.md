# H41_LAMBDA_RELABEL_AND_C_PRIME_TARGET_ADDENDUM_008

A record-and-correction object. **No new mathematics, no new level computed.**
`ADDENDUM_007` (`c1a6f8ea…`) is preserved byte-identical and is not superseded.

**1. The λ re-labelling, scope corrected.** `ADDENDUM_007` §5 printed `λ = 1/4, 3/4, 9/4, 117/4` as bare
rationals with no evidentiary marking. That was a defect. But the correction applies to **one** value,
not two: `λ = 9/4` at `N = 16382` is **already exactly certified** in the frozen record
(`d5888b62…`), by a rigorous 192-bit interval plus a proved denominator bound `q ≤ 24·d_max = 96` and a
uniqueness test — re-audited here at all eight covered levels by exact integer arithmetic, and all 24
recorded input digests still match. Only `λ = 117/4` at `N = 262142` rests on database decimals alone.

    CERTIFIED   v₂(λ) = −2 at N = 62, 254, 16382, 66, 114, 258, 4098, 16386
    SUPPORTED   v₂(λ) = −2 at N = 262142

**2. No circularity.** The certificate's script states "No database, floating point, or guessed optimal
representative is an input", takes the **minimal model's** period, and bounds denominators agnostically
over the whole isogeny class. So it never presupposed `a = 0`, `ADDENDUM_007` is logically independent of
it, and their agreement at `16382` is a real cross-check that also validates `ecdata`'s period and
L-value columns against a rigorous interval. At `N = 62, 254, 16382` both legs hold, giving `w_ℓ` odd.

**3. A cheap certified route to `262142` exists and is NOT run.** Denominator reconstruction needs 2000
coefficients and an AGM period — no modular symbols, so not blocked by the genus-2047 wall. Recorded as
available per the directive to stop numerical level checks; it would change no conclusion.

**4. `(L)` is not closed by known theorems** — recorded from the operator's literature check, not
re-verified here. Ohta covers primary torsion away from 6; Yoo primes `≥ 5` plus some 3-primary; Yoo–Yu
2025 give the rational *cuspidal* subgroup, not that all rational 2-torsion is cuspidal. The gap is
exactly ours: the **2-primary part at even level**.

**5. The target narrows to `(C′)`: `T_p = π̂(S₀)`.** `(L)` is retired as the object of proof — it is
sufficient but possibly strictly stronger, since characteristic-2 multiplicity one may fail globally
while this one cuspidal line still lands correctly. The statement to attack: *the unique order-two point
in `⟨[0]−[∞]⟩` lies in the embedded optimal H41 elliptic factor of `J₀(2p)`.* The closed form
`((p²−1)/16)([0]−[∞])` carries a prerequisite — it names that point only when
`v₂(ord([0]−[∞])) = n−2` — so the order-theoretic description is the definition. Hecke action, old/new
decomposition, optimal quotient. **No L-values.**

**6. A separate question, not to be conflated:** is the negative-H41 base `Γ₀(N)`-optimal for every
admissible `p`? Four cases say yes; proving it gives `a = 0` uniformly but does **not** prove `(C′)`.
Recorded as a question, not promoted to a conjecture.

    ADDENDUM.md      the eight sections
    computation/     audit_lambda_certificates.py, verify_certificate_inputs.py
    receipts/        LAMBDA_CERTIFICATE_AUDIT, CERTIFICATE_INPUTS_INTACT, CERTIFICATE_PROVENANCE
    MANIFEST.sha256  DIGESTS.md

**The H41 seed remains unproved.**
