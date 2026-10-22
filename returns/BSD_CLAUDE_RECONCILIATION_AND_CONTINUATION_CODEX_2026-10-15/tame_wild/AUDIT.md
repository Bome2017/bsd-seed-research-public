# Independent audit of the October 14 tame/wild experiments

Date: 2026-10-15. Author: Codex audit subagent. Originals were read only. No source coefficients or heights were regenerated, no theorem source was silently upgraded, and no publication was made.

**Verdict: the saved numerical arithmetic supports the three bounded experimental results. The universal-form, exact-global-constant, and route-exhaustion language requires correction. None of the four returns supplies FIN, ORDER9, Q36, or a new seed coefficient-prime exclusion.**

This is an independent reconstruction of arithmetic from saved raw outputs and a source-code/scope audit. It is not independent reconstruction of PARI modular symbols, the seed Fourier/Arb computations, the actual point multiples, or the retained arithmetic theorem chain.

## 1. What was checked

The executable audit is `check_saved_arithmetic.py`; results and exact input hashes are in `CHECKS.json` and `INPUT_BINDINGS.json`.

| Packet | Manifest entries matched | Independently reconstructed arithmetic |
|---|---:|---|
| `BSD_SEED_FULL_LEVEL_LAW_TEST_2026-10-14` | 100 | Seven complete tables, 622 plus symbols and 622 minus symbols, two primitive-root coordinates, point counts, determinant arithmetic from saved height entries |
| `BSD_TWO_LEG_TAME_EXPERIMENT_2026-10-14` | 27 | All 714 clean congruences, using 695 raw symbol-pair outputs; sealed height vectors were matched back to raw height output |
| `BSD_WILD_LEG_EXPERIMENT_2026-10-14` | 47 | Original failed candidate family, corrected post-hoc formula, all 386 fresh confirmation rows, forced coefficients, raw-height bindings and fresh-row disjointness |
| `BSD_TAME_LAW_PROOF_ATTEMPT_OPUS_2026-10-14` | No manifest supplied | Written claims and their logical scope; no new arithmetic proof is present |

The four present prediction digests match the current prediction files. This checks custody consistency, not an independently witnessed timestamp. The documents report that sealing preceded coefficient production; this audit does not supply external attestation of that chronology.

The control producer error logs inspected contain stack-growth warnings, not GP top-level errors. Their symmetry checks have their stated scope: the two-leg and mixed-wild producers check a bounded initial subset of representatives, whereas the pure-wild producer checks every representative used. This audit checks saved flags, not those source evaluations afresh.

## 2. Seed full-level test: retain the deeper congruences

I independently recovered every symbol from the printed decimal interval and the retained lattice `1/1024 Z`, without using the printed candidate fraction or uniqueness flag to choose its value. Every interval has exactly one lattice point; the label sets, plus/minus symmetry and integral plus values pass. The interval validity and lattice theorem remain retained inputs.

For the least primitive root the recovered residues are:

| Auxiliary prime ell | Odd modulus m | c2 mod m | K residue obtained by dividing by `(a_ell-2) R_ell` |
|---:|---:|---:|---:|
| 19 | 9 | 0 | 0 |
| 37 | 9 | 0 | 0 |
| 73 | 9 | 0 | 0 |
| 101 | 25 | 1 | 13 |
| 109 | 27 | 9 | 18 |
| 127 | 63 | 9 | 36 |
| 163 | 81 | 18 | 45 |

The denominator `(a_ell-2) R_ell` is a unit at each displayed full odd modulus. Both primitive-root choices give the same scalar residue, and both saved point multipliers give the same regulator. The scalar residues agree with 288. The independent point counts also agree with all seven saved traces.

For example, the exact recovered coefficients are:

* ell=101: `(c0,c1,c2)=(0,-44300,-1209274)`;
* ell=109: `(0,-6912,-208080)`;
* ell=163: `(0,-10044,-263718)`.

This is additional seed data at deeper augmentation moduli, including a nonzero valuation-two 3-adic leading coefficient. It tests a feature absent from the older depth-one rows. It is not an evaluation at a new coefficient prime: the only coefficient primes here are 3, 5 and 7. The retained Ota singleton checker accepts ell=127 for p=7, which was already covered. The other singleton reports are outside that checker's frozen prime/depth domain; those verdicts are not arithmetic failures of the full-level experiment.

### The global constant is not determined

These seven new rows jointly give only

`K == 288 (mod lcm(9,25,27,63,81))`, hence `K == 288 (mod 14175)`.

For example, the distinct integer **14463 = 288 + 14175** satisfies every scalar congruence in these seven rows. This does not contest the sealed value 288; it identifies the information actually obtained. Older rows give further congruences, not an automatic proof of one exact rational scalar or a fixed support bound.

The identity `288 = 32 * #Sha` in the proof-attempt report, lines 16 and 52, must be withdrawn as an established statement. What is available is the candidate scalar `288=32*9`, with a retained 3-primary result and the displayed congruences. Full ORDER9 remains open. Likewise, the fixed quotient 9 in other normalizations is not in conflict with 288: the raw omega1 convention and its factor 32 must remain attached.

