# Review of the joint class-repair obstruction

Date: 2026-10-15. Scope: the exact compatibility-quotient algebra, exhaustive independent checks of the exported matrices, and rational Hensel checks. The original number-field/source files and the sibling agent's files were not modified.

**Verdict: the compatibility quotient and its claimed vanishing criterion are correct. The actual mirror389 matrices provide a nonzero obstruction even though the global and local conditions each admit a unit repair separately.** This is a new discriminating control for the joint screen, not a seed theorem or a classification of all Selmer classes.

## 1. Precise construction and proof

Let `0 -> U -> H -> C -> 0` be an exact sequence of vector spaces over a field k. Suppose `G:H->A` and `L:H->B` are linear maps. In the implementation, H is the valuation-zero source, U is the ordinary-unit subspace, C is its ordinary ideal-class boundary, G consists of scalar and selected necessary additivity rows, and L consists of the specified local conditions.

Write `K_G=ker(G|U)` and `K_L=ker(L|U)`. Let `C_G` and `C_L` denote the images in C of `ker G` and `ker L`. The compatibility map is defined on **`C_G intersect C_L`**, not on a class that fails one of these separate conditions.

For `c in C_G intersect C_L`, choose a lift beta in H and repairs u_G,u_L in U satisfying

`G(beta+u_G)=0`, `L(beta+u_L)=0`.

Define

`omega(c) = [u_G-u_L] in U/(K_G+K_L)`.

Changing the global repair adds an element of K_G and changing the local repair adds an element of K_L. Changing beta to beta+u shifts both repairs by -u. Therefore omega is independent of these choices. Adding representatives and repairs proves linearity.

A common repair exists precisely when the affine spaces `u_G+K_G` and `u_L+K_L` meet. This happens precisely when `u_G-u_L in K_G+K_L`, which is exactly `omega(c)=0`. Consequently there is an exact sequence at the indicated terms:

`0 -> K_G intersect K_L -> ker G intersect ker L -> C_G intersect C_L ->[omega] U/(K_G+K_L)`.

There is no assertion that the last arrow is surjective. The dimension of its target is not automatically the number of independent rejected class directions. In particular, separate vanishing of the two class-defect maps does not imply joint vanishing; the repairs must be compatible.

## 2. Independent actual-matrix check

`check_compatibility.py` uses direct enumeration, with no import of the producer's Gaussian-elimination routines. On each of nine retained controls it enumerates all 81 unit corrections and all 243 valuation-zero source elements, verifies `H=U+<beta>` and the exact three class fibers, and checks the compatibility criterion for every repair pair. It also verifies the sibling report's displayed repair vectors and quotient dimensions.

For the eight controls `718b1`, `997c1`, `1070a1`, `1141a1`, `1246c1_retry600`, `1480a1`, `1525c1`, and `1613a1_grh`, the quotient `U/(K_G+K_L)` has dimension three. Nevertheless, omega vanishes on the one-dimensional ordinary-class source, and each nonzero class fiber has three common repairs. The arithmetic/source grades remain attached, including `1613a1_grh`, whose saved BNF subsequently received complete certification: `search/1613a1_grh/certify_saved.gp` reads that BNF and invokes `bnfcertify(B)`, and its retained output records `BNFCERTIFY_SAVED_GRH_BNF=1;MS=1295558`. This costly certification was not freshly replayed here; the directory suffix does not leave the final result GRH-dependent. These zero obstructions are exact statements about the supplied matrices; they do not promote positive admission through finite global rows to a complete Selmer certificate.

For `mirror389`, the matrix file is bound by SHA-256

`a5c45a386a0ff05260e3c189a4a76008ad98d5627d79f5445a3e423503ba99c2`.

The model in its source context is `[0,0,1,-21,-27]`. This is the changed-rank mirror control, not the original rank-two BSD seed. The empty point list is an input to the experiment, not itself a proof of rank zero.

On `H=F_3^5`, use coordinates `(u1,u2,u3,u4,c)`, where c is the ordinary-class coordinate. The exported source has four unit directions and one class direction. Both repair kernels are zero, so

`U/(K_G+K_L) = F_3^4`.

For c=1, exhaustive enumeration yields unique repairs

`u_G=(0,1,2,2)`, `u_L=(2,2,2,2)`.

