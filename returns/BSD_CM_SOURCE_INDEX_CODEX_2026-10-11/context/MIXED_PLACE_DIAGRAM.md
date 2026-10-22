# Mixed-place experiment: the actual elliptic-quotient diagram

Date: 2026-10-11.
Grade: written derivation under explicitly admitted Shimura/Galois inputs. This is not a constructed Shimura parametrization or an evaluated CM trace, and it does not assume Sha vanishing. It identifies exactly which quantities the executable elliptic pilot measures and the additional factors needed to recover the source in the original task.

## 1. The common source and its two genuine realizations

Let X=X_(N+,N- ell1), J=Pic^0(X), and let pi:J -> E1 be a specified elliptic quotient defined over Q. The existence of a rational newform E1 at the raised conductor does not specify pi's integral lattice or show that its map on the selected residual quotient is an isomorphism. Those are separate admission obligations.

Let V_J be the retained residual quotient and suppose pi induces pi_5:V_J -> E1[5]. Let K meet the actual Shimura splitting hypotheses, ell2 be an admitted good auxiliary prime, and retain fixed embeddings into both local fields. The finite-field and singular Kummer maps give a commuting diagram on actual degree-zero divisor classes:

    J(K) / 5  -- pi -->  E1(K) / 5
        |                    |
   (partial_ell1,        (partial_ell1,
    loc_ell2)            loc_ell2)
        |                    |
    H1_sing(K_ell1,V_J) + H1_fin(K_ell2,V_J)
                -- pi_5 -->
    H1_sing(K_ell1,E1[5]) + H1_fin(K_ell2,E1[5]).

This uses the same global pi_5 at the two places. The bottom comparison is not two independently chosen scalar normalizations. Functoriality follows directly by applying pi to a chosen division point in the Kummer cocycle. Reduction commutes with pi at ell2 through Neron models; specialization commutes with pi at ell1.

For divisors of arbitrary degree, use the existing correction A_q=T_q-q-1. If c_q=a_q(E)-q-1 is a unit modulo 5 and the stated Hecke congruence holds, define q_5(D)=c_q^(-1)Kum_I([A_q D]). Then

    pi_5(q_5(D)) = c_q^(-1) Kum_E1(pi_*[A_q D]).

This is a concrete, source-preserving realization. A primitive rational point of E1 is not a substitute for the right-hand side unless its exact multiple is proved. No requirement that the CM divisor itself provide a toric generator is imposed.

## 2. The measured quantities and the two source factors

Let phi_J be the canonical singular generator obtained from the retained component normalization. Let phi_1 be the singular generator of E1 obtained from a specified generator of its split component group modulo 5. Define k by

    pi_5(phi_J)=k phi_1.

Let D_K be the corrected CM divisor. If its image in E1(K)/5 is nY, for a known rational point Y, define n by that actual identity. The condition is not automatic from rank(E1/Q)=1: E1(K) may have an additional twisted point direction. More generally retain the full image vector in a certified basis of E1(K).

With beta_J=loc_ell2(kappa_J(D_K)) and beta_Y=loc_ell2(kappa_E1(Y)), functoriality gives two separate identities:

    pi_5(beta_J)=n beta_Y,
    pi_5(phi_J)=k phi_1.

These identities are valid before division. If pi_5 is an isomorphism and k is a unit, they yield the tensor identity

    beta_J tensor phi_J^(-1)
        = (n/k) (beta_Y tensor phi_1^(-1)),

after the stipulated transport. Together with one verified global isomorphism E1[5] -> E[5], the term in parentheses is a directly instrumentable mixed-place tensor. If k=0 modulo 5, division is forbidden: the chosen quotient has lost the component normalization and does not evaluate the original tensor. If n=0 modulo 5, replacing the CM image by primitive Y would incorrectly manufacture a nonzero source.

No analytic Sha value is used to determine n. No separate local basis choice may absorb n or k. Multiplying pi by an integer multiplies both maps and demonstrates why individual factors cannot be silently normalized away. If the integer is a 5-unit the tensor ratio remains unchanged; multiplication by 5 destroys the residual comparison.

