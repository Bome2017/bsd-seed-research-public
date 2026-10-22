# K288 raw custody audit: RESULT

Claude (Opus 5.5), 2026-10-06. $0: no new L-value computation; inputs are the nine certified singleton runs. Assignment: step 1 of Pro's 10-06 re-prioritization ("Raw K288 custody audit first"), relayed by the user.

**Best-case endpoint effect, stated before running:** it pins down the nine K288 residues under one stated convention, so that the W-identity attack (steps 2–3) has audited inputs. It does not move FIN, ORDER9 or Q36 by itself.

**Verdict: `K288_CUSTODY_CONFIRMED`.**
- **Inputs.** Each c₂ was recomputed from the raw certified symbol tables. Each tame regulator was recomputed in fresh code. One normalization was used throughout.
- **Residues.** w(p,ℓ) = c₂ / ((a_ℓ − 2)·R(p,ℓ)) ≡ 288 (mod p) at all nine (p, ℓ).
- **Combined.** By CRT the nine residues give exactly 288 modulo M = 17·19·23·29·31·37·41·43·47 = 20,475,850,236,047. Rational reconstruction returns 288/1, the unique rational with |a|, |b| ≤ 3,199,675 that fits all nine.
- **New today.** Three sealed extra checks from the same tables also match: p = 5 at ℓ = 191 and at ℓ = 311, and p = 3 at ℓ = 103.

## 1. One normalization for all nine

- **Curve.** The minimal model is [0,−1,0,−66020924,−65074271436]. The runs use y² = x³ − 22735x² + 106272484x, which is the same curve with u = 1 and r = 7578, so the Néron differential and the periods agree.
- **Symbols.** [a/ℓ]⁺ is the plus candidate divided by 1024, read from each run's certified `XB` line. This is the production normalization Re λ/ω₁, with ω₁ the least positive real period. All symbols are integers, and [a]⁺ = [−a]⁺.
- **Coefficients.**
  - g is the least primitive root mod ℓ, and ind_g(a) ∈ [0, ℓ−2].
  - c_k = Σ_a C(ind_g(a) mod p, k)·[a/ℓ]⁺.
- **Tame height.** For Q ≡ O (mod ℓ) with Q ∈ E⁰ at every bad prime, write x(Q) = a/d² and y(Q) = b/d³ in lowest terms. Then h(Q) = ind_g(−a/b mod ℓ) mod p.
- **Regulator.**
  - The Gram matrix is [[h₁, b₁₂], [b₁₂, h₂]] on Q_i = M·P_i, with b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2.
  - R(p,ℓ) = det / M⁴. Here M = cexp·exp(E(F_ℓ)) and cexp = lcm of the Tamagawa numbers = 2.
  - The frozen `tame_reg.gp` uses a different M (cexp·lcm of the generator orders). The agreement through w therefore also checks the M⁴ scaling.
- **Euler factor.** a_ℓ − 2 ≡ −#E(F_ℓ) (mod p) because ℓ ≡ 1 (mod p). Checked at all nine.
- **Basis.**
  - P₁ = (−3031, 327384) and P₂ = (−2394, 281520) are on the curve.
  - PARI `ellsaturation(E, [P₁,P₂], 50)` returns index 1, which covers every p in the table. Full saturation is the record's R.1/R.4/S.2.
  - PARI's Reg is 17.79651747249034.

## 2. The nine residues

| p | ℓ | a_ℓ | #E(F_ℓ) | g | c₂ (exact) | c₂ mod p | R(p,ℓ) | w | 288 mod p | how 288 entered |
|---|---|---|---|---|---|---|---|---|---|---|
| 17 | 103 | −2 | 106 | 5 | 46298 | 7 | 6 | 16 | 16 | fit (in-sample) |
| 19 | 191 | −10 | 202 | 19 | −30432 | 6 | 3 | 3 | 3 | evaluated after the result (inputs fixed earlier) |
| 23 | 47 | 4 | 44 | 5 | 103854 | 9 | 9 | 12 | 12 | fit (in-sample) |
| 29 | 233 | −14 | 248 | 3 | −98942 | 6 | 2 | 27 | 27 | forecast written during the run |
| 31 | 311 | 16 | 296 | 17 | 330990 | 3 | 17 | 9 | 9 | sealed before launch (4853a5fb…) |
| 37 | 149 | −10 | 160 | 2 | 762756 | 1 | 32 | 29 | 29 | sealed before launch (4853a5fb…) |
| 41 | 83 | −8 | 92 | 2 | −83420 | 15 | 19 | 1 | 1 | sealed before launch (4853a5fb…) |
| 43 | 173 | −22 | 196 | 2 | −227412 | 15 | 17 | 30 | 30 | sealed before launch (4853a5fb…) |
| 47 | 283 | −4 | 288 | 3 | 596378 | 42 | 38 | 6 | 6 | sealed before launch (ADDENDUM_2 2be68ea1…) |

