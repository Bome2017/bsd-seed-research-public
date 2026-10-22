# Phase 1 — independent review of the Néron-area normalization

**Verdict: PASS.** For every prime `p >= 5` with `p ∤ N`,

    v_p(M) = v_p(xi_{f_B}(N^+,N^-)) = v_p(eta_f(N^+,N^-)) = v_p(eta_f(N)) = v_p(r) = v_p(d),

and hence `u_E = ed/(c_E^2 M) ∈ Z_p^x`. No false or missing load-bearing interface was found.
- **Grade:** a written synthesis. Published theorems are imported at their stated
  hypotheses. The interfaces below were replayed from definitions.
- **Not established:** `p ∤ M`, any global identity `M = d` or `M = r`, and anything at `p ∈ {2,3}` or `p | N`.

Sources, all offline in this handoff:
- `sources/kim_ota_1905.02926v4.txt` (KO): Thm 1.1, §2.1–2.2, §5.2, §6.1;
- `sources/agashe_ribet_stein_moddeg3.txt` (ARS): §1, §2.1, Thm 2.1, Thm 3.6, Rem 3.7;
- retained `02_curve.tex` (A.1–A.4), `F_lattice_proof.tex` (chosen map), `context/01_THETA_KERNEL.md`.

## 1. The chosen map and the pullback identity (replayed)

**The map.** It is taken from the retained appendix, §"The chosen parametrization":
- `pi : J_0(N) -> E_0` is the optimal quotient, and `phi_0 = pi ∘ iota_infty`.
- `phi_E = phi_0` if `E = E_0`; otherwise `phi_E = psi ∘ phi_0`, with `psi : E_0 -> E` the rational 2-isogeny.
  No further multiplication map is allowed.
- `phi_E^* omega_E = c_E omega_f` with `omega_f = 2 pi i f(z) dz` and `c_E ∈ Z`, the sign fixed.
- `c_E | 2^9` is retained (A.4 / appendix, geometric grade retained). `e := deg psi ∈ {1,2}` and
  `d := deg phi_0` (the modular degree of `E_0`), so `deg phi_E = ed`.

**The Néron differential.** By A.1(i) the substitution `x = X + 7578` has `u = 1`. So `omega_E = dx/(2y)` on
`y^2 = x^3 - 22735x^2 + 106272484x` is the Néron differential of the global minimal model.

**The identity.** For `A_E = (i/2) ∫_{E(C)} omega_E ∧ conj(omega_E)`, the covolume of the complex Néron period
lattice (neither `Omega^+` nor the BSD real period):

    ed * A_E = (i/2) ∫_{X_0(N)} phi_E^*omega_E ∧ conj(phi_E^*omega_E)
             = (i/2) c_E^2 (2 pi)^2 ∫ |f|^2 dz∧dzbar = 4 pi^2 c_E^2 P_f,

using `dz ∧ dzbar = -2i dx∧dy` and `P_f = ∫_{Gamma_0(N)\H} |f|^2 dx dy`. Hence, with
`lambda_f(G) = P_G/P_f` (a ratio, independent of the measure normalization) and `01` Theorem A:

    K_E(v,w) := (4 pi^2/A_E) P_{Theta(v,w)} = (ed/c_E^2) lambda_f(Theta(v,w)) = (ed/c_E^2) psi(v)psi(w)/M.   (1.1)

**Scope.** The identity is homogeneous under replacing `phi_E` by `[m] ∘ phi_E`: the degree scales by
`m^2` and `c` by `m`. The retained bound `c_E | 2^9`, however, holds only for the chosen map. `Delta > 0`
(A.1), so the period lattice is rectangular and `A_E = Omega_1 · |Omega_2|`; §5 records a numerical cross-check.

## 2. Interface (3): `(M) = xi_{f_B}(N^+,N^-)` in `Z_p` (replayed from definitions)

