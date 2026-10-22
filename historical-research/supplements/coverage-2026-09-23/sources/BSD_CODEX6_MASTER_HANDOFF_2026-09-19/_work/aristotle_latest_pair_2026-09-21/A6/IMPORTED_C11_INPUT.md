# Imported `C₁₁` input, and the one argument it unblocks

## 1. What was imported

From `ARISTOTLE_C11_RESULT.tar.gz` (supplied with this project):

```
C₁₁ := [T²] L₁₁(E, T) ≡ 8 (mod 11)      in the ω₁ convention
                        ≡ 4 (mod 11)      in the full-real-period convention Ω_E = 2ω₁
E : y² = x³ − 22735x² + 106272484x,   N = 2³ · 3 · 2243 · 4547² · 5843
```

with predeclared weighted sum `2(−110) + 3(−70) + 5(−10) + 6(102) + 7(−46) = −190 ≡ 8 (mod 11)`,
and the resulting qualified fixed-prime theorem

```
Ш(E/ℚ)[11^∞] = 0
```

under the packet's retained rank, full residual-image, modular-symbol-lattice, Manin-constant,
local-reduction and computational qualifications.

The execution blocker recorded in `C11_EXECUTION_BLOCKER.md` is therefore superseded; that file is
left unedited for provenance.

**Check actually run here.** The packet's own portable verifier (`verify_packet.py`) was executed
on the extracted packet and reported `PACKET_HASHES_PASS` and `EXACT_DOWNSTREAM_REPLAY_PASS:
C11=8 modulo11 (omega1), 4 (full real period)`. The arithmetic identity `−190 ≡ 8 (mod 11)` and
the weighted sum were re-checked directly.

**Trust boundary (as stated by the packet, and respected here).** That check is finite exact
arithmetic on imported certified symbols. The large numerical corpus (remaining coefficient
segments, witness files, Arb work units) stays in the originating local project and is only
hash-bound here, so the analytic inputs are imported computer-assisted results at the packet's
declared grade. Nothing about the analytic or arithmetic proof of `Ш[11^∞] = 0` is
Lean-verified. In every Lean statement in this project the `11`-primary vanishing appears only as
an explicit hypothesis `h11`; no axiom was added.

## 2. The existing argument this input completes

The one place where the prime `11` was load-bearing in the retained record is the **endgame
threshold argument**, not the assembly implication:

> `#Ш = 9t²` with `gcd(t, 210) = 1`, so the first admissible order after `9` is `9 · 11² = 1089`;
> hence `Ш` finite with `#Ш < 1089 ⟹ #Ш = 9`, and the threshold `1089` is sharp because
> `(ℤ/3)² ⊕ (ℤ/11)²` realises it with an alternating perfect pairing.
> (`THE_ENDPOINT.md` §"Why the threshold is 1089 and why it is sharp"; `PROVED_FACTS.md` §3;
> `record/MASTER_BSD_DAG.md` line 156; the countermodel in `RequestProject/TargetBCountermodel.lean`.)

That argument's missing premise was exactly the `11`-primary component: its sharpness witness is a
group with nonzero `11`-torsion. The imported input deletes the witness, and the argument then
continues by itself. The exact now-unblocked arrow is

```
Ш[11^∞] = 0   ⟹   the admissible-order gap moves from (9, 1089) to (9, 1521),
              ⟹   the sufficient bound for order nine relaxes from #Ш < 1089 to #Ш < 1521.
```

This is instantiated and machine-checked:

* `RequestProject/ThresholdGap.lean`
  * `SeedBSD.Gap.card_primaryPart_eq_factorization` — for a finite abelian group the `p`-primary
    order is the `p`-part of the group order (proved from Cauchy's theorem, not assumed);
  * `SeedBSD.Gap.card_eq_nine_or_ge_of_small_primes_vanish` — the gap theorem in the general form:
    if `#A[3^∞] = 9`, `A[p] = 0` for every prime `p ≠ 3` below a bound `q`, and every primary order
    away from `3` is a square, then `#A = 9` or `#A ≥ 9q²`. The bound `q` is a parameter, so each
    further settled prime advances the threshold with no new proof;
  * `SeedBSD.Gap.card_eq_nine_or_ge_1521` and `SeedBSD.Gap.card_eq_nine_of_card_lt_1521` — its
    instance at `q = 13`, the first prime not yet excluded: `#Ш = 9` or `#Ш ≥ 1521`, and
    `#Ш < 1521 ⟹ #Ш = 9`.
* `RequestProject/ThresholdSharpness.lean`
  * `SeedBSD.ThresholdSharpness.old_witness_has_eleven_torsion` — the record's sharpness witness
    `(ℤ/3)² ⊕ (ℤ/11)²` has nonzero `11`-torsion, i.e. it is excluded by the imported input;
  * `SeedBSD.ThresholdSharpness.threshold_1521_is_sharp` — `(ℤ/3)² ⊕ (ℤ/13)²` satisfies every
    retained input (including `11`-primary vanishing and square primary orders) and carries a
    nondegenerate alternating pairing on each primary part, with order exactly `1521`. So `1521`
    is the last improvement obtainable from the `11`-primary input alone.

Two consequences of the same computation, recorded because the record states them in the old form:

* the countermodel of `RequestProject/TargetBCountermodel.lean` (order `1089`, `C_E = 33`) is
  superseded: target (B) is still insufficient for order nine, but its minimal countermodel now has
  order `1521` with `C_E = 39`;
* `RequestProject/Assembly.lean` gains `card_eq_nine_of_torsion_free_from_thirteen`, the same
  retained implication with the outstanding universal premise starting at `p ≥ 13`. This is pure
  renumbering, recorded so the file does not state an overtaken premise; it is not offered as a
  result of this run.

## 3. What is *not* unlocked

* **FIN, order nine and `q = 36` remain open.** The outstanding arithmetic premise is unchanged in
  kind: `Ш[p] = 0` for every prime `p ≥ 13`, including the unresolved bad primes `2243`, `4547`,
  `5843`. Nothing here proves any instance of it.
* **No uniform theorem is inferred from the fixed-prime success.** The `p = 11` certificate is a
  fixed-prime computation; it gives no tail statement, and none is claimed.
* **No new route to FIN is opened.** The gap theorem strictly weakens the *sufficient bound* a
  future finiteness argument must reach (`< 1521` instead of `< 1089`); it does not supply such an
  argument, and under the retained inputs a bound below `1521` remains equivalent to order nine.
* **No next-prime calculation was launched**, and no engine was rebuilt: the packet's own portable
  check is the only computation run here.
