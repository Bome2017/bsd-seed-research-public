# Biextension scalar attempt

Start with the actual proposed rational line and its realizations. No endpoint promotion.
## Construction checkpoint

The submitted ZIP is a task proposal, not a proof. Its SHA256 matches the user and its three listed manifest entries verify.

The retained G2 proof already constructs normalized rational Poincare fibers at Q_i=16P_i. Two concrete issues must be repaired before a scalar quotient can do what the brief asks:

1. Tensoring P_11 P_22 / (P_12 P_21) realizes B_11+B_22-B_12-B_21, not det(B). The correct quadratic carrier is the squared Mordell-Weil determinant line with a map into Sym^2 of the tame-height target.
2. A tame splitting of a G_m torsor transforms by adding the tame character of a rational multiplier. It is not a Q-linear realization with scalar reduced mod p. The full global height instead kills a change by a principal idele.

The elementary repair is D=(wedge^2 L)^tensor2, embedded primitively in Sym^2(Sym^2 L) by (P1 wedge P2)^tensor2 -> (P1^2)(P2^2)-(P1P2)^2. This is a candidate for an explicit verified construction below, not a new uniform bound. The September 18/19 RANK2_GLOBAL_OBJECT_COMPOSITION.md already contains this carrier and the unproved LINE comparison. Historical scope overclaims in that file are not adopted.

Next: write normalized sections with their integral normalization, check the quadratic carrier and seed normalization, then attempt the modular section in the actual finite augmentation quotient. Do not replace the missing modular lift by a freely chosen scalar, and do not label the repaired old carrier as a new global input.

## Completion

- Exact rational Q_i and Q_i+Q_j were computed by separate Fraction and PARI group laws and matched.
- The retained pairing checker reproduced its three cases. The fixed Q16 matrix at p=17,l=103 distinguishes the raw tensor value 1 from determinant 7.
- All 102 old identified plus symbols at that pair were recombined: C2=7 mod 17, production R=6, a_l=-2, w_17=16. This is input reuse, not new analytic certification or primary progress.
- PROOF.md repairs the determinant carrier and scalar-action distinction, then explicitly attempts the modular lift. Rationalization of the finite augmentation quotient loses the class; retaining all components does not supply the rational lift.
- The squared determinant carrier and LINE already appear in the historical record. No new uniform input is claimed. Overall status NO_GLOBAL_SCALAR_CONSTRUCTED, not a blanket TNC/nonexistence verdict.
