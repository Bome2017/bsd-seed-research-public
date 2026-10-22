action(a)=subst(lift(a),VV,SG);
{
alarm(115);gettime();
C=read("/Users/bsm/BSD_CLOSED_CLASS_CONSTRUCTION_2026-10-20/inputs/seed_field.gp");
NF=read("/Users/bsm/BSD_CLOSED_CLASS_CONSTRUCTION_2026-10-20/inputs/seed_nf.gp");
E=C[1];T=C[6];SG=C[7];VV=variable(NF.pol);
if(!ellisoncurve(E,T)||ellmul(E,T,5)!=[0],error("point"));
if(vector(2,j,action(T[j]))!=ellmul(E,T,2),error("scalar"));
T2=ellmul(E,T,2);T3=ellmul(E,T,3);T4=ellmul(E,T,4);
if(T3!=[T2[1],-T2[2]]||T4!=[T[1],-T[2]],error("torsion symmetry"));
ELS=[T[1],T2[1],T[2],T2[2],T[1]-T2[1],T2[2]/T[2],T2[1]/T[1]];
NAMES=["x(P)","x(2P)","y(P)","y(2P)","x(P)-x(2P)","y(2P)/y(P)","x(2P)/x(P)"];
BAD=[2,3,5,2243,4547,5843];PRS=vector(#BAD,j,idealprimedec(NF,BAD[j]));OUT=List();
for(i=1,#ELS,my(a=ELS[i],t=action(action(a))/a,nn=nfeltnorm(NF,a),ex=vector(#BAD),cof,imgs=vector(4),witnesses=vector(2),II=matid(24),vals=List());
if(t!=1&&t!=-1,error("not parity eigenvector"));
cof=abs(nn);for(j=1,#BAD,ex[j]=valuation(cof,BAD[j]);cof/=BAD[j]^ex[j]);if(cof!=1,error("new norm support"));
for(j=1,#BAD,for(k=1,#PRS[j],my(vv=idealval(NF,a,PRS[j][k]));if(vv,II=idealmul(NF,II,idealpow(NF,PRS[j][k],vv)));listput(vals,[BAD[j],k,vv])));if(II!=idealhnf(NF,a),error("incomplete prime support"));
imgs[1]=a;for(j=2,4,imgs[j]=action(imgs[j-1]));if(action(imgs[4])!=a,error("order4"));
for(cc=1,2,my(lam=if(cc==1,2,3),ee=vector(4,j,lift(Mod(lam,5)^(-(j-1)))),bb=prod(j=1,4,imgs[j]^ee[j]),root=(imgs[1]*imgs[2])*t^((ee[3]+ee[4])%2));
if(root^5!=bb,error("fifth power witness"));witnesses[cc]=[lam,ee,root,1]);
listput(OUT,[NAMES[i],nn,ex,t,Vec(vals),witnesses]));
write("TORSION_SUNIT_RESULT.gp",Vec(OUT));print("TORSION_SUNIT_ADMISSION_COMPLETE;ELEMENTS=",#ELS,";FAITHFUL_CHECKS=",2*#ELS,";MS=",gettime());quit;
}
