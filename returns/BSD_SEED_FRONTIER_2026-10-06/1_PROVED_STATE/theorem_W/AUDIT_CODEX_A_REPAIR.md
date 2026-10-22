# A: repaired proof of auxiliary-prime independence

Date: 2026-09-29. Written deduction at the retained arithmetic and imported-theorem grades. This replaces the composite-production identification in WORKING_2, Step 3; the input files remain unchanged.

## Statement

Put B* = {2,3,19,59,487,2243,4547,5843}. Let p be a prime outside B*, and let l and q be distinct primes with gcd(lq,pN)=1, l=q=1 mod p, p not dividing #E(F_l)#E(F_q), and both production tame regulators nonzero modulo p. Use one period, one saturated Mordell–Weil basis, and matching discrete-log and group-ring generators. Then

    C2(p,l)/((a_l-2)R_(p,l)) = C2(p,q)/((a_q-2)R_(p,q)) in F_p.

There is no full-Sha finiteness hypothesis. At p=5 this is a comparison for pairs satisfying the displayed conditions; G2's retained infinitude theorem excludes 5 and is not being extended here.

## 1. Removing the global-finiteness assumption from this particular use of BKS

The printed BKS II §2.1 assumes that the whole Sha(E/Q) is finite. Consequently, citing (27) without explanation under a weaker hypothesis is insufficient. The following p-primary adaptation supplies the explanation, rather than changing the source's stated hypotheses.

If Sha(E/Q)[p] is nonzero, Ota Theorem 6.4, contrapositively, makes every eligible C2 zero. This branch is finished. Ota's argument does not assume finiteness; its Selmer groups include a possible divisible contribution.

Otherwise Sha(E/Q)[p^infinity]=0: any nonzero p-primary torsion group contains a nonzero element of order p. In this branch the Kummer and Selmer-duality identifications give

    H^1_f(Q,T) = Z_p tensor E(Q) = Z_p^2,
    H^2_f(Q,T) = Sel_(p^infinity)(E/Q)^vee = (Z_p tensor E(Q))^*.

These assertions concern the p-primary part alone. They do not concern Sha at any other prime.

Let F=F_l F_q and R=Z_p[C_p x C_p]. BKS Hypothesis 2.2 gives the perfect Selmer complex and its base change (§§5.2–5.3). BKS Lemma 4.2 constructs the determinantal Kato element from the equivariant Stark/Kolyvagin-system comparison under Hypothesis 2.2; neither its argument nor the evaluation in Corollary 5.3 uses the algebraic BSD element. In particular, the equality with that algebraic element in (28) is not invoked.

Here is an elementary verification of the part of Proposition 5.4 needed in this branch. Represent the Selmer complex by the two equal-rank free R-modules supplied in Proposition 5.2. Its augmentation has free kernel and cokernel of rank two. Over Z_p choose bases splitting the augmented differential into an invertible block and a zero 2-by-2 block, and lift these bases to R. R is local, so the invertible block remains invertible. Its Schur complement is a 2-by-2 matrix with entries in the augmentation ideal I. Its determinant lies in I^2, and modulo I^3 is the determinant of its linear terms, times the augmentation of the invertible-block determinant. Those linear terms give the connecting/Bockstein map. BKS uses its negative; rank two makes the determinant sign positive. This is precisely the leading-term diagram of Proposition 5.4 in the present torsion-free branch.

The remaining determinant-line scalar lies in the single rank-one module

    Z_p tensor (exterior^2 E(Q) tensor exterior^2 E(Q))
      = Z_p (omega tensor omega).

Thus Corollary 5.3 and this diagram give, for this one compositum,

    theta_(F,S) = X R_F in I^2/I^3,       X in Z_p.                 (A1)

This proves the required p-primary version of (27). It imports the arithmetic complex, Kato-element existence, and Bockstein/Mazur–Tate identification from the named sources. It is not a reproof of those foundations. It assumes neither Sha(F) finite nor a unit Kato coordinate. The group C_p x C_p is permitted: it is abelian of p-power order, and no cyclic-group step occurs here.

## 2. Exact repair at composite conductor

Write Theta_m for the raw production sum and D_m for its regularization in the SAME period convention. Darmon's §2.3.1 defines regularized symbols, not raw symbols. Since the seed has L(E,1)=0, his definition at m=lq gives exactly

    D_(lq) = Theta_(lq)
       - ((q-1)/p) N_q sigma_q Theta_l
       - ((l-1)/p) N_l sigma_l Theta_q,                         (A2)

after projection to C_p x C_p. Here N_l and N_q are the respective group norms; a singleton sum is embedded in its own factor; sigma_q is q in the l-factor, and conversely. The omitted divisor-1 term is zero because its symbol is L(E,1) divided by the fixed period. Formula (A2) also follows directly by grouping the regularization sum into CRT fibers.

