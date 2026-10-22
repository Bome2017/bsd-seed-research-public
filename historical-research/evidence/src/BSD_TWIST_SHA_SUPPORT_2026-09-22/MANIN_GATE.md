# MANIN / DENOMINATOR GATE — verdict: `MANIN_DENOMINATOR_BOUND_MISSING`

Date 2026-09-22. But the gap is a **citation** gap with a named source, not a mathematical one. See §5.

---

## 0. My error, first

`SAGE_KATO_CHECK.md` §5 said that if `Supp(c) ⊆ {2, 7, 4547}` then "`v_p(#Sha_an)` would be unchanged for every
other `p`." **That inference is invalid and is withdrawn.** A rational near 49 with denominator `7^k` has a
*numerator* that may be divisible by any prime whatever. Knowing the prime support of the *denominator* says nothing
about the prime support of the resulting value. Prime support of `c` and size of `c` are different questions, and
only the second controls the rational reconstruction.

## 1. Step 1 — ARS Cor. 3.7, source-checked. FROZEN.

Agashe–Ribet–Stein, *The Manin Constant*, PAMQ 2 (2006), verbatim:

> **Corollary 3.7.** If `A = A_f` is an optimal newform quotient of `J_0(N)` and `` ` | c_A `` is a prime, then
> `` ` = 2 `` or `` `^2 | N ``.

(Generalising Theorem 2.3, Mazur [Maz78, Cor. 4.1]: `p | c_E ⟹ p² | 4N`.) For
`N_{-7} = 2^3 · 3 · 7^2 · 2243 · 4547^2 · 5843` the odd primes with `q² | N` are `7` and `4547`, so

    Supp_odd(c) ⊆ {7, 4547}

and therefore **every BLV-admissible `p` (`p >= 5`, `p ∤ N`, `p ∤ disc K`) satisfies `p ∤ c`.** Frozen.

## 2. Step 2 — Edixhoven at `4547`. The type-III prime is ELIMINATED.

Edixhoven [Edi91] (published): for additive `p > 7`, `ord_p(c) = 0` **unless** `E/Q_p` has potentially **ordinary**
reduction of Kodaira type II, III or IV.

`4547` is type III, so the exception is live *only if the reduction is potentially ordinary*. It is not. Since
`v_{4547}(j) = 0` the reduction is potentially good, so the reduced curve has `j̄ = j mod 4547`, and Sage gives

    j mod 4547 = 1728,   curve with that j over F_4547 has a_q = 0   =>  SUPERSINGULAR

The mechanism is the classical one: `j = 1728` is the CM-by-`Z[i]` invariant, supersingular mod `q` exactly when
`q ≡ 3 (mod 4)` — and `4547 = 4·1136 + 3`. So `4547` is potentially **supersingular**, the type II/III/IV exception
does not apply, and

    4547 ∤ c        =>        Supp_odd(c) ⊆ {7}

At `q = 7`: `j mod 7 = 4`, `a_7 = 2`, **not** supersingular, so potentially ordinary — and `7` is not `> 7`, so
[Edi91] does not reach it regardless. `7` survives, exactly as predicted.

## 3. Step 3 — the strongest bound on `v_7(c)`: it exists, and it is UNPUBLISHED

ARS §2, verbatim:

> "B. Edixhoven also has unpublished results (see [Edi89]) which assert that the only primes that can divide `c_E`
> are 2, 3, 5, and 7; **he also gives bounds that are independent of `E` on the valuations of `c_E` at 2, 3, 5, and
> 7.** His arguments rely on the construction of certain stable integral models for `X_0(p^2)`."

`[Edi89]` = **B. Edixhoven, *Stable models of modular curves and applications*, Thèse de doctorat, Utrecht (1989)**,
which ARS cite with a URL at `maths.univ-rennes1.fr/~edix/publications/`.

So an `E`-independent bound on `v_7(c)` **does exist in the literature**, in a doctoral thesis that ARS classify as
unpublished. No refereed exponent bound at `p ≤ 7` was located. Other published results checked and found not to
help here: Thm 2.4 (Raynaud) `4 | c ⟹ 4 | N`; Thm 2.5 (Abbes–Ullmo) `p | c ⟹ p | N`; Thm 3.11
`` ` | c ⟹ `^2 | N or ` | m_A `` — at `` ` = 7 `` the first disjunct already holds, so it adds nothing.

## 4. Step 4/5 — exactly how much precision each bound would need

`L_ratio = L/(2 ω_1)` is pinned by rational reconstruction iff `2 · halfwidth(L_ratio) < 1/D`, i.e.
`halfwidth(L) < ω_1/D`, where `D` is the denominator bound. Sage uses `D = C = 8dt = 32` **assuming `c <= 2`**.
Taking the denominator to scale with the extra factor from `c` (see the caveat below):

    NOW (120 segments, halfwidth(L) = 5.07e-5):   max pinnable D = 226
      => tolerates 32·7^1 = 224  -- i.e. v_7(c) <= 1, and only barely (margin 1.01x)
      => 32·7^2 = 1568 already FAILS

| segments | `T` | halfwidth(L) | max `v_7(c)` handled | cost |
|---:|---:|---:|---:|---:|
| **120** | 2,013,265,919 | 5.07e-5 | **1** | done |
| 179 | 3,003,121,663 | 9.04e-10 | 6 | ~6 min |
| 239 | 4,009,754,623 | 1.33e-14 | 12 | ~8 min |
| **299** | 5,016,387,583 | 1.95e-19 | **17** | **~11 min** |
| 418 | 7,012,876,287 | 4.88e-29 | 29 | ~15 min |

**So the user's "extra precision does not solve an unbounded-denominator problem" is right, and the converse is also
worth stating: extra precision solves any *bounded* one, cheaply.** Since Edixhoven's bounds are described as
*independent of `E`*, they are very unlikely to exceed 17. A ~11-minute rerun would almost certainly close it — but
only once the bound is in hand.

**Caveat on this table.** Sage's `C = 8dt` is derived *under* `c <= 2`; I have assumed the bound scales linearly in
the extra factor from `c`. The exact dependence of the denominator bound on `c` was **not** verified at source, and
should be before the rerun is used as a certificate.

## 5. Step 6 — direct modular-symbol computation is hopeless here

`N_{-7} = 318,656,212,624,190,616 ≈ 3.19e17`. The modular symbol space at that level has dimension on the order of
`N/12 ~ 2.7e16`. No implementation — Sage, PARI's Pollack–Stevens overconvergent symbols, or anything else — computes
at that level; this is not an efficiency question. Sage's own `L_ratio` failure was a PARI stack overflow at
`2·isqrt(N) ≈ 1.13e9` summation terms, which is the *easy* half. **No resource estimate is warranted; the route is
closed.** Our certified Arb streaming computation is the only viable way to the `L`-value here, and it already ran.

## 6. Verdict and ledger

    MANIN_DENOMINATOR_BOUND_MISSING

with the qualification that the missing bound is *named and locatable*: Edixhoven's 1989 Utrecht thesis.

    MANIN_PRIME_SUPPORT        = SETTLED.  Supp_odd(c) ⊆ {7}.   [ARS Cor 3.7 + Edixhoven Edi91 at 4547]
    4547_ELIMINATED            = YES, potentially supersingular (j ≡ 1728, 4547 ≡ 3 mod 4)
    p ∤ c FOR ADMISSIBLE p     = FROZEN
    v_7(c) BOUND               = EXISTS but UNPUBLISHED ([Edi89], Utrecht thesis)
    MANIN_DENOMINATOR_SIZE     = THE LAST FIXED-TWIST GAP
    L_RATIO = 392              = conditional on c <= 2 (equivalently v_7(c) = 0 and v_2(c) <= 2)
    #Sha_an = 49               = same condition
    TWIST_SHA_SUPPORT ⊆ {7,4547} = same condition
    ORDINARY_BRIDGE            = NOT CLOSED

**Do not write `Sha(E^{-7}/Q)[p^inf] = 0` for admissible `p` yet.** The honest status is the user's:
`MANIN PRIME-SUPPORT = SETTLED; MANIN DENOMINATOR SIZE = LAST FIXED-TWIST GAP.`

## 7. What would close it, in order of cost

1. **Obtain `[Edi89]`** and read off the bound on `v_7(c)` (and `v_2(c)`). ARS give a URL. Cheapest by far.
2. Verify at source how Sage's denominator bound scales with `c` (§4 caveat).
3. If `v_7(c) <= 17`, rerun the certificate at 299 segments (~11 min) and redo the reconstruction.
4. Only then does `Sha(E^{-7}/Q)[p^inf] = 0` for every BLV-admissible good-ordinary `p` become writable — and the
   ordinary branch collapses to `[c_2] != 0` alone.
