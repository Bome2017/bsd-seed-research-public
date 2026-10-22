# BSD seed — frontier freeze

2026-09-22. Short by design. Not a master map; `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md` remains the
canonical mathematical record. This exists to stop future runs re-deriving the same obstruction under new vocabulary.

    E : y^2 = x^3 - 22735 x^2 + 106272484 x,    N = 2^3 * 3 * 2243 * 4547^2 * 5843

## 1. Proved endpoint data

* `rank E(Q) = 2 = ord_{s=1} L(E,s)`. RANK is **closed**. `E(Q) = <(0,0)> (+) Z P_1 (+) Z P_2`,
  `P_1 = (4547, 327384)`, `P_2 = (5184, 281520)`.
* Primary components settled: `Sha[2^inf] = 0`, `Sha[3^inf] = (Z/3)^2`, `Sha[5^inf] = Sha[7^inf] = Sha[11^inf] =
  Sha[13^inf] = 0`. All `PROVED_COMPUTER_ASSISTED` with the retained source/lattice/image qualifications.
* Under FIN: `#Sha = 9 t^2` with `gcd(t, 2*3*5*7*11*13) = 1`, so the conditional next possible order is
  **2601 = 9 * 17^2**. Sharp under these inputs via `(Z/3)^2 (+) (Z/17)^2`.
* Rigorous analytic side: `L''(E,1)/2 in [35.929604, 35.941023]`, `R in (17.79651747249034020748, ...039153)`,
  `q in (35.99427, 36.00573)`. Certified twist: `39.512236 <= L'(E^{-23},1) <= 40.182321`, hence
  `rank E(Q(sqrt -23)) = 3`.

**Prime ladder: stopped at 13.** Each further rung only moves the conditional threshold
`2601 -> 3249 -> 4761 -> 7569 -> ...` while never touching the infinite tail, at rising cost (cutoff `3.9e10` at
`p = 11`, `5.5e10` at `p = 13`, ~2.5 h each). Reopen only if a future theorem reduces the tail to a finite exceptional
set containing 17, or 17 becomes strategically special for an independent reason. The 13-run was worth doing; that does
not make 17 the next rational use of compute.

## 2. The two open obligations

1. **FIN** — `Sha(E/Q)` finite of order 9. Requires genuine control of the quotient `Sel_p(E)/(E(Q)/pE(Q))`; see §4.
2. **The real leading-term comparison** — `q = L''(E,1)/(2 Omega_E R) = 36`, equivalently `q = 4 #Sha`.

Both are open. Neither has a surviving candidate mechanism.

## 3. Route stops — one sentence each, with scope

| route | stop | scope of the stop |
|---|---|---|
| GL(3) / Eisenstein | yields `Hom(B_aut, F_p) -> Sel_p(E)` whose image is a selected subspace with nothing bounding the complement; separately `1 (+) rho_E` has irregular HT weights `{0,0,1}` | not a proof that no automorphic route exists |
| Saito-Kurokawa / GSp_4 | Berger-Betina Cor. 7.8 bounds the eigenvariety tangent **by** the Selmer dimension (`2 <= dim t <= 1 + s^2`), which cannot be inverted | a weight-2 carrier **does** exist (AIF 2022); irregular weight is *not* the obstruction here |
| RS2 cross-cusp kernel | constructive Fourier side terminates in Estermann / shifted-divisor special values with no regulator or Sha interface | **procedural** archive; the final continuation lemma was never closed, so this is not a nonexistence result |
| MCS / Heegner-Stark | `I_3(eps^Hg_{1,0})` has no evaluation method; the Heegner Λ-index provably does not determine it (explicit counterexample) | the comparison **is** applicable at `p = 13, 31, 41, 47, 71, 73, 101, 127, 139, 151` after the certified twist; this is open, not closed |
| WC / witness content | Theorem O1 makes the antecedent equivalent to the ordinary vanishing tail of FIN | an equivalence, not an impossibility |
| Visibility | varying ambient covers all classes but gives no horizontal bound; fixed ambient is equivalent to ordinary vanishing | no universal impossibility for unrelated fixed-level proofs |
| Scalar automorphic pairings | BROAD_CURVATURE_ORTHOGONALITY: `int_Y alpha_f ^ dJ = 0` for moderate-growth global scalar `J` | **kills only that class.** It does *not* close real-regulator comparisons generally, higher Green objects, arithmetic cycles, finite-place constructions, or nonlocal kernels |

