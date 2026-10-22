default(nbthreads,1);
install("mspadicmoments_chunk","GGLLL","mschunk","/Users/bsm/BSD_PAIRED_EXCESS_EXPERIMENT_2026-10-12/build/modsym_chunk.dylib");
chunked(mp,phi,d,batch)={my(oms=mstooms(mp,phi),s=0,t);forstep(lo=1,abs(d)-1,batch,t=mschunk(mp,oms,d,lo,min(lo+batch,abs(d)));if(s==0,s=t,s[1]=lift(Mod(s[1]+t[1],5^t[3][2]))));s};
{E=ellinit([0,-1,1,-7820,-263580]);[ms,phi]=msfromell(E,1);mp=mspadicinit(ms,5,5,0);for(i=1,3,dd=[13,29,-7][i];a=mspadicmoments(mp,phi,dd);b=chunked(mp,phi,dd,3);if(a!=b,error("small exact moments mismatch"));print("CONTROL ",[dd,a==b]));b=chunked(mp,phi,43737,2000);a=read("/Users/bsm/BSD_ODD_EXCESS_CONTROL_EXPERIMENT_2026-10-12/outputs/candidate43737_mu.bin");if(a!=b,error("43737 saved moments mismatch"));print("CONTROL ",[43737,a==b,mspadicseries(b)]);print("DONE");}
quit;
