read("relative_setup.gp");
{
alarm(115);gettime();relative_setup();SS=read("support_matrices.gp");B=SS[1];CI=SS[4];PI=SS[7];PMAP=Map();ans=List();outside=0;inside=0;
for(h=1,#PI,
 j=0;for(k=1,#B,if(CI[k]==PI[h],j=k;break));if(j==0,error("missing private orbit"));
 nn=idealnorm(NF,B[j]);FF=factor(nn,419776);bad=0;cnt=0;large=1;
 for(i=1,matsize(FF)[1],q=FF[i,1];if(q>419775,large*=q^FF[i,2];bad=1;next);
   if(!mapisdefined(PMAP,q,&PP),PP=idealprimedec(NF,q);mapput(PMAP,q,PP));
   for(k=1,#PP,v=idealval(NF,B[j],PP[k]);if(v,cnt++;if(q^PP[k][4]>419775,bad=1)))
 );
 if(bad,outside++,inside++);listput(ans,[PI[h],j,nn,FF,large,bad,cnt]);
 if(h%25==0,print("PRIVATE_SUPPORT_PROGRESS;DONE=",h,";OUTSIDE=",outside))
);
write("private_support_result.gp",[Vec(ans),inside,outside]);
print("PRIVATE_SUPPORT_COMPLETE;PRIVATE_ORBITS=",#PI,";SUPPORTED_WITHIN_BOUND=",inside,";WITH_SUPPORT_OUTSIDE_BOUND=",outside,";MS=",gettime());quit;
}
