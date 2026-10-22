# A local period comparison, with the integral correction retained

Date: 2026-10-11. Grade: written derivation using the named local theorems; not independently certified. No seed Kato coefficient was evaluated.

**Result:** the signed local-resolvent period can be compared to the Lubin–Tate regulator with an explicit conductor factor and a proved principal-unit correction. A logarithmic version repairs the trace-compatibility issue in the thesis's coordinate construction. This is a local comparison. It does not establish the global theta/Kato realization or the required bound on the seed derivative.

## 1. Fixed conventions and imported inputs

Fix p≥5, L=Q_{p²}, O=O_L, π=−p, and one Lubin–Tate formal group F for π, with logarithm λ and invariant differential dλ. Put L_a=L(F[π^a]). Let Ψ_n/L be the degree-p^n anticyclotomic layer, with generator γ of its infinite Galois group. A character χ of exact order p^n has full Lubin–Tate conductor a=n+1. Thus BKO's Φ_n is SV's L_{n+1}; these indices must not be equated.

Use the local reciprocity and cup-product convention in Sano–Venjakob §1.4: the point/exponential class is first in the Tate pairing. Identify the dual de Rham line using dλ. Fix a Tate-module generator and its compatible dual once. The coefficient representation in this note is V=T_π(F)^∨(1)=L(τ), τ=χ_cyc χ_LT^{-1}. It is **not** the full non-CM seed representation.

Imported local results: BKO 2023 Lemma 2.6 gives formal-group trace compatibility of c_n^±; BKO 2025 Proposition 4.3 makes c_n^{(-1)^n} a uniformizer. Proposition 4.6 gives, for a primitive χ and a uniformizer c,

\[
R_χ(λ(c))/R_χ(c)\in1+p\mathcal O_{\mathbf C_p},
\qquad R_χ(x)=\sum_{σ\in\mathrm{Gal}(Ψ_n/L)}χ(σ)σ(x).
\tag{1}
\]

Its actual statement is stronger: the difference belongs to pR_χ(c)R_n. BKO equation (4.10), in its dual bases v_±, gives

\[
R_{χ^{-1}}(λ(c_n^ε))\,δ_χ(v_{-ε})
=ω_n^{-ε}(χ(γ)),\qquad ε=(-1)^n.
\tag{2}
\]

Here ω_n^+=∏_{1≤k≤n, k even}Φ_{p^k}(γ) and ω_n^-=(γ−1)∏_{1≤k≤n, k odd}Φ_{p^k}(γ). These source formulas are local and contain no Sha assumption.

## 2. Repair the trace step before comparing periods

The thesis's printed pp.346–347 form t_m using coordinates c_m and invoke BKO's trace relation. BKO's cited trace is on F(m_m), so it is a formal-group trace; it does not by itself prove the displayed ordinary coordinate-trace identity. The pages were visually checked. I do not infer that no stronger coordinate identity could exist, but it is not supplied by that citation.

There is a direct repair. For odd m define

\[
\widetilde t_m=p^{-(m+1)/2}
\left(λ(c_m^{(-1)^m})+λ(c_{m-1}^{-(-1)^m})\right).
\]

The logarithm converts formal addition and formal trace to field addition and field trace. Across two layers the first summand traces to pλ(c_{m-2}^{(-1)^m}); the second traces to pλ(c_{m-3}^{-(-1)^m}). Hence

\[
\mathrm{Tr}_{Ψ_m/Ψ_{m-2}}\widetilde t_m=\widetilde t_{m-2}.
\]

Therefore \(\widetilde\Omega_χ=\sum_σχ(σ)σ(\widetilde t_m)\), for any sufficiently large odd m, is well defined. Reducing to the smallest permissible odd layer gives, with h_n=⌈n/2⌉,

\[
\boxed{\widetilde\Omega_χ=p^{-h_n}R_χ(λ(c_n^ε)),\quad ε=(-1)^n.}
\tag{3}
\]

