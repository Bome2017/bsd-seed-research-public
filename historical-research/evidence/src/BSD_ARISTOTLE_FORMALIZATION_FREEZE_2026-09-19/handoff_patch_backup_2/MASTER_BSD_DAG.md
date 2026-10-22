# MASTER_BSD_DAG — seed (2243,12), state of 2026-09-19

## 0. Immutable top level (THIS LIST MUST NOT GROW)

    FULL BSD(E)  =  RANK ∧ FIN ∧ FORMULA

    RANK     rank E(Q) = ord_{s=1} L(E,s)                                   PROVED_COMPUTER_ASSISTED — done (§1)
    FIN      Sha(E/Q) is finite                                             OPEN
    FORMULA  L″(E,1)/2 = Ω_E·Reg(E)·∏c_ℓ·#Sha(E/Q)/#E(Q)_tors²              OPEN
             ⟺ L″(E,1)/(2·Ω·Reg) = 4·#Sha      (∏c_ℓ = 16, #tors = 2)

Remaining top-level obligations: **FIN, FORMULA**. Every route-specific problem (p = 4547, supersingular primes, the
multiplicative primes, the large-p tail) is a node UNDER FIN. FORMULA presupposes FIN (it mentions #Sha).

## 1. RANK (closed)

    R.a  rank E(Q) = 2, E(Q) = Z/2 × Z·P₁ × Z·P₂                 PROVED (Zywina preprint + exact PARI 2-descent replay)
    R.b  L(E,1) = L′(E,1) = 0                                    PROVED
    R.c  L″(E,1)/2 ∈ [35.929604, 35.941023]                      PROVED_COMPUTER_ASSISTED (Arb)
    RANK ⟸ R.a ∧ R.b ∧ R.c

## 2. FIN and its sub-nodes

    FIN  ⟺  (∀p: Sha[p^∞] finite)  ∧  (Sha[p] = 0 for all but finitely many p)

Two ways to discharge FIN:

    (G) GLOBAL:  one theorem giving finiteness of Sha(E/Q) outright (as Kolyvagin/Kato do in analytic rank ≤ 1).   OPEN
    (P) PRIME-BY-PRIME:  the table below PLUS an effective tail theorem H(p₀).                                     OPEN

| node | statement | status | what closes it |
|---|---|---|---|
| FIN.2 | Sha[2^∞] = 0 | PROVED | — |
| FIN.3 | Sha[3^∞] ≅ (Z/3)² | PROVED_COMPUTER_ASSISTED (Skinner Thm A as printed; R1 carried; R2 remains OPEN as a provenance seam, narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N) | closing R2 would harden it |
| FIN.5 | Sha[5^∞] = 0 | PROVED_COMPUTER_ASSISTED (`P5_RIGOROUS_SHA5_ZERO_CONFIRMED`, sealed: node N7 upgraded from CERT-NUM to PROVED_COMPUTER_ASSISTED; a_{2,2} ≡ 2 mod 5 (ω₁), ord₅ a₂ = 0) | — |
| FIN.30 | #Sha[30^∞] = 9 | PROVED_COMPUTER_ASSISTED (from FIN.2, FIN.3, FIN.5; no CERT-NUM qualifier remains; inherits R1/R2) | — |
| FIN.ord(p), 7 ≤ p ≤ p₀ good ordinary | Sha[p^∞] = 0 | OPEN (decision procedure on paper; none run) | Kato + SW 6.1 per prime, ≈ 0.23·p² CPU-h |
| FIN.ss(p), good supersingular | Sha[p^∞] = 0 | SEMI_DECISION — CRITERION_SS PROVED (hostile gate `CRITERION_SS_VALID_WITH_CORRECTIONS`); no bit computed | depth-2 symbols [a/p²]⁺; ≈ 270 / 460 CPU-h at 23 / 29 (≈ 500 shared); fallback, not the global FIN route |
| FIN.2243, FIN.5843 | Sha[p^∞] = 0 at the multiplicative primes | COST_BLOCKED | Skinner Thm A + SW (split case needs L-invariant ≠ 0); ≈ 2·10⁴ / 10⁵ CPU-h (not re-derived) |
| FIN.4547 | Sha[4547^∞] = 0 | SEMI_DECISION + ROUTE_BLOCKED | no cyclotomic p-adic L-function, no IMC, no control theorem at this additive potentially supersingular prime; Kim Thm 1.8 witness n ≈ 8.1·10¹⁵ |
| FIN.tail = H(p₀) | Sha[p] = 0 for all p > p₀, p ∤ N | OPEN | F3: NOT_FOUND. Candidate mechanisms: LINE (FORMULATED); WC (Codex: the implication is PROVED, the antecedent J_E ≠ 0 is OPEN; weaker than LINE, NOT shown easier than FIN — `FIN_FRONTIER.md` §5) |

Which kind of global theorem would absorb which sub-node (from F2 §F.2 and the LINE audit):

| type of future theorem | good ord. | good s.s. | 2243, 5843 | 4547 | 2, 3 |
|---|---|---|---|---|---|
| (G) outright finiteness (any method) | yes | yes | yes | yes | yes |
| Kolyvagin type (all odd p with surjective ρ̄_p, p ∤ index) | yes | yes | yes | yes | not 2 |
| Kato / Iwasawa type (p ∤ N or p semistable) | yes | depends on a ± IMC | semistable: yes | **no** | no |
| Ota / Mazur–Tate / LINE type (R inverts p ∣ 6N) | yes | yes | **no** | **no** | no |

## 3. FORMULA and its sub-nodes

    FOR.num   L″(E,1)/(2ΩReg) = 36 ± 3·10⁻¹⁵                       CERTIFIED_NUMERIC (evidence only; NOT a rigorous ball)
    FOR.int   q_∞ := L″(E,1)/(2ΩReg) ∈ (35.99427, 36.00573)        PROVED_COMPUTER_ASSISTED (Arb L″/2 ball ÷ rigorous Ω·Reg;
              Codex REGULATOR_CERTIFICATE 2026-09-19, replayed identically by Opus)
    FOR.srat  q_∞ ∈ Q with reduced denominator ≤ 174                 OPEN (F4: NOT_FOUND; not an impossibility claim) — the MINIMAL target
              (historical CERT-NUM-level figures: L″/(ΩReg) ∈ (1/D)Z with D < 1.6·10¹⁴, and D < 3.3·10¹⁴ for q_∞. GPR_an and order-two
               Gross–Zagier are stronger candidate routes — FORMULA_FRONTIER §0.)
    FOR.alg   bounded algebraicity (Codex Lemma E)                   OPEN — incomparable alternative to FOR.srat (FORMULA_FRONTIER §0b(ii))
    FOR.B     one-sided common certificate B                         OPEN — gives FIN ∧ FORMULA together (FORMULA_FRONTIER §0b(iii))
    FORMULA ⟸ FIN ∧ (#Sha = 9) ∧ FOR.int ∧ (FOR.srat ∨ FOR.alg)     [the implication is PROVED; note that FIN ⇏ #Sha = 9]
    FIN ∧ FORMULA ⟸ FOR.B ∧ FOR.int ∧ FIN.3                          [the implication is PROVED]
    and conversely FIN ∧ FORMULA ∧ FOR.int ⟹ #Sha = 9 ⟹ every FIN.* node above with its predicted value.

Logic fixed by F4 §1 (keep): rationality alone is NOT enough; per-prime valuations cannot replace a denominator bound;
every first-derivative formula reads 0 = 0 on the seed; "(1,1)-type rank two" (L(E/K) = L(E)·L(E^K), both of order 1) is
not the seed's situation (one primitive L-function with a double zero).

## 4. The older computational decomposition (kept, demoted)

    FULL BSD(E)  ⟺  S3 ∧ S≥7 ∧ SRAT          (F2: TRUE in both directions, relative to the certified nodes)
    S3 := #Sha[3^∞] = 9 (now PROVED_COMPUTER_ASSISTED) · S≥7 := Sha[p^∞] = 0 ∀p ≥ 7 · SRAT := FOR.srat with value 36

This is a useful COMPUTATIONAL decomposition under the top level (S3 ∧ S≥7 ⟹ FIN with #Sha = 9; SRAT ⟹ FORMULA given that).
It is NOT the finish line, and its "roots" W1 (tail), W3 (4547) are sub-nodes of FIN; W2 = FOR.srat.

## 5. Candidate mechanisms attached to the DAG (none is a proof)

| mechanism | attaches to | status | file |
|---|---|---|---|
| LINE (one rational scalar a/b with b·δ_n = a·ρ_n at all core pairs, all good p) | FIN.tail, FIN.ord, FIN.ss | FORMULATED; Theorem C′ CONDITIONAL on it; stopping point known | `FIN_FRONTIER.md` §1 |
| WC — witness content (Codex 2026-09-19): J_E ∋ A ≠ 0 ⇒ Sha[p^∞] finite for all p ∉ S0, and zero for p ∤ A | FIN.tail, FIN.ord, FIN.ss | the implication is PROVED (conditional on Ota 5.17/6.4); the antecedent is OPEN; weaker than LINE; possibly FIN in Ota coordinates on the ordinary tail (Opus caveat; kill gate CODEX_QUESTIONS Q0). Its finite algebra is MACHINE-CHECKED: STATUS = CONDITIONAL, LEVEL = A1_FULL; the antecedent is NOT PROVED; FIN is UNCHANGED (A1 freeze) | `FIN_FRONTIER.md` §5 |
| other p-independent rank-2 Euler / Kolyvagin / Mazur–Tate object | FIN (G or tail) | OPEN | `FIN_FRONTIER.md` §2 |
| CRITERION_SS | FIN.ss | PROVED as a SEMI_DECISION (gate `CRITERION_SS_VALID_WITH_CORRECTIONS`, 2026-09-19); not run | `FIN_FRONTIER.md` §4; gate file |
| Ota per-prime certificate (one ℓ ≡ 1 mod p, leading term of θ_ℓ) | FIN.ord, FIN.ss | PROPOSED (cost UNVERIFIED) | `FIN_FRONTIER.md` §4 |
| Fouquet–Wan IMC (unpublished) | FIN.ss, FIN.4547 (decision instead of semi-decision) | PROPOSED (unrefereed preprint; not relied on by its co-author's later paper) | F2 §E′ |
| order-2 Gross–Zagier object; GPR/BKS with complex scalar | FORMULA (and FIN) | OPEN | `FORMULA_FRONTIER.md` |
| one-sided common certificate B (Codex) | FIN ∧ FORMULA | the implication is PROVED; no object has been constructed | `FORMULA_FRONTIER.md` §0b(iii) |
