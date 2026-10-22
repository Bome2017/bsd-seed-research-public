# RETRACTION AND CORRECTED VERDICT — MCS source-application check

Date 2026-09-21. **Additive.** `MCS_APPLICATION_VERDICT.md` is not edited; it is preserved unmodified as evidence.
Where the two conflict, **this file governs**. Authority for the correction:
`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/MCS_RETURN_REVIEW.md`.

I re-read the paper properly this time — `pdftotext` of `arXiv:2603.23978v1`, §3.2, lines 1360-1500 of the extraction.
Every correction below is verified verbatim at the source. **Three of the four reasons I gave were wrong**, and the
fourth was stated as a permanent structural no-go that the evidence never supported.

## RETURN (unchanged in outcome, corrected in reasons): `NO_CHANGED_ARROW`

The stopping decision stands. The reasons are replaced.

---

## 1. Retracted: "no Greenberg/Kummer comparison supplied"

**Proposition 3.7 (verbatim).** "Assume Hypothesis 3.6(iv). Then we have canonical identifications
`Sel_{p^n}(E/K_m) = H^1_F(K, A_{n,m}) = H^1_{F*}(K, A*_{n,m}(1))`."

The classical `p^n`-Selmer group **is** identified with the Selmer-structure cohomology, under `p` non-anomalous
(Hyp. 3.6(iv)). The proof checks the image of the Kummer map at every `v | pN` explicitly, citing
[Gre97, Prop. 2.5] at `v | p` and `H^1_F(K_v, A_{n,m}) = H^1_f(K_v, A_{n,m})` by definition at `v ∤ p`.

My claim that the paper "supplies no comparison" and that the brief's warning applied was **false**. The comparison is
Proposition 3.7.

## 2. Retracted: "Hypothesis 2.17 is an unproved nonvanishing input"

**Lemma 3.8 (verbatim).** "Assume Hypothesis 3.6. Then there exists a core vertex for `F` on `A_{n,m}` (see
Definition 2.16) that belongs to `N_{n,m}`. Moreover, we have `χ(F) = χ(F) = 0`. **(In particular, Hypothesis 2.17 is
satisfied.)**"

It is proved, not assumed — via `p >= 5` and Hyp. 3.6(i), the Poitou-Tate sequence, and Proposition 3.7. My claim that
it is "the same species of unproved arithmetic nonvanishing" was **false**.

## 3. Retracted, and this one was the serious error: the Heegner-torsion argument

**What the construction actually is.** Theorem 3.9 takes `y_∞ ∈ Sel(T)`, *the system of Heegner points* over the
anticyclotomic tower, and produces a **unique Λ-basis** `z^Hg_∞ ∈ det^{-1}_Λ(RΓ_F(K,T))` with
`π(z^Hg_∞) = y_∞ ⊗ y_∞`. Definition 3.10 forms `z^Hg_m` as the image of `z^Hg_∞` under the natural **surjection**
to level `m`, and sets `ε^Hg_{n,m} := ϖ_{n,m}(z^Hg_m)`. **Remark 3.11 (verbatim):** "Since `z^Hg_∞` is a Λ-basis, we
see that `ε^Hg_{n,m}` is an `R_{n,m}`-basis."

So the object is a **determinant basis of a Λ-module, and it remains a basis after specialization**. My inference

    y_K torsion  =>  the Heegner Stark system degenerates  =>  the Fitting identity carries no bound

is **invalid at the middle step**. Vanishing of one specialization does not imply vanishing in the family:
`T != 0` in `Z_p[[T]]` yet `T|_{T=0} = 0`; and a Λ-basis `e` of `Λe` still reduces to a basis mod `T` even where an
associated element such as `T^2 e` specializes to zero.

**Worse than a wrong step.** I wrote that this is "not repairable", that it holds "for every admissible `K`", and that
"any anticyclotomic Heegner construction inherits it." That is a structural impossibility claim about an entire class
of constructions, asserted from the introductory statements alone — my own recorded reading grade said the application
proofs were not audited, which is exactly what such a claim would require. **It must not enter the no-resurrection
register**, and I withdraw it in full. The Gross-Zagier computation for the base point `y_K` may well be correct; it
simply does not license the conclusion I drew from it.

## 4. The obstruction I missed, which is the real one

**Hypothesis 3.6 (verbatim).**
(i) `ρ : G_K -> Aut(E[p])` is surjective.
(ii) `E(K_v)[p] = 0` for every `v | N`.
**(iii) `N` is square-free.**
(iv) `p` is non-anomalous, i.e. `H^0(K_v, Ẽ_v[p]) = 0` for any `v | p`.

The seed's conductor `N = 2^3 * 3 * 2243 * 4547^2 * 5843` **fails (iii)**. Theorem 3.12 is therefore not directly
importable as stated. **This is an applicability failure, not a proof that an extension is impossible**, and no
extension is attempted or assessed here.

Note the irony worth recording: the non-squarefree conductor is the same hypothesis failure that has now blocked
Dickson-Neururer, Berger-Betina's (St), and this paper. It is the seed's most persistent literal obstruction, and it is
a hypothesis in each case — never a theorem that no extension exists.

## 5. What actually remains unknown (corrected)

An abstract determinant-module isomorphism does not by itself evaluate the arithmetic coordinates that a Sha bound
needs. No seed-specific coordinate estimate, all-prime bound, or real regulator comparison is obtained here. And —
a second thing I asserted without proof — **calling the paper's coordinates and the WC witness both "coordinates" does
not identify them.** I claimed the unknown coordinate "is the same object the WC audit isolated". That identification
was not proved and is withdrawn. The retained WC equivalence (Theorem O1) stands unchanged, neither strengthened nor
weakened by this paper.

An auxiliary quadratic field is also **not** by itself fatal, contrary to the tone of my §3: for odd `p`, restriction on
primary Sha is injective, since local triviality is preserved and corestriction-after-restriction is multiplication
by 2, an automorphism of a `p`-primary group. That observation supplies no bound and no seed application; it only
removes a bad reason I gave.

## 6. Threshold and custody (this part of the original stands)

Under finiteness, the retained small-primary results (`2, 3, 5, 7, 11`) give `#Sha = 9t^2` with `gcd(t,2310) = 1`, so
order 9 or at least `9 * 13^2 = 1521`. `< 1089` remains **sufficient** but is no longer the sharp threshold. The
2026-09-20 invention packet is historical and should not be presented as current without that qualification; my count
of stale occurrences in it was not independently verified by the review. Fresh references should cite master §3 and its
bound inputs rather than a movable line number.

## 7. Status

FIN, ORDER9 and Q36 remain open. No global arrow is established. No successor operation is authorized or launched.
Nothing in the master handoff, the invention packet, or any sealed folder was modified by this operation.
