# Independent check of the October 4 RS2 Laurent construction

**Date:** 2026-10-04  
**Object reviewed:** `BSD_RECEIVER_AND_RS2_PUSH_CODEX_2026-10-04.zip`, RS2 portion only.  
**Verdict:** The finite-level identities, Laurent extraction, and direct seed pairing have no blocking error in this written review under the stated conventions and retained seed inputs. No Q36 or Sha theorem is established here. This is a separate mathematical reconstruction and computational check, not human peer review or a Lean certification.

## 1. Correction to the earlier assistant claim

The archive contains the September 20 file `context/RS2_NORMALIZED_A2_VERDICT.md`. Its sections 0–2 already remove the bad-Euler factors by the identity

\[
\widetilde P(x)=D_N(-x/2)P(x),\qquad
D_N(s)=\prod_{q\mid N}(1-q^{-2s}),
\]

and give the rational-Euler-factor pairing for its quadratic coefficient. In particular, the product of bad-prime logarithms was already identified as normalization-dependent and removed. The later September 20 `context/RS2_L3_VERDICT.md`, section 6, explicitly archives RS2 under that run's stopping rule. Those are contents of supplied, hash-bound historical files; this review does not independently establish their historical creation timestamps.

**Consequently my earlier October 4 statements that I had supplied a new logarithmic-denominator removal and recovered an overlooked live route were not supported. I withdraw those descriptions.** The October 4 file `SEED_BSD_RS2_NORMALIZED_CONSTRUCTION_2026-10-04.md` is an elementary rescaling of an inherited identity, not a new arithmetic input. Its algebra does not demonstrate a height comparison. The archival stopping decision is not a mathematical impossibility theorem either.

The new return goes beyond that rescaling: it writes both level-N factors as finite full-level dilation sums and supplies the needed coefficient extraction. The following sections check that calculation without treating the earlier stopping labels as proofs.

## 2. The finite-level identities: reconstruction from primitive pairs

Use the source's **unitary weight** convention. Thus \(V_dF(z)=F(dz)\) has no extra power of d. Let

\[
E(z,s)=\frac12\sum_{(a,b)=1}\frac{y^s}{|az+b|^{2s}},
\quad E^*(z,s)=\theta(s)E(z,s),
\quad\theta(s)=\pi^{-s}\Gamma(s)\zeta(2s).
\]

These definitions are imported from Diamantis–O'Sullivan, equations (2-2)–(2-5), printed pp. 1885–1886. All subsequent finite-level identities in this section are derived.

For a prime q, split the primitive terms of \(E(qz,s)\) according to whether q divides b. If \(q\nmid b\), the substitution \((a,b)\mapsto(qa,b)\) gives exactly the terms of E with q dividing the first coordinate, multiplied by \(q^s\). If \(q\mid b\), the substitution \((a,b)\mapsto(a,b/q)\) gives exactly the terms with q not dividing the first coordinate, multiplied by \(q^{-s}\). Hence, writing \(E_{q\nmid a}\) for the restricted primitive sum,

\[
E(qz,s)=q^sE_{q\mid a}(z,s)+q^{-s}E_{q\nmid a}(z,s),
\]

and therefore

\[
(1-q^{-s}V_q)E=(1-q^{-2s})E_{q\nmid a}. \tag{2.1}
\]

The restrictions for different primes are preserved by these substitutions and commute. For
\(\sigma_0=\left(\begin{smallmatrix}0&-1/\sqrt N\\\sqrt N&0\end{smallmatrix}\right)\), a matrix in \(\Gamma_0(N)\) has primitive upper row (a,b) with \((a,N)=1\); conversely every such row is completed to a matrix since \((a,Nb)=1\). The lower row of \(\sigma_0^{-1}\gamma\) is \(-\sqrt N(a,b)\). Thus

\[
E_{0,0,N}(z,s)=\frac{N^{-s}}2
\sum_{(a,b)=1,\ (a,N)=1}\frac{y^s}{|az+b|^{2s}}.
\]

Multiply (2.1) over q dividing N and then by \(\theta(s)\). This proves

\[
D_N(s)E^*_{0,0,N}(z,s)
=N^{-s}\sum_{d\mid\operatorname{rad}N}\mu(d)d^{-s}E^*(dz,s). \tag{2.2}
\]

