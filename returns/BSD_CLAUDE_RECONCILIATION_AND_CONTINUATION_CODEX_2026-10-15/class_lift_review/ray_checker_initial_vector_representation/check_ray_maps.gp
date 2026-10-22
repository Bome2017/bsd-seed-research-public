alarm(60);
C=read("certificate.gp");Q=read("quotient_certificate.gp");RAY=read("ray.bin");RR=read("ray_coordinates.gp");nf=C[1];
F=Q[1];EL=Q[2];KG=Q[3];CY=Q[6];
if(CY!=matdiagonal(RAY.cyc),error("wrong ray cyclic matrix"));
if(idealpow(nf,C[5],3)!=idealhnf(nf,C[6]),error("literal J cube mismatch"));
if(idealnorm(nf,C[7])!=3^14*389^4,error("modulus norm mismatch"));
{my(col=0);for(i=1,matsize(F)[1],my(bid=idealstar(nf,idealpow(nf,F[i,1],F[i,2]),2));for(j=1,#bid.cyc,col++;my(g=EL[col]);for(k=1,matsize(F)[1],my(t=if(k==i,bid.gen[j],1));if(nfeltval(nf,g-t,F[k,1])<F[k,2],error("actual CRT congruence failed")));if(bnrisprincipal(RAY,idealhnf(nf,g),0)!=KG[,col],error("actual principal ideal to ray coordinate failed"))));if(col!=#EL,error("CRT column count"));print("ACTUAL_CRT_AND_PRINCIPAL_RAY_COLUMNS_VERIFIED=",col);}
if(Q[14]*Q[15]!=Mod(matid(matsize(Q[14])[1]),3),error("old log basis right inverse"));
if(Q[5]!=KG*Q[15],error("KS basis transport mismatch"));if(Q[9]!=Q[5]*lift(C[11]),error("allowance mismatch"));
RAW=matconcat([CY,3*KG]);FINAL=matconcat([CY,3*KG,Q[9]]);
if(mathnf(RAW)!=Q[7]||mathnf(FINAL)!=Q[10],error("actual relation lattice differs"));
if(Q[18][1]*Q[7]*Q[18][2]!=Q[18][3]||Q[19][1]*Q[10]*Q[19][2]!=Q[19][3],error("Smith transformations fail"));
if(RAW*Q[17]!=RR[3]-Q[13][,1],error("beta residue relation fails"));if(FINAL*Q[16]!=3*RR[2],error("3J final relation fails"));
ORD(S,v)={my(w=S[1]*v,o=1);for(i=1,#w,o=lcm(o,S[3][i,i]/gcd(S[3][i,i],w[i])));o;};
if(ORD(Q[18],RR[2])!=9||ORD(Q[19],RR[2])!=3,error("lift orders mismatch"));
if(select(x->x>1,matsnf(Q[7]))!=[9,3,3,3,3,3]||select(x->x>1,matsnf(Q[10]))!=[3,3,3,3],error("quotient invariant mismatch"));
if(C[12]*C[10]!=0*(C[12]*C[10]),error("residual class boundary nonzero"));
print("OLD_LOCAL_LOG_TRANSPORT_VERIFIED");print("LITERAL_IDEAL_CUBE_AND_ACTUAL_INTEGER_RELATIONS_VERIFIED");print("RAW_QUOTIENT=[9,3,3,3,3,3];FINAL_QUOTIENT=[3,3,3,3];LIFT_ORDERS=[9,3]");print("INDEPENDENT_RAY_MAP_REVIEW_PASS");quit;
