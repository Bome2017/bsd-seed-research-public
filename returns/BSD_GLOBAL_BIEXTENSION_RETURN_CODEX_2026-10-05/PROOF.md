# Global biextension construction: the line, its realizations, and the attempted modular lift

2026-10-05. Written derivations, under the expressly retained arithmetic and geometric inputs below. Not human peer review, formal verification, or a novelty claim.

**Status: NO_GLOBAL_SCALAR_CONSTRUCTED.** The requested Neron side can be made precise. Neither the raw biextension operation nor its repaired quadratic carrier constructs the required modular section. This is a result about the constructions actually attempted, not a nonexistence theorem.

## 1. Domain and retained inputs

We use

\[
E:y^2=x^3-x^2-66020924x-65074271436,
\quad P_1=(-3031,327384),\quad P_2=(-2394,281520).
\]

The saturated basis, rank two, rational torsion of order two, Tamagawa product 16, residual image, and the Ota implication retain their existing grades. They are not proved by the controls in this return.

`context/G2_PROOF.md` and its review supply the fixed normalized Poincare fibers, their integral identity-component extension, and G2. `context/THEOREM_W_REPAIRED.md` supplies fixed-p auxiliary independence, including the composite-symbol repair and the fixed period convention. We use the common cofinite domain

\[
p\notin S_*:=\{2,3,5,19,59,487,2243,4547,5843\}.
\]

