# Point-relative joint repair and a discriminating arithmetic test

2026-10-15. This is a finite-source algebra interface and an executable
diagnostic, not an independent arithmetic upper bound. Its role is to specify
what the new source calculations must measure and what would refute an
explanation based on only class groups, marginal ranks or unit indices.

## 1. Keep the actual point plane and allowed valuations

Let B be an authenticated finite F_p source containing the possible descent
classes. Write v for the allowed-prime valuation map, H=ker(v), and suppose
the actual unit/class sequence on H is

    0 -> U -> H -> C -> 0.

For a complete source C is the relevant ordinary p-torsion class group. It is
not the S-class group. For the seed3 retained calculation H is only a
specified source span: its two-dimensional class quotient is established,
but completeness of the old class group is not inferred.

Let G and L be linear defect maps, with G containing necessary scalar and
additivity conditions and L the authenticated local Kummer quotient maps.
Finite global residue rows need not characterize global cohomology exactly.
Set J_full=ker(G,L) in B and J=J_full intersect H. Let W be the actual
rational-point image, assumed contained in J_full, and W0=W intersect H.

For K_G=ker(G|U) and K_L=ker(L|U), put K=K_G intersect K_L. Let C_G and
C_L be the class directions which separately admit a unit repair for G and
L, and put C0=C_G intersect C_L. A lift beta(c) and separate repairs u_G,u_L
give the well-defined linear map

    omega : C0 -> U/(K_G+K_L),  c -> [u_G-u_L].

Its kernel C_adm is precisely the class image of J. Quotienting the exact
sequence 0 -> K -> J -> C_adm -> 0 by the actual point image gives

\[
\boxed{0\to K/(U\cap W)\to J/W_0
       \to C_{\rm adm}/\partial W_0\to0.}
\]

There is no assumption that all points are units. Indeed, the class-carrying
negative controls have a nonzero point image in C_adm. The proof is direct:
the class of j in J/W0 maps to its ordinary class modulo partial(W0); if
that class is zero, subtract a point with the same ordinary class to obtain
an element of K. The ambiguity in doing so is exactly U intersect W.

The complete source also has the valuation quotient

\[
\boxed{0\to J/W_0\to J_{\rm full}/W
       \to v(J_{\rm full})/v(W)\to0.}
\]

Dropping it without proof can erase actual candidates, as the saved 433a1
scalar/additivity calculation already demonstrates. These two sequences
separate unit excess, class excess and valuation excess while retaining
point occupancy in every part.

If the retained descent map injects Sel_p into B and sends its point plane
to W, then Sha[p] injects into J_full/W. Completeness of the finite global
screen is unnecessary for this *upper-containing-space* use. Conversely,
passing those rows is insufficient to prove Selmer membership. A calculation
on an incomplete source span cannot bound the full Selmer group.

## 2. The dual object exposes actual mixed rows

The target of omega has dual

\[
\bigl(U/(K_G+K_L)\bigr)^*
 =\operatorname{Row}(G|U)\cap\operatorname{Row}(L|U).
\]

Choose a row h in this intersection and representations
h=a(G|U)=b(L|U). Then

    eta_h = aG - bL

vanishes on U. It consequently gives an actual functional eta_h(beta(c))
on the ordinary class quotient, independent of the chosen lift. On C0 this
functional is the negative of h(omega(c)), since

    aG beta = -h(u_G),  bL beta = -h(u_L).

Changing a or b changes the functional only by one of the individual class
defects; these vanish on C0. Thus the matrix of these mixed class functionals
restricted to C0 detects omega exactly, with no loss of rank.

This is a useful arithmetic output: a nonzero row can be exported as a named
linear combination of actual cubic-symbol, scalar and local characters.
It is stronger evidence than a printed rank, but still only a finite-source
identity. A uniform theorem would have to control such arithmetic rows and
their relation to the points, not merely invoke this duality.

In particular, the overlap dimension

    rank(G|U)+rank(L|U)-rank((G,L)|U)

does not determine the rank of omega. It measures the number of available
mixed functionals, not their values on actual class lifts.

## 3. Concrete calibration before fresh arithmetic

`dual_overlap.py` reads the actual saved field-source matrices. It uses only
standard-library exact F_3 arithmetic and exports every mixed functional
with its original global-row and local-row coefficients. It treats the
actual point *span* as W; for example, 1525c1 supplies three point columns
of rank two, so counting printed columns as dimensions would be wrong.

Thirteen existing datasets were calibrated: three class-free rank-two
controls, eight ordinary-C3 rank-two controls, mirror389, and the retained
seed3 span. This is retrospective calibration, not newly generated
source arithmetic. The decisive full-block outcomes are:

