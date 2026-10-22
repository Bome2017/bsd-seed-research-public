E=ellinit([0,-22735,0,106272484,0]); N=ellglobalred(E)[1]; print("N=",N);
for(i=1,4,D=[-119,-271,-79,-311][i]; print("D=",D," h=",qfbclassno(D)," kron(D,p) p=2,3,5,2243,4547,5843: ",vector(6,j,kronecker(D,[2,3,5,2243,4547,5843][j]))," w(E^K)=",ellrootno(ellinit(elltwist(E,D)))," sqrtN_K=",sqrt(N*D^2*1.0)));
