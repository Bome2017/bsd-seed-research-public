# Seventeenth addendum — κ is odd: the κ-parity theorem and the supersingular-graph lemma, referee-audited, sealed

**Tier: PROOF — REFEREE-AUDITED (two fresh Claude referees, no-repair mandate), PASS WITH REMARKS on both objects; operator pre-review of revision 1 carried; operator re-audit of the sealed texts NOT performed.** Seals, byte for byte, the working directory `H41_KAPPA_PARITY_2026-09-14` as it stood when the three referee reports were received (`R/`, 27 files): `R/KAPPA_PARITY_PROOF.md` revision 2 (`825c91d2…`), `R/GRAPH_LEMMA.md` revision 2 (`29091400…`), both revisions 1 (`9e57f73f…`, `4094e2a4…`), the operator's review, the three referee reports as written, the generators, receipts and checkers. Nothing here adds mathematics to the carried documents: the only computation is digest checks, regeneration of the carried documents and receipts, and mechanical extraction of the quotations below, each re-checked byte for byte (`receipts/VERBATIM_VERIFICATION.txt`). Prior objects unmodified and byte-identical (`receipts/PRIOR_OBJECTS.txt`).

## 1. The theorems

The proof is stated on the six operator-fixed inputs of its §0 and on (K1)–(K5) of its §4; two of those inputs, Input 1 and (K1), are proved by the companion lemma.

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 69-71
```text
**Theorem A.** $B-A=3\,(2^{m+1}-1)$. Consequently $e_x\mid B-A$ for every $x\in S$, and the slope
$$s_x:=\frac{B-A}{e_x}\in\{\,3(2^{m+1}-1),\ 2^{m+1}-1\,\}$$
is odd for every $x\in S$.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 98-102
```text
**Theorem B.** Let $x\in S$, put $\widehat{\mathcal O}:=\widehat{\mathcal O}_{X_R,x}\cong R[[U,V]]/(UV-2^{e_x})$ (Input 1), and choose the coordinates so that, near $x$, $C_\infty=\{V=0\}$ and $C_0=\{U=0\}$ (thus $U$ is a local coordinate on $C_\infty$ at $x$ and $V$ one on $C_0$; this is a relabelling of $U,V$ if necessary). The coordinates $U,V$ exist only in the completed local ring, and the statement is made there. Then, in $\widehat{\mathcal O}[1/2]$ and in the completed stalk $\widehat\Omega_x:=\Omega_x\otimes_{\mathcal O_{X_R,x}}\widehat{\mathcal O}$ respectively,
$$F_p=2^{A}\,U^{s_x}\,u_x\quad\text{with }u_x\in\widehat{\mathcal O}^{\times},\qquad d\log F_p=s_x\,\frac{dU}{U}+\frac{du_x}{u_x},$$
and therefore, in $\bar{\mathbf F}_2$,
$$\operatorname{res}_x(\bar\omega_\eta)=s_x\equiv 1,\qquad\text{residue of }\bar\omega_\eta|_{C_0}\text{ at }x=-s_x\equiv 1 .$$
By Input 4 the same holds for $\bar\omega_f$: $\operatorname{res}_x(\bar\omega_f)=\pm s_x\not\equiv 0\pmod 2$ at every $x\in S$, for $e_x=1$ and $e_x=3$ alike.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 135-139
```text
**Theorem C.**
(i) *(The toric residue map.)* $\rho_J:H^0(X_{\bar{\mathbf F}_2},\Omega)\to\operatorname{Cot}(T_J)\cong X_J\otimes\bar{\mathbf F}_2$ is surjective with kernel the residue-free differentials. Consequently $\eta\mapsto(\operatorname{res}_x\eta)_{x\in S}$ induces an isomorphism
$$\operatorname{Cot}(T_J)\ \cong\ \Bigl\{\,r\in\bar{\mathbf F}_2^{\,S}:\ \textstyle\sum_{x\in S}r_x=0\Bigr\}=H_1(\Gamma,\bar{\mathbf F}_2)=X_J\otimes\bar{\mathbf F}_2 ,$$
and a regular differential with a nonzero residue at some node has nonzero image in $X_J\otimes\bar{\mathbf F}_2$.
(ii) *(Parity.)* $\kappa$ is odd. In particular $\kappa\ge1$ and $q^*(\xi_E)\ne0$.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 202-202
```text
**Theorem D (position E).** Assume $E_0=E$. Then $P_c=q(c)$ has exact order $t=4$; equivalently $[2]P_c\ne O$. By (K5) this is the exact missing assertion of position E: $|(C_0\cap K_q)[2^\infty]|=2^{m-2}$, $w_3\equiv1\pmod 2$, $4\lambda$ odd — the negative H41-W bit (N) in position E.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 208-208
```text
**Theorem D′ (position B).** Assume $E_0=B$. Then $P_c\ne O$, i.e. $t=2$; by (K5): $|(C_0\cap K_q)[2^\infty]|=2^{m-1}$, $w_3\equiv1\pmod 2$, $4\lambda$ odd — the bit (N) in position B.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 212-212
```text
**Positions G and F: OPEN.** In both, $n=m-2$ is odd, so $\Phi[2^\infty]=0$: the $2$-primary image of $\operatorname{sp}(P_c)$ is trivial whatever $\kappa$ is, and Lemma 4.1 holds but decides nothing. For G the required assertion is $P_c\ne O$ ($t=2$), which the component group at $2$ cannot see. For F the required assertion is the mod-$4$ statement $w_3\equiv2\pmod4$ on the integer lift $z$ (W §2), which no mod-$2$ residue argument can produce. Both remain open; so does the vertex identification itself.
```

The companion discharges the two inputs that were "operator-fixed, not in a sealed object":

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 32-32
```text
**Input 1 (thicknesses; regular dual graph).** For $x\in S$,
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 173-173
```text
**(K1)** Geometric Néron component group of $J$ at $2$: $\Phi_J:=\pi_0(\mathcal J_{\bar{\mathbf F}_2})\cong\mathbf Z/3\cdot2^m$, and for $c:=[0]-[\infty]\in J(\mathbf Q)$ the specialization $\operatorname{sp}_J(c)\in\Phi_J$ has exact order $2^m$; hence
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/GRAPH_LEMMA.md` lines 216-229
```text
**Theorem G (the supersingular graph of $X_0(2p)$ at $2$).**

**(i) Points.** $S$ is in bijection with the set of $\operatorname{Aut}(E)$-orbits on the $p+1=2^{m+2}$ cyclic subgroups of order $p$ of the supersingular curve $E/\bar{\mathbf F}_2$, and
$$\#S=\frac{2^m+4}{3}.$$

**(ii) Thicknesses.** For $x\in S$ let $e_x:=\tfrac12|\operatorname{Aut}(E,C_x)|=|\operatorname{Stab}_{\bar G}(C_x)|$. Then $e_x\in\{1,3\}$: **exactly two** points have $e_x=3$ and the remaining $(2^m-2)/3$ have $e_x=1$. Consequently
$$\sum_{x\in S}\frac1{e_x}=\frac23+\frac{2^m-2}3=\frac{2^m}3\qquad\Bigl(=\frac{p+1}{12}\Bigr).$$

**(iii) Local structure and regular dual graph** ($=$ Input 1). $\widehat{\mathcal O}_{X_R,x}\cong R[[U,V]]/(UV-2^{e_x})$ with $e_x$ as in (ii); the minimal regular model $X'_R\to X_R$ replaces each $x\in S$ by a chain of $e_x-1$ projective lines of self-intersection $-2$; the special fibre $X'_{\bar{\mathbf F}_2}$ is reduced, its dual graph $\Gamma'$ is the two vertices $C_\infty,C_0$ joined, for each $x\in S$, by a path of length $e_x$ — two paths of length $3$ and $(2^m-2)/3$ paths of length $1$.

**(iv) Component group** ($=$ (K1)). Let $\mathcal J$ be the Néron model over $R$ of $J_K=J_0(2p)_K$ and $\Phi_J:=\pi_0(\mathcal J_{\bar{\mathbf F}_2})$. Then
$$|\Phi_J|=3\cdot2^m,\qquad \Phi_J\cong\mathbf Z/3\cdot2^m\ \text{(cyclic)},$$
and for $c:=[0]-[\infty]\in J_0(2p)(\mathbf Q)\subset J_K(K)$ the specialization $\operatorname{sp}_J(c)\in\Phi_J$ has exact order $2^m$; hence
$$\Phi_J[2^\infty]=\langle\operatorname{sp}_J(c)\rangle\cong\mathbf Z/2^m .$$
```

