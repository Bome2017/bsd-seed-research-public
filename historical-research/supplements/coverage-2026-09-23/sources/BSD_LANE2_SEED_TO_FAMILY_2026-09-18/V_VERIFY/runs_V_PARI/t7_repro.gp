\\ Minimal reproduction: ellpadicheight / ellpadicregulator depend on the Weierstrass model
\\ (canonical p-adic height must be invariant under isomorphism).
E = ellinit([0,0,1,-1,0]); P = [0,0]; p = 5; n = 10;     \\ 37a1, a_5 = -2 (good ordinary), rank 1
H(e,Q) = ellpadicheight(e,p,n,Q) * [1, -ellpadics2(e,p,n)]~;   \\ canonical height, as in ??ellpadicheight
F = ellinit(ellchangecurve(E, [1,1,0,0])); PF = ellchangepoint(P, [1,1,0,0]);    \\ u = 1, r = 1
G = ellinit(ellchangecurve(E, [1/2,0,0,0])); PG = ellchangepoint(P, [1/2,0,0,0]); \\ u = 2 (integral model)
H(E,P)
H(F,PF) - H(E,P)            \\ expected O(5^10); observed nonzero
H(G,PG) - H(E,P)            \\ expected O(5^10); observed nonzero
[ellpadicregulator(E,p,n,[P]), ellpadicregulator(F,p,n,[PF]), ellpadicregulator(G,p,n,[PG])]
\\ the r-term: with u = 1 the discrepancy is exactly -2*r*log(P)^2, r = ellglobalred(F)[2][2]
r = ellglobalred(F)[2][2]; g = ellpadicheight(E,p,n,P)[2];   \\ g = -log(P)^2
H(F,PF) - H(E,P) - 2*r*g      \\ O(5^10)
\\ the u-term: doc says g = -(log_E P)^2 on the GIVEN model; check on G with Q = k*P in E^1 (k = #E(F_5) = 8)
QG = ellmul(G, PG, 8); lG = ellpadiclog(G, p, n, QG);
ellpadicheight(G,p,n,QG)[2] + lG^2    \\ expected O(5^n); observed nonzero (PARI multiplies by u instead of dividing by u^2)
