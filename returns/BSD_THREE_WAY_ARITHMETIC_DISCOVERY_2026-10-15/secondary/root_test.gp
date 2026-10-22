alarm(45);z;w;gettime();
{makeembed(E,T,fa)=my(a=-E.c4/48,b=-E.c6/864,XT=T[1]+E.b2/12,YT=T[2]+(E.a1*T[1]+E.a3)/2,mb=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w)),cv=vector(8,i,polcoef(w,i-1,w))~,cc=matsolve(mb,cv),fb=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2,m=Mod(z,fb)/6,g=x^3-m^2*x^2+(m^4+2*a)*x-(m^6+2*a*m^2-4*b),Y=Mod(m*x-(m^4+a)/(2*m),g),W=sum(i=1,8,cc[i]*Y^(i-1)));
 if(subst(fa,w,W)!=0||subst(lift(XT),w,W)!=Mod(x,g)||subst(lift(YT),w,W)!=Y,error("embedding"));[fb,g,W]};
tanval(E,T,P)={my(s=(3*T[1]^2+2*E.a2*T[1]+E.a4-E.a1*T[2])/(2*T[2]+E.a1*T[1]+E.a3));P[2]-T[2]-s*(P[1]-T[1])};
ROWS=List();CERTS=List();
{for(ci=1,3,my(label=[718,1913,28042][ci],D=read(Str("inputs/",label,"_data.gp")),E=D[1],fa=D[3],T=D[5],nf=nfinit(fa),A,types);
 if(ci==1,my(W=read("inputs/718_witness.gp"));A=[W[3],W[6]];types=["false_antiunit","point_unit"];if(W[8]^3!=W[6]/tanval(E,T,D[2][2]),error("point-unit binding")),my(N=read(Str("inputs/",label,"_norm.gp")));A=N[8][1..2];types=["excess_unit_1","excess_unit_2"]);
 my(EM=makeembed(E,T,fa),nfB=nfinit(EM[1]));
 for(j=1,#A,my(alpha=A[j]);if(idealhnf(nf,alpha)!=matid(8),error("input not unit"));my(betaNorm=polresultant(EM[2],lift(subst(lift(alpha),w,EM[3])),x),rr=nfroots(nfB,x^3-betaNorm),rootunit=0);
 if(#rr,if(rr[1]^3!=betaNorm,error("cube identity"));rootunit=idealhnf(nfB,rr[1])==matid(8));
 my(cube=#nfroots(nf,x^3-alpha));if(cube,error("input unexpectedly a cube"));
 if(ci==1&&j==1,if(#rr,error("false antiunit unexpectedly admitted")),if(#rr!=1||!rootunit,error("prediction failure")));
 listput(ROWS,[label,types[j],1,cube,#rr,rootunit]);listput(CERTS,[label,types[j],fa,alpha,EM,betaNorm,rr]);));}
print("ROWS=",Vec(ROWS));write("ROOT_CERTIFICATES.gp",Vec(CERTS));print("COMPLETE;MS=",gettime());quit;
