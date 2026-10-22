# Independent same-team desk review of the residual graph norm

Date: 2026-10-11. Reviewed `comparison/GRAPH_NORM_COMPARISON.md` against the current base Brandt output, the retained component construction, and BD05 §5.5. **Verdict: the displayed square comparison is supported under its retained C3 and graph identifications.** This is a written mathematical audit, not an external review, Lean certificate, or new seed conclusion.

## The quotient degree and the factor five

The maps can be made explicit to remove a possible contravariance ambiguity. Write `i = π*:X_E→X_J` for pullback of torus characters, and `j = (π∨)*:X_J→X_E` for the map from the polarized dual homomorphism. The monodromy pairings make these adjoint: `<i(a),x>_J = <a,j(x)>_E`. Since `ππ∨=[δ]`, contravariance gives `j i=[δ]`. The elliptic character generator has pairing `<1,1>_E=v_167(Δ_E)=5`. Thus, with `v=i(1)`,

    <v,x>_J = 5 j(x),       j(v)=δ,       <v,v>_J=5δ.

The 5 is the geometric component order, not a rational Tamagawa replacement or the coefficient characteristic inserted artificially. This also proves that `v mod5` is in the radical of the graph-cycle pairing. No assumption that the character injection is an isometry is made.

## The radical and the doubled norm

The integral incidence map has image the degree-zero vertex lattice for a connected graph. Its cokernel is torsion-free, so reducing the cycle sequence modulo 5 is exact. With all edge weights one, elementary duality gives `(ker d)^perp=im d^t`, and a radical cycle is therefore a gradient whose potential is harmonic. Normalizing the potential by total sum is legitimate because 352 is a 5-adic unit. Hecke equivariance, the nonconstant T2 eigenvalue, and the executed one-dimensional simultaneous base eigenspace give the residual potential `(a f,b f)`. The displayed Laplacian has kernel `a=b`, as claimed.

The base file was independently read and its vector sums recomputed: length 176, sum zero, norm 144, every weight 1, entries `f_0=1,f_1=0`. The potential in the literal bipartite graph is `(f,f)`, with norm **288**, not 144. Each geometric edge occurs once in C1; BD05's diagonal monodromy convention has no compensating factor 1/2. I find no factor-two loss here.

## The congruence and the component coordinate

From `v=c d^tξ−5w` and `dv=0`, one gets `dw=36c ξ`. Therefore `<v,v>=−180 c²<ξ,ξ>+25<w,w>`. Dividing by 5 before reducing modulo 5 gives `δ=−36 c²·288 (mod5)`. This division is justified by the exact equality, not by dividing a congruence modulo 5.

BD05 Corollary 5.12 sends a vertex divisor D to the class of the edge lift's character functional: choose `dz=D` and restrict `<z,−>` to X. For `D=(e_0−e_1,0)`, the retained source functional and the literal potential both evaluate to 1. Hence its image on the elliptic component group is `<z,v>=c (mod5)`. This establishes `k=c` for this representative. It does not require identifying the full odd-coordinate convention, and introduces no half or additional degeneracy degree. An overall edge orientation sign cancels in the squared ratio.

Consequently

    δ/k² = −36·288 = 2 (mod5).

Combining with the separately reviewed polarized quotient degree `δ=293952`, also 2 modulo 5, gives **k²=1**. The sign remains uncomputed. The existence of a nonzero k continues to use the retained component map (and is independently consistent with the degree/component-index calculation in `BASIS_AND_DEGREE_REVIEW.md`).

## Scope and sources

This review does not certify the CM coefficient, Gross–Zagier local factors, or a seed comparison. It accepts the current C3 input and the standard doubled-graph identification; it has not constructed the 29,000-edge graph. The base residual eigenspace computation is retained as executed evidence; only its saved vector's arithmetic was independently recomputed here.

Freshly read primary source: Bertolini–Darmon, *Iwasawa's Main Conjecture for elliptic curves over anticyclotomic Zp-extensions*, Annals 162 (2005), §5.5, Proposition 5.11 and Corollary 5.12 (printed pp.44–45), with §5.4's Picard/Albanese distinction retained: https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf . The adjoint-character and norm calculation above is the reviewer's deduction, not a quotation of a theorem with the present numerical data.
