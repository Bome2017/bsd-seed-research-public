# C1_PROJECTED_CHI_RELATIONS_001 — report (2026-09-17)

**Return: PROJECTED_RELATIONS_INSUFFICIENT.**
- N = 8 918 projected generators.
- Achieved rank 0.
- 396 962 exact candidates examined; none gave a relation.

This is **GRH-conditional reconnaissance only**. Nothing here says anything about b; missing relations are not evidence about the class group. No bnfinit, bnfcertify, Minkowski sweep, units, regulator or SNF.

**Setting.**
- Seed (m, n) = (2243, 12).
- Dual field L_d, defined by `pLd`; the automorphism τ is `tauLd`, both from `~/BSD_SMALL_SEED_FIXED_PRIME_2026-09-17/runs/fields_2243_12.gp`.
- G = Gal(L_d/F₀) = ⟨τ⟩ ≅ C₄.
- **Retained convention:** b = dim ker(T_τ − 2) on Cl(L_d)/5, where T_τ[𝔞] = [τ𝔞]. This is the calibration convention, in which 389a1 gave τ-eigen-dims [0,1,0,0]. So χ(τ) = 2.

**Tools and budget.**
- Tool: PARI 2.17.4 (source-matched), one thread.
- Budget: about 170 of 300 aggregate CPU-s; peak RSS 23 MB.

## Phase 0 — the reduction (verified, with two amendments)

Let A = Cl(L_d)/5. Since x⁴ − 1 splits into distinct linear factors over F₅, A = ⊕_{λ∈F₅*} A_λ. The projector onto A₂ is e_χ = −Σ_{k=0}^{3} 3^k T_τ^k.

1. **Non-free orbits project to zero.**
   - A nontrivial stabilizer contains τ², so e_χ[𝔓] = T_τ² e_χ[𝔓] = χ(τ²) e_χ[𝔓] = −e_χ[𝔓], hence e_χ[𝔓] = 0.
   - A prime 𝔓 is in a free orbit ⟺ e(𝔓/𝔭₀) = f(𝔓/𝔭₀) = 1, i.e. 𝔭₀ splits completely in L_d/F₀.
   - In particular every prime with e = f = 1 over Q is free.
2. **One generator per free orbit.** e_χ[τ^k 𝔓_O] = 2^k x_O.
3. **Rows.**
   - Take (α) = ∏𝔓^{v_𝔓}. Every free-orbit prime in its support must have norm ≤ B; non-free primes of any norm are allowed, because they project to 0.
   - Then Σ_O (Σ_k v_{τ^k𝔓_O}(α)·2^k) x_O = 0.
   - Changing α to τα multiplies the row by 2 (the shift identity).
   - Elements of F₀ or of the degree-12 subfield M_d = L_d^{τ²} (index 2) give zero rows, since Σ_k 2^k = 15 ≡ 0 and 1+4 ≡ 2+8 ≡ 0.
4. **Bound.** Under GRH, V = F₅^N ↠ A₂. So any valid rows of rank r give **b ≤ N − r**.

**Amendment 1 — the GRH bound B = 419 775 was computed for L, not L_d. It transfers.**
- L = Q(vector of E[5]) and L_d = Q(covector). The permutation characters of GL₂(F₅) on these agree, because dim ker(g−1) = dim ker(g − det g) for every g. So L and L_d are **Gassmann-equivalent**, and ζ_L = ζ_{L_d}.
- PARI 2.17.4's GRH generation test (`buch2.c`: `init_GRHcheck`, `get_fs`, `GRHchk`) sees a field only through N, R₁, log|D| and the residue-degree multiset at each p.
- Verified: **zero** L/L_d pattern mismatches over all 35 373 primes p ≤ B, with exact `idealprimedec` at ramified and index primes. Discriminant and signature are equal.
- So under GRH, the prime ideals of L_d of norm ≤ 419 775 generate Cl(L_d).
- Fallback, not needed: the uniform Grenié–Molteni c₂ = 4 bound, 962 724.

**Amendment 2 — "χ and χ⁻¹ dimensions must agree" is false.**
- The retained 389a1 calibration had dim A₂ = 1 and dim A₃ = 0.
- The convention was instead checked directly:
  - (Z4) τ(𝔓_r) = 𝔓_{τ⁻¹(r)}, by exact `nfgaloisapply` on prime ideals: 8/8 primes.
  - (Q1) columnwise v_{τ𝔓}(τα) = v_𝔓(α) = v_p(Nα) on 12 genuine element–prime pairs: 12/12.
  - τ⁴ = id, and τ² = (θ ↦ −θ), the unique involution.

## Phase 1 — streamed projected factor base (`runs/phase01.gp`): viable

| item | value |
|---|---|
| primes scanned | 35 373 (all p ≤ 419 775) |
| **N (free C₄-orbits of norm ≤ B)** | **8 918** |
| p with exactly 4 degree-1 primes (1 orbit each) | 8 366 |
| p split completely (24 degree-1 primes, 6 orbits) | 86 (516 orbits) |
| exact-route orbits (p ≤ 647, or ramified/index primes) | 36 (incl. the ramified m-orbit at 2243; f ≥ 2 orbits at 7, 13, 29, …) |
| non-free prime ideals of norm ≤ B met (excluded, zero projection) | 77 |
| other root counts | none (only 0, 4 and 24 occur) |
| CPU / memory | 6.8 s; heap about 1.4 MB, RSS 17 MB. **The 4 GiB wall is gone.** |

