alarm(20);gettime();C=read("affine_norm_certificate.gp");FB=C[2];b=C[6];d=denominator(lift(b));P=polresultant(FB,d*x^3-d*lift(b),z);P=P/content(P);
if(poldegree(P)!=24||!polisirreducible(P)||poldegree(minpoly(b))!=8,error("degree24 field presentation failed"));
write("splitting_polynomial.gp.data",P);write("splitting_polynomial.json",Str("{\"coefficients\":",vector(25,i,polcoef(P,i-1,x)),",\"degree\":24,\"irreducible\":true,\"norm_element_degree\":8}"));print("DEGREE24_SPLITTING_POLYNOMIAL=PASS;MS=",gettime());quit;
