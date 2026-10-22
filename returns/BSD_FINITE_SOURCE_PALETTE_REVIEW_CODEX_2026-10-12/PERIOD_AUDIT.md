# Period, primitive plus line, and ordinary coefficient audit

Date: 2026-10-12. Scope: submitted `PROOF.md` Sections 4 and 6. Lab identity: `581f7a26a1d110bcd6131739f94569e4810a719e`.

**Verdict: SOURCE_COMPARISON_PASSES_UNDER_RETAINED_INPUTS; RECEIPT_LOCATOR_GAP_REPAIRED.** The period claim is supported by an actual preserved symbol receipt, with the required newform, minimal-differential and real-period binding. The displayed comparison with the standard ordinary measure follows from the full interpolation formula; no additional coefficient-prime Euler factor or unknown lattice index is needed once the submitted literal lattice equality is established. This audit imports that lattice equality from the separate geometric audit, and retains the original computer-assisted symbol certificate rather than replaying its numerical engine.

The first repairable defect in the submission was documentary: it cited an old value 144 without locating the receipt or identifying whether its integrand was the normalized newform or a parametrization pullback. The predecessor had the same omission. The pinned lab contains the needed receipts and source convention. The paths and hashes below repair it. No further blocking gap in Sections 4 and 6 was found within this retained-input scope.

## 1. Exact custody of the retained one-fifth value

Let `BASE` be the following directory inside the pinned lab:

`work/state-sync-2026-09-30/release/v0.2.6/evidence/src/`

Let `P5` be `BASE/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/`, and let `CORE` be `BASE/BSD_RIGOROUS_STREAM_CORE_2026-09-19/`.

| Receipt | Exact content used | SHA-256 |
|---|---|---|
| `P5/run/SYMBOLS_m5.txt:1-5` | The row with numerator 1 is `1 144 -8`; the first value is the plus symbol. | `fb7b98d89b1885bacbb1d9d306c6c17fcefeafbb094baf1fcb5258756e6edf9c` |
| `P5/run/msl_m5.txt:15-21` | `OMEGA_PLUS` is the retained real period; `XB 1` encloses the plus value as `[144.000 +/- 3.87e-4]`, with candidate `147456/1024`, containment 1, uniqueness 1. | `be3b9ad17cf75ca9ccd0d3c065f3c96bab344989cf494135e11440563fa761f7` |
| `P5/P5_CERTIFICATE.md`, Sections 1 and 3 | The denominator lattice is `(1/1024)Z`; the normalizer is `omega_1`; the complete four plus values are `(144,-144,-144,144)`. | `2dfa96d000efa7a4862674f5cdc7953341fcc5fb3ef0e4308281456eba441d77` |

All three current byte hashes agree with their historical `P5_MANIFEST.sha256` entries. Their Git blobs are respectively `a9961d9d45bc22605a331c994a3dee4119c1c12b`, `ce2778600afce0c069f679703c24d539f25a3e18`, and `008c22932c67d6df5fe4948bd55f1f2dcd930e56`. Each current file agrees with its blob at the stated lab commit. Full paths, hashes, pinned blob checks, and additional convention-source bindings are in `PERIOD_BINDINGS.json`; small byte-identical copies are in `period_evidence/`.

This is a check of custody, content and convention. It is not a fresh modular-symbol calculation, coefficient-corpus replay, or independent proof of the denominator lattice. The original exact identification retains its stated theorem input `c_E | 512` (hence the conservative `(1/1024)Z` lattice), retained central vanishing, and numerical software/hardware trust base. The fact that the displayed candidate is an integer does not eliminate that original reconstruction dependency.

## 2. The reference newform and minimal period are identifiable

`CORE/DESIGN.md`, Objects enclosed and O1/O3, specifies the coefficients as the seed's L-series coefficients and the symbol as

\[
 [r]^+_{\mathrm{receipt}}=\operatorname{Re}\lambda_f(r)/\omega_1(E),
 \qquad f=\sum_{n\ge1}a_nq^n.
\]

The coefficients are normalized by `a_1=1`; equivalently the holomorphic differential is `omega_f=2*pi*i*f(z) dz`, and its antiderivative has Fourier coefficients `a_n/n`. The source implementation `CORE/src/arbcore.c:9-10` states the same `lambda` and period normalization. `P5/P5_CERTIFICATE.md`, Section 4's normalization table, expressly distinguishes its computed `lambda_f/omega_1` from symbols involving the curve's parametrization and its Manin constant. Thus the submitted alternative “if the receipt is expressed with the old minimal X_0 parametrization” is unnecessary for this actual receipt: it is expressed using the normalized newform.

The numerical receipt uses

\[
 E_{\rm raw}:[0,-22735,0,106272484,0].
\]

