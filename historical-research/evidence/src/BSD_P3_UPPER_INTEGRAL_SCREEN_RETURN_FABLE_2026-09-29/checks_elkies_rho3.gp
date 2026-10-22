E=ellinit([0,-1,0,-66020924,-65074271436]); j=E.j;
g=3^7*(x^2-1)^3*(x^6+3*x^5+6*x^4+x^3-3*x^2+12*x+16)^3*(2*x^3+3*x^2-3*x-5); den=(x^3-3*x-1)^9;
A=x^6+6*x^5+4*x^3+12*x^2-18*x-23; B=7*x^6+24*x^5+18*x^4-26*x^3-33*x^2+18*x+28;
print("+sign: f = 1728 + 27A^2B^2(2x^3-3x^2+4)/den ? ", g/den == 1728 + 3^3*A^2*B^2*(2*x^3-3*x^2+4)/den);
print("+sign: f(oo)=",pollead(g)/pollead(den)," f(0)=",subst(g,x,0)/subst(den,x,0));
for(s=-1,1, if(s==0,next); print("sign ",s,": controls 4374,419904,-44789760 -> ",vector(3,i,#nfroots(,s*g-[4374,419904,-44789760][i]*den)), " rational roots;  seed: ", nfroots(,s*g-j*den), " ; x=oo: ", s*pollead(g)/pollead(den)==j));
\\ cube test (Elkies' mod-3 remark): j is a cube?
print("j cube? ", ispower(j,3));
