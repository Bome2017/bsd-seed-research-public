# GATE

## K0. Stage order is binding
Do not open `STAGE_II_ONLY/` before freezing a Stage I verdict. If you do, say so explicitly in the return; a
silent violation invalidates the run.

## K1. Do not use BSD to bound Sha
The BSD quotient `L * #tors^2 / (Omega * prod c_v)` may be computed and reported as a **prediction**, clearly
labelled. It may **not** be used to conclude anything about `#Sha(E^{-7}/Q)` unless the p-part of BSD for this twist
is independently proved at that p. Using it would be circular with respect to the wider project.

## K1b. The prediction is supplied, and repeating it is a FAILED run
`READ_FIRST/BSD_QUOTIENT_PREDICTION.txt` contains the rank-zero BSD quotient formed from the certified `L`-value and
the computed local data. It is supplied because withholding a computed fact you would re-derive in a minute is
theatre, not blindness. It is **a prediction and nothing more.**

Your Stage I verdict is measured by the gap between that prediction and what is **proved**. Specifically:

* A verdict that merely restates the prediction, or that argues "the predicted support is excluded anyway, so we are
  done", is a **failed run**.
* You must state, for each `p >= 5`, whether `Sha(E^{-7}/Q)[p^inf] = 0` is *proved unconditionally*, and by which
  theorem with which hypotheses checked against this curve — independently of the prediction.
* If the unconditional result is weaker than the prediction, say so and quantify the gap. That gap is the finding.

## K2. Failure-to-find is not a theorem
If you cannot locate a result, return the missing statement. Do not convert "no such theorem was found" into "no
such theorem exists". This project has had to withdraw two verdicts for exactly that.

## K3. No standard-equivalence hand-waving
"Standard", "well known", "up to harmless factors" are not steps. Cite a theorem or do the work.

## K4. Label every claim
proved theorem (with citation) / identification you proved yourself (with the proof) / conditional (on what) /
prediction / conjecture / unsupported inference. Nothing conditional may be promoted.

## K5. Out of scope
* proving `[c_2] != 0`;
* supersingular primes (interface A3);
* the anomalous `a_p = +-1` primes (interface B);
* redoing the numerical `D = -7` certificate;
* any claim of full BSD, FIN or FORMULA for the seed.

## K6. Do not reason backwards from the prediction
The prediction tells you where to look. It does not tell you what is proved, and K1b makes restating it a failure.
Do not let it stop you from finding an obstruction at some `p` it does not flag: a prediction is exactly the kind of
thing that is wrong in the interesting cases. An explicit finite exceptional set is a fine answer; so is a clean
negative; so is "the unconditional result is far weaker than the prediction, here is the gap".
