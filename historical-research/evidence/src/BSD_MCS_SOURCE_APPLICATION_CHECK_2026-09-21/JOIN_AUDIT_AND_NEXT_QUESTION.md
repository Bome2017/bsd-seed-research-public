# Audit of MCS_NONSQUAREFREE_JOIN, and the shape of the coefficient question

Date 2026-09-21. Audits `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/MCS_NONSQUAREFREE_JOIN.md`
as a **positive** claim. No successor campaign launched; per the join's own research decision, the squarefree question is
closed at this scope and is not reopened below.

## 1. The load-bearing point, verified independently

The join's step 5 asserts that MCS's Proposition 3.7, Lemma 3.8 and the finite-level comparison "require no additional
use of squarefreeness". I checked this directly against the extracted text rather than accepting it.

**Every occurrence of "square-free" in the paper:**

| line | occurrence | what it is |
|---|---|---|
| 1372 | Hypothesis 3.6(iii) "`N` is square-free" | the conductor hypothesis |
| 1450 | "Under Hypothesis 3.6, Perrin-Riou's Heegner point main conjecture is proved in [BCK21]" | **the only place (iii) is consumed** |
| 670, 679, 1212, 1381 | "square-free products of primes/places" defining `N_{n,m}`, `N(P)`, Def. 2.16 | the auxiliary **Kolyvagin index sets** `n`, unrelated to the conductor |

And the proofs bear this out: Proposition 3.7 invokes only 3.6(iv); Lemma 3.8's proof uses (i) (`p >= 5`, surjectivity),
(ii) (`E(K_v)[p] = 0`), and (iv). Neither touches (iii).

**Conclusion: confirmed.** Within §3.2, `Hypothesis 3.6(iii)` is a pure conduit for the BCK21 import. If the Heegner
point main conjecture is available for a given `(E, K, p)` without squarefreeness, the rest of §3.2 goes through. The
join's structure is sound.

Note the notation collision that makes this easy to get wrong: the paper uses `N` for the conductor **and** `n`,
`N_{n,m}`, `N(P)` for squarefree products of auxiliary primes. A reader scanning for "square-free" sees four false
positives before the real one.

## 2. Citation check — a suspicion of mine that was wrong

The join cites Kataoka-Sano via `jamathr.org/index.php/jamr/article/download/Vol-2Issue-2Paper-1/...`, a URL shape I
initially took for a predatory-journal artefact. It is not. MCS's own bibliography reads:

> `[KaSa24] T. Kataoka, T. Sano, On Euler systems for motives and Heegner points, J. Assoc. Math. Res. 2 no.2 (2024) 154-208.`

*Journal of the Association for Mathematical Research*, volume 2, issue 2 — consistent with the URL. **Citation
verified; no concern.** Recorded because I nearly raised a false alarm, and a false alarm about a source's legitimacy
is as costly here as a missed one.

## 3. The residual-image argument is correct

Step 4's argument: an index-two subgroup of `GL_2(F_p)` is the preimage of the squares under `det` (for `p >= 5`,
`SL_2(F_p)` is perfect, so the abelianization is `F_p^x` via `det`); the corresponding quadratic field is the quadratic
subfield of `Q(mu_p)`, which is ramified at `p`; `K` is coprime to `Np` hence unramified at `p`. So
`rhobar_{E,p}(G_K) = GL_2(F_p)`, and `E(K)[p] = 0`. **Checked, correct.**

## 4. What I did not verify, and deliberately did not pursue

BCK Theorem A and its Hypothesis `♠` — in particular the claim that its ramification clause admits the seed's
`N^- = 1` configuration with multiplicative valuations `2, 1, 2` at `3, 2243, 5843`. The join grades this "imported,
not independently re-audited" and binds it to the author manuscript. I have left it there on purpose: re-auditing it is
the cleanup campaign the join's research decision rules out. It is the single inherited external dependency of (J) and
should be named as such wherever (J) is used.

---

## 5. The coefficient question has a named object, inside the same paper

You asked: can the Heegner-system coefficients be independently computed or bounded? I have not established a method
either. But the object is not shapeless, and the matched machinery is **§4 of the same paper**.

