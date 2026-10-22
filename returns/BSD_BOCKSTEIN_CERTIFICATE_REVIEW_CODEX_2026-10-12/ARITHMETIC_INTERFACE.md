# Arithmetic interface: the primitive target and the corrected coefficient ratio

October 12, 2026. **DERIVED_UNDER_RETAINED_INPUTS; SOURCE_INTERFACE_CHECKED; NO_NEW_SEED_VALUE.**

The corrected certificate has a useful arithmetic refinement. Its primitive torsion-free target can be identified from the saturated point lattice and the full local logarithm row, after the actual derivative is known to be nonzero. There is no remaining unknown Sha-cardinality factor in this target identification. With the retained, source-matched Rubin comparison and a nonsingular height matrix, the corrected quantity is

\[
 m_p-w_p-b_p=v_p(K_p)+v_p(\epsilon_{p,\rho})+1-v_p(\det H_p).
\]

At good non-anomalous ordinary primes this becomes

\[
 \boxed{m_p-w_p-b_p=v_p(K_p)-v_p(\det H_p).}
\]

Here **H is already the height matrix in the U=gamma−1 coordinate**, exactly as in the retained `RUBIN_COMPARISON.md`. No additional division by the cyclotomic logarithm belongs in this displayed formula. These are deductions from retained arithmetic inputs, not new evaluations or an independent recertification of the Kato construction.

## 1. Evidence and scope

The lab HEAD checked in this review is `02e86ce876cb83cef314b53d86f73a193298b203`. In the references below:

- `LAB` means `/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab`.
- `OLD` means `LAB/work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07`.
- `EXIT` means `/Users/bsm/BSD_EXIT1_KATO_POINT_LINE_MAP_CLAUDE_2026-10-07`.
- `BKS` means `/Users/bsm/BSD_BKS_INDEX_PREFLIGHT_CHECK_CODEX_2026-10-01/sources/BKS2024_published.txt`.
- `NEW` means `/Users/bsm/BSD_BOCKSTEIN_CERTIFICATE_REVIEW_CODEX_2026-10-12/submitted/BSD_BOCKSTEIN_CORRECTED_CERTIFICATE_2026-10-12/PROOF.md`.

The domain, actual smoothed class, simultaneous lattice transport, minimal differential, saturated point basis and local vanishings are imported. On this domain, `delta != 0` establishes primary finiteness and identifies actual global H1 with the point lattice (`OLD/CONTENT_BOUND_PROOF.md:38–54`). The local/global sequence and its finite-kernel consequence are retained at lines 102–151 of that proof. None of this supplies a new nonzero derivative.

## 2. Integral primitive-target identification

Write A=Z_p, W=A P1+A P2, and

\[
 \lambda=(\log_\omega(P_1)/p,\log_\omega(P_2)/p),\quad
 w=\min_i v_p(\lambda_i),\quad \lambda_0=p^{-w}\lambda.
\]

The row lambda is nonzero and integral; lambda0 is primitive. Let

\[
 F_0=\ker(\lambda_0:W\longrightarrow A),\qquad
 Q_0=-\lambda_{0,2}P_1+\lambda_{0,1}P_2.
\]

Thus F0=A Q0, and Q0 is a primitive vector of W. It is normally a p-adic linear combination of rational points, not a new rational point.

The retained discrete localization row gives

\[
 K_{\rm MW}=\ker((\mathbb Q_p/\mathbb Z_p)^2\xrightarrow{\lambda}\mathbb Q_p/\mathbb Z_p),
 \qquad K_{\rm MW}^{\vee}=W^*/A\lambda.
\]

The exact sequence `OLD/CONTENT_BOUND_PROOF.md:144–151` is

\[
 0\longrightarrow\Sha[p^\infty]^\vee\longrightarrow H^2_S
 \longrightarrow K_{\rm MW}^\vee\longrightarrow0.
\]

Its kernel is finite because nonzero delta has already established primary finiteness. Any torsion element of K_MW^vee lifts to torsion: a sufficiently large p-power of a lift lies in the finite kernel and is then killed by a further p-power. Therefore the induced map on torsion-free quotients is an isomorphism, not merely an isogeny:

\[
 \boxed{H^2_{S,\rm tf}\simeq (K_{\rm MW}^\vee)_{\rm tf}
       =W^*/A\lambda_0\simeq F_0^*.}\tag{A}
\]

The final map is restriction of functionals to F0. Its kernel is A lambda0 and it is onto because F0 is a direct summand of W. Evaluation at Q0 consequently identifies H2_tf with A in a **primitive integral basis**. Replacing Q0 by a unit multiple only changes that basis by a unit.

No value of the finite kernel's order is used in (A); no assertion that Sha vanishes is used. Primary finiteness is a proved prerequisite in this branch, not a hypothesis smuggled into the endpoint. A noncanonical splitting of an extension is unnecessary. In particular this does not assert a direct-sum decomposition of H2 torsion.

