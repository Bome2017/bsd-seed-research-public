# K-A1 verdict table (Lane A1, Opus, 2026-09-29)
(i) = mod p (non-archimedean); (ii) = uniform in p for a FIXED form; "Obj" = does the statement concern order-p
twists at the trivial-character jet of depth >= 2 (the F2 object)? Level: T = theorem statement read at source;
S = author's survey restatement; A = abstract only (TRIAGE). Details and quotes: SRC_*.md.

| # | source (grade, level) | (i) | (ii) | Obj | first failing condition (verbatim fragment) |
|---|---|---|---|---|---|
| 03 | Fearnley–Kisilevsky–Kuwata 0711.1771 (THM, T) | yes | yes | depth 0 | "such that L(E, 1) != 0" (seed: L(E,1) = 0) |
| 16 | Kriz–Nordentoft 2310.20678 Thm 1.4/Cor 5.20 (PREPRINT, T) | yes | no | depth r(p), r(p) uncontrolled | hypothesis is the "mod p Kurihara Conjecture" at that p; ">>_{E,p}" |
| 16 | Kriz–Nordentoft Cor 1.5 (PREPRINT, T) | no (as stated) | density 1 | as above | "for 100% of primes p"; conclusion L(E,chi,1) != 0 |
| 19 | BCGS 2312.09301 Thm C / Cor C (THM, T) | yes | ordinary non-anomalous p only | corank level | "ord(kappa^Kato) = r_str(E/Q)" |
| 18 | Burungale–Hida–Tian 1712.02148 (PREPRINT, T) | yes | yes | no (order prime to p) | "(i) p ∤ h_K"; statement on "X(E/H_K)^chi" |
| 04 | Ono–Skinner, Ann. 1998 (THM, T) | yes | yes | no (quadratic) | "fundamental discriminants D for which ... L(f_D, k)" |
| 07 | Chida–Hsieh 1204.2427 Thm D (THM, T) | yes | yes in reduction prime | no (p-power order, p != l) | "l ∤ pN D_K" with "chi : Gamma^- -> mu_{p^inf}" |
| 05 | Brakočević 1010.6066 (PREPRINT, T) | yes | partial (split p outside S(N,l)) | no (l-power order) | "anticyclotomic characters chi of l-power conductor" |
| 07 | Chida–Hsieh Thm C (mu = 0) (THM, T) | yes | no | depth 0, tower | p fixed; "the Iwasawa mu-invariant of Theta_inf vanishes" |
| 06 | Vatsal 2003 via ICM survey (THM, S) | yes | no | depth 0, tower | "characters chi of conductor p^n, as n -> infinity" |
| 08 | Hamieh 1302.3249 (THM, T) | yes | no | depth 0, tower | "We fix a prime ideal P of F"; "n >> 0" |
| 01 | Lee–Sun 1902.06277 Thms B, D, E (THM, T) | yes | no | depth 0 values | "Let N >= 3 and p ∤ 2N"; limit "M -> infinity" |
| 02 | Constantinescu–Nordentoft 2010.12403 (PREPRINT, T) | yes | no | depth 0; N | q | "as Q -> infinity"; outcome space needs "N | q" |
| 09 | Kim–Kim–Sun 1709.05780 (THM, T) | yes | no | Kurihara numbers | Conj 1.8 per lambda: "delta~_n != 0 in F_lambda" |
| 17 | Kriz–Nordentoft 2507.01836 (PREPRINT, T) | yes | no | moments, tower | fixed good p; "n large enough" |
| 10 | Petridis–Risager 1703.09526 (THM, T) | no | — | — | "standard normal distribution" |
| 11 | Bettin–Drappeau 1903.00457 (PREPRINT, T) | no | — | — | "equidistributed according to a stable law" |
| 12 | Nordentoft 1812.08378 (THM, T) | no | — | — | "standard complex normal distribution" |
| 13 | Nordentoft 2105.09130 (THM, A-level beyond (i)) | no | — | — | complex "weak simultaneous non-vanishing" |
| 15 | Dasgupta–Khan 2502.19566 (+Chinta, S) | no | — | — | "L(f (x) chi, 1/2) != 0" |
| 14 | Mazur–Rubin 1910.12798 (CONJECTURES, T) | no | — | — | Conj 10.1: "{chi in C : L(E, chi, 1) = 0} is finite" |
| 20 | 17 triage rows (secondary or abstract only) | — | — | — | UNCHECKED; not exclusions |

## K-A1 outcome
No theorem read meets (i) AND (ii) for the F2 object. The two rows meeting (i) and (ii) with order-p characters
of conductor prime to p are FKK (depth 0, needs L(E,1) != 0) and, at density one only, Kriz–Nordentoft Cor 1.5
(archimedean conclusion; valuation bound r(p)/(p-1) with r(p) not bounded). Rows meeting (i) and (ii) in full
(Ono–Skinner, BHT, Chida–Hsieh D) use characters of order prime to p, so they concern other Sha-components.
