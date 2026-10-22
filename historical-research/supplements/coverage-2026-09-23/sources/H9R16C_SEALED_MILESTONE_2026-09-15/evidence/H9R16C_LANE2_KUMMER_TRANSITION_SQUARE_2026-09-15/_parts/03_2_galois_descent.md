## 03.2 Galois descent of the finite balanced point (point normalization over `K_0`)

### 03.2.1 BCPV (4.5) pins the Galois law of `W`

Inputs, all printed: (4.1) `<a_1,a_2,a_3> Δ_r[e] = Δ_r[a_2a_3e_1, a_1a_3e_2, a_1a_2e_3]`;
(4.2) `σ_m Δ_r[e] = Δ_r[me]`; (4.4) `Δ_r^ord = (e'W_{Np^r})^{⊗3}Δ_r`; (4.5)
`σ_m Δ_r^ord[e] = Δ_r^ord[m^{-1}e]`; KLZ2 diamond rule `<d>W = W<d^{-1}>`.

Suppose `W^{σ_m} = <m>^k ∘ W` on the p-part for some exponent `k`. Then

    σ_m Δ_r^ord[e] = (e' W^{σ_m})^{⊗3} Δ_r[me] = (e'W)^{⊗3} <m^{-k},m^{-k},m^{-k}> Δ_r[me]
                   = (e'W)^{⊗3} Δ_r[m^{1-2k} e] = Δ_r^ord[m^{1-2k} e].

(4.5) holds for all `m ≡ 1 (mod p)` iff `k = 1`. So **BCPV's printed (4.5) forces
`W^{σ_m} = <m> ∘ W`**, which is also what the KLZ2 moduli definition gives (the class `P''` with
`<P_Q, P''> = ζ_Q^z` is `z·P'_Q`), and has the same shape as Hida's `w_r^σ = <z>∘w_r` (S4 §5).
This is a free consistency test for Lane 1: a dictionary producing the opposite law contradicts (4.5).

The same inputs give, for `m = μ^2`, `μ ≡ 1 (mod p)`:

    <μ,μ,μ> Δ_r^ord[e] = (e'W)^{⊗3} <μ^{-1},μ^{-1},μ^{-1}> Δ_r[e] = Δ_r^ord[μ^{-2}e] = σ_m Δ_r^ord[e].    (G1)

The tame part of `W_{Np^r}^{⊗3}` moves by the diagonal tame diamond, which fixes the diagonal cycle;
so `Δ_r^ord` is `L_r`-rational, as BCPV (4.4) states.

### 03.2.2 The contracted point

`Φ_r^mod(t_2 ⊗ t_3) = Π_{Z,*}((1 ⊗ t_2 ⊗ A_r t_3) Δ_r^ord)`, `A_r = W_{N_g p^r}^{-1}(U'_p)^r` on factor 3.
Take `σ ∈ G_{K_0}` with `σ(ζ_{N_g p^r}) = ζ^{z}`, `z = (z_p, z_N)`, `z_p = m = μ^2`. All of `Π_Z`,
`t_2`, `t_3`, `U'_p`, `e'` are Q-rational; `A_r^σ = W^{-1}<z>^{-1}(U'_p)^r = A_r <z_p>^{-1}<z_N>^{-1}`. Using (G1),
`Π_{Z,*}(<μ>⊗1⊗1)(−) = <μ> Π_{Z,*}(−)`, and commutativity of the primed Hecke algebra:

    σ Φ_r^mod(t_2 ⊗ t_3) = <μ>_{(1)} Φ_r^mod( t_2<μ> ⊗ <z_N>^{-1} <m>^{-1} <μ> t_3 ).

Balance (H9R16-A/B, `u' = <μ>`; check: `ρ(<d>) A_r = <d>^{-1}W^{-1}U'^r = W^{-1}<d>U'^r = A_r<d>`)
moves `<μ>` from factor 2 to factor 3, and `<μ><μ><m>^{-1} = 1`:

    σ Φ_r^mod(t_2 ⊗ t_3) = <c_r(σ)^{1/2}>_{(1)} Φ_r^mod( t_2 ⊗ <z_N(σ)>^{-1} t_3 ).      (G2)

### 03.2.3 Reading (G2)

* **p-part.** The whole dagger twist lands on the `J_r`-factor as `<c_r^{1/2}>`; the carrier is
  untwisted at `p`. This is exactly what BCPV's target requires: in Def. 4.14 the trace passes through
  `ad(T_g)` with no dagger on it. If `W^σ = <z>^{-1}W` instead, the carrier would carry `<c_r>` and the
  contracted point would no longer map to BCPV's `T^† = T_f^† ⊗ ad(T_g)`.
* **tame part.** The carrier is twisted by `<ε_N>^{-1}` on factor 3 — on `g`-isotypic parts this is
  `ε_g^{-1}`, i.e. **the `g^c` twist of S1 (1.7)**. The balanced point is `K_0`-rational only after this
  twist; without it it is defined over `K_0(μ_{N_g})`. "Schematically over `Q(μ_p)`" is correct only
  with the tame nebentype twist written into the carrier.
* **Type.** (G2) says `Φ_r^mod ∈ Hom_{G_{K_0}}( B_r^{(ε)}, e'Ĵ_r(Q̄)^{(c^{-1/2})} )`, i.e. (by S3
  Thm. 1.4 with the inverse convention of Lemma 1.3) `Φ_r^mod ∈ P_r^{tr,†}`: a `K_0`-rational point of
  the type-B twist with lattice character `c_r^{+1/2}` on `J_r` and tame lattice character on factor 3.
  The normalized `Q_r` lies there too (`U'_p`, `e'` are Q-rational and `G_r`-central).

**Level caveat (inherited, not introduced here).** The frozen H9R16-A/B formula applies
`W_{N_g p^r}` on factor 3 of a cycle living at common tame level `N = lcm(N_f, N_g)`. As an
Atkin–Lehner operator `W_Q` on `X_1(Np^r)` this needs `Q = N_g p^r ∥ Np^r`, i.e. `gcd(N_g, N/N_g) = 1`;
otherwise factor 3 must first be pushed to the native level `N_g`. Only the tame factor `<z_N>` in
(G2) depends on this choice, and it lands on factor 3 either way. Fixing the level is Lane-1 bookkeeping.

**Status.** `C_POINT_NORMALIZATION` — descent of the finite point to the fixed-base type-B object —
is **PROVED here from printed inputs** ((4.1), (4.2), (4.4), (4.5), KLZ2 diamond rule, H9R16-A/B
balance) plus one step used by BCPV without statement: the pushforward `Π_{Z,*}` commutes with
factor-1 diamonds (the graph `X_{14}` is `<μ>×<μ>`-stable). No `W/w` dictionary is used.