**Why the seed's coefficients are degenerate at the base layer.** With every prime of `N` split in `K` (so `N^- = 1`),
the root number of `E/K` is `-1`, hence `ord_{s=1} L(E/K, s)` is odd; with `ord L(E/Q, s) = 2` this forces
`ord L(E/K, s) >= 3`, and Gross-Zagier gives `hhat(y_K) = 0`. So `y_K` is torsion. **This is not an obstruction** — the
retraction settled that, since `z^Hg_∞` is a Λ-basis and stays one after specialization. What it *is*, is quantitative
information: the base-layer specialization of `y_∞` vanishes, so `y_∞` lies in a positive power of the augmentation
ideal `I = ker(Λ -> Z_p)`, and `π(z^Hg_∞) = y_∞ ⊗ y_∞` lies in a correspondingly deeper power. **The unevaluated
coefficients `I_i(ε^Hg_{n,0})` are therefore governed by the augmentation depth of `y_∞`.**

**That depth is exactly what derived p-adic heights measure**, and MCS §1.4 / §4 is about them:

* Bertolini-Darmon define a filtration `S_p(E/K) = S_p^(1) ⊃ S_p^(2) ⊃ ... ⊃ S_p^(p)` and pairings
  `<·,·>_k^BD : S_p^(k) x S_p^(k) -> Q_k`, where **`Q_k := I^k / I^{k+1}`**. `k = 1` is the usual `p`-adic height.
* Nekovář's spectral sequence for the `I`-adic filtration on `RΓ_F(K,T)` gives `<·,·>_k^Nek : E_k^{0,1} x E_k^{0,1} -> Q_k`.
* **Theorem 1.8 (= Thm 4.2):** for `1 <= k <= p-1`, `E_k^{0,1} = S_p^(k)` and `<·,·>_k^BD = -<·,·>_k^Nek`.

Derived heights exist precisely for the case where the naive (`k = 1`) height degenerates — which is the seed's case.
So the honest restatement of your next question is:

> **Determine the augmentation depth `k` with `y_∞ ∈ I^k Sel(T) \ I^{k+1} Sel(T)`, and evaluate the derived height
> pairing `<·,·>_k` on the resulting class in `Q_k = I^k/I^{k+1}`.**

Theorem 1.8 means either computational tradition may be used, and the Bertolini-Darmon side has an established
anticyclotomic calculus. **This is a shape for the question, not an answer**, and I am not asserting that the depth is
finite, computable, or bounded for this seed.

## 6. A friction at `m = 0` that (J) does not yet handle, and a way to remove it

`(J)` computes `Fitt^i(Sel_{p^n}(E/K)^*)`, and

    0 -> E(K)/p^n E(K) -> Sel_{p^n}(E/K) -> Sha(E/K)[p^n] -> 0,

so extracting `Sha(E/K)[p^n]` requires knowing `#(E(K)/p^n)`, i.e. `rank E(K) = 2 + rank E^K(Q)`. **The twist's rank is
not known for the seed**, so as stated (J) bounds a group of unknown Mordell-Weil content. This is the same Shape-2
failure the project already guards against — controlling a group without separating the known part — and it applies to
(J) at `m = 0` unless `K` is further constrained.

**Proposed refinement (my derivation, not verified against a source):** add to the conditions on `K`

    ord_{s=1} L(E^K, s) = 1.

This is consistent with everything else — root number `-1` over `K` needs `ord L(E^K,·)` odd, and `1` is the smallest
admissible value — and it is checkable numerically for each candidate `K`. Then Gross-Zagier and Kolyvagin apply **to
the twist** (analytic rank one, where that machinery is valid and where the seed's own primitive rank 2 does not
interfere), giving `rank E^K(Q) = 1` and `Sha(E^K)` finite. Hence `rank E(K) = 3` is *known*, `#(E(K)/p^n) = p^{3n}` for
`p` prime to the relevant index, and (J) becomes an identity with a determined Mordell-Weil contribution.

Then, for odd `p`, restriction `Sha(E/Q)[p^n] -> Sha(E/K)[p^n]` is injective — local triviality is preserved and
`cores . res = 2` is an automorphism of a `p`-primary group — so a bound over `K` transfers to `Q`. That is the correct
direction, and it is the one the earlier review already noted.

## 7. Status

No Sha bound. No new primary component. No evaluation of any `I_i(ε^Hg_{n,0})`. FIN, ORDER9 and Q36 unchanged.

What is added here: an independent confirmation that the join's structure is sound, one citation cleared, one residual
external dependency named, a named object and matched machinery for the coefficient question, and one refinement to the
choice of `K` that would remove an otherwise fatal ambiguity in using (J). Nothing modified: master, packet and all
sealed folders untouched.
