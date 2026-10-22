\\ Separate PARI rational-point calculation. No modular symbols or Sha calculation.
E=ellinit([0,-1,0,-66020924,-65074271436]);
P1=[-3031,327384]; P2=[-2394,281520];
Q1=ellmul(E,P1,16); Q2=ellmul(E,P2,16);
v=[P1,P2,Q1,Q2,elladd(E,Q1,Q1),elladd(E,Q1,Q2),elladd(E,Q2,Q2)];
for(i=1,#v,if(!ellisoncurve(E,v[i]),error("off curve")); print(v[i][1],"|",v[i][2]));
quit;
