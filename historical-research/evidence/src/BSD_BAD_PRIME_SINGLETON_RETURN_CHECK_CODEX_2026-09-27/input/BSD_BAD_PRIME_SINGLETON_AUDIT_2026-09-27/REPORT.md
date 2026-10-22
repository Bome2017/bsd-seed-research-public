# Bad-prime singleton criterion: independent reading-only review

Date: 2026-09-27.

## Verdict

**CRITERION_VALID_AT_ALL_THREE_PRIMES**, as a written corollary of Bullach–Honnor, arXiv:2511.07203v1, Theorem 1.4(b), with the seed's explicitly retained rank, integral-symbol lattice, and Galois-image inputs.

The implication applies at **2243, 4547, and 5843**. In particular, additive reduction at 4547 does not exclude this auxiliary-conductor application. The exact production-to-source conversion is **one half**, not an unknown normalization unit.

This review establishes a sufficient certificate route. It does not evaluate a certificate at any of these primes, prove that a nonzero singleton exists, establish an affordable computation, or prove any new Sha component, FIN, ORDER9, or Q36. The imported Bullach–Honnor result is a **preprint theorem**, not represented here as independently human-refereed or fully re-proved. Its Fitting-ideal conclusion is used, not the refined leading-term conjecture.

## 0. Object, integrity, and permitted work

Input ZIP: `BSD_BAD_PRIME_SINGLETON_REVIEW_BRIEF_2026-09-27.zip`.

SHA-256: `63ebb9e8e924c39ffba1ffe0af611dd1df6af0e6f3737cd8462a84b264210540`.

Before substantive reading, archive members were checked for duplicate names, absolute paths, parent traversal, and symlinks. None was found. The internal manifest verifies **10/10** payloads, with no unlisted payload files; the manifest itself is excluded from its own entries. The six copied files in `SOURCE_BINDINGS.json` separately match **6/6** declared hashes. Those checks bind the supplied copies, not inaccessible original-host files.

`READ_FIRST.md`, `REFRESH.md`, the review task, both claim-specification files, both residual-image documents, the singleton specification, and the current atlas were read as text. No supplied Python file was imported or executed. Work comprised archive/hash processing, source reading, and written algebra. No point counting, primality/candidate search, modular-symbol evaluation, coefficient generation, local build, Lean build, cloud job, or repository change was performed. Batch C was not accessed or altered.

See `MANIFEST_CHECK.json`, `SOURCE_BINDINGS_CHECK.json`, and `FINAL_INPUT_CHECK.json`.

## 1. Precisely normalized statement

Keep the curve, differential, and normalized newform in the input:

\[
E:y^2=x^3-x^2-66020924x-65074271436,
\qquad N=6503188012738584.
\]

Import the recorded facts \(\operatorname{rank}E(\mathbf Q)=2\), full odd residual image and its full p-adic lift for \(p\ge5\), and the unitary-cusp symbol lattice of claim A.4. No fresh replay of those arithmetic inputs is claimed.

**Corollary BH–singleton.** For each

\[
p\in\{2243,4547,5843\},
\]

for every prime \(\ell\nmid pN\) with \(p\mid\ell-1\), let \(K\) be the unique degree-p subfield of \(\mathbf Q(\mu_\ell)\), let \(g\) be a primitive root modulo \(\ell\), and let \(\gamma=\sigma_g|_K\). Put

\[
j(a)=\operatorname{ind}_g(a)\bmod p\in\{0,\ldots,p-1\},
\qquad s_a=\frac{\operatorname{Re}\lambda_f(a/\ell)}{\omega_1},
\]

where \(\omega_1\) is the least positive real period used by the production pipeline and
\(\lambda_f(r)=2\pi\int_0^\infty f(r+it)\,dt\).
Define the **all-label** coefficients

\[
C_i=\sum_{a=1}^{\ell-1}\binom{j(a)}i s_a,\qquad i=0,1,2.
\]

The retained lattice gives \(s_a\in2^{-10}\mathbf Z\), hence \(C_i\in\mathbf Z_p\). Then

