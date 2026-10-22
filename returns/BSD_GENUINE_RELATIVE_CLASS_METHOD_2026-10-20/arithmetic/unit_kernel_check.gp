read("relative_setup.gp");
{
alarm(115);gettime();relative_setup();BR=readvec("batch_rows.gp");KD=read("integer_kernel_data.gp");KK=KD[2];KS=KD[3];UU=vector(2*#BR);done=vector(2*#BR);units=List();seen=Map();RR=List();
for(h=1,#KS,
 j=KS[h][3];u=Mod(1,NF.pol);
 for(i=1,2*#BR,if(KK[i,j],
   if(!done[i],a=BR[(i+1)\2][5];if(i%2==0,a=subst(lift(a),w,SG));UU[i]=a/ta(a);done[i]=1);
   u*=UU[i]^KK[i,j]
 ));
 if(idealhnf(NF,u)!=matid(24)||u*ta(u)!=1,error("kernel multiplier is not a relative unit"));
 cls=if(u==1,1,if(u==-1,-1,0));listput(RR,[j,KS[h][1],cls]);
 if(cls==0&&!mapisdefined(seen,Str(u)),mapput(seen,Str(u),1);listput(units,[j,KK[,j],u]);write("genuine_relative_units.gp",[j,KK[,j],u]);print("NONTRIVIAL_RELATIVE_UNIT;KERNEL_COLUMN=",j));
);
write("unit_kernel_result.gp",[Vec(RR),#units]);
print("UNIT_KERNEL_CHECK_COMPLETE;KERNEL_COLUMNS=",#KS,";NONTRIVIAL_UNITS=",#units,";PLUS_ONE=",#select(r->r[3]==1,Vec(RR)),";MINUS_ONE=",#select(r->r[3]==-1,Vec(RR)),";MS=",gettime());quit;
}
