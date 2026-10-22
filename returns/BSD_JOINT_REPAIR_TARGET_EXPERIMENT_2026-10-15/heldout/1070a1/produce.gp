alarm(120);gettime();
D=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14/arithmetic/1070a1/data.gp");B=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14/search/1070a1/bnf.bin");nf=B.nf;E=D[1];T=D[5];G=D[6];
read("/Users/bsm/BSD_CLAUDE_RECONCILIATION_AND_CONTINUATION_CODEX_2026-10-15/class_lift/mirror389/lib/selmer.gp");
fl=vector(#G,j,flat(nf,G[j]));
ratc(a)=[numerator(a),denominator(a)];
pc(a)=vector(8,i,ratc(polcoef(lift(a),i-1,w)));
FF=vector(#G,j,vector(#fl[j],k,[pc(fl[j][k][1]),fl[j][k][2]]));
write("source.json","{\"model\":",vector(5,i,E[i]),",\"field\":",vector(9,i,polcoef(nf.pol,i-1)),",\"torsion_point\":",vector(2,i,pc(T[i])),",\"source_factors\":",FF,"}");
{produce()=my(q=10000,got=0,disc=poldisc(nf.pol));
while(got<12 && q<200000,
 q=nextprime(q+1);if(q>200000,break);if(q%3!=1||disc%q==0||E.disc%q==0,next);
 my(rs=polrootsmod(nf.pol,q));if(#rs!=8,next);
 my(Eq=ellinit(E,q),pts,chi,om=znprimroot(q)^((q-1)/3),ok=1);
 iferr(pts=vector(8,i,[subst(lift(T[1]),w,rs[i]),subst(lift(T[2]),w,rs[i])]),er,ok=0);if(!ok,next);
 for(i=1,8,if(!ellisoncurve(Eq,pts[i])||ellmul(Eq,pts[i],3)!=[0],error("torsion root mismatch")));
 chi=vector(8,i,vector(#G,j,my(sm=0);for(k=1,#fl[j],my(v,u);v=iferr(subst(lift(fl[j][k][1]),w,rs[i]),er,ok=0;0);if(!ok||v==0,ok=0;break);u=v^((q-1)/3);if(u!=1&&u!=om&&u!=om^2,error("cubic symbol"));sm+=fl[j][k][2]*if(u==1,0,u==om,1,2));sm%3));if(!ok,next);
 my(rr=List(),tt=List());
 for(i=1,8,for(j=i,8,my(Q=elladd(Eq,pts[i],pts[j]));if(Q==[0],next);my(kq=0);for(k=1,8,if(pts[k]==Q,kq=k));if(!kq,error("torsion sum"));listput(tt,[i-1,j-1,kq-1]);listput(rr,(chi[i]+chi[j]-chi[kq])%3)));
 if(#rr!=32,error("triple count"));
 write("blocks.jsonl","{\"label\":",q,",\"q\":",q,",\"roots\":",Vec(lift(rs)),",\"omega\":",lift(om),",\"points\":",vector(8,i,vector(2,j,lift(pts[i][j]))),",\"characters\":",chi,",\"triples\":",Vec(tt),",\"rows\":",Vec(rr),"}");got++;
);
if(got!=12,error("bounded split-prime selection exhausted"));print("HELDOUT_BLOCK_PRODUCER_PASS;PRIMES=",got,";MS=",gettime());}
produce();quit;
