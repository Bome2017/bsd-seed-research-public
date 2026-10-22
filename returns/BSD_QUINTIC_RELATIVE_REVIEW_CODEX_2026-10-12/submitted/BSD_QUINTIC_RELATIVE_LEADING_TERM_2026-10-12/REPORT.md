# Exact relative leading term over the first quintic layer

2026-10-12. Baseline lab commit: `84a7333af028ff5bc694bc82bcb3c768a019f5c6`.

**EXACT_RELATIVE_LEADING_TERM_DERIVED_UNDER_RETAINED_INPUTS; NO_NEW_SHA_ORDER.**

The new point-group equality E(Q_1)=E(Q) makes an exact relative leading-term calculation possible without an unknown regulator index. I executed that calculation using the original 20 denominator-25 symbols. This is not another source-normalization construction and not a new p-adic coefficient digit.

Let F=Q_1 be the degree-five subfield of Q(mu_25), and let A_K denote the fully BSD-normalized analytic leading term over K, including its field discriminant, full real period, relative-height regulator, torsion, and finite local factors. This is a real analytic quantity, not an assumed Sha order. The written deduction gives

    A_F = 19^4 A_Q = 130321 A_Q.

Since the seed's A_Q=q_E/4,

    A_F = (130321/4) q_E.

No BSD conjecture or separate rationality of either leading term is used in this identity. [Full proof](PROOF.md).

## Arithmetic extracted from the saved table

For a primitive fifth root zeta, the correctly full-period-normalized character sum is

    B(zeta)=38(-1-zeta^2+zeta^3+zeta^4)
           =-38 zeta^2(1+zeta)(zeta-1)^2.

All four conjugates are nonzero. Its exact norm is 38^4*25=52128400. The two inverse-character Gauss products are each 25, verified directly in Z[mu_25]. Therefore the four nontrivial order-five twists have

    [ product_{chi != 1} L(E,chi,1) ] / Omega_E^4 = 38^4/25.

This also gives analytic rank exactly two over F, using the retained analytic rank over Q. These are evaluations of twisted complex L-values from old symbols, not extra digits of [U^2]L_std,p.

## Complete field and arithmetic factors

The first layer has discriminant 5^8 and sqrt(discriminant)=625. A Gaussian-period generator has minimal polynomial

    X^5-10X^3+5X^2+10X+1,

whose polynomial discriminant is 7^2*5^8. The extra 7 is a power-basis index and is not inserted into the BSD formula.

The bad primes 2,3,4547 are inert, while 2243 and 5843 split completely. The minimal differential stays minimal. Using the retained local types gives C_Q=16 and C_F=256. The new point equality gives identical torsion and R_F/R_Q=25 in the field-relative height convention. Thus the relative factor is exactly

    (38^4/25) * 625 / (25*16) = 19^4.

The proof includes the additive-place check at 2, rather than assuming the seed is semistable. No number-field point search, Tate algorithm, or large Fourier computation was launched.

## What this does and does not say about BSD

The equality A_F=19^4 A_Q is a derived analytic identity. The additional equality #Sha(E/F)=19^4 #Sha(E/Q) remains conditional on BSD over the two fields. No actual 19-primary class, relative Sha size, or support theorem was proved.

Q36 is equivalent to A_F=1172889, but that is a reformulation rather than a second independently known value. Unknown base-field ell-primary classes for ell != 5 inject into the first layer by restriction/corestriction. The field extension does not remove those original obligations.

The explicit character numerator supplies a concrete relative 19-primary target. Turning it into an arithmetic group statement still needs an applicable independently checked Selmer or leading-term theorem; a conjectural Artin-twist ideal formula is not substituted for that input.

## Verification and review grade

The [standard-library checker](checks/verify.py) and [deterministic output](checks/RESULTS.json) verify the pinned 20-row input, two constructions of its character map, the factorization and norm by independent exact algorithms, two finite Gauss identities, the Gaussian-period polynomial and its discriminant, the five splitting rows, the rational leading-term factors, and four normalization countercontrols. The norm is also recovered from all four character conjugates. None of these computations determines a Sha group.

The original symbol certification, differential convention, local types, rank/image inputs, and the reviewed point-group equality remain retained. This is a single-assistant written derivation with executable exact arithmetic, not independent human, separate-agent, or formal verification. Sources and scopes are in [SOURCES.md](SOURCES.md); hashes and pinned paths are in [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json).

Run `python3 checks/verify.py` and compare with the saved output. Run `sha256sum -c SHA256SUMS` in this folder for file integrity. Hashes verify custody, not mathematical hypotheses.

**FIN, ORDER9, Q36, and base-field coefficient-prime coverage are unchanged.** Publication is additive on a separate lab branch; main and the expert-review repository are not modified.
