# The precise integral presentation gate for a class-map bound

Date: 2026-10-22. Elementary bookkeeping for deciding whether an integral class-map/Fitting experiment can bound all class directions. This is not asserted to be new mathematics or a seed certificate.

Let C_A and C_B be the actual finite p-primary class components and u:C_A -> C_B the actual arithmetic class map. Suppose finite presented p-groups P_A,P_B have authenticated surjections q_A:P_A -> C_A and q_B:P_B -> C_B, and an authenticated integral lift U:P_A -> P_B makes q_B U = u q_A. Put K_A=ker q_A, K_B=ker q_B, so U(K_A) lies in K_B.

The snake lemma supplies

    0 -> ker(U|K_A) -> ker U -> ker u
      -> K_B/U(K_A) -> coker U -> coker u -> 0.

In particular, writing d_p(G)=dim_Fp(G/pG)=dim_Fp G[p] for a finite abelian p-group,

    d_p(ker u) <= d_p(ker U) + d_p(K_B/U(K_A)).          (1)

Indeed the image of ker U in ker u is a quotient of ker U, and the remaining quotient embeds in K_B/U(K_A). The generator rank of a subgroup or quotient of a finite abelian p-group cannot exceed that of the group. The extension inequality completes the proof.

A useful asymmetric certificate follows. If the TARGET presentation is p-exact (K_B=0), it is enough for the SOURCE presentation to be a complete surjection; unknown extra source relations are harmless for this upper bound:

    d_p ker u <= d_p ker U.                            (2)

One need not determine the exact source class number or every source relation. But one does need complete source generation and a target with no hidden p-relations, or an independently bounded error in (1). A numerical Fitting ideal of a selected matrix supplies neither assertion by itself.

The integral kernel of U can be computed from exact finite presentations by Smith/Hermite operations. Reducing U mod p does not in general compute the map on C_A[p]. In particular, a surjection P_A -> C_A need not induce a surjection P_A[p] -> C_A[p]: Z/p^2 -> Z/p is a counterexample. Any claimed shortcut must retain the whole finite p-group or prove exponent control.

## A sharp target-error check

Take P_A=P_B=F_p^e and U=identity. Let q_A be identity and let C_B=0, so K_A=0 and K_B=F_p^e. Then ker U=0 but ker u=F_p^e. Formula (1) is exact. Thus an arbitrary number of actual class-kernel directions can be hidden by target relations even when the displayed lifted map is an isomorphism.

This is a presentation countercontrol, not a seed realization.

## Why exponent control is not enough by itself

Even authenticated maps u,v satisfying vu=p and uv=p do not bound the p-torsion kernel. For C_A=C_B=(Z/p^a)^e, choose u=p and v=identity. Then ker u=(Z/p)^e for arbitrary e. At a=1 there is no deeper nonzero p-power layer to compute, but the kernel still has arbitrary dimension. Thus a higher-exponent/Bockstein proposal must add a property beyond the formal incidence composition.

## Actual next arithmetic admission test

Before running an integral class-map or Fitting calculation on the seed, identify:

1. the finite ideal generators that cover the entire source p-component (or a proved omitted-generator bound);
2. the exact integral relations and ideal incidence lift defining U;
3. the target p-relation defect K_B/U(K_A), certified zero or quantitatively bounded independently;
4. whether the resulting bound for d_p ker u is less than the current complete allowance, after the unit and valuation contributions are restored.

The saved 1664n1 control supplies complete source and target presentations and a zero class map on its C3; it passes the certificate interface but does not reject its point-occupied class. The actual seed p=5 does not yet have items 1 and 3 in an unconditional finite presentation. Therefore no new seed bound is claimed from (1) or (2).
