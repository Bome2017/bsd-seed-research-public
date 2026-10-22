# Can the seed's tame law be proved the way rank 0 and rank 1 were? (attempt, 2026-10-14)

Claude, Opus 5.5. Same-session written analysis using the record's citations and standard L-function factorizations; not
reviewed, not a theorem. FIN, ORDER9 and Q36 unchanged.

## 1. The target

For p ≥ 5 outside B* = {2,3,19,59,487,2243,4547,5843}, at one G2 auxiliary prime ℓ (ℓ ≡ 1 mod p, Frob_ℓ = −I on E[p],
R(p,ℓ) ≢ 0):

    c₂(p,ℓ) ≡ 288·(a_ℓ − 2)·R(p,ℓ)  (mod p).

Nonvanishing of c₂ alone gives Ш[p^∞] = 0 (Ota). Per prime, the law at one ℓ carries the same information as Ш[p] = 0 plus
one unit (Ota's criterion, Theorem W, G2; and the Lean link `link_iff_fin_and_kato`: existence form ⟺ FIN-tail ∧ (K)).
So the law can only beat FIN-tail through a proof that covers all p at once. Its new strength is that its constant is
visible and exact: 288 = 32·#Ш, confirmed at full level on the seed on 10-14 (`~/BSD_SEED_FULL_LEVEL_LAW_TEST_2026-10-14`).

## 2. The recipe rank 0 and rank 1 used, and where rank 2 stands

| Step | rank 0 | rank 1 | rank 2 (seed) |
|---|---|---|---|
| A. order of vanishing: θ_ℓ ∈ I^r | trivial | Kato's Euler system (Ota) | Kato's Euler system (Ota), imported |
| B. shape: leading coefficient = w·(a_ℓ−2)·(tame regulator), w independent of ℓ | Hecke relation Σ_a [a/ℓ]⁺ = (a_ℓ−2)[0]⁺, a formal identity | Euler-system / Kolyvagin structure | Theorem W, per p ∉ B*, Codex CONFIRMED_WITH_CORRECTIONS |
| C. w is one global number, the same for every p | w = [0]⁺ = L(E,1)/Ω, one modular symbol computed once (Manin) | one Heegner point y_K feeds the complex side (Gross–Zagier) and every p-adic side (Perrin-Riou, Kobayashi, Bertolini–Darmon–Venerucci) | **missing** |

The record's 09-18 hunt (`F4_SECOND_DERIVATIVE_RATIONALITY_HUNT.md`, rows C8, C12, "(D)") already found that the p-adic
Beilinson / Perrin-Riou comparison "is a theorem only for r = 1 … where one Heegner point feeds both the complex and the
p-adic" sides. So for the seed, steps A and B are in hand at the record's grades, and the whole problem is step C.

## 3. What step C needs, and why every known object fails it

Step C needs a global object, independent of p and ℓ, that (a) sees L(E,s) and (b) is nonzero in rank two.

| Candidate | Sees L(E,s)? | Nonzero in rank 2? | Status |
|---|---|---|---|
| modular symbol at the cusp 0 | yes | no: equals L(E,1)/Ω = 0 | fails (b) |
| Heegner point over K = Q(√−23) | yes, via L(E/K,s) | no: ord L(E/K,1) = 3, y_K torsion | fails (b) |
| derived Heegner points, Kolyvagin/Kurihara classes, level-raised forms, Gross points at fixed level | yes | yes | each auxiliary prime serves finitely many p (claim X.9): not global in p |
| Beilinson–Kato K₂ element | yes, at s = 2 | yes | reaching s = 1 is p-adic interpolation; derivative per p (MI-1, M10) |
| weight (2,2,2) diagonal cycles, Chow–Heegner points (Darmon–Rotger–Sols) | only for (f,g,g): L(f⊗g⊗g,s) = L(f⊗Sym²g,s)·L(E,s−1) | no: height ∝ L′ at the center, which is 0 when ord L(E,1) = 2 | fails (b); for g ≠ h they are global points on E but their heights are triple-product L′, unrelated to L(E,s) |
| weight (2,1,1) generalized Kato classes, (f,g,g*): V_g⊗V_g* ⊇ 1 | yes | yes | g of weight one is not cohomological: the class exists only as a p-adic limit, one prime at a time (Castella–Hsieh prefactor θ̄_p/h_p) |
| higher Gross–Zagier (Yun–Zhang; Feng–Yun–Zhang) | yes, r-th derivative | yes | function fields only: uses the everywhere-unramified constant-field direction, which Q lacks (record 10-07 Yun–Zhang reading) |

The pattern: over Q, every global object with a height formula yields a first derivative. In rank two those vanish. The
nonzero rank-two objects that exist are p-adic, one prime at a time.

## 4. Consequence

Step C for the tame law needs a second-derivative height formula over Q: a global object whose height is L″(E,1). That is
also exactly what Q36 needs (`BSD_Q36_MELLIN_COMPARISON_ATTEMPT_CODEX_2026-09-30/NEXT_COMPARISON.md`). So the tame law is not
easier than Q36 at the level of the missing idea. Its value is that it states, exactly and on the seed's own data, what such a
formula must output at every tame level: 288 = 32·#Ш times the tame regulator.

## 5. What would change this

Any one of these would reopen step C:
1. a number-field mechanism playing the role of Yun–Zhang's unramified derivative direction;
2. a global cycle over Q whose height is a second central derivative;
3. a theorem that the rank-two p-adic classes for different primes are realizations of one global class.

None is known in the record or in the 2026 papers screened on 10-13. Status: unsolved; no known method.
