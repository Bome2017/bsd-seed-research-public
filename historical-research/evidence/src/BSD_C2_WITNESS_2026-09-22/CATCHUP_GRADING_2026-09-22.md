# Catch-up grading — four returns plus one external audit

Date 2026-09-22, evening. Covers the two twist-Sha bias-control returns (15:55) and the two `c_2` returns
(19:14, 19:52), together with the external audit of the second `c_2` return. Archives are copied into
`~/BSD_TWIST_SHA_SUPPORT_2026-09-22/returned/` and `~/BSD_C2_WITNESS_2026-09-22/returned/`.

    AWARE  21db96b2c9e142d19fb2e5a56c1d905b084939263a1368ec25edae0491a8b18d
    BLIND  fd7d45c4b99b009715d686171225e9b02ca35be44a6625a6e3650531b0eaa6d7
    c2 run1 71c6285221a8f5dfacaf5dad6d2c258156204125555071d1947787e0cb056253
    c2 run2 86b65a0b1cca07c2b153fcdee887335abc96be8d4bdfa80ad0756ef6823fa707

---

## A. The twist-Sha bias-control pair — now off the critical path, but informative

**The experiment was compromised, by my packaging error.** I built the blind variant by copying the aware folder, and
its root-level `STATE.json` still carried `"omega_1"` and `"sha_predicted": 49`. My leak check scanned only
`READ_FIRST/`. The blind run **disclosed this itself**, which is the honesty clause K1b was written for: it saw the
prediction before freezing, and it lists which Stage I conclusions don't depend on it (the curve arithmetic, the
residual-image theorem, the hypothesis audit). Both arms saw the prediction, so the pair **cannot measure anchoring
as designed**. Lesson: a leak check must scan every file the package ships, including metadata.

| | AWARE | BLIND |
|---|---|---|
| Stage I.A | `TWIST_SHA_COFINITE_ONLY` | `FIRST_MISSING_THEOREM` (the additive-prime `p`-part bound; bites at 7) |
| Stage I.B | `EIGENSPACE_REFINEMENT_OBSTRUCTED` | `EIGENSPACE_REFINEMENT_UNKNOWN` |
| Stage II | `PRIOR_BOUND_CONFIRMED` | `PRIOR_BOUND_CONFIRMED` |
| changed Stage I after Stage II | no | no |
| unresolved `p >= 5`, even granting an exact `L`-value | `{7, 4547, 5843}` | `{7, 4547, 5843}` |

**What both confirm independently:**
* **The rational-reconstruction gap.** AWARE proved in Lean that for **every** prime `p`, the certified interval
  contains a rational with a 2-power denominator whose numerator is divisible by `p`. So the interval, together with
  every integrality statement available here, excludes nothing at any prime; the "nearest integer" step is rounding,
  not a theorem. This is the Manin-constant / denominator gap, found **independently of** `MANIN_GATE.md`.
* **Stage II holds:** both prior bounds are correct, and the "equivalently `A_2 = 0`" demotion is upheld. AWARE gives a
  Lean counterexample to the converse (a symmetric 2×2 matrix, every entry with denominator 5, determinant 1). BLIND
  gives two separate failures of equivalence.
* **The Cassels–Tate shortcut is unaffected.** BLIND: run B's bound is "correct for this curve, but not a valid
  general lemma". In general it needs an extra `v_p(exp E^{-7}(Q)_tors[p^∞])` term, and that term is 0 for `p >= 5`
  because the torsion is `Z/2` (checked twice in Lean). So the shortcut's `v_p #Sha(E/K)[p^∞] <= 2c` stands.

**Where they disagree with the record — `5843`.** Both call `5843` split multiplicative with a trivial zero that
"kills the naive rank-0 bound" (BLIND machine-checked `a_5843 = +1`). Together with the two ordinary-bridge audits,
that makes **four** Aristotle runs taking this position. On the other side is **only the Sage docstring** for
`bound_kato`, whose stated theorem excludes additive reduction and nothing else. That docstring summarizes Kato and
Grigorov's thesis; it is a secondary characterization, and relying on it is the same mistake as trusting ARS's
summary of Edi89. `SAGE_KATO_CHECK.md`'s `5843_IS_AN_OBSTRUCTION = FALSE [BOTH ARISTOTLES WRONG]` is therefore
**downgraded to DISPUTED**. At a split multiplicative prime the rank-0 bound requires the Greenberg–Stevens
exceptional-zero correction (the `L`-invariant), and whether Sage's statement accounts for it has not been checked
against a primary source. **Off the critical path either way:** `5843 | N`, so it lies outside the BLV lane, and the
Cassels–Tate shortcut does not need the twist's Sha support.

**Two smaller corrections to my record:**
* **The period convention** (AWARE). I selected `Ω = 2ω₁` using a squareness argument (49 is a square, 98 is not).
  That argument is BSD-circular. The value is correct for geometric reasons (`Δ > 0` gives two real components, so
  `Ω = 2ω₁`), which Sage's `L_ratio` source also encodes. Accepted: the squareness argument is withdrawn as a
  justification, and the geometric one replaces it.
* **Mazur torsion** (BLIND). I wrote that the only primes that can divide a torsion order over `Q` are `2, 3, 5`.
  That is wrong: `Z/7` occurs, so the list is `2, 3, 5, 7`. It is harmless here, since the torsion is exactly `Z/2`.

