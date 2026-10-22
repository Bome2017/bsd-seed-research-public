pack(a)={my(b=lift(a),den=denominator(b,1));[vector(24,i,polcoef(b*den,i-1,w)),den]};
{alarm(58);gettime();C=read("../p5_arithmetic/field.gp");NF=read("../p5_arithmetic/nf.gp");FU=read("../p5_arithmetic/units_compact.gp")[1];FS=List();EX=List();
for(j=1,#FU-1,my(f=FU[j],rows=List());for(i=1,matsize(f)[1],my(a=f[i,1],b=if(type(a)=="t_COL",nfbasistoalg(NF,a),a));listput(rows,[pack(b),f[i,2]]));listput(FS,Vec(rows)));
write("eval_data.json",[vector(25,i,polcoef(C[4],i-1,w)),pack(C[6][1]),pack(C[6][2]),pack(C[7]),Vec(FS)]);
print("COMPACT_UNIT_EXPORT_PASS;UNITS=",#FS,";MS=",gettime());quit;}