## 3. Exact Tate-curve formula for the local toric instrument

At ell1 != 5 suppose E1 is split multiplicative and has Tate parameter q with c=v_ell1(q)>0. The component coordinate of a point represented by u is v_ell1(u) modulo c. When E1[5] is unramified and 5 divides c, the singular Kummer class of u evaluates on tame inertia as

    partial_ell1(kappa(u)) = v_ell1(u) e_mu,

where e_mu is the fixed fifth-root-of-unity torsion direction. To check this, lift the point with u^(1/5): tame inertia multiplies the lift by zeta_5^v(u). Changing u to uq^j changes the valuation by jc, hence does not change its value modulo 5. The formula is integral and independent of the representative. The condition that q admit an unramified fifth root also includes its unit part; in the present admissible regime 5 does not divide ell1^2-1, so units of the unramified quadratic field are fifth-divisible and only 5|c remains.

A local component generator therefore defines phi_1 even if every global rational point has zero singular localization. In particular one must not define phi_1 as partial_ell1(kappa(Y)) unless that value is separately shown nonzero.

At ell2 the finite-local image is the actual quotient E1(F_(ell2^2))/5. It can be measured by finite-field group arithmetic. It must be transported using the same global residual isomorphism as the toric direction. A point count or two locally fitted scalars alone does not construct that transport.

## 4. A common-source trap discovered before scalar fitting

The CM class and the canonical toric generator are not supposed to be two nonzero local images of the same global point. This is forced already by reciprocity in many admitted models.

Precisely, let c in H1(K,E[5]) obey the base finite/Selmer conditions away from ell1. For every rational-point Kummer class P the global reciprocity identity gives

    <partial_ell1(c), loc_ell1(P)>_ell1 = 0.

If the finite local line is generated by one of the known point images, its perfect pairing with the singular line forces partial_ell1(c)=0. This uses no assumption on Sha. If a putative globally admissible point image instead has a nonzero component coordinate, then some other local condition or the claimed residual identification needs checking. That discrepancy is data to localize, not a scalar to fit away.

The same reasoning for two relaxed places gives two linear equations in the two singular coordinates. If the two-point localization determinant is a unit, both singular coordinates vanish. With three relaxed places only a one-dimensional permitted boundary remains, generated by the 2-by-2 minors of the localization matrix when its rank is two. This is the standard reciprocity source of the project’s existing higher-depth/determinant structure; it is not counted as a new bound or a new discovery of that theorem.

Thus the experiment must keep the independent local component generator, the globally defined CM source, and their arithmetic index. Insisting on a single globally admissible point realizing a nonzero toric generator would set an impossible subtask in this setting. The corrected diagram above avoids it without discarding any source factor.

## 5. What the current small candidates permit

For the retained candidates E=2541c1 and E1=287133c1 or 424347b1, the executable outputs are: actual rational points, local reduction/component data, finite Kummer cosets, and—only after certification—their transport through one global five-torsion isomorphism. They constitute an instrumentation test.

Recovering the original CM tensor still needs pi_*D_K and pi_*phi_J, or an independent theorem that computes their ratio with its exact integral factor. A characteristic-zero quotient's existence, its generator's primitivity, and short trace congruence do not supply these. A modular or Shimura parametrization degree cannot be asserted to cancel without proving the commutative diagram and the exact resulting ratio. Source-matched CM arithmetic is required; computing a known point on E1 with an unrelated Heegner field would not determine n for the chosen K.

The problem is now decomposed into computable geometric source indices rather than an arbitrary fitted unit. This decomposition is an executed map derivation, not a new arithmetic upper bound. No seed quantity, Kato coefficient, or CM trace is evaluated in this note.

## 6. Source and verification boundary

The local project files actually read are the discovery brief, FIRST_EXPERIMENT.md, C0-C9 of construction/CONSTRUCTION.md, A1-B7 of notes/stage2_derivation.md, and CM_MAP_ATTEMPT.md. The old C3 stop is superseded by the later finite-modulus construction and is not reopened here.

