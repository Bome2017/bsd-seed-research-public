alarm(60);gettime();
B=read("/Users/bsm/BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/work/kb2a_bnf.bin");nf=B.nf;f=nf.pol;xx=variable(f);print("READ_MS=",gettime(),";FIELD=",f,";CLASS=",B.cyc);if(subst(f,xx,w)!=w^8-1188376638*w^4-7030398068360*w^2-117686586145348587,error("A field mismatch"));
cyc=B.cyc;k=#cyc;G=B.gen;tau=Mod(-xx,f);ps=[2,3,2243,4547,5843];SL=concat(vector(#ps,i,idealprimedec(nf,ps[i])));
A=matconcat(vector(k,j,bnfisprincipal(B,nfgaloisapply(nf,tau,G[j]),0)));D=matdiagonal(cyc);LP=matconcat(vector(#SL,j,bnfisprincipal(B,SL[j],0)));H=mathnf(matconcat([D,LP]));HM=mathnf(matconcat([H,A+matid(k)]));OM=mathnf(matconcat([D,A+matid(k)]));
if(denominator(D^-1*(A^2-matid(k)))!=1,error("involution compatibility"));if(denominator(H^-1*A*H)!=1,error("S invariance"));
write("presentation.gp",[f,nf,cyc,G,SL,A,LP,H,HM,OM]);print("TAU=",A,";S_PRIME_CLASSES=",LP,";S_CLASS=",matsnf(H),";S_MINUS=",matsnf(HM),";ORD_MINUS=",matsnf(OM));print("CACHE_INSPECTION_COMPLETE;MS=",gettime());quit;
