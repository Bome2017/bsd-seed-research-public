d=43737;
p=x^4+5*d*x^2+5*d^2;
print("original=",p);
r=polredabs(p);print("reduced=",r);
b=bnfinit(r,1);print("disc=",b.disc);print("cyc=",b.cyc);print("units=",b.fu);print("cert=",bnfcertify(b));print("autos=",nfgaloisconj(b));
quit;
