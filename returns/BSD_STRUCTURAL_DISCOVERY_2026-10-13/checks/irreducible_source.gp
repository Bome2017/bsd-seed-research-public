\\ Exact check that the seed unit experiment is not a rational3-isogeny case.
z;t;s;X;w;
R=read("../seed3/actual_representatives.gp");
if(!polisirreducible(R[5]),error("field polynomial reducible"));
E=ellinit(R[1]);T=R[6];
if(!ellisoncurve(E,T)||ellmul(E,T,3)!=[0]||T==[0],error("invalid torsion point"));
dy=poldegree(minpoly(T[2]));
if(dy!=8,error("torsion orbit not proved size8"));
print("FIELD_IRREDUCIBLE=1; TORSION_Y_DEGREE=",dy);
print("NONZERO_TORSION_ORBIT=8; RESIDUAL_REPRESENTATION_IRREDUCIBLE");
print("NO_RATIONAL_3_ISOGENY_FROM_ORBIT");
quit;
