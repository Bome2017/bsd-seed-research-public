# Closed cycle to two-prime Kurihara content: result

**Status: NO_TWO_PRIME_COMPARISON_FROM_TESTED_CONSTRUCTIONS.**

I carried out the proposed comparison in the mixed augmentation quotient and then checked finite combinations across different pairs. I did not prove the membership -2 in I_p^(2), disprove it for the seed, or obtain a uniform vanishing theorem. The failure of the tested maps is explicit below; it is not a claim that every arithmetic comparison is impossible.

## The main finding

The closed-lift construction's nonzero period is valid under its retained inputs. But its final weighted operator has a stronger identity than the original proof recorded:

    (sum_j j^2 (beta_j)_*)(U_*-1)^2
       = 2(T_p alpha_*-beta_*) pi_*   mod p.

The noninvariant choice disappears from the final cycle modulo p. For the prescribed oldform cycle C and its primitive starting cycle v this gives

    R_p = 2u(T_p^2-1)v in H_1(X_0(N),F_p),
    u((p+1)^2-a_p^2)=1 mod p.

Therefore z_E(R_p)=-2 is the old primitive period transported by an explicitly invertible scalar on the f-period quotient. It does not yet provide an independent reason why the canonical arithmetic packet has unit content.

The operator identity is proved integrally, with the two wraparound terms retained, in [CLOSED_CYCLE_AUDIT.md](CLOSED_CYCLE_AUDIT.md). It also explains why varying the chosen closed lift cannot improve its final mod-p content.

## The mixed quotient was actually constructed

Let X=sigma-1 and Y=tau-1 for the two degree-p tame directions. The closed period sequence can be polarized and projected, with no p-denominator, to the class -2XY in

    I_1 I_2/(I_1^2 I_2+I_1 I_2^2).

The actual complete two-prime homology packet is eta delta_(ell_1 ell_2) XY there, where eta=2c_E is a p-unit. These are different coefficient constructions. Their difference in that quotient is exactly

    (-2-eta delta_(ell_1 ell_2))XY.

Replacing the artificial coefficients by the actual packet fixes the arithmetic identification but destroys the proposed finite-difference nonvanishing: the genuine packet already belongs to J^2, and the two differences place it in J^4. Its mixed quadratic coefficient is then zero. This is true even for a packet whose original delta was a unit.

Omitting those extra differences recovers the right coefficient delta. The two conductor norm projections, however, do not determine it: their degree-two kernel is precisely the one-dimensional mixed coordinate kXY. This is the explicit augmentation-quotient mismatch requested in the task.

## Allowing combinations of pairs does not resolve this particular calculation

I also used the retained, reviewed comparison

    delta_ab=C_p e_a e_b D_ab^2.

The determinant and local factors have a nonzero value for some cyclic pair independently of Sha. Thus the ideal of all these pair coefficients is (C_p). Every proposed finite combination remains C_p times the corresponding known determinant combination. Inverting those known determinants computes C_p from a witness; it does not identify C_p with the independently chosen period -2. Assuming 1/C_p would be circular.

This does not require a rational constant common to different coefficient primes, and does not prohibit a new proof that C_p is a unit. It answers the specific suggestion that replacing one-packet identification with ideal membership might make the already available relations sufficient. They have not supplied the required inhomogeneous arithmetic identity.

Full derivations and the jointly assembled oldform-matrix test are in [MIXED_COMPARISON_ATTEMPT.md](MIXED_COMPARISON_ATTEMPT.md). Exact source conventions and the endpoint implication are in [SOURCED_TARGET.md](SOURCED_TARGET.md).

## What this changes for the BSD attempt

The inference that the newly repaired noninvariant cycle is already an additional constraint on the two-prime witness content should not be used. The concrete operator above reduces its endpoint content to the original primitive-period comparison. The desired seed-specific membership remains a valid sufficient target, but it has not been established by this construction or its tested repairs.

No new two-prime seed witness, cofinite vanishing bound, fixed annihilator, FIN, ORDER9, or Q36 result was obtained. This pass is a mathematical check and construction attempt, not progress through the uniform upper bound.

## Evidence and review limits

The exact controls pass. They check the integral finite-difference coefficients, Borel commutators, mixed group-ring substitutions, vanishing after applying extra differences to a unit leading packet, the simultaneous old-transfer matrix, and the scalar factor retained in multi-pair sums. Small seed point counts serve only as local normalization controls. No actual seed Kurihara coefficient was evaluated.

The closed-lift input manifest verifies 10/10 entries. Twelve retained inputs are bound in INPUT_BINDINGS.json, including the exact selected release claims. Their substantive imported arithmetic proofs were not re-certified in this pass. Novelty is not assessed; this is not a human or Lean review. [SCOPE_AND_COLLISIONS.md](SCOPE_AND_COLLISIONS.md) separates the reused results from the present derivations.
