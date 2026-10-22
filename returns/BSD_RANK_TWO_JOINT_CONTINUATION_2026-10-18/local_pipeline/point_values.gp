facrows(n)={my(M=factor(abs(n)));vector(#M~,j,Vec(M[j,]))};
{alarm(10);gettime();
E=ellinit([0,1,1,-2,0]);P=[0,0];R=[-1,1];Q=elladd(E,P,R);DP=elldivpol(E,7);
V389=vector(3,i,subst(DP,x,[P,R,Q][i][1]));
F=ellinit([0,0,1,-13,18]);P=[1,2];R=[3,2];Q=elladd(F,P,R);DP=elldivpol(F,7);
V655=vector(5,i,subst(DP,x,[1,3,-4,2,-4][i]));
if(Q!=[-4,-3]||ellmul(F,P,2)!=[2,-1],error("point arithmetic mismatch"));
if(4*(x^3-13*x+18)+1-(-4*x+9)^2!=4*(x-1)^2*(x-2),error("tangent identity"));
TANGENTNORM=V655[1]^2*V655[4]/7^3;
NF=read("/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/rank_two_source/nf.gp");FD=read("/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/rank_two_source/field.gp");if(nfeltnorm(NF,FD[6][2]+2*FD[6][1]-4)!=TANGENTNORM,error("direct norm mismatch"));
write("TANGENT_NORM.json",[numerator(TANGENTNORM),denominator(TANGENTNORM),facrows(numerator(TANGENTNORM)),facrows(denominator(TANGENTNORM))]);
if(V389!=[-2357,-16715917,18041]||V655!=[2197265625,-1831360821,-11566477556396484375,-15669,-11566477556396484375],error("division values mismatch"));
write("POINT_VALUES.json",[V389,V655,vector(3,i,facrows(V389[i])),vector(5,i,facrows(V655[i]))]);
print("POINT_VALUES_COMPLETE;389=",V389,";655=",V655,";MS=",gettime());quit;}
