alarm(90);gettime();
B=read("/Users/bsm/BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/work/kb2a_bnf.bin");print("INPUT_CLASS=",B.cyc,";FIELD=",B.nf.pol);
c=bnfcertify(B,1);print("CLASS_QUOTIENT_CERTIFICATE=",c);if(c!=1,error("quotient certification did not return1"));print("SOURCE_QUOTIENT_CERT_COMPLETE;MS=",gettime());quit;
