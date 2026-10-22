# Independent audit of G2 and the accompanying status report

Date: 2026-09-26. Verdict: **G2_SOURCE_AND_PROOF_CHECK_PASS**, relative to the explicitly retained seed inputs.

I found no blocking mathematical error in `G2_PROOF.md`, including its decisive §§3–5. I would retain G2 as a conventional written deduction, now independently source-and-proof reviewed by this audit. This is not a Lean verification, human peer review, or a fresh proof of the seed's saturation and residual-image claims.

The attached summary needs one substantive scope clarification: **G1 is the remaining gate of this proposed finite-support argument, not the only remaining mathematical obligation for full BSD.** Even a successful G1+G2 argument leaves the primes dividing its multiplier and its finite exceptional set to be handled, and does not itself provide the real leading-term comparison.

No source document, project map, sealed certificate, research repository or lab repository was modified. No successor, new modular-symbol computation, cloud run, or external communication was initiated.

## 1. Identity, scope, and source boundary

The audited proof is the archived file

`/Users/bsm/BSD_BUILD_MAP/pro6/G1G2_REVIEW_2026-09-26/BSD_GLOBAL_G1G2_REVIEW_2026-09-26/G2_PROOF.md`

with SHA-256

`b643667e481ceb5d9bff55d22b02b2f44c3ee08fa65a525d40310f42d6060c60`.

All 18 entries in the review's own `SHA256SUMS` verified. The copied inputs and their original locations are in `INPUT_BINDINGS.json`; a final rehash found all six originals unchanged. These are snapshot checks, not an attestation of earlier execution dates.

I read the entire G2 proof, the G1/G2 task, the returned report, the actual `tame_reg.gp`, and the relevant earlier translated-divisor discussion. I obtained and read the relevant primary-source passages independently:

