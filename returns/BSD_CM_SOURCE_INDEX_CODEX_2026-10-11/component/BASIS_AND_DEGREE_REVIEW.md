# Independent same-team review: coefficient lattice, Shimura degree and Manin normalization

Date: 2026-10-11. Scope: the small raised curve E1=[1,1,1,1878418,-485198548] and K=Q(sqrt(-19)). This reviews the proposed CM-index extraction's discrete arithmetic inputs. It does not independently certify the analytic Gross–Zagier evaluation or claim a seed consequence.

## Verdict

The actual integral CM image has an **integer**, not merely half-integer, coefficient in the point Y=(480,22723):

    E1(K)=E1(Q)=Z*Y.

The saturation was freshly executed at all primes, and torsion over K was independently excluded with two tiny finite-field counts. The retained exact rational/twist rank bounds are used explicitly.

The source-matched optimal Shimura degree is

    delta_(501,847)=293952,

conditional on the recorded classical modular degree 20576640. Pastén's degree-comparison identity applies with nonsquarefree Eichler level 847. The geometric component indices occurring in that identity can all be computed in this case; no general component-surjectivity assertion is assumed. The same argument proves surjectivity of the optimal Shimura quotient on its full geometric component groups at 3 and 167.

The positive classical Manin constant is 1 by the published divisibility theorem and semistable-prime support, without promoting the analytic BSD quotient to an actual Sha order.

## 1. Fresh complete saturation of Y

The primary Cremona `allgens` row is

    424347 b 1 [1,1,1,1878418,-485198548] 1 [] [480:22723:1].

Cremona's accompanying Table Two documentation explicitly describes these as checked generators, not merely independent points. This is one retained database input. I additionally ran the current eclib saturation implementation through Sage on the given point, using `MW.saturate()` with its default unrestricted bound, rather than stopping at 5 or at an arbitrary small prime.

The exact returned status was

    (True, 1, '[ ]'),       resulting basis [[480,22723,1]].

The transcript reports saturation index bound 1 for the good-reduction points, adds the Tamagawa index primes 2 and 5, and proves saturation at both. Its maximum sieve primes were 13 and 43. The official/local API states that a True return with the default bound proves saturation at all primes. Modern eclib division uses exact division-polynomial methods; this is a computer-assisted library result, not a Lean certificate or an independently reimplemented proof of the height-bound algorithm.

Combined with the retained exact rank bound rank E1(Q)=1, this proves Y is a primitive generator of the free rational Mordell–Weil group. The script, raw output and error file are `basis_check.py`, `basis_check.out`, and `basis_check.err`; the final error file is empty.

## 2. Torsion over K vanishes, and no new half-generator appears

The curve has good reduction at 2 and 5. In K, 2 is inert because -19 is 5 modulo 8, while 5 splits. The reductions needed are therefore over F4 and F5 respectively. The standard-library checker enumerates every affine pair, obtaining

    #E1(F4)=8,       #E1(F5)=9.

Over F4 it directly uses y^2+xy+y=x^3+x^2 in F2[u]/(u^2+u+1); it does not infer the answer from an L-function coefficient. Over F5 it uses the original displayed model.

For torsion of order prime to the residue characteristic, good reduction is injective. Consequently the 2-primary torsion over K injects into the group of order 9 at a place over 5, so it is zero; the 5-primary torsion injects into the group of order 8 at the place over 2, so it is zero. Every other primary torsion subgroup injects at both places, hence has order dividing gcd(8,9)=1. Thus

    E1(K)_tors=0.

Retain the independently computed rank bounds

    rank E1(Q)=1,       rank E1^(-19)(Q)=0.

The quadratic rank decomposition gives rank E1(K)=1. The nontrivial element sigma of Gal(K/Q) acts on this torsion-free rank-one group by +1 or -1; it fixes the nonzero point Y, so its action is +1. Every K-point is therefore rational. Full rational saturation now gives

    E1(K)=E1(Q)=Z*Y.

In particular, for **any genuine integral** degree-zero CM divisor class D in J(K), its actual image Z=pi(D) satisfies Z=nY with n in Z. No finiteness or vanishing assertion for Sha is used.

This conclusion is intentionally not applied to the rational Hodge-normalized divisor before clearing its denominators. A value in E1(K) tensor Q need not have integral coordinates. To extract an integer square from a height calculation, use the actual integral Hecke-corrected image Z.

## 3. The degree comparison uses geometric component orders

Freshly read source: Pastén, *Shimura curves and the abc conjecture*, Proposition 6.13, §6.4 and the proof of Lemma 6.14. In the inspected 2018 manuscript these appear on printed pp.28–31; the currently cited arXiv version has shifted pagination. The proof explicitly states that the identity does not require M squarefree.

For the two factorizations of 424347,

    (D,M)=(1,424347),     (501,847),

both optimal elliptic quotients belong to the rational isogeny class of E1. The exact `ellisomat` computation in this folder proves that this class contains only one Q-isomorphism class. Hence the two quotients have identical geometric component orders.

At 3 the curve has multiplicative type I14; at 167 it has type I5. Thus the geometric orders are

    c3=14,       c167=5.

