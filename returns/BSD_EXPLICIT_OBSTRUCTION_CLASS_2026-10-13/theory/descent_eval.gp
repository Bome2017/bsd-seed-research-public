default(nbthreads,1);
d=43737; pol=y^2-y-10934; bn=bnfinit(pol,1); rr=Mod(2*y-1,pol); P=[[1778638/9,1169009812/27],[6466626346478/36517849,2366996613841078836/220677361507]];
ff(z)= (z[1]-11*d/3)*(z[2]+1/2)+rr*(-4*z[1]^2+161*d*z[1]/6-785*d^2/18);
{eps=Mod(224*y+23311,pol);for(i=1,2,zz=ff(P[i]);print("F",i,"=",zz);print("N",i,"=",norm(zz));print("IDEAL",i,"=",idealfactor(bn,zz));for(j=0,4,rat=zz/eps^j;print("POWER ",[i,j,nfroots(bn,x^5-rat)])));print("EPSNORM ",norm(eps));print("END");}
