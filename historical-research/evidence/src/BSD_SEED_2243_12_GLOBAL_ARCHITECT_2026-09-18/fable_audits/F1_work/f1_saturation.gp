\\ Is the basis returned by ellsaturation(.,.,3) a unimodular (+ torsion) change of <P1,P2>, or a strictly larger lattice?
E0 = ellinit([0,-22735,0,106272484,0]); Em = ellminimalmodel(E0, &ch);
P1 = ellchangepoint([4547,327384], ch); P2 = ellchangepoint([5184,281520], ch); T = [-7578,0];
S = ellsaturation(Em, [P1,P2], 3);
R0 = matdet(ellheightmatrix(Em,[P1,P2])); R1 = matdet(ellheightmatrix(Em,S));
print("real regulator of <P1,P2>      = ", R0);
print("real regulator of returned basis = ", R1);
print("index^2 = R0/R1 = ", R0/R1);
\\ express each returned point as a*P1 + b*P2 + e*T with small a,b
findcomb(Q) = my(res=[]); for(a=-4,4, for(b=-4,4, for(e=0,1, my(W=elladd(Em, elladd(Em, ellmul(Em,P1,a), ellmul(Em,P2,b)), if(e,T,[0]))); if(W==Q, res=concat(res,[[a,b,e]]))))); res;
print("S[1] = a*P1+b*P2+e*T with [a,b,e] in ", findcomb(S[1]));
print("S[2] = a*P1+b*P2+e*T with [a,b,e] in ", findcomb(S[2]));
\\ saturation to a larger bound for good measure (cheap): primes <= 100
S100 = ellsaturation(Em, [P1,P2], 100);
print("index^2 after saturating at all primes <= 100: ", R0/matdet(ellheightmatrix(Em,S100)));
