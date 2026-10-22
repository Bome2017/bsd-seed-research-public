# Exact primary groups for both isogenous control pairs

2026-10-13. Grade: written theorem application under retained computational and arithmetic inputs, with separate same-team source review. No new L-value, height, descent or Selmer computation is claimed.

Write A_d,F_d for the d-twists of the conductor11 isogeny class used in the experiment. Their minimal models are:

| d | A_d coefficients [a1,a2,a3,a4,a6] | F_d coefficients |
| --- | --- | --- |
| 43737 | [0,0,1,-19766893413,-1937478573143510] | [0,0,1,-14959712463303,-22270654620235278500] |
| 329233 | [0,-1,1,-1120075138986,-826418095533154920] | [0,-1,1,-847680091476076,-9499397825675855099600] |

Retain the recorded rank2 upper bounds and the exact point-independence/5-saturation checks, trivial rational torsion, good ordinary reduction at5, a5=-1, C_A=20,C_F=4, and the actual canonical-height and Neron-period conventions. The computational rank bounds and coefficient production retain their prior grades.

## 1. The applicable integral theorem

Both twists have residual semisimplification chi_d plus omega*chi_d. Since d is prime to5 and is a nonsquare mod5, chi_d is a nontrivial unramified local character. Neither constituent is1 oromega locally. Castella--Grossi--Skinner TheoremA/7.1.1 applies separately to both curves in each pair, giving the integral ordinary main conjecture. Its scope is not limited to algebraic rank0 or1. See MAIN_CONJECTURE_AUDIT.md for primary-source matching.

Combining it with the algebraic leading-term theorem as in LEADING_TERM_AUDIT.md gives, when L2 is nonzero,

    length_Z5 Sha(C/Q)[5-infinity]
      = v5(L2_C) - v5(det H_U,C) - v5(C_C),

because torsion and the ordinary Euler factor are5-units here. Nonzero L2 establishes primary finiteness before this equality is applied. We do not assume full Sha finite.

## 2. The two F groups

The saved direct series give:

    d43737: L2_F=4*5^2+O(5^3),  v5(det H_U,F)=0;
    d329233: L2_F=3*5^4+O(5^5), v5(det H_U,F)=2.

The second line is the actual precision8 result, not the earlier precision7 zero residue. In each case C_F=4. Thus both primary groups are finite of length2, hence order25.

The separate Cassels isogeny-Selmer calculations, which do not use these numerators or finiteness, already give dim_F5 Sha(F_d)[5]>=2. A group of order25 with at least25 elements killed by5 is killed by5. Consequently

    Sha(F_43737/Q)[5-infinity] ~= (Z/5)^2,
    Sha(F_329233/Q)[5-infinity] ~= (Z/5)^2.

The second statement is additional to the supplied Pro packet. It completes the primary-group identification for the combined positive-excess/nonunit-regulator control.

## 3. The A partners

The retained degree5 isogeny phi:A_d -> F_d has differential multiplier1, five real kernel points, and point-map determinant5 on the displayed5-saturated pairs. Its period relation is Omega_F=Omega_A/5. Thus the standard Neron-normalized measures obey L_std,F=5 L_std,A, in the same cyclotomic coordinate and with the same ordinary root.

Functoriality of the canonical unit-root height gives M^t H_F M=5H_A. Taking rank-two determinants, with detM=5, gives detH_F=detH_A. These are the source-matched identities, not an inference from matching numerical determinants.

It follows that

| d | v5(L2_A) | v5(det H_U,A) | v5(C_A) | primary Sha length |
| --- | ---: | ---: | ---: | ---: |
| 43737 | 1 | 0 | 1 | 0 |
| 329233 | 3 | 2 | 1 | 0 |

The first A numerator was also independently calculated in the paired experiment. The second is derived through the exact isogeny normalization; we do not claim an independent A_329233 numerator run. The nonzero F coefficient makes each A coefficient nonzero. The same integral theorem and leading-term argument therefore prove

    Sha(A_43737/Q)[5-infinity]=0,
    Sha(A_329233/Q)[5-infinity]=0.

Equivalently, the fully corrected quotients obey Q_F=25Q_A. Their valuations are2 and0. The main conjecture does not fix their remaining p-adic units; neither Q_F=25 nor Q_A=1 is asserted as an exact infinite-precision identity.

## 4. Research consequence

We now have two paired controls with exact primary groups under the retained grades, one pair with a unit regulator and one with a nonunit regulator. In each pair the same height determinant occurs on opposite sides of an exact primary contrast. Thus neither regulator degeneracy nor equality of regulator determinants determines the corrected excess.

This is a theorem application to completed experiments, not a uniform estimate or a transfer theorem to the seed. The rational5-isogeny makes these residual representations reducible, and the new combined control has coincident height/logarithm lines. The seed17 configuration remains distinct-line with full residual image. No seed prime or whole-Sha endpoint is settled here.