For n odd, the lower-level summand has zero χ-projection. For n even use m=n+1: the trace of λ(c_{n+1}^-) lands in Ψ_{n-1} and its χ-projection is zero, while the λ(c_n^+) summand acquires a factor p. This proves the exponent h_n without guessing parity.

Define also the **minimal-level coordinate period** Ω_χ^min=p^{-h_n}R_χ(c_n^ε). Equation (1) proves

\[
\widetilde\Omega_χ=u_χ\Omega_χ^{min},\qquad u_χ\in1+p\mathcal O_{\mathbf C_p}.
\tag{4}
\]

Thus the repair preserves the minimal-level valuation, with a proved valuation-zero ratio. I do not assert equality to the thesis's arbitrarily lifted coordinate definition; that requires its coordinate trace claim or another comparison. The original theorem's global integral family cannot simply be rescaled character by character.

## 3. Exact signed local-duality factor

Combining (2) and (3) proves

\[
\boxed{\widetilde\Omega_{χ^{-1}}\,δ_χ(v_{-ε})
=p^{-h_n}ω_n^{-ε}(χ(γ)).}
\tag{5}
\]

For the minimal coordinate period the right side must be multiplied by u_{χ^{-1}}^{-1}. This unit is not declared constant in p or χ; its valuation is proved zero, which suffices for a valuation comparison.

For ζ=χ(γ), put

\[
s_n=\frac{\mathbf1_{n\text{ even}}+
\sum_{1≤k<n,\;(-1)^k=(-1)^{n-1}}(p^k-p^{k-1})}
{p^{n-1}(p-1)}.
\]

Indeed v_p(ζ−1)=1/(p^{n-1}(p−1)), and
Φ_{p^k}(ζ)=(ζ^{p^k}−1)/(ζ^{p^{k-1}}−1), giving the displayed summands. Hence

\[
v_p(\widetilde\Omega_χ)=\frac{n+1}{2}-h_n
=\begin{cases}0&n\text{ odd},\\1/2&n\text{ even},\end{cases}
\quad
v_p(δ_χ(v_{-ε}))=s_n-\frac{n+1}{2}.
\tag{6}
\]

This fixes the conflicting parity prose in the thesis by using its normalization exponent and the local theorem. The first three exact cases are:

| n | nonzero signed polynomial | v_p(Ω̃χ) | v_p(δχ) |
|---|---|---:|---:|
| 1 | 1 | 0 | −1 |
| 2 | (ζ−1)Φ_p(ζ)=ζ^p−1 | 1/2 | −3/2+1/(p−1) |
| 3 | Φ_{p²}(ζ) | 0 | −2+1/p |

These are derived local-factor values for arbitrary p≥5, not computed seed values.

## 4. Match the Lubin–Tate regulator and keep its factors

Use SV Corollary 2.6.6 with k=1 and j'=0. This special corollary matters: V=L(τ) lies at an excluded Frobenius value in the preceding general corollary.

**The integral lift used here.** This is not a general assertion that Iwasawa H¹ commutes with specialization. In BKO 2023 §2.1.1, put Λ₂=O[[Gal(Θ∞/L)]], J=ker(Λ₂→Λ), and let Δ=Gal(Φ∞/Θ∞), of order d=p²−1. Their actual definitions are

\[
U_\infty^*=(\varprojlim U_n\otimes_{\mathbf Z_p}T_\pi(F)^\vee)^\Delta,
\qquad
V_\infty^*=U_\infty^*\otimes_{\Lambda_2}\Lambda
=U_\infty^*/J U_\infty^*.
\]

Thus a signed basis vector v_{−ε} has an integral preimage u∈U∞*. This surjectivity is the elementary quotient map, not a cohomological base-change claim. BKO's Kummer/twist isomorphism (2.3) puts u in the Δ-invariant part of full LT Iwasawa cohomology. Their separate control identification (2.7) identifies V∞* with lim H¹(Ψ_n,Tπ(F)^∨(1)), compatibly with the anticyclotomic projection; that published local identification is an explicit import here. Merely knowing the two source modules are isomorphic would not supply this compatibility.