The assertion in the return that Darmon's composite element is just the raw sum times a fixed period constant is therefore false literally. It is not enough to say that Ota enters only at singleton level: Step 3 explicitly uses the raw composite sum from WORKING_1.

The required repair is nevertheless exact. Modulo p, with x=gamma_l-1 and y=gamma_q-1,

    N_l = x^(p-1),       N_q = y^(p-1).

Ota gives Theta_l and Theta_q augmentation order at least two. Both corrections in (A2) therefore have total augmentation degree at least p+1, so

    D_(lq) = Theta_(lq) mod (p,I^3).                           (A3)

This needs only p>=5 and l,q=1 mod p, not exact valuation one.

BKS's theta_(F,m) is D_m times the fixed period/Manin-conversion factor. Its (10) now applies to the correct element. Explicitly,

    Eul_N theta_(F,m) = u theta_(F,S),
    u = (1+((l-1)/p)N_l)(1+((q-1)/p)N_q).

This is integral, has augmentation lq, and is a unit. Eul_N has augmentation c_N=product_(r|N) #E^ns(F_r)/r, a p-unit. A multiplier acts on I^2/I^3 by its augmentation. Combining (A1)–(A3), and absorbing the common period conversion and the regulator factor 4, proves the raw degree-two identity claimed in Step 3. No exact equality of the two full composite sums is claimed.

## 3. A second, shorter proof avoiding composite production symbols

This is also a check on the normalization repair. Put

    E_q = 1-(a_q/q)sigma_q^(-1)+(1/q)sigma_q^(-2).

CRT gives tau_(lq)(chi)=-chi(q)tau_l(chi) for every character inflated from the l-factor. BKS's defining interpolation (3) therefore gives the exact projection

    pi_l(theta_(F,S)) = -sigma_q E_q theta_(F_l,S_l).           (A4)

The augmentation of this multiplier is -#E(F_q)/q, reducing to a_q-2 modulo p. At singleton conductor the regularization's divisor-1 term is zero. Accordingly theta_(F_l,S_l)=c_per Eul_N Theta_l, with one fixed period-conversion p-unit c_per, the same for l and q. For the retained production least-real-period versus total-Neron-period convention, c_per=1/2.

Naturality of the augmentation extension and the Bockstein map gives pi_l(R_F)=R_(F_l). Both relevant E_S lattices become the same Z_p tensor E(Q), since their local indices are p-units. In the retained G2 normalization R_(F_l)=4R_(p,l)T_l^2. Equation (A1) then gives

    (a_q-2)c_per c_N C2(p,l) = 4 Xbar R_(p,l),
    (a_l-2)c_per c_N C2(p,q) = 4 Xbar R_(p,q).

Dividing gives the same ratio

    4 Xbar / (c_per c_N (a_l-2)(a_q-2))

on both sides. This proves the plus sign with no comparison between independently chosen Kato scalars.

## 4. Local projection and conventions

At an eligible good l, multiplication by p is invertible on the formal group and the reduction group, hence E(Q_l) is p-divisible. The difference between the valuation of the tame splitting and the Neron splitting descends to a homomorphism E(Q_l) to F_p and is zero. Thus the local valuation contributes nothing to the other, unramified degree-p factor. This validates the local proof in WORKING_1, given its retained pairing constructions. Alternatively the Bockstein naturality argument above suffices. No division by the extension degree p occurs.

The joint generator change cancels between C2 and the regulator. A mismatched change gives a square factor; it is WRONG to add 'never a sign': -1 is a square when p=1 mod 4. At p=5, s=2 gives s^(-2)=-1. A period change scales every ratio by a common constant; equality survives, but the numerical ratio is not period-invariant. The same saturated basis, reciprocity and period must be used throughout.

The image hypothesis, including p=5, is an explicitly retained odd-residual-surjectivity input in G2 §1, not a new image proof here. The non-anomalous condition at p>=7 follows from rational 2-torsion and Hasse; the retained p=5 count is 8. The bad nonsingular point counts give precisely the additional exclusions 19,59,487.

## 5. Verification and limits

The two supplied 389a1/p=7 checks were replayed in this output folder. Five pairs agree, with both types of negative controls rejected. A new exact 389a1 check evaluates the regularization directly and verifies (A2), rejects equality of raw and regularized full sums, and verifies (A3). These are calibration checks, not seed certificates.

The mixed-coefficient experiment uses the assembled regulator from Step 2; it does not independently test that arithmetic pairing identification. The original sign control contains a permissive zero-projection disjunct. A strict additional check confirms that the actual projection is nonzero and the opposite sign fails in this example.

This establishes fixed-p auxiliary independence at retained/imported-input grade. It supplies neither a cross-prime rational scalar, its value 288, nor its nonvanishing. No p^k extension is established here.