### One real but nonblocking code defect

`eval/evaluate_full_level.py` says that reducing discrete-log exponents modulo odd m preserves the binomial coefficients used for k=0,1,2,3. This is true for the tested degree-two conclusion, but false in degree three when 3 divides m. For example, `binom(9,3)=84 == 3 mod 9`, whereas `binom(0,3)=0`.

The mismatch occurs in actual saved output, not only a synthetic example:

| ell, root | modulus | full-index c3 mod m | reduced-index c3 mod m |
|---|---:|---:|---:|
| 109, 6 | 27 | 0 | 18 |
| 109, 10 | 27 | 0 | 9 |
| 37, 2 | 9 | 0 | 3 |
| 37, 5 | 9 | 3 | 6 |
| 73, 5 | 9 | 6 | 3 |

The report uses c2, so its seven reported tests survive. Before reusing this evaluator for higher order, restrict the documented invariant calculation to k<=2 or derive the correct higher augmentation relations. Do not promote its c3 field to a coordinate-independent degree-three certificate.

## 3. Two tame legs: a successful determinant-shape test

The count is **1,333 height-screened pairs**, **1,378 (pair,q) prediction rows**, **695 actually evaluated symbol pairs**, and **714 clean congruence rows**. Nineteen extra congruence rows reuse a symbol pair at another q; these are not 714 independent source constructions.

The mixed coefficient agrees with

`K_E (a_l1-2)(a_l2-2) [h11*h22 + h21*h12 - 2*b1*b2] / (cexp^2*index)^2`

at all 714 rows. The 512 nonzero-mod-q comparisons, the pure coefficients, augmentation, linear terms and saved polarization checks also pass. Counts by q are 476 at 3, 134 at 5, 56 at 7, 27 at 11, and 21 at 13; mixed precision reaches 27 and 25. My implementation recomputed these values from raw coefficients and height vectors, not `mix_ok` fields.

The selected negative variants have the reported inferior pass counts: omitting both Euler factors 382/714, omitting one 313/714, wrong sign on the cross term 304/714, omitting the cross term 304/714, and negating the result 189/714. None of the 512 nonzero rows passes the negated formula. This is a discriminating finite test of shape and sign.

The algebraic form has a direct exact explanation:

`det(A X+B Y) = det(A) X^2 + (a*f+c*d-2*b*e) XY + det(B) Y^2`

for symmetric matrices `A=[[a,b],[b,c]]`, `B=[[d,e],[e,f]]`. Expanding both sides proves this identity. The arithmetic conjecture is that the actual modular-symbol leading coefficient is represented by these particular height matrices with this scalar; the matrix identity itself does not prove that comparison.

Accordingly, lines 43–51 of the two-leg report should say that **the tested rows support** the determinant shape of a common pairing, not that a universal global pairing or comparison has been constructed. Equality of the two polarization recipes on the sampled four points is a useful consistency check, but is not by itself a proof of a quadratic law on every lattice point.

## 4. Wild leg: genuine prospective confirmation after a failed first guess

The first sealed candidate family really fails: its best results are 5/24 pure rows and 38/110 mixed rows. The corrected factor `(a_p-1)^2` fits the original data and then passes the separate confirmation set:

* 98/98 pure rows, including 94 nonzero observations;
* 288/288 mixed rows, including 253 nonzero observations;
* 386/386 augmentation and first-order checks;
* 288/288 forced wild-square distribution checks.

There is no overlap between the 134 initial raw `(curve,p,ell)` coefficient keys and the 386 confirmation keys. Some curves recur and many rows share a curve and p, so freshness of rows must not be described as a wholly independent source implementation. The forced-square comparisons sometimes reuse the original pure-wild coefficient, as the confirmation code explicitly states.

The finite wild coordinate is well defined. For a unit modulo p^2,

`phi(u)=-(u^(p-1)-1)/p mod p`

is additive under multiplication, kills -1, and sends 1+p to 1. These follow by multiplying `1+p*a` expressions modulo p^2; the checker additionally verifies 34,616 unit cases over the sampled prime range. The degree-two norm sum `sum_{j=0}^{p-1} binom(j,2)=binom(p,3)` vanishes modulo p for p>=5. These elementary facts justify the finite coordinate and the applicable transfer cancellation; they do not supply a canonical Kato/ordinary-height comparison.

The newly fitted squared factor is consistent with the ordinary unit-root factor: `alpha^2*(1-alpha^-1)^2=(alpha-1)^2 == (a_p-1)^2 mod p`. Matching the finite theta coefficient and canonical heights still requires the stated interpolation/source conventions. The report's description of an actual p-adic class and the tame classes as one proved form is too strong: it has produced a successful finite-level comparison on controls, not a new cohomological identification.

The stated restrictions matter: control curves only, a1=0 models, good ordinary non-anomalous p, depth one modulo p. No supersingular data, unresolved seed coefficient, or higher-precision seed coefficient/height ratio is supplied. In particular, a mod-p determinant-zero row cannot decide the next valuation digit required at a nonunit regulator.

## 5. Normalization and source independence

