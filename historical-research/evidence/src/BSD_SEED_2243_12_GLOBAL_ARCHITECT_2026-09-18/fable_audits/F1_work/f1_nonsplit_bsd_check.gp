\\ Sanity check of the NON-SPLIT bookkeeping (SW Conj 5.1 / Thm 6.1 with eps_3 = 2 and the plain sigma-height) on small curves with a_3 = -1.
\\ L-side: PARI modular symbols (ellpadicL). Height side: ellpadicregulator (independently validated on the seed in f1_indep_height.gp).
\\ p-adic BSD in the s-variable:  L_p^{(r)}(1)/r!  =  eps_p * prod c_v * #Sha * Reg_p / #tors^2   (Reg_p un-normalised).
\\ a-invariants / generators / sha_an from the local Cremona ecdata (curvedata.00000-09999).
chk(name, ai, G, shaan) = my(E=ellinit(ai), p=3, n=10, r=#G, gr=ellglobalred(E)); my(tam=gr[3], tor=elltors(E)[1], ap=ellap(E,p)); my(Lr=ellpadicL(E,p,n,,r)/r!); my(R=if(r==0, 1, ellpadicregulator(E,p,n,G))); my(rhs=(1-1/ap)*tam*R/tor^2); print(name, ": N=", gr[1], " a_3=", ap, " rank=", r, " prod c=", tam, " tors=", tor, " sha_an(Cremona)=", shaan); print("   ord_3 L^(r)(1)/r! = ", valuation(Lr,3), " ; ord_3 rhs(without Sha) = ", valuation(rhs,3)); print("   ratio L/rhs = ", Lr/rhs);
chk("57a1  (rank 1)", [0,-1,1,-2,2], [[2,1]], 1);
chk("681c1 (rank 2)", [0,-1,1,0,2], [[0,1],[3,4]], 1);
chk("681b1 (rank 0)", [1,1,0,-1154,-15345], [], 9);
chk("33a1  (rank 0)", [1,1,0,-11,0], [], 1);
