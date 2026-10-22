# External preprint delta: sources not previously theorem-read in the searched record

Date: 2026-10-11. Grade: targeted primary-source reading and hypothesis screen, not a proof audit or a new seed theorem.

## Custody and novelty scope

The search covered Markdown, JSON and TeX in `/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work`, including the synchronized compendium and return dossiers. It did not search every file on the host. Exact paths returned by the searches are retained in `sources/external/PRIOR_RECORD_SEARCH.json`; source HTML hashes are in `sources/external/BINDINGS.json`.

A name in the compendium is not proof that its theorem was read. In particular, the September 29 `BSD_UNIFORM_STEP_FRESH_RETURN_OPUS_2026-09-29/hits/H08_ABSTRACT_LEVEL_EXCLUSIONS.md`, lines 17–18, explicitly labels 2511.08793, 2503.09034 and 2605.29783 as **titles only, UNCHECKED**. The observed later copies reproduce that row; no theorem-level use of these exact papers was found. The separately studied Angurel ultra-Kolyvagin paper is 2605.26917, not Loeffler–Zerbes 2511.08793.

These are newly checked sources, not claims of newly released Oxford material.

## 1. A precise nonordinary index-bound machine

David Loeffler and Sarah Livia Zerbes, *Ultra-Kolyvagin systems and non-ordinary Selmer groups*, arXiv:2511.08793v2, 18 November 2025. [Primary text](https://arxiv.org/html/2511.08793v2).

Read §§6.1–6.7, Theorem 7.9, and the integral-complex/error discussion in §8. Theorem 6.15 is

\[
\ell_{\mathcal O}H^1_{f\mathcal F}(\mathbf Q,T^\vee)\le\operatorname{ind}_{\mathcal O}(\kappa_1,H^1(\mathbf Q,T)),\qquad T^\vee=\operatorname{Hom}(T,\mu_{p^\infty}).
\]

Here the index is the largest exponent of the uniformizer dividing the supplied initial ultra-Kolyvagin class. The dual local condition at p is the Tate-orthogonal complement of the source condition. Input: an actual tame Euler system satisfying norm relations and saturated finite conditions away from p; its p-local condition must propagate via closedness (Theorem 6.8). Hyp1–3 require a cyclotomic-kernel element with rank-one free cokernel, an element with no fixed vectors, residual irreducibility, and specified H¹ vanishings over a trivializing field.

**Relevance:** nonordinary local-condition transport and explicit index bounds; not restricted to an ordinary filtration. **Boundary:** the initial class and its index are inputs. The paper does not turn the seed's divided derivative into such an Euler system. Theorem 7.9 works over the analytic distribution algebra and retains two local error ideals; it cannot replace integral height-one control at (p).

**Next admissible use:** compare the seed's actual class/system against Definition 6.2 and Theorem 6.8, especially its full norm relations and local conditions. Do not rerun the content bound without a new class or independently smaller index.

## 2. Supersingular inert-prime Fitting control, now actually read

Ryota Shii, *On the Mazur–Tate refined conjecture for the anticyclotomic tower at inert primes*, arXiv:2503.09034v1, submitted 12 March 2025. [Primary text](https://arxiv.org/html/2503.09034v1). The HTML internally prints August 24, 2026; arXiv history lists only v1, so this is not advertised as a new post-event revision.

Theorem 1.2 proves

\[
\mathcal L_{f,n}\iota(\mathcal L_{f,n})\in\operatorname{Fitt}_{\mathbf Z_p[\operatorname{Gal}(K_n/K)]}\operatorname{Sel}_{p^\infty}(E/K_n)^\vee.
\]

Hypotheses: good supersingular p≥5, p inert in the imaginary quadratic field K, discriminant coprime to pN, p prime to h_K, squarefree N⁻ with an odd number of inert factors, residual surjectivity at 5/irreducibility above 5, and residual ramification at each ell|N⁻ with ell²≡1 mod p. Sections 3–4 explicitly pass through signed local conditions, their finite control terms, and Fitting ideals.

**Relevance:** matches the definite quaternionic setup and covers inert supersingular primes in a finite-level upper-control framework. **Boundary:** inclusion supplies no unit leading coefficient. At augmentation, positive rank prevents reading it as a nonexceptional unit statement. Proposition 2.2 leaves the interpolation scalar as a nonzero algebraic factor; it is not the exact 288 tame normalization.

### Seed hypothesis screen, completed at retained-input grade

Take the retained seed and K=Q(√−7), with

\[
N^-=3\cdot2243\cdot5843=39317547,\qquad
N^+=2^3\cdot4547^2=165401672.
\]

The exact integer arithmetic below is saved in `checks/SHII_SEED_ARITHMETIC.json`. This checks the auxiliary-field splitting and minimal-discriminant data needed here; it does not re-prove the retained conductor or the all-prime residual-image theorem.

| Shii hypothesis | Seed check | Status/boundary |
|---|---|---|
| p≥5, good supersingular at p | Restrict to good supersingular p≥5; then a_p=0 | Domain restriction, not an all-prime claim |
| D_K coprime to pN | D_K=−7, gcd(7,N)=1 | Exclude p=7 |
| p inert in K | (−7/p)=−1 | Domain restriction; split supersingular primes are not covered by this theorem |
| (cp) p∤h_K | h(−7)=1: Minkowski bound 2√7/π<2 leaves only ideal norm 1 | Holds for every p |
| N⁺ split, N⁻ inert | (−7/3)=(−7/2243)=(−7/5843)=−1; (−7/4547)=1; −7≡1 mod8 makes 2 split | Exact residue checks completed |
| (def) N⁻ squarefree, odd number of factors | N⁻ has the three distinct prime factors above | Holds for retained conductor |
| (Im) surjective at 5, irreducible above 5 | Retained full GL₂(F_p) residual image for p≥5 | Retained theorem, not re-certified in this pass |
| (ram) nontrivial inertia at ell∣N⁻ whenever ell²≡1 modp | All three ell are multiplicative: c₄ modell is 1,2005,731; v_ell(Δ_min)=2,1,2. Thus p≥5 never divides the Tate-parameter valuation | Holds at **every** ell∣N⁻, stronger than the conditionally requested subset |

For the last row, a multiplicative curve becomes a Tate curve after at most an unramified quadratic twist. For ell≠p, inertia on E[p] is nontrivial when p does not divide v_ell(q_Tate)=v_ell(Δ_min). An unramified twist does not change that inertia test. The displayed integral model has unit c₄ at these three primes and hence is minimal there. This uses standard local Tate-curve theory plus the exact displayed arithmetic, not an assumption that every bad-prime local group vanishes.

**Result of the screen:** under the retained full residual-image and conductor inputs, all of the explicit hypotheses of Shii Theorem 1.2 hold for the seed at every good supersingular p≥5, p≠7, inert in Q(√−7). There is no further (cp) or (ram) exceptional set here. No Tamagawa-unit assumption is separately printed in Theorem 1.2. This is a source-hypothesis application at written-proof grade, not an independent audit of Shii's proof.

**Next admissible use:** the hypothesis screen is finished. Compare the **actual** theta element/lattice in Shii §2 with the project's detector before importing its Fitting inclusion for that detector. This is an applicable supersingular comparison theorem, not a FIN certificate or an exact integral 288 identity. In particular it covers an inert supersingular subset, not all supersingular primes and not a cofinite set of all coefficient primes.

## 3. Actual theta-content formulas including both supersingular splitting types

Abhishek, Jishnu Ray and Pronay Kumar Karmakar, *Iwasawa invariants of Bertolini–Darmon theta elements*, arXiv:2605.29783v2, 11 August 2026; v2 adds the inert case. [Primary text](https://arxiv.org/html/2605.29783v2).

Read Theorems A–C, §4.2 and the matrix construction in §5.2. In the ordinary case, Theorem A relates sufficiently deep theta elements to the anticyclotomic p-adic L-function by μ(theta)=0 and 2λ(theta)=λ(Lp), under irreducibility and the stated definite/discriminant assumptions. Theorems B/C give signed analogues with explicit q_n corrections for split/inert nonordinary p, retaining the equal finite signed-μ hypothesis. The matrix factors are

\[
C_{f,n}=\begin{pmatrix}a_p(f)&1\\-\Phi_n&0\end{pmatrix}.
\]

**Relevance:** explicit control of unavoidable signed factors and theta content, with finite-level formulas rather than an ordinary-only heuristic. **Boundary:** eventual μ=0 somewhere in the full polynomial does not control its quadratic coefficient; λ remains uncontrolled as p varies. The ordinary proof imports Vatsal/Pollack–Weston μ-vanishing, whose precise normalization and hypotheses need source matching before seed import.

**Next admissible use:** use the signed matrices to identify exactly which factor/content survives a proposed theta-to-derivative comparison. No new theta computation is justified merely to repeat eventual μ-vanishing.

## 4. Newly located finite-level transition law, including additive reduction

Naman Pratap and Anwesh Ray, *An analogue of Kida's formula for Mazur–Tate elements*, arXiv:2511.21979v2, 6 July 2026; published *Mathematische Nachrichten* 299(9), 2652–2679 (2026). [Primary text](https://arxiv.org/html/2511.21979v2), [publisher](https://doi.org/10.1002/mana.70211).

No matches were found for this ID or its Kida/Mazur–Tate title in the searched record. Read Assumptions 1.1–1.2, Theorem 1.3 and §1.5. For an abelian p-extension L/K, after the paper's layer shift and under preservation of additive reduction and its K-p condition, base μ=0 implies upstairs μ=0 and

\[
\lambda_L=[L_\infty:K_\infty]\lambda_K+\sum_{w\in P_1}f_w(e_w-1)+2\sum_{w\in P_2}f_w(e_w-1).
\]

P₁ records split multiplicative primes away from p; P₂ records good primes with local p-torsion. No good/ordinary assumption at p enters this finite-layer theorem.

**Relevance:** tracks exact local costs of an auxiliary abelian extension, including settings involving the seed's bad coefficient primes. **Boundary:** it propagates supplied μ=0 and carries the unknown base λ forward. It is not a source of μ=0, a quadratic leading coefficient, or cofinite Sha vanishing.

**Next admissible use:** apply the explicit local terms to a specified auxiliary-field comparison before claiming that changing fields preserves the required depth/index.

## Lower-priority new source, screened but not a seed import

Dummigan–Golyshev–de Jeu–Kerr, arXiv:2605.11100v1 (11 May 2026), *The 2-part of the Bloch–Kato conjecture, and indivisibility results, for K₂ of some elliptic curves*. [Primary text](https://arxiv.org/html/2605.11100v1). ID and author-combination searches found no matches. Read Introduction/Theorem 1: explicit motivic symbols have bounded regulator divisibility, with different integral-model and generic-fiber lattices carefully separated. It is a concrete example of proving arithmetic content control. But it concerns L(E_u,2), a full-two-torsion Legendre family, and coefficient 2. There is no supplied map to this seed's rank-two Kato derivative. Retain as a technique reference only.

## Duplicates and negative scope

- Bullach–Honnor 2511.07203: already extensively recorded (280 ID hits); arXiv still lists only November 2025 v1. Not a new source delta.
- BKS, Castella–Sano, generalized Kato rank-two papers, Kim's higher Gross–Zagier, DLRV, plectic Heegner classes, Gajek-Leonard–Lei 2508.11007 and Angurel 2605.26917 were already inspected somewhere in the record; not counted anew.
- Feuerpfeil 2608.10811 and 2509.20144 were new search hits. The former's tame Fontaine–Mazur uniform-quotient target is not this residual Selmer bound. No seed-ready application was found; not prioritized.
- A search suggestion attached rank-two CM language to 2609.02030. Opening that actual arXiv ID gives *The Complexity of Justified Representation with Additive Utilities*. The real Banwait rank-two CM paper is 2609.08431 and is already in the September record.

## Assessment

The strongest new source reading for a continuation is Shii's finite-level supersingular Fitting theorem, paired with the explicit signed theta formulas. Loeffler–Zerbes provides a careful local-condition and finite-index comparison toolkit if a genuine new Euler-system input appears. Pratap–Ray supplies auxiliary-extension bookkeeping that was absent from the searched record.

These are relevant additions, not a new arithmetic bound for the seed. None supplies the missing independent cofinite estimate on m_p−w_p, nor the exact cross-prime tame scalar. FIN, ORDER9 and Q36 are unchanged.
