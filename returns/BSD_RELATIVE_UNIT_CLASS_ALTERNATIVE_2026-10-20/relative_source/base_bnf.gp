{main()=alarm(55);C=read("fields.gp");RF=polredbest(C[4],1);NF=nfinit(RF[1]);BB=bnfinit(RF[1],1);writebin("base6_bnf.bin",BB);write("base6_class.gp",[RF,BB.cyc,BB.no]);print("BASE6_BNF_CLASS=",BB.cyc,";CLASS_NUMBER=",BB.no);Z=bnfcertify(BB);write("base6_certificate.gp",Z);if(Z!=1,error("base6 certification failed"));print("BASE6_CERTIFIED");}
main();quit;
