read("relative_setup.gp");
sigelt(a,k) = {for(t=1,k,a=subst(lift(a),w,SG));a;};
sigideal(ID,k) = {for(t=1,k,ID=ai(ID));ID;};
acceptcycle(ii,jj,kk) = {
  my(Bi=BR[ii],Bj=BR[jj],ga,ct,LH,RH,u,rr2,rr3,key);
  key=Str([ii,jj,kk]);if(mapisdefined(CM,key),return());mapput(CM,key,1);
  if(Bi[7]!=sigideal(Bj[7],kk),error("scalar cycle identity"));
  ga=Bi[5]/sigelt(Bj[5],kk);ct=idealdiv(NF,Bi[6],sigideal(Bj[6],kk));
  LH=idealdiv(NF,Bi[4],sigideal(Bj[4],kk));RH=idealmul(NF,idealhnf(NF,ga),ct);
  if(LH!=RH||ti(ct)!=ct,error("cycle principal witness"));
  rr2=lift(Mod(Bi[3]-2^kk*Bj[3],5));rr3=lift(Mod(Bi[3]-3^kk*Bj[3],5));
  listput(R2,rr2);listput(R3,rr3);write("closed_cycles.gp",[ii,jj,kk,ga,ct,rr2,rr3]);
  if(Bi[4]==sigideal(Bj[4],kk),
    u=ga/ta(ga);
    if(idealhnf(NF,u)!=matid(24)||u*ta(u)!=1,error("relative unit cycle"));
    if(u!=1&&u!=-1&&!mapisdefined(UM,Str(u)),mapput(UM,Str(u),1);UN++;write("unit_cycles.gp",[UN,ii,jj,kk,u]);print("ACTUAL_RELATIVE_UNIT;ID=",UN))
  );
};
{
alarm(175);gettime();relative_setup();BR=readvec("batch_rows.gp");MM=Map();CM=Map();UM=Map();R2=List();R3=List();UN=0;
for(ii=1,#BR,
  JJ=BR[ii][7];
  if(JJ==matid(24),listput(R2,lift(Mod(BR[ii][3],5)));listput(R3,lift(Mod(BR[ii][3],5)));write("principal_original.gp",[ii,BR[ii][3]]));
  for(kk=0,3,
    key=Str(JJ);
    if(mapisdefined(MM,key,&old),
      if(old[1]!=ii||old[2]!=kk,acceptcycle(ii,old[1],lift(Mod(old[2]-kk,4)))),
      mapput(MM,key,[ii,kk])
    );
    JJ=ai(JJ)
  )
);
RR2=if(#R2,matrix(#R2,#ORB,i,j,R2[i][j]),matrix(0,#ORB));RR3=if(#R3,matrix(#R3,#ORB,i,j,R3[i][j]),matrix(0,#ORB));
RK2=if(#R2,matrank(Mod(RR2,5)),0);RK3=if(#R3,matrank(Mod(RR3,5)),0);
write("closed_relation_matrices.gp",[RR2,RR3]);
write("cycle_result.gp",[#BR,#ORB,#R2,RK2,RK3,UN,#Mat(MM)[,1]]);
print("RELATIVE_CYCLE_ANALYSIS_COMPLETE;ROWS=",#BR,";SELECTED_GENERATORS=",#ORB,";CYCLE_ROWS=",#R2,";RANK_CHI2=",RK2,";RANK_CHI3=",RK3,";UNITS=",UN,";MS=",gettime());quit;
}
