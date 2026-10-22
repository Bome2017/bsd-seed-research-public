# BSD target-curve push: global biextension scalar attack

Date: 2026-10-05

## Status
NEW DIRECTION AFTER THE W3 FOUR-VALUE REDUCTION.

The W3 route now has an explicit finite arithmetic test, but still needs a uniform nonvanishing theorem for a p-dependent Kato object. This attack changes the type of object: construct one p-independent rational scalar from two global trivializations of the same determinant biextension attached to the fixed rational points P1,P2.

This file does not claim that theorem is already proved.

## Retained endpoint data
Use the retained prime-conductor depth-two class C2(p,l), tame regulator R_{p,l}, and:
- C2(p,l) != 0 => Sha(E/Q)[p^infinity]=0.
- G2 supplies admissible l with (a_l-2)R_{p,l} != 0 on its stated domain.
- Theorem W gives a fixed-p scalar w_p but does not prove cross-p compatibility.

## 1. Build one p-free determinant line
Let P be the Poincare biextension on E x E, extended over the Neron model away from a fixed finite set S.

Restrict to L=<P1,P2>. Construct the determinant/exterior-square biextension line D_L whose tame realization is the determinant of the bilinear tame-height matrix on P1,P2.

Required theorem:
construct a nonzero rational section tau_Ner of D_L such that for every admitted (p,l),

    tame_{p,l}(tau_Ner) = u_Ner(p,l) R_{p,l},

with u_Ner explicitly determined by the already frozen production normalization.

Do not define tau_Ner using R_{p,l}; construct it from the Poincare/Neron biextension first.

## 2. Build the modular-symbol section in the same line
Construct a nonzero rational section tau_MT of the same D_L, or of one fixed tensor power D_L^m with m independent of p, from the Mazur-Tate/modular-symbol side, such that

    tame_{p,l}(tau_MT)
      = u_MT(p,l) C2(p,l)/(a_l-2).

Allowed ingredients include:
- theta_l and its I^2/I^3 class;
- the repaired Theorem W;
- the accepted U22 exact Klingen-boundary coefficient carrying C2 at depth eight;
- existing modular-symbol cycle constructions;
- Fourier-Jacobi/Jacobi line-bundle realizations if they genuinely evaluate on (E,P1,P2).

Forbidden: any refined BSD / ETNC / generalized Perrin-Riou leading-term formula whose hypotheses already assume Sha finite.

## 3. Exact payoff
If tau_MT and tau_Ner are nonzero rational sections of the same Q-line, then

    Z = tau_MT/tau_Ner in Q^x

is defined independently of p and l.

After matching the normalizations, prove

    C2(p,l) = red_p(Z) (a_l-2) R_{p,l}   in F_p.

No exact value of Z is needed.

Outside the finite set consisting of:
- model/theorem exceptions;
- numerator/denominator primes of Z;

G2 gives an l with the last two factors nonzero, hence C2 != 0, hence Sha[p^infinity]=0.

This is the desired cofinite mechanism.

## 4. First concrete calculation
Do not start with another survey.

1. Construct D_L explicitly from P1,P2.
2. Write the Neron/Poincare rational trivialization at one good auxiliary l.
3. Take the prime-conductor Mazur-Tate theta_l and isolate its degree-two class in I^2/I^3.
4. Express R_{p,l} as the exterior-square regulator of the same two Kummer directions.
5. Attempt to lift both realizations to the same Z[1/S]-line before reducing modulo p.

The first acceptable new identity is an equality in a p-independent Q-line or Z[1/S]-line.

## 5. Kill tests
K1. If tau_MT exists only after inserting #Sha or a leading-term object requiring Sha finiteness:
    GLOBAL_BIEXTENSION_COLLAPSES_TO_TNC

K2. If only separate F_p scalars are produced, with no common rational line:
    NO_GLOBAL_SCALAR_CONSTRUCTED

K3. If the determinant of tame heights cannot be lifted canonically to an exterior-square/determinant biextension object:
    DETERMINANT_LINE_NOT_CONSTRUCTED

K4. If the automorphic realization works only on a non-cofinite Chebotarev subset of coefficient primes:
    PARTIAL_DENSITY_ONLY

K5. If the comparison retains an uncontrolled p-dependent unit:
    P_DEPENDENT_UNIT_REMAINS

## 6. Required statuses
Return exactly one:
- GLOBAL_BIEXTENSION_SCALAR_PROVED
- GLOBAL_BIEXTENSION_PARTIAL
- GLOBAL_BIEXTENSION_COLLAPSES_TO_TNC
- DETERMINANT_LINE_NOT_CONSTRUCTED
- P_DEPENDENT_UNIT_REMAINS
- PARTIAL_DENSITY_ONLY
- NO_GLOBAL_SCALAR_CONSTRUCTED
- NO_NEW_RESULT

For GLOBAL_BIEXTENSION_PARTIAL, name the exact p-independent object or map newly constructed and the one remaining comparison.

Do not replace the requested construction by another audit of W3.

## 7. Why pivot now
The W3 four-value result is useful but still p-dependent: one authenticated Kato value nonzero mod p^4 would kill Sha[p], yet no cofinite nonvanishing theorem is known from the present packet.

The new route attacks the cross-prime problem directly: if the fixed-p scalar w_p is the reduction of an automorphism of one fixed rational determinant line, its support is automatically finite.
