# Fresh arithmetic blocks: the compatibility value varies despite equal ranks

2026-10-15. These conclusions use the sealed new cubic-symbol blocks together
with the retained source and local matrices. The arithmetic producer and its
independent field/point/symbol replay are separate from this exact F_3 analysis.
No BNF, local Kummer image, rank computation or complete seed source was
constructed by this analyzer.

## 1. Initial sealed panel

All120 single-prime choices and all660 unordered pairs recover the full saved
joint kernel when **all** fixed local conditions are imposed. All supplied
point classes pass, and all four certified seed3 classes pass individually.
Thus `H_single`, `H_pair` and `H_protected` pass on their original fixed panel.
The seed outcome remains its retained positive span, with point-relative
dimensions `(unit,class,valuation)=(1,1,0)`. Passing here does not mean the
seed excess vanishes.

Every one of the twelve fresh mirror blocks has a separately repairable
ordinary-class space of dimension one and a mixed obstruction of rank one.
The class is not already excluded by the global marginal test. Eight blocks
have dual overlap dimension four; the blocks at14683,15013,16843,16981 have
dimension three. Those four therefore have the same overlap dimension as the
old127 block, whose mixed obstruction was zero. The difference is the actual
value on the class lift, not the number of available mixed rows.

For example, in zero-based producer row indices the fresh10753 block gives,
on H0,

    c = 2 scalar[6] + scalar[7] + 2 add_10753[1] - local3[1].

The corresponding full eleven-entry source row is
`[2,1,0,2,1,2,0,0,0,0,1]`. It restricts to the ordinary class coordinate on
the valuation-zero source. The exact coefficients and arithmetic row labels
are retained in `mirror389.json` and the fresh block file.

## 2. Local3 alone: class compatibility versus the full source

The narrow question in `H_local3`—whether local3 retains the same ordinary
class obstruction as all local places—passes on all780 initial choices.
It would be wrong to report the following failures as class-counterexamples.

The stronger claim that local3 replaces all local conditions on the complete
source fails. The additional directions have **nonzero allowed valuations**:

- For mirror389 all78 choices leave the same extra line with sparse exponent
  vector `[0,0,0,1,2,0,0,2,1,1,2]`. Its valuation vector is
  `[0,0,0,1,2,0]`. It passes local3, but its389-local defect is `[1,2,0]`.
  Every one of the twelve fresh global blocks also admits this vector. The
  missing389-local condition, rather than another selected global block,
  removes it in this sample.
- For1246c1 the singles11467 and15667 and their pair leave one valuation
  direction if only local3 is used. A minimum-support witness is
  `[0,1,0,0,0,0,1,2,0,0,1,0,1]`; its valuation vector is
  `[2,1,0,0,0,0,1,2,0]`. It passes local3 and local7, but has defects
  `[2,1,0]` at2 and `[1,2,0,0]` at89. Independently, fresh10009 row1 has
  value1 on it, so another selected global block also removes it.

There are81 such full-kernel failures, but zero class-admission failures.
This directly demonstrates why the valuation term in the filtration cannot
be dropped or conflated with ordinary class support.

## 3. Separately sealed mirror extension: a fresh failure is found

After the initial panel completed, the next60 admissible split primes beyond
16981 were selected under a new seal. All60 were computed. Six single blocks
fail to recover the saved zero joint kernel:

    19219, 22699, 23671, 26431, 33751, 45841.

Mirror389 is the changed rank-zero control, bad at the coefficient prime3;
it is not the original rank-two seed or a new good-prime seed example.

The first failure19219 has a matched success18757 with identical marginal
dimensions:

| Auxiliary prime | rank G on units | rank L on units | joint unit rank | overlap | separately repairable classes | omega rank |
|---|---:|---:|---:|---:|---:|---:|
|19219|3|4|4|3|1|0|
|18757|3|4|4|3|1|1|

At19219 the actual class lift beta, source coordinate11, has common unit
repair `(2,2,2,2)`. Its repaired source vector is

    [0,0,0,0,0,0,2,2,2,2,1].

Equivalently, its scalar multiple
`[0,0,0,0,0,0,1,1,1,1,2]` is the smallest extra vector by Hamming support
then lexicographic order. Every allowed valuation and every actual local
defect is zero. This is a class-supported survivor of the selected necessary
global rows. It is **not** a demonstrated Selmer class: another necessary
global row rejects it.

The arithmetic difference is particularly explicit. The same global repair
`u_G=(0,1,2,2)` works at both19219 and18757, while the unique local repair is
`u_L=(2,2,2,2)`. Their difference is `(1,2,0,0)`.

- At19219 the global unit-repair kernel is the line spanned by `(2,1,0,0)`;
  it contains that difference, so the repairs can be made equal.
- At18757 that kernel is spanned by `(1,0,0,0)`; the difference is not in it,
  and the local repair kernel is zero. Compatibility therefore fails.

Fresh17791 row1 evaluates to1 on the sparse survivor. The first *larger*
prime giving such an eliminating row is19483: its row1, torsion triple
`[0,1,4]`, is

    [2,1,0,0,0,2,0,2,2,2,2],

and also evaluates to1. The field embeddings, points and cubic symbols of
these rows are retained in `heldout/mirror_extension/blocks.json`.

## 4. Explicit post-hoc pair and six-block countercontrols

All six failed blocks admit the same sparse survivor. Consequently every one
of their fifteen pairs, including19219+22699, and their full six-block union
leaves exactly the same one-dimensional class-supported kernel. These unions
were selected after the single-block outcomes and are labelled **post hoc**.
They were not the original sealed `H_pair` panel.

This disproves an unqualified rule that arbitrary two split primes must
suffice, and shows that increasing the count to six need not repair a poor
choice. It does not contradict the
initial panel's660 passing pairs and does not establish that arbitrarily
large failing sets exist. The actual distinction is which arithmetic
functionals the primes supply, not merely how many primes were sampled.

## 5. What this experiment learned

The new data isolate a concrete arithmetic variable: the global unit-repair
kernel's position relative to the fixed local repair difference. Equal
source ranks, equal marginal class admission, equal local ranks and equal
dual-overlap size do not determine it. The passing/failing primes produce
actual differently oriented unit rows, and the exact exported identities
show how that changes the class obstruction.

This gives a specific next source-formula question: what arithmetic of the
cubic-symbol state forces the relevant repair difference outside the global
unit kernel, and can it be controlled without recomputing every coefficient
prime's whole source? The present finite experiment has not answered that
uniform question. It also has not eliminated the separate unit-supported
excess, which is genuine in the protected seed3 span.

Thus this is fresh arithmetic discrimination and a constructive exclusion
of selected false candidates, not a new seed-prime certificate or an
independent cofinite bound. FIN, ORDER9 and Q36 are unchanged.

## Reproduction and scope

`analyze.py` computes2340 profiles (780 choices times three local aggregates)
for the initial panel. It verifies source bindings, equality of old/new row
payloads after the polynomial-JSON repair, exact protected-class admission,
and the point-relative filtration identities. `mirror_extension.py` computes
the60 extension profiles and the explicitly marked post-hoc unions.

Witnesses are chosen by an exhaustive search in each small relevant kernel,
minimizing support and then the exponent tuple. All outputs bind the actual
source matrices and new block files. Adding `source_sha256` was the only
change to the initial arithmetic block files; no row, root, point or symbol
was edited. The source producer's independent arithmetic replay remains a
separate receipt from these F_3 calculations.
