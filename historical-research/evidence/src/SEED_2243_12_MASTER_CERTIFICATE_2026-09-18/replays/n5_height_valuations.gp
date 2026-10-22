\\ Valuations of PARI's 5-adic height pairing entries on several models (needed for the N5 invariance argument).
m=2243; n=12; A=m+16*n^2; B=m+25*n^2; E=ellinit([0,-5*A,0,4*A*B,0]); P1=[A,6*n*A]; P2=[36*n^2,12*n*(m-2*n^2)];
hp(EE,X,Y)=my(a=ellpadicheight(EE,5,12,elladd(EE,X,Y)),b=ellpadicheight(EE,5,12,X),c=ellpadicheight(EE,5,12,Y)); if(type(a)=="t_VEC", a=a[1];b=b[1];c=c[1]); (a-b-c)/2;
H(EE,Q)=matrix(2,2,i,j, if(i==j, my(t=ellpadicheight(EE,5,12,Q[i])); if(type(t)=="t_VEC",t[1],t), hp(EE,Q[i],Q[j])));
for(k=0,2, r=[0,1,7578][k+1]; v=[1,r,0,0]; Er=ellchangecurve(E,v); Q=ellchangepoint([P1,P2],v); M=H(Er,Q); print("r=",r," b2=",Er.b2," ord5 of [h11,h12,h22] = ", [valuation(M[1,1],5), valuation(M[1,2],5), valuation(M[2,2],5)], "  ord5 det = ", valuation(matdet(M),5), "  det/ellpadicregulator ord = ", valuation(matdet(M)/ellpadicregulator(Er,5,12,Q),5)));
