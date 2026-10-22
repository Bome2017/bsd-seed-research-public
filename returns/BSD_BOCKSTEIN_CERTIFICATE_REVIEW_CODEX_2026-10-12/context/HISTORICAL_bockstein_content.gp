\\ Light check (Claude 2026-10-07): second wild factor B in the scale of delta_p.
\\ beta(x) = <x, n_fine>_p (relaxed-strict pairing; splitting-independent since loc_p n_fine = 0).
\\ vB := min_i v_p(<Q_i, n_fine>), n_fine = primitive point with log_omega = 0. Generic vB = 1 (heights in pZ_p).
\\ Unit-root bilinear height from ellpadicregulator on singletons (ordinary p only).
E0=ellinit([0,-22735,0,106272484,0]); P1=[4547,327384]; P2=[5184,281520];
E=ellminimalmodel(E0,&ch); Q1=ellchangepoint(P1,ch); Q2=ellchangepoint(P2,ch);
S=elladd(E,Q1,Q2); D=ellsub(E,Q1,Q2); N=ellglobalred(E)[1];
lg(E,Q,p,np,pr)=ellpadiclog(E,p,pr,ellmul(E,[Q[1]+O(p^(pr+4)),Q[2]+O(p^(pr+4))],np))/np;
out=List();
{forprime(p=7,400, if(N%p==0,next); ap=ellap(E,p); if(ap%p==0,next); np=p+1-ap;
  h11=ellpadicregulator(E,p,8,[Q1]); h22=ellpadicregulator(E,p,8,[Q2]);
  h12=(ellpadicregulator(E,p,8,[S])-ellpadicregulator(E,p,8,[D]))/4;
  l1=lg(E,Q1,p,np,8); l2=lg(E,Q2,p,np,8); k=min(valuation(l1,p),valuation(l2,p));
  n1=l2/p^k; n2=-l1/p^k;
  b1=h11*n1+h12*n2; b2=h12*n1+h22*n2; vB=min(valuation(b1,p),valuation(b2,p));
  R=h11*h22-h12^2; vR=valuation(R,p);
  listput(out,[p,ap,vR,k-1,vB]))}
print("[p, a_p, v(Reg_p) (base 2), k_p, vB (base 1)] for ordinary p in 7..400, p notin S_*:");
{for(i=1,#out, my(r=out[i]); if(r[3]!=2||r[4]!=0||r[5]!=1, print("  NONGENERIC ",r)))}
print("ordinary primes tested: ",#out, ";  first rows: ", vector(min(6,#out),i,out[i]));
