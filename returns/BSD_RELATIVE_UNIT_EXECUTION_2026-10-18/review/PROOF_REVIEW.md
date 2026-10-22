# Independent review of the relative-unit admission argument

Date: 2026-10-18
Status: MATHEMATICAL_ADMISSION_ARGUMENT_SUPPORTED; NO_CANDIDATES_ADMITTED_IN_BOUNDED_EXECUTION.

Scope: a separate agent checked the following deductions from the pinned actual field/action and current contract. This is a written mathematical review, not a formal proof or an independent recertification of the number-field construction, residual-image theorem, or Dirichlet-character dimension. No broad arithmetic search or BNF was run by this reviewer.

## 1. Exact ideal test

Let A be the actual degree-48 point field, O its full ring of integers, and tau its scalar-minus-one automorphism. Let I be a nonzero integral O-ideal. Require all of:

1. tau(I)=I as integral ideals, checked in the same maximal-order basis;
2. alpha is a nonzero element of I;
3. |N_{A/Q}(alpha)|=N(I), as exact integers.

Membership gives (alpha) contained in I. Since both are integral ideals, the finite index [I:(alpha)] is N((alpha))/N(I). The equality of norms makes this index one, so (alpha)=I. This argument uses the absolute value of the element norm, not its sign.

It follows that epsilon=alpha/tau(alpha) has principal fractional ideal I/tau(I)=O. Therefore epsilon and epsilon^{-1} are algebraic integers: epsilon is an ordinary unit. Moreover tau(epsilon)=epsilon^{-1}, so N_{A/A^tau}(epsilon)=1 exactly.

The same conclusion should additionally be checked by independently constructing the principal ideal of alpha and comparing its HNF to I. This is redundant mathematically but useful for implementation admission. Relative norm one alone is insufficient: valuations can cancel between tau-paired primes. Approximate norm equality is also insufficient.

## 2. No faithful unit component is lost by the relative formulation

Put E=O^*/(O^*)^7, written additively. The map u -> u/tau(u) is (1-tau) on E and lands in ordinary relative norm-one units. On either faithful scalar character of F_7^*, tau acts as -1. Consequently (1-tau) acts as 2, invertible in F_7.

Thus images of relative norm-one units span the entire faithful unit component: passing to relative units is a legitimate source restriction. It does not assert that a particular finite relative-unit search finds a spanning set.

There is also an explicit unrestricted representation by the admitted form. Given an ordinary norm-one unit epsilon != -1, set alpha=1+epsilon. Then alpha is a nonzero algebraic integer and tau(alpha)=epsilon^{-1} alpha. Thus (alpha) is tau-stable and alpha/tau(alpha)=epsilon. For epsilon=-1 the class modulo seventh powers is already zero. This proves completeness of the form when all invariant principal ideals and generators are allowed, not completeness of the bounded list of fourteen ideals or of the weighted search. It cannot be used to compute an unknown epsilon or bound search height.

Central-odd is necessary but not sufficient. There is also a central-odd nonfaithful character. Each admitted unit still needs the exact order-six scalar-character projection used by the existing norm/local engine. No division by an algebraic integer or rational power is permitted to manufacture that projection; integral group-ring exponents representing the projector modulo seven suffice.

If tau(alpha)=alpha or tau(alpha)=-alpha, epsilon is respectively 1 or -1, both seventh powers. Such generators are excluded before claiming faithful source progress. Mixed alpha is necessary for this construction but does not guarantee a nonzero faithful class or a nonzero image under the constraints.

## 3. What an accepted result can bound

Retain the audited complete faithful ordinary-unit dimension four. If admitted units have constraint images of rank r in the actual global-norm plus required local-condition map, then the rank of that map on the whole unit component is at least r. Hence its complete unit kernel has dimension at most 4-r. A fundamental-unit basis is not required for this one-sided bound.

A zero image on a finite list yields no upper bound on the unseen unit kernel beyond four. A nonzero unit as a field element is not sufficient; the actual faithful projected row image must be calculated and its rank authenticated.

The complete ordinary class contribution remains separate. With the previously audited zero valuation allowance, the whole-source expression is (4-r_U)+(c-r_C). Relative-unit production does not bound c or r_C and does not replace the ordinary class group by an S-class quotient. No seed or uniform-prime consequence follows solely from a successful control source.

## 4. Why the previous 24 orbits cannot simply be reprocessed

The pinned finite source has a divisor matrix D with 144 independent columns. The central automorphism permutes these columns by J. The divisor matrix of alpha/tau(alpha) is D(1-J), so injectivity of D implies ker D(1-J)=ker(1-J). Those kernel elements pair a ratio with its inverse and produce one. This exact finite-family failure is preserved. New elements or genuinely changed ideal search geometry are required.

## 5. Required prospective algorithm checks

The producer must record the invariant ideal, its exact norm, the maximal-order lattice, the central action matrix, and the archimedean weights. For a claimed change in geometry, the selected weight/Gram form must not commute with the central action; simply renaming an unweighted LLL search is insufficient. Mixed vectors must be allowed and exact admission remains independent of the floating-point reduction.

A numerical LLL failure, a search timeout, or failure to find a generator is a computational boundary. None proves that an invariant ideal is nonprincipal or that relative units do not exist.

The official PARI documentation describes rnfisnorm as solving an individual relative norm equation using an S-integer search containing class-group-generator data. Calling rnfisnorm(1) is not a substitute for constructing a relative-unit basis; one is already a trivial solution. No such shortcut is assumed here.

Source: https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#rnfisnorm (checked 2026-10-18).
