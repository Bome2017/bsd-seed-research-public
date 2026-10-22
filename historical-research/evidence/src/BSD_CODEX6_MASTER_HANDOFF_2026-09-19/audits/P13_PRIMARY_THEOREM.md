# The 13-primary component of the fixed seed vanishes

**Result, 2026-09-21:** for

\[
E:y^2=x^3-22735x^2+106272484x,
\qquad \Sha(E/\mathbf Q)[13^\infty]=0.
\]

**Grade:** computer-assisted theorem with the retained rank/basis, full residual-image, modular-symbol lattice, local-reduction and published Iwasawa-theoretic inputs. The basis theorem's preprint status and the Manin-constant source qualifications remain. This completion review is not a Lean proof, independent human review, fresh replay of the full integer witness verifier, or second end-to-end numerical implementation. It checks the original verifier receipts and actual witness bytes, recombines the saved Arb units with the unchanged engine, and independently evaluates the exact downstream coefficient in two ways.

The certified new arithmetic input is

\[
C_{13}:=[T^2]L_{13}(E,T)\equiv2\pmod{13}
\]

in the retained \(\omega_1\) convention, or **1** for the full real period \(\Omega_E=2\omega_1\). The returned values 7 and 8 are both misnormalized; their nonvanishing conclusion survives. The exact corrections are proved below. Only one digit of the infinite series is certified.

## 1. Exact coefficient and normalization

The predeclared [evaluation gate](../_work/bridge_repair_assessment_2026-09-21/P13_EVALUATION_GATE.md) fixes the generator \(\gamma=14\), the symbols \(S_b=[b/169]^+\), \(s_a=[a/13]^+\), and the coefficient formula before the numerical run. Exact point counting agrees with the independently verified coefficient stream:

\[
\#E(\mathbf F_{13})=18,\qquad a_{13}=-4.
\]

Thus 13 is good ordinary and nonanomalous. The unit root of \(X^2+4X+13\) has

\[
\alpha\equiv9\pmod{13},\quad \alpha\equiv126\pmod{169},
\quad \alpha^{-1}\equiv3,\quad \alpha^{-2}\equiv9\pmod{13}.
\]

With \(\omega(a)\) the Teichmuller lift, put

\[
P_2(T)=\sum_{a=1}^{12}\sum_{j=0}^{12}
\left(\alpha^{-2}S_{\omega(a)14^j\bmod169}
-\alpha^{-3}s_{\omega(a)14^j\bmod13}\right)(1+T)^j.
\]

The retained Manin argument makes the symbols at all denominators \(13^n\) 13-integral: these cusps are equivalent to 0, the central unweighted period vanishes, and the parametrization's Manin constant is a power of two. The engine uses the valid uniform lattice \((1/1024)\mathbf Z\). Stein--Wuthrich Proposition 3.5 therefore gives

\[
C_{13}\equiv[T^2]P_2(T)\pmod{13}.
\]

For a unit \(b\bmod169\),

\[
j(b)\equiv-\frac{b^{12}-1}{13}\pmod{13},\qquad 0\le j(b)\le12.
\]

The lower-level quadratic term vanishes modulo13 because its symbol is independent of \(j\) and \(\sum_{j=0}^{12}\binom j2=286\). Conjugation gives \(S_b=S_{169-b}\) and \(j(b)=j(169-b)\). Consequently the folded weight is

\[
w(b)=2\alpha^{-2}\binom{j(b)}2\equiv18\binom{j(b)}2\pmod{13}.
\]

The six groups fixed before the run give the following exact sums of **symbols**, not lattice numerators:

| Weight | Folded representatives \(b\) | Sum of \(S_b\) |
|---|---|---:|
| 1 | 4, 18, 58, 76, 77, 81 | 163 |
| 2 | 11, 25, 28, 32, 35, 40, 43, 60, 68, 73, 75, 84 | -138 |
| 4 | 2, 7, 8, 9, 15, 17, 29, 36, 38, 44, 46, 53 | 272 |
| 5 | 5, 6, 12, 27, 31, 37, 54, 55, 59, 62, 74, 82 | -52 |
| 10 | 20, 33, 42, 47, 48, 49, 50, 56, 64, 67, 79, 83 | -230 |
| 11 | 3, 10, 21, 24, 41, 45, 51, 57, 61, 66, 69, 71 | -215 |

It follows that

\[
C_{13}\equiv163+2(-138)+4(272)+5(-52)+10(-230)+11(-215)
=-3950\equiv2\pmod{13}.
\]

The alternative returned weights omit \(\alpha^{-2}\). Their ratio to the predeclared weights is \(9^{-1}=3\); folding contributes the same factor two in both formulas. Separately, the returned evaluation uses the integer lattice candidates \(Z_b=1024S_b\). The exact symbol files already divide by 1024. Since \(1024\equiv10\) and \(1024^{-1}\equiv4\pmod{13}\), both returned residues have an exact explanation:

