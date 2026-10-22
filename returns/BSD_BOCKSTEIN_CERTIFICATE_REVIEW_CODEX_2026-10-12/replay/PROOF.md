# Exact Bockstein content with an explicit Kato-index defect

Date: October 12, 2026.

**Grade: DERIVED.** The algebraic proposition below has a complete written proof. Its application to the BSD seed imports the explicitly listed arithmetic inputs from the October 7 content-bound return. Those arithmetic inputs have not been independently recertified here. No literature-novelty, formal-verification, or independent-human-review claim is made.

## 1. The actual change to the accepted criterion

The retained seed criterion is

\[
 \delta_p\ne0,\qquad m_p-w_p\le1
 \quad\Longrightarrow\quad \Sha(E/\mathbb Q)[p^\infty]=0.
\]

We derive the less restrictive sufficient criterion

\[
 \boxed{\delta_p\ne0,\qquad m_p-w_p-b_p\le1
 \quad\Longrightarrow\quad \Sha(E/\mathbb Q)[p^\infty]=0,}
\]

where \(b_p\) is the content of the **actual integral first Bockstein map into the primitive torsion-free quotient of global \(H^2\)**. It is not an arbitrarily normalized height, a freely rescaled regulator, or a definition in terms of Sha.

The precise identity behind the change is

\[
 \boxed{m_p=\operatorname{length}_{\mathbb Z_p}\Sha[p^\infty]
               +w_p+b_p+e_p,\qquad e_p\ge0.}\tag{1}
\]

The nonnegative defect \(e_p\) is defined from the actual integral Kato divisibility below. We do **not** assume it vanishes. Accordingly, no main-conjecture equality or augmentation-unit comparison is needed for the displayed sufficient criterion.

This sharpens the written inequality; it does not evaluate the new criterion at any seed prime.

## 2. Algebraic objects and hypotheses

Fix an odd prime \(p\), put \(A=\mathbb Z_p\), and let \(R=A[[U]]\). Consider the actual finite-free complex

\[
 C=[R^{n+1}\xrightarrow{D(U)}R^n]
\]

in degrees 1 and 2, for \(n\ge1\). Assume:

1. \(D(U)\) has generic row rank \(n\); \(M=\ker D\) is free of rank one, with basis \(\eta(U)\); and \(X=\operatorname{coker}D\) is torsion over \(R\).
2. \(D_0=D(0)\) has rank \(n-1\) over \(\mathbb Q_p\), and \(\eta(0)\ne0\).
3. The specified class is \(z=Ug\eta\), where \(g\in R\) and \(g(0)\ne0\). Its divided augmentation is \(\delta=g(0)\eta(0)\ne0\).
4. At **every** height-one prime \(\mathfrak q\) of \(R\), including \((p)\),
   \[
   \operatorname{length}_{R_{\mathfrak q}}X_{\mathfrak q}
   \le\operatorname{length}_{R_{\mathfrak q}}(M/Rz)_{\mathfrak q}.
   \tag{2}
   \]

Set

\[
 W=\ker D_0,\qquad H=\operatorname{coker}D_0,
 \qquad H_{\mathrm{tf}}=H/H_{\mathrm{tors}}.
\]

Then \(W\) is free of rank two and \(H_{\mathrm{tf}}\) is free of rank one over \(A\).

Write \(D(U)=D_0+UD_1+O(U^2)\). The first Bockstein followed by projection to the torsion-free quotient is

\[
 \overline\beta:W\longrightarrow H_{\mathrm{tf}},
 \qquad x\longmapsto[D_1x]_{\mathrm{tf}}.\tag{3}
\]

The possible minus sign in a connecting-map convention does not change any content. Formula (3) uses the generator \(U\) of the augmentation direction. Invariantly its target is \(H_{\mathrm{tf}}\otimes_A (U)/(U^2)\).

For a nonzero vector in a finite free \(A\)-module, content means the largest \(k\ge0\) for which the vector belongs to \(p^k\) times that module. Define

\[
 m=\operatorname{cont}_W(\delta),\qquad
 \tau=\operatorname{length}_A H_{\mathrm{tors}}.
\]

We will prove that \(\overline\beta\ne0\). Once this is proved, define

\[
 b=\operatorname{length}_A\operatorname{coker}\overline\beta
   =\min\{v_p(\overline\beta(w_1)),v_p(\overline\beta(w_2))\},\tag{4}
\]

where \(w_1,w_2\) is any \(A\)-basis of \(W\) and a primitive basis of \(H_{\mathrm{tf}}\) has been chosen. These choices change neither integer.

## 3. Proposition: exact content decomposition

**DERIVED proposition.** Under the hypotheses of §2, there is a nonnegative integer \(e\) such that

\[
 \boxed{m=\tau+b+e.}\tag{5}
\]

The integer is not unspecified: with the notation of the proof,

\[
 e=v_p\bigl(\rho(0)\bigr),\qquad \rho=g/d_1\in R\setminus UR.\tag{6}
\]

