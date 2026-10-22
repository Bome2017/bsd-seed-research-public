alarm(25);read("cubinv.gp");read("classimg.gp");read("selmer.gp");setrand(20261013);gettime();
nf=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/nf_only.gp");D=read("stage1_data.gp");G=D[1];H0=D[3];TAU=D[4];LR=D[5];AC=D[6];UD=read("stage3_data.gp");UB=UD[4];Norm=TAU+matid(15);
B0=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/actual_representatives.gp");E=ellinit(B0[1]);T=B0[6];ps=[2,3,2243,4547,5843];Rows=[;];Info=List();
{for(i=1,#ps,my(l=ps[i],Dl=[locdata(nf,pr)|pr<-idealprimedec(nf,l)],Bl=lockummer(E,nf,T,l,Dl,40),Ml=matconcat(vector(#G,j,Mod(concat(vector(#Dl,q,locvec(nf,G[j],Dl[q]))),3)~)),Rr=if(Bl[2]==0,Ml,matker(Bl[1]~)~*Ml));listput(Info,[l,Dl,Bl,Ml,Rr]);Rows=if(#Rows,matconcat([Rows;Rr]),Rr);write("local_checkpoints.gp",[l,Dl,Bl,Ml,Rr]);print("LOCAL_DONE=",l,"; rankrows=",matrank(Rr),"; locdim=",Bl[2],"; elapsed_ms=",gettime()));}
if(Rows*AC!=0*(Rows*AC),error("local screens reject certified classes"));
print("LOCAL_FULL_DIM=",#matker(Rows),"; LOCAL_UNRAMIFIED_DIM=",#matker(Rows*H0),"; LOCAL_UNIT_DIM=",#matker(Rows*UB));
print("LOCAL_NORM_UNIT_DIM=",#matker(matconcat([Rows;Norm])*UB));
print("LOCAL_GLOBAL_FULL_DIM=",#matker(matconcat([Rows;Norm;LR])));
print("LOCAL_ROWS=",lift(Rows));write("stage4_local_data.gp",[Rows,Vec(Info)]);print("LOCAL_COMPLETE");quit;
