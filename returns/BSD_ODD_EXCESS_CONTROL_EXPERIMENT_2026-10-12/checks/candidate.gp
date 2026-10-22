default(nbthreads,1);
{E=ellinit([1,-1,0,94,9]);
 print("MODEL ",E[1..5]);print("GLOBAL ",ellglobalred(E));
 print("TORSION ",elltors(E));
 forprime(p=3,19,print("LOCAL ",[p,ellap(E,p),p+1-ellap(E,p)]));
 print("RANK ",ellrank(E,1));
 print("DONE");}
quit;
