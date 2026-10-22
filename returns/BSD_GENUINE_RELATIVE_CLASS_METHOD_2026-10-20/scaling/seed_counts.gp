forprime(q=5,2000,if(q==2243 || q==4547 || q==5843,next); E=ellinit([0,-22735,0,106272484,0],q); print([q,q+1-ellcard(E),ellgroup(E)]));
quit;