Fresh primary source read: Bertolini–Darmon, Annals 162 (2005), https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf, extracted text around equation (29), Theorems 4.1–4.2, Corollary 4.3, and Section 5.6. The paper supplies the reciprocity/finite-singular framework. Its original ordinary anticyclotomic and multiplicity hypotheses are not silently promoted to the model; the specific finite-level transports retain their project grades. No fresh visual PDF audit is claimed.

The Kummer functoriality, source-index decomposition, and Tate representative calculation above are direct written deductions; they are not independently formalized. The exact arithmetic controls from the accompanying computation remain separate from these imported geometric hypotheses.

## 7. Concrete finite-field realization of the toric direction

For both selected raised primes, ell1 has order four modulo 5. Over the unramified degree-four residue field, the nonsingular points of the split nodal special fiber form the multiplicative group and contain its full mu_5. These five-torsion points are the reductions of the toric subgroup of E1[5]. The other Tate direction, represented by q^(1/5), reduces to the node.

The maps constructed by the parallel arithmetic task require a directional correction here. The coefficients of the inverse E1[5] -> E[5] map have denominators supported at ell1 itself, so directly reducing that inverse is invalid. The forward E[5] -> E1[5] map has coefficients with denominators prime to ell1. Enumerate the 24 nonzero base five-torsion points over F_(ell1^4), evaluate that forward map with all denominator checks, and identify the four images in the smooth mu_5 subgroup. The preimages identify the toric direction inside E[5]. This is exact finite arithmetic; it does not pretend the inverse model extends integrally. If a coordinate denominator or indeterminate value occurs, it requires an actual integral extension or a justified limit. No independently chosen local map may replace it. Together with the finite Kummer quotient at ell2 this gives an executable realization of the instrumented tensor, but does not compute the CM source indices n,k or justify a modulo-25 lift.


## 8. Executed toric controls and the actual global-point discrepancy

The independent Python control `toric_mu5.py` constructs F_ell[zeta]/Phi_5 and the four smooth toric points by the explicit nodal parametrization. In completed-square coordinates Y=y+(a1*x+a3)/2, write Y^2=(x-r)^2(x-s), d=r-s and choose v^2=d. For zeta != 1 set

    X=4*d*zeta/(1-zeta)^2, x=r+X,
    u=v*(1+zeta)/(1-zeta), y=u*X-(a1*x+a3)/2.

The identity corresponds to zeta=1. All eight affine points satisfy the actual reduced curve equations. All 50 pairwise sums match multiplication of the mu_5 parameters, and all eight Frobenius checks match exponentiation by ell. No curve point is obtained from a BSD prediction. The exact coordinates are retained in TORIC_MU5.json.

For 287133c1 at 113, the node has x=80, d=100, and the selected square-root orientation is v=10. For 424347b1 at 167, the node has x=7, d=64 and v=8. Reversing v reverses the mu_5 orientation; it must not be changed independently in a transported pairing.

The parent arithmetic transcript `checks/local_points.out` gives split multiplicative type I_5 and component order 5 for both raised curves. Its actual rational points have smooth reductions: the two gradient entries are (42,6) at 113 and (64,2) at 167. Therefore these particular rational-point Kummer classes have zero singular localization at the raised prime. Their use as canonical toric generators would have failed in the actual experiment, exactly as Section 4 warns. This is a measured distinction between the local component source and the global point source, not a claim that the CM trace is zero.

At 167 the transcript also proves twist-by-minus-19 rank bounds [0,0], while at 113 its [0,2] bounds remain unresolved. Thus the 167 partner is the cleaner K-rank-one instrument. To identify its returned point Y with a mod-5 basis it suffices additionally to establish one nonzero local mod-5 Kummer image, or to certify saturation; rank bounds alone do not prove that the displayed point is a saturated generator. The source coefficient n still refers to the actual, unevaluated Shimura CM image.
