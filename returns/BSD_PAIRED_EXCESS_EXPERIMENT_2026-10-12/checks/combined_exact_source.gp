default(nbthreads,1);
{A=ellinit([0,-1,1,-1120075138986,-826418095533154920]);F=ellinit([0,-1,1,-847680091476076,-9499397825675855099600]);iso=ellisomat(A,5);for(j=1,#iso[1],Fs=ellinit(iso[1][j][1]);Fm=ellminimalmodel(Fs,&cv);if(Fm[1..5]==F[1..5],print("MAP ",iso[1][j][2]);print("CHANGE ",cv)));print("LOCAL ",[ellglobalred(A),ellglobalred(F)]);print("DISC ",[A.disc,F.disc]);print("FACTOR ",factor(329233));print("DONE");}
quit;