The numerator producer and height producer are separate: the coefficient sums do not receive the predicted regulator or Sha value. That is a useful experimental separation. However, they use shared PARI routines, and the raw scalar calibration is numerical:

* `s2_sym2.gp` and `confirm/s2_confirm.gp` compute Birch ratios at auxiliary levels using floating-point L-values;
* `bestappr(real(ratio),10^4)` selects `kap` and the code checks agreement within 1e-25;
* every printed `kap` here is 1, with much smaller displayed errors;
* rational modular-symbol sums are then exact **conditional on that normalization**.

These are strong numerical calibration checks, not interval-certified proofs of the real-period scaling. The audit therefore does not label the control computations fully certified arithmetic proofs. This is a scope boundary, not evidence that their normalization is wrong.

The predicted control constant is programmed as `4*c_infinity*Sha_an*Tamagawa/torsion^2`; the tables use `Sha_an=1`. Thus these runs test whether source coefficients reproduce a specified expected constant. They do not construct a Sha-independent predictor of that constant. They also do not include the independently established positive odd-primary-excess control discussed in the user's earlier work. The seed full-level experiment does include the retained nontrivial 3-primary calibration, but it does not determine the remaining seed support.

## 6. Claims that should not become permanent walls

The primary decomposition of finite abelian groups makes cross-primary tensor products vanish. It explains why the displayed coefficient comparisons can be checked one q at a time, and why finitely many congruences do not determine a rational constant without further information. It **does not prove** that every arithmetic method using finite-level objects is incapable of imposing cross-prime constraints. A uniformly proved integral identity, an independent global index bound, or a uniform correlated valuation estimate would be additional arithmetic information, not a contradiction to that decomposition.

The two-leg report's lines 55–61 and wild report's line 33 should therefore be qualified. A compatible family of local residues need not be the diagonal image of a rational number; showing that it is would require new input. This is a limitation of the supplied evidence, not a theorem prohibiting future finite-level arithmetic constructions.

The proof-attempt report also cannot infer from its list of candidate failures that:

* every global rank-two object with a useful formula must be absent;
* a second-derivative Gross–Zagier formula is the only way to prove the tame law;
* a sufficient tame FIN identity is mathematically equivalent in difficulty or implication to Q36;
* every possible uniform estimate must first produce a p-independent rational scalar.

Its narrower conclusion is sound: **the candidates discussed there did not supply the missing seed comparison.** The report itself is labelled analysis rather than theorem. Its individual literature claims were not exhaustively re-audited here, and its cited retained Stage A/W/K inputs were not re-certified.

As a targeted primary-source cross-check, Bullach–Honnor's current paper, Introduction Remark 1.8(b), explicitly distinguishes its result from the finer positive-rank congruence and describes additional height/comparison input for the latter. That confirms that the paper's title is not a ready-made proof of the tested rank-two identity. Source: [On the refined Birch–Swinnerton-Dyer type conjectures of Mazur and Tate](https://dominikbullach.github.io/MazurTate.pdf), pp. 4–5, accessed 2026-10-15. This is a source-scope check, not a new comprehensive literature survey.

## 7. Correct retained state and continuation relevance

Retain three finite experimental facts:

1. The seven deeper seed tables agree with the predicted 288 law in the specified omega1 convention.
2. The two-leg control data discriminate in favor of the determinant cross term and both tame Euler factors.
3. The failed initial wild factor was repaired to a squared factor that passed genuinely new coefficient rows.

These constrain the shape and normalization an eventual arithmetic comparison must reproduce. They are not proof that its missing scalar or content is uniformly bounded. Another formula that inserts `Sha_an` as its constant would test the same prediction rather than supply the requested independent bound.

The admissible next discovery step must bring an independently controlled source or upper-bound mechanism and use these rows as held-out constraints. It must handle the existing positive-excess controls and the seed's nonunit-regulator configurations rather than only reproduce unit-Sha control rows. This audit does not select or claim to have constructed that source.

**Endpoint ledger:** FIN unchanged; ORDER9 unchanged; Q36 unchanged; exceptional-primary obligations unchanged; seed coefficient-prime coverage unchanged. No universal impossibility conclusion follows.

## Source pointers

* Seed: `REPORT.md`, `PREDICTIONS_SEALED.md`, `PRE_RUN_CLARIFICATION.md`, `eval/evaluate_full_level.py`, `eval/regulator_gmpy2.py`, `eval/regulator_independent.jsonl`, seven `production/l*/msl.txt` and `SINGLETON_REPORT.json` files.
* Two-leg: `REPORT.md:7–67`, `scripts/seal.py`, `scripts/s1_reg2.gp`, `scripts/s2_sym2.gp`, `scripts/lib_tl.gp`, `outputs/reg2.txt`, all `outputs/sym2_*.txt`, `predictions.json`.
* Wild: `REPORT.md:6–37`, `confirm/RULE.md`, original and confirmation sealing/producing/evaluating scripts, raw height and symbol outputs, both prediction JSON files.
* Proof attempt: `REPORT.md:13–16`, `:30–52`, `:54–61`.

Original roots remain unchanged. The accompanying executable writes only into this audit directory.
