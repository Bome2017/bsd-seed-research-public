# Scope of the new seed calculation

Date: 2026-10-13. This file records the implication before the production result is available.

The curve is

`E: y^2 = x^3 - 22735*x^2 + 106272484*x`.

The calculation uses coefficient prime 83 and singleton conductor 167. All 166 plus modular symbols are evaluated from the retained coefficient corpus by the pinned interval engine. The fixed lattice is `(1/1024) Z`, and the cutoff is 57,378,078,719. The output must independently identify one lattice rational in each rigorous interval; approximate agreement with a desired residue is insufficient.

For the smallest primitive root 5 modulo 167, put `x(a)=ind_5(a) mod83`. The projected group-ring coefficients are

`c_k = sum_{a=1}^{166} binom(x(a),k) [a/167]^+`, for `k=0,1,2`.

The frozen checker requires exact `c0=0` and `c1=0 mod83`, before deciding whether the actual `c2` is nonzero. The pre-existing tame prediction 44 is excluded from this calculation and from acceptance. No BSD quotient, regulator, Sha order or inferred Kato coefficient is an input to the numerator.

## Arithmetic implication

Ota, *Kato's Euler system and the Mazur–Tate refined conjecture of BSD type*, Theorems 1.5 and 6.4, supplies the conditional theorem application. The primary source was freshly read in this session: <https://arxiv.org/pdf/1509.00682>. The source permits cyclic reduced 83-torsion at the auxiliary prime, including the zero group; it does not require `a_167=2 mod83`.

The retained rank is two and the integral Tate-module image is full. The retained conductor is 6503188012738584 and Tamagawa product is16. Fresh exact enumeration gives `#E(F83)=92` and `#E(F167)=168`. Thus the coefficient prime is good and non-anomalous, and the auxiliary prime is good with `167-1=2*83` and zero reduced83-torsion. The period and lattice comparison stays at its previously retained grade; this run does not re-prove that antecedent.

On these matched inputs, an accepted nonzero leading degree-two augmentation coefficient implies `Sha(E/Q)[83]=0`. Any nonzero element of an83-primary torsion group has a nonzero multiple of order83, so this implies `Sha(E/Q)[83^infinity]=0`. No prior83-primary finiteness is needed for this final step.

The detailed hypothesis ledger is `selection/P83_OTA_THEOREM_CHECK.md`; the frozen copy is retained in the input package. The independent interval verifier checks output arithmetic, not the generation of the underlying Fourier coefficients or the analytic enclosure theorem. Same-team review is not independent human or Lean certification.

## What the outcome can change

- Accepted nonzero: new base-field83-primary vanishing, under the retained arithmetic and computational inputs.
- Accepted zero: this auxiliary is inconclusive. It does not establish a nontrivial83-primary group.
- Invalid or interrupted: no mathematical conclusion from the incomplete or rejected run.

The baseline lab state is commit `15db242ee6224c85f60e7a9a999df3e8cfd6469b`. Coefficient83 was not listed as settled there. Even success here does not settle coefficient53, improve the conditional next-order floor25281, prove a cofinite bound, or finish FIN, ORDER9 or Q36. This is direct finite coverage on the seed, not a new mechanism for controlling infinitely many coefficient primes.

## Custody boundary

The 9,673,187,648-byte cached coefficient prefix has been freshly hashed against retained arithmetic receipts. It has not been generated again by an independent engine. Its raw bytes remain an explicitly external local dependency unless a distribution package specifically includes them. The new production work units, final interval table, frozen parameters, receipts and independent output verification must all remain available. A compact archive must not present a hash or local path as though it included the coefficient corpus.
