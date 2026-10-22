# Attempt: use the integral tame coefficient to bound the lifting layers

**Disposition: valid sufficient criterion; collision with retained Corollary S′; NO_NEW_UNIFORM_INPUT.**

This candidate was admitted because its stated success would prove cofinite primary vanishing, rather than only produce another divisor identity. Its proof obligation and missing arithmetic input are separated below.

## Candidate theorem sufficient for the seed

For all p outside one fixed finite set, produce an auxiliary prime ℓ meeting the retained level-p² tame hypotheses such that the quadratic coefficient

    C2^(2)(p,ℓ) is nonzero in Z/p².

The auxiliary may depend on p. No demand for one common auxiliary, one common number, or one p-independent object is imposed. Ordinary and supersingular coefficient primes are both within the retained tame framework.

The required hypotheses include ℓ ≡ 1 mod p², ℓ coprime to pN, p not dividing #E(F_ℓ), and the retained BKS prime domain. They are **not** the Kato-prime conditions. A unit tame regulator is needed to use the normalized scalar w, but not for the direct coefficient criterion just stated.

For comparisons using a normalized w and the recorded existence result G2, one can harmlessly add 5 to the finite exceptional set, preserving the original G2 domain rather than silently extending it. The unnormalized implication below does not use a G2 existence theorem.

## Implication, without assuming FIN

Write A=Sha(E/Q)[p∞]=D ⊕ F, with d=corank D and F finite. The retained integral factorization, stated in `context/WORKING_1.md` as Lemma S and in `context/WORKING_2.md` as Corollary S′, gives for every level k:

    d > 0  =>  C2^(k)(p,ℓ)=0;
    d = 0  =>  C2^(k)(p,ℓ) belongs to #F · (Z/p^k).

All these implications retain that factorization's import and normalization assumptions. Its integral Kato coordinate is not assumed to be a unit.

If C2^(2) is nonzero, then d=0. Its valuation is either 0 or 1. The second implication gives log_p #F ≤ 1. A finite elliptic-curve Sha p-part has a perfect alternating Cassels–Tate pairing for odd p, so its order is a square. Therefore F=0 and the entire primary group is zero.

In the notation of the uploaded pairing audit, a nonzero level-k coefficient with valuation v<k gives the more informative accounting

    D=0,
    sum_n (n+1) rank(b_n) = log_p #F ≤ v.

The same statement holds for w_p^(k) when its denominator is a proved p-unit. This is the precise way the integral factorization could constrain the higher lifting layers. It controls the persistent part as well as the finite layers; the abstract pairings alone control neither.

## Why this is not a new route or a proved bound

Corollary S′ already states that a nonzero level-k scalar bounds the order by p^v. The p² criterion above is its square-order consequence. Adding the pairing filtration explains the bound's contents but supplies no new arithmetic estimate.

The following retained inputs do not prove the candidate's cofinite premise:

- G2 provides auxiliaries with a unit tame regulator. It does not make the numerator or the unknown Kato coordinate a unit, or merely nonzero modulo p².
- W^(k) identifies normalized values at different admissible auxiliaries for a fixed p and k. This transfers a value; it does not prove that value is nonzero, and does not relate different coefficient primes.
- Existence of a nonzero Kurihara witness at some length does not bound that length by two and is not this G2 coefficient statement.
- The finite K288 congruences do not construct a common rational scalar or prove its height. Substituting 288 for the unknown integral scalar would assume the missing comparison.
- The exact receiver and its secondary pairings do not supply an upper valuation estimate. A p² coefficient is zero whenever the actual finite part has order at least p², exactly as the retained divisibility requires.

Thus the missing independent input is specific: a theorem bounding this quadratic coefficient's valuation below two, with a single proof covering all but finitely many p, or some different independently controlled annihilator/rank argument. None has been constructed in this pass.

The criterion is only sufficient. This note does not assert that Sha[p∞]=0 forces the particular tame coefficient to be nonzero, since the extra Kato factor is not controlled here.

## Decision under the user's gate

Do not launch a per-prime coefficient or receiver computation based on this accounting. No cofinite nonvanishing estimate has been supplied. The attempted combination is retained as a collision check, not promoted to a new main-line BSD result.

FIN, ORDER9 and Q36 are unchanged.