\[
7\cdot4=2\pmod{13},\qquad 8\cdot4\cdot9=2\pmod{13}.
\]

The lattice inverse and the interpolation factor \((1-\alpha^{-1})^2\) both happen to be 4 modulo13; they have distinct definitions and are not interchangeable.

An independent downstream calculation constructs the Hensel unit root and Teichmuller lifts modulo \(13^{20}\) and evaluates the full finite measure, retaining the lower-level term. Its constant, linear and quadratic coefficients reduce to \((0,0,2)\) modulo13. The finite constant coefficient is exactly zero, and the lower-level quadratic term is zero modulo13. These are not extra certified digits of the infinite series. The same implementation reproduces the retained residues at 7 and 11. All 179 exact checks pass, including the predeclared weights, conjugation and 24 two-level Hecke identities. Both downstream calculations share the certified symbol tables.

## 2. From the unit coefficient to 13-primary vanishing

The retained full residual-image theorem and lifting argument give full 13-adic image. Kato's integral good-ordinary divisibility, in Stein--Wuthrich Theorem 7.3, gives

\[
L_{13}(T)=f_E(T)d(T),\qquad f_E,d\in\mathbf Z_{13}[[T]].
\]

The retained algebraic rank is two. Theorem 6.1 gives \(\operatorname{ord}_T f_E\ge2\). The computed unit quadratic coefficient then forces \(\operatorname{ord}_T L_{13}=\operatorname{ord}_T f_E=2\), with unit quadratic leading coefficients. The equality clause of Theorem 6.1 yields finiteness of \(\Sha[13^\infty]\) and nondegeneracy of the canonical 13-adic height. These are conclusions, not hypotheses supplied to the leading-term formula.

The torsion and Tamagawa factors are 13-units, as is \((1-\alpha^{-1})^2\equiv4\pmod{13}\). Thus the leading-term valuation formula reads