Fix the full-tower lift **in corestriction normalization**: if (2.4) is implemented by inverse restriction from Θ_n to Φ_n, take y=d⁻¹u under (2.3). Then cor_{Φ_n/Θ_n}(y_n)=u_{Θ_n}, because cor∘res=d. Hence cor_{Φ_n/Ψ_n}(y_n)=v_{−ε,n} under (2.7). The factor d⁻¹ is integral and a p-unit, but has not been silently omitted from the choice of y. Equivalently one may choose any full-tower class satisfying these corestriction equalities. This establishes existence for BKO's signed class with its stated control theorem retained.

The H² term is not presumed absent in an arbitrary descent: for a quotient by a single direction J=(h−1), derived control would normally give

\[
0\longrightarrow H^1_{\rm Iw}/JH^1_{\rm Iw}
\longrightarrow H^1_{\rm ac}
\longrightarrow H^2_{\rm Iw}[J]\longrightarrow0.
\]

We rely on BKO (2.7) for this specific local coefficient module, not on a general claim that the last term vanishes. No analogous global or seed-Kato specialization is inferred. This also means the formulas below have a precise fallback scope independent of any reinterpretation of (2.7): they hold for classes with a compatible, corestriction-normalized full-tower lift.

Finally, a change of lift whose anticyclotomic corestriction is zero has zero χ-component: compatibility of exp* with corestriction makes its full-tower χ-weighted sum zero. Thus the finite-character value occurring below is independent of the compatible lift.

The de Rham twist V(τ^{-1}) is trivial, with e_0=1 and φ_L acting as 1. Compatibility of corestriction with the dual exponential turns the full-tower character sum into BKO's anticyclotomic sum. The inverse on σ in SV's formula reverses the character. Thus

\[
\mathcal L_τ(y)(χ^{-1})=
\pi^{n+1}\tau_{LT}(χ^{-1})^{-1}\,δ_χ(v_{-ε}).
\tag{7}
\]

There is no omitted Ω_LT power: its exponent j' is zero. The two occurrences of τ in this section mean different things: τ=χ_cycχ_LT^{-1} is the coefficient character; τ_LT(χ^{-1}) is SV's explicitly defined Gauss sum. Combining (5) and (7) yields

\[
\boxed{\widetilde\Omega_{χ^{-1}}\mathcal L_τ(y)(χ^{-1})
=\frac{(-p)^{n+1}}{\tau_{LT}(χ^{-1})}\,
p^{-h_n}ω_n^{-ε}(χ(γ)).}
\tag{8}
\]

For Ω^min insert u_{χ^{-1}}^{-1}. This is an actual factor formula, not an assertion that the two named periods are equal.

The normalized Gauss factor in (8) has valuation zero for these pure anticyclotomic characters. The additive-character identification is explicit, not inferred just from the name “Gauss sum.” SV §2.3 defines

\[
\tau_{LT}(\rho)=\sum_{g\in\mathrm{Gal}(L_a/L)}\rho(g^{-1})g\eta(1,\eta_a).
\]

SV's footnote 2 (printed p.19) identifies this with the finite local-character sum in MSVW §6. In MSVW arXiv:2404.09974v2, printed pp.49–50, ψ_u(x/π^a)=η(x,u_a); formula (57) gives the sum over (O/π^a)^×, and Remark 6.2 proves n(ψ_u)=0. Its proof shows that ψ_u is trivial on O but nontrivial on π⁻¹O. Therefore x↦ψ_u(x/π^a) is primitive on the additive group O/π^a. Remark 6.1 and (55) give ψ_L(x)=ψ_u(cx), where c generates the different. Since L/Q_p is unramified, c∈O^×. In particular the additive term is ψ₀(Tr(c′x)/π^a) for a fixed unit c′, with no unknown power of p in the additive conductor.