- **The fit.** K was fitted on 17 and 23 on 09-26 (`mt_prescreen/MT_PRESCREEN.md`). The two fitted residues, 16 mod 17 and 12 mod 23, have least nonnegative CRT lift 288 mod 391.
- **The interpretation came later.** 288 was identified as 32·#Ш = 8q on 09-29 (lane NORM).
- **The archimedean side.** The record's R.6 gives 35.99427 < q < 36.00573, so 287.95416 < 8q < 288.04584. This open interval contains exactly one integer, 288.
- **Wording.** Codex's rule applies: "six PRE-RESULT forecasts matched" (29, 31, 37, 41, 43, 47).

## 3. Extra checks from the same tables (sealed before computing c₂)

`PREDICTION_EXTRA.md` (sha256 9791e0aa…) was written after the regulators were computed (`extra_rows.out`) and before any c₂ mod 5 or mod 3. Both steps were done in the same session, so the ordering is custodian-attested only.

| p | ℓ | a_ℓ | g | R | predicted c₂ mod p | certified c₂ | c₂ mod p | result |
|---|---|---|---|---|---|---|---|---|
| 5 | 191 | −10 | 19 | 1 | 4 | −4516 | 4 | MATCH (c₁ = −2860 ≡ 0) |
| 5 | 311 | 16 | 17 | 3 | 1 | −2804 | 1 | MATCH (c₁ = −1970 ≡ 0) |
| 3 | 103 | −2 | 5 | 2 | 0 | 168 | 0 | MATCH (c₀ = c₁ = 0; the whole element vanishes in F₃[C₃]) |

- **p = 5.** These are two new out-of-sample residues of the 288 law, at a prime where Ш[5^∞] = 0 is already proved. At p = 5 the record has Theorem W for pairs only, and G2 excludes 5 (Codex 09-29).
- **p = 3.** This check does not discriminate: 3 ∣ 288, and Ш[3^∞] ≅ (ℤ/3)² is proved.
- **(3, 283)** is not admissible, because 3 ∣ #E(F₂₈₃) = 288.

## 4. What was re-checked and what was taken as certified

**Re-checked, 9/9 runs:**
- `msl.txt` sha256 equals `RUN_MANIFEST.msl_output_sha256`.
- The msl's `AP_SEGROOT` equals the manifest's `pinned_segroot`.
- All 1,564 symbol lines have a unique candidate in both halves.
- The label set is (ℤ/ℓ)^×; every symbol is an integer and symmetric.
- c₀ = 0 and c₁ ≡ 0 (mod p).
- c₂ equals `SINGLETON_REPORT.json` exactly.
- R ≠ 0, and both polarization identities agree.
- w is unchanged under the second-least primitive root. Both c₂ and R scale by v², so this checks that the same g was used throughout.

**Fresh code:**
- `c2_from_symbols.py` does not import `recompute_downstream.py`.
- `tamereg_audit.gp` does not read `tame_reg.gp`.
- `assemble.py` does the CRT and the rational reconstruction.

**Taken as certified, not re-derived:** the symbol values themselves, i.e. the arbcore interval engine 47d07f2e… and the a_q corpus behind the pinned roots.
- 31, 43 and 47 have Codex's Batch C PASS.
- 37 and 41 were reviewed by Codex and by Pro.
- 17, 19, 23 and 29 still carry the record's qualifier "outside artifact-level review outstanding".

## 5. What this establishes, and what it does not

- **Establishes.**
  - The nine K288 residues reproduce from certified inputs under one stated convention. There is no per-prime sign, generator or normalization drift.
  - 288 is the only small-height rational that fits them.
  - The same law holds at p = 5 at two further auxiliaries.
  - Under these conventions the unit in Pro's step 2 is u_{p,ℓ} = 1 at all eleven nontrivial residues (nine, plus two at p = 5).
- **Does not establish** any theorem. "w_p ≡ 288 for all p" is the open cross-prime law; see `~/BSD_BUILD_MAP/K288_UNIFORMITY_ANALYSIS_2026-09-27.md`, as corrected by Codex.
- **FIN, ORDER9 and Q36 are unchanged.**

**For Pro's step 2.** With free p-units u_{p,ℓ}, the carrier statement is equivalent to a finite alarm set. Aristotle's `Frontier.exists_fixed_carrier_iff_finite_alarms` proves this, and it was recompiled here with standard axioms only. So the step-2 target is not circular only when it is read as the exact law (u = 1, or u in a fixed finite set). That is the law reproduced above.

## 6. Files (sha256)

| file | sha256 |
|---|---|
| c2_from_symbols.py | 58584347… |
| tamereg_audit.gp | f735769e… |
| assemble.py | abbd0a6d… |
| extra_rows.gp | 11215550… |
| c2_from_symbols.json | 5719830… |
| tamereg_audit.out | ea299417… |
| K288_AUDIT.json | 89adba43… |
| PREDICTION_EXTRA.md | 9791e0aa… |
| extra_rows.out | ecf6486d… |
| extra_c2.out | a126a127… |

Replay commands:

```
python3 c2_from_symbols.py
gp -q -D parisizemax=16000000000 tamereg_audit.gp < /dev/null > tamereg_audit.out
python3 assemble.py
```

The gp step takes about 51 s. Use PARI 2.17 from run040's sage-env.