## 2. The operator's review of revision 1, and the mandate

The operator reviewed revision 1 of the proof (`9e57f73f…`) on 2026-09-14 (`R/audits/OPERATOR_REVIEW_OF_REVISION_1.txt`, extracted mechanically from the session transcript), found the chain coherent, verified Česnavičius Theorem 2.13 and the Conrad–Stein monodromy sequence independently, and required one repair before audit:

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/OPERATOR_REVIEW_OF_REVISION_1.txt` lines 10-10
```text
There is, however, one technical correction I would make before audit. In Theorem B the coordinates \(U,V\) are supplied only in the completed local ring
```

The repair was made as revision 2 (`R/receipts/REVISION_1_TO_2.diff`; the proof's own record):

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 242-242
```text
- **Revision 2** (this file): one local-ring/completion repair in Theorem B, made on the operator's review of 2026-09-14 ("the coordinates $U,V$ are supplied only in the completed local ring … the clean repair is simply to do this entire local argument in $\widehat{\mathcal O}$ and conclude $u_x\in\widehat{\mathcal O}^\times$"). The statement now asserts $u_x\in\widehat{\mathcal O}_{X_R,x}^\times$ and the identity $d\log F_p=s_x\,dU/U+du_x/u_x$ in the completed stalk $\widehat\Omega_x$; the proof computes the divisor of $F_p$ on $\operatorname{Spec}\widehat{\mathcal O}$ (normal, as the completion of an excellent normal local domain), identifies the valuations $\operatorname{ord}_{\mathfrak p_\infty},\operatorname{ord}_{\mathfrak p_0}$ of $\widehat{\mathcal O}$ with $\operatorname{ord}_{C_\infty},\operatorname{ord}_{C_0}$, and writes $du_x/u_x=c_x\,dU/U$ with $c_x\in\widehat{\mathcal O}$ before restricting to the two branches. The header line and this section were updated accordingly. No other statement, constant, input or citation was changed; the exact edit is `receipts/REVISION_1_TO_2.diff`.
```

The operator's ledger at that point, and the mandate the seal follows:

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/OPERATOR_REVIEW_OF_REVISION_1.txt` lines 24-33
```text
SLOPE_PARITY = CANDIDATE_PROVED
SLOPE_RESIDUE_BRIDGE = CANDIDATE_PROVED
RESIDUE_KAPPA_BRIDGE = CANDIDATE_PROVED
KAPPA_ODD = CANDIDATE_PROVED

NEGATIVE_E_SEED = CANDIDATE_PROVED
NEGATIVE_B_SEED = CANDIDATE_PROVED
NEGATIVE_G_SEED = OPEN
NEGATIVE_F_LIFT = OPEN
NEGATIVE_ONE_CYCLE = OPEN
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/OPERATOR_REVIEW_OF_REVISION_1.txt` lines 37-37
```text
I would now give the exact `KAPPA_PARITY_PROOF.md` to a fresh referee with a no-repair mandate: verify A, B, C, Lemma 4.1, and D/D′ independently; specifically attack the regular-resolution intersection computation, the \(UV=2^e\) residue normalization, the Picard/Néron toric-cotangent identification, and the direction of the monodromy functoriality. If any step fails, require a concrete first invalid equality. If it passes, then seal the graph lemma and κ-parity theorem together. KAPPA_PARITY_PROOF
```