Now \(R_0=iy\partial_{\Re z}+y\partial_y\) satisfies \(R_0E=sE_2\); multiplication by \(\theta(s)\) gives exactly \(E_2^*=R_0E^*\), with completion \(\pi^{-s}\Gamma(s+1)\zeta(2s)\). The chain rule gives \(R_0V_d=V_dR_0\). Applying it to (2.2) proves the submitted weight-two identity, including all scalar factors:

\[
\boxed{D_N(s)E^*_{2,0,N}(z,s)
=N^{-s}\sum_{d\mid\operatorname{rad}N}\mu(d)d^{-s}E_2^*(dz,s).} \tag{2.3}
\]

For the weight-zero infinity-cusp factor, Fricke inversion of (2.2) and full-level inversion invariance give

\[
D_N(s)E^*_{0,\infty,N}(z,s)
=N^{-s}\sum_{d\mid\operatorname{rad}N}\mu(d)d^{-s}E^*((N/d)z,s). \tag{2.4}
\]

The proofs first hold for \(\Re(s)>1\), then extend meromorphically. They do not require N squarefree. At the seed there are precisely \(2^5=32\) terms in each formula. This is a count of dilation terms, not a bound on the dimension of a seed cusp space or on its evaluation cost.

## 3. Fourier normalization, poles, and coefficient extraction

The full-level expansion in the source gives, with \(w_n(y;s)=2\sqrt{|n|y}K_{s-1/2}(2\pi|n|y)\),

\[
E^*=\theta(s)y^s+\theta(1-s)y^{1-s}
+\sum_{n\ne0}|n|^{s-1}\sigma_{1-2s}(|n|)w_n(y;s)e(n\Re z).
\]

Applying R_0 makes the nth Fourier factor \((y\partial_y-2\pi ny)w_n\). In (2.3) the arithmetic simplification is the exact divisor-convolution identity

\[
\sum_{d\mid\operatorname{rad}N,\ d\mid n}
\mu(d)d^{1-2s}\sigma_{1-2s}(n/d)
=\sigma^{(N)}_{1-2s}(n), \tag{3.1}
\]

where the latter divisor sum omits divisors sharing a prime factor with N. The identity follows prime by prime by subtracting the geometric series shifted by one power. Thus the submitted nonconstant and constant coefficients are correctly normalized. For fixed positive y, the relevant finite number of parameter derivatives converge normally by exponential Bessel decay. No statement about interchanging with an improper integral to y=0 is inferred from this fact.

Set

\[
A(x,z)=E^*_{0,\infty,N}(z,1-x/2)=\sum_{i\ge-1}a_i(z)x^i,
\quad F(x,z)=D_N(-x/2)E^*_{2,0,N}(z,-x/2)=\sum_{j\ge0}f_j(z)x^j.
\]

The full-level residue at s=1 is 1/2. Formula (2.4) gives

\[
a_{-1}=-\frac1{N\prod_{q\mid N}(1+1/q)}.
\]

The submitted recipe

\[
f_j=\sum_{d\mid\operatorname{rad}N}\mu(d)
\sum_{h+k=j}\frac{(\log(Nd)/2)^h}{h!}\frac{(-1/2)^k}{k!}
\left.\partial_s^kE_2^*(dz,s)\right|_{s=0}
\]

is the product rule applied to (2.3), with the correct signs. Let

\[
\mathcal L=\prod_{q\mid N}\log q,\qquad
B(x)=\prod_{q\mid N}\frac{x\log q}{e^{x\log q}-1}
=1+b_1x+b_2x^2+b_3x^3+O(x^4).
\]

For five bad primes, \(\mathcal L E^*_{2,0,N}(z,-x/2)=-x^{-5}B(x)F(x,z)\). Direct multiplication gives

\[
b_1=-S_1/2,\qquad b_2=(3S_1^2-S_2)/24,
\qquad b_3=(S_1S_2-S_1^3)/48,
\]

where \(S_1=\sum\log q\), \(S_2=\sum(\log q)^2\). These are also checked as polynomial identities in five independent symbols, not merely at sample logarithms.

Writing \(g_j=\sum_{h=0}^jb_hf_{j-h}\) recovers the submitted exact formula

