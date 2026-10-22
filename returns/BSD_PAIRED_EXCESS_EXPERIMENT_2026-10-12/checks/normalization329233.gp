default(nbthreads,1);
{E0=ellinit([0,-1,1,-7820,-263580]);d=329233;T=elltwist(E0,d);F=ellminimalmodel(T,&cv);print("TWIST_MINIMAL ",[F[1..5],cv]);print("AP ",ellap(F,5));print("PERIOD_NUMERICAL_CONTROL ",sqrt(d)*F.omega[1]/E0.omega[1]);print("DONE");}
quit;
