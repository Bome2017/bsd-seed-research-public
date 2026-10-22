default(parisize,256000000);
a=read("../inputs/seed_nf.gp");k=read("../inputs/nf12.gp");
print("DA=",a.disc);print("DK=",k.disc);print("SIGNATURES=",[a.sign,k.sign]);print("RELATIVE_DISC_NORM=",a.disc/k.disc^2);
print("DA_FACTORS=",factor(a.disc));print("DK_FACTORS=",factor(k.disc));
quit;