### Step 1: retain the actual maximal minors

Let \(\Delta(U)\) be the vector of signed maximal minors of \(D(U)\), with signs chosen so that \(D\Delta=0\). Since the kernel has basis \(\eta\),

\[
 \Delta=d\eta\qquad\text{for some nonzero }d\in R.\tag{7}
\]

The coordinates of \(\eta\) have no common irreducible factor. Otherwise division by such a factor would give another integral kernel vector, contradicting that \(\eta\) is a basis. **This is a greatest-common-divisor assertion, not an assertion that its coordinates generate the unit ideal.** All coordinates of \(\eta(0)\) can still be divisible by \(p\).

Localizing (7) at a height-one prime gives a matrix over a discrete valuation ring. Smith reduction there shows that

\[
 v_{\mathfrak q}(d)=\operatorname{length}_{R_{\mathfrak q}}X_{\mathfrak q}.
\]

Thus \(d\) generates the characteristic ideal of \(X\). Because \(R\) is a unique factorization domain, the all-height-one inequality (2) gives

\[
 d\mid Ug.\tag{8}
\]

Since \(D_0\) has rank \(n-1\), \(\Delta(0)=0\). Equation (7) and \(\eta(0)\ne0\) imply \(d(0)=0\). Since \(g(0)\ne0\), equation (8) then forces

\[
 d=Ud_1,\quad d_1(0)\ne0,\quad d_1\mid g.
\]

Set \(\rho=g/d_1\). It belongs to \(R\), and \(\rho(0)\ne0\). This proves in advance the nonnegativity required in (6).

Taking the coefficient of \(U\) in (7) gives the exact vector identity

\[
 [U]\Delta=d_1(0)\eta(0)\ne0.\tag{9}
\]

### Step 2: identify precisely the factor discarded by the old bound

Use constant \(A\)-unimodular row and column operations to put \(D_0\) in Smith form:

\[
 D_0=\begin{pmatrix}
 s_1&&&0&0\\
 &\ddots&&\vdots&\vdots\\
 &&s_{n-1}&0&0\\
 0&\cdots&0&0&0
 \end{pmatrix}.
\]

There are \(n-1\) nonzero diagonal entries and two remaining columns. Let

\[
 s=\prod_{i=1}^{n-1}s_i,\qquad v_p(s)=\tau.
\]

For \(n=1\), set \(s=1\). In these bases the last row and last two columns of \(D_1\) are a row \((u,v)\), which is exactly the row of \(\overline\beta\).

In a first derivative of any maximal determinant, the last row must supply the derivative term: its constant row is zero. All other rows supply their constant terms. Hence the only possibly nonzero entries of \([U]\Delta\) are the two corresponding to the last two columns, and, up to an overall sign, their values are

\[
 s(v,-u).\tag{10}
\]

Since (9) is nonzero, \((u,v)\ne(0,0)\). Thus \(\overline\beta\ne0\), \(b\) is finite, and

\[
 \operatorname{cont}([U]\Delta)=\tau+b.\tag{11}
\]

The row and column changes multiply determinant expressions by units and apply unimodular vector transformations, so they preserve content. Formula (11) is therefore intrinsic, not a consequence of an unrecorded normalization.

### Step 3: compare to the actual derivative

Let \(\mu\) be the content of \(\eta(0)\) in the ambient free source. The kernel \(W\) is saturated there: if \(px\in W\), then \(pD_0x=0\) in a torsion-free target, so \(D_0x=0\). Consequently content in \(W\) equals content in the ambient source.

Equations (9)–(11) give

\[
 v_p(d_1(0))+\mu=\tau+b,
 \qquad m=v_p(g(0))+\mu.
\]

Subtracting and using \(g=d_1\rho\) proves

\[
 m=\tau+b+v_p(\rho(0)).
\]

This proves (5) and (6). No pseudo-isomorphic replacement of \(X\) has been made. In particular, finite \(R\)-modules and the possibly positive \(\mu\) have not disappeared from the proof.

## 4. Application to the retained seed input

**IMPORTED_RETAINED, not freshly recertified.** Use the exact class, simultaneous lattice transport, smoothing, and cohomology complex of the October 7 `CONTENT_BOUND_PROOF.md`. Its domain is

\[
 \mathcal D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\},
 \quad N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843,
\]

with all additional source-matching conditions retained. The domain includes good ordinary and good supersingular primes; an ordinary height realization has a narrower interface.

The following are the specific imports from that return:

* Nonzero divided augmentation \(\delta_p\) gives primary finiteness and rank two for the actual augmented \(H^1\); the saturated Mordell–Weil lattice is then all of that \(H^1\).
* The all-height-one integral Kato inequality holds for the specified smoothed and transported class.
* For the minimal differential and the fixed saturated point basis,
  \[
  w_p=\min_i v_p\left(\frac{\log_\omega(P_i)}p\right),
  \qquad
  \operatorname{length}_{\mathbb Z_p}(H^2_S)_{\mathrm{tors}}
   =\operatorname{length}_{\mathbb Z_p}\Sha[p^\infty]+w_p.
  \tag{12}
  \]

