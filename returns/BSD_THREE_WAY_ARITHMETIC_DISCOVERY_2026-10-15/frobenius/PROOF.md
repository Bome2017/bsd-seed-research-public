# A fixed degree-nine Kummer extension explains the mirror failures

Grade: new written arithmetic deduction with exact executable source checks, plus forty sealed fresh predictions. This is not a seed upper bound and not a formal proof-assistant certificate. The coefficient prime is 3 throughout. The mirror curve has rank zero and bad reduction at 3; it is a discriminating control, not the rank-two seed.

## 1. The fixed source and the fixed norm

Let E be y²+y=x³−21x−27 and let K=Q(E[3]). Its full GL₂(F₃) image is retained and independently checked in ../incidence_review/image_check.gp: the point-field polynomial is irreducible and its Galois group has order 48. The eight point-field embeddings are the eight nonzero points of E[3]. Hence K contains μ₃ and [K:Q]=48.

The degree-eight point field has polynomial

    f_A(w)=w⁸−4w⁷−17w⁶+12w⁵+270w⁴+33w³−1101w²−1218w+3945.

Use the exact saved source generators G₁,…,G₁₁ and fix

    a = G₇ G₈ G₉ G₁₀ G₁₁².

This choice predates this experiment: it spans the mirror's scalar-plus-all-local kernel. It has zero valuation boundary, nonzero ordinary class coordinate, and no point component because the mirror has rank zero. Old additivity blocks and the full saved joint system exclude it. We do not call it a Selmer class.

`construct_norm.gp` reconstructs the short coordinates X=x, Y=y+1/2 and the source generator w as a rational polynomial in Y. Write m=z/6, where

    f_B(z)=z⁸−54432z⁴+4992192z²−246903552.

The three points on an affine line of E[3] missing zero have coordinate algebra B[X]/(G), B=Q[z]/f_B, with

    G=X³−m²X²+(m⁴−42)X−m⁶+42m²−107,
    Y=mX−(m⁴−21)/(2m).

The code verifies the original field relation, both point coordinates, and the exact 3-division polynomial relation. Thus this is an actual affine line of three distinct nonzero 3-torsion points; their sum is zero by the chord law. The eight slope embeddings give all eight affine lines missing zero.

Define b=Norm_{B[X]/G / B}(a(w(X,Y))). This is one fixed algebraic number. Its eight rational coefficients are given exactly in `norm.json`; the complete nested algebra is in `affine_norm_certificate.gp`. A second checker recomputes this norm as the determinant of its 3×3 multiplication matrix. In particular, b is not fitted from the observed prime outcomes.

For every nonzero torsion point P, denote its conjugate source value by a_P. The literal source tau identities give

    a_P a_{−P} ∈ K×³.

All eleven original identities were replayed, and `odd_cube_certificate.gp` contains a literal cube root for the selected a·tau(a). This step is essential: it makes the following odd-module calculation valid for actual arithmetic elements, not just for formal residue rows.

## 2. Why exactly two norm values suffice

Let Q be the four-dimensional F₃ vector space with formal generators e_P for nonzero P∈E[3], modulo e_{−P}=−e_P. It maps Galois-equivariantly to K×/K×³ by e_P↦[a_P].

For an affine line L missing zero, put n_L=Σ_{P∈L} e_P. Its image is the Kummer class of the corresponding conjugate b_L. On representatives (1,0),(0,1),(1,1),(1,−1), the four odd line-incidence rows form

    N = [1  0  1  1]
        [0  1  1 −1]
        [1  1 −1  0]
        [1 −1  0 −1].

Over the integers NNᵗ=3I and the Smith factors are 1,1,3,3. Over F₃ its row space I has dimension two. It is a GL₂(F₃) submodule of Q. The independent checker in `../incidence_review` verifies all 48 actions and directly checks that none of I's four projective lines is invariant. Thus I is irreducible. It separately checks the value-module action, so no silent identification of point and line representations is used.

If P,Q are independent torsion points, the two affine triples

    (P,Q,−P−Q),    (P,−Q,−P+Q)

give a basis of I. Their residues are the two defects

    χ(a_P)+χ(a_Q)−χ(a_{P+Q}),
    χ(a_P)−χ(a_Q)−χ(a_{P−Q}).

Here χ is any fixed cubic-residue coordinate in F₃ at a good completely split prime. An odd function on E[3] has four coordinates; the displayed two equations force its values on P+Q and P−Q from its values on P,Q, hence force full linearity. Therefore all 32 retained nonzero-sum additivity rows vanish if and only if these two conjugate norm values are cubes.

This criterion uses two evaluations of the polynomial b(z). It does not need the eleven-generator character matrix. It still requires the source torsion coordinates to identify the two chord slopes. It is an exact formula for the selected source, not a claim that any two arbitrary auxiliary primes suffice.

## 3. The exact Kummer extension and its degree

Let V_a be the span of all eight conjugate norm classes [b_L] in K×/K×³. It is the image of the irreducible two-dimensional module I. Consequently dim V_a is either zero or two.

The distinction is settled by actual arithmetic at q=18757, not by declaring b noncube in B. The point polynomial has the eight distinct roots

    12428,12677,12827,13417,13474,14553,15790,17380 (mod 18757).

Hence q splits completely in K. At the selected line embedding z=8881,

    b(z)=4376 (mod 18757),
    4376^6252=14673 ≠1 (mod 18757).

The norm is a unit at that place. If b were a cube in K, its cube root would reduce to an element of F_q, contradicting this residue. Thus b is noncube in K itself. This is stronger than noncubicity in the degree-eight line field: the latter alone would be inadequate because [K:B]=6 is divisible by 3. The complete arithmetic is in `NONCUBE_WITNESS.json` and is recomputed by `validate_predictions.py`.

