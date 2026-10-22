# H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010

Records the successor route after `ADDENDUM_009` withdrew the `ℓ=2` Vatsal application — and proves one
of its steps. **No research object launched, no Codex or Aristotle run, no finite-level computation.**
All prior objects byte-identical.

**`(D2)` is PROVED, uniformly in `p`.** With `F_p` the H41 eta quotient and `e = 3(p−1)/2`:

* Atkin–Lehner `W₂` shifts the exponent vector by `(−3(p−1), 3(p−1), −3(p−1), 3(p−1))`, every entry even;
* `G_p = (η(2z)η(2pz)/(η(z)η(pz)))^e` satisfies all four eta-quotient conditions on `Γ₀(2p)`
  — weight 0, both weighted sums `≡ 0 mod 24` (`v₂ = n ≥ 3`), character product `2^{2e}` a square;
* `div(F_p) + 2·div(G_p) = k·(0,1,−1,0)`, `k = (p²−1)/8`;
* the `W₂` **cusp** action is not assumed — permuting the divisor indices of matrix row 1 gives row 2 and
  of row 4 gives row 3, so `c₂ = W₂[0]`, `c₃ = W₂[∞]`, exactly what the divisor identity needs;
* hence `F_p|W₂ = c·F_p·G_p²`, and **`d log` kills `c`**, giving `W₂^*(ω̄_η) = ω̄_η` with no need to
  determine the constant. The loose end in the proposal was not one.

**`(D1)`: arithmetic core confirmed.** `v₂((p²−1)/8) = n−2 = m ≥ 3`, so `2 | M` and indeed `8 | M`,
uniformly; `e` is odd. The local geometry on the minimal regular semistable model (horizontal cusp, vertical
component, node `xy=2`) is **not** verified here and stays a proposed lemma.

**`(D)` is UNVERIFIED and task 4 is not executable from frozen material.** `[Vat99]` is identified from
Vatsal's own bibliography as *Canonical periods and congruence formulae*, Duke Math. J. 98 (1999) — and
that paper is **not in the corpus**; no Agashe–Ribet–Stein text is either. The only Agashe source here is
the 2018 solo JTNB paper, which contains "Wiles", "multiplicity one", "Lemma 5.17" and "Proposition 5.10"
zero times each. So `(D)`, Lemma 5.17, Prop 5.10 and the `2 ‖ N` special-fibre description are recorded as
handed in and unverified. The route's two ends — `(D)` at the start, `(E)` at the finish — each rest on one
unread paper.

**`(D3)` would not give `(C)`** — the operator's own caveat, endorsed: in characteristic 2 two classes can
share a differential realisation and differ in the étale part. `(X)` and `(C)` stand as in `ADDENDUM_009`.

    ADDENDUM.md      the six sections
    computation/     verify_W2_eta.py (symbolic in p), audit_source_presence.sh
    receipts/        W2_ETA_VERIFICATION, SOURCE_PRESENCE

**The H41 seed remains unproved.**
