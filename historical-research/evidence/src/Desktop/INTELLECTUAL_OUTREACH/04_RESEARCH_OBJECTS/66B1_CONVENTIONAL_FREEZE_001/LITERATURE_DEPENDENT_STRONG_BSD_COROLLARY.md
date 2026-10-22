# Strong BSD for the 66b1 family — a literature-dependent corollary

```text
STRONG_BSD_VIA_BH_2_13 = LITERATURE_DEPENDENT_COROLLARY
```

**Kept deliberately separate from the elementary descent theorem.**  It is not a consequence of the
descent alone and must never be merged into `THEOREM_STATEMENT.md`.

## The claim

The second referee independently found that, **after** `BSD(E_q, 2)` is established by the frozen
conventional result, Banwait–Huang arXiv:2601.16044v3 **Theorem 2.13** appears applicable to this
family and upgrades it to full strong BSD.

## Everything that qualification rests on

- Banwait–Huang v3 is a **public preprint**, marked to appear at ANTS XVII.  Its Remark 2.11
  discloses dependencies on further public-but-unpublished preprints.
- Applicability was checked by the referee against Theorem 2.13's hypotheses; the checked hypotheses
  and source locations are preserved in `02_second_referee/`.
- This is therefore an upgrade **conditional on that preprint and its stated dependencies**, not an
  all-published theorem chain.

## What is separately recorded as NOT applying

```text
BANWAIT_HUANG_CASE_3 = DOES_NOT_APPLY     (their Lemma 2.14 case (3), for E(Q)[2] ≅ Z/2Z)
BSTW_10_12_ROUTE     = DOES_NOT_APPLY     (literal Theorem 10.12 additionally fails a₃(E) = 0)
BSTW_PERIOD_CONVENTION = AMBIGUOUS        (the inspected passages do not fix its component factor)
```

The Theorem 2.13 route is a *different* route from BSTW 10.12 and from BH case (3); it is the only
one of the three the referee found applicable, and only after BSD(2) is in hand.
