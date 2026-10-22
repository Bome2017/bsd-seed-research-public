alarm(90);gettime();B=read("bnf.bin");C=read("certification.gp");if(C[1]!=1,error("uncertified class source"));f=read("field.gp")[1];B=subst(B,variable(B.pol),z);nf=B.nf;if(nf.pol!=f,error("field mismatch"));tau=Mod(-z,f);cyc=B.cyc;k=#cyc;G=B.gen;ps=[2,3,2243,4547,5843];SL=concat(vector(#ps,i,idealprimedec(nf,ps[i])));
A=matconcat(vector(k,j,bnfisprincipal(B,nfgaloisapply(nf,tau,G[j]),0)));D=matdiagonal(cyc);LP=matconcat(vector(#SL,j,bnfisprincipal(B,SL[j],0)));H=mathnf(matconcat([D,LP]));
if(denominator(D^-1*(A^2-matid(k)))!=1,error("class involution"));if(denominator(H^-1*A*H)!=1,error("S class subgroup not stable"));
HM=mathnf(matconcat([H,A+matid(k)]));HP=mathnf(matconcat([H,A-matid(k)]));OM=mathnf(matconcat([D,A+matid(k)]));OP=mathnf(matconcat([D,A-matid(k)]));
SINV=matsnf(H);MINV=matsnf(HM);PINV=matsnf(HP);OMINV=matsnf(OM);OPINV=matsnf(OP);
v3len(M)=valuation(abs(matdet(M)),3);r3(M)=#select(a->a%3==0,matsnf(M));
if(v3len(H)!=v3len(HM)+v3len(HP)||v3len(D)!=v3len(OM)+v3len(OP),error("plusminus length decomposition"));
TI=vector(k,j,nfgaloisapply(nf,tau,G[j]));AA=concat(TI,SL);EX=matconcat([A,LP]);ROOTS=vector(#AA);QQ=vector(#AA);
{for(j=1,#AA,my(Q=idealmul(nf,AA[j],idealinv(nf,idealfactorback(nf,G,EX[,j]))),pr=bnfisprincipal(B,Q,5),I=matid(8));if(pr[1]!=0*pr[1],error("principalization nonzero class"));for(i=1,#pr[2]~,I=idealmul(nf,I,idealpow(nf,idealhnf(nf,pr[2][i,1]),pr[2][i,2])));if(idealhnf(nf,I)!=idealhnf(nf,Q),error("literal principalization mismatch"));ROOTS[j]=pr[2];QQ[j]=Q);}
write("class_certificate.gp",[f,nf,G,cyc,SL,A,LP,H,HM,HP,OM,OP,QQ,ROOTS]);
jm(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j]));
write("CLASS_RESULT.json","{\"certified\":true,\"ordinary_invariants\":",cyc,",\"ordinary_3_length\":",v3len(D),",\"ordinary_minus_3_length\":",v3len(OM),",\"ordinary_plus_3_length\":",v3len(OP),",\"S_invariants\":",SINV,",\"S_3_length\":",v3len(H),",\"S_minus_invariants\":",MINV,",\"S_minus_3_length\":",v3len(HM),",\"S_minus_3_rank\":",r3(HM),",\"S_plus_3_length\":",v3len(HP),",\"class_involution\":",jm(A),",\"S_prime_classes\":",jm(LP),",\"seed_tD\":1,\"independent_global_upper_bound\":",2+v3len(HM),",\"S_prime_rational_support\":",ps,"}");
print("ORDINARY_CLASS=",cyc,";S_CLASS=",SINV,";MINUS_S_3_LENGTH=",v3len(HM),";UPPER_BOUND=",2+v3len(HM),";MS=",gettime());print("CLASS_ANALYSIS_COMPLETE");quit;
