# A residual monodromy calculation for the actual 167 quotient

Date: 2026-10-11. Status: WRITTEN_DEDUCTION_UNDER_RETAINED_C3_AND_GRAPH_IDENTIFICATIONS. This is not an independently certified theorem, a computed CM point, or a BSD conclusion. It supplies a parametrization-independent normalization check.

## Inputs and exact conclusion

Let J be the Jacobian of X of discriminant 501 and Eichler level 847. Let pi:J -> E1 be the quotient for E1=[1,1,1,1878418,-485198548]. Retain the natural C3 comparison, and the component-unit argument in ../component/COMPONENT_UNIT.md. In particular pi induces an isomorphism on the admitted residual two-dimensional quotient, and its map on the normalized component source is k in F5^times. Write delta for the polarized quotient degree: pi*pi^vee=[delta].

The definite quaternion module of discriminant 3 and level 847 has 176 vertices, all weights one. The executed base Brandt calculation gives a primitive integral eigenvector f with sum zero and norm 144. The simultaneous mod-5 eigenspace for T2,T13,T17 is one-dimensional. Its characteristic-zero eigenline is that of E=2541c1, so T167 f=-12 f. The lifted form has U167=+1. Section 4 fixes a source representative supported entirely on the even vertex summand, avoiding an unresolved sign convention on the odd summand.

Then the graph calculation gives

    delta / k^2 = -72*144 = 2 in F5.

Here delta means the actual quotient degree, not a chosen modular-degree proxy. If the separate Pasten degree calculation delta=293952 survives its audit, delta=2 mod5 and this implies k^2=1. It does not determine the sign of k.

## 1. Chain groups and the doubled vertex set

Work over Z_(5). The dual graph has two copies of the 176-vertex definite set. Orient each geometric edge once, from its even endpoint to its odd endpoint. Set C1=Z_(5)[edges], C0=Z_(5)[vertices], and let d send an edge to target minus source. The actual character lattice is X=ker d. Its monodromy pairing is the edge pairing; the edge weights are one, since edge stabilizers are subgroups of the already trivial vertex stabilizers.

All pairings in this note use each edge once and both copies of the vertex set. There is no factor 1/2 in the edge pairing. Under compatible base-set identifications, the Laplacian is

    d*d^t = [[168, -T167],[-T167,168]].

For xi=(f,f), therefore,

    d*d^t xi = 180 xi = 5*36 xi,
    <xi,xi> = 2*144 = 288.

Conjugating by the diagonal matrix (1,-1) changes this matrix to the version with +T167 and changes the potential to (f,-f). Such a change also changes the degree map and boundary coordinates; this note does not silently identify those transformed coordinates with a literal vertex divisor. The calculation below stays in literal graph coordinates. Its norm is 288. A one-copy norm would lose a factor two.

## 2. Why the actual elliptic character vector is in this residual gradient line

Let v=pi^*(1) in X, where 1 generates the character lattice of the split Tate curve E1 at 167. Its geometric Tamagawa number is 5. Functoriality of the monodromy pairing gives a homomorphism lambda:X -> Z_(5) such that

    <v,z> = 5 lambda(z),  lambda(v)=delta.

Consequently <v,v>=5 delta, and the reduction vbar lies in the radical of the pairing on X/5X. Since the graph is connected, d has image the degree-zero vertex lattice, X is saturated in C1, and over F5 the annihilator of ker d is im d^t. Thus

    vbar=d^t xibar,  d*d^t xibar=0.

The potential xibar is unique modulo a global constant. It may be normalized to have total sum zero because there are 352 vertices and 5 does not divide 352.

The graph maps commute with T2,T13,T17. Since v is an E1 eigenvector, the normalized potential is a simultaneous residual eigenvector for their common base eigenvalues. A possible discrepancy by a constant disappears after taking total sum. The T2 eigenvalue is -1, whereas T2 acts on constants by 3, so no constant eigensummand remains. In fact the sum on each parity part is zero. The computed one-dimensional base eigenspace now forces

    xibar=(a fbar,b fbar).

