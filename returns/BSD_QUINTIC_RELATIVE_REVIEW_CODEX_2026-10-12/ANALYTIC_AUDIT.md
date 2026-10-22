# Independent audit of the relative analytic calculation

Date: 2026-10-12.

**Verdict: RELATIVE_ANALYTIC_IDENTITY_SUPPORTED_UNDER_RETAINED_INPUTS.**

I reviewed `submitted/BSD_QUINTIC_RELATIVE_LEADING_TERM_2026-10-12/PROOF.md`, its complete saved denominator-25 table, its checker, source list, and the preceding tower audit's stronger point-group consequence. I found no blocking error in the character calculation, period and Gauss factors, field discriminant, local factors, regulator scaling, or the resulting factor \(19^4\). This is written mathematical review, not formal verification, novelty certification, an independent reconstruction of the original large symbol certificate, or an assertion about actual Sha orders.

## 1. The evaluated algebraic numerator

The supplied table is the same historical 20-row table reviewed in the predecessor. Its grouped coefficients are

\[
S=(-76,0,-76,76,76)
\]

for cosets of \(\Delta=\{1,7,18,24\}\) ordered by powers of 6 modulo 25. I independently recomputed that grouping from the individual rows. The formula

\[
j(a)=4\frac{(a^4\bmod25)-1}{5}\pmod5
\]

is also correct: on \(a=d6^j\), the fourth power is \(1+20j\pmod{25}\), so multiplying the resulting quotient by 4 recovers \(j\).

The table's period is \(\omega_1\), whereas the required full real period is \(\Omega=2\omega_1\). Thus

\[
B(X)=38(-1-X^2+X^3+X^4).
\]

For any nontrivial fifth root \(\zeta\), the exact identity

\[
B(\zeta)=-38\zeta^2(1+\zeta)(\zeta-1)^2
\]

already follows from \(\zeta^5=1\). Each factor is nonzero. The factors \(\zeta\), \(-1\), and \(1+\zeta\) have norm one in \(\mathbf Q(\zeta)\), while \(\operatorname{Norm}(\zeta-1)=5\). Hence

\[
\operatorname{Norm}(B)=38^4\cdot25=52\,128\,400,
\qquad (B)=(38)(\zeta-1)^2.
\]

This ideal factorization concerns the evaluated algebraic numerator. It does not identify a Selmer group or the prime support of Sha.

## 2. Character orientation and Gauss factors

With \(\lambda_f(r)=\sum_{m\ge1}a_m e^{2\pi i m r}/m\), interpreted by its modular-symbol/Abel limit, the direct finite Fourier calculation is

\[
\sum_{a\bmod25}\chi(a)e^{2\pi i ma/25}
 =\tau(\chi)\chi^{-1}(m).
\]

The formula is zero when \(5\mid m\), as required for a primitive conductor-25 character. Taking the appropriate limit gives

\[
B(\zeta^k)=\tau(\chi^k)
 \frac{L(E,\chi^{-k},1)}{\Omega}.
\]

All characters here are even: \(-1\in\Delta\). Therefore the odd imaginary part of the table cancels, and using the real plus table loses no part of this character sum. There is no Teichmüller averaging factor and no additional Manin multiplier in this formula for the already normalized newform table.

Pairing inverse characters gives \(\tau(\chi^k)\tau(\chi^{-k})=25\). The product over the four nontrivial characters is consequently 625. A consistent inverse-character convention merely permutes the four factors; a common reversal of modular-symbol paths changes four signs and leaves their product unchanged. The actual product is

\[
\prod_{k=1}^4\frac{L(E,\chi^k,1)}{\Omega}
 =\frac{38^4\cdot25}{625}
 =\frac{2\,085\,136}{25}.
\]

No rationality claim for the base rank-two leading term has entered.

## 3. Artin factorization and the derivative

The characters of the degree-five field are the trivial character and the four primitive conductor-25 characters above. Artin factorization is therefore exact for the complete finite Euler products:

\[
L(E/F,s)=L(E/\mathbf Q,s)\prod_{k=1}^4L(E,\chi^k,s).
\]

In particular, no Euler factor at 5 is to be deleted by hand. At 5 the nontrivial character twists are ramified, while the trivial factor supplies the local factor of the totally ramified base change. At other primes the usual unramified character decomposition gives the same local factorization.

The twisted weight-two forms have holomorphic L-functions and the displayed central values are nonzero. The retained base analytic rank two then proves analytic rank two over \(F\). Differentiating the product gives

\[
\frac{L''(E/F,1)/2}{L''(E/\mathbf Q,1)/2}
 =\Omega^4\frac{38^4}{25}.
\]

Terms involving derivatives of a twisted factor disappear because the base value and its first derivative vanish. There is no extra factorial or derivative of the character product.

## 4. Number-field normalization checked against a primary source

