# The 7-primary component of the fixed seed vanishes

**Result, 2026-09-20:** for

\[
E:y^2=x^3-22735x^2+106272484x,
\qquad \Sha(E/\mathbf Q)[7^\infty]=0.
\]

**Grade:** computer-assisted theorem using the retained rank, residual-image,
modular-symbol lattice, and published Iwasawa-theoretic inputs. The basis
theorem's preprint status and the existing Manin-constant source qualifications
remain. This operation has not received an independent human review or a
second end-to-end numerical implementation. The coefficient verifier is
independent of the coefficient producer; both downstream evaluations use the
same certified modular symbols.

The exact new premise is

\[
[T^2]L_7(E,T)\equiv1\pmod7
\quad\text{in the }\omega_1\text{ convention},
\]

or 4 modulo7 in the retained Neron/full-real-period convention. Only this
residue of the infinite series is asserted. Higher-precision values of its
finite approximation are not additional certified digits of the infinite
series.

## 1. Derivation from the modular-symbol coefficient

Write \(S_b=[b/49]^+\) and \(s_a=[a/7]^+\) in the engine's \(\omega_1\)
normalization. Exact counting gives \(\#E(\mathbf F_7)=10\), hence \(a_7=-2\).
The independent coefficient stream gives the same value. Let \(\alpha\) be
the unit root of \(X^2+2X+7\), so \(\alpha\equiv5\pmod7\) and
\(\alpha\equiv26\pmod{49}\). With \(\gamma=1+7\), the depth-two polynomial is

\[
P_2(T)=\sum_{a=1}^6\sum_{j=0}^6
\left(\alpha^{-2}S_{\omega(a)8^j\bmod49}
-\alpha^{-3}s_{\omega(a)8^j\bmod7}\right)(1+T)^j.
\]

Here \(\omega\) is the Teichmuller lift. All symbols at denominators \(7^n\)
are 7-integral: those cusps are equivalent to 0, whose unweighted period is
zero, and the retained modular parametrization has Manin constant a power of2.
In particular, the computation uses the valid uniform lattice
\((1/1024)\mathbf Z\). Stein--Wuthrich Proposition3.5 gives

\[
[T^2]L_7\equiv[T^2]P_2\pmod7.
\]

The lower-level term contributes zero modulo7 since
\(\sum_{j=0}^6\binom j2=35\). Enumerating the Teichmuller exponents, folding
\(S_b=S_{49-b}\), and using \(\alpha^{-2}\equiv2\pmod7\) gives the
predeclared formula

\[
\begin{aligned}
[T^2]P_2\equiv{}&5(S_2+S_4+S_{11}+S_{13}+S_{22}+S_{23})\\
&+4(S_6+S_9+S_{10}+S_{15}+S_{16}+S_{24})\\
&+3(S_{12}+S_{17}+S_{20})\pmod7.
\end{aligned}
\]

The three parenthesized sums, obtained from the certified symbol table, are
\(-165,-512,314\). Thus the right side is

\[
5(-165)+4(-512)+3(314)=-1931\equiv1\pmod7.
\]

One exact implementation uses Fermat quotients to recover the exponents. A
second evaluates the complete depth-two measure, retaining its lower-level
contribution and using Hensel/Teichmuller arithmetic modulo \(7^{20}\). They
agree on the certified residue. Both conjugation symmetries and all twelve
\(T_7\) relations between the plus/minus symbols at49 and7 also hold exactly.
The finite constant coefficient is zero, and the finite linear coefficient
is zero modulo7, as required by the independent rank argument below.

## 2. Finiteness is proved before the leading-term order is used

The retained residual image is full, hence the 7-adic image is full. Reduction
at7 is good ordinary. Kato's good-ordinary divisibility, in
Stein--Wuthrich Theorem7.3, gives

\[
L_7(T)=f_E(T)d(T),\qquad f_E,d\in\mathbf Z_7[[T]].
\]

Theorem6.1 gives \(\operatorname{ord}_T f_E\ge2\), from the proved algebraic
rank. The coefficient just computed forces
\(\operatorname{ord}_T L_7=\operatorname{ord}_T f_E=2\) and forces the
leading coefficient of \(f_E\) to be a unit. The equality clause of Theorem6.1
therefore proves both finiteness of \(\Sha[7^\infty]\) and nondegeneracy of
the canonical 7-adic height. Neither is assumed in this inference.

The theorem's leading-term valuation formula now applies. The torsion and
Tamagawa factors are 7-units. Also
\(\epsilon_7=(1-\alpha^{-1})^2\) is a unit since
\(\alpha^{-1}\equiv3\pmod7\). Consequently

\[
0=v_7(\#\Sha[7^\infty])+v_7(\operatorname{Reg}_\gamma).
\tag{1}
\]

## 3. Regulator integrality without a numerical height computation

Use a global minimal integral model, which does not change the canonical
height. Every rational component group has order1 or2. Multiplication by20
therefore takes a rational point into the identity components at all finite
primes and into the formal group at7: the factor2 kills the component groups
and the factor10 kills \(E(\mathbf F_7)\). The integer20 is a 7-unit.

For a nontorsion point \(R\), the canonical sigma-height formula in
Stein--Wuthrich §4.1 and quadraticity give

\[
\widehat h_7(R)=\frac{2}{20^2}
\log_7\!\left(\frac{e(20R)}{\sigma_7(20R)}\right)\in7\mathbf Z_7.
\]

Indeed \(\sigma_7\in\mathbf Z_7[[t]]\) converges in the formal group, its
value at the nontorsion formal point is nonzero, and
\(\log_7(\mathbf Q_7^\times)\subset7\mathbf Z_7\), with \(\log_7(7)=0\).
Torsion points have height zero. Polarization divides by2, so every entry of
the canonical height matrix on the retained basis lies in \(7\mathbf Z_7\).
Its determinant lies in \(7^2\mathbf Z_7\). Since \(v_7(\log_7(8))=1\),

\[
\operatorname{Reg}_\gamma
=\frac{\operatorname{Reg}_7}{\log_7(8)^2}\in\mathbf Z_7.
\]

Both valuations in (1) are nonnegative; their sum is zero. Therefore
\(\Sha(E/\mathbf Q)[7^\infty]=0\). This also shows that the normalized
regulator is a unit and that the cyclotomic characteristic ideal is
\((f_E)=(T^2)\). No main-conjecture equality or p-adic BSD formula is used.

## 4. Numerical certificate and custody

The unchanged Arb engine was used with explicit Fourier truncation bounds.

| Target | Truncation | Upper bound for twice the unnormalized tail | Exact symbol values identified |
|---|---:|---:|---:|
| 49 | 15,569,256,447 | \(1.339894\cdot10^{-5}\) | 42 plus and42 minus |
| 7 | 2,147,483,647 | \(1.150802\cdot10^{-5}\) | 6 plus and6 minus |

After normalization each Arb ball has radius below \(1/2048\) and contains
exactly one point of \((1/1024)\mathbf Z\). All identified values happen to
be integers. Every Fourier coefficient needed by the finite sums is obtained
from independently verified prime coefficients and the retained Hecke rules.
There are 694,457,446 verified primes, of which566 are handled by exhaustive
counting and694,456,880 by integer group-order witnesses.

The run reused885 sealed coefficient segments, checking actual coefficient
bytes and verifier-record bytes against the old sealed manifest. Only43 new
segments, containing30,771,719 primes, were produced and independently
verified. All43 new witness files are retained. The consumed coefficient roots
are

```
m49: 0db19ef80833a5bf8b85e8d644a8b0ef7b6090ab4df8742c219eb64e108d6b86
m7:  006f85212ce6131792ae7f8fa14ebc16fe6c5b21fb1285791c65a398aa5ae857
```

The exact count identities are
\(5,076,972,991+10,492,283,456=15,569,256,447\) and
\(704,514,510+1,442,969,137=2,147,483,647\).
All5,280 atomic Arb work units have valid self-hashes, complete index sets,
and matching coefficient-segment hashes. All ten retained source/binary
identities match the preceding rigorous engine. The run took18 minutes29
seconds with12 workers and roughly1.1GB peak memory for its largest Arb task.

Load-bearing evidence:

- [Exact downstream calculation and symbol tables](../_work/active_full_bsd/p7/DOWNSTREAM.json).
- [Coefficient, witness, source/binary, and work-unit bindings](../_work/active_full_bsd/p7/CERTIFICATE_BINDINGS.json).
- [Arb output at49](../_work/active_full_bsd/p7/run/msl_m49.txt) and [at7](../_work/active_full_bsd/p7/run/msl_m7.txt).
- [Exact cross-check output](../_work/active_full_bsd/p7/run/P3_CHECK.txt).
- [Downstream code](../_work/active_full_bsd/p7/downstream.py), [custody checker](../_work/active_full_bsd/p7/seal.py), and [restartable command](../_work/active_full_bsd/p7/continue.sh).
- [Local Stein--Wuthrich primary-source text](/Users/bsm/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt): Proposition3.5, §4.1, Theorem6.1, and the good-ordinary case of Theorem7.3.
- [Retained coefficient certificate](/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/P3_CERTIFICATE.md), used only for its arithmetic/engine certificate, not its p3 main-conjecture provenance.
- [Canonical retained inputs](../MASTER_BSD_DAG.md), §2: rank/basis, image, local data, and Manin/lattice qualifications.

The computational trust base remains the retained integer verifier, Arb
engine, FLINT/Arb3.3.1, GMP6.3, MPFR4.2.2, compiler, hardware, and OS. The
new exact downstream calculations are explicitly displayed above and are
independently checked against each other. No floating estimate is used to
identify a symbol or a residue.

## 5. Exact effect on the fixed BSD obligation

This closes one previously open necessary prime component. It does not prove
finite prime support, control any other unresolved prime, or compare the
real leading term with the real regulator.

With the retained small-primary results and their qualifications, FIN would
now imply

\[
\#\Sha=9t^2,\qquad t\ge1,\quad\gcd(t,210)=1.
\]

The next possible order is1089, replacing441 under these stronger inputs.
Thus a uniform bound \(\#\Sha[n]<1089\) for all \(n\ge1\) would now force
order9, by the same finite-exhaustion argument already in the master.
No such bound has been proved here. Full FIN, order9, and \(q=36\) remain open.