The Laplacian equation is [[3,2],[2,3]](a,b)^t=0 over F5. Its kernel is a=b. Hence

    vbar=c d^t(fbar,fbar).

This is a deduction for the actual quotient character vector, not an assumption that an arbitrary graph cycle is the elliptic eigenvector. The component-unit argument makes c nonzero: if vbar=0, every integral character functional evaluates to zero on v, contradicting k != 0.

## 3. A graph lemma that needs no 29,000-edge construction

Put g=d^t xi. Choose an integral lift of c. Since v=cg mod5, write v=cg-5w. The cycle condition gives dw=36c xi. Then

    <v,v> = c^2<g,g> -10c<g,w> +25<w,w>
            =180c^2<xi,xi> -360c^2<xi,xi> +25<w,w>.

Therefore

    <v,v>/5 = -36c^2<xi,xi> mod5.

The answer is independent of the unknown w. Its existence follows from the actual v; alternatively the surjectivity of d onto degree-zero divisors supplies a flow with the required boundary. No claim of an integral Smith form over a Hecke algebra is used.

## 4. Match the component source before canceling c

Let D be a degree-zero vertex divisor representing the normalized component generator. Choose z in C1 with dz=D. The component class is the image of the character functional x_D(z')=<z,z'> on X. Replacing z by a cycle changes x_D by a monodromy row, as required. This is precisely the construction of the component map in BD05 Corollary 5.12.

The earlier source convention says

    rho_f(x,y)=f(x)-f(y).

with x in the CM-even class. It is unnecessary to assert that the full difference functional in these degeneracy coordinates is the literal graph's plus functional. Instead choose two base vertices i,j with f_i=1 and f_j=0; the printed primitive vector has such entries. Put x=e_i-e_j and take the literal vertex divisor

    D=(x,0).

It is degree zero, including degree zero on each parity summand. The source definition itself gives rho_f(omega(D))=f(x)=1, and the literal graph potential gives <xi,D>=f(x)=1. Thus the same representative defines the specified component generator under both descriptions, regardless of the odd-coordinate sign. This establishes the needed normalization on an actual representative, not by a formal change of notation. Consequently

    k=x_D(v)=c<z,d^t xi>=c<D,xi>=c mod5.

Thus <v,v>=5delta and the previous calculation imply

    delta/k^2 = -36*288 = 2 mod5.

The even-supported representative is material. The predecessor does not explicitly print the full change of coordinates between its abstract pair and literal graph divisors; this note does not repair that omission by assertion. It uses only the unambiguous even summand specified there. An overall boundary orientation reversal changes c and k together and does not change the squared ratio. If a future audit changes the source generator by u, this displayed ratio changes by u^(-2), exactly as its definition requires.

## 5. What this buys and what it does not

This controls the square of the component-normalized parametrization degree using the small base Brandt space. It is useful in a generalized Gross-Zagier computation of (n/k)^2, because quotient scaling cancels. It supplies neither n nor its nonvanishing. A Gross-Zagier height calculation also loses the orientation sign; its squared result cannot by itself choose n/k rather than -(n/k).

No analytically predicted Sha order is used. No optimal-quotient component-surjectivity theorem is assumed by itself. The nonzero component factor is the separate C3-based deduction, explicitly retained here.

## Sources and proof grade

- Bertolini-Darmon, Annals 162 (2005), Section 5: Proposition 5.2 identifies X with graph homology; Lemma 5.6 supplies the doubled vertex set; Section 5.5 gives the weighted monodromy pairing and Corollary 5.12 constructs the component map from an actual vertex divisor. The standard degeneracy matrix and its sign-conjugate form are matched in Sections 5.4-5.5. https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf
- Current executable input: ../checks/BASE_BRANDT.json and ../checks/base_brandt.out. This note did not rerun the Brandt engine independently.
- Current retained component input: ../component/COMPONENT_UNIT.md.

The graph linear algebra and norm congruence above are a written deduction. They are not a claim that a new result has been independently reviewed or formalized.
