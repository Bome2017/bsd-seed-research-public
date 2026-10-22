\\ (1) PARI normalisation vs the value printed in Stein-Wuthrich (4.2): E0 = 446d1, p = 5
\\     SW (4.2): Reg_p(E0/Q) = 2*5 + 2*5^2 + 5^4 + 4*5^5 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10)
E446 = ellinit([1,-1,0,-4,4]); G1=[2,0]; G2=[1,-1];
print("446d1: on curve ", [ellisoncurve(E446,G1), ellisoncurve(E446,G2)], " ; conductor ", ellglobalred(E446)[1], " ; a_5 = ", ellap(E446,5));
print("PARI ellpadicregulator(446d1, 5) = ", ellpadicregulator(E446,5,10,[G1,G2]));
SWprinted = 2*5 + 2*5^2 + 5^4 + 4*5^5 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10);
print("SW printed (4.2)                 = ", SWprinted);
print("difference = ", ellpadicregulator(E446,5,10,[G1,G2]) - SWprinted);
\\ (2) 3-saturation sanity check of <P1,P2> on the seed (input is certified upstream; this is only a cheap cross-check)
E0 = ellinit([0,-22735,0,106272484,0]); Em = ellminimalmodel(E0, &ch);
P1 = ellchangepoint([4547,327384], ch); P2 = ellchangepoint([5184,281520], ch);
S = ellsaturation(Em, [P1,P2], 3);
print("ellsaturation at primes <= 3 returns: ", S, " ; unchanged = ", S == [P1,P2]);
\\ (3) log_3 of topological generators of 1+3Z_3
print("ord_3 log_3(4) = ", valuation(log(4+O(3^20)),3), " ; ord_3 log_3(1+3u) for u=1,2,4,5,7,8: ", vector(6,i,valuation(log(1+3*[1,2,4,5,7,8][i]+O(3^20)),3)));
\\ (4) F: exponent e_{3,2} = min_{1<=i<=2} ord_3 binomial(27,i); and the neighbours
e(n,j) = vecmin(vector(j,i,valuation(binomial(3^n,i),3)));
print("e_{n-1,j} for n=4 (depth 4): j=1..6 -> ", vector(6,j,e(3,j)), " ; for n=5: ", vector(6,j,e(4,j)), " ; for n=3: ", vector(6,j,e(2,j)));
\\ (5) local data at 3 for D
print("#E~_ns(F_3) = p - a_p = ", 3 - ellap(Em,3), " ; eps_3 = 1 - 1/a_3 = ", 1 - 1/ellap(Em,3));
\\ (6) root number
print("global root number = ", ellrootno(Em), " ; local root numbers at bad primes: ", vector(5,i,ellrootno(Em,[2,3,2243,4547,5843][i])));
