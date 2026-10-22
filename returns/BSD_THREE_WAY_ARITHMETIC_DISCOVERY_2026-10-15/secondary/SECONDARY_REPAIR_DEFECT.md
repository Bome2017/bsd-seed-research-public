# A genuine secondary repair defect

This is a cohomological construction and an algebraic derivation, not a computed invariant for the seed. It explains exactly which additional arithmetic is missing from first-descent norm-root certificates.

Let ξ ∈ Sel₃(E/Q). Write V=E[3], V₉=E[9], and use the coefficient sequence

    0 → V --i--> V₉ --r=[3]--> V → 0.

The maps and the Kummer maps are fixed by this sequence; no choice of a generator of μ₃ is needed until a pairing is converted to an F₃ entry.

## Construction, once a global lift is supplied

Choose η ∈ H¹(Q,V₉) with r(η)=ξ. The existence of an arbitrary global covering lift is distinct from its local solubility. In the present odd-prime setting, the covering construction used in Fisher–Newton Lemma 1.2 supplies the relevant existence statement. It is not an algorithm for finding η or a statement that η lies in Sel₉.

For each place v, choose P_v∈E(Q_v) with κ₃(P_v)=ξ_v. Compatibility gives r(κ₉(P_v))=ξ_v, so exactness allows h_v∈H¹(Q_v,V) with

    i(h_v)=η_v−κ₉(P_v).

Put K_v=κ₃(E(Q_v)/3E(Q_v)). The class of h_v in H¹(Q_v,V)/K_v is independent of the choices made locally:

1. Replacing P_v by P_v+3Q_v changes h_v by −κ₃(Q_v), modulo ker i.
2. The kernel of i is the connecting image of E(Q_v)[3] from the coefficient sequence. This is contained in K_v: it is the ordinary 3-Kummer image of a local 3-torsion point.

Replacing η by η+i(h), for h∈H¹(Q,V), adds the localization of h to the tuple. Thus the class

    o₉(ξ) = [(h_v)_v] in
    (⊕_v H¹(Q_v,V)/K_v) / image(H¹(Q,V))

is independent of the choices. Outside a finite set the local terms lie in the unramified Kummer subgroup, so this direct-sum expression is appropriate. A finite-S implementation must prove that its chosen source includes every allowed global adjustment and that its omitted places contribute zero; merely keeping S={3,bad primes} is not automatically sufficient for a newly chosen lift.

## Exact zero criterion

The defect vanishes iff there is h∈H¹(Q,V) such that h_v−loc_v(h)∈K_v for every v. Then

    η′=η−i(h)

is locally Kummer everywhere: its local difference from κ₉(P_v) is i of a 3-Kummer element, and iκ₃(Q_v)=κ₉(3Q_v). Hence η′∈Sel₉ and r(η′)=ξ.

Conversely, a Sel₉ lift η′ differs from η by i(h) globally. Its local Kummer representatives differ from P_v by a multiple of three, so the same tuple is the localization of h modulo K_v. Therefore

    o₉(ξ)=0  ⇔  ξ∈image(Sel₉(E/Q)→Sel₃(E/Q)).

This is an exact secondary local-global repair problem. The input ξ, its first-descent norm roots, and its local 3-Kummer membership do not already give η or the h_v.

## The pairing interpretation and its limitation

After the exact normalizations are fixed, local duality pairs this repair defect with Sel₃; the resulting row is the Cassels–Tate row. A local cup product of two already-admitted local Kummer classes is zero and is not a substitute for this row.

A rational point gives a 9-Kummer lift directly, hence zero defect. A nonzero defect proves that ξ is not a rational-point class. But zero defect also permits genuine 3-divisible Sha, so it cannot establish pointhood without an independent bound on higher divisibility. Neither nonzero nor zero pairing alone is an upper bound eliminating the original excess.

## A finite arithmetic witness, once the missing data are computed

Suppose a complete finite source of global adjustments H has been independently established, and the finite local target and all its omitted-place controls are authenticated. Write its localization matrix L and the defect vector d in common bases. Then:

* a repair is an explicit solution Lc=d;
* a rejection is an explicit dual row λ with λL=0 and λd≠0;
* the row must be computed from the global lift and local Kummer comparisons, not from the already-known quotient labels;
* source completeness is necessary for rejection: annihilating a sampled subspace does not exclude a repair outside it.

Thus the next small computation is a normalized covering/lift construction followed by this finite repair test. It is not another rank calculation on the first-descent norm map. No such secondary matrix or dual row was computed in this return.