The rational Tamagawa number at 3 is 2. Substituting that 2 into Pastén's formula would be an error: his c_p here is the order of the **geometric** component group, namely v_p(Delta) for multiplicative reduction.

Let i3 and i167 be the image orders for the classical optimal quotient from J0(424347), and let j3 and j167 be the cokernel orders for the Shimura quotient from J_0^501(847). The classical component groups at primes exactly dividing the level are Eisenstein. The proof of Pastén's Lemma 6.14 gives, on their images in an elliptic quotient,

    i_r divides q+1-a_q(E1) for every q not dividing 424347.

The two exact good traces a5=-3 and a13=-2 therefore give

    i3 | gcd(9,16)=1,       i167 | gcd(9,16)=1.

So i3=i167=1.

Now Proposition 6.13, applied in its two symmetric orders, reads

    delta_(1,424347)/delta_(501,847)
      = 14*5/(i3^2*j167^2)
      = 5*14/(i167^2*j3^2).

It follows that j3=j167. But a component-map cokernel is a quotient of the elliptic target component group, so j3 divides 14 and j167 divides 5. Thus

    j3=j167=1.

The recorded classical modular degree is 20576640. Its provenance is the exact `alldegphi` row for the same displayed model, not an analytic recognition. Therefore

    delta_(501,847)=20576640/70=293952.

This simultaneously proves component surjectivity in this particular case. It does not invoke the false general assertion that every optimal quotient of a toric Jacobian is surjective on component groups. The argument computes both cokernel orders by the exact comparison identity and coprimality.

The degree is the polarization degree of the optimal quotient in Pastén's convention, equivalently the degree of its associated parametrization after a geometric basepoint choice. Translation of that map does not change its degree. If a CM formula instead uses a nonoptimal multiple of the quotient, its degree and height must both be scaled; 293952 may not be inserted for that different map.

## 4. Classical Manin constant

For the optimal classical parametrization to E1, the positive Manin constant c0 is an integer. Pastén §10.1 records the established implication

    v_q(N)<=1 implies q does not divide c0,

including q=2 after the cited Cesnavicius result. Only 11 can therefore divide c0.

Cesnavicius–Neururer–Saha, *The Manin constant and the modular degree*, arXiv:1911.09446v3, Theorem 1.2, gives c0 dividing the modular degree for cube-free conductor. Here

    N=3*7*11^2*167

is cube-free, and 11 does not divide 20576640. Consequently c0=1. This proves the normalization from the named theorem and degree input; no semistability assumption at 11 is made, and no exceptional p=2 factor is silently omitted.

This controls the classical differential normalization. It does not assert that an arbitrarily selected quaternionic eigenform or CM parametrization has the same differential without its own stated normalization. The relevant CM formula must use the above optimal quotient and its polarization pairing.

## 5. The integral correcting operator and the discrete extraction

For the proposed correction

    c = 2(T5-6) - (T13-14),

the degree character is zero, so c applied to a CM point is an integral degree-zero divisor. On the g-eigenquotient its scalar is exactly

    2(a5-6)-(a13-14) = 2*(-9)-(-16) = -2.

Provided the Hodge class is the Hecke eigenclass stipulated in the actual CM formula, this gives Z=-2 times the Hodge-normalized image in E1(K) tensor Q. Thus the height of Z is four times that Hodge height. This is a normalization identity, not an independently evaluated height.

Since the actual Z lies in E1(K)=Z*Y,

    canonical_height(Z)/canonical_height(Y)=n^2,     n in Z.

A genuinely rigorous enclosure, for example 35 < this ratio < 37, therefore forces n^2=36 and Z=+6Y or -6Y. In particular its Kummer class modulo 5 is nonzero. A floating approximation near 36 alone is not such an enclosure. I have not certified that analytic interval here; the separate Gross–Zagier formula and interval computation must supply it. Nor does this review determine the sign of Z.

No seed-primary conclusion follows simply from this small-model coefficient extraction.

## 6. Evidence and scope

Fresh computations: complete eclib saturation, full small-field enumerations, local/isogeny controls, and exact integer arithmetic on the component-index and degree expressions. Retained inputs: rational and twist rank bounds, Jacquet–Langlands occurrence, the published degree-comparison theorem, and the classical modular-degree data row. Not checked here: the full analytic height formula, its local test-vector constants, the rigorous L-value/period/height enclosures, or the exact CM embedding choice.

Primary references actually consulted:

- https://johncremona.github.io/ecdata/ , Table Two generator documentation and the bound `allgens`/`alldegphi` rows.
- Installed Sage primary method documentation for `mwrank_MordellWeil.saturate`, saved as `SATURATION_API.txt`. The public documentation URL was attempted but unavailable through the browser; it is not claimed as freshly read.
- https://people.math.harvard.edu/~hpasten/preprints/ShABC.pdf , §6.4, Proposition6.13, Lemma6.14 proof, §10.1.
- https://arxiv.org/pdf/1705.09251 , corresponding revised primary source identified by the constructing agent.
- https://arxiv.org/pdf/1911.09446v3 , Theorem1.2 and the introduction's semistable support discussion.

The supporting script `torsion_and_indices.py` is standard-library only. Its output is `TORSION_AND_INDICES.json`. It does not compute any Sha group or use an analytic Sha value.