Apply the proposition to this complex. Equation (12) substitutes for \(\tau\) in (5) and proves (1). In particular,

\[
 \operatorname{length}_{\mathbb Z_p}\Sha[p^\infty]
 \le m_p-w_p-b_p.\tag{13}
\]

Primary finiteness is obtained **before** applying the alternating Cassels–Tate pairing. Its even-length consequence gives

\[
 \operatorname{length}_{\mathbb Z_p}\Sha[p^\infty]
 \le 2\left\lfloor\frac{m_p-w_p-b_p}{2}\right\rfloor.
\]

The integer inside the floor is nonnegative under the hypotheses. Thus a value at most one in (13) forces vanishing. This is the corrected certificate.

No assertion is made when the actual first divided derivative vanishes. A higher-order derivative is a different problem; the present proof does not automatically extend to it.

## 5. What finite precision actually needs to establish

Suppose a residue calculation detects at least one nonzero coordinate of the actual \(\delta_p\) modulo \(p^{N_\delta}\). Its content \(m_p<N_\delta\) is then exact. Suppose separately that correctly normalized computations establish only

\[
 w_p\ge w_0,\qquad b_p\ge b_0.
\]

Then (13) still implies

\[
 \operatorname{length}\Sha[p^\infty]\le m_p-w_0-b_0.\tag{14}
\]

Consequently **lower bounds on both correction terms suffice**. One need not prove they are units or even find their exact valuations. Two zero residues modulo \(p^N\) give the lower bound \(N\), not an infinite valuation or a zero map.

If the proposed bound in (14) is negative, the inputs or their source identifications cannot all satisfy the retained hypotheses. A verifier must reject the packet rather than claim a negative group length. If both derivative residues vanish, its nonvanishing is not established at that precision.

## 6. Relation to the pending Exit 1 formula

The archived Exit 1 excerpt already proposed an exact Bockstein-content formula, with a claimed ordinary source-unit comparison. This return does **not** claim to have originated the decomposition, and does not certify the complete Exit 1 report.

What is established here is the exact cochain-level algebra with an explicit defect:

\[
 m_p-w_p-b_p=\operatorname{length}\Sha[p^\infty]+e_p,\qquad e_p\ge0.
\]

Removing \(e_p\) requires proving the appropriate equality/unit comparison for the **same** class and lattice. That source question is not settled here. Crucially, it is unnecessary for the one-sided corrected certificate.

Nor is a numerical height row automatically the row in (3). To reuse those values, one must match its target to the primitive lattice \(H^2_{\mathrm{tf}}\), its cyclotomic generator, its local splitting conventions, and the actual transported class. Multiplying the row by \(p\) would change \(b_p\) and could manufacture a false certificate; only unit changes of primitive bases preserve the content.

## 7. Exact controls and sharpness

Consider the genuine algebraic complex over \(R\) with \(P=p^a\):

\[
 D(U)=\begin{pmatrix}
 P&U&0&0\\
 0&P&U&0\\
 0&0&0&p^bU
 \end{pmatrix},\qquad
 \eta=(U^2,-PU,P^2,0)^t.
\]

Its maximal-minor vector is \(p^bU\eta\); the characteristic ideal of the cokernel is \((p^bU)\). Set

\[
 z=U p^{b+e}\eta,\qquad a,b,e\ge0.
\]

Then

\[
 \tau=2a,\quad b(\overline\beta)=b,\quad
 \delta=p^{2a+b+e}e_3,\quad m=2a+b+e.
\]

For \(a=0\), \(b=2\), \(e=1\), the old bound is three and the corrected bound is one. For \(a\ge1\), the finite pair remains: even with \(e=0\), the corrected bound is exactly \(2a\), not zero. This simultaneously demonstrates a strictly stronger formal certificate and retention of the earlier finite-error obstruction. These are not elliptic-curve realizations.

Dropping the height-one condition at \((p)\) invalidates the conclusion. In the same family, take \(a=1\), \(b=2\), but \(z=U\eta\). Then \(m=2\), \(b=2\), and \(\tau=2\). The false inference \(\tau\le m-b=0\) is possible precisely because \(p^2U\nmid U\). The supplied negative control records this failure. A residue-only program cannot authenticate the missing arithmetic inequality.

## 8. Endpoint disposition

**No seed Kato derivative, integral Bockstein row, or new primary component was evaluated in this return.** The stronger sufficient inequality does not prove its own premise. In particular it gives no cofinite estimate, no primary-finiteness result at 59, 487, 2243, 4547, or 5843, and no proof of FIN, ORDER9, or Q36.

The actual program change is to compare the specified derivative against the two independently normalized correction terms, rather than demand that their divisibility disappear. The still-missing arithmetic is control of the corrected quantity (or a different independently justified upper-control mechanism), not another proof of the matrix identity above.
