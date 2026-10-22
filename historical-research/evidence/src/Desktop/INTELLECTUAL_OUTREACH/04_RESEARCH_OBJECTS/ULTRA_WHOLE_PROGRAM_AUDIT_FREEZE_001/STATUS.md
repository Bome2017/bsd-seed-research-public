# STATUS — ULTRA_WHOLE_PROGRAM_AUDIT_FREEZE_001

**Object type:** external whole-program audit, audited and frozen.
**Reviewer:** Codex 6 Ultra, two-stage protocol with a frozen Stage-I reconstruction.
**Disposition:** ACCEPTED AS A SUCCESSOR AUDIT RECORD. Its five findings are confirmed. Its
principal mathematical consequence is confirmed by construction. **It is not a certification of
anything new, and no new theorem is released by this object.**

## 1. The header, disambiguated

    CURRENT_CERTIFIED_BOUNDARY = PROBLEM_FOUND
    RANK_GATE                  = CLOSED

Both are correct and they are consistent. `PROBLEM_FOUND` refers to **five defects in
Claude-built verification records**, not to any defect in a theorem, statement, proof or certified
boundary. All five were checked independently and all five are real. None is in the theorem class.
See `receipts/THEOREM_VS_RECEIPT_DEFECTS.txt`.

The sharpest of them: my shipped construct scanner's axiom check omitted `re.MULTILINE`, so it
was structurally incapable of finding an `axiom` declaration below line 1. An injected control
file declaring `axiom another_one : False` is reported by it as `axiom 0`. My positive controls
were all plain substrings and never exercised the regex path — having written "positive controls
are mandatory for construct scanners" as a standing rule, I shipped a scanner whose controls did
not cover the one check that could silently fail.

**What that did and did not touch.** The axiom evidence the certification rests on is
`#print axioms` on each of the five theorems, regenerated externally: standard axioms only. That
is kernel-level and cannot be fooled by a text scan. The residual risk — an axiom declared in the
tree but unused by the five theorems — is now closed by a corrected, self-tested scan:
**0 axiom declarations in both returned trees**, with 296 `theorem` and 13 `lemma` hits firing as
positive controls, and 0 for sorry/admit/native_decide/ofReduceBool/trustCompiler/sorryAx.

## 2. The principal missed consequence — CONFIRMED IN LEAN

    E_q(Q) is finite.

Ultra's argument is correct and short: pointwise torsion makes the doubling orbit of any `P` land
in a finite set of multiples; a maximal-height member `Q` of that set satisfies
`H(Q)^4 ≤ C·H(2Q) ≤ C·H(Q)`, so `H(Q)^3 ≤ C`; and `H(P) ≤ H(Q)`, so every rational point lies in
one certified-finite height sublevel.

I formalised it against **both** certified trees from the certified inputs only — 45 lines, exit 0,
`[propext, Classical.choice, Quot.sound]`. This is substantially stronger than rank zero and needs
no Mordell–Weil. **It is not certified**: it is a Claude reachability check, withheld from any
handoff, exactly as in `GATE_R_FINAL_ASSEMBLY_PRESHIP_RECORD_001`.

One addition Ultra does not make: the derivation does not use `1 ≤ C` from the R1 statement.

## 3. The 2-primary consequence — true, with a concrete availability gap

`E_q(ℚ)[2^∞] ≅ C₂`, hence `v₂(|E_q(ℚ)|) = 1`, is mathematically correct. It requires `T ∉ 2E`,
and **`T ∉ 2E` is `private` in both returned modules** (run A line 153, run B line 143), with
nothing equivalent exported by the certified base. So the corollary is *not* available from the
public certified interface; a future packet must export or reprove that lemma.

The public interface alone is genuinely insufficient, not merely inconvenient: `C₄` is finite with
`|A/2A| = 2` and `v₂(|A|) = 2`. The same `C₄` obstruction the three earlier design reviews raised,
one level up.

## 4. The analytic finding, and its tier

    UNIFORM_ALL_H41_ANALYTIC_CONTROL = UNSUPPORTED

Unsupported by the literature Ultra found — **not disproved**. The named research target checks
out as far as exact arithmetic can take it:

* `r = −128` gives `ε = −1, m = 7, A = 257, B = 16384, D = 513 = 3³·19`, and **H41 holds on the
  positive branch**: two distinct prime divisors, both ≡ 3 mod 4, both valuations odd, `m ≥ 3`.
  A valid H41 base, verified here.
* The curve chain is exact: the base curve at `q = 1` and Ultra's `[1,64,0,1024,0]` share
  `j = 4824238966273/537919488`; `c₄ = 16897`, `c₆ = 1973503`, `Δ = 537919488 = 2²⁰·3³·19` all match
  Ultra's values; and the stated translation `U = X−21, V = Y+11`, i.e. `(r,s,t) = (−21,0,11)`,
  maps it to `[1,1,1,−352,−2431]` exactly. Δ support `{2,3,19}` matches `N = 114 = 2·3·19`.
* `L(E,1)/Ω_R = 5/4` is **NOT CERTIFIED**, and Ultra says so itself. The database decimals give
  `1.250000000000000000000000000000657989756`, consistent with 5/4 to 30 places. Strong numerical
  support; not a certificate. No gp, sage or magma is installed here, so no modular-symbol
  computation was possible on this machine.
* The Cremona/LMFDB label is database-tier, authenticated by digest, not recomputed.

**Literature versions matter and Ultra's disclosure is load-bearing.** Banwait–Huang v1 and v3 are
genuinely different documents (641 KB vs 950 KB; 14 vs 24 numbered theorems), and the string
`Theorem 2.13` occurs **0 times in v1 and once in v3**. Ultra's independently frozen literature
pass retrieved v1, which does not contain the theorem its downstream full-BSD route now relies on.
Its handling — supersede the frozen pass with a separate post-freeze comparison rather than edit it
— is correct.

## 5. Certification boundary — UNCHANGED

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO
    PRIOR_ART_BLOCKER        = UNRESOLVED

Still certified, exactly as before this audit: `E_q(ℚ)/2E_q(ℚ) ≅ ℤ/2ℤ`, every rational point is
torsion, `Module.rank ℤ E_q(ℚ) = 0`.

Still **not** certified: finiteness of `E_q(ℚ)`; `E_q(ℚ)[2^∞] ≅ C₂`; genuine cohomological `Sel₂`;
genuine Ш or any of its torsion subgroups; continuous-H¹/Kummer/local–global comparison; central
nonvanishing; analytic rank; BSD(2) or full BSD; all-H41 analytic control; novelty of 66b1.

No Lean theorem was written, commissioned or released by this object. Ultra performed no fresh Lean
build; every Lean figure here was produced by me.