- **The pairing (KO (6.1)).** `<f_B,g_B>_N = sum_{[b]} <f_B(b), g_B(bw)>_k · (#(B^x ∩ b Rhat^x b^{-1} Qhat^x)/Q^x)^{-1}`, with `w` the
  Atkin–Lehner element for `N^+` and `[b]` running over `B^x\Bhat^x/Rhat^x Qhat^x`.
  - For `k = 2`, `<,>_k` is multiplication.
  - `Qhat^x = Q^x Zhat^x` and `Zhat^x ⊂ Rhat^x`, so the double-coset set is the lab's class set `X`.
  - `B^x ∩ b Rhat^x b^{-1} Qhat^x = Q^x · O_b^x`, whose quotient by `Q^x` is `O_b^x/{±1}`. This is trivial for every class
    (`01` §0.2: all stabilizers are `{±1}`, and `|X|` equals the mass). **All weights are 1.**
- **Atkin–Lehner sign.** `w` permutes `X` and commutes with every `T_l`, `l ∤ N`. The `f`-eigenline of the
  prime-to-level algebra on `Q[X]` is one-dimensional (`01` §2; JL + strong multiplicity one). So
  `psi(xw) = eps_w psi(x)` with `eps_w = ±1`, since `w^2` acts trivially. Hence `<psi,psi>_N = eps_w M`.
- **Lattice and localization.**
  - On `O^X` the Gram matrix of (6.1) is a permutation matrix, so the pairing is unimodular.
  - The prime-to-level Hecke operators are self-adjoint, so the decomposition by maximal ideals is
    orthogonal. The non-Eisenstein summand `(O^X)_{m_f}` (`rho-bar` irreducible) therefore carries a
    perfect pairing, and constants disappear there.
  - This is the pairing KO call perfect on `S_2^{N^-}(N,O)_{m_f}`.
- **The ideal.** KO define `xi_{f_B}` as "the quaternionic analogue of the cohomology congruence ideal
  using (6.1)" (§6.1.2). The classical ideal is `delta_f(N) = ∧^2 M_N[p_f]`, the image of the perfect
  pairing on the `f`-eigen-submodule (§5.2).
  - Here the eigen-submodule is `O f_B`, with `f_B` normalized by mod-`p` non-vanishing (KO §6.1.1), i.e.
    `f_B = psi` up to `Z_p^x`: `psi` is globally primitive.
  - Hence `xi_{f_B}(N^+,N^-) = <psi,psi>_N Z_p = M Z_p`.
- **Residual risk (recorded, not load-bearing on the reading above).** The cited definitions
  (CH18 (3.9), (4.3); PW11 §2.1) are not in the offline set. The reading uses KO's own description.

## 3. KO imports and every CR+ hypothesis at the seed

**Imports** (statements read in KO; proofs not replayed):
- **Corollary 6.7(1):** `eta_f(N^+,N^-) = xi_{f_B}(N^+,N^-)`, from Thm 6.5 (freeness, via CH18 Prop 6.8),
  Thm 6.2 (JL) and DDT Lemma 4.17.
- **Corollary 6.7(2):** `ord(eta_f(N)/eta_f(N^+,N^-)) = sum_{q|N^-} t_f(q)`, which is also Thm 1.1.
- **Non-ordinary `p`.** Theorem 6.5 carries no ordinarity hypothesis. KO Remark 6.6(1) asserts that
  replacing CH18's ordinary deformation condition by the low-weight crystalline one "does not affect
  any of result in [CH18, §6]", with a one-sentence justification (DFG04, Dim09).
  - At the seed's supersingular good primes (23, 29, 131, …; A.1(iv)), the freeness therefore rests on
    that remark.
  - This is a published assertion whose adaptation is **sketched, not proved in detail**. It is
    recorded as the weakest imported link.
  - The ordinarity of KO §6.2 (Assumption 6.8) is not used.

**Hypotheses** (Assumption 2.1 and 6.3 (1)–(7); Thm 1.1 (1)–(6) are implied, Remark 6.4). All hold for
every `p >= 5`, `p ∤ N`:

