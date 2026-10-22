default(parisizemax,256000000);
E=ellinit([1,1,1,3,12]); E1=ellinit([1,1,1,-1669982047,-25795561267816]); E2=ellinit([1,1,1,1878418,-485198548]);
print("VERSION ",version());
for(i=1,3,e=[E,E1,E2][i];print("CURVE ",[i,ellglobalred(e)[1],factor(e.disc),e.c4,e.c6,ellap(e,5)]));
print("RAISING ",[ellap(E,113),ellap(E,167),ellap(E1,113),ellap(E2,167)]);
forprime(q=2,50,if(2541%q&&q!=5,print("FROB ",[q,ellap(E,q),kronecker(ellap(E,q)^2-4*q,5)])));
forstep(D=-1,-500,-1,if(isfundamental(D)&&gcd(D,2541*113*167*5)==1&&kronecker(D,11)==1&&kronecker(D,3)*kronecker(D,7)==-1&&kronecker(D,113)==-1&&kronecker(D,167)==-1,print("CM ",[D,kronecker(D,3),kronecker(D,7),kronecker(D,5),qfbclassno(D)])));
for(i=1,2,l=[113,167][i];N=2541*l;idx=N*prod(j=1,matsize(factor(N))[1],1+1/factor(N)[j,1]);B=floor(idx/6);a=ellan(E,B);b=ellan([E1,E2][i],B);bad=List();for(n=1,B,c=a[n]-if(n%l==0,l*a[n/l],0)-b[n];if(c%5,listput(bad,[n,c%5])));print("STURM ",[l,N,idx,B,#bad,if(#bad,Vec(bad)[1],[])]) );
quit
