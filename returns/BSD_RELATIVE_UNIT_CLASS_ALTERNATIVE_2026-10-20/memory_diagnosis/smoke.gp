install("bsd_lowmem_init","G","bsd_lowmem_init","./libbsd_lowmem.dylib");
{
alarm(40);
F=w^8-60*w^4-144*w^2-300;NF=nfinit(F);
B0=bnfinit(NF,1);B1=bsd_lowmem_init(NF);
if(B0.cyc!=B1.cyc || B0.disc!=B1.disc,error("class/basis mismatch"));
if(bnfcertify(B0)!=1||bnfcertify(B1)!=1,error("unmodified certification"));
U0=B0.fu;U1=B1.fu;
if(#U0!=#U1,error("unit rank mismatch"));
for(i=1,#U1,if(abs(nfeltnorm(NF,U1[i]))!=1,error("unit norm")));
C=matrix(#U0,#U1,i,j,bnfisunit(B0,U1[j])[i]);
if(abs(matdet(C))!=1,error("unit bases differ by index"));
print("RUNTIME=",version());
print("CLASS_GROUP=",B0.cyc,";CERTIFICATES=[1,1];UNIT_CHANGE_DET=",matdet(C),";UNIT_RANK=",#U0);
writebin("smoke_bnf.bin",B1);
print("LOW_MEMORY_SMOKE_PASS");quit;
}
