# The seed index bound at ten critical specializations

Grade: WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS_AND_IMPORTED_EULER_SYSTEM_THEOREMS. Independent review is pending. This extends the arithmetic implication; it does not establish that one of the values is small.

## 1. The ten specializations

For i,j≥0 with i+j≤3 put

    w=10+i, s=7+j,
    t_w=(1+p)^w-1, t_s=(1+p)^s-1.

Specialize U at (T,S)=(t_w,t_s). Let g_w be the ordinary Hida newform of weight k=w+2 and nebentypus omega^(-w), with its retained integral lattice. Then

    U_(w,s)=V(g_w) chi^(-s) omega^s,
    det V(g_w)=chi^(w+1)omega^(-w).

All principal-unit characters reduce to 1, so U_(w,s)/p=E[p]. The coefficient DVR is Z_p on the retained cofinite Hida domain.

In the convention D(g)=V(g)^vee and D(g tensor psi)=D(g)psi^(-1), put

    h_(w,s)=g_w tensor omega^(w-s),
    r=w+1-s.

Then U_(w,s)=D(h_(w,s))(r). Here 1≤r<k/2, since

    w-s=3+i-j≥0,
    2r-k=w-2s=i-2j-4≤-1.

Thus these are genuine noncentral critical twists of modular representations. The weights are 12 through 15. Kato's noncentral results apply; they are not assertions about the seed's characteristic-zero rank dropping in its own representation.

## 2. The residual Selmer group remains the seed's

At p the filtration specializes to

    A_(w,s)=Z_p(alpha_w^(-1)chi^(w+1-s)omega^(s-w)),
    M_(w,s)=Z_p(alpha_w chi^(-s)omega^s).

The cyclotomic exponent of A is r≥1; that of M is -s≤0. The residual characters remain alpha-bar^(-1)chi-bar and alpha-bar, with alpha-bar≠1. Their local H^0 and H^2 vanish, integrally as well as residually. The rational Bloch–Kato finite subspace is H^1(A[1/p]): its dimension is one, while the finite subspace for M[1/p] is zero. This also follows from the ordinary critical-range local comparison and the absence of exceptional eigencharacters.

LOCAL_REVIEW.md makes H^1(A) a saturated rank-one submodule of H^1(U); hence the integral finite condition is exactly its image. The same residual local condition is the ordinary Kummer condition for E[p]. For discrete coefficients, invariants of the relevant graded modules vanish, so propagation and taking p-torsion introduce no extra local class. This proves the p-local residual comparison without assuming any rational basis point is locally primitive.

At the bad q≠p, the retained residual H^0 and H^1 vanish outside the recorded finite exceptions, also on the dual side. The same residual representation is present at every new specialization. The compact and discrete local comparisons therefore remain valid. At other q≠p the representations are unramified and the propagated finite condition is unramified. These are precisely the away-from-p arguments in the retained VERIFIED_DERIVATION.md, now applied to the same residual module.

Let B_(w,s) be the propagated discrete Bloch–Kato Selmer group of U_(w,s). Kato's noncentral theorem gives its finiteness. The residual control just proved gives

    B_(w,s)[p]=Sel_p(E/Q),
    0 -> W_p -> B_(w,s)[p] -> Sha(E/Q)[p] -> 0,
    dim W_p=2.

No finiteness of the seed's Sha is assumed here.

## 3. Use the index of this actual Euler system

Specialize the integral arithmetic family Z_p(r) of ARITHMETIC_SOURCE.md in the weight direction, retaining the full cyclotomic variable and all auxiliary conductors. This is an integral Euler system. Recenter the cyclotomic variable at s. If its singular specialization z has nonzero image, set

    b^Z_(w,s)=length_Zp(Q_(w,s)/Z_p loc_p^s z),
    Q_(w,s)=H^1(Q_p,U_(w,s))/H_f^1(Q_p,U_(w,s)).

If the image is zero, write b^Z_(w,s)=infinity. The local Coleman isomorphism gives, whenever finite,

    b^Z_(w,s)=v_p(F_p(t_w,t_s)).                         (I1)

This is a lattice index, not a valuation obtained by replacing a period by an arbitrary rational de Rham basis.

## 4. Integral Euler-system bound, with specialization terms

The Steinberg place 2243 still has tame conductor one at every specialization: residual ramification excludes conductor zero. The finite Dirichlet twists above are unramified there. An inertia element is a unipotent with unit off-diagonal entry because its residual action is nontrivial. Its cokernel on the lattice is free of rank one, and it belongs to the cyclotomic kernel. This verifies the integral transvection condition of Kato 13.4(3).

Apply the Euler-system inequality to the specialized system itself. A nonzero value at the point being tested makes its cyclotomic component nonzero. If a full Delta-system nonvanishing hypothesis is used, fill the other components by the integral idempotent combination of standard modular systems described in retained VERIFIED_DERIVATION.md §3.3, without changing the tested component. The local Iwasawa H^2 term is zero: over Q_p(mu_(p^infinity)) the dual graded residual characters are the nontrivial unramified characters alpha-bar and alpha-bar^(-1).

On that cyclotomic component write H_Iw=Z_p[[X]]e, z_Iw=Fe, and M=H^2_Iw. The integral height-one bound is

    length_P M ≤ length_P(H_Iw/Z_p[[X]]z_Iw).

This is the usual Euler-system inequality for the genuine system, not an assumed primitive-Kolyvagin-system equality. Global irreducibility and the retained lattice comparison give the rank-one integral H_Iw used here. The noncentral Kato results supply finite H^2 and rank-one H^1 at the point.

Retain the specialization exact sequence and its Tor term:

    0 -> H_Iw/X -> H^1(Q,U_(w,s)) -> M[X] -> 0.

Put a=length(H^1/Z_p z), h=length H^2, and t=length M[X]. If a0 is the index in H_Iw/X, then a=a0+t, and the specialized height-one inequality gives h-t≤a0. Therefore h≤a. This is the cancellation in the retained proof, applied to the new system. It does not specialize a three-dimensional characteristic ideal while discarding pseudo-null error.

The integral Poitou–Tate sequence and the noncentral equality of the orders of the dual Bloch–Kato groups give

    length B_(w,s)=b^Z_(w,s)-a+h≤b^Z_(w,s).

Subtract the two-dimensional W_p and use B[p]/W_p as a subspace of (B/W_p)[p]. We obtain

    dim_Fp Sha(E/Q)[p] ≤ b^Z_(w,s)-2.                   (I2)

This repeats the necessary arithmetic part of the retained index proof for these new points. It does not assume equality or an integral ratio between this class and the old normalized z_g.

## 5. Consequence

For each of the ten points, a nonzero value modulo p^4 forces b^Z≤3. Retained even parity then forces Sha[p]=0, hence Sha[p^infinity]=0. Equivalently,

    F_p(t_w,t_s) not in p^4 Z_p => Sha(E/Q)[p^infinity]=0. (I3)

The conclusion concerns the original seed. It does not concern only the higher-weight forms. Supersingular p and the fixed finite excluded primes are not covered.