`CORE/ANALYTIC_RANK_CERTIFICATE.md:35` records the change `[u,r,s,t]=[1,7578,0,0]`. Direct substitution `x_raw=x_min+7578`, `y_raw=y_min` gives

\[
 E_{\rm min}:[0,-1,0,-66020924,-65074271436].
\]

In particular `dx_raw/(2y_raw)=dx_min/(2y_min)`; the period in the receipt is already a period of the submitted minimal Neron differential. There is no hidden nonunit scaling from a nonminimal Weierstrass equation.

`CORE/DESIGN.md:80-82` specifies `omega_1` as the least positive real period via the AGM for positive discriminant. The retained seed has two real components. Its full real Neron period is therefore

\[
 \Omega_E=2\omega_1.
\]

This factor is also explicit in the P5 normalization table. Its only prime support is 2.

## 3. The Manin-constant argument has the correct hypotheses and direction

For the optimal connected-kernel quotients `q_1:J_1(N)->E_1` and `q_0:J_0(N)->E_0`, both attached to the same rational weight-two newform, [CNS Lemma 6.5, printed page 42](https://arxiv.org/pdf/1911.09446) gives, up to the harmless choice of differential signs,

\[
 \mu_0=\mu_1 I,\qquad I\in\mathbf Z_{>0},
\]

where `I` is the Lie-algebra cokernel index for the induced isogeny between the Neron models. It also gives integrality of the Manin constants. The subgroup inclusions and connected-kernel hypotheses match the submitted choices. Therefore `v_p(mu_0)=0` forces `v_p(mu_1)=0`; the direction was not reversed.

There is a direct primary theorem for the good-prime input: [Agashe–Ribet–Stein, Corollary 3.7, printed page 623](https://wstein.org/papers/ars-manin/agashe-ribet-stein-the_manin_constant.pdf) says that an odd prime dividing the Manin constant of an optimal newform quotient of `J_0(N)` must have its square divide `N`. This applies to `E_0`, not arbitrarily to the seed with an unspecified map. Hence it gives `p ∤ mu_0` whenever `p>=5` and `p ∤ N`.

As an independent direct formulation, [Cesnavicius, Theorem 1.2 (= Theorem 2.13)](https://arxiv.org/pdf/1703.02951) gives the unit assertion at `p^2 ∤ N` for an optimal elliptic new quotient of an intermediate modular Jacobian, including `J_1(N)`. The seed is not globally semistable, but this theorem's primewise hypothesis is what is used; global semistability is not required here.

For the least-degree isogeny `psi:E_1->E`, the Section 2 argument gives `p ∤ deg(psi)` from the retained irreducibility of `E[p]`. Its integral Neron differential multiplier and that of its dual multiply to `deg(psi)`, so both are `p`-units. Consequently

\[
 \phi^*\omega_E=\mu_\phi\omega_f,\qquad
 \mu_\phi\in\mathbf Z_p^\times
 \quad(p\ge5,\ p\nmid N).
\]

Nothing here proves a unit statement for arbitrary multiples of the chosen map, or needs the old additive-prime/2-part Manin bound. That old bound remains in the historical numerical receipt's exact-reconstruction trust chain, a distinct use.

## 4. From the relative symbol to the actual primitive plus line

The matrix `xi=[[1,0],[5,1]]` has determinant one, with `xi(0)=0` and `xi(infinity)=1/5`. In BKS's notation, `delta(xi)` is the image of this relative path under (2.1.2), and `e+=(1+g)/2` is the plus projection. The basis requirement is exactly (2.1.3), in the plus part of the actual image lattice `H`; it is not a statement merely that an abstract rational plus line is nonzero. [BKS, Sections 2.1 and 6.3](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en).

The Manin–Drinfeld projection and pushforward are compatible with integrating holomorphic differentials. Thus, using `lambda_f(r)=integral_infinity^r omega_f` and the retained central value `lambda_f(0)=-L(E,1)=0`, the receipt gives

\[
 \begin{aligned}
 \Omega_\xi
 &=\int_{e^+\delta(\xi)}\omega_E\\
 &=\mu_\phi\operatorname{Re}\int_0^{1/5}\omega_f\\
 &=144\mu_\phi\omega_1.
 \end{aligned}
\]

If the chosen path orientation or differential sign is reversed, the same equalities carry the corresponding sign. In particular the full-period comparison is the concrete formula

\[
 \Omega_\xi/\Omega_E=72\mu_\phi
\]

with those signs understood. The exact integer `mu_phi` need not be computed to establish its valuation. This explains precisely why no prime at least 5 is introduced by the period conversion.

Now use the submitted Section 3 equality `H tensor Z_p = H_1(E(C),Z) tensor Z_p`. For the seed's positive discriminant, the primitive real cycle has period `omega_1`. Therefore the coordinate of `e+delta(xi)` in the actual plus lattice is `144 mu_phi`, a `p`-unit at every good `p>=5`. Passing from the completed rank-one lattice to its localization at `(p)` gives BKS (2.1.3). The factor `1/2` in `e+` is harmless for these primes. This is the needed primitive-line conclusion, beyond mere nonvanishing.

Without the Section 3 lattice equality, the last inference would still have an unknown image-lattice index. The period receipt alone does not prove that equality. The present result uses the newly specified map, not an arbitrary historical Kato packet.

## 5. Full ordinary interpolation and the quadratic coefficient

Take `S={infinity,p} union {q:q|N}`, the unit root `rho` of `X^2-a_p X+p`, `sigma=p/rho`, the fixed minimal differential, and the same `U=gamma-1` as the retained height comparison. `COFINITE_NORMALIZATION.md`, Section 3, specifies the standard measure by its trivial-character value `(1-rho^-1)^2 L(E,1)/Omega_E` and nontrivial-character value `tau(chi) rho^-n L(E,chi^-1,1)/Omega_E`.

BKS printed page 895 specifies the corresponding S-truncated measure using `Omega_xi`; Theorem 6.10 and (6.3.3), printed page 899, identify the Coleman image of the actual smoothed source with that measure times

\[
 t_{c,d}=cd(c-\sigma_c)(d-\sigma_d).
\]

Here `sigma_a` acts on roots of unity by exponentiation by `a`. At augmentation, `t_cd(0)=cd(c-1)(d-1)`. These are precisely the actual integral smoothings in the submission, before any division.

For a nontrivial cyclotomic character, the good coefficient-prime local factor is already trivial in the ramified twist. The removed multiplicative bad-prime factors are represented, in the stated arithmetic-Frobenius convention, by

\[
 E_N(U)=\prod_{q\mid N,\,\mathrm{mult}}
 (1-a_q q^{-1}[\mathrm{Frob}_q]^{-1}).
\]

Additive bad primes contribute 1. At the trivial character, the additional removed `p`-factor is `(1-rho^-1)(1-sigma^-1)`. BKS's separate prefactor is `(1-rho^-1)/(1-sigma^-1)`. Multiplication leaves exactly `(1-rho^-1)^2`, the standard measure's prefactor. It is not permissible to remove another `p`-Euler factor afterward. The ordinary interpolation uniqueness then gives

\[
 L_{S,p}=(\Omega_E/\Omega_\xi)E_N(U)L_{\rm std,p},
 \qquad
 \operatorname{Col}(z_{c,d})
 =t_{c,d}(U)(\Omega_E/\Omega_\xi)E_N(U)L_{\rm std,p}.
\]

This is an equality for the specified measure and BKS Coleman normalization. A separate integral unit choice of source coordinates changes its displayed scalar by a unit. It does not authorize arbitrary rescaling of an evaluator or of the source, or changing the height convention.

The retained rank-two weak-order input removes degrees zero and one. Extracting degree two therefore uses only the augmentations:

\[
 K_p=t_{c,d}(0)(\Omega_E/\Omega_\xi)c_N L_{2,p},
 \qquad
 c_N=\frac{17469664}{13105849}
 =\frac{2^5\cdot19\cdot59\cdot487}{2243\cdot5843}.
\]

The smoothing choice supplies a unit. Section 4 above supplies a period unit. The bad-prime factor is a unit exactly on the stated good-prime domain after excluding `19,59,487`. Literal equality of the target lattice supplies no further `p`-homothety. Thus `v_p(K_p)=v_p(L_2,p)` and the two vanish together for every ordinary `p` in the submission's domain, subject to the retained arithmetic and separately audited geometric inputs.

This comparison does not require a main-conjecture equality or an unproved rank-two leading-term formula. It supplies no value of `K_p`, `L_2,p`, a height determinant, or the source defect. No new seed coefficient computation was performed.

## 6. Minimal documentary correction

Replace the vague “retained symbol receipt” reference in the submitted Section 4 and in `SOURCES.md` with the exact P5 paths and hashes in Section 1. State that the retained symbol is normalized-newform `lambda_f/omega_1`, that the model change has `u=1`, and that the full-period ratio is `72 mu_phi` up to the fixed sign. Cite ARS Corollary 3.7 for the optimal `J_0` good-prime unit and CNS Lemma 6.5 for its transfer to `J_1` (or cite Cesnavicius Theorem 1.2 directly for the latter). Preserve the historical reconstruction and retained-input qualifications.

These corrections can be made without launching any modular-symbol, Kato-coefficient, height or Selmer computation. The submission itself was not edited by this audit.
