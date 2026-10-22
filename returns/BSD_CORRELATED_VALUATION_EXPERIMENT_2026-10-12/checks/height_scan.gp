default(nbthreads,1);
{curves=[["389a1",[0,1,1,-2,0],[[0,0],[1,0]]],
["433a1",[1,0,0,0,1],[[0,1],[-1,1]]],
["655a1",[0,0,1,-13,18],[[1,2],[3,2]]],
["664a1",[0,0,0,-7,10],[[1,2],[3,4]]],
["1615a1",[1,0,0,-215,1192],[[9,-2],[-1,38]]]];}
print("VERSION ",version());
{foreach(curves,c,
 my(E=ellinit(c[2]),G=ellglobalred(E),regv);
 print("CURVE ",c[1]," ",G[1]," ",G[3]," ",elltors(E)[1]);
 forprime(p=5,101,
  if(G[1]%p==0 || ellap(E,p)%p==0 || (p+1-ellap(E,p))%p==0,next);
  regv=ellpadicregulator(E,p,7,c[3]);
  print("ROW ",c[1]," ",p," ",ellap(E,p)," ",valuation(regv,p)," ",padicprec(regv,p)," ",regv);
  write("outputs/height_rows.gp",[c[1],p,ellap(E,p),valuation(regv,p),padicprec(regv,p),regv]);
  ));}
print("DONE");
quit;
