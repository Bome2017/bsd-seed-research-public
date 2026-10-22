# A cyclotomic 5-tower consequence and a one-table quadratic extractor

2026-10-12. Baseline: `Bome2017/bsd-seed-lab@0e8bb6859d1391e6d449b1ef02aff2cfd85310f1`.

**Grade: WRITTEN_DERIVATION_UNDER_RETAINED_ARITHMETIC_INPUTS.** The small exact replay is executed; the global argument is not formally verified or independently reviewed. No novelty claim is made.

## 1. Objects, inputs and distinct conclusions

Retain

\[
 E=[0,-1,0,-66020924,-65074271436],\qquad
 N=6503188012738584.
\]

The retained seed has rational rank two, torsion Z/2, good ordinary reduction at 5 with a_5=-2, and surjective mod-5 representation. The old 5-primary certificate supplies exact normalized-newform modular symbols at denominators 5 and 25. Their original numerical certification, denominator theorem and large Fourier-coefficient corpus are retained, not regenerated here. The two small tables are copied byte-for-byte and their Git blob identities verified.

The current source review fixes the standard ordinary measure using the minimal Neron real period, the ordinary unit root, and U=gamma-1. Here gamma corresponds to 1+p. For the seed Omega_E=2 omega_1; the retained tables use omega_1, so their entries must be divided by 2 for this standard measure.

There are two different outputs:

**DERIVED, seed-specific:** for Q_n the degree-5^n layer of the cyclotomic Z_5-extension of Q,

\[
 \operatorname{rank}E(Q_n)=2,\qquad
 \Sha(E/Q_n)[5^\infty]=0\quad\text{for every }n\ge0.       \tag{T}
\]

**DERIVED, general finite-precision formula:** a raw quadratic moment from the single modular-symbol denominator p^n determines the standard ordinary quadratic coefficient modulo p^(n-1), without a lower-denominator table. This is an executable extraction rule, not a bound on the resulting arithmetic value.

Statement (T) concerns one coefficient prime in infinitely many field layers. It is not cofinite control of coefficient primes over Q. It does not include the other tame character components in the full fields Q(mu_(5^(n+1))). FIN, ORDER9 and Q36 over Q remain unchanged.

## 2. The actual p=5 numerator replay

Use the complete 20-row `inputs/SYMBOLS_m25.txt`. The Teichmuller lifts modulo 25 are 1,7,18,24, and gamma=6. In the group-ring basis gamma^j, summing over the four Teichmuller representatives gives the raw vector

\[
 (-76,0,-76,76,76),\qquad 0\le j<5.
\]

Its constant, linear and quadratic U-coefficients are respectively 0,380,608. An independent discrete-log implementation gives the same quadratic moment. The Neron-normalized raw quadratic moment is therefore 304.

The ordinary unit root satisfies alpha=3 mod5. Using the exact measure formula in Stein--Wuthrich, Section 3.1, and either the original two-table formula or Section 4 below,

\[
 [U^2]L_{\mathrm{std},5}\equiv alpha^{-2}\cdot304
 \equiv1\pmod5.                                      \tag{R}
\]

The full lower table has total augmentation zero. Its transfer contribution vanishes modulo 5; it is included in the independent two-table replay. All four plus Hecke T_5 relations pass exactly. Thus (R) is recovered from actual saved seed symbols, not fitted from the expected Sha value or a synthetic model.

**Precision boundary.** This table determines the infinite coefficient only modulo 5. Hensel-lifting alpha to many digits does not turn the same finite-layer table into a many-digit value of the infinite coefficient. The nonzero finite approximant linear coefficient 380 is not the infinite linear coefficient. Exact vanishing below degree two follows in Section 3 from the rational-point submodule and Kato divisibility, not from rounding the finite approximant.

This is a new replay of an old residue. It is not a new symbol computation, a new coefficient digit, or a new base-field primary-vanishing result.

## 3. From the unit numerator to the entire cyclotomic 5-tower

### 3.1 General unit-leading-term proposition

Let A/Q be an elliptic curve and p>=5 a good ordinary prime. Put Q_infinity equal to the cyclotomic Z_p-extension, Gamma=Gal(Q_infinity/Q), Lambda=Z_p[[Gamma]], and U=gamma-1. Let

