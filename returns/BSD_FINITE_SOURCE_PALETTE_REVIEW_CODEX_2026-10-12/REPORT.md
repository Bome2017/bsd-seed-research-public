# Finite-source palette: reviewed normalization and seed consequence

Date: 2026-10-12.

**Verdict: SOURCE_COMPARISON_SUPPORTED_UNDER_RETAINED_INPUTS; ORIGINAL_PERIOD_RECEIPT_BOUND; NO_NEW_SEED_VALUE_OR_BOUND.**

The submitted normalization proof passes this review for its newly specified source family. The previously unspecified source-lattice index is removed on the stated domain. In particular, the standard ordinary modular-symbol coefficient can replace the actual-source coefficient in the reviewed primary-vanishing certificate, without an additional unknown normalization-prime exclusion.

This is a written mathematical review with separate model-agent audits and executable replay, not independent human certification, formal verification, a novelty assessment, or an end-to-end recertification of the antecedent seed/Kato inputs. No Kato coefficient, modular symbol, height determinant, or Selmer group was newly evaluated. FIN, ORDER9 and Q36 remain unchanged.

## 1. What was checked

The submitted eight files agree byte-for-byte with [lab commit 5110be8805f202ebc9a4a112ec0854fd764a620c](https://github.com/Bome2017/bsd-seed-lab/tree/5110be8805f202ebc9a4a112ec0854fd764a620c/work/returns/BSD_FINITE_SOURCE_PALETTE_2026-10-12), on its separate `research/finite-source-palette-2026-10-12` branch. Their seven manifest entries verify. The supplied checker reproduces its saved output byte-for-byte.

The two substantive review tasks were:

1. Check that the actual BKS open-cohomology image equals the Tate lattice for the chosen map, rather than being merely homothetic to it. See [LATTICE_AUDIT.md](LATTICE_AUDIT.md).
2. Locate the original 144 receipt, bind its differential and period to this map, and check full ordinary interpolation. See [PERIOD_AUDIT.md](PERIOD_AUDIT.md) and [PERIOD_BINDINGS.json](PERIOD_BINDINGS.json).

Both tasks pass under their explicitly retained arithmetic inputs. The source and receipt clarifications below are additive; the submitted files remain unchanged.

## 2. The source-lattice argument is integral

Fix the connected-kernel quotient and least-degree rational isogeny

\[
J_1(N)\twoheadrightarrow E_1\xrightarrow{\psi}E.
\]

If a retained irreducible coefficient prime divided the degree of \(\psi\), the dual isogeny's kernel would contain all of \(E[p]\). Factoring it through \([p]\) would contradict minimality. Thus \(\psi\) is prime to \(p\). Connectedness supplies integral surjectivity on Tate modules, so the proper-curve image is literally \(T_pE\).

The rational Manin–Drinfeld retraction is Galois equivariant and agrees with the identity on proper cohomology. Consequently any finite enlargement

\[
D_p=T_\phi/T_pE
\]

is a quotient of the degree-zero cusp permutation module. The cusps are cyclotomic, so this quotient has abelian Galois action. But it also embeds in \(E[p^\infty]\). A nonzero \(D_p[p]\) would give a nonzero vector fixed by the commutator image \(\mathrm{SL}_2(\mathbf F_p)\), impossible in its standard representation. Therefore \(D_p=0\).

The printed BKS map uses pushforward and integral Weil self-duality. No modular-degree division is hidden in this argument. The purity twist cancels the coefficient twist on the cusp boundary. No cusp-count denominator is introduced.

The resulting Betti statement is equality after localization at each \(p\ge5\); it is not a claim of equality of the global integral lattices at 2 and 3. Nor does it authenticate a different map obtained by postcomposing with \([p]\).

## 3. The 144 receipt now has an exact source binding

The submission cited the value without its original receipt path. The audit recovered the preserved September 19 files from the lab's pinned v0.2.6 evidence:

- `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/SYMBOLS_m5.txt`: row `1 144 -8`.
- `run/msl_m5.txt`: the original ball and unique denominator-lattice identification.
- `P5_CERTIFICATE.md`: the period, denominator, and exact-reconstruction conventions.
- `BSD_RIGOROUS_STREAM_CORE_2026-09-19/DESIGN.md` and `src/arbcore.c`: normalized-newform integrand and real period.

The three receipt files match their historical manifest. Nine supporting files match the pinned baseline commit. Small byte-identical copies and complete paths/hashes are included in this return. These checks authenticate the historical record; they do not replay its large numerical coefficient corpus or reprove the denominator theorem used for its reconstruction.

The actual receipt is \(\operatorname{Re}\lambda_f(1/5)/\omega_1=144\), using the normalized newform. Its model change to the current minimal seed has \(u=1\), so the invariant differential is unchanged. The seed has \(\Omega_E=2\omega_1\). For the chosen map,

\[
\phi^*\omega_E=\mu_\phi\omega_f,\qquad
\boxed{\Omega_\xi/\Omega_E=\pm72\mu_\phi.}
\]

The sign is fixed by the orientation and differential choices. The good-prime Manin theorem, CNS Lemma 6.5 in its correct direction, and the prime-to-\(p\) isogeny give \(\mu_\phi\in\mathbf Z_p^\times\). This supplies the exact period binding needed for the primitive plus source. It is stronger documentation than the submission's two alternative interpretations of the receipt; the actual interpretation is now fixed.

## 4. Three smoothing pairs remove source exceptions, not arithmetic content

For \(M=6N\) and \(c_i=1+iM\), every good \(p\ge5\) divides at most one \(c_i\), and divides none of \(c_i-1\). Thus one of the three fixed pairs has admissible, unit augmentation \(cd(c-1)(d-1)\). This is a proof for all such primes, not an inference from the 1,132 coverage controls.

At a fixed prime, any two admitted pairs with unit augmentation have smoothing series whose ratio is a unit in \(\mathbf Z_p[[U]]\). The full reciprocity comparison shows their actual Coleman images differ by that unit. Since the coefficients below degree two vanish, their quadratic coefficients have the same valuation. Thus selecting a different admitted pair cannot lower the intrinsic excess content or turn an arithmetic failure into a pass. The palette removes artificial source exceptions; it does not create independent nonvanishing witnesses.

The first historical pair is inadmissible at 5, whereas the new second/third pair is admissible there. This repairs that source choice and is not a new result about \(\Sha[5]\). The gcd identity for the three augmentations is not a fixed annihilator of Sha.

## 5. The resulting ordinary seed certificate

Use exactly the specified minimal Neron period, ordinary unit root, character convention and coordinate \(U=\gamma-1\). Let

\[
L_{2,p}=[U^2]L_{\mathrm{std},p},\qquad
\mathcal D_{\mathrm{ord}}=
\{p\ge5:p\nmid N,\ p\notin\{19,59,487\},\ E\text{ ordinary at }p\}.
\]

The full interpolation comparison retains exactly one coefficient-prime Euler cancellation. For the newly selected actual source it gives

\[
K_p=t_{c,d}(0)\frac{\Omega_E}{\Omega_\xi}
\frac{17469664}{13105849}L_{2,p},
\]

up to an integral unit if a unit coordinate choice remains unspecified. Every displayed multiplier is a unit on \(\mathcal D_{\mathrm{ord}}\), because

\[
\frac{17469664}{13105849}
=\frac{2^5\cdot19\cdot59\cdot487}{2243\cdot5843}.
\]

Therefore \(K_p\) and \(L_{2,p}\) vanish together and have identical valuations when nonzero. No further unknown source-lattice index has to be removed for this family.

Composing with the retained, reviewed Bockstein certificate gives

\[
\boxed{
L_{2,p}\ne0,\quad\det H_p\ne0,\quad
v_p(L_{2,p})-v_p(\det H_p)\le1
\ \Longrightarrow\ \Sha(E/\mathbf Q)[p^\infty]=0
}\qquad(p\in\mathcal D_{\mathrm{ord}}).
\]

Here \(H_p\) is the matched BKS height matrix on the saturated point basis in the same \(U\)-coordinate. A raw numerical height determinant in a different logarithmic coordinate cannot be substituted unchanged. The nonzero coefficient supplies the nonzero-derivative branch through the retained reciprocity comparison before primary finiteness is used.

When the two nonzero hypotheses hold, the retained defect-inclusive identity becomes

\[
v_p(L_{2,p})-v_p(\det H_p)
=\operatorname{length}_{\mathbf Z_p}\Sha[p^\infty]+e_p,
\qquad e_p\ge0.
\]

The new source normalization gives no upper bound for this difference or for \(e_p\), and does not prove \(e_p=0\). It is not a proof of a main-conjecture equality or p-adic BSD. Ordinary interpolation is the scope of this standard-coefficient conclusion; the more general retained cohomological criterion must be used separately at supersingular primes and at singular height matrices.

## 6. Consequence for the next arithmetic work

The source-comparison question for this family no longer needs another normalization run. An actual ordinary calculation may now target the specified standard \(L_{2,p}\) and matched \(\det H_p\) directly, including at a named prime in \(\mathcal D_{\mathrm{ord}}\); the unspecified index \(J\) is no longer a reason to postpone that calculation.

The uniform task remains to prove their nonvanishing and the correlated valuation bound on a cofinite ordinary domain, or to supply a different sufficient arithmetic bound. Neither separately forcing a unit regulator nor searching through the three unit smoothings is required. Finite ordinary examples would be instance evidence, not the cofinite theorem. Supersingular coverage and the exceptional primary obligations remain separate.

This review constructs no new value and launches no computation campaign. The existence of the optimal quotient and least-degree isogeny is enough for this source theorem; no explicit equations for that enormous-level map were computed.

## 7. Evidence and ledger

| Item | Result and scope |
|---|---|
| Actual proper/open source lattice | Supported under retained residual image; no extra index at p>=5 |
| Primitive plus source | Supported with the original 144 receipt and good-prime Manin inputs |
| Exact period convention | Bound as ±72 mu_phi; symbol computation retained, not freshly replayed |
| Ordinary quadratic comparison | Supported on the explicit domain for the newly specified family |
| Three-pair coverage | Proof checked; supplied controls replay identically |
| Packet custody | 7/7 manifest entries, 8/8 published files match |
| Supporting historical evidence | Nine pinned bindings checked; three original receipt hashes match their historical manifest |
| Arithmetic upper control | Open: no actual coefficient or cofinite estimate |
| FIN / ORDER9 / Q36 | Unchanged |

The replay includes 1,132 coverage cases, 100 gcd controls, 364 residual-vector inputs, 24 bad-modulus controls, 10 invalid-input controls, and 17 small-field seed counts. The small counts are not new primary certificates. The same-team reviews are separate from the author's derivation but do not count as independent human or formal acceptance.

The primary-source links and exact hypotheses are in the two audits. In particular, see [BKS §2.1 and §6.3](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en), [CNS Lemma 6.5](https://arxiv.org/pdf/1911.09446), and the original receipt bindings. No third-party full paper is redistributed in the review archive.