Write G(ρ,c′) for this sum; the inverse convention on ρ can be retained consistently in both factors. The nontrivial automorphism x↦x̄ of L/Q_p sends a pure anticyclotomic ρ to ρ⁻¹. Substituting x=x̄′ in the finite sum gives G(ρ,c′)=G(ρ⁻¹,c̄′). Changing c̄′ back to c′ multiplies the sum by ρ evaluated at the unit c′/c̄′ (or its inverse, with the inverse-character convention). This is a root of unity. Thus

\[
v_p(\tau_{LT}(\rho))=v_p(\tau_{LT}(\rho^{-1})).
\]

SV's product identity (proof of Lemma 2.6.2, printed p.19), equivalently MSVW (61)–(62) with n(ψ_u)=0, is

\[
\tau_{LT}(\rho)\tau_{LT}(\rho^{-1})\rho(\sigma_{-1})=q^{a(\rho)}.
\]

Here q=p² and a=n+1. The two equal valuations consequently each equal a, proving

\[
v_p\!\left(\frac{(-p)^{n+1}}{\tau_{LT}(\chi^{-1})}\right)=0.
\]

This is a proved valuation-zero factor, not a claim that the factor is rational, prime-independent, or equal to one. An additional tame character need not be sent to its inverse by conjugation; that case requires its own calculation.

In particular

\[
\boxed{v_p(\mathcal L_τ(y)(χ^{-1}))=s_n-(n+1)/2.}
\tag{9}
\]

The 2026 unramified-variable theorem reduces to this formula at the trivial unramified character. It adds no unidentified factor in that specialization.

## 5. Exact remaining interface and seed consequence

The local signed periods and the regulator now have a written valuation dictionary. The local correction is controlled; it cannot legitimately be called an arbitrary unknown power of p. This does not mean the global comparison is done.

The first unproved global step is to realize the theta classes using the repaired coherent periods (or prove that the original coordinate construction agrees with them through one integral family), and then prove that their global pullback/seed projection maps to the specified seed Kato class. Characterwise principal-unit ratios alone do not establish a single integral Iwasawa-module automorphism. The tame component in Theorem E and the thesis's change from +p to −p must also be transported explicitly before claiming the full theorem's normalization.

Nothing here makes the seed derivative's excess content m_p−w_p bounded. Formula (9) controls the local comparison factor on this CM coefficient line; it supplies neither the global numerator nor its nonvanishing. The whole non-CM representation is not automatically L-analytic. These are distinct interfaces, not a reason to suppress the completed local calculation.

FIN, ORDER9 and Q36 remain unchanged.

## Sources and audit scope

- [SV2024 thesis](https://theses-dissertations.princeton.edu/bitstreams/d06bd1e5-3563-446e-b347-654b81c3a8be/download): printed pp.343–349, Definitions 8.2.2.10–15 and their trace argument; Theorem E, printed pp.32–33.
- [BKO 2023/2024](https://doi.org/10.1017/S147474802300021X): printed pp.1423–1425, actual quotient definition and (2.3)–(2.9); printed pp.1427–1428, Lemma 2.6. The control identification (2.7) is an explicit local import; the trace's formal-group domain was checked directly.
- [BKO 2025](https://arxiv.org/html/2507.08221v1): §§4.1–4.3, Proposition 4.6 and equation (4.10), read beyond the abstract.
- [Sano–Venjakob](https://arxiv.org/html/2412.12429v1): §§1.4, 2.3, Gauss-product identity in the proof of Lemma 2.6.2, Corollary 2.6.6.
- [MSVW](https://arxiv.org/html/2404.09974v2): §6, printed pp.49–52, Remarks 6.1–6.2 and (55), (57), (61)–(62). These fix the additive conductor and the finite Gauss sum, not any global period comparison.
- [Venjakob 2026](https://www.mathi.uni-heidelberg.de/~venjakob/papervenjakob/LT-maxabelian.pdf): Theorems 1.2–1.3.

Source-cache bindings are recorded in LUBIN_TATE_SOURCE_BINDINGS.json; the preceding return binds the thesis and SV papers. No raw sources are proposed for republication. The deductions (3)–(9) need independent mathematical review; no novelty claim is made.
