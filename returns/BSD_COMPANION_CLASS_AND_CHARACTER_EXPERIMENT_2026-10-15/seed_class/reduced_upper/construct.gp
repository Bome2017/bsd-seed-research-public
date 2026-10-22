alarm(120);gettime();
R=read("reduction.gp");B=bnfinit(R[5],0);writebin("bnf.bin",B);write("provisional_class.gp",[B.no,B.cyc,B.gen]);
print("PROVISIONAL_CLASS_NUMBER=",B.no,";CLASS_INVARIANTS=",B.cyc,";BNF_MS=",gettime());print("BNF_UPPER_CONSTRUCTION_COMPLETE_PROVISIONAL");quit;
