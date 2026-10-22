# Referee-ready algebraic lemmas and failed shortcuts

All proofs here are ordinary mathematical proofs, not Lean certificates. **FORMALIZABLE_NOW** marks finite algebraic content. No novelty claim is made.

## A. Finite augmentation quotients do not survive direct rationalization

Let G be a finite group of exponent e, R=Z[G], and I its augmentation ideal. For every r>=1,

    e I^r is contained in I^(r+1).

Indeed, for g of order dividing e, write g=1+x. Expanding (1+x)^e=1 gives ex in I^2. The elements g-1 generate I as an abelian group, hence eI is contained in I^2. Multiply by I^(r-1). Therefore I^r/I^(r+1) is finitely generated and killed by e, and is finite. After tensoring with Q it vanishes. Equivalently, the rational augmentation ideal is idempotent: in Q[G], 1-|G|^(-1) sum_g g is an idempotent generator.

Consequences: a fixed conductor S, or any finite list of conductors, can have higher augmentation information only at finitely many primes. Simply rationalizing each finite group ring cannot recover the desired characteristic-zero leading term.

**Scope correction.** This does not show that inverse limits contain no characteristic-zero information. For a procyclic pro-p tower, the completed augmentation quotient is Z_p and becomes Q_p on rationalization. Nor does it exclude geometric or derived lifts. It identifies why rationalization cannot be interchanged with completion. Statements that a product of finite groups has “no rational line” should be replaced by this precise finite-stage assertion.

## B. Global lattice descent is stronger than local finite generation

Let d=(d_p) in product_p Z_p with d_p != 0 for every p. Then the following are equivalent:

1. d_p is a unit for all but finitely many p;
2. there exists a nonzero A in Z with A in d_p Z_p for every p;
3. product_p (Z_p/d_p Z_p) is a finite group;
4. multiplication by d becomes an isomorphism after inverting all nonzero integers in product_p Z_p.

Proof: (1) gives A=product of p^v_p(d_p) over the finite nonunit set. (2) confines that set to prime divisors of A. Under (1), the product in (3) has finitely many nontrivial finite factors; if infinitely many are nontrivial the product has arbitrarily large finite quotients. For (4), an inverse has a common integer denominator exactly when the nonunit valuations can be cleared by a single A; this is (2). QED.

A perfect complex over Z with rationally acyclic cohomology has finite cohomology: its cohomology is finitely generated over Z and torsion. A perfect complex over product Z_p, even rationally acyclic separately at each p, does not have that implication. WC's counterexample d_p=p^2 shows the difference, while preserving local even lengths.

This is a conditional descent criterion, not an assertion that the seed's Selmer defect already descends to a rationally acyclic perfect Z-complex. Finite exceptional support plus finite primary groups would be sufficient; rationality of all unit parts is extra structure.

## C. The strict-line obstruction does not forbid a determinant source

Let V be two-dimensional over a field K, ell:V->K a nonzero linear functional, and D=exterior^2 V. Define

    i_ell(v1 wedge v2) = ell(v1) v2 - ell(v2) v1.

This is a K-linear isomorphism D -> ker(ell). For any v with ell(v)!=0, its inverse sends kappa in ker(ell) to

    (v wedge kappa)/ell(v).

Proof: in a basis P1,P2, write ell_i=ell(P_i). The contraction of P1 wedge P2 is ell_1 P2-ell_2 P1, a nonzero kernel vector. Both spaces are one-dimensional. For v=aP1+bP2, its wedge with that vector is (a ell_1+b ell_2)(P1 wedge P2)=ell(v)(P1 wedge P2). This also proves independence of v. QED.

Apply formally with K=Q_p and ell=log_p. A rational determinant omega can produce a strict vector with transcendental coefficient ratio. Thus the H9 coefficient gate does **not** obstruct this type of source. But extracting omega from an actual H9 class gives c_p omega, with c_p still unknown. The lemma establishes neither integrality, bounded content, nonvanishing of the H9 class, nor cross-prime or archimedean compatibility. Before local finiteness, identifying the relevant Selmer space with V=E(Q) tensor Q_p is itself an arithmetic input.

## D. Rational reconstruction at an integer

Let q=a/b be rational in lowest terms, b>0, and m an integer. If b<=D and |q-m|<=epsilon with D epsilon<1, then q=m. Otherwise the nonzero integer a-mb has absolute value at least 1, giving |q-m|>=1/b>=1/D>epsilon.

For the rigorously enclosed seed, m=36 and epsilon=573/100000 suffice. The exact inequality is

    174 * 573/100000 = 99702/100000 < 1.

So den(q)<=174 forces q=36. A bound on the reduced denominator and a single specified common denominator are different hypotheses; either has this consequence at the displayed threshold. The former does not mean 174q is integral.

## E. Rationality is not the only possible arithmeticity certificate

Suppose q is algebraic, with primitive irreducible polynomial f in Z[X], degree d, leading coefficient a, and conjugates q=q_1,...,q_d. If

    |a| product_(j>1) |36-q_j| <= B,
    |q-36| <= epsilon, and epsilon B < 1,

then q=36. For if q!=36, f(36) is a nonzero integer (irreducibility rules out another conjugate equal to 36), while

    |f(36)| = |a| product_j |36-q_j| <= epsilon B < 1,

a contradiction. For degree one B is precisely the reduced denominator. A degree bound alone is insufficient; conjugate/height control is essential. This is an alternative sufficient certificate, **not** a new algebraicity theorem for L''/(2 Omega Reg).

## F. Finite p-adic digits cannot prove global rationality

Given positive real epsilon, prime p, and k, choose a positive integer b coprime to p with b>p^k/epsilon. Then

    q'=36+p^k/b

is a rational different from 36, with |q'-36|<epsilon and v_p(q'-36)>=k. Without a denominator bound even rationality plus arbitrarily prescribed finite p-adic precision fails to determine the value. If rationality is not known, a real interval contains irrational alternatives too; assigning a p-adic realization needs a proved comparison.

## G. Central-value algebraicity cannot be differentiated by itself

For any real c, f_c(s)=c(s-1)^2 is analytic, satisfies f_c(1)=f_c'(1)=0 and the even symmetry f_c(2-s)=f_c(s), but f_c''(1)/2=c. Thus algebraicity of a zero critical value and the functional-equation symmetry do not imply algebraicity of its second derivative. This is a counterexample to that inference, not a counterexample about modular L-functions.

Likewise, if L has a double zero and M is holomorphic at 1, (LM)'(1)=0 and (LM)''(1)=L''(1)M(1). A first-derivative identity specialized to this product loses the desired information. A meromorphic auxiliary factor with a pole can change the derivative order, but the needed regularized arithmetic identity then becomes an additional theorem. No exclusion of such a theorem is claimed.

## H. FIN does not determine the order

Subject to the retained p=3 theorem and FIN, the alternating Cassels–Tate pairing makes the odd-primary orders squares. Together with the solved 2-,3-,5-parts this gives

    #Sha = 9 t^2, with t a positive integer and gcd(t,30)=1.

Nothing in FIN alone forces t=1. For example, the abstract finite group (Z/3)^2 direct-sum (Z/7)^2 has the known primary parts and a nondegenerate alternating pairing, but order 441. It is a logical countermodel to the deduction, not asserted to occur for the seed.

All these algebraic proofs can be formalized separately from the analytic, Galois-cohomological, and Euler-system inputs. A formal proof of the implications would not establish their currently unknown arithmetic antecedents.
