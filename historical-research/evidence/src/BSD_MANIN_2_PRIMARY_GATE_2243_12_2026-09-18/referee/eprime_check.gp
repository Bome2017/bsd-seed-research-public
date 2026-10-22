\\ Referee sanity check: 2-adic exponent e' of S/H for S_2(Gamma_0(N)), v_2(N)=3,
\\ using CNS Prop 5.14 thresholds (weight 2, p=2, n=3):
\\   cusp type a=v_2(L): a=0 -> v >= -3 ; a=1 -> v >= -1 ; a=2 -> v >= 0 ; a=3 -> v >= 0
\\ v = val_2(F|_c) as in CNS (4.2.2): min 2-adic valuation of coefficients of F|_2 gamma, gamma in SL2(Z), gamma(oo)=c.
\\ Read-only check; no files written except stdout.

dedpsi(N)=N*prod(i=1,#factor(N)~,1+1/factor(N)[i,1]);

\\ cache of nf per cyclotomic modulus
NFC=Map();
v2elt(c)=
{
  my(t=type(c),nf,P,best=+oo,m);
  if(c==0,return(+oo));
  if(t=="t_INT"||t=="t_FRAC",return(valuation(c,2)));
  if(t=="t_POLMOD",
    m=c.mod;
    if(!mapisdefined(NFC,m,&nf), nf=nfinit(m); mapput(NFC,m,nf));
    P=idealprimedec(nf,2);
    for(i=1,#P, best=min(best, nfeltval(nf,lift(c),P[i])/P[i].e));
    return(best));
  error("unexpected coefficient type ",t);
}
vexp(E)=my(b=+oo);for(i=1,#E,b=min(b,v2elt(E[i])));b;

thr=[-3,-1,0,0];

run(N,extra)=
{
  my(mf,B,d,n0,M,Lz,F,cols,res,emax=0,g,E,prm,vv,e,L,a,Ls,nt,tag);
  mf=mfinit([N,2],1); B=mfbasis(mf); d=#B;
  n0=floor(2*dedpsi(N)/12)+extra;
  M=matrix(n0+1,d,i,j,mfcoefs(B[j],n0)[i]);
  Lz=matrixqz(M,-2);
  \\ representatives: one cusp 1/L for each 2-type a, with odd part of L = 1
  Ls=[1,2,4,8];
  nt=floor(2*dedpsi(N)/12)+6;
  print("N=",N,"  dim S_2=",d,"  sturm=",floor(2*dedpsi(N)/12),"  #Zbasis=",#Lz);
  cols=vector(#Lz,j,Lz[,j]);
  for(j=1,#cols,
    F=mflinear(mf,mftobasis(mf,Vec(cols[j])));
    vv=vector(4);
    for(a=0,3,
      L=Ls[a+1];
      g=if(a==0,[0,-1;1,0],[1,0;L,1]);
      E=mfslashexpansion(mf,F,g,nt+10,1,&prm);
      vv[a+1]=vexp(E));
    e=0; for(a=1,4, e=max(e, ceil(thr[a]-vv[a])));
    emax=max(emax,e);
    print("  basis ",j,": v(a=0..3)=",vv,"  e'(F)=",e));
  print("  => e'(",N,") = ",emax);
  emax;
}

\\ normalization check on newforms (CNS Thm 5.15 predicts e'=0 for each newform)
checknew(N)=
{
  my(mf,L,F,vv,e,E,prm,Ls=[1,2,4,8],nt);
  mf=mfinit([N,2],0); L=mfeigenbasis(mf);
  nt=floor(2*dedpsi(N)/12)+6;
  for(i=1,#L, F=L[i];
    if(poldegree(mfparams(F)[4])>1 || #mffields(mf)==0, );
    vv=vector(4);
    for(a=0,3, E=mfslashexpansion(mf,F,[1,0;Ls[a+1],1],nt+10,1,&prm); vv[a+1]=vexp(E));
    e=0; for(a=1,4, e=max(e, ceil(thr[a]-vv[a])));
    print("  newform ",i," field ",mfparams(F)[4]," v=",vv," e'=",e));
}