\[
 \mathscr S=\varinjlim_n\operatorname{Sel}_{p^\infty}(A/Q_n),
 \qquad X_{\rm cyc}=\mathscr S^\vee.
\]

These are the usual p-infinity Selmer groups and restriction transition maps. In particular, X_cyc is **not** the full-S Iwasawa H^2 module used in the Bockstein packets.

Assume:

1. A(Q)[p]=0 and rank A(Q)=r.
2. X_cyc is a finitely generated torsion Lambda-module, and its characteristic generator f divides the specified integral ordinary series L in Lambda.
3. The coefficient [U^r]L is a p-adic unit.
4. X_cyc has no nonzero finite Lambda-submodule.

Then restriction identifies

\[
 \mathscr S=A(Q)\otimes\mathbf Q_p/\mathbf Z_p,
 \qquad X_{\rm cyc}\simeq(\Lambda/(U))^r,              \tag{V}
\]

and, for every n>=0,

\[
 \operatorname{rank}A(Q_n)=r,\qquad
 \Sha(A/Q_n)[p^\infty]=0.                            \tag{W}
\]

No p-adic height nondegeneracy, finite-level Sha finiteness, or main-conjecture equality is an assumption of this proposition.

### 3.2 Proof of the proposition

First A[p^infinity](Q_infinity)=0. Indeed, a nonzero space A[p](Q_n) is a nonzero finite F_p-representation of the finite p-group Gal(Q_n/Q). Such a representation has nonzero invariants, contradicting A(Q)[p]=0. The same reasoning applies at every finite layer, and every torsion point over Q_infinity is defined at one such layer. Higher p-power torsion would yield p-torsion by multiplication.

Inflation--restriction now gives an injection

\[
 H^1(Q_n,A[p^\infty])\hookrightarrow
 H^1(Q_\infty,A[p^\infty])                            \tag{I}
\]

for every n. Restriction preserves the Selmer local conditions. In particular the base-field Kummer subgroup

\[
 W=A(Q)\otimes\mathbf Q_p/\mathbf Z_p
   \simeq(\mathbf Q_p/\mathbf Z_p)^r
\]

injects into S. Gamma acts trivially on it. Pontryagin duality therefore supplies a surjection of Lambda-modules

\[
 X_{\rm cyc}\twoheadrightarrow W^\vee
          \simeq(\Lambda/(U))^r.                     \tag{Q}
\]

Characteristic ideals are multiplicative in exact sequences of finitely generated torsion Lambda-modules. Thus U^r divides f. By assumption 2, U^r divides L as an actual integral power series. Assumption 3 then implies

\[
 L=U^r u,\qquad u\in\Lambda^\times,
 \qquad (f)=(U^r).                                  \tag{C}
\]

In particular mu(X_cyc)=0 and lambda(X_cyc)=r. The structure theorem for finitely generated torsion Lambda-modules now makes X_cyc a finitely generated Z_p-module of rank r: it is pseudo-isomorphic to a finite direct sum of Lambda/(U^a), of total Z_p-rank r, with only finite kernel and cokernel.

The Z_p-torsion of X_cyc is finite and Lambda-stable. Assumption 4 forces it to be zero. Consequently X_cyc is free of Z_p-rank r. The surjection (Q) is between two free Z_p-modules of the same rank; its kernel has rank zero and is a submodule of a torsion-free module. Its kernel is therefore zero. This proves (V), including the trivial Gamma action. It is stronger than a pseudo-isomorphism.

For each n, (I) injects Sel(A/Q_n) into S. Its image contains the restricted base-field Kummer subgroup W, which by (V) is all of S. Thus restriction is an isomorphism. The Kummer subgroup A(Q_n) tensor Q_p/Z_p of Sel(A/Q_n) already contains W, so it is the whole Selmer group. The usual Kummer exact sequence then proves Sha(A/Q_n)[p^infinity]=0, with no prior finiteness assumption. Comparing coranks proves the rank assertion in (W).

This proof does not assume a surjective integral Mazur control map with discarded local errors. The injections come from the vanishing of global p-power torsion, and surjectivity follows from the already exhaustive base-field point subgroup.

### 3.3 Arithmetic inputs to the proposition for the seed