## B. The c_2 runs — the witness is open at every prime; close this bounded attempt

**Run 1 (c508db76) — `FIRST_MISSING_THEOREM`, quantifier level 0.**
The missing theorem is **exactness of the order**: `ord_T(calL mod p) = 2`, i.e. `μ = 0` and `λ(calL) = 2`,
equivalently `λ(L_p) = 4`. The lower order is unconditional. `μ = 0` is the subject of the existing literature.
**Nothing known supplies `λ <= 2`.** For `r = 2` that bound is exactly `c_2(p) ∈ Z_p^×`. Checked in Lean, with no
`sorry` and no added axioms:
* the reduction formula, derived from BLV's layer-one element rather than assumed;
* vanishing of the first moment, so that `c_2(p)` is a unit iff `Σ_j j²·ψ̄(γ^j P_1) != 0` in `F_p`;
* independence of the choice of generator;
* the Iwasawa form: `c_2` unit ⟺ `calL mod p` has order exactly 2;
* the `T^4` example for the converse gap;
* **the sharp form: `c̄_2(p) = −c_{p−3}`, where `v(x) = Σ c_i x^i` is the Lagrange interpolating polynomial of the
  conductor-`p²` packet on `F_p`.** The witness is one designated high-degree coefficient of the packet.

*Flag:* the run's remark that equidistribution input "cannot close it" is a **heuristic explanation, not a theorem**
(K5). The underlying point stands: over `F_p` the group `Z/p` has no nontrivial characters, so character-sum and
equidistribution methods, which run over `C` or at `ℓ != p`, do not apply directly. That is the diagonal `ℓ = p`
obstruction, a known limitation of those methods rather than a proof of impossibility.

**Run 2 (7f61b6c8) — a bounded derivation on `D_p = Σ_j j² γ^j Q_1`.** The external audit's corrections are all
**confirmed at source** (BLV arXiv 2306.17784v2 §2.5, §4.2):

| run 2 claimed | correct | source |
|---|---|---|
| `Tr_{K_1/K} P_1 = T_p P_0 − c_p P_{-1}`, with `c_p = 2` split and `0` inert | `Tr_{K_{n+1}/K_n} P_{n+1} = T_p P_n − P_{n−1}` for **every** `n >= 0`; the coefficient is **−1 uniformly** | BLV (2.5) |
| the split/inert `2` / `0` | belongs to the **separate** formula `u_K P_0 = T_p P_K` (inert) / `T_p P_K − 2P_K` (split) | BLV (2.4) |
| `ψ̄(Q_0)`, `ψ̄(Q_{-1})` are remaining open inputs | both are **zero**: `calL ∈ I²` gives `calL(1) = 0`; Lemma 4.2 gives `calL_g(1) = ψ_g(P_K)` up to a unit, so `ψ(P_K) = 0`; then (2.3) `P_{-1} = u_p P_K` and (2.4) give `ψ(P_{-1}) = ψ(P_0) = 0`. The corrected trace equation just says `M_0 = 0`. | BLV (2.3), (2.4), Lemma 4.2 |
| "`ι`-evenness is a necessary condition for the witness" | **unsupported.** Even ⟹ first moment 0 and odd ⟹ second moment 0 are both proved, but the packet need not be purely even or purely odd. `calL` is defined only up to a group element, which preserves the quadratic coefficient (the lower ones vanish) but can break exact `ι`-symmetry: `F = T²/(1+T)` is `ι`-invariant, `(1+T)F = T²` is not, and both have quadratic coefficient 1 | checked by hand |

Also checked here, by computation for `p = 5..37`: `N = t^{p−1}` and `W_2 = Σ j²γ^j = t^{p−3}(1+t)(2+t)` hold in
`F_p[t]/(t^p)`. The countermodel `v(x) = 2c·x^{p−3}` gives `M_0 = M_1 = 0` and `c̄_2 = c` for every `c` (checked for
`p = 7, 11, 13`).

**What survives, and is retained:** the group-algebra identities; the fact that the relation module is
one-dimensional (`λ·(N Q_1) = ε(λ)·N Q_1`); and the narrow result that **the trace relation, even with evenness
added, does not determine the second moment.** The countermodel is about abstract packets that satisfy the chosen
constraints. It is not a realization theorem for actual Gross-point values and does not show that the Hecke relations
are exhausted. **The unresolved `ι`-sign is not a research task.**

**Disposition: close this bounded attempt. No further run is needed to repair it.** No prime is settled, the forward
bridge is untouched, and direct evaluation remains unavailable.

## C. The frontier after catch-up — unchanged in substance, sharper in statement

    ORDINARY LANE:  for p >= 5, p ∤ 7N, E ordinary at p:   c_2(p) ∈ Z_p^x  ==>  Sha(E/Q)[p^inf] = 0
                    forward bridge intact (externally source-audited; not Lean-verified)
    c_2(p)       :  OPEN at every prime.  Missing theorem: lambda(calL mod p) = 2, equivalently the
                    degree-(p-3) Lagrange coefficient of the conductor-p^2 packet is nonzero mod p.
    NEXT         :  A3 supersingular, as a separate package (per the agreed sequence).
    OFF PATH     :  twist-Sha support; Manin/modular degree; 5843 exceptional zero (now DISPUTED, not resolved)
    OPEN, LOCAL  :  bad primes 2243, 4547, 5843;  I_3(13) = OPEN_TWIST_13_PRIMARY_INPUT
