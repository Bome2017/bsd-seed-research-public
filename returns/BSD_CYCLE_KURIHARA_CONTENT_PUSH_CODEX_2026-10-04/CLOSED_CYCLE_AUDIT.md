# What the closed-cycle operator actually does

Grade: written derivation under the retained modular-curve and primitive-period inputs. This is a review and continuation of the submitted proof, not human or formal certification.

## 1. The closed lift is valid on the stated domain

Use X=X_0(N), Y=X_0(Np), Z=Z_p, alpha, beta, pi, a=alpha pi, beta_infinity=beta pi, U, z=z_E, and v from the submitted PROOF.md. Here p is a good seed prime at least 5. Distinguish the elliptic trace a_p from the map a.

The mod-p pushforward H_1(Z,F_p) -> H_1(Y,F_p) is onto. Indeed the punctured regular cover has deck group the Borel B in PSL_2(F_p). Its unipotent subgroup is contained in [B,B], since

    [diag(t,t^-1), u(b)] = u((t^2-1)b)

and some t has t^2 != 1 for p>=5. Thus B_ab has order prime to p. Abelianizing the fundamental-group sequence and then reducing modulo p proves surjectivity for the punctured surfaces. Compactification surjects on H_1 and commutes with the map. This verifies the proof without dividing by the degree of the cover. The loop correction in the input has the same effect.

The oldform matrix [[p+1,a_p],[a_p,p+1]] and its use are also consistent. Put d=p+1 and choose u in Z with

    u(d^2-a_p^2)=1 mod p.

The retained seed data make this possible: a_p is even; for p>=7 the Hasse interval excludes the even residues +/-1 modulo p; at p=5, a_5=-2. The cycle

    C=u(-a_p alpha^*v+d beta^*v)

has z(alpha_*C)=0 and z(beta_*C)=z(v) modulo p. Normalize z(v)=1 modulo p. Any closed lift D with pi_*D=C modulo p then has the prescribed periods. None of these operations uses Selmer vanishing.

## 2. Exact operator identity, including wraparound

Write B_j=(beta_j)_*:H_1(Z,Z)->H_1(X,Z), for j in F_p. The indexing convention is B_j U_*=B_(j+1). Define

    Phi_p = (sum_(j=0)^(p-1) j^2 B_j)(U_*-1)^2.

This is the complete operator whose value on D was called R_p. For k=0,1,2,...,p-1 its coefficient at B_k is

    (k-2 mod p)^2 - 2(k-1 mod p)^2 + k^2.

Using representatives from 0 to p-1, these coefficients are 2-p^2 at k=0, 2+p(p-2) at k=1, and 2 otherwise. Consequently the following is an integral identity of maps:

    Phi_p = 2 sum_(j in F_p) B_j
              + p((p-2)B_1-pB_0).                         (A1)

In particular, modulo p the second-difference weighted operator is the unweighted sum of the p finite quotient maps, multiplied by 2. This is an operator identity, not just an equality of one chosen numerical period.

## 3. Descent to the original Hecke correspondence

The p+1 quotient maps are the p+1 branches of the T_p correspondence. Thus on integral homology

    sum_(x in P^1(F_p)) (beta_x)_* = T_p a_*.

One way to justify the integral statement is first to pull back all holomorphic differentials using the trace correspondence. The same statement holds for their conjugates. The integration pairing detects real homology; integral homology is torsion free. Equivalently, lift a cycle avoiding branch values and sum its p+1 quotient branches.

Subtract the infinity branch and apply (A1). This proves

    Phi_p = 2(T_p alpha_*-beta_*) pi_*   mod p.            (A2)

Therefore the final weighted operator factors through Y, modulo p, even though the chosen lift D and its second difference need not be deck invariant. Changing D by any element in ker(pi_*) modulo p makes no change to R_p modulo p.

This matters for the proposed arithmetic comparison: the noninvariant choice has disappeared from the final cycle at the coefficient modulus being used.

Substitution of C gives the stronger identity in H_1(X,F_p):

    R_p = 2u[d T_p^2 - p a_p T_p - d^2]v
        = 2u(T_p^2-1)v.                                 (A3)

The first equality follows from alpha_*alpha^*=beta_*beta^*=d and alpha_*beta^*=beta_*alpha^*=T_p. Since z T_p=a_p z,

    z(R_p)=2u(a_p^2-1)z(v)=-2 mod p.                    (A4)

Thus the claimed nonzero value is correct. Its source is the already primitive period z(v). Equation (A3) introduces no independent constraint on the arithmetic packet coefficients.

## 4. Precise consequence for content

Let K_p be the F_p-span in H_1(X,F_p) of the *actual* two-prime discrete-log cycles defined in SOURCED_TARGET.md. Its evaluated image is 2c_E I_p^(2). Taking Hecke translates cannot enlarge that image: every T_m multiplies z by the integer a_m.

On the one-dimensional quotient detected by z, the operator in (A3) is multiplication by -2. Hence

    z(R_p) in z(K_p)  <=>  z(v) in z(K_p).               (A5)

This does not refute the desired membership. It shows that the closed-lift construction does not independently establish it by adding a new period direction or a new scalar to the target. Any proof of membership must use arithmetic information about K_p beyond the calculation above.

The original proof's statement that its output is not yet an admissible witness remains correct. The stronger interpretation that its repaired noninvariance itself moves the output into that witness content is unsupported.
