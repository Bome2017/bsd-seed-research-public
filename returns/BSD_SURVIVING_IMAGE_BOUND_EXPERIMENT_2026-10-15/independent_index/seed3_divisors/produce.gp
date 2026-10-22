alarm(90);gettime();
D0=read("inputs/actual_representatives.gp");E=ellinit(D0[1]);T=D0[6];D0=0;nA=read("inputs/nf_only.gp");nA=subst(nA,variable(nA.pol),w);fA=nA.pol;ps=[2,3,2243,4547,5843];
SA=-E.c4/48;SB=-E.c6/864;XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;
BT=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w));ww=matsolve(BT,vector(8,i,i==2)~);ta=sum(i=1,8,ww[i]*(-YT)^(i-1));
if(subst(fA,w,ta)!=0||subst(lift(ta),w,ta)!=Mod(w,fA),error("scalar involution"));
fB=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2;nB=nfinit(fB);mm=Mod(z,fB)/6;
GG=x^3-mm^2*x^2+(mm^4+2*SA)*x-(mm^6+2*SA*mm^2-4*SB);YY=Mod(mm*x-(mm^4+SA)/(2*mm),GG);WW=sum(i=1,8,ww[i]*YY^(i-1));
if(subst(fA,w,WW)!=0||subst(lift(XT),w,WW)!=Mod(x,GG)||subst(lift(YT),w,WW)!=YY,error("incidence geometry"));
if(Mod(3*x^4+6*SA*x^2+12*SB*x-SA^2,GG)!=0,error("affine line not3torsion"));
u(a)=norm(subst(lift(a),w,WW));

PA=concat(vector(#ps,j,idealprimedec(nA,ps[j])));PB=concat(vector(#ps,j,idealprimedec(nB,ps[j])));
approx(nf,PP,k)={my(v=idealappr(nf,matrix(#PP,2,i,j,if(j==1,PP[i],i==k))));v=nfbasistoalg(nf,v);if(vector(#PP,j,nfeltval(nf,v,PP[j]))!=vector(#PP,j,j==k),error("Kronecker valuation failed"));v;};
XA=vector(#PA,k,approx(nA,PA,k));XB=vector(#PB,k,approx(nB,PB,k));
TA=matrix(#PA,#PA,i,j,nfeltval(nA,subst(lift(XA[j]),w,ta),PA[i]));TB=matrix(#PB,#PB,i,j,nfeltval(nB,subst(lift(XB[j]),z,Mod(-z,fB)),PB[i]));
if(TA^2!=matid(#PA)||TB^2!=matid(#PB),error("prime involution"));
IA=select(i->sum(j=i+1,#PA,TA[j,i])==1,[1..#PA]);IB=select(i->sum(j=i+1,#PB,TB[j,i])==1,[1..#PB]);
DA=matrix(#PA,#IA,i,j,(i==IA[j])-TA[i,IA[j]]);DB=matrix(#PB,#IB,i,j,(i==IB[j])-TB[i,IB[j]]);
AA=vector(#IA,j,XA[IA[j]]/subst(lift(XA[IA[j]]),w,ta));NN=vector(#IA,j,u(AA[j]));VA=matrix(#PA,#AA,i,j,nfeltval(nA,AA[j],PA[i]));VB=matrix(#PB,#NN,i,j,nfeltval(nB,NN[j],PB[i]));
if(VA!=DA,error("anti divisor basis"));MD=matsolve(DB,VB);if(DB*MD!=VB||denominator(MD)!=1,error("nonintegral divisor map"));
if(matsize(MD)[1]!=matsize(MD)[2]||matdet(MD)==0,error("divisor norm notfullrank"));TD=valuation(matdet(MD),3);VD=3*MD^-1;if(denominator(VD)!=1,error("reverse composition notintegral"));

write("divisor_certificate.gp",[fA,fB,GG,WW,ta,PA,PB,XA,XB,TA,TB,DA,DB,AA,NN,VB,MD,VD]);
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,A[i,j]));
write("INDEX.json","{\"divisor_rank\":",#IA,",\"forward_divisor_matrix\":",jm(MD),",\"forward_tD\":",TD,",\"source_class_completeness\":\"not recertified\",\"companion_classgroup_computed\":false,\"point_or_selmer_data_used\":false}");
print("DIVISOR_MATRIX=",MD,";TD=",TD,";MS=",gettime());print("INDEPENDENT_INDEX_PRODUCER_COMPLETE");quit;
