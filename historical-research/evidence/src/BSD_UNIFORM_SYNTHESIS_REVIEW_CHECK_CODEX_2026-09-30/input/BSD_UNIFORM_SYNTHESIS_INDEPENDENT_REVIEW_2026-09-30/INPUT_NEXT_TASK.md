# Exact handoff: review the newly available coverage input

This is a proposed task for the user's next review, not an instruction to launch a session.

Read `REPORT.md`, `NEW_INPUT_APPLICATION.md`, and `DEPTH_TARGET.md`. Source versions and hashes are provided. Retained seed input grades are not to be upgraded.

## Part A: the genuinely new source application

Attempt to refute the following implication at its first failing step:

    CLW author revision dated September 21, 2026, Theorem A
      + seed residual ramification at 2243
      + Castella–Sano Theorem A/Corollary A
    => for every good p>=5, M_infinity(delta)=0.

Check in particular:

1. The older squarefree hypothesis is absent from the current theorem and is not silently reinstated by a standing assumption.
2. At every good supersingular p>=5, the fixed prime 2243 meets (ram), the seed has large image, and p-regularity holds.
3. The omega component for V_f in CLW becomes the trivial component for T_pE; integral Kato elements and the bad-prime Euler products match the determinant conjecture used by Castella–Sano.
4. No rank-zero step from CLW section 5.6 is used in rank two.
5. The ordinary case and all hypotheses involving Tamagawa and Manin factors really cover every remaining good p>=5.

Return ACCEPT_AT_IMPORT_GRADE, ACCEPT_WITH_CORRECTIONS, or BLOCKED_AT_[exact step]. A negative finding must name the actual missing assertion, not merely note that these are preprints.

## Part B: precise consequence, not a new nonvanishing claim

Check the deduction

    minimum mod-p unit Kurihara length
      = dim_Fp Sel_p(E/Q)

using Kim Theorem 1.8, M_infinity=0 and the root-number parity of the Kurihara indices. In particular, distinguish the first nonzero p-adic index from the first unit index. Check that no finiteness of Sha was inserted.

Check the sufficient BH criterion at composite conductor:

    v_(zeta_p-1)(chi(theta_K)) < 4 => Sha[p^infinity]=0.

Track the full normalized element, Fitting base change, restriction, and parity. Do not silently replace the strict bound by <=4 or a complex nonvanishing assertion.

## What a subsequent construction would actually need

The open target may use p-dependent objects and conductors. A suitable conclusion is:

    There is a fixed finite S such that for every p outside S,
    there is a real cyclic degree-p K/Q, conductor coprime to pN,
    and a faithful chi with the above normalized depth <4.

Alternatively, prove a two-prime unit Kurihara witness, an independent uniform Selmer upper bound, or an independent finite-support annihilator. Exact 288 and Q36 are not required.

Before a new construction session, write the proposed identity or inequality and identify the step that bounds depth from above. If its bound is r_p itself, or assumes a length-two unit witness, it has not crossed the gap. An upper bound of four is also insufficient. Do not commission a repeat of the completed A1 source screen or U22 lower-bound construction without a new input for this step.

No new upper-bound mechanism is claimed in this handoff. Passing Parts A and B justifies adopting the coverage update; it does not itself authorize or justify another broad invention campaign.

Keep computations frozen. No paid jobs, repository changes, push, correspondence or new prime certificates are needed for this check.