\[
\boxed{\mathscr A_N=-\frac{a_{-1}g_3+a_0g_2+a_1g_1+a_2g_0}{2\pi y}.} \tag{3.2}
\]

A useful way to check the two normalizations is to define all coefficients \(\widetilde A_j=[x^j]AF/(2\pi y)\). The exact whole-function relation is

\[
\mathscr A_N=-\widetilde A_2-b_1\widetilde A_1-b_2\widetilde A_0-b_3\widetilde A_{-1}. \tag{3.3}
\]

In particular \(\mathscr A_N\) and \(-\widetilde A_2\) are not to be identified as unprojected functions. Their seed pairings agree only after using the vanishing of the lower seed pairings.

At s=0,

\[
E_2^*(z,0)=-\tfrac12+\tfrac{\pi y}{6}
-4\pi y\sum_{n\ge1}\sigma_1(n)e(nz).
\]

The n=1 Fourier coefficient of \(F(0,z)=\prod_{q\mid N}(1-V_q)E_2^*(z,0)\) is nonzero. Thus the second unnormalized factor has order-five pole, the first has order-one pole, and their unprojected product has order-six pole. The order-three pole of a particular pairing is a different statement. Also, each dilation in (2.4) is a multiple of \(N/\operatorname{rad}N=18188\), establishing the claimed Fourier sparsity. The older modulus 9094 is not used.

## 4. Direct mixed-cusp pairing: independent reconstruction

Let f be the normalized seed newform with real coefficients, retaining its stated arithmetic provenance. For independent parameters s,t put

\[
P(s,t;z)=E^*_{0,\infty,N}(z,s)E^*_{2,0,N}(z,t)/(2\pi y).
\]

Use the unnormalized weight-two Petersson pairing \(\int P\overline f\,dx\,dy\). Unfold the first factor in an absolute-convergence region. The integral left in the nth coefficient is

\[
I_n(s,t)=\int_0^\infty y^{s-1}(y\partial_y-2\pi ny)w_n(y;t)e^{-2\pi ny}\,dy.
\]

Integration by parts cancels the two terms with an additional \(2\pi n\) and leaves

\[
I_n=-s\int_0^\infty y^{s-1}w_n(y;t)e^{-2\pi ny}\,dy
=-(4\pi n)^{-s}\frac{\Gamma(s+t)\Gamma(s+1-t)}{\Gamma(s)}. \tag{4.1}
\]

For completeness, the Bessel integral follows by inserting the positive-real integral representation of K (DLMF 10.32.9), performing the gamma integral first, and reducing the remaining integral to the beta function. One obtains

\[
\int_0^\infty u^{\lambda-1}e^{-u}K_\nu(u)\,du
=\frac{\sqrt\pi\,\Gamma(\lambda+\nu)\Gamma(\lambda-\nu)}
{2^\lambda\Gamma(\lambda+1/2)},\quad \Re\lambda>|\Re\nu|.
\]

Take \(\lambda=s+1/2\), \(\nu=t-1/2\), then use meromorphic continuation. Multiplying the completions and n-powers gives

\[
\langle-P(s,t),f\rangle=
\frac{\zeta(2s)N^{-t}\Gamma(s+t)\Gamma(s+1-t)}
{(2\pi)^{2s+1}D_N(t)}
\sum_{n\ge1}\frac{a_n\sigma^{(N)}_{1-2t}(n)}{n^{s+1-t}}. \tag{4.2}
\]

This establishes the mixed-cusp normalization directly; no unchecked extension of a same-cusp theorem is needed.

For the local Euler product, with \(L_q(X)=(1-a_qX+qX^2)^{-1}\) and a formal variable u,

\[
\sum_{r\ge0}a_{q^r}(1+u+\cdots+u^r)X^r
=\frac{L_q(X)-uL_q(uX)}{1-u}
=\frac{1-quX^2}{(1-a_qX+qX^2)(1-a_quX+qu^2X^2)}. \tag{4.3}
\]

This is a rational-function identity, including u=1 by a removable limit. At bad primes the depleted divisor sum is one. Inserting \(s=1-x/2\), \(t=-x/2\) gives exactly the submitted depleted Euler product and pairing. Meromorphic continuation of the paired family is justified by polynomial/logarithmic growth of the Eisenstein coefficients and exponential cusp decay of f; it does not prove the older L3 coefficientwise improper-integral continuation.

