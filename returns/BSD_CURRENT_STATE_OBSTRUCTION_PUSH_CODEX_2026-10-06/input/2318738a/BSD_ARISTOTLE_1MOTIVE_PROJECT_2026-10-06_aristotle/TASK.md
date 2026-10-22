# Task: the Ш-free Tame Law (G1)

Read `CURRENT_FRONTIER.md` first. It is the canonical state and replaces earlier state files in your project.

## Do not

- Redo G2 (auxiliary primes, biextension fullness, the Frobenius–regulator dictionary). It is proved; see `1_PROVED_STATE/G2/`.
- Search for auxiliary primes, work on `Deg`, or study the trace-two density.
- Prove another ν_p or Selmer bookkeeping equivalence.
- Compute or recompute any settled prime, or start any per-prime computation.
- Re-derive Theorem W, receiver exactness, the K288 residues, or the existence-form equivalence `link_iff_fin_and_kato`.
- Reopen any lane in `2_CLOSED_LANES/CLOSED_LANES.md` without a new mathematical input that changes its stated first failure.
- Use any of these as inputs: FIN, BSD, #Ш, dim Sel_p = 2, Ш[p] = 0, q = 36, or q ∈ ℚ (unless you prove it).

## The work

Attack G1 at the **residue level**. A successful return does one of the following.

- **(a) A construction.** Construct, without FIN, BSD or #Ш, a rational m ≠ 0 with s_p ≡ m (mod p) for all p outside a finite set. Alternatively, construct a residue-level law with such a mechanism, for example bounded units (s_p ≡ m·u with u in a fixed finite set) or finitely many candidate constants.
- **(b) An equivalence.** Prove that a specific, precisely stated version of G1 that you propose is equivalent to FIN-tail, or to FIN-tail ∧ (K). Name the step where FIN enters.
- **(c) A scoped negative.** Name the candidate, its first failing arrow, and the input that would change the verdict.

Note: "a form of G1 weaker than FIN-tail that still gives finite support" is impossible as stated, because anything sufficient for finite support implies FIN-tail (`3_LIVE_QUESTION/STATUS.md` §4). The useful weakenings are residue-level laws that are weaker than the exact Law.

## Admission test (run it before developing a construction; stop at the first failure)

Exhibit, before choosing p:

1. The object, defined over ℚ or ℤ[1/D], with no p in its definition.
2. No Ш, no BSD, and no assumption that q is rational.
3. Its degree-two (tame) realization gives C₂(p,ℓ), and not 0 = 0.
4. Its regulator realization gives G2's (a_ℓ − 2)·R_{p,ℓ}.
5. Exact normalization, not "up to an arbitrary p-unit".
6. A nonzero rational coordinate m.
7. Consistency with the eleven audited residues: s_p ≡ 288 at p = 5 (ℓ = 191, 311) and at p = 17, …, 47, under the convention in `CURRENT_FRONTIER.md` §1.7.
   - If the mechanism is general rather than seed-specific, it must also be consistent with the record's calibration K_E = 4c∞·Tam·#Ш/tors² (288 on the seed, 24 on the N = 2900 fiber, and 68/68 rows on six curves).

## Return format

- One STATUS line.
- Each claim labelled PROVED (with the proof or a Lean file), IMPORTED (with exact source and theorem number) or HEURISTIC.
- Lean files must build with no `sorry`. List `#print axioms` for every new theorem.
- End with "FIN, ORDER9 and Q36: unchanged" or a precise statement of what changed.