| hypothesis | check at the seed |
|---|---|
| 2.1 (FL): `2 <= k <= p-1`, `p ∤ N`, `rho-bar_f ≅ rho-bar` | `k = 2`, `p >= 5` |
| 2.1 (TW): `rho-bar|_{G_Q(sqrt p*)}` abs. irreducible | A.3: image `GL_2(F_p)` for every odd `p`; since `Q(sqrt p*) ⊂ Q(zeta_p)` and `det` is cyclotomic, the restriction's image is the square-determinant subgroup `⊇ SL_2(F_p)`, which is abs. irreducible |
| 6.3(2): `2 <= k < p-1`, `p ∤ N` | `2 < p-1` iff `p >= 5` |
| 6.3(3): `p, N^+, N^-` pairwise coprime | `N^+ = 2^3·4547^2`, `N^- = 3·2243·5843` |
| 6.3(4): `N^-` squarefree, odd number of primes | three primes |
| 6.3(5): `q | N^-`, `q ≡ ±1 (p)` ⇒ `q | N(rho-bar)` | holds for **all** `q | N^-`: `v_q(Delta) = 2,1,2` is prime to `p`, so the Tate-curve inertia class (for non-split `q`, after the unramified quadratic twist) stays nonzero mod `p` |
| 6.3(6): `q ‖ N^+`, `q ≡ 1 (p)` ⇒ `q | N(rho-bar)` | vacuous: no prime exactly divides `N^+` |
| 6.3(7): `(N(rho-bar), N/N(rho-bar)) = 1` | `N(rho-bar) = N` (next item) |

**Conductor preservation, `N(rho-bar) = N`.** At `q | N^-` the exponent is 1 (by 6.3(5)). At 2 and 4547
the reduction is potentially good:
- `v_2(j) = 3·4 - 8 = 4 >= 0`;
- `v_4547(j) = 3·1 - 3 = 0`, with `v_4547(c_4) = 1` since `c_4 = 16·4547·43559`.

So inertia acts through a finite group `Phi`. Its order divides 24 at 2 (Serre–Tate / Kraus) and is
exactly `4 = 12/gcd(12, 3)` at 4547. Both orders are prime to `p >= 5`. For every ramification subgroup
`H ⊆ Phi`, the idempotent `|H|^{-1} sum_{h∈H} h` is `p`-integral, so `rank T^H = dim (T/p)^H`. The Artin
conductor exponents (3 at 2, 2 at 4547) are therefore unchanged mod `p`.

**Tamagawa exponents.** `t_f(q) = 0` for `q | N^-` (KO Def. 2.12 and the note "`t_f(q) = 0` if `q | N(rho-bar)`").

**Conclusion.** `v_p(eta_f(N)) = v_p(eta_f(N^+,N^-)) = v_p(xi_{f_B}) = v_p(M)`.

## 4. Interface (5): `eta_f(N) Z_p = r Z_p` (replayed)

- **KO's `eta_f(N)`.** It is `pi_f(Ann(ker pi_f))` in `T(N)_{m_f}`, the full Hecke algebra over `O` acting faithfully on
  `H^1_{et,c}(Y_1(N), F)[<.> - 1]` and localized at the non-Eisenstein `m_f` (§2.1.2, Def. 2.6, Thm 1.1).
  - Eichler–Shimura and non-Eisenstein localization make this Hecke module `S_2(Gamma_0(N), Q_p)_{m_f}^{⊕2}`
    rationally.
  - A ring generated by fixed operators inside `End` of a faithful lattice depends only on their
    action on the rational space. So `T(N)_{m_f} = (T_Z ⊗ Z_p)_{m_f}`, with `T_Z = Z[T_n : n >= 1] ⊂ End S_2(Gamma_0(N))`,
    ARS's `T`.
- **Full vs anemic (a check, not needed).** Because `N(rho-bar) = N`, every form in `S_2(Gamma_0(N))_{m_f}` is new
  of level `N`.
  - If `q ‖ N`, then `a_q(g) = ±1` and `a_q(g) ≡ a_q(f) (mod m)`, so `U_q = a_q(f)`, a scalar, on the `m_f`-part.
  - If `q^2 | N`, then `U_q = 0` on newforms with trivial character.

  So the anemic and full algebras coincide after localization.