The actual local signs used in the constant were also independently re-counted on the displayed seed cubic. The numbers of projective points including the singular node are respectively 5, 2243, and 5845 at q=3,2243,5843. With c4 a unit these give \(a_3=-1,a_{2243}=1,a_{5843}=-1\). Exact rational arithmetic then gives

\[
D_N(1)=\frac{2367493793168102489088}{3551241671398414932409},
\qquad
\boxed{C_N=\frac{270966167197441}{2168324513321472}.}
\]

Using the retained double central zero, (4.2)–(4.3) imply

\[
\langle\widetilde A_2,f\rangle=-C_N\pi^{-3}L(f,2)L''(f,1),
\qquad
\langle\mathscr A_N,f\rangle=C_N\pi^{-3}L(f,2)L''(f,1).
\]

The latter sign follows from (3.3) and the lower seed-pairing vanishings. Both identities agree with the new packet.

## 5. What the review establishes, and what it does not

The particular Laurent-expansion task has a valid finite-level formula and a valid coefficient-extraction recipe. The direct pairing calculation also fixes the earlier cross-cusp normalization uncertainty. These are the mathematical claims approved in this review.

The cusp projection H is an explicitly defined **complex** cusp form. Neither the 32-term presentation nor a rational nonzero C_N proves rationality or a denominator bound for its seed coefficient. Parameter derivatives still contain logarithms and special-function derivatives; cancelling the global product of logarithms is not an arithmeticity theorem.

The equation

\[
\langle H,f\rangle=72C_N\pi^{-3}L(f,2)\Omega_E\operatorname{Reg}(E)
\]

is equivalent, using the displayed pairing, to the retained Q36 target. It is not proved by that pairing or by the expansion. This review neither proves it nor claims that the expansion can never contribute to a future proof. No Sha bound, FIN, ORDER9, or Q36 conclusion is added. The receiver/pairing material elsewhere in the supplied ZIP was not substantively re-audited here.

## 6. Check record and limitations

All 41 entries in the supplied top-level SHA-256 manifest verified; ZIP CRC check passed. The supplied RS2 CHECKS.py was run in a separate work directory; CHECK_RESULTS.json reproduced byte-for-byte. That is reproduction, not independent proof of all claims in the ZIP.

A separately written `independent_checks.py` verifies the generic Rankin rational-function identity, Bernoulli coefficients in five independent symbolic variables, the Laurent coefficient relation (3.3), 5888 exact rational primitive-pair summand comparisons, the three seed odd-multiplicative point counts, and the rational constants. The all-s proofs are written above; the finite checks do not replace them. The supplied high-precision integrations remain numerical controls, not interval-certified integrations.

Seed modularity, the conductor, analytic rank, period, saturated basis, regulator, and the Q36 interpretation retain their pre-existing grades. No new class group, global Selmer group, production coefficient campaign, or peer review has been performed. No canonical master, repository, or original input file has been altered.

### Sources inspected

- Input derivation: `input/rs2/EXPLICIT_LAURENT_CONSTRUCTION.md`, sections 1–6.
- Input pairing: `input/rs2/PAIRING_AND_HEIGHT_TARGET.md`, equations I, U, E, Pair, Height.
- Historical comparison: `input/context/RS2_NORMALIZED_A2_VERDICT.md`, sections 0–2; `input/context/RS2_L3_VERDICT.md`, sections 0 and 6–7. Copies are unmodified and hash-bound.
- Diamantis–O'Sullivan, *Kernels for products of L-functions*, Algebra & Number Theory 7 (2013), pp. 1885–1886 and 1913–1915. Publisher PDF: https://msp.org/ant/2013/7-8/ant-v7-n8-p05-p.pdf . Relevant text was read through web extraction, and the rendered page 1886 was inspected. Rendering the other requested pages and downloading a full local PDF failed; no claim of a full rendered-source audit is made.
- NIST DLMF, 10.32.9 (K-Bessel integral representation), https://dlmf.nist.gov/10.32.E9 ; 5.12.1 (beta function), https://dlmf.nist.gov/5.12.E1 .

The review derives the finite-level and pairing identities from those definitions. It does not attribute an arithmetic-regulator comparison to these analytic sources.
