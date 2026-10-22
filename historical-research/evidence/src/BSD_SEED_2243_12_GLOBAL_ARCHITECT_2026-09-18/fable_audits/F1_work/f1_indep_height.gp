\\ f1_indep_height.gp -- F1 hostile audit, block E.
\\ Independent 3-adic canonical height on the seed via the Mazur-Tate integrality characterisation of sigma_3.
\\ Does NOT use ellpadics2 / ellpadicheight / Tate parameters for the independent value; those are only called at the end for comparison.
{
E0 = ellinit([0,-22735,0,106272484,0]);
Em = ellminimalmodel(E0, &ch);
print("change of variables [u,r,s,t] = ", ch, "   (u = 1 required)");
print("minimal model a-invariants = ", [Em.a1,Em.a2,Em.a3,Em.a4,Em.a6]);
print("disc factorisation (minimal) = ", factor(Em.disc));
gr = ellglobalred(Em);
print("conductor = ", gr[1], " = ", factor(gr[1]), " ; Tamagawa product = ", gr[3]);
bad = factor(gr[1])[,1]~;
for(i=1,#bad, my(l=bad[i], lr=elllocalred(Em,l)); print("  l = ", l, " : f = ", lr[1], ", Kodaira code = ", lr[2], ", c_l = ", lr[4], ", v_l(disc) = ", valuation(Em.disc,l), ", a_l = ", ellap(Em,l)));
print("torsion = ", elltors(Em));
print("ellisomat degrees = ", ellisomat(Em)[2]);
P1 = ellchangepoint([4547,327384], ch); P2 = ellchangepoint([5184,281520], ch);
print("P1, P2 on minimal model: ", P1, " ", P2, " ; on curve: ", ellisoncurve(Em,P1), ellisoncurve(Em,P2));
}

\\ --- formal series, exact over Q ---
{
NN = 36;
X  = ellformalpoint(Em, NN+4, 't)[1];        \\ x(t) = t^-2 - a1/t - a2 - ...
Z  = ellformallog(Em, NN+4, 't);             \\ z(t)
Tz = ellformalexp(Em, NN+4, 'z);             \\ t(z)
xz = subst(X, 't, Tz);                       \\ x(z)
g  = xz - 'z^(-2);                           \\ holomorphic, even
print("x(z) - z^-2 = ", truncate(g + O('z^5)), " + O(z^5)   [constant term should be -b2/12 = ", -Em.b2/12, "]");
G  = intformal(intformal(g, 'z), 'z);
sBz = 'z * exp(-G);                          \\ Bernardi sigma: (log sigma)'' = -x, sigma = z + ...
sBt = subst(sBz, 'z, Z);                     \\ as series in t
print("sigma_B(t) = ", truncate(sBt + O('t^8)), " + O(t^8)");
print("z(t)       = ", truncate(Z + O('t^10)), " + O(t^10)");
}

\\ --- integrality scan: sigma_c = sigma_B * exp(-(c/2) z^2), c = j/3, j mod 243 (c in (1/3)Z_3 mod 81) ---
DEG = 31;
Z2 = Z^2;
minval(S) = my(m=10^6); for(n=1, DEG, my(a=polcoeff(S,n)); if(a!=0, m=min(m, valuation(a,3)))); m;
firstbad(S) = my(f=0); for(n=1, DEG, my(a=polcoeff(S,n)); if(a!=0 && valuation(a,3)<0, f=n; break)); f;
sig(c) = sBt * exp(-(c/2)*Z2 + O('t^(NN+4)));
good = List(); for(j=0, 242, if(minval(sig(j/3)) >= 0, listput(good, j/3)));
print("c in (1/3)Z mod 81 giving a 3-integral sigma_c through degree ", DEG, " : ", Vec(good));
c0 = good[1];
for(k=-1,4, print("  perturb c by 3^",k," -> first non-integral degree (0 = none up to ",DEG,") = ", firstbad(sig(c0+3^k))));

\\ --- heights of Q = 8P (good reduction everywhere, in E_1(Q_3)) ---
PREC = 40;
sing1(Q,l) = my(x=Q[1],y=Q[2]); if(valuation(denominator(x),l)>0, 0, my(fx=3*x^2+2*Em.a2*x+Em.a4-Em.a1*y, fy=2*y+Em.a1*x+Em.a3); (valuation(fx,l)>0 && valuation(fy,l)>0));
goodred(Q) = my(ok=1); for(i=1,#bad, if(sing1(Q,bad[i]), ok=0)); ok;
hind(P, c) = my(Q=ellmul(Em,P,8)); if(!goodred(Q), error("bad reduction")); my(d=denominator(Q[1]), e=sqrtint(denominator(Q[1]))); if(e^2!=d, error("denominator not a square")); my(tq=-Q[1]/Q[2]); if(valuation(tq,3)<1, error("not in E_1(Q_3)")); my(S=truncate(sig(c)+O('t^(DEG+1)))); my(sv=subst(S,'t,tq+O(3^PREC))); 2*log(e/sv)/64;
P12 = elladd(Em,P1,P2);
print("good reduction of P1,P2,P12 themselves at bad primes (1 = nonsingular everywhere): ", [goodred(P1),goodred(P2),goodred(P12)]);
print("v_3(t(8P)) for P1,P2,P12 = ", [valuation(-ellmul(Em,P1,8)[1]/ellmul(Em,P1,8)[2],3), valuation(-ellmul(Em,P2,8)[1]/ellmul(Em,P2,8)[2],3), valuation(-ellmul(Em,P12,8)[1]/ellmul(Em,P12,8)[2],3)]);
cc = c0;
h11 = hind(P1,cc); h22 = hind(P2,cc); h12 = (hind(P12,cc)-h11-h22)/2;
print("INDEPENDENT (SW (4.1) normalisation 2*log_3(e/sigma_3), c = ", cc, "):");
print("  h11 = ", h11); print("  h22 = ", h22); print("  h12 = ", h12);
detI = h11*h22-h12^2;
print("  det = ", detI, "   ord_3 = ", valuation(detI,3));
print("  ord_3 [h11,h12,h22] = ", [valuation(h11,3),valuation(h12,3),valuation(h22,3)]);

\\ --- PARI's values for comparison ---
n = 16;
s2 = ellpadics2(Em,3,n);
print("PARI s2 = ", s2);
hp(P) = ellpadicheight(Em,3,n,P)*[1,-s2]~;
H11 = hp(P1); H22 = hp(P2); H12 = (hp(P12)-H11-H22)/2;
print("PARI ellpadicheight*[1,-s2]~ : H11 = ", H11); print("                               H22 = ", H22); print("                               H12 = ", H12);
R = ellpadicregulator(Em,3,n,[P1,P2]);
print("PARI ellpadicregulator = ", R, "  ord_3 = ", valuation(R,3));
print("ratios independent/PARI: h11/H11 = ", h11/H11, " ; h22/H22 = ", h22/H22, " ; h12/H12 = ", h12/H12);
print("det_indep / R_PARI = ", detI/R);
\\ robustness of my own determinant under the residual uncertainty of c (c known mod 3^k): shift c by 27 and by 81
for(k=2,4, my(a=hind(P1,cc+3^k), b=hind(P2,cc+3^k), m=(hind(P12,cc+3^k)-a-b)/2); print("  c+3^",k,": ord_3 det = ", valuation(a*b-m^2,3), " ; ord_3(det - det0) = ", valuation(a*b-m^2-detI,3)));
