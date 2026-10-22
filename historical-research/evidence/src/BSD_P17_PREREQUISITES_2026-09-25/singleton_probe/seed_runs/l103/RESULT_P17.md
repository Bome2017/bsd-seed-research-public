# Result: Sha(E/ℚ)[17^∞] = 0 (singleton Ota witness, p = 17, l = 103; 2026-09-26)

**Verdict: NONZERO,** the first of the three pre-registered outcomes. All bindings and checks passed, with zero failed
checks.

    c₂(θ₁₀₃) ≡ 7 (mod 17)   ⟹ (Ota, arXiv:1509.00682v1, Thm 1.5 / 6.4 with 5.17)   Sha(E/ℚ)[17] = 0   ⟹   Sha(E/ℚ)[17^∞] = 0.

**Curve:** E: y² = x³ − 22735x² + 106272484x, with N = 6503188012738584 and rank 2.

## Grade

- **The implication** was independently source-audited (`~/BSD_BUILD_MAP/pro6/SINGLETON_AUDIT_REPORT_PRO.md`, verdict
  SOUND_WITH_CORRECTIONS; all corrections implemented before the run).
- **The inputs** stay at their retained grades: rank 2 (R.1/R.4), residual images (A.3), the local data and
  Tamagawa 16 (A.1), and the Manin lattice (A.4).
- **The computation** is certified. Arb symbols are identified exactly in (1/1024)ℤ. The coefficients are
  verifier-proved (receipt root pinned in advance).
- **Overall:** computer-assisted, a published theorem applied, and a written deduction. It is not formalized in Lean.
- **Consequence for S.FIN.** Conditional on FIN, #Sha = 9t² with gcd(t, 30030·17) = 1. The next possible order above
  9 is **3249 = 9·19²**; it was 2601.

## Bindings, as enforced by the frozen checker (package commit 7248cf53…)

| item | value |
|---|---|
| PARAMS | `msl 0 -22735 0 106272484 0 103 6503188012738584 1 33218887679 16777216 …/p13/run/ap …/l103/units 1024`, equal to the frozen command line |
| receipt root (1,980 segments) | 5509573097647fcb6e7f92439bc707a0a894d2b0cc18f282974fb95eb4695a17, equal to AP_SEGROOT and to the pinned root |
| COUNT | smooth 10,808,527,050 + pairs 22,410,360,629 = 33,218,887,679 = T, identity 1 |
| symbols | 102/102 identified, labels exactly (ℤ/103)ˣ with each label once |
| engine | arbcore sha256 47d07f2e856e82d2…, equal to the freeze manifest |
| output | msl.txt sha256 cb7d4735b8e43e1a…, bound in RUN_MANIFEST.json |
| corpus | read-only: no coefficient file was modified during the run; Stage W was not run |

## Witness computation (generator g = 5, the smallest primitive root mod 103)

- c₀ = 0 exactly. This is the Hecke relation, with [0]⁺ = 0.
- c₁ = 7242 = 17·426 ≡ 0 (mod 17), as Ota 5.17 forces.
- c₂ = 46298 ≡ **7** (mod 17).

**Independent recomputation,** by separate code rather than the checker:
- the audit's formula 13·Σ C(ind₅(a) mod 17, 2)·h_a gives 7 (mod 17);
- over all 32 primitive roots, c₂ mod 17 takes exactly the values {3, 5, 6, 7, 10, 11, 12, 14}. That is 7 times the
  nonzero squares, as the u⁻² invariance predicts, and it is never 0;
- the plus and minus symmetry holds.

## Resources

- 1,654 s wall (27.6 min) on 8 threads.
- 13,094 CPU-s user, which is 3.64 CPU-h, under the 5.4 estimate.
- Peak RSS 737 MB.
- About 0.1 GB of new output.
- Start 14:26:39Z, end 14:54:13Z.

## Not claimed

FIN, ORDER9, Q36, and anything at the other primes. The depth-three route remains archived as the fallback, and it is
not needed for 17.
