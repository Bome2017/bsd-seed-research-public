# ARISTOTLE_A — return

## Verdict

    ARISTOTLE_NO_SURVIVOR

No construction I generated survives its own gate. Below: the mandatory five-line cards, the
new results that *were* proved (with their scope and an honest novelty grading), the exact first
unproved arrow of the only candidate with the right shape, and the corrections to the packet's
admission rules that I adopted after review.

**Nothing here proves, or brings measurably closer, finiteness of `Ш(E/Q)` or order nine.**
Two of the items below are no-go results that close listed-open directions; the rest are
clarifications that remove false leads. None of it is a BSD arrow.

---

## 0. Corrected terminology and rules in force

I adopt the review's corrections, which override the packet where they conflict.

| term | meaning used here |
|---|---|
| `FIN` | `Ш(E/Q)` is finite (the canonical master's definition) |
| `ORDER9` | `#Ш(E/Q) = 9` |
| `Q36` | `q = L''(E,1)/(2 Ω_E Reg(E)) = 36` |

`BSD(E) ⟺ ORDER9 ∧ Q36`. `FIN` alone is strictly weaker than `ORDER9` and would still be real
progress. My target was `ORDER9`, secondarily `FIN`.

Gate rules used (corrected):

1. **Map gate.** A map is admissible if it comes with the property the bound needs: a
   bounded-source **surjection** `M_p ↠ Sel_p(E)` or `M_p ↠ Ш[p]`, a bounded-target
   **injection** `Ш[p] ↪ T_p`, or a proved cokernel/annihilator theorem. A map with none of
   these is inadmissible regardless of orientation. (The packet's blanket ban on
   `M_p → Sel_p(E)` is wrong: `M_p ↠ Sel_p(E)` with `dim M_p ≤ 2` would close the tail.)
2. **Equivalence gate.** A mere change of formulation without new proved information is
   rejected. An *independent proof* of an equivalent assertion is accepted — it would solve the
   problem. So I do not discard a candidate merely for being equivalent to `ORDER9`; I discard
   it if it has no independent proof route.
3. **Integrality gate.** Rejected: passage from a rational corank/dimension to a finite order.
   Accepted: characteristic-zero constructions that retain a controlled integral lattice,
   index, valuation or congruence ideal. (The retained 7-primary proof is of exactly this kind.)
4. No assumption of `FIN`, BSD, the desired Selmer bound, or an unproved exhaustive exceptional
   set.

Two packet statements I found to be **incorrect** and did not use:

* **Target (B) as written does not give `ORDER9`.** Confirmed and machine-checked; see §3.1.
* **Target (A) is not a weaker target.** `#Ш[n] < 1089` for all `n` is *equivalent* to `ORDER9`
  under the retained inputs. Machine-checked; see §3.2. It remains a legitimate goal (rule 2),
  but it may not be advertised as strictly easier, and the same holds for the `441` form.

---

## 1. Required declaration (made before any proof was attempted)

Starting from

    0 → E(Q)/nE(Q) → Sel_n(E) → Ш[n] → 0,

the known term `E(Q)/nE(Q)` has order `n²` for odd `n`. Note the structural consequence that
governed the whole search:

> `Sel_n(E)` contains `(Z/n)²` and is therefore **never** bounded independently of `n`.
> Any admissible construction must see the **quotient**, i.e. produce a bounded-source surjection
> onto `Ш[n]` (or its dual), or a bounded-target injection out of it, or bound
> `dim_{F_p} Sel_p(E)` by an absolute constant — a bound on the *dimension*, never on the order.

Candidate cards are in §2. Each is five lines; a card that cannot be completed was killed at once.

---

## 2. Candidate cards

### C1 — Quantitative Poitou–Tate / Greenberg–Wiles

1. **Object.** The global Euler-characteristic formula for `M = E[n]` with the Kummer local
   conditions `L_v = im(E(Q_v)/nE(Q_v) → H¹(Q_v, E[n]))`.
2. **Map involving `Ш[n]`.** None — the formula is a ratio `#Sel_L / #Sel_{L^⊥}`.
3. **Direction.** Not applicable.
4. **Independently bounded target.** None.
5. **Previously failed arrow changed.** None.

**Killed, with a proof.** See Theorem A (§3.3): the formula is *identically* the product formula
for `n` and therefore carries no information whatever about `#Sel_n(E)`.

### C2 — Modified local conditions (Σ-strict / Σ-relaxed) plus duality

1. **Object.** `Sel^{Σ-str}_n` and `Sel^{Σ-rel}_n` for a finite set `Σ`, with the local index
   `∏_{v∈Σ} [L_v : L'_v]`.
2. **Map.** `0 → Sel^{Σ-str}_n → Sel_n → ⊕_{v∈Σ} L_v`, giving
   `#Sel_n ≤ #Sel^{Σ-str}_n · ∏_{v∈Σ} #L_v` — the correct direction.
3. **Direction.** Upper bound on `Sel_n`, hence on `Ш[n]` after dividing by `n²`.
4. **Independently bounded target.** **Absent.** By Greenberg–Wiles with self-duality,
   `#Sel_{L'} = #Sel_{(L')^⊥} · ∏_v (#L'_v/#L_v)`. Every upper bound the calculus produces has
   another Selmer group of the *same* module on its right-hand side. Since `(L'^⊥)^⊥ = L'`, the
   calculus is a closed system with no terminal object.
5. **Changed arrow.** None. Making the localisation `Sel_n → ⊕_{v∈Σ} L_v` near-surjective is
   exactly the construction of global classes with prescribed localisations — an Euler system.

**Killed.** Reduces to Euler systems, where the seed's primitive analytic rank 2 kills Kato's
`κ₁`. Additionally, choosing `Σ` so that `loc_Σ` is injective on `⟨δ(P₁), δ(P₂)⟩` is the
already-archived localisation-determinant route (control of the known 2-plane).

### C3 — Artin–Verdier: `Ш` as a single étale `H¹` over `Spec Z`

1. **Object.** The Néron model `𝓔/Spec Z`; `Ш(E/Q)` is (up to bad-fibre corrections)
   `H¹_ét(Spec Z, 𝓔)`, with Artin–Verdier duality inducing the Cassels–Tate pairing.
2. **Map.** Equality (up to the correction terms) — the most "finite-looking" incarnation of `Ш`.
3. **Direction.** Equality.
4. **Independently bounded target.** **Absent.** The available finiteness theorem is for
   *finite* étale sheaves: it gives `H¹(Spec Z, 𝓔[n])` finite, hence `Sel_n` finite, hence
   `Ш[n]` finite — for each `n` separately. The orders `#𝓔[n] = n²` are unbounded, so nothing
   uniform follows.
5. **Changed arrow.** None.

**Killed.** Reproduces exactly "`Ш[n]` is finite for each `n`", which is already known. There is
no finiteness theorem for `H^i(Spec Z, F)` with `F` a smooth group scheme that is neither finite
nor torsion-free.

### C4 — Cassels' isogeny invariance via the seed's rational 2-isogeny

1. **Object.** `φ : E → E'` of degree 2 (`E` has the rational point `T = (0,0)`), with
   `E' : y² = x³ + 2·22735 x² + 9·2243·4547 x`.
2. **Map.** Cassels' theorem relates `#Ш(E)` and `#Ш(E')` by an explicit product of local
   factors; for odd `p`, `Ш(E)[p^∞] ≅ Ш(E')[p^∞]`.
3. **Direction.** Isomorphism.
4. **Independently bounded target.** **Absent** — `Ш(E')` is exactly as unknown as `Ш(E)`.
5. **Changed arrow.** None.

**Killed.** Transports the problem; the ratio is a power of 2 and the 2-part is already settled.
(I checked that `E'` also has torsion `Z/2` only: `45470² − 4·91790289 = 1700359744` is not a
square.)

### C5 — Descent over the field of `p`-division points

1. **Object.** `K = Q(E[p])`; `Sel_p(E/Q) ↪ Sel_p(E/K)^{Gal(K/Q)} ⊆ Hom(G_{K,S}, (Z/p)²)`.
2. **Map.** Injection of `Sel_p(E/Q)`, hence a bound on `Ш[p]`.
3. **Direction.** Bounded-target injection — correct shape.
4. **Independently bounded target.** **Absent.** The target is controlled by the `p`-rank of the
   `S`-class group and the `S`-unit group of `K`, and `[K:Q] ~ p⁴`, so the bound grows like `p⁴`.
5. **Changed arrow.** None.

**Killed.** This is the standard weak-Mordell–Weil bound; it is genuinely an upper bound, and
genuinely useless, because it is unbounded in `p`.

### C6 — Iwasawa / control theorem (the only candidate with the right shape)

1. **Object.** `X_∞ = Sel_{p^∞}(E/Q_∞)^∨` and `M_p := X_∞/(γ−1)X_∞`.
2. **Map.** Mazur's control theorem gives `Sel_{p^∞}(E/Q) → Sel_{p^∞}(E/Q_∞)^Γ` with finite
   kernel and cokernel; dualising, `M_p ↠ Sel_{p^∞}(E/Q)^∨` up to bounded error, and
   `Ш[p^∞]^∨` is a quotient of `Sel_{p^∞}(E/Q)^∨`. So **`M_p ↠ Ш[p^∞]^∨`**.
3. **Direction.** Bounded-source surjection onto the dual of the target. **Admissible.**
4. **Independently bounded target.** Kato's divisibility `char(X_∞) | (L_p)` bounds
   `#(X_∞/(γ−1))` by the `p`-adic valuation of the leading Taylor coefficient of `L_p`, with the
   `p`-adic regulator and Tamagawa factors removed. This retains integral structure, so it
   survives the integrality gate. This is exactly how `p = 5` and `p = 7` were closed.
5. **Changed arrow.** **Nothing has changed.** The mechanism is the one already in use; the
   obstruction is uniformity in `p`, not the shape of the map.

**Not killed at the level of shape; killed at the level of uniformity.** Its exact first unproved
arrow is §4.

---

## 3. What was actually proved

Novelty grading is deliberately conservative. Items marked *standard, made precise* are not new
mathematics; they are standard facts stated sharply enough to close a direction the packet had
listed as open, and machine-checked where feasible.

### 3.1 Target (B) is insufficient — confirmed and machine-checked

*File:* `RequestProject/TargetBCountermodel.lean`, theorem
`SeedBSD.TargetB.target_B_does_not_give_order_nine`.

`G = (Z/3)² ⊕ (Z/11)²` with `C_E = 33` satisfies, all machine-checked:

* `C_E ≠ 0` and `G[p] = 0` for every prime `p ∤ C_E` (so `G[p] ≠ 0 ⇒ p | C_E`);
* exponent `33`, so complete depth control (depth 1) at every divisor of `C_E`;
* `G[2^∞] = G[5^∞] = G[7^∞] = 0` and `#G[3^∞] = 9` — all four retained primary inputs;
* a nondegenerate alternating pairing on each primary part;

and yet `#G = 1089 ≠ 9`. Target (B) therefore earns `FIN`, never `ORDER9`.

*Grade:* the countermodel is the review's; the machine-checked verification is mine.

### 3.2 Target (A) is equivalent to `ORDER9`, not weaker

*File:* `RequestProject/Assembly.lean`, theorems `bounded_torsion_implies_finite` and
`level_bound_of_card_lt`.

> **Theorem.** Let `A` be a torsion abelian group with every `A[n]` finite and `#A[n] < K` for
> all `n ≥ 1`. Then `A` is finite and `#A < K`.

*Proof (formalised).* Let `s ⊆ A` be finite and `n = ∏_{a∈s} ord(a) ≥ 1`. Then `s ⊆ A[n]`, so
`#s < K`. A type all of whose finite subsets have fewer than `K` elements is finite of
cardinality `< K`. ∎

With `K = 1089` and the square-order step this gives `ORDER9`; conversely `#A = 9` gives
`#A[n] ≤ 9 < 1089`. So (A) is a reformulation. Under rule 2 it is still a legitimate goal, but
the packet's claim that the `1089` form is *strictly easier* than the `441` form is not
established by the larger constant alone — both are equivalent to `ORDER9` here.

*Grade:* standard, made precise; the argument is the review's, the formalisation is mine.

### 3.3 Theorem A — the global-duality Euler characteristic for `E[n]` is the product formula

> **Theorem A.** Let `E/Q`, `n ≥ 1`, `M = E[n]`, and let `L_v ⊆ H¹(Q_v, M)` be the local Kummer
> conditions. Then the Greenberg–Wiles formula
>
>     #Sel_L(Q, M) / #Sel_{L^⊥}(Q, M^∨)
>       = (#H⁰(Q,M)/#H⁰(Q,M^∨)) · ∏_v (#L_v / #H⁰(Q_v, M))
>
> reduces to the identity `1 = 1`. Concretely: its left side is `1`, and its right side is
> `∏_v |n|_v⁻¹ = 1`. The formula is *equivalent to the product formula for `n`* and yields no
> bound on `#Sel_n(E)`, a fortiori none on `#Ш[n]`.

*Proof.* (i) The Weil pairing gives `M ≅ M^∨ = Hom(M, μ_n)`, so the `H⁰` prefactor is `1`.
(ii) By local Tate duality the Kummer image `L_v` is its own annihilator, so `L_v^⊥ = L_v` and
`Sel_{L^⊥}(M^∨) = Sel_L(M)`; the left side is `1`. (iii) For every place,
`#L_v = #(E(Q_v)/nE(Q_v)) = #E(Q_v)[n]·|n|_v⁻¹ = #H⁰(Q_v,M)·|n|_v⁻¹`: at finite `v` this is the
structure `E(Q_v) ≅ Z_ℓ^{d} × (finite)`; at `v = ∞` with `n` odd, `H¹(R,M) = 0`, `L_∞ = 0`-index
`1/n`, and `|n|_∞⁻¹ = 1/n`. (iv) Hence the right side is `∏_v |n|_v⁻¹`, which is `1` by the
product formula. ∎

*Machine-checked core:* `RequestProject/DualityTautology.lean`,
`SeedBSD.greenberg_wiles_rhs_eq_one` and `SeedBSD.local_index_product_one` — the numerical
bookkeeping `(1/n)·∏_{p|n} p^{v_p(n)} = 1` with the local index hypothesis. The three arithmetic
inputs (Weil self-duality, maximal isotropy of the Kummer image, the local index formula) are
classical and are cited, not reproved.

*Grade:* **standard, made precise.** Experts know the Greenberg–Wiles ratio is trivial for a
self-dual module with maximal isotropic conditions. What is new is only its use as a *closure*:
it kills, with a proof, the packet's first listed-open direction ("a global duality /
Poitou–Tate argument producing a uniform numerical bound").

### 3.4 Theorem A′ — maximal isotropy is exhausted by `dim ≤ ½ dim V`, and that is sharp

*File:* `RequestProject/IsotropicSharpness.lean`, theorem `SeedBSD.duality_bound_is_sharp`.

In the Poonen–Rains picture, `Sel_n(E) = X ∩ L` inside `V = ⊕'_v H¹(Q_v, E[n])` with its perfect
alternating local-duality pairing, where `X = im H¹(Q, E[n])` and `L = ∏_v L_v` are both maximal
isotropic. Global duality asserts *exactly* those two maximal-isotropy statements.

> **Theorem A′ (machine-checked).** For every field `F` and all `d ≤ n` there exist, in the
> `2n`-dimensional symplectic space `V = F^n × F^n` with
> `ω(x,y) = ∑_i (x₁ᵢ y₂ᵢ − x₂ᵢ y₁ᵢ)`, two isotropic subspaces `X, L` of dimension `n` (hence
> maximal isotropic, `ω` being nondegenerate — also checked) with `dim(X ∩ L) = d` exactly.

Hence maximal isotropy constrains `dim Sel_n(E)` by nothing beyond `0 ≤ dim Sel_n ≤ ½ dim V`, and
`½ dim V` grows with the level and with the ramification set. **No quantitative bound on `Ш[n]`
is extractable from duality alone.** This is the structural reason C1 and C2 fail, and it is why
an Euler system or a main-conjecture input is logically necessary and not merely customary.

*Grade:* **standard, made precise** (the linear algebra is elementary; the closure is the point).

### 3.5 The seed's "uninterpreted datum" and "unusual conductor pattern" are family identities

*Files:* `RequestProject/Family.lean`, `RequestProject/SeedData.lean`.

Reparametrising the review's family `y² = x(x² − 5tx + 4t(t+9))`, `P₁ = (t,6t)`,
`P₂ = (36, 12(t−18))` by `x ↦ s²x`, `y ↦ s³y` with `A = ts²`, everything becomes integral:

    B := A − 16s²,  C := A + 9s²,
    𝓔(A,s) : y² = x(x² − 5A x + 4AC),
    Q₁ = (A, 6As),   Q₂ = (36s², 12(A − 18s²)s).

The seed is exactly **`A = 4547`, `s = 12`**, whence `B = 2243`, `C = 5843`, and I verified
`a₂ = −5A = −22735`, `a₄ = 4AC = 106272484`, `Q₁ = (4547, 327384)`, `Q₂ = (5184, 281520)`.

Machine-checked identities, valid for **all** `A, s`:

| identity | consequence |
|---|---|
| `5·x(Q₁) = −a₂` | `x(P₁) = 4547` is how the family is parametrised, not a seed property |
| `A ∣ a₂`, `A ∣ a₄` | `Q₁` always reduces to the cusp at any prime dividing `A` |
| `a₂² − 4a₄ = 9AB` | — |
| `Δ = 2⁸·3²·A³·B·C²` | the pattern `2³·3·(…)·(…)²·(…)` and the exponents `(3,1,2)` are generic |
| `Q₁, Q₂ ∈ 𝓔(A,s)` | both generators are generic family points |

So `N = 2³·3·2243·4547²·5843` is the family's universal shape with `(A,B,C) = (4547,2243,5843)`;
the three large primes are `A`, `A − 16s²`, `A + 9s²`. **There is no seed-specific content to
exploit**, and the packet's suggestion to treat the conductor pattern as a distinguishing feature
should be withdrawn.

*Grade:* the family is the review's; the integral reparametrisation, the identity
`5x(Q₁) = −a₂`, the discriminant identity and the machine-checking are mine.

### 3.6 The local structure at 4547, and why it cannot see `Ш[p]`

*File:* `RequestProject/SeedData.lean` (all valuations machine-checked).

Exact integral data, verified: `c₄ = 2⁴·43·1013·4547`, `c₆ = 2⁶·5·4547²·8501`,
`Δ = 2⁸·3²·2243·4547³·5843²`. Hence at `4547`: `v(c₄) = 1`, `v(c₆) = 2`, `v(Δ) = 3`, and the
model is minimal (`v(c₄) < 4`). By Tate's algorithm this is **Kodaira type III**, `f = 2`
(matching `4547² ‖ N`), Tamagawa number `c_{4547} = 2`, component group `Φ_{4547} ≅ Z/2`.
The reduced curve is the cuspidal cubic `y² = x³` (`4547 | a₂`, `4547 | a₄`).

Since `v_{4547}(x(P₁)) = 1 > 0`, `P₁` reduces to the singular point, so `P₁ ∉ E₀(Q_{4547})` and
its class generates `Φ_{4547}`; likewise `T = (0,0)`; whereas `4547 ∤ x(P₂) = 5184`, so
`P₂ ∈ E₀(Q_{4547})`. The specialisation `E(Q) → Φ_{4547} ≅ Z/2` is thus
`aT + bP₁ + cP₂ ↦ a + b mod 2`.

At the remaining bad primes: `v(c₄) = 0` at `3, 2243, 5843` with `v(Δ) = 2, 1, 2`, i.e. types
`I₂, I₁, I₂`; at `2`, `v(c₄) = 4`, `v(Δ) = 8`, and Ogg's formula with `f₂ = 3` gives `6`
components, i.e. type `I₁*`.

> **Orthogonality.** For every prime `p ∉ {2, 4547}` the local Kummer condition at `4547` is the
> **zero** subgroup, independently of the component group and of `x(P₁)`.

*Proof.* `E(Q_v) ⊇ E₀(Q_v) ⊇ E₁(Q_v)` with `E(Q_v)/E₀ ≅ Z/2`, `E₀/E₁ ≅ Ẽ_ns(F_v) ≅ (F_{4547},+)`
of order `4547` (additive reduction), and `E₁ ≅ (Z_{4547},+)`. For `p ∉ {2,4547}` each graded
piece has trivial `p`-torsion, so `E(Q_v)[p] = 0`; and for `v ∤ p`,
`#(E(Q_v)/pE(Q_v)) = #E(Q_v)[p] = 1`. ∎

So the entire arithmetic content of the datum `x(P₁) = 4547` is the Tamagawa number
`c_{4547} = 2` and a 2-torsion component class — inputs to `Q36`, invisible to `Sel_p` for every
odd `p ≠ 4547`. **The lead is closed.**

*Grade:* routine Tate-algorithm bookkeeping plus a standard local dévissage; new only to the
record. Settles the packet's explicit request to derive an exact consequence before spending on
the datum.

### 3.7 The minimal sufficient condition for `ORDER9`

*File:* `RequestProject/Assembly.lean`, theorem `card_eq_nine_of_prime_torsion_free`.

> **Theorem (machine-checked).** Let `A` be a torsion abelian group with `A[p] = 0` for every
> prime `p ≠ 3`, and `#A[3^∞] = 9`. Then `#A = 9`.

Supporting lemma `three_primary_of_no_other_prime_torsion`: if `A` is torsion and `A[p] = 0` for
all `p ≠ q`, every element has `q`-power order. So the divisible-part worry is void at the level
of primes — a nonzero `p`-primary group always contains an element of order exactly `p`.

Consequence: given the retained inputs, **`ORDER9` follows from "`Ш[p] = 0` for every prime
`p ≥ 11`" alone** — no Cassels–Tate square order, no `1089` threshold, no quantification over
all levels `n`. This is strictly the cleanest of the three sufficient forms, and it is the one a
tail argument should target.

*Grade:* elementary; the value is that it removes apparatus the packet treated as necessary.

---

## 4. Exact first unproved arrow (candidate C6)

Fix the seed. Let `p ≥ 11` be a prime of good ordinary reduction with `ρ_{E,p}` surjective, let
`L_p ∈ Λ = Z_p[[T]]` be the cyclotomic `p`-adic `L`-function and `X_∞ = Sel_{p^∞}(E/Q_∞)^∨`.
Kato gives `char(X_∞) | (L_p)`, hence `λ(X_∞) ≤ λ(L_p)` and `μ(X_∞) ≤ μ(L_p)`. Rank 2 forces
`ord_{T=0} L_p ≥ 2` and `λ(X_∞) ≥ 2`. Mazur's control theorem then yields the bounded-source
surjection `M_p = X_∞/(γ−1)X_∞ ↠ Ш[p^∞]^∨` up to explicitly bounded local error, and

    Ш(E/Q)[p^∞] = 0   provided   λ(L_p) = 2, μ(L_p) = 0, and the leading coefficient is a
    p-adic unit after dividing by the p-adic regulator Reg_p(P₁,P₂) and ∏_{v|N} c_v.

This is precisely the argument that closed `p = 5` and `p = 7`, one prime at a time. The uniform
statement required for the tail is:

> **(★)** For all but finitely many good ordinary primes `p`, `λ(L_p) = 2` and `μ(L_p) = 0`;
> equivalently, the second Taylor coefficient of `L_p` at `T = 0` is a `p`-adic unit.
>
> **(★★)** The analogous statement for Pollack's `L_p^±` at the (infinitely many, by Elkies)
> supersingular primes.

**(★) is unproved, and I did not prove it.** Two honest remarks on its status, neither of which
is a no-go theorem:

* `μ(L_p) = 0` for residually irreducible `ρ_p` is the better-understood half and is plausibly
  available from the surjectivity of the mod-`p` modular-symbol map; I did not verify this for
  the seed.
* `λ(L_p) = 2` is the hard half, and there is a **circularity risk that must be checked before
  anyone invests in it**: the seed has `3 ‖ N`, `2243 ‖ N`, `5843 ‖ N`, so Skinner–Urban's
  ramification hypothesis is *prima facie* satisfiable, and if the main conjecture holds as an
  equality at such `p`, then `char(X_∞) = (L_p)` and `λ(L_p) = 2` becomes **equivalent** to
  `Ш[p^∞] = 0` together with `p ∤ Reg_p · ∏ c_v`. Under rule 2 an equivalence is not
  automatically fatal — but it means (★) is not an independently accessible target, and a route
  to it must not pass through the `p`-part of BSD.

  *I did not verify that Skinner–Urban's hypotheses hold for this seed.* That verification is the
  first thing a successor should do, because it decides whether (★) is a genuine target or a
  restatement.

This is the honest terminus: **no theorem obtained; exact unresolved step recorded.**

---

## 5. New obstructions (the `NO_SURVIVOR` payload)

1. **Duality is closed and cannot bound.** (Theorems A, A′.) The Greenberg–Wiles formula for
   `(E[n], Kummer)` is the product formula; the whole content of Poitou–Tate here is that two
   subspaces are maximal isotropic, which bounds their intersection only by `½ dim V`, sharply.
   *Closes the packet's listed-open direction "global duality giving a uniform numerical bound".*
2. **Artin–Verdier gives nothing uniform.** Realising `Ш` as `H¹_ét(Spec Z, 𝓔)` is the most
   finite-looking incarnation available, but the only applicable finiteness theorem is for finite
   sheaves and reproduces "`Ш[n]` finite for each `n`", i.e. "`Sel_n` finite". *New card.*
3. **The seed has no exploitable specificity.** (§3.5.) `x(P₁) = 4547`, the divisibilities
   `4547 | a₂, a₄`, the exponents `(3,1,2)` in `Δ` and the constant `2⁸·3²` are identities of a
   two-parameter family. *Closes the packet's listed-open direction "treat the conductor pattern
   as a feature".*
4. **The 4547 component group is invisible to odd `Ш[p]`.** (§3.6.) Its content is exactly
   `c_{4547} = 2`, a `Q36` input. *Closes the "uninterpreted seed datum" lead with the exact
   consequence the packet demanded.*
5. **Two of the packet's own success conditions are defective.** (§3.1, §3.2.) Target (B) accepts
   too little; target (A) is not a weaker target. *Both machine-checked.*

---

## 6. What I did not do

* I did not prove `FIN`, `ORDER9`, or any bound on `Ш[p]` for any prime outside `{2,3,5,7}`.
* I did not attempt `Q36`; no construction of mine controlled both sides.
* I did not verify Skinner–Urban's hypotheses for the seed (see §4) — this is the single most
  useful next check, and it is a literature/verification task, not an invention task.
* I did not replay any historical certificate, Lean freeze, or numerical bound from the record.
* I make **no novelty claim** for Theorems A and A′ as mathematics; see their gradings.

---

## 7. Machine-checked artifacts

All build against Lean 4.28.0 / Mathlib `8f9d9cff…`, with no `sorry` and axioms within
`{propext, Classical.choice, Quot.sound}`.

| file | contents |
|---|---|
| `RequestProject/SeedData.lean` | exact integral invariants `c₄, c₆, Δ` and their factorisations; the points; the `4547`-adic valuations (Tate-algorithm input); valuations at `2, 3, 2243, 5843` |
| `RequestProject/Family.lean` | the two-integer family; `5x(Q₁) = −a₂`; `Δ = 2⁸·3²·A³BC²`; both points generic; seed `= (A,s) = (4547,12)` |
| `RequestProject/DualityTautology.lean` | Theorem A's bookkeeping core: the Greenberg–Wiles right-hand side is the product formula |
| `RequestProject/IsotropicSharpness.lean` | Theorem A′: nondegeneracy, two maximal isotropic subspaces, intersection of every prescribed dimension |
| `RequestProject/Assembly.lean` | `#A[n] < K ∀n ⇒ A` finite with `#A < K` (and converse); `A[p] = 0 ∀p≠3` + `#A[3^∞] = 9` ⇒ `#A = 9` |
| `RequestProject/TargetBCountermodel.lean` | `(Z/3)² ⊕ (Z/11)²` with `C_E = 33` meets all of (B) and all four retained primary inputs, with order `1089` |
