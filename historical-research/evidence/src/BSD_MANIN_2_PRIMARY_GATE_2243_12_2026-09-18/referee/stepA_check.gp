\\ Referee check of Step A on small levels with v_2(N)=3 and a prime = 3 mod 4 dividing N.
\\ S = S_2(Gamma_0(N)) with Z_(2)-integral q-expansion at oo; H = forms meeting CNS (5.14.1) at p=2.
\\ For an optimal curve with newform f (c0 = 1 from Cremona's table):
\\   kappa = v_2[P_chi(H) : Z_(2) f],  rE = v_2[P_chi(S) : Z_(2) f] (= v_2 of congruence number),
\\   e' = 2-exponent of S/H.
\\ Step A predicts:  kappa <= v2(deg phi) - v2(c0)   and   v2(deg phi) <= rE <= e' + kappa.

dedpsi(N)=N*prod(i=1,#factor(N)~,1+1/factor(N)[i,1]);
thr=[-3,-1,0,0];
NFC=Map();
getnf(m)=my(nf);if(!mapisdefined(NFC,m,&nf),nf=nfinit(m);mapput(NFC,m,nf));nf;

\\ rows of 2-local integrality conditions for one cusp type
condrows(Ev,t)=
{
  my(d=#Ev,n=#Ev[1],rows=List(),c,nf,m,v,k);
  for(j=1,n,
    m=0; for(i=1,d, c=Ev[i][j]; if(type(c)=="t_POLMOD", m=c.mod; break));
    if(m==0,
      listput(rows, vector(d,i,2^(-t)*Ev[i][j])),
      nf=getnf(m);
      v=vector(d,i, my(c=Ev[i][j]); nfalgtobasis(nf, if(type(c)=="t_POLMOD",lift(c),c)));
      for(k=1,poldegree(m), listput(rows, vector(d,i,2^(-t)*v[i][k])))));
  matrix(#rows,d,r,i,rows[r][i]);
}
mat2(T)=
{
  my(D=denominator(T),a=valuation(D,2),b=D/2^a,M,K,d=#T);
  if(a==0,return(matid(d)));
  M=b*2^a*T;
  K=matkermod(M,2^a);
  mathnf(concat(K,2^a*matid(d)));
}

run(N,curves)=
{
  my(mf,B,d,n0,M,X,cols,Ev,T,Hb,nt,ex,eprime,gam,Ls=[1,2,4,8],Fint,newf,fc,W,Pinv,kap,rE,E,ok,a,j,i,prm,Tl,cv,ci);
  mf=mfinit([N,2],1); B=mfbasis(mf); d=#B;
  n0=floor(2*dedpsi(N)/12)+8;
  M=matrix(n0+1,d,i,j,mfcoefs(B[j],n0)[i]);
  X=matrixqz(M,-2);                         \\ integral q-expansion vectors (columns)
  X=matrix(d,d,i,j,mftobasis(mf,Vec(X[,j]))[i]);  \\ integral basis in mfbasis coordinates
  Fint=vector(d,j,mflinear(mf,X[,j]));
  nt=floor(2*dedpsi(N)/12)+10;
  T=matrix(0,d);
  for(a=0,2,
    gam=if(a==0,[0,-1;1,0],[1,0;Ls[a+1],1]);
    Ev=vector(d,j,mfslashexpansion(mf,Fint[j],gam,nt,1,&prm));
    T=concat(T~,condrows(Ev,thr[a+1])~)~);
  Hb=mat2(T);                                \\ H in integral-basis coordinates (columns)
  ex=matsnf(Hb); eprime=vecmax(apply(x->valuation(x,2),ex));
  print("N=",N," dim=",d," [S:H] 2-part=2^",valuation(matdet(Hb),2)," elementary divisors=",ex," e'=",eprime);
  \\ Hecke complement W = sum_l Im(T_l - a_l(f))
  for(ci=1,#curves, cv=curves[ci];
    E=ellinit(cv[1]);
    newf=0;
    foreach(mfeigenbasis(mf),g, if(poldegree(mfparams(g)[4])==1,
      ok=1; forprime(l=3,40, if(N%l, if(mfcoef(g,l)!=ellap(E,l), ok=0; break)));
      if(ok, newf=g)));
    if(type(newf)!="t_VEC", print("  no newform matched ",cv),
      fc=mftobasis(mf,newf); if(type(fc)=="t_VEC",fc=fc~);
      W=matrix(d,0);
      forprime(l=3,60, if(N%l, Tl=mfheckemat(mf,l); W=concat(W,Tl-mfcoef(newf,l)*matid(d))));
      W=matimage(W);
      Pinv=concat(fc,W)^(-1);
      kap=-vecmin(vector(d,j,valuation((Pinv*(X*Hb[,j]))[1],2)));
      rE=-vecmin(vector(d,j,valuation((Pinv*X[,j])[1],2)));
      print("  curve ",cv[1]," deg phi=",cv[2]," v2(deg)=",valuation(cv[2],2),"  rank W=",#W,
          "  kappa=",kap,"  v2(r_E)=",rE,"  e'=",eprime,
          "  [A.4 kappa<=v2deg: ",kap<=valuation(cv[2],2),"] [ARS v2deg<=rE: ",valuation(cv[2],2)<=rE,"] [A.5 rE<=e'+kappa: ",rE<=eprime+kap,"]")));
}