This is consistent with, and makes usable after `delta != 0`, the earlier conditional lattice repair at `LAB/work/state-sync-2026-10-04/dossiers/BSD_INDEX_DISCOVERY_ABC_REPAIR_CODEX_2026-10-01/DETERMINANT_AND_BOCKSTEIN_REPAIR.md:153–188`.

## 3. Matching the actual Bockstein to a height row

BKS (2.3.2) defines the actual global Bockstein with target H2_tf tensor I/I2 (`BKS:798–806`). Lemma 5.8 identifies it, rationally, with the image of the height functional through the canonical Poitou–Tate quotient (2.2.2) (`BKS:597–605,1926–1984`). Its proof uses functoriality of the Selmer/global exact triangles. The ordinary height itself is constructed from Bockstein and duality (`BKS:1649–1688`).

Combining this published rational comparison with the integral target identification (A) gives, for the BKS height,

\[
 \overline\beta(P_i)(Q_0)=\langle P_i,Q_0\rangle_p
 \quad\text{in } I/I^2,
\]

up to the harmless global sign caused by the connecting-map convention. If H_ij is the coefficient of this height in U=gamma−1, then

\[
 \boxed{b=\min_i v_p((Hq_0)_i),\quad
 q_0=(-\lambda_{0,2},\lambda_{0,1})^t.}\tag{B}
\]

This uses the actual cohomological row, not the determinant of the height matrix. No height nondegeneracy is needed for (B). In the nonzero-derivative branch the submitted algebraic proposition forces this row to be nonzero (`NEW:159–170`).

BKS Section 5.2 assumes Hypothesis 2.2 (`BKS:1878–1887`), including primary finiteness (`BKS:586–605`). Here it is available because delta is nonzero. If one instead starts from K nonzero, the retained zero-case proves `delta=0 => K=0`, so K nonzero establishes the same prerequisite before this comparison is used (`OLD/context/RUBIN_COMPARISON.md:39–47`). The argument never uses the unproved converse “height row nonzero implies primary finiteness.”

Primary source: [Burns–Kurihara–Sano, JMSJ 76 (2024)](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en), especially (2.2.2), (2.3.2), Lemma 5.8 and (5.3.2). This source supplies the comparison; equations (A), (B) and the deductions below are the review's own lattice calculations under the stated retained hypotheses.

## 4. The useful cancellation in the coefficient target

Use exactly the notation of `OLD/VALUATION_TARGET.md:7–24` and `OLD/context/RUBIN_COMPARISON.md:14–19,49–59`:

\[
 \ell=(\log_\omega P_1,\log_\omega P_2)^t,
 \quad H\delta=\epsilon_{p,\rho}K\ell,
 \quad r=v_p(\det H),
 \quad c=\operatorname{cont}(\operatorname{adj}(H)\ell).
\]

Assume K is nonzero and H nonsingular. The retained formula is m=v(K)+v(epsilon)+c−r. Set

