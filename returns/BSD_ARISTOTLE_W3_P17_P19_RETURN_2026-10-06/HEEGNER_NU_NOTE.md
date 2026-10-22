# Heegner lane: what the target "ν_p ≤ 2" actually is

The seed is `E = [0,-22735,0,106272484,0]` with `N = 6503188012738584`. The field is `K = Q(√-23)`.

**Grades**
- **LEAN**: machine-checked, no `sorry`.
- **COMPUTED**: produced by a program in this project.
- **IMPORTED**: depends on a cited theorem or a retained input.

## 1. The Zhang-domain correction at p = 53 (checked against the curve)

Your correction holds up. The local data behind it were recomputed directly from the Weierstrass model (COMPUTED, `w3_p17/`):

| quantity | value |
|---|---|
| `Δ` | `2^8 · 3^2 · 2243 · 4547^3 · 5843^2` |
| `c4` | `2^4 · 43 · 1013 · 4547` |
| `N` | `2^3 · 3 · 2243 · 4547^2 · 5843` |
| Kronecker `(-23/q)`, `q = 2,3,2243,4547,5843` | `+1` for all five, so `N^- = 1`, `N^+ = N` |
| `a_3, a_2243, a_5843` | `-1, +1, -1` (multiplicative; `c4` is a unit there, so the model is minimal) |
| `ord_q Δ` at `3, 2243, 5843` | `2, 1, 2` |
| `a_53` | `-6` (good ordinary, and not anomalous) |
| Kolyvagin prime `ℓ = 3391` | `3391 ≡ -1 (mod 53)`; `a_3391 = 0`; `(-23/3391) = -1` (inert) |

**What follows from the table.**
- **Ramification.** `53` divides none of `ord_q Δ` at the three primes `q ∥ N`. So `ρ̄_53` is ramified at each of them.
- **The square-full primes 2 and 4547.** Here the reduction is additive and `53 ∤ ℓ`. The component group has order at most 4, `E_0/E_1 ≅ F_ℓ`, and `E_1` is pro-`ℓ`. Hence `E(Q_ℓ)[53] = 0`, so `H^0 = 0`, and `H^2 = 0` by local duality. Since `ℓ ≠ 53`, the local Euler characteristic is 0, so `H^1(Q_ℓ, E[53]) = 0`. This is the clause of Hypothesis ♥ for `ℓ^2 | N^+`.
- **Surjectivity.** `ρ̄_53` is surjective by Serre's criterion. The Frobenius witnesses are at `ℓ = 5, 17, 5`, each with nonzero trace (COMPUTED, `w3_p17/surjectivity_check.py`).
- **Not re-checked here.** I did not re-read the remaining clauses of Zhang's hypotheses.

## 2. ν_p is fixed by the two Selmer ranks (LEAN)

Write
- `r^+ = dim Sel_p(E/K)^+`, which equals `dim Sel_p(E/Q)`;
- `r^- = dim Sel_p(E/K)^-`, which equals `dim Sel_p(E^K/Q)`.

Take Zhang's Lemma 8.4 with `ε(E/Q) = +1`. Then `ε_ν = +` exactly when `ν` is odd, and the lemma becomes two hypotheses:
- `ν` odd: `r^+ = ν+1` and `r^- ≤ ν`;
- `ν` even: `r^- = ν+1` and `r^+ ≤ ν`.

Add `r^+ ≥ 2`, which comes from the two rational points. File `RequestProject/KolyvaginVanishingOrder.lean` then proves:

- `Heegner.nu_succ_eq_max`: `ν_p + 1 = max(r^+, r^-)`.
- `Heegner.one_le_nu`: `ν_p ≥ 1`.
- `Heegner.nu_le_two_iff`: `ν_p ≤ 2 ⟺ r^+ = 2 ∧ r^- ≤ 3`.
- `Heegner.nu_le_two_iff_of_rm_eq_one`: if `r^- = 1`, then `ν_p ≤ 2 ⟺ r^+ = 2`, and `ν_p ≤ 2` forces `ν_p = 1`.

None of these needs a parity hypothesis.

**Consequences.**

