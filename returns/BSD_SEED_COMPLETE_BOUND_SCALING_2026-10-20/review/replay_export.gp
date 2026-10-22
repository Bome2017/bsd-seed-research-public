unpack(a)={sum(i=1,#a[1],a[1][i]*w^(i-1))/a[2]};
{
alarm(20);gettime();
C=read("../same_curve_scaling/field.gp");F=C[4];NF=read("../same_curve_scaling/nf.gp");
FU=read("../same_curve_scaling/units_compact.gp")[1];
D=read("../same_curve_scaling/eval_data.json");
if(sum(i=1,#D[1],D[1][i]*w^(i-1))!=F,error("export field"));
if(Mod(unpack(D[2]),F)!=C[6][1]||Mod(unpack(D[3]),F)!=C[6][2]||Mod(unpack(D[4]),F)!=C[7],error("export torsion scalar"));
if(#D[5]!=13,error("export unit count"));
for(j=1,13,
 if(#D[5][j]!=matsize(FU[j])[1],error("factor count"));
 for(i=1,#D[5][j],
  my(a=FU[j][i,1],actual=if(type(a)=="t_COL",nfbasistoalg(NF,a),a));
  if(Mod(unpack(D[5][j][i][1]),F)!=Mod(actual,F),error("export factor binding"));
  if(D[5][j][i][2]!=FU[j][i,2],error("export exponent binding"))
 )
);
print("EXACT_EXPORT_BINDING_PASS;MS=",gettime());quit;
}
