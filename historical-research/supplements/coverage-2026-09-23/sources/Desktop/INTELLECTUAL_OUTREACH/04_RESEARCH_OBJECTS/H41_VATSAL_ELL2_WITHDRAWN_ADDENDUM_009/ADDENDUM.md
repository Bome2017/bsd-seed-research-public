# Ninth addendum — the ℓ = 2 Vatsal application is WITHDRAWN; the missing statement is `(X)`

**Tier: NEGATIVE SOURCE-AUDIT RESULT, plus two corrections to this project's own drafts.** No new
mathematics is claimed. No computation or research stage was launched. Prior objects unmodified and
byte-identical: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`,
`3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`.

## 1. The result — a direct source audit of Vatsal Proposition 5.3 AND ITS PROOF

Read from the full paper text frozen in `CODEX_H41_SEED_RESEARCH_FREEZE_001`
(`vatsal.txt`, `15b31f6f…`, 1920 lines), not from any summary or theorem statement.

**Proposition 5.3 as actually written** (line 1481):

> Let `E₀ ⊂ J₀(N)` be the strong Weil curve. Suppose that `E₀[ℓ]` is reducible as a `Gal(Q̄/Q)`-module,
> **and that `E₀` is ordinary at `ℓ`**. Then 1. `ℓ² ∤ N`, for the conductor `N`, and 2. there exists an
> `E′ ∈ C` such that there is an étale isogeny `E₀ → E′` of degree `ℓ`.

* It **assumes** reducibility of `E₀[ℓ]` **and ordinariness at `ℓ`**.
* It **concludes** `ℓ² ∤ N` and the existence of an étale degree-`ℓ` isogeny. `ℓ² ∤ N` is therefore a
  **conclusion, not a hypothesis**; any deduction that feeds `4 ∤ N` in as the unlocking hypothesis has
  the implication backwards.
* Section 5 operates with `ℓ` odd from its opening paragraph — 5.1, line 1461: *"Let `E ∈ C`, and let `ℓ`
  denote an **odd** prime."* — and the immediately preceding Lemma 5.2 is explicitly *"`ℓ` is an **odd**
  prime"*.

**The decisive step of the proof** (line 1736), which is the step that places the cuspidal subgroup
inside `E₀`:

> Note also that the action of `Gal(Q̄/Q)` on `C_g` is via the character `χ`, and that **each of the
> ±-eigenspaces for complex conjugation in `E₀[ℓ]` has dimension 1**. But now the multiplicity one
> theorem of `J₀(N)[m]^et` … shows that **the `α` eigenspace for complex conjugation** inside `J₀[m]` is
> one-dimensional over `F_ℓ`, where `α` denotes the parity of `χ`. It follows that
> **`C_g ∩ E[ℓ] = E[ℓ]^α ≠ 0`**, and this proves our proposition.

**This step does not survive at `ℓ = 2`, where `+1 = −1`.** Over `F₂` there is no decomposition into
`±`-eigenspaces for complex conjugation: the claim that each has dimension 1 is not a statement, the
"`α` eigenspace" indexed by the parity of `χ` separates nothing, and `E[2]^α` is undefined. The
intersection conclusion `C_g ∩ E[ℓ] ≠ 0` is therefore unavailable at 2 — and it is precisely the
conclusion that would put a cuspidal point on the elliptic factor.

Note carefully **which** ingredient fails. It is the eigenspace separation under complex conjugation, not
the multiplicity-one theorem. A characteristic-2 extension of a multiplicity-one lemma — Wiles's lemma or
any successor — therefore does **not** repair this proof, because the proof needs multiplicity one *and*
the `±` splitting, and only the latter is what breaks.

**Consequently the attempted Vatsal/Byeon deduction of a rational cuspidal 2-torsion point on the
optimal H41 factor is WITHDRAWN.** It was an invalid application of an odd-`ℓ` theorem.

Recorded as handed in by the operator and **not independently verified here** (no Ohta source is present
in this corpus and no search was performed): Ohta's later description of Vatsal's result characterises it
as an odd-prime / non-two-torsion theorem, consistent with the direct reading above.

## 2. Corroborating exclusions at ℓ = 2 — recorded at their literal hypotheses only, not upgraded

**Byeon–Kim**, Acta Arith. 165.4 (2014), *Optimal curves differing by a 5-isogeny* (`ab7ce81d…`). The
word "cuspidal" occurs in it **zero** times. Its relevant statement:

> **Theorem 2.2 (Dummigan).** Let `E ∈ C` be an elliptic curve defined over `Q` of square-free conductor
> `N` with a rational point of order **`l ∤ N`**. Then `E₀ ∈ C` has a rational point of order `l`.

The hypothesis is `l ∤ N`, not `l² ∤ N`. Our `N = 2p` has `2 | N`, so the hypothesis fails outright. Its
Proposition 4.1 additionally requires `l` odd, `N` squarefree, `l ∤ N`.

**Agashe**, J. Théor. Nombres Bordeaux 30 (2018), *Rational torsion in elliptic curves and the cuspidal
subgroup* (`558108697d…`) — the paper whose title is the desired statement:

> Let `A` be an elliptic curve over `Q` of square free conductor `N` that has a rational torsion point of
> prime order `r` such that **`r` does not divide `6N`**. … If `A` is optimal, … `r` divides the order of
> `A ∩ C`.

`r = 2` divides `6` **and** divides `N`: excluded on both counts. Its Lemma 3.2 (Dummigan) and
Corollary 3.4 are stated for odd `r`; Proposition 3.6 for `r > 3`.

Every statement audited on this line excludes `ℓ = 2` either directly (`r ∤ 6`, `r` odd, `r > 3`) or via
`ℓ ∤ N`. Our case — `ℓ = 2`, `2 | N`, `4 ∤ N` — lies in the intersection of both excluded regimes. These
are recorded as exclusions at their literal hypotheses. **No claim is made that no theorem anywhere can
close the gap**; only that none of the audited ones does.

## 3. CORRECTION — cuspidal 2-primary cyclicity is NOT an outstanding obligation

`ADDENDUM_008` §5 recorded a prerequisite on the order of `[0]−[∞]`, and a draft of this object listed
2-primary cyclicity as a missing obligation. **Both were wrong: the frozen record already discharges
them.** `CODEX_H41_SEED_RESEARCH_FREEZE_001/01_stage_I/STAGE_I_RECONSTRUCTION.md` (`995227e9…`),
tier-marked **THEOREM**:

> **THEOREM — negative source.** For `N=2p`, `p=2^n−1` prime, Chua–Ling's table gives
> `#C₀=(p²−1)/8`, `#C₀[2^∞]=2^m`. Their level-1 minus level-`N` cusp is `[0]−[∞]`, up to sign. Here
> `p≡1 (mod 3)`, `v₂(p−1)=1`, `v₂(p+1)=n`. **The entire cuspidal 2-part is also cyclic of this order, by
> their Theorem 1(iii).**