- **Duality** (import: standard Hecke duality). `S_2(Gamma_0(N), Z) ≅ Hom_Z(T_Z, Z)` via `g -> (t -> a_1(tg))`.
- **Computation.**
  - `T_Z ⊗ Q = Q e_f × T'`, and `Ann(ker lambda_f) = T_Z ∩ Q e_f = Z t_0` with `t_0 = n e_f` primitive, so `eta = nZ`.
  - For `g ∈ S_2(Z)`, the Petersson projection is `e_f g = phi_g(e_f) f = (phi_g(t_0)/n) f`.
  - `{phi_g(t_0)} = Z` because `t_0` is primitive and `T_Z` is free.
  - So the projection of `S_2(Z)` is `n^{-1} Z f`, and `S_2(Z)/(Zf + (Zf)^perp) ≅ Z/n`.
- **Result.** This is ARS's `r_E` (definition (ii), §2.1, same lattice `S_2(Z)` of integral `q`-expansions). Other
  maximal ideals are orthogonal to `f`, so `v_p(r) = v_p(eta_f(N))`.

## 5. ARS (import) and the conclusion

- ARS Thm 2.1 applies to the **optimal** quotient `E_0` (ARS §1, §2.1), with `m_{E_0} = d`: `d | r`, and `ord_p(r) = ord_p(d)`
  when `ord_p(N) <= 1`.
- It is proved via Thm 3.6(b): for `Gamma_0(N)`, `p ∤ N` gives `ord_p(r~_A) = ord_p(n~_A)`, and newforms give equality
  whenever `p^2 ∤ N`. Remark 3.7 identifies exponents with degrees for elliptic curves. No extra
  multiplicity-one hypothesis appears in the statement.
- `r` depends only on `f`. `d` belongs to `E_0`, not to the possibly 2-isogenous seed model.

**Theorem (unit scale; written, from the imports above).** For every prime `p >= 5` with `p ∤ N`,
`v_p(M) = v_p(d)`. Since `e ∈ {1,2}` and `c_E | 2^9`, `u_E = ed/(c_E^2 M) ∈ Z_p^x`. Consequently
`K_E(v,w) = u_E psi(v)psi(w)`, and `K_E(z,z) ∈ Z_p^x` iff `psi(z) ≢ 0 (mod p)`.

**Numerical cross-check of the analytic factor** (`output/scripts/period_area_check.py`, independent of
the packet code). The periods of `dx/(2y)` were computed by direct quadrature and by AGM, and
`4 pi^2/(Omega_1 |Omega_2|) = 4 g_1 g_2` agree (see the script's output file). This checks only the period-area
convention of PROOF.md (9); the arithmetic above does not depend on it.

## 6. Replayed vs imported

| step | status |
|---|---|
| pullback identity (1.1), chosen map, `u = 1` | replayed (retained map data) |
| (3) weights, Atkin–Lehner sign, unimodularity, `xi = (M)` | replayed from definitions; KO's definitional text read; CH18/PW11 not available offline |
| CR+ at the seed, `N(rho-bar) = N`, `t_f(q) = 0` | replayed from retained A.1–A.3 data |
| KO Cor. 6.7 (1)–(2), Thm 6.5 (incl. Remark 6.6(1) non-ordinary) | imported (statement read) |
| (5) `eta_f(N) = (r)` | replayed; Hecke duality imported |
| ARS Thm 2.1 / 3.6(b) | imported (statement read) |
| residual surjectivity A.3, `c_E | 2^9`, `e ∈ {1,2}`, Theorem A | retained, grades unchanged |

**Failure modes checked and excluded.** None of the following occurs here:
- a global `M = r` identification;
- stabilizer weights;
- an Atkin–Lehner sign changing the ideal;
- a prime-to-level versus full Hecke algebra mismatch after localization;
- a primitive vector ceasing to be primitive after localization;
- a lattice other than integral `q`-expansions in `r`.
