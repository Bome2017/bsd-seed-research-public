# Exact common-certificate contract

The curve is unchanged:

\[
E:y^2=x^3-22735x^2+106272484x,\qquad
N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]

The family parameters are `(m,n)=(2243,12)`, `A_seed=4547`,
`B_seed=5843`. The letter **B below is a different object**.

Use the predecessor's minimal differential, total real period
\(\Omega=\int_{E(\mathbb R)}|\omega_E|\), full Mordell--Weil basis,
and BSD-normalized Neron--Tate regulator \(R=\operatorname{Reg}\).
Explicitly, the retained basis is
\(P_1=(4547,327384)\), \(P_2=(5184,281520)\). If h denotes the
absolute logarithmic x-height, use
\(H(P)=\lim_{n\to\infty}4^{-n}h(x(2^nP))\) and
\(\langle P,Q\rangle=(H(P+Q)-H(P)-H(Q))/2\), with
\(R=\det(\langle P_i,P_j\rangle)\). These are precisely the
normalizations in the predecessor's regulator certificate.
Thus

\[
q=\frac{L''(E,1)}{2\Omega R},\quad
35.99427<q<36.00573,\quad
\frac{\prod_\ell c_\ell}{|E(\mathbb Q)_{\rm tors}|^2}
=\frac{16}{2^2}=4.
\]

These are retained inputs, not recomputed in this task. In particular, Ota's
period is not silently substituted for the total real period.

## Required construction and interfaces

An admissible answer constructs, before FIN, a distinguished
\(B\in\mathbb Q_{>0}\) and proves independently:

* **Real interface:** \(q=4B\).
* **Arithmetic interface:** for every prime \(p\), the group
  \(\Sha(E/\mathbb Q)[p^\infty]\) is finite and
  \[
  \operatorname{length}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]
  \leq v_p(B).
  \]

The primary finiteness assertion is part of the interface. An expression
for the order of an unknown-finite group cannot replace it. An annihilator
bound alone also cannot replace an order/length bound.

The arithmetic interface includes **2243, 4547, and 5843**. For these primes,
a route using the quoted good-prime Ota/BKS theorems has a separate
unproved finiteness-and-length obligation. It is not enough to omit them
from an Euler product. The retained 2-, 3-, and 5-primary results remain
imports; the 3-primary order-nine result retains its Skinner/Jones/period
provenance qualifications.

The predecessor already proves that these interfaces force \(B=9\), full
Sha order nine, and FORMULA. That implication is not reproved here.
No exact p-adic unit coherence is required: the one-sided length inequality
is the actual target.

## Construction record required for a candidate

For each candidate, record the coefficient ring, arithmetic complex or
module, distinguished element, pre-FIN definition, realization maps,
integral normalization, and the status of both comparisons. In this task
those records are in `CANDIDATE_AND_SOURCE_ANALYSIS.md` and the dominant
analytic candidate is examined in `MELLIN_JET_THEOREM.md`.

Merely setting \(B=q/4\) gives a real number, not this certificate.
Setting \(B=\#\Sha\) presupposes FIN. Specifying a rational determinant
line without its analytic coefficient gives neither interface.

The top-level architecture remains **FULL BSD = RANK AND FIN AND FORMULA**.
RANK is retained closed; the other two branches are open.