There is no ordinary-only condition here. An admitted singleton auxiliary prime satisfies the hypotheses of W, including \(p\nmid\#E(\mathbf F_\ell)\). G2 supplies choices with \(\operatorname{Frob}_\ell=-I\), hence \(a_\ell-2=-4\pmod p\), and nonzero production regulator \(R_{p,\ell}\). Every use of G2 below is at that retained theorem grade.

## 2. Explicit rational Poincare fibers before p is chosen

Put \(Q_i=16P_i\). These points belong to the identity component at every finite place, by the retained Tamagawa data. Let \(\mathcal L=\mathcal O_E(O)\), with the rigidification from the minimal parameter \(t=-x/y\). Choose the principal-polarization sign convention in which

\[
\mathcal P=m^*\mathcal L\otimes\mathrm{pr}_1^*\mathcal L^{-1}
 \otimes\mathrm{pr}_2^*\mathcal L^{-1}\otimes\mathcal L_O.
\tag{2.1}
\]

This is the usual square construction of the rigidified Poincare bundle. It follows from the theorem of the square and the universal property of the dual variety; see Milne, *Abelian Varieties*, Sections 9–10. Reversing the polarization sign negates the pairing matrix and leaves its rank-two determinant unchanged.

Let \(s\) be the canonical section of \(\mathcal O_E(O)\), and let \(e_0\) be its rigidifying frame at O. None of \(Q_i,Q_j,Q_i+Q_j\) is O, so the expression

\[
r_{ij}=s(Q_i+Q_j)\otimes s(Q_i)^{-1}\otimes s(Q_j)^{-1}\otimes e_0
\tag{2.2}
\]

is an explicit nonzero rational element of \(\mathcal P(Q_i,Q_j)\). This formula gives a section of the fiber, not a number obtained by evaluating the vanishing section s at O.

Write \(d(Q)>0\) for the square root of the denominator of x(Q) in lowest terms. Under the retained cubical extension/identity-component normalization in G2 Section 4.2, the finite valuation of s(Q) is \(v(d(Q))\). Tensoring (2.2) therefore gives

\[
n_v(r_{ij})=v(d(Q_i+Q_j))-v(d(Q_i))-v(d(Q_j)).
\]

Consequently the rationally specified normalized fiber section is

\[
 r_{ij}^0=\frac{d(Q_i)d(Q_j)}{d(Q_i+Q_j)}\,r_{ij}.
\tag{2.3}
\]

Its finite unramified Neron valuations are all zero. The integral model assertion used here is the retained G2 input, including at the bad primes; the rational-coordinate check is not a new proof of that model assertion. The numbers in (2.3) are recorded exactly in `checks/CONSTRUCTION_RESULTS.json`. Two separate implementations agree on the seven rational points used to compute them. The sections are constructed from the points and the line bundle before selecting either p or ell.

As in G2, any two rational lifts with all finite Neron valuations zero differ by ±1. This ambiguity is killed by an odd-order tame character. The fixed 1-motive retaining the four fibers is already constructed in G2 Section 3; constructing these sections does not supply its missing Mazur–Tate comparison.

## 3. Why the raw tensor determinant has the wrong realization

Consider the literal line

\[
\mathcal P(Q_1,Q_1)\otimes\mathcal P(Q_2,Q_2)
 \otimes\mathcal P(Q_1,Q_2)^{-1}\otimes\mathcal P(Q_2,Q_1)^{-1}.
\tag{3.1}
\]

The two biextension laws identify (3.1) with \(\mathcal P(Q_1-Q_2,Q_1-Q_2)\). In additive tame coordinates its section has value

\[
B_{11}+B_{22}-B_{12}-B_{21}.
\tag{3.2}
\]

The requested regulator instead uses \(B_{11}B_{22}-B_{12}B_{21}\). Tensor product adds tame logarithms; it does not multiply them. More generally, a fixed tensor-power expression in these fibers gives an integer linear combination of their tame coordinates. Under simultaneous multiplication of the points by n it scales by n², whereas the determinant scales by n⁴. This rejects that class of tensor recipes, not every possible higher geometric construction.

Nor can one subtract the two tensor sections before identifying their different fibers. An arbitrary identification would not fix the issue: a tame logarithm of a difference of scalar products is not the difference of products of tame logarithms.

The retained seed calibration at p=17, ell=103 gives, on Q_i=16P_i and with primitive root 5,

\[
B=\begin{pmatrix}15&10\\10&6\end{pmatrix}\pmod {17}.
\]

Expression (3.2) is 1; det(B) is 7. This calibration was replayed using rational points, denominator divisors, and tame logarithms. It is not a new primary certificate.

## 4. A rational torsor ratio does not have the asserted scalar action

For a local Poincare splitting, the actual equivariance law is

\[
b_v(c r)=\chi_v(c)+b_v(r), \qquad c\in\mathbf Q_v^\times,
\tag{4.1}
\]

where \(\chi_v\) is the chosen additive character of the multiplicative group. This is Definition 2.2(a) of Tan, in additive notation. It is not \(\overline c\,b_v(r)\).

An exact control on the same seed fiber makes the distinction explicit. Fix the rational integer c=131072=2^17. At p=17, ell=103 it has zero tame character, because it is a seventeenth power, but c reduces to 2 modulo 17. Thus a fiber value 15 stays 15 under multiplication by c, whereas the incorrectly asserted scalar rule gives 13.

Globally the distinction is stronger: the product of local splittings is passed to an idele-class quotient. A rational change of lift is principal and vanishes there. Hence the global height pairing does not depend on that change of rational lift. This is the well-definedness in Tan, Definition 2.6. If both lifts are also required to retain the all-finite Neron normalization, their ratio was only ±1 to begin with.

This does not disprove the proposed endpoint for a correctly constructed **linear** determinant realization. It shows that such a realization must be constructed separately. Triviality of a rational line over Q and existence of its section ratio alone do not give it. In particular one cannot deduce cofinite unitness of the height image merely from finite prime support of that ratio.

## 5. Repair: the primitive integral quadratic determinant carrier

Let \(L=\mathbf ZP_1\oplus\mathbf ZP_2\), modulo torsion, and put

\[
D=(\wedge^2 L)^{\otimes2},\qquad
\omega=(P_1\wedge P_2)^{\otimes2}.
\]

This is an integral rank-one module, not the G_m torsor in (3.1). It has a canonical primitive map

\[
j:D\longrightarrow\operatorname{Sym}^2(\operatorname{Sym}^2 L),
\quad
j(\omega)=(P_1^2)(P_2^2)-(P_1P_2)^2.
\tag{5.1}
\]

Here inner and outer symmetric products are distinct operations. To verify canonicity, take U=aP_1+bP_2 and V=cP_1+dP_2. Expanding in the three inner monomials gives

\[
(U^2)(V^2)-(UV)^2=(ad-bc)^2\big((P_1^2)(P_2^2)-(P_1P_2)^2\big).
\]

Furthermore multiplication \(\operatorname{Sym}^2(\operatorname{Sym}^2L)\to\operatorname{Sym}^4L\) sends six basis monomials onto the five quartic monomials; the only repeated image comes from \((P_1^2)(P_2^2)\) and \((P_1P_2)^2\). Its integral kernel is exactly the primitive rank-one image of j. No division by 2 is hidden in (5.1).

For any symmetric bilinear pairing h valued in a commutative ring, the induced linear map on this symmetric square sends j(omega) to det(h(P_i,P_j)). For a group-valued height one first lands in the symmetric square of that group and then its augmentation quotient or the specified finite-field character coordinate.

Apply this to the retained B matrix on Q_i. G2 proves

\[
\det B(Q_i,Q_j)=4\cdot16^4 R_{p,\ell}.
\]

Thus we obtain an honest reduction-linear regulator map on a fixed integral lattice,

\[
\rho_{p,\ell}:D\otimes\mathbf Z[1/2]\longrightarrow\mathbf F_p,
\qquad
\rho_{p,\ell}(\omega)=\frac{\det B(Q_i,Q_j)}{4\cdot16^4}=R_{p,\ell}.
\tag{5.2}
\]

The target scalar action in (5.2) is reduction of \(\mathbf Z[1/2]\), not a nonexistent Q-linear map to F_p. A rational section can be reduced at primes not dividing its denominator by extending this lattice accordingly.

This explicitly supplies the correctly typed Neron section \(\tau_{\rm Ner}=\omega\). It is not a novel global carrier: `context/HISTORICAL_LINE_SEP18.md`, Sections 4 and 6, already uses the squared Mordell–Weil determinant and names its unproved modular comparison LINE. Only that precise historical collision is retained; that older file's stronger general insufficiency claims are not imported.

## 6. The actual Mazur–Tate class and the attempted rational lift

Use the frozen production period and the smallest primitive root g modulo ell. Set \(x(a)=\operatorname{ind}_g(a)\bmod p\), represented from 0 to p-1. After projection to the degree-p cyclic quotient, write X=gamma-1. The actual symbol expansion is

\[
\theta_\ell=\sum_a [a/\ell]^+ (1+X)^{x(a)},\qquad
C_2(p,\ell)=\sum_a\binom{x(a)}2[a/\ell]^+\pmod p.
\tag{6.1}
\]

The lower two coefficients vanish on the retained theorem domain. This is a class in I²/I³, with its fixed generator convention, rather than a characteristic-zero coordinate in D.

At p=17, ell=103, exact recombination of all 102 **previously identified** plus symbols gives c_0=0, c_1=7242 and c_2=46298. Hence the residual class is 7X². The stored analytic identification and corpus were not rerun; their input hash matches the retained receipt. Together with the replayed R=6 and a_ell=-2,

\[
\frac{C_2}{(a_\ell-2)R}=\frac7{(-4)6}=16\pmod {17}.
\tag{6.2}
\]

This agrees with 288 mod 17. It constructs just the retained residual section \(16\omega\), not a unique rational section. Infinitely many nonzero rational coefficients have that residue.

### Attempt A: rationalize the finite-level quadratic class

For a finite group G over Q, let \(e=1-|G|^{-1}\sum_{g\in G}g\). The augmentation ideal is eQ[G], e²=e, and therefore I²=I³=I. In particular

\[
(I_{\mathbf Z[G]}^2/I_{\mathbf Z[G]}^3)\otimes\mathbf Q=0.
\tag{6.3}
\]

Applying this operation to (6.1) loses the nonzero residual class; it cannot produce the required nonzero rational section. This rejects rationalizing a finite augmentation quotient, not all possible motivic lifts of integral modular symbols.

### Attempt B: retain all integral levels and use W

For each p, W and G2 define a unique w_p by the ratios at nonzero regulators. On the repaired line they give \(\tau_p=w_p\omega\in D/pD\). They do not supply a rational preimage of this family.

More precisely, consider reduction of rational sections, interpreted outside their finite denominator support,

\[
 D\otimes\mathbf Q\longrightarrow
 \left(\prod_{p\notin S_*}D/pD\right)\big/\left(\bigoplus_{p\notin S_*}D/pD\right).
\tag{6.4}
\]

The map is injective: if two rational coefficients agree modulo every prime outside a finite set, their nonzero difference would have infinitely many numerator divisors. It need not be surjective. As an elementary control, a family taking value zero on one infinite set of primes and one on a disjoint infinite set is not the reductions of a rational number. This control is not a claim about the seed's actual w_p.

The attempted inverse image of \((\tau_p)_p\) under (6.4) is the exact remaining construction. We have no proof that it is nonempty, nor that its possible preimage is nonzero. Choosing 288 times omega would merely assume all the unproved comparisons. Fixed-p auxiliary independence and finite CRT matches cannot supply this inverse image. This recovers the historical LINE obligation without asserting that every possible uniform proof must go through it.

### Attempt C: use the retained determinant/BKS or U22 comparison

The repaired W proof explicitly retains a local determinant scalar X in Z_p. Its no-finiteness proof treats the possible nonzero-Sha branch separately; it does not create a common rational X. This proof must not be replaced by inserting a unit, an algebraic BSD constant, or the desired Sha order.

BKS II Section 2.1 defines the algebraic constant under full Sha finiteness; Theorem 4.1 imports the algebraic generalized Perrin–Riou conjecture. These are not unconditional ways to define the required section here. The current Bullach–Honnor manuscript, Remark 1.8(b), also explicitly distinguishes its split-multiplicative leading-term theorem from the finer positive-rank regulator comparison. Its theorem cannot fill this rank-two gap.

U22's retained corrected Link-2 review preserves a boundary coefficient carrying C2 but supplies no map evaluating it on these fixed Poincare fibers. It specifically corrects the confusion between an off-diagonal corner product and a scalar trace-cycle ideal. We did not invent such a missing map or assume its normalization. These source checks do not prove all future geometric comparisons would collapse to TNC/BSD.

## 7. The exact valid payoff, and what this pass did not obtain

If one independently constructs a nonzero \(\tau_{\rm MT}=Z\omega\in D\otimes\mathbf Q\) such that

\[
\rho_{p,\ell}(\tau_{\rm MT})=C_2(p,\ell)/(a_\ell-2)
\]

cofinitely with the same lattice and conventions, then reduction-linearity of (5.2) proves the desired formula. Outside numerator and denominator primes of Z and S_*, G2 and Ota then prove \(\Sha[p^\infty]=0\). This implication covers ordinary and supersingular good primes on the retained domain. Exceptional-primary finiteness, ORDER9 and Q36 remain separate.

The repaired construction supplies (5.2), not tau_MT. It supplies no independent nonzero rational scalar, no bound on w_p, and no new vanishing prime. Equations (3.2) and (4.1) explain why the literal torsor-ratio construction does not fill this gap automatically. Equation (6.4) records the remaining lift accurately; naming that map is not counted as progress through uniform FIN.
