{
alarm(55);gettime();
C=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp");NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");E=C[1];DP=C[2];T=C[6];SG=C[7];R=readvec("../arithmetic/norm_rows.gp");
PP=[[576,232080],[4547,327384],[5184,281520],[5843,210348],[18188,654768],[23372,1682784]];
if(DP!=elldivpol(E,5) || NF.pol!=C[4] || !ellisoncurve(E,T) || ellmul(E,T,5)!=[0],error("division-point source"));
if(vector(2,j,subst(lift(T[j]),variable(NF.pol),SG))!=ellmul(E,T,2),error("scalar source"));
FX=x^3+E.a2*x^2+E.a4*x+E.a6;OUT=List();KEYS=Map();
for(i=1,#R,my(r=R[i],m=r[2][1],b=r[2][2],tag=r[2][3],P=PP[tag[2]],a=T[2]-m*T[1]-b,nn=nfeltnorm(NF,a));if(mapisdefined(KEYS,Str([m,b])),error("duplicate function"));mapput(KEYS,Str([m,b]),1);if(!ellisoncurve(E,P) || P[2]!=m*P[1]+b,error("point incidence"));if(tag[1]==0,if(2*P[2]*m!=3*P[1]^2+2*E.a2*P[1]+E.a4,error("tangent")),if(tag[1]==1,if(b,error("origin line")),my(Q=PP[tag[3]]);if(!ellisoncurve(E,Q) || tag[4]*Q[2]!=m*Q[1]+b,error("chord"))));if(a!=r[3] || nn!=r[4] || nn!=polresultant(DP,FX-(m*x+b)^2,x)/pollead(DP)^3,error("norm identity"));listput(OUT,[i,m,b,numerator(nn),denominator(nn),r[7],r[8]]));
if(#R!=31,error("function count"));write("line_norm_audit_input.gp",Vec(OUT));write("line_norm_integer_input.gp",vector(#OUT,i,[OUT[i][1],OUT[i][4],OUT[i][5],OUT[i][6],OUT[i][7]]));print("INDEPENDENT_LINE_NORM_REPLAY_COMPLETE;FUNCTIONS=31;MS=",gettime());quit;
}
