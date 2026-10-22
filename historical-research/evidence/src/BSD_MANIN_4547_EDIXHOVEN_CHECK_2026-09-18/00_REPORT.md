# MANIN_4547_EDIXHOVEN_CHECK_001: 4547 ∤ c₀ for the isogeny class of the seed (2243, 12)

**Claim checked (operator, 2026-09-18).** Edixhoven's theorem excludes 4547 from the Manin constant c₀ of the strong Weil curve. With Mazur's p | c₀ ⇒ p² | 4N, this leaves c₀ = 2^a.

**Verdict: VERIFIED.** The citation goes through two published statements of the theorem; the original paper was not read (see Provenance).

## 1. The theorem as stated in the sources read

- **Česnavičius–Neururer–Saha, arXiv:1911.09446v3, §1.** They summarize [Edi91, Theorem 3], in the context of optimal φ: p ∤ c_φ for every prime p ≥ 11 at which E does not have an additive, potentially ordinary reduction of Kodaira type II, III or IV. Their footnote 3 adds that the unfinished manuscript [Edi01] tried to remove the Kodaira-type assumption, still for p ≥ 11.
- **Česnavičius, arXiv:1703.02951, §1.2.** Same theorem, stated for a new elliptic optimal quotient J₀(n) ↠ E and a prime p ≥ 11: if E_{Q_p} does not have potentially ordinary reduction of type II, III or IV, then ord_p(c) = 0.

The exception needs all three conditions at once: additive reduction, **potentially ordinary** reduction, and type II, III or IV. Potentially supersingular reduction is never an exception.

## 2. Local data at p = 4547 (`local4547.gp`, `local4547_output.txt`)

The isogeny class has exactly two curves, joined by a 2-isogeny. Both have the same local data at 4547:

| quantity | value |
|---|---|
| conductor exponent f | 2 |
| Kodaira type | III |
| v(Δ_min) | 3 |
| v(j) | 0, so potentially good reduction |
| j mod 4547 | 1728 |

The curves y² = x³ ± x (j = 1728) have a₄₅₄₇ = 0: #E(F_p) = p + 1 and #E(F_{p²}) = (p + 1)². Since 4547 ≡ 3 (mod 4), the potentially good reduction is **supersingular**, for whichever curve is optimal.

## 3. Conclusion

- Edixhoven's theorem gives **ord₄₅₄₇(c₀) = 0**.
- Mazur (p | c₀ ⇒ p² | 4N, with 4N = 2⁵·3·2243·4547²·5843) then gives **c₀ = 2^a**.
- For the streaming certificate (run report §3.3): c_E = u·c₀ with u ∈ {1, 2}, and the certificate needs c_E ≤ 399 575.
  - a ≤ 17 always suffices.
  - a ≤ 18 suffices if the seed is the strong Weil curve.
- The only remaining obstruction is **2¹⁸ | c₀**.

## 4. Status of the 2-part (sources read; nothing closes it)

- **CNS Theorem 1.2.** It gives val₂(c_φ) ≤ val₂(deg φ) + ε. Here ε = 1 only if val₂(N) ≥ 3 *and* no prime p′ ≡ 3 (mod 4) divides N. In our case 3, 2243, 4547 and 5843 are all ≡ 3 (mod 4), so ε = 0 and v₂(c₀) ≤ v₂(deg φ₀). The modular degree deg φ₀ is not computable at N ≈ 6.5·10¹⁵, so this gives no explicit bound.
- **Raynaud** (ARS 2006, Thm 2.4): 4 | c ⇒ 4 | N. This is vacuous here because 8 | N.
- **Edixhoven's E-independent bounds at 2, 3, 5, 7.** ARS 2006 calls them unpublished ([Edi89], his thesis); CNS footnote 3 refers to the unfinished manuscript [Edi01]. **Not used.**
- **Pasten's uniform bound.** Operator-supplied; not checked in this task.

## 5. Provenance and limits

- [Edi91] is Progr. Math. 89 (Birkhäuser, 1991), pp. 25–39. It is paywalled and was not read. The statement used is the one given identically in two published secondary sources, both co-authored by Česnavičius.
- Both PDFs are in `src/` with their text extractions (`CNS.txt`, `Ces18.txt`).

## 6. Resources

- Seconds of GP (under 100 MB).
- Two arXiv PDFs fetched as sources.
