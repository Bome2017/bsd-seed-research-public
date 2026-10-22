# Stark branch — fixed-ambient base change is not a difficulty reduction

2026-09-22. `returned_A_basechange.tar.gz`, sha256
`20d21d8128bb449c99920ab094a4e64e914eae1472f6167ae5b409fe936d132c`. New `RequestProject/BaseChange.lean`;
`Ancestor`, `BaseChange`, `Main` all `sorry`-free. **Value: it closes off a tempting continuation of A.**

## 1. The central equivalence, and why it is the right diagnosis

Within the stated finitely generated-module class,

    fixed rank-3 ambient base-change model   <=>   finite lane support.

Verified here. If `M` is a fixed f.g. module of rank 3 then `M = Z^3 (+) T`, so `dim_{F_p}(M (x) F_p) = 3` for every `p`
not dividing the invariant factors of `T` — a finite set. Meanwhile Kummer gives

    dim Sel(K, E[p]) = dim E(K)/p + dim Sha(E/K)[p] = 3 + dim Sha(E/K)[p],

using `rank E(K) = 3` (from the certified `D_1 = -23` twist) and `E(K)[p] = 0` for odd `p` (surjective residual image).
So `M (x) F_p ~ Sel(K, E[p])` — or any one-sided comparison forcing `dim Sel <= 3` — **already kills the extra Sha
dimension outside finitely many primes.** Constructing that ambient object *is* doing the lane-tail arithmetic.

Retained precisely so no future run spends itself on "maybe build a universal integral Selmer module."

## 2. Normalization is not an independent knob

`linearIndependent_reduce_square_iff_not_dvd_det`: in the square nondegenerate model with lattice matrix `Y`, the single
maximal minor is `det Y`, so

    I_3(p) = F_p   <=>   p does not divide det Y.

And `saturating_normalization_forces_unit_ideal`: any normalization exactly saturating the available `p`-divisibility
forces success. Therefore a genuine lane failure *away from the lattice index* must come from **additional
`p`-divisibility of the arithmetic class inside the ambient module**. Normalization cannot be turned into a second knob
that solves the tail once the ambient object exists.

**This relocates A's problem to the arithmetic class itself**, which is a sharper statement than "ambient Selmer is the
unknown half".

## 3. The bounded version is correctly weaker

`dim Sel(K, E[p]) <= B` gives only `#Sha(E/K)[p] <= p^{B-3}`:

    B = 3 -> <= 1 (vanishing)    B = 4 -> <= p    B = 5 -> <= p^2    B = 6 -> <= p^3

The bound **grows with `p`**, so it never becomes finite support. Only `B = 3` suffices, and that is essentially the
vanishing statement itself.

## 4. Recorded status

    FIXED_AMBIENT_BASECHANGE = NOT_A_DIFFICULTY_REDUCTION   (in its stated class)

**Not** "impossible", and **not** a universal no-go for integral Selmer complexes — the run asserts no impossibility in
either `C_mat` or `C`, and its one scoped negative (`C_wedge`) stays where it was. What the formal result shows is what
such a construction would already entail, so there is no reason to spend another run merely trying to build a fixed
rank-three ambient module.

A's residual target is now: **control extra `p`-divisibility of the Heegner/Stark class uniformly** — with its obvious
fixed-ambient implementation known to be equivalent to the desired tail.

## 5. B is the stronger surviving branch

    A reduces to:  control extra p-divisibility of the Heegner/Stark class, uniformly
                   (obvious implementation == the tail theorem itself)

    B reduces to:  sum_sigma c_2(sigma) phi_E(x_{p^n}(sigma)) != 0 (mod p),
                   after ordinary p-stabilization and norm-coherence were proved to vanish mod (p*Lambda + I^3)

B's target is an **actual integral distribution sum**, not an existential global module. That makes it the more
executable object.

**Next question is no longer "can we build an integral ancestor?" It is:**

> Can the Gross-point distribution relations force the degree-two weighted sum to be nonzero mod `p` for all but
> finitely many ordinary `p`?

Attack by tracing the distribution relations, symmetries, Hecke recurrences, and possible divisibility of that exact
integer sum. If those relations make the sum the reduction of one fixed nonzero (algebraic) integer, ordinary-side tail
compression follows. If it genuinely varies with `p`, what is wanted is the **exact recurrence governing that
variation** — not another abstract Selmer model. The supersingular signed construction remains separately necessary.

## 6. Priority order

    B finite-layer Gross-point nonvanishing  >  B supersingular signed companion  >>  more A ambient-base-change work

No change to FIN. No change to 2601. Still no justification for computing `p = 17`.
