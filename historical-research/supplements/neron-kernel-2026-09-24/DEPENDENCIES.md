# Mathematical dependencies and source grade

The labels use the existing [research vocabulary](../../claims/LABELS.md). `PROVED_WRITTEN` means a written deduction relative to the named imports, not independent human endorsement or Lean verification. These imports were source-checked in the retained reviews; this transfer preserves that reading grade rather than claiming another reproof.

| Input or deduction | Exact scope | Grade / review boundary |
|---|---|---|
| Existing A.1 | Seed model, conductor, local reductions and inertia | Retained exact arithmetic; same model and differential |
| Existing A.3 | Full residual image at every odd prime | Retained written application of published results |
| Existing A.4 and manuscript Appendix F | Chosen optimal map followed, if necessary, by the rational 2-isogeny; \(c_E\mid2^9\) | Retained written geometric argument with its named imports; not freshly reproved here |
| Lab `01_THETA_KERNEL.md`, Theorem A | Stabilizer weights one, primitive one-dimensional \(f\)-line, \(B(1)=\mathrm{Id}\), kernel \(\psi(x)\psi(y)/M\) | Prior audited written derivation. No assertion that all bad-prime Hecke or global congruence identities follow from the elementary rank-one lattice statement |
| Lab `03_NELSON_CONTINUATION.md`, Lemmas 4 and 4′ | Plain weight-two slash expansion by Poisson summation; split and division-place Gauss sums | Retained written derivation. Small exact checks here cover Eichler sums; the general division-place identity remains a written input |
| Kim–Ota, §6.1, Assumption 6.3, Theorem 6.5, Corollary 6.7 | Quaternionic pairing ideal and classical congruence ideals under CR+ | `IMPORTED_PUBLISHED`; hypotheses checked at the seed in the copied Phase 1 proof |
| Kim–Ota, Remark 6.6(1) | Low-weight crystalline extension at nonordinary good primes | Explicit published import; its short deformation-theoretic justification is not reproved in this project. No use of §6.2's ordinary hypothesis to justify this extension |
| Full Hecke / integral cuspform duality | \(\eta_f(N)\mathbf Z_p=r\mathbf Z_p\) for the full congruence number | Standard duality imported; the lattice identification is written out in Phase 1 §4 |
| Agashe–Ribet–Stein, Theorem 2.1 (and Theorem 3.6, Remark 3.7) | \(v_p(r)=v_p(d)\) for the optimal elliptic quotient at good primes | `IMPORTED_PUBLISHED`; \(d\) is the optimal modular degree, not an unspecified parametrization's degree |
| Česnavičius–Neururer–Saha, Proposition 5.14 | General cuspform differential-lattice criterion, plain slash coefficients, \(v_q(q)=1\) | `IMPORTED_PUBLISHED`; it is not the narrower normalized-newform Theorem 5.15 |
| CNS, Proposition 6.2, Example 6.3, Theorem 6.12 | Néron cotangent lattice identified using rational singularities | `IMPORTED_PUBLISHED`; all primes covered, including 2 since \(3\mid N\) and \(3\equiv3\pmod4\) |
| Néron pullback | \(i_E^*\omega_G=(ed/c_E)\lambda_f(G)\omega_E\) | Written deduction from the chosen dual map and Hecke projection; only one Manin factor after pullback |
| Existing B.5 | \(M_2(p)\ne0\Rightarrow\Sha(E/\mathbf Q)[p^\infty]=0\) for good \(p\ge5\), \(p\nmid7N\) | Existing conditional bridge. Its previously Lean-checked algebra does not make this supplement Lean-checked |

## Published sources

1. Chan-Ho Kim and Kazuto Ota, *On the quantitative variation of congruence ideals and integral periods of modular forms*: [arXiv:1905.02926v4](https://arxiv.org/pdf/1905.02926v4).
2. Amod Agashe, Kenneth Ribet and William Stein, *The modular degree, congruence primes, and multiplicity one*: [author-hosted manuscript](https://www.math.fsu.edu/~agashe/math/moddeg3.pdf).
3. Kęstutis Česnavičius, Michael Neururer and Abhishek Saha, *The Manin constant and the modular degree*: [arXiv:1911.09446v3](https://arxiv.org/pdf/1911.09446v3).

The exact local PDF and text hashes are preserved in [PRIMARY_SOURCE_BINDINGS.json](reviews/codex/PRIMARY_SOURCE_BINDINGS.json). Source-reading details are in [SOURCE_CHECKS.md](reviews/pro6/SOURCE_CHECKS.md). Publications are not included in this repository.

## New claims and what was actually tested

NK.1 and NK.2 are `PROVED_WRITTEN` with `IMPORTED_PUBLISHED` dependencies. NK.3 is a conditional sufficient criterion, with exact arithmetic checks of the acceptance rule. All three have cross-family model review at the recorded scope; none has independent human review.

The 262 exact checks prove those finite identities, not the general theta transformation or any published theorem. Numerical period comparisons and floating Gauss checks in the source reports are `NUMERICAL_EVIDENCE`. They are not load-bearing rigorous error certificates. No large coefficient corpus, Gross packet or seed analytic value was replayed for this supplement.
