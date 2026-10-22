read("theory/descent_eval.gp");
{z=ff(P[1]);fac=idealfactor(bn,z);fac[,2]=fac[,2]/5;aa=idealfactorback(bn,fac);print("ROOTIDEAL ",aa);print("ROOTIDEALCLASS ",bnfisprincipal(bn,aa,0));print("CLASSGROUP ",bn.cyc);print("POINT_RELATION ",nfroots(bn,x^5-ff(P[2])/z^2));print("CERTIFY ",bnfcertify(bn));}
