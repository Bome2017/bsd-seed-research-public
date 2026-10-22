read("relative_setup.gp");
recordrow(tag,cv,ID,al,ct,JJ,steps) = {
  if(idealmul(NF,idealmul(NF,idealhnf(NF,al),ct),JJ)!=ID,error("full pseudo-relation identity"));
  if(ti(ct)!=ct,error("discarded base ideal not invariant"));
  RN++;write("batch_rows.gp",[RN,tag,cv,ID,al,ct,JJ,steps]);
  print("RELATIVE_ROW;ID=",RN,";TAG=",tag,";NORM_DIGITS=",#Str(idealnorm(NF,JJ)),";STEPS=",steps);
};
reduceinput(tag,cv,v) = {
  my(ID=matid(24),al=Mod(1,NF.pol),ct,JJ,R,nn,st=0);
  for(h=1,#ORB,if(cv[h],ID=idealmul(NF,ID,idealpow(NF,ORB[h][2],cv[h]))));
  ct=contentideal(ID);JJ=idealdiv(NF,ID,ct);
  for(k=1,4,
    R=shortstep(JJ,v);nn=idealnorm(NF,R[1]);
    if(nn>=idealnorm(NF,JJ),
      if(R[1]!=JJ,recordrow(concat(tag,[k,-1]),cv,ID,al*R[2],idealmul(NF,ct,R[3]),R[1],st));
      break
    );
    al*=R[2];ct=idealmul(NF,ct,R[3]);JJ=R[1];st++
  );
  recordrow(tag,cv,ID,al,ct,JJ,st);
};
{
alarm(285);gettime();relative_setup();RN=0;Ex=[5,25,96,97,125,192,256,512];
for(h=1,#ORB,for(e=1,#Ex,for(d=0,1,
  cv=vector(#ORB);cv[h]=Ex[e];vv=vector(14);if(d,vv[1+(h%14)]=12);
  reduceinput([h,Ex[e],d],cv,vv)
)));
for(h=1,min(4,#ORB),for(j=h+1,min(4,#ORB),
  cv=vector(#ORB);cv[h]=96;cv[j]=97;reduceinput([h,j,2],cv,vector(14))
));
print("RELATIVE_BATCH_COMPLETE;ROWS=",RN,";MS=",gettime());quit;
}
