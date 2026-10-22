default(nbthreads,1);
lg(E,Q,p,np,pr)=ellpadiclog(E,p,pr,ellmul(E,[Q[1]+O(p^(pr+4)),Q[2]+O(p^(pr+4))],np))/np;
{rows=[["control43737",5,[0,0,1,-14959712463303,-22270654620235278500],[[6288329,-11502941299],[8502485,21568458354]]]];}
{foreach(rows,c,
 my(E=ellinit(c[3]),p=c[2],ps=c[4],np=p+1-ellap(E,p),hs,hh,logs,w,nf,br);
 if(E[1..5]!=ellminimalmodel(E)[1..5],error("not minimal"));
 hs=ellpadicheightmatrix(E,p,8,ps);hh=hs*[1,-ellpadics2(E,p,8)]~;
 logs=vector(2,i,lg(E,ps[i],p,np,8)/p);
 w=vecmin(vector(2,i,valuation(logs[i],p)));
 nf=[logs[2],-logs[1]]~/p^w;
 br=hh/p*nf;
 print("GEOMETRY ",[c[1],p,w,lift(Mod(logs,p)),lift(Mod(hh/p,p)),lift(Mod(nf,p)),lift(Mod(br,p)),vecmin(vector(2,i,valuation(br[i],p)))]);
 if(valuation(matdet(hh)-ellpadicregulator(E,p,8,ps),p)<7,error("regulator mismatch"));
 );}
print("DONE");quit;