Arithmetic consistency, checked here: `v₂(#C₀) = v₂(p−1) + v₂(p+1) − 3 = 1 + n − 3 = n−2 = m`, matching
the stated `#C₀[2^∞] = 2^m`. So `[0]−[∞]` generates `C₀` of order exactly `(p²−1)/8`, whose 2-primary
part is cyclic of order `2^m`. A cyclic 2-group has exactly one element of order two. Therefore

    T_p = ((p²−1)/16)·([0]−[∞])

**is already the unique nonzero cuspidal point of order two on the negative branch**, uniformly in `p`.
Nothing further about the structure of the cuspidal 2-part needs proving. That side is finished.

## 4. CORRECTION — the "unique 2-torsion line" conclusion does NOT hold uniformly

A draft of this object concluded that the line-identification problem is vacuous uniformly. **That was
circular and is withdrawn.** What is actually proved is a statement about the **displayed base** `E`:

    A² − 4B = (1−2r)² − 4r² = 1 − 4r = D = −p < 0,

symbolically for every member, so `x²+Ax+B` is irreducible over `Q`, `E(Q)[2] = ⟨(0,0)⟩ ≅ C₂`, and `E[2]`
has a single `Gal`-stable line. Confirmed at `n = 5, 7, 13, 17, 19, 31`, torsion `C₄` throughout.

This does **not** transfer to the optimal curve `E₀`, because `E₀ = E` is not proved uniformly. The
frozen four-vertex analysis, tier-marked **THEOREM**:

> `E,F,G` each have one rational 2-torsion point, whereas **`B` has all three** … rational torsion
> `C₄, C₂×C₂, C₂, C₂`, respectively, at the 2-part.

and, tier-marked **OPEN**:

> **OPEN — optimal selection, including cyclic four.** The actual `Γ₀(N)`-optimal vertex is not
> classified.

The `B` position remains admissible, and `B(Q)[2] ≅ C₂ × C₂` has **three** rational 2-torsion lines. So
in an optimal position with several rational 2-torsion lines the identification problem is live. The
statement *"the question of which 2-torsion line is cuspidal is vacuous uniformly"* must not enter the
record. It holds for the displayed base, and at `n = 5, 7, 13, 17` where `E₀ = E` was independently
proved in `ADDENDUM_007` — four levels, which do not establish it uniformly.

## 5. The corrected remaining architecture

The missing existence statement is

    (X)      T_p ∈ π̂(E₀)[2] ⊂ J₀(2p)[2].

`T_p` is already pinned on the cuspidal side (§3). What is unproved is that it lands on the embedded
optimal elliptic factor. **Vatsal does not prove `(X)` at `ℓ = 2`** (§1), and no audited theorem supplies
it (§2).

Even granted `(X)`, in an optimal position carrying several real 2-torsion lines one must still verify
that the corresponding Kummer/Betti character is the **particular primitive character** `α_p`. So the
safest ultimate target remains unchanged:

    (C)      χ_p = α_p (mod 2).

`(L)` stays retired — sufficient, and stronger than needed. `S₀ ∈ E₀(Q)[2]` is still not to be written
without proof: a Betti character fixed by complex conjugation is not thereby rational, and in
disconnected-real-locus positions that distinction bites.

## 6. Explicit statements for the record

* **Vatsal does not prove `(X)` at `ℓ = 2`.** The ℓ=2 application is invalid and is withdrawn.
* **`T_p` itself is already uniquely determined on the cuspidal side**, uniformly, via Chua–Ling
  Theorem 1(iii) as recorded in frozen Stage I. This is not an open obligation.
* **The displayed base has a unique rational 2-torsion line**, by the symbolic identity `A²−4B = −p`.
* **Uniform optimality `E₀ = E` is not proved.** The `B` position, with `C₂ × C₂`, is not excluded.
* **The accessible levels where `E₀ = E` is proved — `n = 5, 7, 13, 17` — do not establish that
  uniformly.**
* **The negative H41 seed remains unproved.**
* **The positive branch remains entirely outside this architecture** (`N = 2·3·ℓ`; `F_p` is not defined
  there).

## 7. What this object leaves cleaner than the draft it replaces

Nothing new must be proved about the structure of the cuspidal 2-part; that is finished. The genuinely
new characteristic-2 question is narrower and better posed than the old Jacobian problem: **whether the
unique order-two point of the cuspidal group lands on the correct optimal elliptic Betti line.** That is
`(X)`, followed where necessary by the line identification feeding `(C)`.

**The H41 seed remains unproved.**
