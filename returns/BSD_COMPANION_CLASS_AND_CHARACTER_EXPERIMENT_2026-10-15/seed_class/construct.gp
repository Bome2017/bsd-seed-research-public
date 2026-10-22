alarm(120);gettime();
D=read("inputs/divisor_certificate.gp");fB=D[2];D=0;NF=nfinit(fB);if(poldegree(fB)!=8||!polisirreducible(fB),error("companion field degree"));
print("FIELD=",fB,";SIGNATURE=",NF.sign,";DISCRIMINANT=",NF.disc,";NF_MS=",gettime());write("field.gp",[fB,NF]);
B=bnfinit(NF,1);writebin("bnf.bin",B);write("provisional_class.gp",[B.no,B.cyc,B.gen]);print("PROVISIONAL_CLASS_NUMBER=",B.no,";CLASS_INVARIANTS=",B.cyc,";BNF_MS=",gettime());print("BNF_CONSTRUCTION_COMPLETE_PROVISIONAL");quit;