I freshly read Dokchitser–Evans–Wiersema, *On a BSD-type formula for L-values of Artin twists of elliptic curves*, arXiv:1905.04282v2, §1.1, Notations 16–18, and Lemma 36(2)–(5) with its proof:

<https://arxiv.org/pdf/1905.04282>.

These locations fix full real periods, the square root of the field discriminant, finite differential corrections, and the field-relative height convention. The height used there scales by the field degree; it is explicitly distinguished from the absolute height. Only those definitions and elementary base-change facts are imported here. The paper's BSD conjecture and conjectural Artin-twist arithmetic are not assumed.

Since \(F\) is totally real of degree five, the archimedean factor is \(\Omega^5\). Each of its four nontrivial characters has conductor 25, so conductor–discriminant gives

\[
D_F=25^4=5^8,\qquad\sqrt{D_F}=625.
\]

The Gaussian-period polynomial's discriminant has the extra factor \(7^2\); it is not the field discriminant. The packet keeps this distinction correctly. Conductor–discriminant can also be read from the induction conductor identity applied to the direct sum of these five characters.

## 5. Finite local factors, including 2

The supplied local types and rational Tamagawa numbers are retained from the historical seed certificate. Direct reduction modulo 25 gives the following decomposition data:

| Rational prime | Character exponent | Number of places | Residue degree | Tamagawa product |
|---|---:|---:|---:|---:|
| 2 | 2 | 1 | 5 | 2 |
| 3 | 4 | 1 | 5 | 2 |
| 2243 | 0 | 5 | 1 | 1 |
| 4547 | 4 | 1 | 5 | 2 |
| 5843 | 0 | 5 | 1 | 32 |

These products are valid under the retained types:

- Split multiplicative type remains split. Nonsplit multiplicative reduction stays nonsplit under an unramified extension of odd degree; its Tamagawa number remains two for type \(I_2\).
- Type III has geometric component group of order two, so an unramified degree-five extension changes neither its geometric configuration nor its fixed component group.
- At 2, type \(I_1^*\) has geometric component group of order four. Its automorphism group has order dividing 6 (indeed the odd-star case is cyclic of order four). Thus the order of Frobenius on the component group is prime to five. Frobenius and its fifth power have the same fixed subgroup, so the retained rational Tamagawa number two remains two. This argument does not assume semistability at 2 or apply a tame-residue-characteristic formula there.

The extension is unramified away from 5, so the bad-prime discriminant valuations remain \(8,2,1,3,2\), all below 12. No further integral minimization is possible: such a change would lower the valuation by a positive multiple of 12. At the ramified prime 5 the curve already has good reduction, which remains good. Therefore the chosen differential is minimal everywhere after base change and every differential correction is one.

It follows that

\[
C_{\mathbf Q}=16,\quad C_F=256,\quad C_F/C_{\mathbf Q}=16.
\]

No number-field Tate algorithm was run; this is a deduction from retained local types and unramified base-change theory.

## 6. Point lattice and final cancellation

The input required here is the full equality \(E(F)=E(\mathbf Q)\), including torsion, proved in §6 of the preceding tower audit under the additional retained irreducibility hypotheses at all coefficient primes at least five. Rank equality alone would not suffice. With this explicit stronger input,

\[
t_F=t_{\mathbf Q}=2,\qquad R_F=5^2R_{\mathbf Q}.
\]

The latter uses the same full free basis and the degree-scaled height convention. An absolute height used without changing the BSD normalization would lose a factor 25. There is no unknown point index left in this calculation.

Consequently the submitted analytic numbers satisfy

\[
\frac{A_F}{A_{\mathbf Q}}
 =\frac{38^4}{25}\cdot625\cdot\frac1{25}\cdot\frac1{16}
 =19^4=130\,321.
\]

Also \(A_{\mathbf Q}=q_E/4\), since the rational torsion factor is four and the rational Tamagawa product is sixteen. Thus \(A_F=(130321/4)q_E\). The calculation neither needs nor establishes \(q_E\in\mathbf Q\) or \(q_E=36\).

## 7. Scope of the accepted result

This proves an exact relative analytic leading-term identity from genuine saved seed arithmetic, under the listed retained inputs. It is stronger than a numerical approximation or a guessed factor. It does **not** prove \(\#\Sha(E/F)=19^4\#\Sha(E/\mathbf Q)\); that interpretation needs a separate arithmetic theorem or BSD over both fields. Nor does the factorization of \(B\) itself produce a 19-primary class or a two-sided order bound.

The next meaningful arithmetic use is to address the nontrivial character components with their integral normalizations and local terms intact. That is a different task from the complete relative analytic calculation reviewed here. The base-field unknown components do not disappear merely by extension to \(F\).

FIN, ORDER9, Q36, and base-field coefficient-prime coverage are unchanged by this audit. No new symbol value, p-adic coefficient digit, point search, or actual Sha computation was performed.