**THEOREM INPUT, ordinary Kato divisibility.** Stein--Wuthrich, Section 6.1 and Theorem 7.3, state the torsion property and integral divisibility f | L for good ordinary p with full p-adic representation. Their Proposition 7.2 supplies full p-adic image from full mod-p image for p>=5. Only the good ordinary case is used; no claim about the more delicate nonsplit multiplicative extension of the statement is needed.

The seed has good ordinary reduction at 5, full residual image at 5 and rational rank two, as retained in the old certificate. Hence assumptions 1 and 2 hold for the actual ordinary Selmer group and standard series. The current source review also authenticates the standard measure's period at 5. Equation (R) supplies assumption 3, with r=2.

**THEOREM INPUT, finite-submodule exclusion.** Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:math/9809206v1, Proposition 4.14, printed pp.52-53, gives: cotorsion of the cyclotomic Selmer group together with vanishing of the base-field p-primary torsion excludes proper finite-index Lambda-submodules of that discrete Selmer group. Pontryagin duality translates this exactly to assumption 4. Its two hypotheses have already been checked here. The published chapter is in LNM 1716 (1999), pp.51-144; the proposition was checked in the author's arXiv text, including a rendered image of its statement.

We can therefore apply (V)-(W), obtaining the seed conclusion (T) and the integral module identification

\[
 \boxed{X_{\rm cyc,5}\simeq(\mathbf Z_5[[U]]/(U))^2.}  \tag{S}
\]

The input is the old exact numerator unit plus published Iwasawa structure, not an assumed rank-two BSD formula. No height determinant is required for this particular unit-leading case.

### 3.4 Why the finite-submodule theorem is indispensable

Characteristic ideal (U^2) alone allows

\[
 X_{\rm bad}=(\Lambda/(U))^2\oplus\Lambda/(p,U).
\]

The last summand is finite and invisible to height-one characteristic ideals. A less visibly split example is the Z_p-module Z_p e_1 + Z_p e_2 + F_p f, with U e_1=f, U e_2=U f=0. It also has characteristic (U^2), and its U-coinvariants are Z_p^2, yet it has nonzero finite torsion. Thus even free base coinvariants would not by themselves justify the torsion-free step above.

Conversely, Lambda/(U^2) has no finite submodule and the right characteristic ideal, but it does not admit the surjection (Q) for r=2. The rational point subgroup is also essential. The proof uses both pieces, not just mu=0 and lambda=2.

These are abstract module controls, not realizations of the seed. They isolate exactly the extra theorem and point map used to eliminate finite errors.

## 4. A single-denominator quadratic numerator extraction

### 4.1 Definition and hypotheses

Let p>=5 be ordinary, alpha its unit root, and n>=2. Use the same standard plus-symbol normalization and gamma=1+p. Define q_n=p^(n-1) and

\[
 \Theta_n(U)=\sum_{a=1}^{p-1}\sum_{j=0}^{q_n-1}
 [\omega(a)(1+p)^j/p^n]^+ (1+U)^j,
 \qquad A_n=[U^2]\Theta_n.
\]

Rational arguments are reduced modulo p^n; omega is the Teichmuller lift modulo that denominator. Theta_1 is constant. Assume the normalized raw symbol coefficients at the layers used are p-integral, and that the ordinary measure is the specified integral measure. On the retained seed's good-prime domain this is the modular-symbol integrality input, compatible with the reviewed image-lattice and Manin units. Integrality is a hypothesis of the general extraction proposition; finite numerical shape checks alone cannot establish it for an unauthenticated source.

Write L_2=[U^2]L_std. Then

\[
 \boxed{L_2\equiv(1-p/alpha^2)alpha^{-n}A_n
                \pmod {p^{n-1}}.}                   \tag{M}
\]

Since the multiplier is a unit, a nonzero residue of A_n modulo p^(n-1) determines the valuation of L_2 exactly. For a valuation-only test, neither a lower-denominator table nor a computed alpha is needed. For the actual coefficient residue, the multiplier and period convention must still be applied.

### 4.2 Proof with the transfer and precision error retained

Let

\[
 \nu_n(U)=\sum_{k=0}^{p-1}(1+U)^{kp^{n-2}}.
\]

The ordinary distribution formula of Stein--Wuthrich Section 3.1 gives the exact finite projection

