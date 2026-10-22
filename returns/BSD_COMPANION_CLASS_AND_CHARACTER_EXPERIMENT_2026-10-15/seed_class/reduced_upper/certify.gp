alarm(180);gettime();
B=read("bnf.bin");if(type(B)!="t_VEC",error("BNF object"));v=bnfcertify(B,1);write("certification.gp",v);print("QUOTIENT_CERTIFICATION=",v,";CERTIFY_MS=",gettime());if(v!=1,error("quotient certification not one"));print("CLASS_UPPER_CERTIFICATION_COMPLETE");quit;