1. **Your sufficient criterion is right.** Some `n` with `ω(n) ≤ 2` and `c(n) ≠ 0` gives `Ш(E/Q)[p] = 0`. As a *certificate at one prime*, a nonzero two-prime class is legitimate and widens the search.

2. **As a cofinite target, it is not weaker.** `ν = 2` needs `dim Sel_p(E^K/Q) = 3`. Suppose `E^K` has rank 1 and finite Ш. Then `r^- = 1` for every `p ∤ #Ш(E^K/Q)`, so for all but finitely many `p`
   ```
   ν_p ≤ 2  ⟺  ν_p = 1  ⟺  Ш(E/Q)[p] = 0.
   ```
   A uniform proof of "`ν_p ≤ 2` for cofinitely many ordinary `p`" is therefore exactly FIN on the ordinary primes, and the two-prime branch is empty there. The first nonzero class must be a one-prime class `c(ℓ)`.

3. **A ν-bound is a Selmer bound.** `ν_p = max(r^+, r^-) − 1` holds as an identity once Zhang's lemma applies. So any mechanism that bounds `ν_p` uniformly *is* a uniform Selmer bound. The request for a mechanism forcing `ν_p ≤ 2` that "does not assume a Sha/Selmer bound" cannot be met by reorganising `ν`. The only non-circular inputs are:
   - explicit nonzero classes at individual primes (computation); or
   - a uniform indivisibility statement for `c(ℓ)` itself.

   By the stopping rule you set, this is a restatement result, so I stopped the ν-route here.

4. **The rank of `E^K = E^{(-23)}` matters.** Its root number is `w(E)·χ_{-23}(-N) = -1`. If its rank were 5 or more, `ν_p ≥ 4` for every `p`, and the `ν ≤ 2` target would be empty. §3 gives the numerical evidence on this.

## 3. Analytic rank of E^{(-23)} (COMPUTED, numerical)

I computed `L'(E^{(-23)}, 1)` with the same coefficient engine (`w3_p17/msl_sq.c` compiled with `-DKERNEL_E1`). The setup:
- buckets `n mod 23` with `χ(n) = (n/23)`;
- conductor `23^2 N = 3440186458738710936`;
- `T = 3·23·√N`.

The result (`w3_p17/TWIST23_RESULTS.json`):

```
L'(E^{(-23)}, 1) = 39.847278064 ...
```

**Functional-equation test.** With root number `−1`, the split-parameter formula `Σ a_n χ(n)/n [E_1(2πnt/X) + E_1(2πn/(tX))]` must give the same value for every `t`. At `t = 1.2` it gives `39.84727806413`, a discrepancy of `7·10^{-12}`. This checks the conductor, the root number and the twisted coefficients.

**Consequence (IMPORTED).** So `E^{(-23)}` has analytic rank exactly 1. By Gross–Zagier–Kolyvagin:
- `E^{(-23)}(ℚ)` has rank 1;
- `Ш(E^{(-23)}/ℚ)` is finite;
- `r^- = dim Sel_p(E^{(-23)}/ℚ) = 1` for every odd `p ∤ #Ш(E^{(-23)}/ℚ)`, which is all but finitely many `p`.

Combined with `Heegner.nu_le_two_iff_of_rm_eq_one`, this gives, for all but finitely many `p` at which Zhang's Lemma 8.4 applies:

```
ν_p ≤ 2  ⟺  ν_p = 1  ⟺  Ш(E/ℚ)[p] = 0.
```

**Caveat.** The value is floating point and is not interval-certified. Its size, about 40 against a discrepancy of `10^{-11}`, makes the nonvanishing numerically unambiguous, but it is not a certified proof.

## 4. What remains on this lane

- **`c(3391) mod 53`.** This needs Heegner points of conductor `3391` on a curve of conductor `6.5·10^15`, i.e. over a ring class field of degree `h(-23)·3392 = 10176`. That is far beyond what can be computed here, and no value is claimed.
- **Supersingular primes.** As you noted, Zhang's theorem is ordinary-only. Nothing here addresses supersingular `p`, which for this seed have `a_p = 0`.