| Source | admitted units | point/unit intersection | admitted class directions | point/class image | point-relative (unit,class,valuation) |
|---|---:|---:|---:|---:|---|
| 389a1,433a1,655a1 | 2 | 2 | 0 | 0 | (0,0,0) |
| eight ordinary-C3 rank-two controls | 1 | 1 | 1 | 1 | (0,0,0) |
| mirror389, rank-zero changed-curve control | 0 | 0 | 0 | 0 | (0,0,0) |
| seed3 known four-class span | 2 | 1 | 2 | 1 | (1,1,0) |

The last row is a structural statement about the certified positive span,
not a new upper bound on a complete seed source. Its four genuine classes
are protected individually by the checker: every global and local block
used must annihilate all four, not just the two point columns.

There is a sharper within-curve contrast in mirror389:

| Global block, with scalar and all local conditions | dual overlap dimension | separately repairable class dimension | omega rank | surviving class excess |
|---|---:|---:|---:|---:|
| scalar only | 2 | 1 | 0 | 1 |
| split prime127 alone | 3 | 1 | 0 | 1 |
| split prime151 alone | 3 | 1 | 1 | 0 |

The last two rows have identical marginal overlap size but different
arithmetic class values. This already refutes a proposed explanation based
only on overlap dimension. The earlier four-row certificate used both127
and151, but the full151 block suffices with scalar/local conditions; the
short certificate was not asserted to use a minimal set of primes.

## 4. The next fresh-row experiment

The sample rule is recorded before generating new row outputs:

1. Use mirror389, 718b1, 389a1 and the original seed3 span as the minimal
   panel. Mirror389 tests a rejected class; 718b1 tests a repaired class
   occupied by points; 389a1 tests unit-only point occupancy; seed3 protects
   genuine positive unit and class directions. A fresh complete rank-two
   positive candidate may be added under the separate source/cost gate.
2. For each field take the first four completely split auxiliary primes
   beyond its largest saved additivity prime, omitting bad primes and primes
   where a source element cannot be reduced as a unit. Do not select them
   using any resulting class-defect value. If the producer instead uses a
   different predeclared sample, retain that exact rule in its seal.
3. Generate each full32-row additivity block from actual reductions of the
   source elements and the actual eight torsion points. Keep the ordered
   roots, primitive cube root, torsion addition triples and exact generator
   symbols. This is fresh arithmetic; ablation of existing rows alone is
   not the experiment's new outcome.
4. For each block separately, and successively, measure C0, the dual overlap,
   omega, admitted units, the actual point intersections and allowed
   valuation contribution. Also distinguish the coefficient-prime local
   block from other local blocks. Export actual mixed source rows whenever
   a compatibility defect is nonzero.
5. Test the proposed mechanism that all completely split auxiliary blocks
   with the same marginal ranks impose the same class obstruction. The
   saved127/151 contrast already rejects its strongest form. Fresh values
   test whether a smaller arithmetic feature of the cubic-symbol state
   predicts the difference. Any feature discovered from these fresh values
   requires a further held-out sample; it is not retrospectively predicted.

The informative discovery would be an actual additional arithmetic row,
or an exact source identity generating its class value, whose dependence on
the local/unit/point data can be justified independently. Merely obtaining
the already-known final dimension again is a calibration check. A fresh
positive rank-two case can discriminate whether the class obstruction
vanishes because points occupy that class or because genuine excess does.

## 5. Countercontrols and hard failures

- **Marginal repair is insufficient.** Mirror389 has separate global and
  local repairs, but no common repair for its nonzero class.
- **Overlap rank is insufficient.** Mirror127 and151 have overlap dimension
  three but different compatibility values.
- **A repairable class is not excess by itself.** In the eight rank-two
  class controls the repaired class is already a point class.
- **Zero omega is not vanishing.** The seed3 positive span has omega zero,
  yet one unit-supported and one class-supported direction remain modulo
  points. No valid necessary row may remove those certified classes.
- **A zero class quotient says nothing about extra units.** Both terms of
  the exact sequence must be retained. A synthetic U=H=F_p^3, W of dimension
  two, G=L=0 is the minimal algebraic counterexample; it is not seed data.
- **Ordinary ray quotienting is insufficient.** The actual mirror ray
  quotient admits the local repair after dividing out all units, while the
  scalar/additivity-compatible repair does not. Do not identify its zero
  ray boundary with omega.
- **Partial-source upper bounds are invalid.** The seed span protects
  known positive classes but cannot exclude additional classes elsewhere.

None of the displayed dimension formulas is an arithmetic bound independent
of the source computation. No cofinite statement, new coefficient-prime
coverage, FIN, ORDER9 or Q36 follows from this diagnostic alone.