## 4. Admission gate — what counts as controlling the quotient

The target is the **whole** unknown quotient

    Sha(E/Q)[p^n] = Sel_{p^n}(E) / (E(Q)/p^n E(Q)).

A candidate is admissible if it controls all of it, by **any** of:

* a bounded source **surjecting** onto it, `M_p ->> Sel_p(E)`;
* a bounded target **receiving it injectively**, `Sel_p(E) --> M_p`;
* bounded kernel **and** cokernel of a comparison map;
* an explicit annihilator;
* an exact sequence with the other terms controlled;
* an independently proved equivalent assertion.

**There is no arrow-orientation rule.** "Must map out of Selmer, not into it" is **wrong** and is withdrawn wherever it
appears — it would reject a valid bounded-target injection. The real defect in the killed automorphic routes was
**absence of coverage**: the image was a selected subspace and nothing bounded the complement. Diagnose coverage, not
direction.

> Correction notice: `~/BSD_ARISTOTLE_INVENTION_PACKET_2026-09-20/` ships this error as "Shape 1 — WRONG DIRECTION"
> in `KILLED_ROUTES.md` and trap 1 of `KNOWN_TRAPS.md`. That packet has already been run and returned; **it must not be
> reissued without replacing that rule with this section.**

## 5. Current computational capability

* **Certified fixed-prime pipeline.** Settles one primary component end to end in ~2.5 h on a 16 GiB / 20-core host,
  ~1 GiB peak RSS, with per-segment restart, independent integer witness verification, exact stage-C identities
  (segment root, count identity, symbol identification in `(1/1024)Z`, Hecke/`U_p` relations) and byte-level custody.
* **Coefficient corpus.** 3,281 verified segments of `2^24`, covering `T = 55,046,045,695`, hash-bound and reusable.
* **Certified twist `L'` evaluation.** Ball enclosure of the first derivative of a quadratic twist from the same
  corpus, with an explicit proved tail bound; demonstrated at `D = -23` in 708 s.
* **Record discipline.** Evidence grades (`PROVED` / `PROVED_COMPUTER_ASSISTED` / `CERTIFIED_NUMERIC` /
  `LEAN_CHECKED`), additive supersession rather than editing sealed artifacts, and manifest verification throughout.

## 6. Do-not-overclaim rules

1. **No arrow-orientation dogma.** See §4.
2. **No "p-adic work cannot supply FORMULA."** What is established is narrower: *no current p-adic-to-real comparison
   is available.* A future theorem comparing a p-adic leading term/regulator with the real Néron-Tate regulator could
   in principle bridge them.
3. **No "all duality impossible."** Global duality / Poitou-Tate, Cassels-Tate on this seed's rank-two basis, and
   simultaneous descent have never been attempted here.
4. **No "the family is exhausted."** Absence of a located theorem is not nonexistence. Every table entry in §3 carries
   its scope for this reason.
5. **No procedural archive reported as a theorem.** RS2 was stopped by a stopping rule, not refuted.
6. **A specialization is not the family.** Vanishing of one specialization does not imply vanishing of a Λ-adic object.
7. **Coincidence is not confirmation.** `1024^-1 = 4` and `(1 - alpha^-1)^2 = 4` agree in `F_13` with different roles;
   reading one as confirming the other produced a wrong residue.

---

Full BSD for this curve is **not** close. RANK is closed; the two obligations in §2 are open research problems, and the
durable output of the work so far is the precise knowledge of which approaches fail and exactly where — plus the
capability in §5. Nothing here authorizes a successor operation.
