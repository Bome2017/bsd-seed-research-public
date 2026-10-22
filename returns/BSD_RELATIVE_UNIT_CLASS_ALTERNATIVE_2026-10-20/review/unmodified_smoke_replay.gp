{main()=
alarm(35);B1=read("../memory_diagnosis/smoke_bnf.bin");NF=B1.nf;B0=bnfinit(NF,1);if(bnfcertify(B0)!=1||bnfcertify(B1)!=1,error("unmodified class certification"));if(B0.cyc!=B1.cyc||B0.no!=6,error("class profile"));U0=B0.fu;U1=B1.fu;CC=matrix(#U0,#U1);WIT=List();
for(j=1,#U1,my(ex=bnfisunit(B0,U1[j]),z=Mod(1,NF.pol));if(#ex!=#U0+1,error("unit membership"));for(i=1,#U0,z*=U0[i]^ex[i];CC[i,j]=ex[i]);z*=B0.tu[2]^ex[#ex];if(z!=U1[j],error("literal unit reconstruction"));if(idealhnf(NF,U1[j])!=matid(8),error("nonunit principal ideal"));listput(WIT,[U1[j],ex]));if(abs(matdet(CC))!=1,error("unit lattice index"));
for(j=1,#B1.cyc,my(J=idealpow(NF,B1.gen[j],B1.cyc[j]),a=bnfisprincipal(B1,J,1));if(a[1]!=0*a[1]||idealhnf(NF,nfbasistoalg(NF,a[2]))!=J,error("class relation")));
write("unmodified_smoke_certificate.gp",[B0.cyc,CC,Vec(WIT)]);print("UNMODIFIED_RUNTIME_SAVED_BNF_CERTIFIED;CLASS=",B1.cyc,";UNIT_INDEX=",abs(matdet(CC)),";RELATIONS=",#B1.cyc);}
main();quit;
