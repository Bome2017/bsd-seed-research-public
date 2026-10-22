# Light check of the integral linear algebra behind Thm 5.15's proof (BD05 p.59), done over Z instead of Z/p^n.
# U'_ell acts on Im(delta_*) = (Z[S]^0)^2 by (x,y) -> (t x - y, ell x)  (BD05 Prop 5.8(2), p.52).
# On the f-isotypic quotient t = a_ell (an integer). Claims:
#  (C1) coker(U' - eps) on Z^2 is cyclic of order |ell+1-eps*a|, and phi(x,y) = x - eps*y kills im(U'-eps) mod that order;
#  (C2) det(U' + eps) = eps*(... ) gives |det| = |ell+1+eps*a|; mod m | ell+1-eps*a it is 2(ell+1) mod m (unit iff (m,2(ell+1))=1).
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
cases = [(283,-4),(47,4),(223,-16),(13,-4),(73,-6),(59,-4),(173,-22),(229,-10)]   # seed (ell, a_ell) from seed_facts2_output.txt
ok = True
for ell, a in cases:
    for eps in (1,-1):
        M = Matrix([[a-eps, -1],[ell, -eps]])          # matrix of U'-eps in the basis (x,y) -> columns are images of e1,e2
        d = ell + 1 - eps*a
        snf = smith_normal_form(M, domain=ZZ)
        diag = sorted(abs(snf[i,i]) for i in range(2))
        c1 = diag == [1, abs(d)]
        # phi o (U'-eps) == 0 mod d
        phi = Matrix([[1, -eps]])
        c1b = all((x % d) == 0 for x in (phi*M)) if d != 0 else True
        P = Matrix([[a+eps, -1],[ell, eps]])           # U'+eps
        c2 = abs(P.det()) == abs(ell+1+eps*a)
        # mod d: a == eps*(ell+1) so det(U'+eps) == eps*eps*(ell+1)+ell... check numerically
        c2b = (P.det() - 2*(ell+1)*eps*eps) % d == 0 if d != 0 else True
        ok &= c1 and c1b and c2 and c2b
        print(f"ell={ell:4d} a={a:4d} eps={eps:+d}  d=ell+1-eps*a={d:5d}  SNF={diag}  C1={c1 and c1b}  C2={c2 and c2b}")
print("ALL OK" if ok else "FAILURE")
# order-of-magnitude mass of the seed's definite Shimura set (disc N^- = 3*2243*5843, Eichler level N^+ = 2^3*4547^2):
from fractions import Fraction
mass = Fraction(1,12)
for q in (3,2243,5843): mass *= (q-1)
for q, e in ((2,3),(4547,2)): mass *= q**e * Fraction(q+1, q)   # index of Gamma_0(q^e) in SL2(Z_q)
print("seed definite Shimura set: mass ~ %.3e (class number >= mass)" % float(mass))
