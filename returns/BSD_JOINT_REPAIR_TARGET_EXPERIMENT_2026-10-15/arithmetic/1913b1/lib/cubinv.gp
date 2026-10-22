\\ Ternary cubic invariants c4, c6 from Hessian covariants (classical: coefficient of l^2 m in
\\ H(lU+mH(U)) = k*S*U ; H(H(U)) = a*S^2*U + b*T*H(U)). Constants calibrated on Weierstrass cubics.
z; a1; a2; a3; a4; a6;
hessm(U) = my(v=[x,y,z]); matrix(3,3,i,j, deriv(deriv(U, v[i]), v[j]));
hess(U) = matdet(hessm(U));
monos = [x^3,y^3,z^3,x^2*y,x^2*z,y^2*x,y^2*z,z^2*x,z^2*y,x*y*z];
cvec(U) = vector(10, i, my(m=monos[i]); polcoef(polcoef(polcoef(U, poldegree(m,x), x), poldegree(m,y), y), poldegree(m,z), z));
{raw4(U) = my(HU = hess(U), D1 = trace(matadjoint(hessm(U)) * hessm(HU)), q = D1 / U);
  if (type(q) == "t_RFRAC" || poldegree(q,x)>0 || poldegree(q,y)>0 || poldegree(q,z)>0, error("raw4: not a multiple of U")); q;}
{raw6(U) = my(HU = hess(U), HH = hess(HU), cU = cvec(U), cH = cvec(HU), cHH = cvec(HH), i1, i2, d, A, B);
  \\ pick two coordinates where [U,H] is invertible
  for (i=1,10, for (j=i+1,10, d = cU[i]*cH[j]-cU[j]*cH[i]; if (d != 0, i1=i; i2=j; break(2))));
  A = (cHH[i1]*cH[i2]-cHH[i2]*cH[i1])/d; B = (cU[i1]*cHH[i2]-cU[i2]*cHH[i1])/d;
  if (cHH != A*cU + B*cH, error("raw6: H(H(U)) not in span(U,H)")); [A, B];}
c4c(U) = raw4(U)/12;
{c46(U) = my(r4 = raw4(U), AB = raw6(U), c4 = r4/12, c6 = AB[2]/16);
  if (AB[1] != 48*c4^2, error("c46: A != 48 c4^2")); [c4, c6];}
\\ substitute a 3x3 matrix: U(g*[x,y,z]~)
csubst(U, g) = my(v = g*[x,y,z]~); substvec(U, [x,y,z], [v[1],v[2],v[3]]);