It follows that dim V_a=2. Let

    M=K(cube roots of b_L for every affine line L).

Kummer theory now gives Gal(M/K)≅(Z/3)² and [M:K]=9. The generating Kummer subspace is stable under Gal(K/Q), and μ₃⊂K, so M/Q is Galois. Therefore [M:Q]=432. We have defined this field by its actual arithmetic generators and proved its degree; we have not computed a degree-432 absolute polynomial or its discriminant.

The external theorem used here is the standard Kummer correspondence and its degree formula: Milne, *Fields and Galois Theory*, Theorem 5.30 and Remark 5.32, printed pp.75–76. The primary PDF was freshly read: https://www.jmilne.org/math/CourseNotes/FT.pdf .

## 4. An exact density and forty prospective predictions

Outside the finite ramification/denominator set, let q split completely in K. All conjugate b_L are cubes mod q if and only if Frobenius in Gal(M/K) is trivial. Therefore

    selected false source passes a split-prime block
    ⇔ q splits completely in M.

Chebotarev gives density 1/432 for splitting completely in M and 1/48 for splitting completely in K. Thus the relative density of auxiliary primes missing this false class is exactly

    (1/432)/(1/48)=1/9.

Detection has relative density 8/9. This is a relative density among completely split primes, not among all rational primes. It gives no effective bound for the next detecting prime and no independent or random-trial assertion about successive primes. The standard density theorem was freshly read in Milne, *Algebraic Number Theory*, Theorem 8.31 and its splitting corollary, printed pp.147–149: https://www.jmilne.org/math/CourseNotes/ANT.pdf .

The selected mirror local kernel was already exactly the line generated by a. Thus these Frobenius states explain the varying mixed repair outcome for that fixed local problem. They do not change the local repair or replace it with a scalar fit.

The prospective experiment was sealed in `PREDICTIONS.md` and `SEAL.json` before fresh outcomes. It selected the first 40 eligible split primes greater than 47653, ending at 63127. The predictor evaluated only two b-values per prime and saved `NORM_PREDICTIONS.json`; its hash was sealed before the source character calculation.

It predicted survival at exactly 51439,56701,58237. Independent evaluation of all eleven source generators at all eight embeddings, and all 32 additivity rows at each prime, confirmed every prediction. This is 3,520 fresh source characters and 1,280 rows. The exact b-values also equal the independent products over the corresponding three source embeddings. All 72 prior calibration cases agree. These counts validate the implementation; the density follows from the theorem, not from the fraction 3/40.

The old contrast is now arithmetic: at 18757 the two norm values are (4376,461), with cubic coordinates (1,0); at 19219 both selected norm values (18889,11223) are cubes. Equal matrix ranks at those primes concealed different Frobenius states of one fixed extension.

### One fixed polynomial states the same law

After the prospective test, I eliminated z from f_B(z) and X³−b(z). The primitive integer resultant P(X), saved in `splitting_polynomial.gp.data` and `.json`, is irreducible of degree24. An exact minimum-polynomial check gives [Q(b):Q]=8, so b generates B. The faithful action on the eight affine lines implies that the normal closure of B is K. Hence the splitting field of P is exactly M, rather than an unspecified extension containing it.

This gives a single fixed-polynomial criterion: among eligible q splitting in K, the false source survives if and only if P splits completely modulo q. Outside its discriminant, a nontrivial element of Gal(M/K) is a nonzero linear functional on V_a. Exactly two of its eight nonzero norm classes lie in its kernel. Thus P has24 roots at a miss and exactly6 roots at a detecting prime. All forty previously selected primes avoid the polynomial discriminant and satisfy this sharper root-count law. This is a post hoc exact re-expression of the already tested law, not a second prospective experiment. No degree432 polynomial or heavy number-field computation was needed; the degree24 resultant took2 ms.

## 5. The point and genuine-excess controls delimit the result

`check_genuine_controls.gp` independently replays the exact multiplication-matrix norm and literal cube roots for:

* the two admitted unit classes of 1913b1, a rank-zero full-image good-at-3 positive control whose retained source theorem and rank certificate give two genuine Sha[3] classes;
* the seed's two point images and two retained cubic images, which give the known positive four-class source span at coefficient 3.

All six norms are literal cubes already in their degree-eight line fields. This replay does not reprove the global/local source-admission or rank theorems. Those are retained inputs, with paths bound in `SOURCE_BINDINGS.json`.

Consequently the corresponding norm Kummer modules are zero. Every eligible split-prime additivity test passes both point classes and genuine excess classes. This is an exact blindness statement, supported by the source formula and the actual cube roots; increasing the number of auxiliary primes cannot make this detector separate these two kinds of admitted class.

The new result is an arithmetic explanation and prospective predictor for **false-candidate admission**, replacing an unexplained variation of matrix orientation by a fixed degree-nine field. It is not an independent upper bound on actual seed Selmer excess. No new coefficient-prime coverage, FIN, ORDER9 or Q36 result follows. A continuation seeking to distinguish genuine excess from points must act after this norm-admission gate, for example through a separate point-relative arithmetic or lifting invariant. It cannot obtain that distinction merely by accumulating more split-prime additivity rows.

Finally, this theorem is for the selected nonzero Kummer module. We do not claim that every failure of full source admission remains nonzero after passage to K; a line-field class can in principle become a cube in K. That additional comparison has not been proved here and is not needed for the displayed mirror witness.
