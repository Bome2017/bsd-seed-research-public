> **CORRECTED 2026-09-27 by Codex** (`~/BSD_K288_UNIFORMITY_AUDIT_CODEX_2026-09-27/CORRECTIONS_FOR_CLAUDE.md`).
> The conditional tail argument stands. Withdrawn:
> 1. "This gives FIN". Finite support is not FIN: the exceptional primary groups still need proofs, and
>    criteria are not certificates.
> 2. "One exact w_p". Auxiliary independence of unit parts is unproved (E10 claims only the zero pattern).
> 3. "v_p(w_p) = v_p(#Sha)". A residue in F_p only detects Sha[p] = 0 versus ≠ 0, not the size of Sha.
> 4. "W = 288" from rationality. Rationality of q does not give q = 36.
> 5. "Is the refined Mazur–Tate conjecture". Overstated: BKS Thm 1.1 has further hypotheses (BSD, GPR).
>
> Status: a formulation of an open target, overlapping E10/E11. It is not a new method.

# Can c₂ ≡ (a_l − 2)·288·R_{p,l} be promoted to a uniform theorem? (analysis, 2026-09-27)

This is a written deduction from retained inputs. The imports are named, it has not been independently audited yet,
and no computation was done.

## 1. The multiplier, defined without Sha

Fix p outside B = {2, 3, 5, 19, 59, 487, 2243, 4547, 5843}. Choose l ∈ L_p⁰ with R_{p,l} ≠ 0; G2 supplies such l for
every p. Define

    w_p := c₂(θ_l) / ((a_l − 2)·R_{p,l})  ∈ F_p.

- Both c₂ (modular symbols) and R (the tame height of E(ℚ)) are defined without any reference to Sha.
- Independence of l is the retained Σ-compatibility import (E10 Prop. D and BKS II §5).
- So w_p is a well-defined, Sha-free quantity. The observed law is w_p ≡ 288 (mod p) at
  p = 17, 19, 23, 29, 31, 37, 41, 43, 47.

## 2. What w_p is, by the retained factorization

This uses BKS II Lemma 4.2, Prop. 5.2, Cor. 5.3 and §5.3, together with the Burns–Macias Castillo Bockstein ≐ tame
regulator comparison. Up to a p-adic unit,

    w_p = x_{ℚ,Σ} · #A_p     if s_p = 2  (Sha[p^∞] finite; then #A_p = #Sha[p^∞]),
    w_p = 0                  if s_p > 2.

Here x_{ℚ,Σ} ∈ ℤ_p is the coordinate of Kato's determinantal zeta element in its integral line.

At good ordinary p, x_{ℚ,Σ} is a unit (Kato + Skinner–Urban IMC import; SU's hypothesis holds since v₂₂₄₃(Δ) = 1).
Hence, at those p:

    v_p(w_p) = v_p(#Sha[p^∞])   (with v = ∞ when Sha[p^∞] is infinite).

## 3. Consequences

**(a) Uniform version ⟹ finite support.** Suppose there is a nonzero rational W with w_p = W·(unit) for all p outside
a finite set. For p outside B and not dividing num(W)·den(W), G2 gives an l with c₂(θ_l) ≢ 0, and Ota Thm 6.4 then
gives Sha[p^∞] = 0. Together with certificates at the finitely many remaining primes (2–47 are done; 59 and 487 are
Ota-eligible good primes; 2243, 4547 and 5843 have the Bullach–Honnor criterion), this gives **FIN**. With W = 288
exactly, the 3-part matches 9 as well.

**(b) The observed law carries more than vanishing.** At every p where Sha[p] = 0, it says x_{ℚ,Σ} ≡ 288·u⁻¹ (mod p).
That is a congruence for Kato's p-adic coordinate that is the same rational number for all p, i.e. **"the p-adic Kato
coordinates are shadows of one rational number."** This is exactly the content of the p-adic Tamagawa number
conjecture for h¹(E)(1), and of BKS's Generalized Perrin-Riou conjecture at tame level. There, W = 8·q with
q = L''(E,1)/(2Ω·Reg), and q ≈ 36.

**(c) Known implications.**
- ETNC / BSD ⟹ the refined Mazur–Tate law (Burns; Tan under BSD).
- The refined law with a nonzero rational constant ⟹ FIN-b (this note, via G2 + Ota).
- The missing arrow is a proof of the refined law, with any nonzero rational constant, **without assuming Sha finite**.

## 4. Where the determinant route stops, exactly

The only Sha-free handle on w_p inside the determinant formalism is w_p itself. At ordinary p its valuation equals
#Sha[p^∞]'s, so any valuation-only uniform statement about w_p is the statement "Sha[p] = 0 for almost all p".
- On this route there is no weaker target.
- This is not an impossibility claim: another method could prove the same statement.
- What is missing is an **external global input** that produces the p-adic numbers w_p from one p-independent object.

## 5. Candidate global inputs (none constructed)

1. **Archimedean.** RAT (q ∈ ℚ) plus the tame-level GPR/p-adic Beilinson identity without assuming finiteness. This
   gives W = 8q. It is the same arrow Q36 needs.
2. **A global integral object whose index is W.** This is the rank-2 analogue of the Heegner index, which supplies
   the constant in rank 1. y_K is torsion here, so the candidates are:
   - an index built from derived Heegner or derived Beilinson–Kato classes that is independent of p;
   - a rank-2 cycle over ℚ, which is known only over function fields.
3. **Analytic nonvanishing** (a genuinely different method). Show directly, for every large p, that some l gives
   v_π(θ_l(χ)) = 2 exactly for a character χ of order p.
   - Here θ_l(χ) = τ(χ)·L(E,χ̄,1)/Ω ∈ ℤ[ζ_p], and π = 1 − ζ_p.
   - The inputs would be the rational modular symbols [a/l]⁺, via a residual-distribution or equidistribution
     theorem for depth-two Mazur–Tate coefficients.
   - Such a theorem would have to detect Sha, since the coefficient vanishes for every l when Sha[p] ≠ 0. I know of
     no such result; this is the question to ask of experts in modular-symbol distribution.

## 6. Verdict

The K = 288 law, promoted to all p, **is** the refined Mazur–Tate conjecture for this curve (rank 2, tame level,
constant 288). It would prove FIN-b immediately, via G2 and Ota. A proof needs one of the three external inputs above.
The determinant/Bockstein formalism alone reproduces Sha rather than bounding it.
