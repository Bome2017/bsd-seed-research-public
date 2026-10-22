# The actual experiment: seed-localized lifting and a sparse dual forcing certificate

Status: **PROPOSED GLOBAL CONSTRUCTION**, with the local coefficient construction implemented. No global seed matrix, lift, or dual certificate has been produced in this session.

## 1. Fixed target, not a generic family

Use the seed

    y^2=x^3-x^2-66020924x-65074271436,
    N=6503188012738584.

Use p=31 first. Exact counting gives a_31=-8 and the ordinary root alpha_0=57776 modulo 31^4. This checks good ordinarity, not the retained Hida/source theorem's exceptional-domain hypotheses.

Construct the specialization through this eigenform. Do not select a convenient other form, an arbitrary member of a residual eigenspace, or an independently rescaled numerical eigenvector. Retain the appropriate sign and tame character throughout.

The initial weight-zero distribution-valued ordinary symbol Xi_0 is not merely its scalar classical moment. Its higher distribution moments must be obtained by justified ordinary control/lifting. A few previously computed classical symbols do not uniquely specify all its required divisor values without a reconstruction argument.

## 2. Independently fixed equations

Work with an actual arithmetic Manin/coset presentation for Gamma_0(Np), or prove an equivalent localized presentation. Let D(T) be its relation operator, and H_q(T) actual Hecke operators on the coefficient module; include the U_p ordinary condition. Their weight dependence comes from

    K_gamma(z,T)=(1+T)^L_gamma(z),

whose coefficients and mixed precision are implemented in the accompanying module. Do not apply the non-semigroup Manin generators naively to the primitive chart.

Write

    Xi(T)=sum_(n>=0) Xi_n T^n,
    a_q(T)=sum_(n>=0) a_(q,n) T^n,
    D(T)=sum D_n T^n,
    H_q(T)=sum H_(q,n) T^n.

The coefficients a_(q,n) for n>0 are unknowns. They cannot be set equal to the weight-two eigenvalues. All equations below arise by expanding

    D(T)Xi(T)=0,
    H_q(T)Xi(T)=a_q(T)Xi(T).

Choose a fixed integral source functional nu with nu(Xi_0) a unit and normalize nu(Xi(T))=1. Such a functional must be exhibited from the primitive seed source. Neither q-expansion normalization a_1=1 nor the central symbol at a rank-two zero supplies this normalization automatically. If the inspected older modular-symbol table supplies a suitable evaluation, bind its lattice and period evidence before using it.

## 3. A reusable bordered linear system

At weight order n=1,2,3, all lower-order data are already known. Set the correction unknowns to x=Xi_n and b_q=a_(q,n). Define the bordered operator

    J(x,(b_q)) = (D_0 x,
                  ((H_(q,0)-a_(q,0))x-b_q Xi_0)_q,
                  nu(x)).

Its required right-hand side is

    relation component:  -sum_(r=1)^n D_r Xi_(n-r),
    q-component:         -sum_(r=1)^n H_(q,r) Xi_(n-r)
                         +sum_(r=1)^(n-1) a_(q,r) Xi_(n-r),
    normalization:       0.                                         (L_n)

This is an inhomogeneous construction: the forcing terms come from the already identified seed and explicit coefficient-action derivatives. They are not chosen after observing a desired W3 value.

The same base operator J occurs at all three orders; the right-hand side changes. The moment precision at order n is p^(4-n-j). Work in a common integral presentation before reducing to those weighted quotients, or prove the equivalent weighted lifting statement. Do not discard a p-torsion relation merely because it disappears at one precision.

This observation does not prove J has a unit inverse. Simplicity of the localized branch, absence of relevant congruence defects, ordinary control, and compatibility of integral lattices must be proved or independently certified. If more than one branch survives, retain that algebra and its coordinates rather than arbitrarily declaring rank one. A finite-quotient eigenvector is not automatically a liftable family symbol.

## 4. Avoid the full ambient matrix when possible

The first computational target is not a basis for all modular symbols at level Np. It is a certificate for one of the four specific functionals.

For a desired row v, seek a finite-support dual row lambda such that

    lambda J = v                                                    (D)

in the actual, correctly normalized presentation and at the required precision. Then every genuine solution to (L_n) has

    v(x,(b_q)) = lambda RHS_n.                                      (C)

Equation (D) must be checked exactly with all cusp/coset identifiers and coefficients. It cannot be a fit to observed data or a relation checked only on the known Mordell-Weil subspace. Its finite support must close in the actual presentation; omitted tail columns must be zero or have their precision bound proved.

A source-specific implementation may generate the support incrementally using Hecke correspondences and the existing seed symbol oracle. If it grows too large, preserve the concrete support, equations and unsolved columns. Do not replace a measured resource failure with a theorem that no short certificate exists.

A dual identity computes a source value only after the existence and arithmetic identity of the genuine Xi are established. It can avoid computing its entire coordinate vector; it cannot replace that existence/comparison theorem.

The first ambitious goal is to compose these dual identities through orders one, two and three so that a four-value functional becomes an explicit inhomogeneous expression in authenticated base-source data and the independently determined eigenvalue corrections. Showing that this expression has valuation <=3 would finally constrain the actual Kato index.

## 5. The discriminating experiment

Produce one authenticated p=31 source computation, either a complete enough common-frame moment table or the sparse dual certificates that evaluate the required functionals. For the four pairs, report V modulo 923521, not merely V/p^2 modulo 31. Keep any valuation-three outcome.

Then compare the independently derived forcing expression with the direct source functional. A mismatch is an arithmetic/convention failure, not a candidate BSD counterexample. Agreement on toy assignments is not sufficient. The functional's identity must hold on the actual seed source.

All four zero modulo p^4 is an inconclusive W3 bound at that precision. It is still a genuine source computation if authenticated. It does not establish nonzero Sha or failure of BSD. Nonzero modulo p^4 yields the retained pointwise implication only after domain hypotheses are checked.

Use the already certified p=17 material solely for orientation, lattice and reproducibility controls. Do not turn this into a new singleton-witness prime sweep.

## 6. From a source experiment to a uniform bound

The desired new arithmetic information is the forcing expression in (C), not simply the existence of a primitive symbol. Investigate whether its numerator/content can be independently controlled as p varies.

One sufficient result would be a proved formula, for a selected one of the four functionals at each ordinary p outside a fixed finite set,

    V_(w,s),p = p^e u_p c  (mod p^4),
    e in {2,3}, u_p a proved unit, c a fixed nonzero integer,

with all normalization and exceptional factors specified. This is a possible outcome, not an assumed law or an assertion that every uniform method must have this form. A direct uniform inequality would be equally useful.

Finite samples cannot establish the formula. A matrix fitted after seeing source values cannot establish it. Proving a unit determinant for the local coefficient module or for J does not establish it either: the forcing vector could still have vanishing image.

If a sparse dual identity is found but its forcing term has uncontrolled valuation, preserve the identity as a source-evaluation result and name precisely the new valuation problem. Do not relabel it a bound.

## 7. Exact scope

A uniform success here is initially an ordinary-prime result. It does not cover infinitely many supersingular primes just because the BFR receiver does. It also does not settle excluded bad primes or the fixed exceptional components.

To claim seed FIN and ORDER9, combine independently proved primary vanishing at every p>=5 with the retained full 2- and 3-primary certificates. Cofinite vanishing alone still requires full-primary finiteness and orders at every exception. The exact analytic identity Q36 is not supplied by this experiment.
