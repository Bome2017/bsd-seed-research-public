alarm(30);
Es=[["seed",[0,-22735,0,106272484,0]],["389a1",[0,1,1,-2,0]],["37a1",[0,0,1,-1,0]]];
{for(ee=1,#Es,
 E=ellinit(Es[ee][2]); curve=Es[ee][1];
 ms=if(ee==1,[-144,-72,-24,-12,-6,-3,-2,-1,0,1,2,3,6,12,24,72,144],vector(25,i,i-13));
 bs=if(ee==1,Set(concat(vector(25,i,i-13),[-1309536,-1126080,-654768,-563040,-327384,-281520,281520,327384,563040,654768,1126080,1309536])),vector(25,i,i-13));
 for(pp=1,3,
 p=[5,7,11][pp]; D=elldivpol(E,p); C=4*x^3+E.b2*x^2+2*E.b4*x+E.b6;
 SS=Set(concat([2,p],factor(abs(E.disc))[,1]~)); rows=List(); good=List();
 for(i=1,#ms,for(j=1,#bs,
 m=ms[i]; b=bs[j]; Q=(m*x+b)^2-C;N=norm(Mod(D,Q))*pollead(Q)^poldegree(D); R=abs(N); vv=vector(#SS,k,0);
 if(R==0,error("rational p torsion intersection"));
 for(k=1,#SS,vv[k]=valuation(R,SS[k]);R=R/SS[k]^vv[k]);
 listput(rows,[m,b,N,vv,R]);if(R==1,listput(good,[m,b,vv]));
 ));
 fn=Str("direct_",curve,"_",p,".json");write(fn,Str("{\"curve\":\"",curve,"\",\"p\":",p,",\"S\":",SS,",\"candidates\":",Vec(rows),",\"source_Sunit_candidates\":",Vec(good),"}"));
 print(curve," p",p," tested=",#rows," Sunit=",#good," good=",Vec(good));
 ));}
print("EXACT_RESULTANT_SOURCE_SCREEN_COMPLETED");quit;
