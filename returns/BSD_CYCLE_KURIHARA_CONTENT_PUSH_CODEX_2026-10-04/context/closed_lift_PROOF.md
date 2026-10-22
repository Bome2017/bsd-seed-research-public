# Closed lifts and nonzero quadratic isogeny periods

Status: written derivation under the retained primitive-period input; independent review pending. This constructs actual closed modular-curve cycles, including the noninvariant lift missing from the preceding attempt. It does not identify them with the project's admissible BSD witnesses. Novelty is not assessed.

## 1. Precise target and domains

Let X=X_0(N), let z=z_E:H_1(X,Z)->Z be the retained elliptic period functional, and fix a good seed prime p>=5. The retained period image has index dividing 2. Normalize an integral cycle v modulo p so that z(v)=1 modulo p. All subsequent cycle identities and prescribed periods are modulo p, unless an integral statement is explicit.

The actual two-prime witness cycles in HOMOLOGY_SOURCE_THEOREM.md use products of discrete logarithms at admissible auxiliary primes. The actual Gross packets in C2_D_P_DERIVATION.md use the specified traced conductor-p^2 CM point. Neither definition allows replacing the underlying arithmetic packet by an arbitrary homology cycle.

We first construct a genuinely nonzero weighted period, then check this distinction. We do not assume a witness interpretation.

## 2. Prescribe two periods at level Np

Let Y=X_0(Np), with alpha forgetting the order-p subgroup and beta quotienting by it. Their integral homology pull-push relations have diagonal d=p+1 and off-diagonal T_p. The geometric differential convention is beta^* f(z)dz = p f(pz)dz. Thus the period matrix on transfers of v is

    [[d,a_p],[a_p,d]].

This is the previously audited prime-level degeneracy calculation, not a new period theorem. Its determinant Delta=d^2-a_p^2 is a p-unit for the seed. Rational 2-torsion gives even a_p; for p>=7 the Hasse interval contains no even integer congruent to +/-1 mod p; at p=5, a_5=-2.

Choose an integer u with u Delta=1 mod p and set

    C=u(-a_p alpha^*v+d beta^*v) in H_1(Y,Z).

Then

    z(alpha_* C)=0,       z(beta_* C)=1 mod p.             (1)

Both ordinary and supersingular good primes are covered.

## 3. A closed lift instead of the full transfer

Let Z_p be the compact modular curve associated to Gamma_0(N) intersect Gamma(p), where the ineffective sign is removed when passing to the analytic quotient. There are maps

    Z_p --pi--> Y --alpha--> X.

The cover pi has deck group B, the upper triangular subgroup of PSL_2(F_p). Its order is p(p-1)/2. This is not a prime-to-p cover, so dividing its transfer by its degree is invalid.

Nevertheless its pushforward on H_1(-,F_p) is surjective.

Proof of the group input: reduction of Gamma_0(N) modulo p is onto SL_2(F_p). Upper unipotents and lower unipotents with lower entry divisible by N give its two elementary generators because p does not divide N. The image of Gamma_0(Np) is therefore the upper triangular subgroup. Its unipotent radical U is additive F_p; diagonal t,t^-1 conjugates u(b) to u(t^2 b). For p>=5 choose t with t^2 !=1. The commutators therefore contain all of U. B/U has order dividing p-1, so B has no nonzero quotient of order p.

Proof of the homology statement: remove the finitely many branch values of pi and their preimages. The resulting connected regular cover has exact fundamental-group sequence

    pi_1(Z_p^o) -> pi_1(Y^o) -> B -> 1.

On abelianization, the cokernel of H_1(Z_p^o,Z)->H_1(Y^o,Z) is B_ab. After reduction modulo p that cokernel is zero. Compactification maps H_1(Y^o,F_p) onto H_1(Y,F_p), and the two pushforwards commute with compactification. Hence H_1(Z_p,F_p)->H_1(Y,F_p) is onto. This argument includes cusp and elliptic-point ramification; no unramified-cover assertion is made for the compact curves.

Choose D in H_1(Z_p,Z) with pi_*D=C modulo p. Such an integral representative exists because the homology of a compact Riemann surface is free. This is an existence construction by finite homology operations; no enormous homology matrix was computed.

There is also a loop-level recipe, without taking a full fiber sum. Represent C by based loops avoiding the branch values. For a loop gamma with monodromy g in B, put d=p-1; then g^d lies in U. Write g^d=u(b). Choose two based loops k,eta whose monodromies are diag(t,t^-1) and u(b/(t^2-1)); their commutator has monodromy u(b). The loop gamma^d[k,eta]^-1 therefore lifts closed. Its homology downstairs is d[gamma], since the commutator abelianizes to zero. Multiplying by an integer inverse of d modulo p gives the desired lift of [gamma]. Repeat on the finitely many loops in C. Existence of k,eta follows from connectedness of the punctured regular cover. This prescription proves the lift without dividing by a p-divisible degree.