The operator also asked that the $A_4$-orbit/thickness calculation become "its own small proved lemma" and that (K1) be derived from the same graph; that is `R/GRAPH_LEMMA.md`.

## 3. The audits

Three reports, each by a fresh Claude agent under a no-repair mandate, launched from session `9c846d6b-0835-4fb2-b039-7eb92193e32d` on 2026-09-14 and carried as written (`R/audits/`). Referee 1 audited the proof; referee 2 audited the lemma, failed it on one clause, and — continued in the same context — re-audited the repaired revision 2.

| object | digest | referee | verdict |
|---|---|---|---|
| `R/KAPPA_PARITY_PROOF.md`, revision 2 | `825c91d2…` | `REFEREE_1_KAPPA_PARITY_REV2.md` | PASS WITH REMARKS |
| `R/history/revision_1/GRAPH/GRAPH_LEMMA.md`, revision 1 | `4094e2a4…` | `REFEREE_2_GRAPH_LEMMA.md` | FAIL on one delimited clause (§3 local ring) |
| `R/GRAPH_LEMMA.md`, revision 2 | `29091400…` | `REFEREE_2B_GRAPH_LEMMA_REV2.md` | PASS WITH REMARKS; revision-1 defect removed |

**Referee 1** (the proof) verified Theorems A, B, C, Lemmas 4.1–4.2, Theorems D, D′ and the G/F paragraph step by step, with the four stress points the operator named: the regular-resolution intersection computation (re-derived by an independent Laplacian/effective-resistance argument and checked numerically), the $UV=2^{e}$ residue normalization (revision 2's completed-ring bookkeeping verified line by line and cross-checked globally), the Picard/Néron toric-cotangent identification (checked against Č16, Č18, Mazur and BLR 9.2/8, 9.7/2, 8.4/1), and the direction of the monodromy functoriality (checked against variance and against Conrad–Stein Lemma 6.3 / Proposition 6.5, whose Prop. 6.5 forces $\kappa\mid n_E$, consistent with Lemma 4.1).

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_1_KAPPA_PARITY_REV2.md` lines 40-40
```text
None found.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_1_KAPPA_PARITY_REV2.md` lines 126-126
```text
**PASS WITH REMARKS.** Every step of the chain Theorem A → Theorem B → Theorem C → Lemma 4.1 → Theorems D, D′ holds as written, on the stated Inputs 1–6 and (K1)–(K5): the regular-model intersection computation was re-derived by an independent Laplacian/effective-resistance argument and verified numerically at $m=3$ (and $m=5,7,9,11$), the completed-local-ring residue computation of revision 2 was verified line by line and cross-checked globally by the degree of the reduced function $\bar F$ on each component, the Picard/Néron identifications (C1)–(C4) and the commutative square were verified against the cited sources (Č16, Č18, Mazur, BLR 9.2/8, 9.7/2, 8.4/1) and standard duality, the functoriality direction in (K2)/Lemma 4.1 was checked against variance and against Conrad–Stein Lemma 6.3/Proposition 6.5 (with the consistency bonus that their Prop. 6.5 forces $\kappa\mid n_E$, in agreement with Lemma 4.1), and Lemma 4.2 was recomputed symbolically and with PARI for all Mersenne $m\le17$. No invalid equality or implication was found. The remarks — the exact value of $\#S$ in a non-load-bearing Remark relying on "exactly two thickness-3 points" beyond Input 1 as stated, the unwritten (but derivable) multiplicity-1 claim in A(b), the notational sense of $\operatorname{Cot}$, the receipt rows $m=7,9$ lying outside the hypothesis $p$ prime, the stale `MANIFEST.sha256` (revision-1 digest, and not the contents l.235 claims), and the still-unverified theorem number SGA 7 IX 11.5 — do not affect validity. What this report does not certify: Inputs 1–6 and (K1)–(K5) themselves (taken as given per mandate; Input 1 and (K1) rest on the unsealed companion `GRAPH_LEMMA.md`), and the vertex identification $E_0\in\{E,B\}$, which the document correctly keeps as a hypothesis of §4.
```

**Referee 2** (the lemma, revision 1) passed (i), (ii), the graph derivation of (iv) and the receipts, and failed the local-ring clause of (iii):

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_2_GRAPH_LEMMA.md` lines 32-34
```text
**First invalid assertion (document line 86, verbatim):**

> The hypothesis "$p\ne2,3$" in the appendix is introduced only *after* the chain statement, for the classification "$k>1\Rightarrow j=0,k=3$ or $j=1728,k=2$"; that classification is not used here — §2 below determines $k_x$ directly.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_2_GRAPH_LEMMA.md` lines 128-128
```text
**FAIL** — on one precisely delimited defect, with everything else passing.
```

Revision 2 of the lemma answered this by proving the clause in residue characteristic $2$ (its §3: the $\Gamma_1(p)$-rigidified curve is regular and semistable at $2$ by Č16, so its completed local rings at supersingular points are $R[[u,v]]/(uv-2)$; the coarse curve is its quotient by the diamond operators, whose stabilizer is $\operatorname{Aut}(E,C_p)/\{\pm1\}$ of order $e_x\in\{1,3\}$; the invariants of a tame cyclic action on $uv=2$ are $UV=2^{e}$; the minimal resolution of $UV=2^3$ is computed explicitly), quoting the appendix's standing convention and marking Mazur–Rapoport as orientation only. The lemma's own record:

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/GRAPH_LEMMA.md` lines 353-354
```text
- **Revision 1** (2026-09-14, sha256 `4094e2a4f73fbe25b009b595e4d1e6911abb89323797c114ad196be0259db835`): audited by a fresh referee (no-repair mandate), verdict FAIL on one delimited clause: §3 justified the local ring $\widehat{\mathcal O}_{X_R,x}\cong R[[U,V]]/(UV-2^{e_x})$ by citing Mazur–Rapoport Theorem (1.1) c), which the appendix states under the standing convention "$N$ … not divisible by $2$ or $3$" (corpus l.6568–6569, not quoted in revision 1); revision 1's claim that the hypothesis "$p\ne2,3$" entered only for the classification $k\in\{2,3\}$ was false. Everything else — (i), (ii), the graph derivation of (iv), the receipts — passed.
- **Revision 2** (this file): §3 rewritten to *prove* the local-ring clause in residue characteristic $2$: the $\Gamma_1(p)$-rigidified curve $Y$ is regular and semistable at $2$ (Č16, quoted as [S5]), so its completed local rings at supersingular points are $R[[u,v]]/(uv-2)$ (Lemma 3.1); $X_R=Y_R/H$ for the diamond operators, with completed local rings the invariants under the stabilizer (Lemma 3.2), which is $\operatorname{Aut}(E,C_p)/\{\pm1\}$ of order $e_x\in\{1,3\}$ (Lemma 3.3, anchored on Mazur's [S6]); the action is faithful and branch-preserving (Lemma 3.4); and the invariants of a tame cyclic action on $uv=2$ are $UV=2^e$ (Lemma 3.5). The minimal resolution of $UV=2^3$ is computed explicitly (Lemma 3.6). §0 now quotes the appendix's standing convention, marks [S2] as orientation only, adds [S5], [S6] and the standard facts (F1)–(F5) — including the two the referee found unlisted, (F2) and (F3) — and §5's accounting is rewritten accordingly. §4(c) now says "as some $e_x=3$" instead of "as both $e_x=3$ and $e_x=1$ occur". Theorem G's statement, §2 and §4 are otherwise unchanged; the receipts are unchanged.
```

**Referee 2B** (the lemma, revision 2, targeted):

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_2B_GRAPH_LEMMA_REV2.md` lines 31-31
```text
None found.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/audits/REFEREE_2B_GRAPH_LEMMA_REV2.md` lines 94-94
```text
**PASS WITH REMARKS.** The defect found in revision 1 is removed: the local-ring clause of Theorem G(iii), previously justified by citing Mazur–Rapoport Theorem (1.1) c) outside the appendix's standing convention 6 ∤ N (now quoted at l.50–54 and marked orientation-only), is now proved in residue characteristic 2 by Lemmas 3.1–3.5 (regular node on the Γ₁(p)-rigidified curve, quotient by the diamond operators, stabiliser Aut(E,C_p)/{±1} of order e_x, faithful branch-preserving action, tame-invariant computation with a rigorous normal form), and the minimal regular model with its chains of (−2)-curves by Lemma 3.6 and the Conclusion. Every step of the new §3 was verified independently by the referee and holds; the quotations [S5], [S6] are byte-identical to the corpus and used only in their quoted form; (F1)–(F5) are correctly stated; the rewritten §5 is accurate as to what is proved and what is cited, and [S2] is used nowhere. All remarks — the terse "same criterion" for the third chart of Lemma 3.6 and the unmentioned maximal ideals off the special fibre in the other charts (both verified by the referee), the notation V(V) for the reduced branch V(2,V), the uncited projectivity of Y and finiteness of π, the line-cited (not verbatim-quoted) normality of X at Č16 l.353–354, Mazur's footnote's "order 4 or 6" omitting order 3, the labelling of [S5](a), and the omission of [S4] from the §5 list — are recorded above with the explicit finding that none affects validity. With revision 2, Input 1 and (K1) of `KAPPA_PARITY_PROOF.md` are discharged by this document, on the quoted corpus passages and the listed standard facts, with no dependence on the coarse local-ring statement of the literature.
```

**Remarks recorded by the referees, none affecting validity** (the reports carry them in full): the proof's Remark (iii) in Theorem A uses "exactly two thickness-3 points", beyond Input 1 as stated there, and Theorem A(b) asserts the reducedness of the resolved fibre — both now proved by Theorem G(ii)–(iii); the working directory's `MANIFEST.sha256` was stale at audit time — regenerated at sealing, and now covers every carried file; the receipt rows $m=7,9$ lie outside the hypothesis $p$ prime (correct identities of the models nonetheless); "Cot" is to be read as invariant differentials; the theorem number SGA 7 I, Exp. IX, 11.5 remains unverified by any referee (its content is the Conrad–Stein Definition 4.2 sequence, which was verified); in the lemma, the third chart of Lemma 3.6 is argued tersely, $V(V)$ denotes the reduced branch $V(2,V)$, the projectivity of $Y$ and finiteness of $\pi$ are uncited, the normality of $X$ is line-cited rather than quoted, Mazur's footnote says "order 4 or 6" where order 3 also occurs, and [S4] is missing from the lemma's §5 list.

## 4. Status, in the operator's format

The proof's own flags, as sealed:

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 160-163
```text
`SLOPE_PARITY = PROVED` (Theorem A: every slope is odd, not merely one).
`SLOPE_RESIDUE_BRIDGE = PROVED` (Theorem B, for $e_x=1$ and $e_x=3$, on the coarse model and on the regular model).
`RESIDUE_KAPPA_BRIDGE = PROVED` (Theorem C).
`KAPPA_ODD = PROVED` on Inputs 1–6 — unaudited, unsealed.
```

**Verbatim** — `H41_KAPPA_PARITY_ADDENDUM_017/R/KAPPA_PARITY_PROOF.md` lines 215-216
```text
`NEG_E_B_ONLY = PROVED`, conditionally on $E_0\in\{E,B\}$ and on (K1)–(K5).
`NEG_G = OPEN`. `NEG_F = OPEN`. `NEG_ONE_CYCLE = OPEN` (no uniformity over the vertex).
```

With this seal, on the referee audits:

    SLOPE_PARITY            PROVED (referee-audited)      Theorem A
    SLOPE_RESIDUE_BRIDGE    PROVED (referee-audited)      Theorem B
    RESIDUE_KAPPA_BRIDGE    PROVED (referee-audited)      Theorem C
    KAPPA_ODD               PROVED (referee-audited)      Theorem C(ii), on Inputs 2–6 and Theorem G
    INPUT_1                 PROVED (referee-audited)      Theorem G(ii)–(iii)
    K1                      PROVED (referee-audited)      Theorem G(iv)
    NEGATIVE_E_SEED         PROVED conditionally on E₀ = E and on (K2)–(K5)   Theorem D
    NEGATIVE_B_SEED         PROVED conditionally on E₀ = B and on (K2)–(K5)   Theorem D′
    NEGATIVE_G_SEED         OPEN
    NEGATIVE_F_LIFT         OPEN
    NEGATIVE_ONE_CYCLE      OPEN
    VERTEX_IDENTIFICATION   OPEN
    OPERATOR_REAUDIT        NOT PERFORMED on the sealed texts

"PROVED (referee-audited)" means: an ordinary proof, independently audited by a fresh agent under a no-repair mandate, with no invalid equality found; not machine-checked, and not yet re-audited by the operator. The E and B bits remain conditional on the vertex identification exactly as the record's rows are; never present them as unconditional.

## 5. What the proof rests on, and what remains external

Inputs 2–6 of the proof are used only in their stated form (referee 1, §5 of its report): the eta unit and its divisor (ADDENDUM_002), the cusp sections (M §2, Č18 Rem. 5.3), $(D3)_M$ (ADDENDUM_016), the Manin constant at $2$ (Č18 Thm 2.11/2.13, verified by the operator and by referee 1), and the character-group index $\kappa$ (definition). (K2)–(K5) are used as stated; (K2)'s functoriality was verified against Conrad–Stein. Input 1 and (K1) are now Theorem G. External citations not in the corpus and not independently checked by any referee: SGA 7 I, Exp. IX, §11, Thm. 11.5 (number), [Con00], [DR73, VI.6.7, VI.6.9], [Edi91, Prop. 2] (quoted via Č16/Č18), [Čes17, 4.1.4, 4.4.4] and [KM85, 2.7.4] (quoted via Č16 in the lemma's [S5]); checked by the referees: BLR 9.2/8, 9.7/2, 8.4/1(a), 9.6/1, 7.2/1; Conrad–Stein 2001 (Def. 4.2, Ex. 4.3, Lemmas 6.2–6.3, Prop. 6.5, Thm 8.2); Silverman AEC III.8.6, V.4 and Ex. 5.7; Edixhoven 1990 (for the record: stated only for $p\ge5$, which is why the lemma proves rather than cites).

