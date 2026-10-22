\\ Steps 1-3: minimal model, Neron differential, sign of Delta, real components, torsion, Tamagawa numbers (PARI 2.17.3)
default(realprecision, 60);
m=2243; n=12; A=m+16*n^2; B=m+25*n^2;
print("A=",A," B=",B);
E=ellinit([0,-5*A,0,4*A*B,0]);
print("a-invariants: ",E[1..5]);
print("disc = ",E.disc," = ",factor(E.disc));
print("sign(disc) = ",sign(E.disc));
print("c4 = ",E.c4," factor ",factor(E.c4));
print("c6 = ",E.c6);
print("j = ",E.j);
M=ellminimalmodel(E,&v);
print("ellminimalmodel change [u,r,s,t] = ",v);
print("minimal model a-invariants: ",M[1..5]);
print("minimal disc = ",M.disc,"  equal to disc of E? ",M.disc==E.disc);
G=ellglobalred(E);
print("ellglobalred = [N, [u,r,s,t], prod c_p, faN, L] : ",G);
print("conductor N = ",G[1]," = ",factor(G[1]));
\\ real components: Delta>0 => 2 components
print("real roots of 4x^3+b2x^2+2b4x+b6: ",polroots(4*x^3+E.b2*x^2+2*E.b4*x+E.b6));
print("number of real components = ",if(E.disc>0,2,1));
print("E.roots = ",E.roots);
\\ 2-torsion: roots of x^2-5Ax+4AB
print("disc of x^2-5Ax+4AB = ",25*A^2-16*A*B," = ",factor(25*A^2-16*A*B)," issquare? ",issquare(25*A^2-16*A*B));
print("elltors(E) = ",elltors(E));
print("elltors(M) = ",elltors(M));
print("--- local data (elllocalred: [f, kodaira, [u,r,s,t], c]) ---");
{
forprime(p=2,10000, if(E.disc%p==0,
  L=elllocalred(E,p);
  ap=ellap(E,p);
  print("p=",p,"  v_p(Delta)=",valuation(E.disc,p),"  f_p=",L[1],"  kodaira=",L[2],"  c_p=",L[3+1],"  change=",L[3],"  a_p=",ap,
    if(L[1]==1, if(ap==1,"  SPLIT multiplicative", if(ap==-1,"  NON-SPLIT multiplicative","  ??")), "  additive"))));
}
print("product c_p = ",G[3]);
print("ellrootno(E) = ",ellrootno(E));
{ \\ kodaira codes: PARI: I_n -> n+4 (n>0), I0 -> 1, II ->2, III->3, IV->4, I_n* -> -(n+4)? ; print dictionary check
print("PARI kodaira code convention check: see ?elllocalred");
}
\\ Neron differential: minimal model => omega = dx/(2y+a1x+a3) = dx/(2y), u=1
print("u for minimal model = ",v[1]);