\[
 P_n=alpha^{-n}\Theta_n-alpha^{-n-1}\nu_n\Theta_{n-1}.
                                                               \tag{F}
\]

These are degree <q_n polynomials representing the image of the same infinite measure in Z_p[Gamma/Gamma^(p^(n-1))]. Therefore L_std-P_n belongs to the ideal generated by (1+U)^(q_n)-1. The coefficients of this generator in degrees one and two are q_n and binom(q_n,2), both divisible by p^(n-1). We obtain

\[
 [U^2]P_n\equiv L_2\pmod {p^{n-1}}.                  \tag{E1}
\]

This is the quadratic specialization of the usual finite-level precision bound; it is also immediate by Weierstrass division in Z_p[[U]].

The constant coefficient of nu_n is p. Its linear coefficient is p^(n-2) sum k, divisible by p^(n-1). Its quadratic coefficient is

\[
 \tfrac12\left(p^{2n-4}\sum k^2-p^{n-2}\sum k\right),
\]

also divisible by p^(n-1), using p>=5. Hence

\[
 [U^2](\nu_n\Theta_{n-1})\equiv p A_{n-1}
                                      \pmod {p^{n-1}}.           \tag{E2}
\]

The integrality assumption matters in multiplying these coefficients. Set B_n=alpha^(-n)A_n and t=p/alpha^2. Combining (F), (E1), (E2) gives

\[
 B_n=L_2+tB_{n-1}+O(p^{n-1}),\qquad B_1=0.
\]

Inductively,

\[
 B_n=L_2(1+t+\cdots+t^{n-2})+O(p^{n-1}).
\]

Multiplication by 1-t proves (M), because v_p(t)=1 and L_2 is integral. Thus the missing lower table is not simply discarded: its contribution is eliminated using compatibility and the precision cost is explicit.

### 4.3 The precision is sharp for integral measures

Put q=p^(n-1). The integral series

\[
 F_0=qU^2,\qquad
 F_1=qU^2+(p-1)U((1+U)^q-1)
\]

both vanish below degree two and have identical projection at this finite group-ring level. Their quadratic coefficients are q and pq. Thus this projection alone cannot, in general, distinguish valuations n-1 and n, even with exact order-at-least-two information. This is an integral-measure countercontrol, not a claim that both series arise from the seed. Additional arithmetic can improve precision, but the finite projection itself does not.

### 4.4 Consequence for the retained p=17 target

Retain the matched value r_17=v_17(det H_17)=1; it was read from earlier evidence, not recomputed here. Formula (M) gives the following adaptive target for the standard series:

- n=2, denominator 289: only L_2,17 mod17. Under the retained ratio lower bound this is forced to vanish and cannot settle the target.
- n=3, denominator 4913: a nonzero A_3 mod17^2 proves valuation exactly one (under the retained lower bound), so the ratio is zero.
- If that residue is zero, n=4, denominator 83521: a nonzero A_4 mod17^3 can prove valuation two and ratio one, which still suffices by the reviewed parity certificate.

These are cyclotomic modular-symbol denominators, not the auxiliary tame primes of the separate Ota certificates. The n=3 and n=4 seed tables were not recovered or computed in this pass. No claimed absence from every branch is inferred from the scoped search.

The proof removes lower-layer inputs from the extractor, not the high-conductor Fourier work needed to create the top table. It provides no runtime speedup claim for the existing streaming engine and no nonvanishing guarantee.

## 5. Review boundary

The check script reproduces (R), validates the historical table hashes, tests the exact moment formula in 84 synthetic compatible cases, and includes precision and malformed-input controls. It does not prove Kato's theorem, Greenberg's finite-submodule theorem, the original symbol certification or the seed's residual-image/rank input.

The tower result requires review of Section 3, particularly the use of the ordinary Selmer group, the characteristic-ideal direction, the no-finite-submodule hypothesis, and the injection of the base-field point group. The moment formula requires review of the layer indexing and integrality in (E2). No independent reviewer or proof assistant has checked this new return.

The established base-field prime set and FIN/ORDER9/Q36 are unchanged. Statement (T), if accepted at this retained-input grade, is an extension of known seed arithmetic in the field direction, not the missing theorem across coefficient primes.