Their difference is

`omega(1)=(1,2,0,0) != 0`.

Thus both separate conditions admit the class, but none of the 81 unit corrections satisfies both. For c=2 the difference is `(2,1,0,0)` and again no common repair exists. For c=0 only the zero unit correction survives both. In this supplied valuation-zero source, the joint kernel is therefore zero.

The globally repaired representative fails only the p=3 local block: zero-based rows 1 and 3 take values 2 and 1. Its local defect at 389 is zero. The locally repaired representative passes both local blocks but fails global rows.

## 3. A short source-row certificate

The nonzero obstruction can be exhibited without a large annihilator matrix. Let G be the row stack `scalar` followed by `additivity`, and use zero-based row indices. Restricted to `(u1,u2,u3,u4,c)`, the following rows are:

| Row | Restricted vector |
|---|---|
| G[7] | `(0,0,1,0,1)` |
| G[12] | `(1,1,1,2,2)` |
| G[44] | `(1,2,0,1,2)` |
| local block at 3, row 1 | `(2,0,2,0,1)` |

Their weighted sum is

`G[7] + G[12] + G[44] + 2*local_3[1] = (0,0,0,0,1)`.

Hence the class boundary itself is a combination of these four necessary equations. Any source element satisfying all four must have c=0. The executable checker verifies this identity on the actual full source vectors, its vanishing on every unit, and its value one on beta.

This is the most compact certificate of what the experiment learned: the obstruction is joint compatibility, rather than a separate class failure in G or L.

## 4. Arithmetic scope required for this rejection

The algebra above applies to the supplied linear maps unconditionally. Turning it into an arithmetic exclusion retains the following source obligations.

1. **Ordinary class group, not S-class group.** The exact sequence uses the valuation-zero boundary H/U. It is not valid to replace C by the S-class group merely because the source was initially built with S-units. The producer separately constructs ideal cube roots and an ordinary-class boundary. Those literal number-field checks and class/unit certification are retained source evidence here; this checker does not re-run them.
2. **G is necessary, not asserted complete.** The scalar rows and finite additivity rows must vanish on true descent classes. Their completeness is unnecessary for a negative result: an element failing even this weaker set cannot be globally admissible. Conversely, passing them alone does not establish a global cohomology class.
3. **Local rows must represent the full local Kummer image for an exclusion claim.** A quotient by only a sampled subspace could reject a legitimate class. Here `lockummer` obtains the expected image dimension from the number of degree-one local torsion-point factors, adding one at l=3, and fills that dimension with independent Kummer samples. The source count gives dimensions two at 3 and one at 389. Its use as full image relies on the retained p-descent injection and local dimension formula, as well as the authenticated local samples. Agreement at two numerical precisions alone would not suffice.
4. **The local samples have exact rational Hensel support.** I independently recomputed all six displayed polynomial values and derivatives for `y^2+y=x^3-21x-27`. Their strict Hensel inequalities hold. Combined with the retained tangent-value prime-ideal valuations, the cube margins are all positive, with minimum 40. The exact Hensel calculation sometimes gives one more digit than the producer's conservative stored margin; it never gives less. This is a rational arithmetic check, not a fresh number-field evaluation of the tangent values.
5. **No seed transfer.** This is a single coefficient-prime control with different rank and curve. No bound on the seed class-supported component, seed unit quotient, or their joint variation across p follows automatically.

## 5. What the result changes

It refutes, within actual arithmetic source data, the assumption that separate repairability guarantees joint repairability. It supplies an explicit independently checked nonzero class-compatibility obstruction and a four-row certificate expressing it. It also identifies why the earlier rank-two controls were not decisive: their class fibers had actual common repairs, and their nontrivial target quotient did not by itself force a nonzero obstruction.

The next arithmetic statement would have to control the kernel or rank of this compatibility map on the seed's relevant class-supported source, while controlling admitted unit directions as well. This control supplies a test case for such a statement, not that statement. A definition of omega or the abstract equivalence `omega=0 iff common repair exists` is not itself a new uniform arithmetic estimate.

FIN, ORDER9, Q36, and seed coefficient-prime coverage remain unchanged.

Files: `check_compatibility.py`, `CHECKS.json`, `CHECK_STDOUT.json`. All producer files were read only.