## Phase 2 — partial exact relations (`runs/phase2.gp`, `runs/phase2b.gp`): none found

| family | candidates | fully B-smooth | norms (log₁₀) | best non-smooth cofactor |
|---|---|---|---|---|
| a − bθ, gcd = 1, a ≥ 0 (a ↦ −a is τ²) | 384 534 | **0** | 52.4 … 110+ (most 90–110) | 10^28.3 (θ itself, norm 10^52.4) |
| skew-reduced elements of 𝔓 = (p, θ−r), p > 10⁵ | 12 428 | **0** | 45.7 … 169.7 (median 118) | 10^31.0 |
| stock `idealred([𝔓,1])` | — | — | returns multiplier 1 (no reduction, no relation) | — |

- No row was produced, so there was nothing to replay or eliminate. **Achieved rank 0; b ≤ 2 needs rank 8 916.**

**Cost statement.** This concerns the method, not b.
- Elements from subfields give zero rows.
- The smallest cofactor seen was 10^45.7 (u ≈ 8.1, Dickman ρ ≈ 2·10⁻⁸), a single extreme among 12 428.
- The a − bθ floor is 10^52.4 (u ≈ 9.3, ρ ≈ 4·10⁻¹⁰), and only a few hundred candidates lie near it.
- Typical cofactors are 10^90–10^118, i.e. u ≈ 16–21 and ρ ≈ 10⁻¹⁹–10⁻²⁷.
- Reaching 8 916 independent rows is beyond this approach by many orders of magnitude.
- The projection fixes memory. It does not fix smoothness, which is the real wall.

## Return and recommendation

    PROJECTED_RELATIONS_INSUFFICIENT
      N = 8918 (GRH factor base, transferred from L by arithmetic equivalence; 0 mismatches over all p <= B)
      rank achieved = 0 ; candidates 396 962 (a - b*theta: 384 534; ideal-reduced: 12 428); fully smooth: 0
      best cofactor 10^28.3 at norm 10^52.4 ; needed rank >= 8916 for b <= 2
    Phase 0 amendments: (1) B = 419775 is L's bound, valid for Ld via zeta equality; (2) chi/chi^-1 dimensions need not agree

Per the operator's own criterion ("if this compressed experiment still cannot get close to codimension 2, park direct class-group computation"): **park direct class-group computation for this seed.**
- This is the smallest non-anomalous parent-family seed checked, so the parking extends to the family.
- It is a resource decision. It says nothing about b.

## Proposed ledger block (not merged; needs operator acceptance)

```
C1_PROJECTED_CHI_RELATIONS_001 (seed (2243,12), dual field Ld) — PROJECTED_RELATIONS_INSUFFICIENT (2026-09-17)
  GRH-conditional reconnaissance only; no claim about b or Sha. Reduction verified: non-free C4-orbits have zero chi-projection
  (tau^2 acts by chi(tau^2) = -1); one generator per free orbit; row = sum_k v_{tau^k P}(alpha) 2^k mod 5 (retained convention
  T_tau[a] = [tau a], chi(tau) = 2); b <= N - rank. The GRH bound 419775 (computed for L) transfers to Ld: L, Ld are Gassmann-equivalent
  (vectors vs covectors of GL2(F5)), zeta_L = zeta_Ld, and PARI's GRHchk sees only (N, R1, log|D|, residue-degree patterns) —
  0 mismatches over all 35373 primes <= B. "chi and chi^-1 dimensions agree" is FALSE in general (389a1 calibration: dims 1 and 0).
  N = 8918 free orbits (streamed in 6.8 CPU-s, RSS 17 MB: the 4 GiB wall is gone). Relations: 396962 exact candidates
  (a - b*theta and skew-reduced ideal elements), 0 fully 419775-smooth; best cofactors 10^45.7 (ideal family) and
  10^52.4 (theta), typical 10^90-10^118 (Dickman u about 16-21).
  Rank 0 of the 8916 needed. Direct class-group computation PARKED for this seed (resource decision, not a statement about b).
```

Files: `runs/phase01.gp` (+ output and time), `runs/phase2.gp`, `runs/phase2b.gp` (+ outputs and times), `runs/api_probe.gp`, `MANIFEST.sha256`.

## Erratum (operator review, 2026-09-17) — supersedes the wording above where they conflict

1. **Norms vs residual cofactors.** The prose and the proposed ledger block called 10^45.7 and 10^52.4 "best cofactors". They are
   the **smallest sampled smoothness targets**:
   - 10^45.7 = min N(α)/N(𝔓) in the ideal-element family (the element norms themselves are about 10^50.7);
   - 10^52.4 = min |N(a − bθ)| in the a − bθ family.
   The **best residual non-smooth cofactors** are 10^31.0 and 10^28.3 respectively. The Dickman estimates (u ≈ 8.1 and ≈ 9.3) were
   computed from the smoothness targets and stand.
2. **Scope of the stop.** "This is the smallest non-anomalous parent-family seed checked, so the parking extends to the family" is
   withdrawn. Minimal conductor or discriminant scale does not imply the relation search is hardest there: a larger member could have
   better polynomial geometry, small principal generators or unusually smooth norms. What is recorded is
   **PROJECTED_RELATION_METHOD_PARKED_FOR_2243_12**. Operationally: do not repeat these naive relation families on nearby or larger
   members without a new reason. This is not a theorem that direct class-group computation fails anywhere in the family.
