# The 11-primary component of the fixed seed vanishes

**Result, 2026-09-20 (completed 2026-09-21 02:55 UTC):** for

\[
E:y^2=x^3-22735x^2+106272484x,
\qquad \Sha(E/\mathbf Q)[11^\infty]=0.
\]

**Grade:** computer-assisted theorem using the retained rank, full residual-image, modular-symbol lattice, local reduction, and published Iwasawa-theoretic inputs. The retained basis theorem's preprint status and the Manin-constant source qualifications remain. This is not a Lean formalization, independent human review, or second end-to-end numerical implementation. The integer coefficient verifier is independent of the producer; the two downstream coefficient calculations share the certified symbols.

The new arithmetic premise is

\[
C_{11}:=[T^2]L_{11}(E,T)\equiv8\pmod{11}
\]

in the engine's \(\omega_1\) convention, or 4 in the retained full-real-period convention \(\Omega_E=2\omega_1\). Only one digit of the infinite series is certified. The higher-precision finite depth-two polynomial is not additional precision on that series.

## 1. The computed coefficient

Write \(S_b=[b/121]^+\) and \(s_a=[a/11]^+\). Exact point counting and the independently verified coefficient stream agree that \(\#E(\mathbf F_{11})=14\) and \(a_{11}=-2\). Reduction is good ordinary. The unit root \(\alpha\) of \(X^2+2X+11\) satisfies \(\alpha\equiv9\pmod{11}\) and \(\alpha\equiv64\pmod{121}\). With \(\gamma=12\),

\[
P_2(T)=\sum_{a=1}^{10}\sum_{j=0}^{10}
\left(\alpha^{-2}S_{\omega(a)12^j\bmod121}
-\alpha^{-3}s_{\omega(a)12^j\bmod11}\right)(1+T)^j,
\]

where \(\omega\) is the Teichmuller lift. Symbols at every denominator \(11^n\) are 11-integral by the retained Manin/lattice argument: these cusps are equivalent to 0, the unweighted central period vanishes, and the Manin constant is a power of two. The calculation uses the uniform lattice \((1/1024)\mathbf Z\). Stein--Wuthrich Proposition 3.5 therefore gives \(C_{11}\equiv[T^2]P_2\pmod{11}\).

The lower-level contribution is zero modulo11 because \(\sum_{j=0}^{10}\binom j2=165\). For a unit \(b\bmod121\), its cyclotomic exponent is

\[
j(b)\equiv-\frac{b^{10}-1}{11}\pmod{11}.
\]

Using \(\alpha^{-2}\equiv3\pmod{11}\) and \(S_b=S_{121-b}\), the predeclared folded formula is

\[
C_{11}\equiv\sum_{w\in\{2,3,5,6,7\}}w\sum_{b\in B_w}S_b\pmod{11},
\]

with the following **computed** exact sums:

| Weight \(w\) | Set \(B_w\), fixed before computation | \(\sum_{b\in B_w}S_b\) |
|---|---|---:|
| 2 | 2, 6, 18, 41, 54 | -110 |
| 3 | 5, 14, 15, 17, 25, 32, 42, 45, 46, 51 | -70 |
| 5 | 8, 20, 24, 26, 43, 47, 49, 56, 59, 60 | -10 |
| 6 | 10, 16, 23, 28, 30, 31, 35, 37, 48, 52 | 102 |
| 7 | 7, 19, 21, 29, 34, 38, 50, 53, 57, 58 | -46 |

Thus

\[
2(-110)+3(-70)+5(-10)+6(102)+7(-46)=-190\equiv8\pmod{11}.
\]

One implementation uses integer Fermat quotients. The other evaluates the complete depth-two measure, including its lower-level correction, with Hensel and Teichmuller arithmetic modulo \(11^{20}\). Both give residue 8. The finite constant coefficient is zero, the finite linear coefficient is zero modulo11, and the lower-level quadratic correction is zero modulo11. Both conjugation symmetries and all twenty two-level Hecke identities hold exactly. The completion review separately recomputes the displayed sums from the symbol table and the prelaunch formula record.

## 2. Finiteness before the leading-term formula

The retained full residual image at11 lifts to full 11-adic image. Kato's good-ordinary divisibility, as stated in Stein--Wuthrich Theorem 7.3, gives

\[
L_{11}(T)=f_E(T)d(T),\qquad f_E,d\in\mathbf Z_{11}[[T]].
\]

The retained algebraic rank is two, so Theorem 6.1 gives \(\operatorname{ord}_T f_E\ge2\). The computed unit quadratic coefficient forces both orders to be two and the quadratic leading coefficient of \(f_E\) to be a unit. The equality clause of Theorem 6.1 now proves finiteness of \(\Sha[11^\infty]\) and nondegeneracy of the canonical 11-adic height. Neither is assumed beforehand.

The torsion and Tamagawa factors are 11-units, as is \(\epsilon_{11}=(1-\alpha^{-1})^2\equiv5\pmod{11}\). The leading-term valuation formula therefore gives

\[
0=v_{11}(\#\Sha[11^\infty])+v_{11}(\operatorname{Reg}_\gamma).
\tag{1}
\]

Every rational component group has order one or two. On a global minimal integral model, multiplication by \(28=2\#E(\mathbf F_{11})\), an 11-unit, takes any rational point into all identity components and into the formal group at11. For a nontorsion point \(P\), the canonical sigma-height formula and quadraticity give

\[
\widehat h_{11}(P)=\frac{2}{28^2}
\log_{11}\!\left(\frac{e(28P)}{\sigma_{11}(28P)}\right)
\in11\mathbf Z_{11}.
\]

Here \(\sigma_{11}(t)=t+O(t^2)\in\mathbf Z_{11}[[t]]\); at a nonzero formal parameter in \(11\mathbf Z_{11}\), its quotient by \(t\) is a unit. The logarithm sends \(\mathbf Q_{11}^{\times}\) into \(11\mathbf Z_{11}\), with \(\log_{11}(11)=0\). Torsion has height zero. Polarization divides by the unit 2, so the canonical height matrix on the retained rational basis has entries in \(11\mathbf Z_{11}\). Since \(v_{11}(\log_{11}(12))=1\),

\[
\operatorname{Reg}_\gamma
=\frac{\operatorname{Reg}_{11}}{\log_{11}(12)^2}\in\mathbf Z_{11}.
\]

Both terms in (1) are nonnegative. Hence \(\Sha[11^\infty]=0\), the normalized regulator is a unit, and the cyclotomic characteristic ideal is \((T^2)\). No main-conjecture equality or prior finiteness assumption is used.

## 3. Certificate and custody

The unchanged Arb engine identifies every symbol using an explicit Fourier tail and the retained lattice.

| Denominator | Truncation | Reported bound for twice the unnormalized tail | Identified symbols |
|---|---:|---:|---|
| 121 | 39,141,244,927 | \(1.366424655\cdot10^{-5}\) | 110 plus and 110 minus |
| 11 | 3,388,997,631 | \(1.312158070\cdot10^{-5}\) | 10 plus and 10 minus |

The displayed decimal tails are the engine's printed values; its Arb interval inequalities and lattice containment/uniqueness flags are the certifying tests. Every normalized enclosure contains exactly one point of \((1/1024)\mathbf Z\). The identified symbols happen to be integers.

All 2,333 prime-coefficient segments were verified. The run rehashed and reused 928 previously sealed segments and produced 1,405 new segments, with all new integer witnesses retained. The total is 1,676,762,136 verified primes, including 982,304,690 new primes; 566 are handled by the retained exhaustive-counting branch. All 12,675 atomic Arb work units pass their self-hash, index-coverage and input-binding checks. The ten retained engine source/binary/script identities are unchanged. There are 248 exact downstream checks, all passing.

The coefficient roots are

```
m121: 01dd10873593119341ca7550c3f8fd5e002f4de9ce77a9b1d4866c6ba3d00c66
m11:  c219a9b3e682f0c41b5bd3373fa150934a13b7f6fbb665cba8b4390bf4d11391
```

The count identities are \(12,732,120,947+26,409,123,980=39,141,244,927\) and \(1,110,879,230+2,278,118,401=3,388,997,631\). Computation through sealing took about 3 hours 10 minutes with 12 workers; the larger Arb stage reported about 1.09 GB peak memory footprint.

Load-bearing evidence:

- [Exact coefficient calculations and symbols](../_work/active_full_bsd/p11/DOWNSTREAM.json).
- [Full coefficient, witness, engine and Arb bindings](../_work/active_full_bsd/p11/CERTIFICATE_BINDINGS.json).
- [Completion review and independently re-summed predeclared formula](../_work/active_full_bsd/p11/COMPLETION_REVIEW.json).
- [Arb output at121](../_work/active_full_bsd/p11/run/msl_m121.txt), [at11](../_work/active_full_bsd/p11/run/msl_m11.txt), and [exact Hecke/lattice checks](../_work/active_full_bsd/p11/run/P3_CHECK.txt).
- [Downstream code](../_work/active_full_bsd/p11/downstream.py) and [custody checker](../_work/active_full_bsd/p11/seal.py).
- [Prelaunch implication](../_work/active_full_bsd/p11/PROOF.md), preserved in its original conditional form; the missing numerical premise is supplied above.
- [Retained fixed-prime argument at7](P7_PRIMARY_THEOREM.md) and [canonical seed inputs](../MASTER_BSD_DAG.md), Section 2.
- [Local Stein--Wuthrich source](/Users/bsm/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt), Proposition 3.5, Section 4.1, Theorems 6.1 and 7.3.

The trust base remains the retained integer verifier, Arb engine, libraries, compiler, hardware and OS, together with the explicitly retained mathematical inputs. The numerical pipeline has not been independently reimplemented.

## 4. Exact endpoint effect

This closes the previously unresolved 11-primary component. Under FIN and the other retained small-primary inputs, the square-order consequence now reads

\[
\#\Sha=9t^2,\qquad t\ge1,\qquad \gcd(t,2310)=1.
\]

The next possible order under those inputs is \(9\cdot13^2=1521\). Thus the sufficient uniform bound \(\#\Sha[n]<1521\) for every \(n\ge1\) would force order nine by finite exhaustion and square order. No such bound is proved here. FIN, total order nine, and \(q=36\) remain open. No other prime or successor computation is launched.
