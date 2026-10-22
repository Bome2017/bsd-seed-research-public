# TWIST-SHA SUPPORT — two-stage hostile audit. Fixed curve.

You are an independent hostile mathematical referee. This runs in **two stages** and the order is binding.

---

# STAGE I — GENUINELY BLIND fixed-curve audit

**Do not open `STAGE_II_ONLY/` until you have frozen a Stage I verdict.** It contains prior work on an adjacent
question **and the BSD quotient for this curve**. Opening it early destroys the independence this audit exists to
provide.

> **BINDING RULE.** Freeze the unconditional `p`-support theorem verdict **before forming or consulting the BSD
> quotient.** The real period is withheld for that reason. Do not reconstruct it, do not look it up, and do not
> estimate the quotient from the data you have. Only after your Stage I verdict is written may you open
> `STAGE_II_ONLY/`, read the prediction, and compare. Report explicitly whether you complied.

Read `READ_FIRST/` and `PRIMARY_SOURCES.md`. Read `GATE.md` before proposing anything.

## I.A — the main question

`E^{-7}/Q` is the quadratic twist of the seed by `D = -7`. The following are **certified inputs**, not conjectures
(`READ_FIRST/FREEZE.md` §1, full record in `READ_FIRST/D7_CERTIFICATE.md`):

    L(E^{-7}, 1) in [9.054319, 9.054421],   so  L(E^{-7},1) != 0
    rank E^{-7}(Q) = 0
    Sha(E^{-7}/Q) is FINITE
    #E^{-7}(Q)_tors = 2

> **Determine, by existing unconditional arithmetic, whether the prime divisors of `#Sha(E^{-7}/Q)` can be
> restricted or eliminated.**

Specifically: is `Sha(E^{-7}/Q)[p^inf] = 0` proved for **all `p >= 5`**, for **all but an explicit finite set**, or
only for an **ineffective** finite complement?

Audit every applicable tool and say what each does and does not give here:

* torsion and isogeny structure; rational isogenies and isogeny descent if any exist;
* Tamagawa numbers and reduction data — `READ_FIRST/FREEZE.md` §5-§6 give `c4`, `c6`, `Delta`, valuations,
  minimality, the minimal model, Kodaira types, `prod_v c_v = 32` and the torsion, all computed with PARI. The real
  period is deliberately withheld (see the binding rule). Verify the rest independently if you wish; say which
  hypotheses they do and do not satisfy;
* mod-`p` Galois representations: image, reducibility, Eisenstein primes;
* Kolyvagin and Kato: what the analytic-rank-zero machinery bounds, and at which `p` it is effective;
* Iwasawa-theoretic `p`-part results at analytic rank 0 (e.g. Kato divisibility with Skinner–Urban, and the
  ordinary **Eisenstein** case), with their exact hypotheses checked against this curve;
* visibility and congruence criteria;
* explicit `p`-descent or Selmer computations that could be certified at this conductor;
* any theorem converting a **certified central value** into `p`-part information *without assuming BSD*.

**Hard constraint:** do **not** infer `#Sha` from the BSD quotient `L/(Omega * prod c_v) * #tors^2` unless the
`p`-part of BSD for **this twist** has independently been proved at that `p`. Using BSD to bound `Sha` here is
circular with respect to the wider project. You may compute the quotient as a **prediction** and label it as such;
you may not promote it.

Freeze exactly one Stage I verdict:

    TWIST_SHA_PGE5_ZERO                     -- proved for every p >= 5
    TWIST_SHA_EXPLICIT_FINITE_SUPPORT       -- proved outside an explicit, listed finite set
    TWIST_SHA_COFINITE_ONLY                 -- only an ineffective finite complement
    FIRST_MISSING_THEOREM: <precise statement>

## I.B — the eigenspace question (independent of I.A)

The wider project needs `Sha(E/Q)[p^inf] = 0`, where `E` is the seed. Over `K = Q(sqrt -7)` and for odd `p`,

    Sha(E/K)[p^inf] = Sha(E/Q)[p^inf]  (+)  Sha(E^{-7}/Q)[p^inf].

Leading-term formulas of Bertolini–Darmon type compute the **full** order `#Sha(E/K)[p^inf]`, not the eigenparts.

> **Is there an eigenspace-refined leading-term statement that isolates the `+`-part?** That is, can the
> characteristic ideal / derived-regulator formula over the anticyclotomic `Lambda` be split under `tau`, so that a
> conclusion about `Sha(E/Q)[p^inf]` is obtained without controlling `Sha(E^{-7}/Q)[p^inf]`?

Note the obstacle before you start: under the anticyclotomic `Lambda`, `tau` acts as the involution `iota` rather
than commuting with `Lambda`, so `Char_p` does not obviously split into eigenparts. **This is an open question, not
a repair known to work.** A clean negative — an argument that no such splitting can exist, or that it would require
a specific unavailable input — is a fully acceptable and valuable answer.

Freeze: `EIGENSPACE_REFINEMENT_EXISTS` (with the theorem), `EIGENSPACE_REFINEMENT_OBSTRUCTED` (with the obstruction),
or `EIGENSPACE_REFINEMENT_UNKNOWN` (with the first missing input).

---

# STAGE II — only after Stage I is frozen

Now open `STAGE_II_ONLY/`. It contains two prior independent audits of an adjacent question, plus a reconciliation.

0. **First** read `BSD_QUOTIENT_PREDICTION.txt` and state plainly whether your Stage I verdict is stronger than,
   weaker than, or equal to what BSD predicts. The gap is a finding in its own right.
1. **Do not revise your Stage I verdict to match them.** If you change it, say explicitly what evidence changed it
   and quote the passage.
2. Those audits bound a saturation defect by `A_2 <= v_p(#Sha(E^{-7}/Q) * #E^{-7}(Q)_tors)` (one run) and by the
   `p`-adic **exponent** of `Sha(E^{-7}/Q)[p^inf]` (the other). **Check both.** Are they correct? Is either
   overstated? Is the exceptional set they derive the right one?
3. Both runs wrote that `v_p(R_der) >= 0` is "equivalently" `A_2 = 0`. The reconciliation demotes this to
   *sufficient, not equivalent*. Adjudicate.
4. Report whether your Stage I findings make their exceptional set **smaller, larger, or unchanged**.

Freeze: `PRIOR_BOUND_CONFIRMED`, `PRIOR_BOUND_OVERSTATED: <how>`, or `PRIOR_BOUND_REFUTED: <how>`.

---

## Deliverable

    STAGE_I_A   = <verdict>
    STAGE_I_B   = <verdict>
    STAGE_II    = <verdict>
    CHANGED_STAGE_I_AFTER_READING_STAGE_II = yes/no   (+ the passage, if yes)

Then a theorem-by-theorem justification. For any failure, state the **first** missing implication, not downstream
consequences. Early, well-scoped negatives are welcome.