\[
0=v_{13}(\#\Sha[13^\infty])+v_{13}(\operatorname{Reg}_\gamma).
\tag{1}
\]

Every rational component group has order one or two. On a global minimal integral model, multiplication by \(36=2\#E(\mathbf F_{13})\), a 13-unit, sends every rational point into all identity components and into the formal group at13. The canonical sigma-height formula and quadraticity give, for a nontorsion point,

\[
\widehat h_{13}(P)=\frac{2}{36^2}
\log_{13}\!\left(\frac{e(36P)}{\sigma_{13}(36P)}\right)
\in13\mathbf Z_{13}.
\]

Here \(\sigma_{13}(t)=t+O(t^2)\in\mathbf Z_{13}[[t]]\); its quotient by a nonzero formal parameter \(t\in13\mathbf Z_{13}\) is a unit. The logarithm, with \(\log_{13}(13)=0\), sends \(\mathbf Q_{13}^{\times}\) into \(13\mathbf Z_{13}\). Torsion has zero height. Polarization divides by the unit two, so the height matrix on the retained rational basis has entries in \(13\mathbf Z_{13}\). As \(v_{13}(\log_{13}(14))=1\),

\[
\operatorname{Reg}_\gamma
=\frac{\operatorname{Reg}_{13}}{\log_{13}(14)^2}\in\mathbf Z_{13}.
\]

Both terms of (1) are nonnegative. Therefore \(\Sha[13^\infty]=0\). The normalized regulator is a unit and the characteristic ideal is \((T^2)\). No main-conjecture equality, prior FIN, auxiliary twist, or specialized anticyclotomic ideal evaluation is used.

## 3. Numerical certificate, replay and incident boundary

| Denominator | Truncation | Printed bound for twice the unnormalized Fourier tail | Identified symbols |
|---|---:|---:|---|
| 169 | 55,046,045,695 | \(1.364252466\cdot10^{-5}\) | 156 plus and 156 minus |
| 13 | 4,026,531,839 | \(1.259222293\cdot10^{-5}\) | 12 plus and 12 minus |

The printed decimals summarize the tails; the engine's Arb inequalities and unique-lattice-point tests are the certificate. Every enclosure identifies one element of \((1/1024)\mathbf Z\); the returned symbols happen to be integers. The exact traversal count identities are

\[
17,890,280,962+37,155,764,733=55,046,045,695,
\]
\[
1,318,345,297+2,708,186,542=4,026,531,839.
\]

The coefficient roots are

```
m169: 67099795305a955062008373ff0f845027e47c3a34b16eb81706963bc45f58f5
m13:  38cdd26014b0206e4cf3debabe59466de42856bd6fc0206459288ea4589e8398
```

The run uses 3,281 coefficient segments: 2,333 reused and 948 new. This review rehashed all coefficient/verifier files and matched every reused segment against the pre-incident C11 bindings. All new witness bytes were hashed against their original witness receipts, with headers and verifier records checked. Those receipts account for 2,324,085,832 verified primes, including 647,323,696 new primes. The full integer witness verifier was not rerun in this review.

All 17,605 saved Arb work units pass their hash, range, serialized-entry and coverage checks. The ten retained engine source/binary/script identities are unchanged. Fresh recombination with that same unchanged engine reproduces both original Arb outputs **byte for byte**. Fresh Stage C reproduces the exact symbol tables and the original `P3_CHECK_PASS failures=0` output, including all 24 Hecke identities. This is a replay of final interval assembly, not a fresh traversal or independent numerical implementation.

The external [incident record](/Users/bsm/BSD_SEED_P13_RUN_2026-09-21/INCIDENT_2026-09-21.md) remains load-bearing provenance. The initial launch omitted completion markers for reused segments and wrote through symlinks into earlier corpus files before being stopped. It is false that those files were never written. The subsequent checks, independently repeated here against the old C11 hashes, prove that all 2,333 retained coefficient/verifier contents match their pre-incident identities. The corrected run then generated the new segments. This review leaves the external source/run artifacts unchanged.

The successful run finished at 16:09:32 PDT, after 2h35m27s. Its reported peak RSS was 1,092,530,176 bytes (about 1.02 GiB). Timing and memory are execution observations, not certificate conditions.

Load-bearing evidence:

- [Exact downstream results](../_work/active_full_bsd/p13/DOWNSTREAM.json), [implementation](../_work/active_full_bsd/p13/downstream.py) and [normalization reconciliation](../_work/active_full_bsd/p13/NORMALIZATION.md).
- [Input and prior-state identities](../_work/active_full_bsd/p13/INPUT_BINDINGS.json) and [full coefficient, witness, engine and work-unit bindings](../_work/active_full_bsd/p13/CERTIFICATE_BINDINGS.json).
- [Completion review](../_work/active_full_bsd/p13/COMPLETION_REVIEW.json), [custody checker](../_work/active_full_bsd/p13/seal.py), and [saved-unit replay](../_work/active_full_bsd/p13/replay_completion.py).
- [Recombined Arb output at169](../_work/active_full_bsd/p13/fresh_m169.txt), [at13](../_work/active_full_bsd/p13/fresh_m13.txt), and [fresh Stage C checks](../_work/active_full_bsd/p13/STAGE_C_REPLAY.log).
- [Exact symbols at169](../_work/active_full_bsd/p13/stage_c_replay/SYMBOLS_m169.txt) and [at13](../_work/active_full_bsd/p13/stage_c_replay/SYMBOLS_m13.txt).
- [Predeclared functional and implication](../_work/bridge_repair_assessment_2026-09-21/P13_EVALUATION_GATE.md), [retained fixed-prime proof at11](P11_PRIMARY_THEOREM.md), and [canonical input qualifications](../MASTER_BSD_DAG.md), §2.
- [Stein--Wuthrich source](/Users/bsm/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt), Proposition 3.5, §4.1, Theorems 6.1 and 7.3.

The retained verifier, Arb engine, libraries, compiler, hardware and OS remain in the computational trust base. The published theorems are imported with the existing source qualifications; their full proofs were not re-audited here.

## 4. Endpoint and precise supersession

This closes the previously unresolved 13-primary component. Under FIN, the retained small-primary inputs and Cassels--Tate square order now give

\[
\#\Sha=9t^2,\qquad t\ge1,\qquad \gcd(t,30030)=1.
\]

The next possible order is \(9\cdot17^2=2601\). It is sharp under these abstract inputs, witnessed by \((\mathbf Z/3)^2\oplus(\mathbf Z/17)^2\) with alternating perfect pairings. The earlier thresholds 441, 1089 and 1521 remain correct under their earlier, weaker inputs. A uniform bound \(\#\Sha[n]<2601\) for every \(n\) would imply finiteness by the increasing exhaustion \(\Sha[m!]\), then order nine; no such bound is supplied.

This theorem supersedes precisely (a) the gate's unevaluated C13 premise, (b) the returned 7/8 normalized values and unresolved scale discrepancy, and (c) the current-threshold claim of 1521. The original external `RESULT.json`, `STATE.json`, `RESUME.md`, incident and preflight files are preserved as historical evidence; stale execution fields there do not authorize restarting the completed run. The prior source statements and earlier fixed-prime proofs are not rewritten.

**FIN, total order nine, and \(q=36\) remain open.** This theorem supplies no uniform tail, no vanishing of the auxiliary twist's 13-primary group, and no evaluation of the anticyclotomic ideal \(I_3\). No successor computation is launched.
