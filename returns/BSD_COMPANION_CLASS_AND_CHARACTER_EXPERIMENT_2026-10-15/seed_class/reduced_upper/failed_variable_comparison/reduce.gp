alarm(30);gettime();
F=read("../field.gp");f=F[1];NF=F[2];R=polredbest(NF,1);P=R[1];a=R[2];b=modreverse(a);
if(subst(f,variable(f),a)!=0,error("original root mapping"));if(charpoly(a)!=f,error("characteristic polynomial mapping"));
if(subst(lift(b),variable(b),a)!=Mod(variable(P),P),error("inverse map one"));
if(subst(lift(a),variable(a),b)!=Mod(variable(f),f),error("inverse map two"));
NR=nfinit(P);if(NR.disc!=NF.disc||NR.sign!=NF.sign,error("field invariants"));
write("reduction.gp",[f,P,a,b,NR]);print("REDUCED_POLYNOMIAL=",P);print("ORIGINAL_GENERATOR_IMAGE=",a);print("INVERSE_GENERATOR_IMAGE=",b);print("REDUCE_MS=",gettime());print("REDUCTION_COMPLETE");quit;
