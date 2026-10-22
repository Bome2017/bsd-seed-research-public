default(nbthreads,1);
{
my(d=43737, pol=y^2-y-10934, bn=bnfinit(pol,1));
if(bnfcertify(bn)!=1,error("BNF certification failed"));
if(bn.cyc!=[20],error("wrong class group"));
my(rr=Mod(2*y-1,pol), eps=Mod(224*y+23311,pol));
if(norm(eps)!=1,error("unit norm"));
my(X=1778638/9,Y=1169009812/27);
my(f=(X-11*d/3)*(Y+1/2)+rr*(-4*X^2+161*d*X/6-785*d^2/18));
my(fac=idealfactor(bn,f));
for(i=1,matsize(fac)[1],if(fac[i,2]%5,error("ideal not fifth power")));
fac[,2]=fac[,2]/5;
my(J=idealfactorback(bn,fac));
if(J!=[58316/3,51026/3;0,1/3],error("root ideal changed"));
my(cl=bnfisprincipal(bn,J,0));
if(cl!=[8]~,error("wrong root ideal class"));
my(prs=idealprimedec(bn,11), pc=vector(2,i,bnfisprincipal(bn,prs[i],0)[1]));
if(pc!=[5,15],error("wrong split prime classes"));
if(#idealprimedec(bn,5)!=1,error("5 not inert"));
my(ga=Mod(-5829-56*y,pol), abar=Mod(subst(lift(ga),y,1-y),pol), a=ga/abar);
if(norm(ga)!=11^4,error("gamma norm"));
if(a!=Mod((68266265+655984*y)/14641,pol),error("alpha11 wrong"));
if(idealval(bn,a,prs[1])!=4 || idealval(bn,a,prs[2])!=-4,error("alpha valuations"));
print("CERTIFIED_FIELD ",["PARI",version(),"cyclic_class_group",bn.cyc,"root_ideal_class",cl,"split11_classes",pc,"alpha11_valuations",[4,-4]]);
print("ALL_CERTIFIED_FIELD_ASSERTIONS_PASS");
}