## 6. Custody

* **Carried byte for byte:** `R/` is the working directory as it stood when the reports were received, every file listed with its digest in `receipts/CARRIED_ARTIFACT_CUSTODY.txt`; the three referee digests (`825c91d2…`, `4094e2a4…`, `29091400…`) are the digests the referees themselves computed and named in their reports.
* **Re-checked at sealing** (`receipts/REPRODUCTION.txt`): revision 2 of the proof regenerates byte for byte from revision 1 and the carried edit script; the lemma and its canonical-verbatim receipt regenerate from the carried generator and the sealed corpus; the verbatim verification, the numerical checker output and the PARI/GP vertex data reproduce.
* **Prior objects** (`receipts/PRIOR_OBJECTS.txt`): ADDENDUM_001–016 and the two CODEX freezes, archive digests and every manifest entry re-checked.
* The operator's review text is the user message at transcript line 6 of session `9c846d6b-0835-4fb2-b039-7eb92193e32d` (2026-09-14T15:19:23.886Z), extracted mechanically; the referee reports are the files the agents wrote, unmodified.

## 7. What is and is not promoted

* **PROVED (referee-audited):** $\kappa$ odd (Theorem C), with Theorems A, B, and Theorem G (Input 1, (K1)).
* **PROVED conditionally:** the negative E and B bits (Theorems D, D′), on the vertex identification and (K2)–(K5).
* **VERIFIED / PROVED, unchanged:** G (ADDENDUM_014); M (ADDENDUM_015); $(D3)_M$ (ADDENDUM_016).
* **Not promoted:** positions G and F; the negative one-cycle theorem; the vertex identification $E_0\in\{E,B\}$; `(C)`; the H41 seed; the positive branch. The mechanism decides nothing at G and F: there $\Phi[2^\infty]=0$ (Lemma 4.2), and F is a mod-$4$ statement no mod-$2$ residue argument can produce.

