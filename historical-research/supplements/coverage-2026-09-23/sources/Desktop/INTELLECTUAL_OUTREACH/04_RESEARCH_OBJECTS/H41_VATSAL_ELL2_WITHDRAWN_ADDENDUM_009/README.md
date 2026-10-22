# H41_VATSAL_ELL2_WITHDRAWN_ADDENDUM_009

A negative source-audit result, plus two corrections to this project's own drafts. **No new mathematics.
No computation or research stage launched.** All prior objects byte-identical.

**The result.** The attempted `ℓ = 2` application of Vatsal Proposition 5.3 is **invalid and is
withdrawn**. Read from the full frozen paper text, not from a summary:

* the proposition **assumes** reducibility of `E₀[ℓ]` and ordinariness at `ℓ`, and **concludes** `ℓ² ∤ N`
  together with an étale degree-`ℓ` isogeny — so `ℓ² ∤ N` is a conclusion, not an unlocking hypothesis;
* §5 operates with `ℓ` odd from its opening paragraph 5.1, and the immediately preceding Lemma 5.2 is
  explicitly for odd `ℓ`;
* the proof's decisive intersection step uses the **separate `+` and `−` complex-conjugation eigenspaces
  in `E₀[ℓ]`**, concluding `C_g ∩ E[ℓ] = E[ℓ]^α ≠ 0`;
* that step **does not survive at `ℓ = 2`, where `+1 = −1`** — over `F₂` there is no `±` decomposition,
  and `E[2]^α` is undefined.

The failing ingredient is the **eigenspace separation**, not multiplicity one. So a characteristic-2
extension of Wiles's multiplicity-one lemma does not repair this proof.

**Corroborating exclusions**, recorded at their literal hypotheses only: Byeon–Kim's Theorem 2.2
(Dummigan) needs `l ∤ N` and we have `2 | N` — and that paper contains the word "cuspidal" zero times;
Agashe 2018, whose title is the desired statement, needs `r ∤ 6N`, and `r = 2` divides both. Our case
`ℓ = 2`, `2 | N`, `4 ∤ N` lies in the intersection of both excluded regimes. No claim that no theorem
anywhere can close it.

**Correction 1 — cyclicity is already done.** Frozen Stage I records, tier-marked THEOREM from
Chua–Ling Theorem 1(iii), that for `N = 2p` we have `#C₀ = (p²−1)/8`, `#C₀[2^∞] = 2^m`, and the entire
cuspidal 2-part is cyclic. Hence `T_p = ((p²−1)/16)([0]−[∞])` **is already the unique nonzero cuspidal
order-two point**, uniformly. This also discharges the prerequisite `ADDENDUM_008` §5 left hanging.
Nothing further about the cuspidal 2-part needs proving.

**Correction 2 — no uniform "unique 2-torsion line".** `A² − 4B = −p < 0` proves the **displayed base**
has one rational 2-torsion line. It does not transfer to `E₀`: the frozen four-vertex analysis gives `B`
the full `C₂ × C₂`, and the optimal vertex is tier-marked **OPEN**. So the claim that line identification
is vacuous uniformly was circular and is withdrawn; it holds for the base, and at `n = 5,7,13,17` where
`E₀ = E` was independently proved.

**The corrected architecture.**

    (X)   T_p ∈ π̂(E₀)[2] ⊂ J₀(2p)[2]        -- the missing existence statement
    (C)   χ_p = α_p (mod 2)                  -- the safe ultimate target

`T_p` is pinned on the cuspidal side; what is unproved is that it lands on the embedded optimal elliptic
factor, and then that the corresponding Kummer/Betti character is the particular primitive `α_p`. `(L)`
stays retired. `S₀ ∈ E₀(Q)[2]` is still not to be written without proof.

    ADDENDUM.md      the seven sections
    computation/     audit_vatsal_source.sh, verify_frozen_record.sh, base_2torsion.gp
    receipts/        VATSAL_SOURCE_AUDIT, FROZEN_RECORD_CHECK, BASE_2TORSION

**The H41 seed remains unproved.**