\[
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Then q0=J ell/p^(1+w). Since H is symmetric (BKS Lemma 5.7, `BKS:1917–1924`),

\[
 \operatorname{adj}(H)\ell=-JHJ\ell.
\]

Multiplication by J merely permutes coordinates and signs. Thus (B) gives the exact equality

\[
 \boxed{c=1+w+b.}\tag{C}
\]

Substitution gives

\[
 \boxed{m-w-b=v_p(K)+v_p(\epsilon_{p,\rho})+1-r.}\tag{D}
\]

For good ordinary non-anomalous p, v(epsilon)=−1; the corrected criterion is precisely

\[
 K\ne0,\quad\det H\ne0,\quad
 0\le v_p(K)-v_p(\det H)\le1
 \quad\Longrightarrow\quad \Sha[p^\infty]=0.\tag{E}
\]

The lower inequality follows from the corrected content identity; the arithmetic task is the upper bound. More exactly, conditional on the submitted proposition and retained inputs,

\[
 v_p(K)-v_p(\det H)=\operatorname{length}\Sha[p^\infty]+e_p,
 \qquad e_p\ge0.
\]

Consequently the independent Wieferich index and Bockstein-content terms disappear from the **correlated comparison target**. One need not prove they are units. This is a valid strengthening of the arithmetic formulation, not a proof that the ratio has bounded content, and it does not remove the same-class Kato defect e_p.

For a matched supersingular root, the retained v(epsilon)=0 instead gives `m−w−b=v(K)+1−r`; the sufficient upper bound is v(K)≤r. Valuations in the root field are normalized by v(p)=1. The BKS comparison makes the projected row in (B) the scalar extension of the actual integral row. No ordinary numerical height convention may be substituted. If H is singular, (D) and (E) cannot be formed, whereas the direct criterion and row description (B) remain meaningful.

## 5. Scalar numerical heights and the single cyclotomic conversion

Let a_gamma=log_p(chi_cyc(gamma)), with gamma a topological generator of the cyclotomic Z_p-extension. For odd p, v_p(a_gamma)=1. The map I/I2→Q_p used by the scalar cyclotomic height sends U to a_gamma; see BKS (5.3.2), `BKS:2206–2209`.

If H_num is **source-matched** to this scalar height, then

\[
 H_{\rm num}=a_\gamma H,\qquad
 b=\min_i v_p((H_{\rm num}q_0)_i)-1,\qquad
 v_p(\det H_{\rm num})=r+2.\tag{F}
\]

An overall sign or fixed factor 2 is a p-unit on this domain and does not affect these valuations. A factor p does affect them and cannot be dismissed. Formula (F) is a change between two named conventions, not an arbitrary renormalization of the integral target.

One may express (E) using scalar numerical heights as

\[
 0\le v_p(K)+2-v_p(\det H_{\rm num})\le1,
\]

provided K is still the coefficient in the U^2 convention. If the variable defining K is also changed, its coefficient transformation must be worked out explicitly; do not apply a second automatic subtraction of 1 or 2.

Nekovář's comparison with the classical universal-norm construction is Theorem 11.3.9 of [Selmer complexes](https://www.numdam.org/item/AST_2006__310__R1_0/). The retained local extraction `/Users/bsm/BSD_UNIFORM_ATTACK_REPAIR_CODEX_2026-10-03/sources/nekovar.txt:20855–20915,21467–21472` records its hypotheses and theorem. BKS Remark 5.2 points to that comparison. This review does not claim to have independently audited PARI's implementation or certified its finite-precision arithmetic.

## 6. What the existing numerical files actually establish

`EXIT/checks/bockstein_content.gp:5–17` is the retained seed calculation. It uses the minimal model and points transported from P1=(4547,327384), P2=(5184,281520). It obtains h11 and h22 from singleton regulators, polarizes to h12, and forms a primitive fine-line vector by dividing the raw logarithm row by its minimum valuation. Its vector has the opposite sign to q0, which is irrelevant for content.

The official [PARI documentation for ellpadicheight and ellpadicregulator](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html#ellpadicheight) defines the scalar ordinary regulator from the canonical cyclotomic height and records its log_p normalization. The unit-root projection is [1,−s2]; the eta component of the vector height is minus the logarithm square. Thus bilinearization gives a log(P)log(Q) correction, which vanishes when Q=Q0. This explains why the correctly constructed fine-line row is independent of that splitting. The exact matching of a particular implementation output to the BKS scalar convention must still be recorded in any accepted arithmetic packet.

`EXIT/checks/RESULTS.md:6–13` reports w=0 for the good-prime logarithm scan and raw height-row valuation vB=1 for its ordinary scan. **That baseline corresponds to b=0 under (F), not b=1.** The same file reports a raw regulator valuation 3 at p=17. This converts to r17=1, matching `OLD/VALUATION_TARGET.md:55–65`, which also retains c17=1 and w17=0. Equation (C) then gives b17=0.

These retained values make the new correction zero at the reported ordinary sample. They do not provide a sample prime at which a positive b creates a newly successful certificate. At p=17 the reduced target remains `v17(K17)−1≤1`, exactly the earlier quantitative target. No K17 value is supplied here.

Custody qualifications from inspection of the actual files:

- The numerical folder contains the script and a short prose results summary; this review found no complete saved 70-row output or independently replayable residue packet there. No computation was rerun.
- The loop at `bockstein_content.gp:10` explicitly filters bad and supersingular primes; it does **not** explicitly filter the set {19,59,487}, despite the printed scope label at line 18. Intersect any reused rows with the accepted domain and all source exceptions; the label alone does not authenticate that intersection.
- The height scan cannot establish the actual Kato derivative's scale. The historical assertion “delta17 is still primitive” at `EXIT/REPORT.md:303–305` does not follow from these height data alone. It would also need the relevant Kato coefficient or an independently justified scale comparison controlling Sha and the Kato defect.
- No actual derivative coordinates, accepted integral Bockstein residue pair, new Sha-primary vanishing, or cofinite ratio bound is produced by this review.

## 7. Audited assumptions and remaining endpoint

| Input or conclusion | Status here |
|---|---|
| Actual class, integral all-height-one Kato inequality, weak-order control and nonzero-derivative primary finiteness | Retained from the October 7 return; not recertified |
| Local non-anomalousness, bad-local vanishings, minimal differential and full point basis | Retained on the stated domain |
| Primitive-target identity (A) | Derived from the retained exact sequence; no Sha-order input |
| Height/Bockstein comparison | Matched to BKS Lemma 5.8 after its finiteness prerequisite is established |
| Corrected ratio identity (D), ordinary sufficient target (E) | Derived from (A), (B), symmetric 2×2 algebra, and the retained Rubin equation |
| Historical numerical b=0 interpretation | Consistent under the named scalar-height convention; historical data, not a new certified replay |
| Uniform upper control of v(K)−v(det H), or direct m−w−b | Open |
| FIN, ORDER9, Q36 and exceptional-prime obligations | Unchanged |

The concrete next arithmetic object is now the correctly normalized coefficient-to-height-determinant ratio when H is nonsingular, or the actual derivative paired with the primitive fine-line Bockstein row when it is not. An independent bound on either can prove something; rewriting its value as `length Sha + e` does not itself supply such a bound and does not make independent arithmetic control logically circular.

No new seed computations, campaigns, publication, push, or external messages were performed in this subreview.
