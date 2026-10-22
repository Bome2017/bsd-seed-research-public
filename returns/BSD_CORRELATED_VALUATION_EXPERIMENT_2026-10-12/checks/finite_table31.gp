default(nbthreads,1);
E=ellinit([0,0,1,-13,18]);p=31;nn=3;q=p^nn;
[ms,phi]=msfromell(E,1);
rows=List();sums=[0,0,0];
{for(a0=1,p-1,
 my(teich=lift(teichmuller(a0+O(p^nn))),aa=Mod(teich,q));
 for(j=0,p^(nn-1)-1,
  my(a=lift(aa),sym=mseval(ms,phi,[oo,a/q]));
  listput(rows,[a,j,sym]);
  sums += sym*[1,j,binomial(j,2)];
  aa*=1+p;
  ));}
write("outputs/655a1_p31_table29791.gp",Vec(rows));
ap=ellap(E,p);al=padicappr(x^2-ap*x+p,ap+O(p^7))[1];
coef=(1-p/al^2)*al^(-nn)*sums[3]+O(p^(nn-1));
print("CURVE ",[E[1..5],p,nn,q,#rows]);
print("SUMS ",sums);
print("L2 ",coef);
print("VALUATION ",valuation(coef,p));
print("DONE");
quit;
