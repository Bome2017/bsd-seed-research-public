# Aristotle A and B — integral-ancestor audits, graded

2026-09-22.
    A (Stark `I_3`)      returned_A_ancestor.tar.gz  sha256 f376d6a7d18a7c37a46d98b8cd374df7f0ea04b4e2b15724aa633f4901ba7f30
    B (definite theta)   returned_B_ancestor.tar.gz  sha256 46a75b730e8892f9207b4c08e2040a3cf5d692c68b4d547ff9bab90d662cd832
All Lean `sorry`-free. Endpoint effect for both: **NONE**. Neither constructed the ancestor.

## A — recorded as `STRICT_REDUCTION within the integral-model architecture`

Better than "endpoint SCOPED": the chain after the specialization step is now formally discharged for a substantial
class —

    fixed integral ambient model + comparison  =>  fixed matrix  =>  C_1 = gcd(maximal minors)  =>  finite lane support

with nondegeneracy free from the certified `p = 13` unit specialization.

**The trace is the useful part.** Stage by stage, `p`-dependence is *not* where it was assumed to be:

| stage | verdict |
|---|---|
| `T = T_p(E)`, layer `E[p]` | not an obstruction — `{E[n]}` is torsion of one `p`-free object (the Néron model) |
| bad places dividing `N` | `p`-uniform on regime (P) |
| local condition at `p` | shape uniform; `p` is **not** inverted in `Z[1/N]`, so `Z[1/N] -> F_p` is an honest reduction |
| **ambient Selmer complex `S_p`** | **the unknown half** |
| Kolyvagin index poset | not used at the bottom class `eps_{1,0}` |
| exterior bidual / Fitting formation | **proved not `p`-specific** (`unitRegulator_iff_linearIndependent`: over a field the ideal is the unit ideal iff the components are linearly independent) |
| **normalization of the class** | **genuinely `p`-placed in the present definition** |

So the live A-arrow: **construct a fixed integral model of the ambient Selmer family + the normalized Heegner/Stark
class, and prove base change/specialization.** `p`-dependence sits in *ambient Selmer + normalization*, not in the
determinant algebra.

**`C_wedge` is not elevated.** It is correctly scoped as a proved negative in one delimited subclass, and the run itself
declines to claim K1 generally. Structurally it says an ancestor preserving a primitive exterior generator at every `p`
would force the unit test everywhere — excluding an unusually rigid ancestor, not the matrix/Fitting strategy.

## B — recorded as `SCOPED`, with a candidate identified and one new hard constraint

**A candidate for the fixed object now exists:** `Θ_int = (φ_E, {x_c})` in
`lim_c Z[Pic(O_c)] = Z[[Gal(K[∞]/K)]]`, with `φ_E` the Jacquet-Langlands transfer to the definite Shimura set of level
`(N⁺, N⁻)`. Ten interfaces classified: 1, 2, 3, 8, 9 (Shimura set, coefficient lattice, anticyclotomic group ring,
augmentation filtration, degree-two specialization) are realizations of fixed integral data; 4 and 6 (ordinary
projector, `p`-stabilization / unit root `α_p`) are normalization, **proved invisible** to both the filtration and the
mod-`p` vanishing test; 5 and 10 are proof technology, not properties of the object.

**Interface 7 is the whole gap.** The fixed conductor system is `a_p`-coherent (a `U_p`-recursion) while the `p`-adic
object is norm-coherent only after the `α_p^{-n}` twist, and `α_p` is not the specialization of a fixed element of `Z`.
So the first arrow is now a single identity rather than "find an integral theta object":

    pr_{Γ_p,*}(Θ_int) ⊗ Z_p  =  u_p · Θ_{E/K,p},   u_p ∈ Z_p^×,  for all p outside a finite S.

**Caveat on grade.** The arithmetic source reconstruction is **prose**; the Lean part formalizes the downstream algebra
*conditional* on it. The displayed comparison is not proved.

**New constraint, independently confirmed here — this is not a footnote.** An elliptic curve over `Q` has infinitely
many supersingular primes (Elkies 1987), and the seed is non-CM. Directly from the corpus, the supersingular primes
below 2000 are

    23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823   (15 of 301).

Therefore **ordinary-tail control != whole-prime-tail control**: even a full proof of `ord_triv Θ_{E/K,p} <= 2` over the
good ordinary tail would not give `TAIL_FINITE_SUPPORT`. Success on B additionally requires either a supersingular
analogue of the same theta/Selmer comparison, or a separate theorem eliminating all but finitely many supersingular `p`.
This changes what success on B buys and had not been recorded before.

## Frontier

    STARK_AMBIENT_INTEGRAL_MODEL       = OPEN
    STARK_SPECIALIZATION               = OPEN
    THETA_INTEGRAL_CANDIDATE           = IDENTIFIED
    THETA_NORM_COHERENCE_COMPARISON    = OPEN
    SUPERSINGULAR_TAIL_CONTROL         = OPEN
    TAIL_FINITE_SUPPORT                = OPEN
    FIN                                = OPEN      FORMULA = OPEN
    CURRENT_THRESHOLD                  = 2601
    p = 17                             = still not justified

**Next move is not another invention package.** For A: the actual integral Selmer / base-change construction and the
normalization. For B: the single norm-coherence identity relating the fixed Gross-point system to the ordinary `p`-adic
theta measure, and separately whether the same published machinery has a supersingular signed analogue.
