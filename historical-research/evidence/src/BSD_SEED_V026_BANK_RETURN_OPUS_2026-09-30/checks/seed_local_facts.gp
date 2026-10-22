\\ V026-BANK: re-derive the local facts used by B.20 on the retained minimal model (PARI/GP). One statement per line.
E = ellinit([0,-1,0,-66020924,-65074271436]);
print("model a-invariants: ", E[1..5]);
G = ellglobalred(E); print("conductor N = ", G[1], " = ", factor(G[1]));
print("Tamagawa product = ", G[3]);
print("root number = ", ellrootno(E));
print("v_2243(disc) = ", valuation(E.disc, 2243), "; Kodaira at 2243: ", elllocalred(E,2243)[2], " (PARI code 4 + n means I_n, so 5 = I_1)");
print("a_p at the bad multiplicative primes: a_3 = ", ellap(E,3), ", a_2243 = ", ellap(E,2243), ", a_5843 = ", ellap(E,5843));
print("a_19 = ", ellap(E,19), ", a_59 = ", ellap(E,59), ", a_487 = ", ellap(E,487));
print("19, 59, 487 ordinary (a_p != 0 mod p): ", [ellap(E,19)%19 != 0, ellap(E,59)%59 != 0, ellap(E,487)%487 != 0]);
print("2242 = ", factor(2242), "; 5844 = ", factor(5844));
print("supersingular good primes 5 <= p < 1000: ", select(p -> G[1] % p != 0 && ellap(E,p) % p == 0, primes([5,1000])));
