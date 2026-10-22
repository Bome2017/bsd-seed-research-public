\\ D is the frozen retained complete source record, loaded by the case launcher.
alarm(120);gettime();
E=D[1];fA=D[3];T=D[5];G=D[6];ng=#G;
S=matker(D[9]+matid(ng));ns=#S;
AE=vector(ns,j,prod(i=1,ng,G[i]^lift(S[i,j])));
SA=-E.c4/48;SB=-E.c6/864;XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;
coeffcol(v)=vector(8,i,polcoef(lift(v),i-1,w))~;
BT=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w));ww=matsolve(BT,coeffcol(Mod(w,fA)));
fB=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2;
if(!polisirreducible(fB),error("dual line field not irreducible"));NF=nfinit(fB);mm=Mod(z,fB)/6;
GG=x^3-mm^2*x^2+(mm^4+2*SA)*x-(mm^6+2*SA*mm^2-4*SB);
YY=Mod(mm*x-(mm^4+SA)/(2*mm),GG);WW=sum(i=1,8,ww[i]*YY^(i-1));
if(subst(fA,w,WW)!=0,error("source generator relation"));
if(subst(lift(XT),w,WW)!=Mod(x,GG),error("short X mismatch"));
if(subst(lift(YT),w,WW)!=YY,error("short Y mismatch"));
if(Mod(3*x^4+6*SA*x^2+12*SB*x-SA^2,GG)!=0,error("division polynomial mismatch"));
NV=vector(ns,j,norm(subst(lift(AE[j]),w,WW)));
write("norms.gp",[fA,fB,GG,WW,S,AE,NV]);
print("SCALAR_DIM=",ns,";NORMS_COMPUTED=",#NV,";MS=",gettime());
RR=matrix(0,ns);CERT=List();count=0;
DEN=lcm(vector(ns,j,denominator(content(lift(NV[j])))));
{
forprime(q=7,2000,
  if(q%3!=1 || DEN%q==0,next);
  Rts=polrootsmod(fB,q);gg=lift(znprimroot(q));rho=Mod(gg,q)^((q-1)/3);
  for(i=1,#Rts,
    Row=vector(ns);Good=1;Rt=lift(Rts[i]);
    for(j=1,ns,
      Val=subst(lift(NV[j]),z,Mod(Rt,q));
      if(Val==0,Good=0;break);
      Char=Val^((q-1)/3);
      Row[j]=if(Char==1,0,if(Char==rho,1,if(Char==rho^2,2,error("bad cubic character"))))
    );
    if(!Good,next);
    count++;
    Candidate=matconcat([RR;Mat(Mod(Row,3))]);
    if(matrank(Candidate)>matrank(RR),
      RR=Candidate;listput(CERT,[q,Rt,gg,Row]);
      print("NONCUBE_RANK=",matrank(RR),";Q=",q,";ROOT=",Rt)
    )
  )
)
}

K=matker(RR);KR=vector(#K);KV=vector(#K);ok=1;
{for(j=1,#K,KV[j]=prod(i=1,ns,NV[i]^lift(K[i,j]));my(rt=nfroots(NF,x^3-KV[j]));if(#rt==0,ok=0;print("UNRESOLVED_KERNEL_COLUMN=",j),KR[j]=rt[1];if(KR[j]^3!=KV[j],error("false cube root"));print("EXACT_KERNEL_CUBE=",j)));}
write("norm_kernel.gp",[RR,Vec(CERT),K,S*K,KV,KR,ok,count]);
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
write("norm_kernel.json","{\"scalar_dimension\":",ns,",\"norm_residue_rank\":",matrank(RR),",\"kernel_dimension\":",#K,",\"kernel_complete\":",if(ok,"true","false"),",\"scalar_basis\":",jm(S),",\"norm_rows\":",jm(RR),",\"norm_kernel_in_scalar_basis\":",jm(K),",\"norm_kernel_in_full_source\":",jm(S*K),",\"noncube_certificates\":",Vec(CERT),",\"eligible_residue_evaluations\":",count,"}");
print("KERNEL_COMPLETE=",ok,";DIM=",#K,";RESIDUE_EVALUATIONS=",count,";MS=",gettime());quit;
