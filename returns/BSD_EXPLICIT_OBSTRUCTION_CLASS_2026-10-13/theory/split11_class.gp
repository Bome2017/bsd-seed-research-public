read("theory/descent_eval.gp");
{prs=idealprimedec(bn,11);for(i=1,2,pr=prs[i];four=idealpow(bn,pr,4); pp=bnfisprincipal(bn,four,1); ga=nfbasistoalg(bn,pp[2]);bar=subst(lift(ga),y,1-y);aa=ga/Mod(bar,pol);print("PRIME ",[i,pr,bnfisprincipal(bn,pr,0)]);print("GENERATOR ",[ga,norm(ga),pp[1]]);print("ALPHA11 ",aa);print("IDEAL11 ",idealfactor(bn,aa)));print("END11");}
