# Attempt beyond fixed E plus a character: a weight-three Hida specialization

Status: DATUM_AND_LOCAL_PROFILE_DERIVED; NO_AUTOMORPHIC_UPPER_BOUND.

This is an actual attempted repair of the fixed-weight obstruction. It is not a general FIN construction, a computational specialization, or a claim of novelty. It applies only to good ordinary primes under the standard Hida-family and ordinary-lattice hypotheses specified below. No supersingular extension is claimed.

## 1. What changes

The fixed-weight-two obstruction depends on the gap between the GL2 weights. A character changes neither that gap nor the number of critical integers. Instead change the GL2 form within an ordinary family while preserving its residual representation.

Let p>=5 be a good ordinary seed prime. Retain residual absolute irreducibility, p-distinguishedness, and non-anomalous reduction. Choose a normalized ordinary Hida branch through the ordinary p-stabilization of the weight-two seed form f, with residual representation E[p]. Use a finite coefficient extension as necessary; do not assume the coefficient ring is Z_p or that the family is etale over weight space.

Hida control, in the conventions displayed in Maksoud section 2.2, formula (10), sends arithmetic weight (k,epsilon) to nebentypus theta*epsilon*omega^(2-k). The branch containing the seed at (2,1) has theta=1. At (3,1) it therefore supplies a classical ordinary specialization g with

    weight(g)=3,   nebentypus(g)=omega^{-1},
    g in S_3(Np,omega^{-1}),   rho_g mod varpi ~= E[p] tensor k.

Here N is the tame level of the chosen branch, retained as the seed tame level in this attempt; if a minimal branch level or oldform realization is used, carry that distinction. Finite-flat branch/control supplies arithmetic points after coefficient extension. No q-expansion coefficients of g were evaluated.

Set

    eta_1=chi*omega^{-1}=<chi>,
    R_g=V_g direct-sum Q_p(eta_1).

Its residual semisimplification is E[p] direct-sum 1. Its three positive Hodge exponents are {0,2,1}={0,1,2}: regular and pure at the elementary coefficient-weight test.

For U=V_g*eta_1^{-1},

    U^*(1)=V_g^* chi^2 omega^{-1}.

With L(V_g^*,s)=L(g,s) and xi^D defined by geometric Frobenius as in BALANCED_GATE.md, the distinguished value is

    L(g,(omega^{-1})^D,2).

Weight three has critical integers 1 and 2, so this value is critical. This removes the criticality obstruction for this modified datum. It does not establish the full integral constant-term formula, the existence of a cuspidal GL3 congruence, or a unit value.

More generally, for positive exponents {0,k-1,j}, the elementary simultaneous requirements of purity, regularity, and 1<=j+1<=k-1 admit the middle value j=(k-1)/2 when k is odd; for even k no integral j works. For k=2 there is none, whereas k=3 permits j=1. This is a calculation of necessary weight conditions, not an automorphy theorem.

## 2. The new local condition is finite ordinary, not strict

Use Hodge–Tate weights with HT(chi)=-1. Fix a saturated ordinary O-lattice in V_g, with unramified quotient character alpha and alpha mod varpi !=1. The standard ordinary filtration and determinant chi^2 omega^{-1} give

    0 -> O(alpha^{-1} chi^2 omega^{-1}) -> T_g -> O(alpha) -> 0.

After twisting by eta_1^{-1}, write A and B for its rank-one rational subquotients:

    0 -> A=Q_p(alpha^{-1}chi) -> U -> B=Q_p(alpha chi^{-1}omega) -> 0.   (L)

The coefficient field may be a finite extension of Q_p; dimensions below are over it. Both residual H^0 groups vanish: the A-character is ramified cyclotomic, and the B-character is unramified alpha-bar !=1.

The weights of U are {-1,+1}, so its de Rham tangent space has dimension one. Bloch–Kato Corollary 3.8.4 gives dim H_f^1(Q_p,U)=1. Meanwhile H^1(Q_p,A)=H_f^1(Q_p,A) has dimension one: A has no invariants and A^*(1)=alpha has no invariants. It injects into H^1(Q_p,U), since H^0(Q_p,B)=0, and functoriality places its image in H_f^1. Thus

    H_f^1(Q_p,U)=image H^1(Q_p,A).                                    (F)

The equality with H_g also holds here. The finite ramification of omega kills D_cris(B). The dual Tate-twisted representation has a noncrystalline rank-one submodule and unramified quotient alpha. Since alpha mod varpi !=1, its phi=1 crystalline space is zero; local duality and the Bloch–Kato exact sequences give H_g^1=H_f^1. This argument does not call U crystalline.

For integral reduction, H^1(Q_p,O(B)) is torsion-free because the residual B-character has no invariants. The image of H^1(Q_p,O(A)) in H^1(Q_p,T_g eta_1^{-1}) is therefore saturated and equals the inverse image of the rational finite subspace (F). Local duality gives

    H^2(Q_p,O(A))[varpi]=0,

since the residual dual Tate twist is alpha-bar !=1. Reduction consequently maps H^1(Q_p,O(A)) onto H^1(Q_p,k(A)). The latter injects into H^1(Q_p,E[p] tensor k) and is one-dimensional. Residual ordinary filtrations match the seed's filtration, so this is its classical finite ordinary Kummer line.

Conclusion of the local calculation:

    residual image of integral de Rham extensions for U
        = H_f^1(Q_p,E[p]) tensor k,                                  (R)

not the zero local condition obtained from fixed V_pE twisted by eta_2^{-1}.

The supplied finite algebra script cannot validate Bloch–Kato theory or the Hida lattice. This proof is written and self-reviewed; the family and local hypotheses must be independently checked before project-grade promotion.

## 3. The first failed endpoint step

A critical value is not an independently bounded residual congruence module. No integral GL3 Hecke module, comparison controlling every excess class, or norm/length bound for it has been constructed in this attempt.

The local calculation gives a particularly cheap test of a proposed UNIT argument. It restores the classical finite condition at p. With compatible unramified conditions elsewhere and the retained zero bad-place local groups outside the stated exceptions, the residual Selmer problem admits the two-dimensional rational-point subspace W. It does not quotient that subspace away.

Therefore, IF a discrete Selmer module A_g is constructed with a proved identification A_g[varpi] ~= Sel_p(E/Q) tensor k, then A_g[varpi] already has dimension at least two. IF an independent inequality

    length_O(A_g) <= v_varpi(L_g)

is then proved, it necessarily gives v_varpi(L_g)>=2. An assertion that L_g is a unit would contradict the known baseline. A comparison for an EXCESS quotient is needed instead, or a valuation bound sharp enough after separately accounting for the baseline. Neither the residual identification for a discrete module nor the displayed upper bound is claimed as proved here.

Accordingly the attempt stops before global upper control. It does not claim that a higher-weight family can never furnish such control. It shows what the nearest change of datum actually changes, and why criticality by itself does not deliver the originally requested independent unit.

## 4. Disposition

Keep this as a bounded feasibility calculation: fixed E plus character is not the same class of constructions as varying the GL2 form in a residual family. The latter passes the elementary critical/weight gates at weight three and has a different, explicitly calculated p-local profile.

Do not launch a full GL3 campaign on these results alone. Its first unbuilt object is an integral automorphic/congruence module with a map controlling the correctly defined excess quotient, followed by an independent bound; there is also no supersingular coverage. Maksoud's adjoint congruence theorem is NOT used as a theorem for standard E[p] extensions.

FIN, ORDER9 and Q36 are unchanged.
