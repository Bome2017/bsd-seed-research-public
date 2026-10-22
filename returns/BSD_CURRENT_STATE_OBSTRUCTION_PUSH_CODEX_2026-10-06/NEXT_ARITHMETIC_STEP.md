# Where the repaired Stage A can actually be continued

This is a continuation of the construction in STAGE_A_DERIVATION.md, not a
launch instruction. No new Aristotle task has been submitted.

## The exact output to use

Subject to independent review of that proof, there is an intrinsically defined
space of actual tame first-order character deformations in which the two
known point classes lift. Its obstruction maps detect every class outside W.
This holds in the original classical Selmer space, without an ordinary
Hida branch and without assuming Sha vanishing. The natural target is S^*,
not one scalar per deformation.

An independent review should first challenge the cochain/local-condition
calculation and the simultaneous Chebotarev prescription. Merely verifying
the symmetric-matrix algebra would not review the arithmetic theorem.

## The next arithmetic equation, before a determinant switch

For a genuine character family chi(t), write

    rho_t(g) = rho(g) [1 + t lambda(g) + t^2 mu(g) + ...],
    c_i(t) = c_i + t a_i + t^2 b_i + ...,

where c_i is the fixed Kummer cocycle of P_i. First-order liftability provides
a_i with the required local conditions and

    d a_i = -lambda cup c_i.

The next equation is

    d b_i = -lambda cup a_i - mu cup c_i.                  (L2)

Multiplicativity of chi requires

    mu(gh) = mu(g) + mu(h) + lambda(g)lambda(h).

For p >= 5 a concrete second-order character choice exists:

    chi(t) = 1 + t lambda + (t^2/2) lambda^2 mod t^3.

Indeed multiplication verifies the formula, and it is a character of the
finite additive group k into (k[t]/t^3)^*. Thus the first higher-order test
need not start by searching for a character lift: one is written down.
Adding another admissible tame additive character eta to mu supplies the
available correction term eta cup c_i in (L2).

What has not been proved is simultaneous solvability of (L2), with the same
eta for i=1,2 and the matching local Selmer conditions. It requires a proof
that the two second-order obstruction classes lie in the image of the
known-point restriction of the first-order character pairing. The section
choices a_i affect this question; they must be tracked, not silently chosen
to make the obstructions zero. Higher orders would then require compatible
solutions, and an actual arithmetic family realizing the finite-order data.

This is a sharper continuation than "prove a rank-two switch": construct the
two point sections to order three and identify the cokernel of this precise
correction map. A successful result would remove a genuine prerequisite of
Stage B. It would not alone give the cross-prime conclusion in Stage C.

## Why Stage A cannot simply be promoted to Stage B

Over k[[t]], consider the two-term complex with differential

    D(t) = diag(t^2 I_2, t I_2).

At t=0 its H^1 has dimension four. Its first derivative has kernel exactly
the first two coordinates, which can be named W. Those two directions have
first-order lifts, but over k((t)) the differential is invertible and H^1=0.
Thus a first-order kernel W does not produce two generic cohomology sections.

The same logical control can be made alternating by replacing the two I_2
blocks by J=[[0,1],[-1,0]], if an ordinary alternating-complex condition is
imposed. Neither formal complex is asserted to arise from the seed or to
match every extra symmetry of the proposed arithmetic family.

This is an implication check, not a claim that the arithmetic lifting
problem is impossible. The explicit equation (L2) is the attempted repair.
The source's rank-one determinant switch still cannot be cited as a
rank-two theorem. Only after actual compatible point sections exist should
one prove the top-exterior-power comparison for their determinant tensor.

## Stage C remains a separate BSD requirement

Even a family preserving W while killing all excess away from its special
fibre can have excess at the original seed specialization. An index with a
nonunit specialization is precisely how that can happen. One needs an
independently controlled integral comparison, uniformly in p, to rule it out.

The requested fixed integer criterion

    Sha[p] != 0 => p divides A_E,   0 != A_E in Z,

would close the cofinite support step. No such A_E or substitute uniform
bound is constructed here. G2 supplies the rational-point regulator side;
it is already proved in the record and is not a new target. If the terminal
index is the existing tame scalar s_p, the remaining assertion must be
identified explicitly with G1 rather than renamed.

Passing Stage A therefore makes this a usable deformation experiment. It
does not establish a complete route to BSD or warrant a long uncontrolled
run. The concrete review/lifting task above is the next admissible step.
Exceptional primary finiteness, ORDER9 and Q36 remain separate.
