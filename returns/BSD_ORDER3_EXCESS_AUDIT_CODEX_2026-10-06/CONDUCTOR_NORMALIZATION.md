# The marked-prime/cochain step: common normalization made explicit

**SAME_AUTHOR_SOURCE_RECHECK; INDEPENDENT_REVIEW_STILL_REQUIRED.**
This expands Sections 4--6 of input/VARIATION_AND_TUNING.md. It found no
blocking discrepancy under that proof's retained inputs. It is not a
second researcher's review or a kernel certificate.

## 1. One normalization, chosen before any pairing entries

Fix one identification of the additive coefficient mu_p with k at a
marked prime q, and identify (1/p)Z/Z with k by a/p -> a. Take q!=p
with q=1 modulo p. Let z_q be the unramified mu_p-valued cocycle with
value 1 on arithmetic Frobenius. Let theta_q be any nonzero degree-p
conductor-q character, valued in k.

Its local restriction is ramified: the corresponding degree-p subfield
of Q(zeta_q) is totally ramified at q. Define

    kappa_q = inv_q(theta_q cup z_q) in k.

Then kappa_q != 0. Indeed, local Tate duality is perfect. The two
one-dimensional unramified subspaces annihilate one another at q!=p;
the annihilator of the unramified mu_p line is the unramified character
line. The ramified theta_q does not belong to that annihilator.

Set mu_q=kappa_q^(-1) theta_q. For every unramified mu_p-valued cocycle z,

    inv_q(mu_q cup z)=z(Frob_q).                         (N1)

This scalar depends on the place, marking, character, and fixed Tate
convention. It does NOT depend on the choice of X,Y or on the matrix
entry. It therefore normalizes every residual and lifted row at once.
Multiplying theta_q by this nonzero scalar preserves its conductor and
all its prescribed zero localizations. A change of reciprocity convention
changes the normalization coherently; it does not introduce separate
unknown factors for different entries.

No condition mu_q(Frob_q)=0 for an arbitrarily chosen Frobenius lift is
needed. Formula (N1) pairs a ramified character with an UNRAMIFIED cocycle,
whose Frobenius value is well-defined.

## 2. Local formula from the actual pairing definition

Use either the residual module V or the first lifted module M_lambda.
Denote it by M and its evaluation pairing by beta:M x M -> mu_p.
For the lifted case beta=J. For the residual convention j(y)=e(y,-),
beta(x,y)=e(y,x). Fix Selmer cocycles X,Y and a global primitive

    dU=X cup_beta Y.

The primitive exists in the retained proof because the cup class is
locally zero and hence globally zero in Br(Q)[p]. This is a choice of
cochain, not a canonical new arithmetic scalar.

At the new marked q, the modules and the chosen cochains are unramified,
and Frob_q acts by -I on M. Put

    A=(Frob_q-1)^(-1)X(Frob_q),
    z=U-(A cup_beta Y).

We have X=dA locally: both are unramified cocycles, and the equality on
Frobenius determines them. Hence dz=0 by the cup-product differential
rule. All terms are unramified at q, so z is the unramified cocycle
with value

    z(Frob_q)=U(Frob_q)-beta(A,Y(Frob_q)).                (N2)

For the extension with twist 1+s mu_q, lift X globally as (0,X).
Its connecting cochain is mu_q cup X. A primitive for its pairing with
Y is -mu_q cup U. Locally use the cocycle (mu_q cup A,X), the coboundary
of (0,A); it has the required zero local class. Substitution in
Morgan--Smith Definition 3.2 gives the local term

    inv_q(mu_q cup [U-A cup_beta Y]).                    (N3)

This is (N2) by (N1). At the old exceptional set Pi, mu_q is zero as
a local character, so these terms are zero. Away from Pi and q the data
are unramified and the local invariant is zero. Thus (N2) is the full
pairing value, with the same normalization for every old and lifted
entry. No global Selmer base-change assertion is used here.

## 3. Simultaneous global realization

Retain nonzero lambda in K_0, G_lambda=GL_2(k) x C_p, and the joint
surjectivity J_lambda -> M_lambda^d proved in Section 4 of the input.
Its proof uses H^1(G_lambda,V)=0 from a nonidentity central scalar,
residual independence in the direct sum V^d, and t-stability from
(I,1). Nakayama is applied to the actual image as a k[t]/t^2-module.
It does not assert semisimplicity of M_lambda.

Choose v,w with X1(v)=t e1, X2(w)=e2, all their other specified joint
coordinates zero. In particular EVERY residual class has zero value
at v. Put c=[v,w]. Then all X_i(c) and x_i(c) vanish; the primitive
cochain equation gives

    u_ij(c)=0 for every old pair,
    U_12(c)=-J(t e1,e2)=-1.                             (N4)

Choose Pi containing Sigma, support(lambda), and the finite ramification
of all modules and cochains, and let

    R=Q(mu_p, a^(1/p) : rational primes a in Pi).

The needed intersection is Q(E[p],lambda) intersect R=Q(mu_p).
R/Q is solvable. Every common solvable quotient of GL_2(k) x C_p kills
the perfect SL_2(k), including at p=5, and is thus abelian. The maximal
abelian subfield of R is Q(mu_p): the Kummer p-part is exhausted by
commutators with a nonidentity cyclotomic scalar. This proves the
intersection statement used to prescribe the two actions together.

Choose gamma acting as (-I,0) on (V,lambda) and trivially on R.
Since J_lambda fixes mu_p, its image on R lies in an abelian Kummer
group. Therefore c fixes R, and gamma c satisfies the same prescriptions.

Take one finite normal quotient that records the modules, cochains and R.
Continuous finite-valued cochains factor through such a quotient after
enlargement. Chebotarev gives distinct primes q0,q1 outside Pi with
marked Frobenius representatives gamma,gamma c. The marking chooses a
prime above each rational prime; it does not assert that Frobenius was
canonically an element rather than a conjugacy class.

At either q, all a in Pi are p-th powers modulo q. The conductor-q
character is unramified at a and has zero value on Frob_a; hence its
entire local character at a is zero. The real place is harmless for
odd p. Normalize the two characters by (N1) and put mu=mu_1-mu_0.

Because X_i(c)=x_i(c)=0, the correction terms in (N2) are the same
for gamma and gamma c. The action of gamma on mu_p is trivial because
det(-I)=1. The cochain equation then gives

    z_(gamma c)-z_gamma = U(c).

Together with (N4), this proves simultaneously

    b_mu(x_i,x_j)=0 for all i,j,
    C_mu^lambda(X1,X2)=-1.

The two nonzero conductor components have distinct new ramification,
so their difference is an actual nonzero character. There is no
entry-dependent normalization or unproved period-unit comparison.
With the retained sign P=-C, the mixed polarization equals 1.

## 4. Audit boundary

The source cochain definition and local Tate normalization were reread
and reconstructed. This is supporting detail for the existing written
proof, not a new finite-order theorem or independent acceptance.
The full classical-Selmer Stage-A result and the complete §§4--6 tuning
argument remain independent-review obligations. This does not upgrade
an Aristotle strict-Selmer result to a full-S result.

The primary source checked was Morgan--Smith, The Cassels--Tate pairing
for finite Galois modules, arXiv:2103.08530v3, Definitions 1.1, 3.1, 3.2
and Theorem 1.3: https://arxiv.org/html/2103.08530 . The source supplies
the pairing framework; the marked-prime construction is our derivation.
