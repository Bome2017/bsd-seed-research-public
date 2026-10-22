lineadd(m,b,tag)={my(key=Str([m,b]));if(!mapisdefined(LM,key),mapput(LM,key,1);listput(LINES,[m,b,tag]));};
{
alarm(115);gettime();C=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp");NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");E=C[1];DP=C[2];T=C[6];SG=C[7];
PP=[[576,232080],[4547,327384],[5184,281520],[5843,210348],[18188,654768],[23372,1682784]];
for(i=1,#PP,if(!ellisoncurve(E,PP[i]),error("source point not on seed")));
LINES=List();LM=Map();
for(i=1,#PP,
 xx=PP[i][1];yy=PP[i][2];m=(3*xx^2+2*E.a2*xx+E.a4)/(2*yy);lineadd(m,yy-m*xx,[0,i]);lineadd(yy/xx,0,[1,i]);
 for(j=i+1,#PP,for(s=-1,1,if(s==0,next);m=(s*PP[j][2]-yy)/(PP[j][1]-xx);lineadd(m,yy-m*xx,[2,i,j,s])))
);
RR=List();passes=0;fx=x^3+E.a2*x^2+E.a4*x+E.a6;
for(i=1,#LINES,
 m=LINES[i][1];b=LINES[i][2];a=T[2]-m*T[1]-b;if(a==0,error("zero source"));nn=nfeltnorm(NF,a);res=polresultant(DP,fx-(m*x+b)^2,x)/pollead(DP)^3;if(nn!=res,error("norm/resultant mismatch"));
 fn=factor(abs(numerator(nn)),419776);fd=factor(denominator(nn),419776);bad=1;
 for(j=1,matsize(fn)[1],if(fn[j,1]>419775,bad*=fn[j,1]^fn[j,2]));for(j=1,matsize(fd)[1],if(fd[j,1]>419775,bad*=fd[j,1]^fd[j,2]));
 ok=bad==1;if(ok,passes++);
 row=[i,LINES[i],a,nn,fn,fd,bad,ok];listput(RR,row);write("norm_rows.gp",row);
 print("GEOMETRIC_NORM;ROW=",i,";NUMERATOR_DIGITS=",#Str(abs(numerator(nn))),";OUTSIDE_COFACTOR_DIGITS=",#Str(bad),";ADMITTED=",ok)
);
write("norm_screen_result.gp",[#LINES,passes]);print("NORM_SCREEN_COMPLETE;FUNCTIONS=",#LINES,";RATIONAL_SUPPORT_PASSES=",passes,";MS=",gettime());quit;
}