\[
\boxed{C_0\equiv C_1\equiv0\pmod p,\quad C_2\not\equiv0\pmod p
\ \Longrightarrow\ \Sha(E/\mathbf Q)[p^\infty]=0.}
\tag{BH-S}
\]

The lower congruences are also forced by the same Fitting/rank argument below and should remain explicit acceptance controls. The stronger exact check \(C_0=0\) follows from the retained \(L(E,1)=0\) and the Hecke relation in the supplied specification.

For an implementation staying within the existing singleton format, impose \(v_p(\ell-1)=1\). The theorem above does not require this stronger condition: even at larger valuation one can project to the **degree-p** quotient. One must not then confuse that quotient with the maximal p-power quotient.

There is no additional hypothesis on \(E(\mathbf F_\ell)[p]\) in this corollary. Its cyclicity or vanishing can be retained as an optional narrower selection restriction, but is not supplied as a necessary condition by this proof. The condition \(p\nmid\#E(\mathbf F_p)\) from the old good-prime specification is likewise not substituted into the bad-prime application.

## 2. Source import and hypothesis ledger

The imported membership is [BH], Hypothesis 1.2 and Theorem 1.4(b), **printed p. 2**:

\[
(\theta_K^{\mathrm{MT}})^\#\in
\operatorname{Fitt}^0_{\mathbf Z_p[G]}
\bigl(\operatorname{Sel}_{p,E/K}^{\vee}\bigr).
\tag{1}
\]

Here \(\operatorname{Sel}_{p,E/K}\) is the **classical p-primary, i.e. p-infinity, Selmer group**, not the finite p-Selmer group and not a modified strict/Greenberg group. The preceding discussion of an integral Selmer group conditioned on finite Sha is not the object used in (1). The relevant proof ends in §4.5, **printed pp. 36–37**, with restriction of classical local conditions and a Fitting-ideal inclusion. Section 3.3, **printed p. 26**, explicitly takes the local conditions from the point Kummer maps.

| Input | 2243 | 4547 | 5843 | Evidence/status |
|---|---|---|---|---|
| p > 3 | Yes | Yes | Yes | Stated target primes |
| Reduction at p | Split multiplicative I1 | Additive III, potentially supersingular | Nonsplit multiplicative I2 | Retained A.1; no new Tate-algorithm run |
| Image contains SL2(Zp) | Yes | Yes | Yes | Retained A.3: full residual image plus p-adic lifting, written/imported grade |
| Hypothesis 1.2(ii)(a): no primitive pth roots in K | Yes | Yes | Yes | K is real: complex conjugation maps trivially to an odd-order quotient |
| Hypothesis 1.2(iii) at additive p | Not needed | Yes | Not needed | K is ramified only at ell, and ell is not p |
| Rational rank two | Yes | Yes | Yes | Retained R.1 |
| Required symbol integrality | Yes | Yes | Yes | Retained A.4; ell is coprime to N, hence a unitary cusp denominator |

The roots-of-unity **alternative** (ii)(a) is the one used. There is no need to prove (ii)(b), semistability, good reduction, ordinarity, or a non-anomalous condition at the coefficient prime. The type III local condition at 4547 is permitted because p is unramified in K.

### Arithmetic input boundary

The included residual-image proof and review were read. Their specialization is the supplied family member m=2243, n=12, A=4547, B=5843. The local irreducibility/transvection argument treats odd coefficient primes away from A, and the rational-isogeny exclusion handles the exceptional coefficient prime A. Claim A.3 additionally carries the standard p-adic lifting step for p>=5. This review does not replace its cited arithmetic inputs with a new proof or an assertion of adelic independence.

The symbol-grid argument also retains its Manin/differential-lattice dependencies. The criterion therefore remains tied to those stated grades; it is not an end-to-end formal certification of the whole seed project.

### Finiteness and main-conjecture imports

The proof of (1) uses [BH] Theorem 3.6, **printed p. 25**, which cites [BB-v1] Corollary 9.6(i), **printed p. 114**. That clause supplies membership of the Kato element in a determinantal image. The stronger generator/equality clause in 9.6(ii), which assumes p-part BSD, is **not** used. No finite-Sha assumption or cyclotomic main-conjecture equality is inserted into this review's corollary.

A source-version caution arose during checking: the current author-hosted [BB-author] has 148 pages rather than the 130 pages of [BB-v1], and its corresponding statement is Corollary 9.7, **printed p. 130**, under Theorem 9.4. At multiplicative p, that version imposes the stronger condition that
\(F(\sqrt{-2A/B})\) contain no primitive pth root of unity for a short model \(y^2=x^3+Ax+B\).
This does not introduce a missing hypothesis here. Every field F used in the conductor-ell proof is a subfield of \(\mathbf Q(\mu_\ell)\), hence unramified at p; adjoining a square root has local ramification index at most 2, whereas \(\mathbf Q_p(\mu_p)\) has ramification index p-1>2. At 4547 the potentially-good alternative applies directly. This elementary verification covers the stronger condition, rather than silently conflating the two source versions. Their full long proofs have not been independently reconstructed here.

## 3. Proof of the Selmer transfer

### 3.1 Large image removes the restriction kernel

For any finite abelian K/Q, the restriction of the residual representation to G_K still has an image containing SL2(Fp): the commutator subgroup of the full GL2(Fp) image is contained in that restriction image. The standard two-dimensional module has no nonzero SL2(Fp)-invariant vector. Thus

\[
E(K)[p]=0,\qquad E(K)[p^\infty]=0.
\]

This also agrees with [BH], Remark 2.9, **printed p. 11**. Inflation–restriction for \(E[p^\infty]\) now gives an injection

\[
H^1(\mathbf Q,E[p^\infty])\hookrightarrow
H^1(K,E[p^\infty])^G.
\]

For each place v of Q and w|v, the diagram of rational point inclusion and Kummer maps commutes. Hence restriction carries the classical local Kummer image at v into the one at w. We need only inclusion of local conditions, not a local control isomorphism. This is valid at the bad places, at p, and at the auxiliary ramified place ell.

Therefore

\[
\operatorname{Sel}_{p,E/\mathbf Q}\hookrightarrow
\operatorname{Sel}_{p,E/K}^{G}.
\tag{2}
\]

No factor [K:Q] is divided out. In particular, the fact that p divides [K:Q] is not ignored.

### 3.2 Fitting membership bounds the minimal number of generators

Let R=Zp[G], X=Sel_{p,E/K}^vee, and Y=X/pX. Classical Selmer groups over number fields are cofinitely generated over Zp without any Sha-finiteness assumption. Thus X is finitely generated over Zp and over R, and the presentations used below are finite over the Noetherian rings in question.

Since G=C_p,

\[
R/pR=A=\mathbf F_p[t]/(t^p),\qquad t=\gamma-1.
\]

Let d=dim_Fp(Y/tY), the minimal number of A-generators. A minimal surjection A^d -> Y has kernel contained in tA^d: reduction modulo t is an isomorphism onto Y/tY. Choosing finitely many relations therefore gives a presentation with every matrix entry in (t). Its maximal minors lie in (t)^d, and hence

\[
\operatorname{Fitt}^0_A(Y)\subseteq(t)^d.
\tag{3}
\]

Fitting ideals commute with arbitrary base change, including the nonflat reduction R->A; see [Stacks], Lemma 15.8.4(3). Reducing (1) gives a member of the ideal in (3). Section 4 below identifies its quadratic coefficient as C2/2 when C0=C1=0. If C2 is nonzero, that element has order exactly two in t, so d<=2. If d>=p then (t)^d=0, which also cannot contain this nonzero element.

Only **Fitting membership**, not annihilation, yields (3). For example, Y=(A/(t))^3 has annihilator (t), which contains the nonzero element t^2, while Y needs three generators and its zeroth Fitting ideal is (t^3). Replacing Fitt by Ann would invalidate the criterion.

### 3.3 Two generators leave no Sha summand

Pontryagin duality in (2) gives a surjection

\[
X_G\twoheadrightarrow X_{\mathbf Q}:=
\operatorname{Sel}_{p,E/\mathbf Q}^{\vee}.
\]

The coinvariant quotient is compact, and the augmentation image is closed because X is finitely generated over Zp. Thus

\[
\dim_{\mathbf F_p}(X_{\mathbf Q}/pX_{\mathbf Q})
\le\dim_{\mathbf F_p}(X/(p,\gamma-1)X)=d\le2.
\tag{4}
\]

The ordinary Kummer exact sequence, with no assumption of finite Sha, dualizes to

\[
0\longrightarrow D\longrightarrow X_{\mathbf Q}
\longrightarrow\mathbf Z_p^2\longrightarrow0,
\qquad D=\Sha(E/\mathbf Q)[p^\infty]^{\vee}.
\]

This splits as a Zp-module sequence because Zp^2 is free. D is finitely generated, and consequently

\[
\dim_{\mathbf F_p}(X_{\mathbf Q}/pX_{\mathbf Q})
=2+\dim_{\mathbf F_p}(D/pD).
\]

Equation (4) forces D/pD=0. Nakayama's lemma forces D=0, and Pontryagin duality gives Sha(E/Q)[p^infinity]=0. This eliminates both finite p-torsion and any hypothetical divisible corank. A corank comparison alone would not suffice; the proof uses the minimal **generator count**. QED.

### 3.4 The lower-order checks also follow without Ota at bad p

The same quotient to Zp^2 gives d>=2 regardless of the witness outcome. Therefore (3) and (1) force the mod-p Mazur–Tate element into (t^2). After the normalization below, C0=C1=0 modp follows. Thus the bad-prime version of the C1 acceptance test is justified by this corollary's BH/Fitting argument, **not** by invoking Ota outside its allowed range.

The stronger C0=0 exact check is already available: the supplied Hecke relation says
\(\sum_{a=1}^{\ell-1}s_a=(a_\ell-2)[0]^+\), and the retained analytic argument gives [0]^+=0.

## 4. Exact correspondence with the production symbols

[BH] §2.1 and Definition 2.2, **printed p. 8**, fix the total Neron real period. The input curve has positive discriminant and two real connected components, so

\[
\Omega^+_{\rm BH}=\int_{E(\mathbf R)}|\omega_E|=2\omega_1.
\]

The coordinate change between the supplied original and minimal models has u=1, so it changes neither the Neron differential nor this period ratio. Both definitions use the same normalized newform and the same lambda_f. Therefore

\[
[a/\ell]^+_{\rm BH}=\frac{s_a}{2}.
\tag{5}
\]

The minus component changes sign under a -> -a, while sigma_-1 restricts trivially to real K. Pairing those terms cancels the entire minus contribution after projection. Projection to the degree-p group ring **sums** terms; it does not average over the kernel. Hence, in the all-label convention,

\[
\boxed{\theta_K^{\rm MT}
=\frac12\sum_{a=1}^{\ell-1}s_a\gamma^{j(a)}.}
\tag{6}
\]

If one instead sums over representatives modulo plus/minus, (6) becomes the sum of s_a over those representatives. One must choose one convention and not divide by two again. The existing specification uses all ell-1 labels, and (6) is its exact conversion.

Claim A.4 gives s_a in 1/1024 Z at these unitary cusps. Thus the BH plus symbols lie in 1/2048 Z, which is p-integral at every target prime. There is no extra Manin multiplier in (5): the retained Manin information is part of proving lattice membership, not another factor relating two definitions of lambda_f divided by a period.

If n_a=1024 s_a is the certified integer, then

\[
C_2\bmod p=1024^{-1}\sum_a\binom{j(a)}2 n_a\bmod p,
\]

and the BH coefficient is the same integer sum multiplied by 2048^{-1}. Both inverses exist. Binomial weights already extract the literal degree-two coefficient; no additional derivative factorial is inserted.

### Involution and generator conventions

In A/(t^3), the source involution gives t -> -t+t^2. Thus

\[
(C_0,C_1,C_2)\longmapsto(C_0,-C_1,C_2+C_1).
\]

With the lower coefficients zero, the BH involuted quadratic coefficient is exactly C2/2 modp. In particular the # in Theorem 1.4(b) does not change its nonvanishing.

Under g -> g^u, with u prime to ell-1, the production coefficients satisfy

\[
C_2'=u^{-2}C_2+
\frac{u^{-2}-u^{-1}}2 C_1\pmod p.
\]

Consequently nonvanishing is generator-invariant after C1=0. This is algebraic covariance, not independent authentication of the symbol table.

### Euler factors and exceptional-zero conventions

Equation (6) compares with the **final Mazur–Tate element of Definition 2.2**. No imprimitive theta_S, modified Kato class, cyclotomic alpha-factor, division by an Euler factor, or division by an L-invariant is introduced. The Euler-factor manipulations inside the source proof are part of the imported theorem, not modifications to be guessed by the certificate program.

The source proof also excludes a Teichmuller component in an intermediate field. It vanishes on projecting to the odd-degree real K; the final Theorem 1.4(b) already states membership for the full theta_K. It is not an additional p-dependent normalization of (6).

## 5. Comparison with the existing bad-prime routes

| Target | Retained route in input B.6–B.8 | New sufficient interface checked here |
|---|---|---|
| 2243 | Cubic cyclotomic coefficient at denominator p^2, with split exceptional-zero/control and height/L-invariant inputs | Quadratic coefficient at a different good auxiliary denominator ell; use BH Fitting membership and classical Selmer transfer |
| 5843 | Quadratic cyclotomic coefficient at denominator p^2, with the retained Skinner/Jones and period-import qualifications | Quadratic coefficient at good auxiliary ell, using the separate BH theorem |
| 4547 | Additive-prime two-prime Kurihara sufficient route; desired cyclotomic machinery not supplied | Quadratic singleton criterion under BH's additive-unramified condition |

The split cubic and the new quadratic coefficients belong to different extension variables. Here the abelian extension has conductor ell, not p^2, and ell is a good prime. The split-multiplicative prime 2243 does not divide that conductor. Thus this application does not import the old cubic exceptional-zero interface. This does not prove that a particular singleton coefficient is nonzero; accidental or arithmetic vanishing remains possible.

The present corollary uses none of the old p-adic height computations, fitted multiplier K=288, G2 auxiliary-regulator theorem, or refined Mazur–Tate leading-term comparison. Those results are not invalidated or upgraded; this is an alternative sufficient route.

No globally uniform nonzero witnesses are obtained. Even if the three target components were eventually settled by it, finite support and the exact real leading term would remain separate obligations.

## 6. Prior-work and novelty boundary

The supplied REFRESH.md reports that BH was already read for uniformity and a p=5 check; it reports a scoped failure to locate this bad-prime singleton transfer in the named earlier sweep and map. I do not claim the paper or general Fitting-ideal idea is new.

I inspected the supplied B.6–B.8 claims, the current atlas, the old singleton specification, and the residual-image source and review. They contain the older cyclotomic/Kurihara routes and the good-prime Ota implementation. They do not already state the fully normalized corollary (BH-S) and its classical Selmer generator argument for these three bad primes. The **candidate argument itself is already in the submitted task**, so its discovery is not claimed by this review either.

The additional work here is independent validation, exact normalization, the bad-prime hypotheses/transfer proof, and explicit limits on implementation. The original-host sweep documents named but not bundled, and the entire current Git history, were not independently searched. Therefore “not already elsewhere in the project” is not established. No mathematical novelty claim is made.

## 7. Only proposed next step: a later bounded cost screen

The mathematics passing does not establish that any run is affordable. No candidate prime or coefficient cutoff was computed in this review.

A later cost screen should use actual prime auxiliaries ell not dividing pN, with p dividing ell-1 (and preferably valuation one to retain the current data format). Every possible odd prime auxiliary satisfies ell>=2p+1. The small good-prime runs do not benchmark this larger range automatically.

For this route the supplied engine interface is still

- denominator m=ell;
- M=1 and Q=N;
- root-number sign +1;
- production lattice 1/1024 Z, with the output divided by two only when mapping to BH's convention.

The corresponding two-cusp exponential scale is m sqrt(Q)=ell sqrt(N). The old multiplicative denominator p^2 route instead has scale p^2 sqrt(N/p)=p^(3/2)sqrt(N). Their ratio ell/p^(3/2) is a comparison of **exponential scales only**, not a verified ratio of CPU-time, truncation bounds, dollar costs, or success rates.

The later screen must derive actual outward cutoffs with the quarter-tail safety rule and all period/division error included, align the cutoff to 2^24-sized segments, and compare with the corpus that exists **at that later time**. The old 3,281-segment specification is a historical record, not a current capacity assertion. It must count the dominant coefficient production, repaired verification and scan, all ell-1 symbol enclosures, transform/assembly work, memory and disk, not just the final three sums. Truncation and lattice identification must use rigorous inequalities, not midpoint reuse or a nonrigorous prescreen.

A future executable specification needs a separately named **BH theorem profile**. Do not simply disable Ota's p-not-dividing-N check while retaining its theorem label. It must carry this hypothesis ledger, period conversion, source version, and new justification of C1. The arithmetic extraction can remain byte-compatible with the old all-label table. Nonzero, inconclusive-zero, and invalid remain distinct; no automatic successor is authorized.

The permissible next deliverable is a measured/derived feasibility report and a user decision, **not production**. This review makes no assertion that it fits the user's budget or that the old $2,000-plus computation has now been replaced by a free one.

## 8. Final disposition

- Candidate sufficient implication: **VALID**, at all three target primes, at the stated written/preprint/import boundary.
- Exact normalization: **theta_BH = (1/2) theta_pipeline**, after projecting to the real degree-p field.
- Arithmetic hypotheses: satisfied using the explicit retained image/rank/lattice inputs; additive 4547 is included because p is unramified.
- New primary component: **NONE**.
- Singleton existence or a nonzero seed value: **NOT PROVED/NOT COMPUTED**.
- Affordability or a runtime guarantee: **NOT ESTABLISHED**.
- Batch C, repositories, frozen records and production tools: **UNCHANGED**.
- Source proof depth: the application and transfer are proved here; BH and its underlying Euler-system theorems remain named preprint imports, not fresh full reconstructions.

This removes the theorem-range objection to this particular bad-prime singleton route. The next open questions for the route are a usable auxiliary, rigorous cost, and a successful certified value—not the good-reduction restriction of Ota.

### References

**[BH]** D. Bullach and M. Honnor, *On the refined ‘Birch–Swinnerton-Dyer type’ conjectures of Mazur and Tate*, arXiv:2511.07203v1, 10 November 2025. Hypothesis 1.2 and Theorem 1.4(b), p. 2; §2.1/Definition 2.2, p. 8; Remark 2.9, p. 11; Theorem 3.6, p. 25; §3.3, p. 26; §4.5, pp. 34–37. Source: https://arxiv.org/pdf/2511.07203v1 ; HTML: https://arxiv.org/html/2511.07203v1 .

**[BB-v1]** D. Bullach and D. Burns, *On Euler systems and Nekovář-Selmer complexes*, arXiv:2509.13894v1, Corollary 9.6(i), p. 114. Source: https://arxiv.org/pdf/2509.13894v1 . Only the relevant statement/dependency was checked; no full audit of this 130-page work.

**[BB-author]** Same authors and title, current author-hosted 148-page manuscript, Theorem 9.4 and Remark 9.6, p. 129; Corollary 9.7, p. 130. Source: https://dominikbullach.github.io/bb.pdf . This is a mutable author-hosted source; no local byte hash is claimed. Its relevant strengthened field condition is separately addressed above.

**[Stacks]** The Stacks Project, §15.8, “Fitting ideals”, Lemma 15.8.2 (definition via presentations) and Lemma 15.8.4(3) (base change). Source: https://stacks.math.columbia.edu/tag/07Z6 .

The mathematical source text was fetched and read through the web tool. Screenshots were inspected for BH p. 2 and p. 8 and for the author-hosted BB pp. 129–130. Some other screenshot and direct-container download attempts failed; no local copy/hash of these PDFs is represented as verified, and third-party papers are not redistributed in this result package.
