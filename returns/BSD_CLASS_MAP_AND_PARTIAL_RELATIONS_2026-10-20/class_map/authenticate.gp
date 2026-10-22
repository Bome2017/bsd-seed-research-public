coeffcol(v)=vector(8,i,polcoef(lift(v),i-1,w))~;
u(a)=norm(subst(lift(a),variable(nf.pol),WW));
{main()=
alarm(60);setrand(20261020);gettime();D=read("data.gp");B=read("bnf.bin");E=D[1];fA=D[3];T=D[5];nf=B.nf;
SA=-E.c4/48;SB=-E.c6/864;XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;
BT=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w));ww=matsolve(BT,coeffcol(Mod(w,fA)));
fB=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2;if(!polisirreducible(fB),error("dualfield"));BB=bnfinit(fB,1);NB=BB.nf;m=Mod(z,fB)/6;
GG=x^3-m^2*x^2+(m^4+2*SA)*x-(m^6+2*SA*m^2-4*SB);YY=Mod(m*x-(m^4+SA)/(2*m),GG);WW=sum(i=1,8,ww[i]*YY^(i-1));
if(subst(fA,w,WW)!=0||subst(lift(XT),w,WW)!=Mod(x,GG)||subst(lift(YT),w,WW)!=YY,error("incidenceembedding"));
if(subst(nf.pol,variable(nf.pol),w)!=fA,error("binary source polynomial mismatch"));
ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);if(#ix!=1,error("sourceclassrank changed"));II=idealpow(nf,B.gen[ix[1]],B.cyc[ix[1]]/3);pp=bnfisprincipal(B,idealpow(nf,II,3),1);if(pp[1]!=0*pp[1],error("sourceprincipal"));beta=nfbasistoalg(nf,pp[2]);if(idealpow(nf,II,3)!=idealhnf(nf,beta),error("sourceidealidentity"));
nu=u(beta);FAC=idealfactor(NB,nu);J=matid(8);
for(i=1,matsize(FAC)[1],if(FAC[i,2]%3,error("primitive norm divisor not3multiple"));J=idealmul(NB,J,idealpow(NB,FAC[i,1],FAC[i,2]/3)));
if(idealpow(NB,J,3)!=idealhnf(NB,nu),error("targetidealidentity"));
pr=bnfisprincipal(BB,J,1);if(pr[1]!=0*pr[1],error("predeterminedzero map changed"));rho=nfbasistoalg(NB,pr[2]);if(idealhnf(NB,rho)!=J,error("falseprincipalgenerator"));vunit=nu/rho^3;if(idealhnf(NB,vunit)!=matid(8),error("connectingrepresentative notunit"));
fu=B.fu;uf=vector(#fu,j,u(fu[j]));UV=matrix(#BB.fu,#fu);
for(j=1,#fu,my(vu=bnfisunit(BB,uf[j]));if(#vu!=#BB.fu+1,error("normunit"));UV[,j]=vector(#BB.fu,k,vu[k])~);
cc=bnfisunit(BB,vunit);if(#cc!=#BB.fu+1,error("connectingunitcoords"));cc=vector(#BB.fu,k,cc[k])~;sol=matinverseimage(Mod(UV,3),Mod(cc,3));if(Mod(UV,3)*sol!=Mod(cc,3),error("connectingnotzero"));
repair=prod(j=1,#fu,uf[j]^lift(sol[j]));rts=nfroots(NB,x^3-vunit/repair);if(#rts!=1||rts[1]^3!=vunit/repair,error("connectingliteralcube"));
write("ideal_map_certificate.gp",[fA,fB,GG,WW,II,beta,FAC,J,rho,vunit,fu,uf,UV,cc,sol,rts[1],B.cyc,BB.cyc]);
print("SOURCE_CLASS=",B.cyc,";TARGET_CLASS_PROVISIONAL=",BB.cyc,";CLASS_IMAGE=0;CONNECTING=0;IDEAL_IDENTITY=1;LITERAL_CONNECTING_CUBE=1;MS=",gettime());
print("TARGETCERT_START");q=bnfcertify(BB);print("TARGETCERT=",q,";MS=",gettime());if(q!=1,error("targetcert"));writebin("certified_target_bnf.bin",BB);print("AUTHENTICATION_COMPLETE");
}
main();
quit;