Unlike the full transfer, D need not be deck-invariant. We have proved existence of a closed lift, not a rational section of the cover and not a distinguished CM cycle.

## 4. The p+1 actual quotient maps

The full marking on Z_p supplies maps beta_x:Z_p->X for x in P^1(F_p), by quotienting the varying elliptic curve by the marked line x. Label beta_infinity=beta composed with pi, and put a=alpha composed with pi.

These are algebraic maps of modular curves (a connected full symplectic marking may be viewed over Q(zeta_p)). The symbols x are actual marked torsion lines here, not invented CM labels.

The Hecke trace identity gives

    sum_x beta_x^* omega_f = a_p a^* omega_f.

For clarity, this identity follows by pulling the trace alpha_* beta^* omega_f=a_p omega_f from Y back to the normal marking cover, where its p+1 cosets are the p+1 lines. The differential factor p in beta^* is retained. Integration and taking the normalized real part yield, with

    v_x=z((beta_x)_*D),

    sum_x v_x=0,         v_infinity=1 mod p.              (2)

Consequently sum_{j in F_p} v_j=-1 mod p.

Choose the deck unipotent U so beta_j composed with U=beta_(j+1), and beta_infinity composed with U=beta_infinity. Choosing the inverse action instead only reverses both shifts in the calculation below.

## 5. The cancellation can be repaired on these cycles

Set D'=(U_*-1)^2D. For finite j put

    v'_j=z((beta_j)_*D')=v_(j+2)-2v_(j+1)+v_j,

with indices taken modulo p. Changing variables in each finite sum proves

    sum_j v'_j=0,
    sum_j j v'_j=0,
    sum_j j^2 v'_j=2 sum_j v_j=-2 mod p.                (3)

This is exact summation by parts over F_p: (j-2)^2-2(j-1)^2+j^2=2. Thus the actual integral cycle

    R_p=sum_{j=0}^{p-1} j^2 (beta_j)_*D' in H_1(X,Z)

satisfies

    z_E(R_p)=-2 mod p.                                 (4)

The quadratic weighted value is a unit at every good seed p>=5. Its zeroth and first moments vanish. This avoids the previous full-transfer cancellation by proving a closed noninvariant lift and weighting its second difference.

The prior formal projective identity can also be realized using these beta_x maps. It is unnecessary for (3): the two independently prescribed periods in (1) supply the required nonzero finite orbit sum directly.

## 6. What would connect (4) to the seed endpoint?

Equation (4) proves nonvanishing of a specified weighted isogeny-period construction. It is not a Kurihara number, the full BH degree-two coefficient at an admissible conductor, or the retained anticyclotomic Gross moment.

The distinction is in the input, not in an omitted unit: D was chosen from the homology lift of an oldform transfer combination. It is not the retained traced CM point, and its unipotent marking action is not identified with the required abelian Artin action. At two-prime modular-symbol levels, the weights must be the prescribed discrete-log weights on the complete arithmetic packet. Vanishing two lower moments does not establish either identification.

The implication toward uniform FIN would require an arithmetic comparison expressing z_E(R_p) in the ideal generated by the admitted witness values, with coefficients integral at p. That would force one such value to be a unit by (4). No such comparison is proved here. Restating this membership condition alone is not a new mechanism and is not a reason to start a campaign.

One direct attempt to reuse the same lifting matrix at Kato auxiliary primes also does not justify the comparison: there ell=1 and a_ell=2 modulo p, so the corresponding matrix [[ell+1,a_ell],[a_ell,ell+1]] is singular modulo p. This observation applies to that transfer formula only. It does not rule out using other cycles, level-raising congruences, or additional arithmetic structure.

No claim is made that the existence of (4) bounds Sha. The construction uses geometric period primitivity and ordinary Hecke correspondences, without any new control of Selmer classes. It applies equally at the seed's supersingular good primes but does not settle a new primary component.

## 7. Review obligations and status

The new step is the closed-lift argument in Section 3 and its use in Sections 4-5. Its independent mathematical review remains open. The proof is not formally verified and its literature novelty has not been screened.

The elementary controls check the Borel commutator formula, the finite-difference identity including wraparound, the oldform matrix inversion, and the supersingular case. They do not compute modular-curve homology, admissible seed witnesses, or Sha.

Outcome: CLOSED_LIFT_AND_WEIGHTED_PERIOD_DERIVED; ADMISSIBLE_WITNESS_COMPARISON_NOT_CONSTRUCTED. No new uniform BSD input is claimed. FIN, ORDER9 and Q36 are unchanged.