## 8. Next — G and F, and the vertex

For G the required assertion is $P_c\ne O$ ($t=2$), invisible to the component group at $2$; for F it is $w_3\equiv2\pmod4$ on the integer lift; both remain open, as does which vertex the optimal curve is (proved $E_0=E$ only for $m+2\in\{5,7,13,17\}$). The operator's direction after the audit is to be recorded in the next object, not here.

## 9. Status ladder

**Verbatim** — `H41_D3M_PROOF_ADDENDUM_016/ADDENDUM.md` lines 157-161
```text
    G         VERIFIED   ADDENDUM_014    (C) ⟺ T_p = q̂(S₀^B)
    M         VERIFIED   ADDENDUM_015    definitions and model resolution
    (D3)_M    PROVED     ADDENDUM_016    this object
    R         NEXT                       (D3)_M ⟹? T_p = q̂(S₀^B)
    (C)       OPEN
```

    G         VERIFIED   ADDENDUM_014    (C) ⟺ T_p = q̂(S₀^B)
    M         VERIFIED   ADDENDUM_015    definitions and model resolution
    (D3)_M    PROVED     ADDENDUM_016    ω̄_η = ω̄_f
    κ odd     PROVED     ADDENDUM_017    this object (referee-audited); Input 1 and (K1) proved (Theorem G)
    E, B bits PROVED     ADDENDUM_017    conditionally on the vertex and (K2)–(K5)
    G, F bits OPEN
    (C)       OPEN

**The H41 seed remains unproved.**