* Tan, *Refined theorems of the Birch and Swinnerton-Dyer type* (1995), §2.1, Definition 2.2, (L3)–(L4), Remarks 1–3; §2.2, Definition 2.6. These specify the local splittings and their global assembly. [Primary PDF](https://aif.centre-mersenne.org/item/10.5802/aif.1457.pdf)
* Jossen, *On the Mumford–Tate conjecture for 1-motives*, author manuscript arXiv:1107.5259, §1.4, Proposition 1.8, Remarks 1.9–1.10. These provide the torsion realization and integral duality construction used here. [Primary PDF](https://arxiv.org/pdf/1107.5259)
* Milne, *Algebraic Number Theory*, Theorem 8.31, for Chebotarev after a nonempty conjugacy class has been constructed. [Primary PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf)

The downloaded Tan and Jossen PDFs and extracted text are retained locally under `sources/`, with URL and hash records. This audit does not invoke Tan's later BSD-dependent results or Jossen's open-image/fully-faithful-realization theorems. In particular, it does not import an unspecified finite exceptional set from an “almost all primes” theorem about 1-motives.

The finite-prime certificates and their large coefficient corpus were not re-audited here. The artifact and G1 literature grades in Pro's report remain their own grades; this report's new mathematical review is G2.

## 2. Exact statement accepted

Let the curve and retained saturated basis be

\[
E:y^2=x^3-x^2-66020924x-65074271436,
\quad P_1=(-3031,327384),\quad P_2=(-2394,281520).
\]

Retain the stated arithmetic inputs: the basis is saturated modulo the rational torsion of order two; the rational Tamagawa product is 16; and the residual representation is surjective at every prime being considered. This audit did not rerun those proofs.

For every prime

\[
p\notin S_0=\{2,3,5,2243,4547,5843\},
\]

the proof supplies infinitely many good auxiliary primes \(\ell\ne p\) satisfying

\[
\ell\equiv1+p\pmod{p^2},\qquad
\rho_{E,p}(\operatorname{Frob}_\ell)=-I_2,\qquad
R_{p,\ell}\ne0\pmod p.
\]

Here \(R_{p,\ell}\) is the normalized determinant of the actual tame pairing defined by the supplied script, not a newly substituted pairing. The conclusion is existential. It supplies no useful upper bound for the smallest \(\ell\) and no cost estimate for its associated modular-symbol calculation.

## 3. The fixed normalization in §3 works

Set \(Q_i=16P_i\). Each rational component-group order divides 16, so these points are on the identity component at every finite place.

For a rational lift \(r\) in a Poincaré fiber over \((Q_i,Q_j)\), the unramified splitting gives integers \(n_v(r)\), zero outside finitely many places. Rational lifts exist by Hilbert 90. Multiplication by

\[
\prod_{v<\infty}v^{-n_v(r)}
\]

removes every finite unramified value. Two resulting rational lifts differ by a rational number of valuation zero everywhere, hence by \(\pm1\). This is invisible in an odd-primary Kummer quotient.

This is a construction over \(\mathbf Q\), where the displayed rational scalar exists. There is no unnoticed ideal-class obstruction. It also does not infer a global normalization from one local computation: the construction explicitly includes all finite places. The corresponding 1-motive is fixed before either \(p\) or \(\ell\) is selected.

## 4. The geometric-to-computational comparison in §4 survives

### 4.1 The local quotient and global contributions

At a good \(\ell\ne p\) with \(p\nmid\#E(\mathbf F_\ell)\), multiplication by \(p\) is bijective both on the formal group and on the finite reduction group. Consequently it is bijective on \(E(\mathbf Q_\ell)\). Applying the multiplication-by-\(p\) sequence to

\[
1\longrightarrow\mathbf Q_\ell^\times\longrightarrow
G_j(\mathbf Q_\ell)\longrightarrow E(\mathbf Q_\ell)\longrightarrow0
\]

gives the torus-induced isomorphism

\[
\mathbf Q_\ell^\times/(\mathbf Q_\ell^\times)^p
\simeq G_j(\mathbf Q_\ell)/pG_j(\mathbf Q_\ell).
\]

Both injectivity and surjectivity matter: the former uses \(E(\mathbf Q_\ell)[p]=0\), the latter uses \(p\)-divisibility. Thus the inverse quotient map, followed by the tame character, is the unique extension of that character to \(G_j(\mathbf Q_\ell)\).

To compare with Tan's formal-group splitting, one may multiply its second elliptic argument by \(\#E(\mathbf F_\ell)\). This multiplier is a \(p\)-unit. Pulling back the splitting and dividing by it gives that same unique character extension. The finite-place normalization from §3 removes the other local terms in the global pairing, and the real sign has no odd-order contribution. This establishes (4.3); it does not discard away-from-\(\ell\) contributions without accounting for them.

### 4.2 The denominator and factor of two

The short diagonal calculation needs to be understood as a calculation with a rigidified integral line, not just an abstract line-bundle isomorphism. Here is the reasoning I used to check it.

On the identity component of a minimal model, extend \(\mathcal O_E(O)\) by the zero section and rigidify it using the minimal differential. The canonical section meets an identity-component rational point with intersection multiplicity \(v(d)\), where \(x=a/d^2\). If the point reduces away from \(O\), both quantities are zero; in the formal disc this follows from \(t=-x/y\), with \(v(t)=v(d)\).

The diagonal of the Poincaré line is the rigidified line

\[
[2]^*\mathcal O_E(O)\otimes\mathcal O_E(O)^{-2}
\simeq\mathcal O_E(O)^2,
\]

up to the common duality-sign convention. The integral cubical identification agrees on the identity component: any possible vertical discrepancy of the generic identification is fixed by its restriction to the rigidified zero section. No component-group correction remains after the points have been multiplied into the identity component. Thus the squared section has finite unramified value \(2v(d)\).

Near \(O\), in the differential-normalized formal frame, the section is \(t\) times a power series with constant term 1. On the diagonal its tame value is therefore \(t^2\) times a principal unit. Principal units are killed by an order-\(p\) tame character at \(\ell\ne p\). The global normalization divides by \(d^2\), giving

\[
B(Q,Q)=\pm 2\operatorname{ind}_g(t(Q)/d)
       =\pm2\operatorname{ind}_g(-a/b)\pmod p.
\]

Polarization then gives twice the script's bilinear pairing. Returning from a common prime-to-\(p\) formal multiple to the retained basis yields

\[
\det B(16P_i,16P_j)=4\cdot16^4R_{p,\ell}.
\]

The common reciprocity sign disappears from this determinant. A different identification of \(\mu_p\) changes it by a square unit. None changes nonvanishing. This also explains why using a varying computational multiplier \(M_\ell\) does not make the fixed 1-motive vary.

**Result:** I accept the identity needed by G2. This review supplies the geometric argument; the finite numerical comparisons below are diagnostics only.

## 5. The actual Galois-image argument also survives

The proof does not assume that two Kummer blocks are independent. This is essential. Jossen's integral duality, reduced modulo \(p\), identifies the upper extension with the dual of the lower one. On \(\Gamma_0=\ker\rho_{E,p}\), compatible bases give

\[
b(g)=-a(g)^tJ,
\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]

up to the uniform polarization convention. Possible changes of splittings are coboundaries and do not affect this restricted identity.

I checked each subsequent step:

1. **Full Kummer image.** The two saturated point classes remain independent modulo \(p\). The central element \(-I\) proves \(H^1(\mathrm{GL}_2(\mathbf F_p),E[p])=0\) by the cocycle identity. A proper submodule of \(E[p]^2\) is annihilated by a nonzero linear combination of its two projections. Inflation-restriction would then contradict independence. Hence \(a(\Gamma_0)=E[p]^2\).
2. **Central directions are genuinely in the image.** Commutators of actual lifts with lower blocks \(\alpha,\alpha'\) have central block \(-\alpha^tJ\alpha'+\alpha'^tJ\alpha\). Choosing the columns explicitly gives \(-2E_{11}\), \(-2E_{22}\), and \(-(E_{12}+E_{21})\). Their products and powers generate every symmetric central matrix. This is stronger than merely saying such matrices would be allowed by an ambient group.
3. **Compatibility with \(E[p^2]\).** Both commutator inputs act on \(E[p^2]\) through \(1+pM_2\), an abelian group. The commutators therefore fix \(E[p^2]\). No linear-disjointness assumption is being silently supplied.
4. **The mod-\(p^2\) lift.** For \(p\ge5\), the \(p\)-th power of every lift of a residual transvection gives the required nonzero trace-zero kernel element. Conjugation gives \(\mathfrak{sl}_2\). If the kernel had no nonzero trace, the mod-\(p^2\) cyclotomic determinant would factor through \(\mathrm{GL}_2(\mathbf F_p)\), whose abelianization has order \(p-1\). This contradicts its order-\(p\) quotient. Thus the kernel is all of \(M_2\), and the specified diagonal matrix lifting \(-I\) exists.
5. **The readout is intrinsic.** Eliminating the elliptic component of a Kummer cocycle gives \(\beta=c-b(A-I)^{-1}a\). The local quotient in §4 identifies its columns with the normalized torus Kummer classes. Depending on row/column conventions, the comparison matrix is transposed; the determinant is unaffected. Conjugation scales \(\beta\) by the cyclotomic scalar, preserving invertibility.
6. **Nonempty conjugacy class.** Multiplication by the central element with block \(tI\) preserves the mod-\(p^2\) congruence and changes \(\beta\) to \(\beta+tI\). Its determinant is a monic quadratic in \(t\), so it is nonzero for some \(t\) in every field at issue. Chebotarev then applies.

The constructed auxiliary has \(\#E(\mathbf F_\ell)\equiv4\pmod p\), so it lies in the strict no-\(p\)-torsion auxiliary domain used throughout §4. The exceptional set in the statement does not need enlargement by an unquantified 1-motive image exception.

## 6. Fresh bounded checks

The checking implementations in this audit do not import Pro's algebra checker or exact elliptic-arithmetic implementation.

`checks/group_check.py` passed over nine fields: \(p=5,7,11,13,17,19,23,29,31\). It verifies the three central generators, 720 conjugation cases, all scalar translations in those cases, and 4,076 transvection lifts modulo \(p^2\). The lift checks exhaust all corrections at 5 and 7. A control at 2 illustrates why the monic-quadratic argument needs the odd-prime restriction. Results: `results/group_check.json`.

`checks/pairing_check.gp` independently calculates the script's quadratic polarization and the translated-divisor denominator pairing. For each case it uses three different translating points, checks symmetry through equality of the full matrices, and checks doubling. The first two cases were not among the three pairing comparisons in the returned Pro report.

| \(p,\ell\) | \(\#E(\mathbf F_\ell)\) | formal multiplier | script \(H_{11},H_{12},H_{22}\) | \(\det H\) | comparison |
|---|---:|---:|---|---:|---|
| 7,29 | 30 | 30 | 2,4,3 | 4 | \(B=2H\), all three translations |
| 11,23 | 24 | 12 | 5,2,2 | 6 | \(B=2H\), all three translations |
| 17,103 | 106 | 106 | 1,12,14 | 6 | \(B=2H\), all three translations |

The deliberately incorrect normalization \(B=H\) fails in every case. These are checks of the comparison on eligible auxiliaries; they do not claim these particular Frobenius elements equal \(-I\), nor do they produce new Ota certificates.

The accepted GP run exited zero, had empty stderr, exactly three expected result rows, and the completion marker. An initial invocation changed the GP stack from inside the input file and did not execute the later checks; it was not accepted. The recorded final command supplies stack size externally. The Python and GP checks are small exact computations, not numerical-corpus extensions.

## 7. Status wording that should travel with the result

### G2 is an auxiliary-existence theorem, not a witness theorem

The proved condition is \(R_{p,\ell}\ne0\). The needed arithmetic certificate remains \(c_2(\theta_\ell)\ne0\). Their connection is precisely the unproved G1 comparison. The fit \(K\equiv288\pmod{215441}\) neither constructs the global integer nor establishes that comparison. The accompanying corrections preserve this distinction correctly.

### G1 is the frontier of this mechanism; the full program has further obligations

Suppose G1 were proved with a nonzero fixed integer \(K_E\), outside a finite set \(B\), with a unit comparison factor. Combining it with G2 and the retained Ota implication would give

\[
\Sha(E/\mathbf Q)[p^\infty]=0
\quad\text{for }p\notin B\cup S_0\cup\operatorname{Supp}(K_E).
\]

This is a finite-support conclusion. It is not yet FIN: the primary groups at the remaining primes must still be proved finite. ORDER9 additionally requires their exact values, and Q36 requires its own real/arithmetic comparison. An infinite group supported at just one prime already demonstrates the logical difference between finite support and finiteness.

If a separate theorem later shows \(K_E=288\), its prime support is then \(\{2,3\}\). That is not available from the present congruences, and even then the excluded bad primes remain unless handled separately.

I would replace “the whole program now rests on G1” by:

> G2 closes the auxiliary-existence gate for this proposed finite-support mechanism. Its remaining global comparison is G1. The finite exceptional primary groups and the exact real leading-term comparison remain separate obligations.

“Rank-two analogue of the Heegner index” can be an explanatory analogy; it is not an established identification or a uniqueness theorem for possible BSD strategies.

### Do not widen today's replay claims

This audit does not close the receipt-root gap from Part A, replay the massive coefficient corpus, or freshly certify all historical theorem dependencies. It does not alter the accepted finite-prime certificates. The chronology, interval-margin, and conditional-unit corrections are sensible distinctions, but their complete original-execution history was not independently reconstructed in this G2 audit.

## 8. Disposition

**Retain G2 at written/imported-input grade, with this independent source-and-proof review attached.** The key geometric identification survives; it should not be sent back as an unresolved objection merely because it is not in Lean. Conversely, finite matrix tests should not be substituted for that geometric review.

No new mathematical prerequisite was identified in G2 under its stated seed hypotheses. The first unresolved mathematical step in the proposed global mechanism remains the actual G1 comparison and a nonzero common integral multiplier, followed by the separate exceptional-prime and real-comparison work described above. This audit has not constructed that multiplier or selected a successor experiment.

Reproduction of the bounded checks:

```sh
cd /Users/bsm/BSD_G2_INDEPENDENT_AUDIT_CODEX_2026-09-26
/opt/miniconda3/bin/python3 checks/group_check.py
/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp -q -f -s 64000000 checks/pairing_check.gp
```

The written argument in §§3–5, rather than the check count, is the reason for the verdict.
