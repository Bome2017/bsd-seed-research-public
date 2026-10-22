{
A=read("split_prime_data.gp");DR=A[1];rows=A[3];pairs=A[4];
rr=[460,20,10];OUT=List();
for(i=1,3,e=rr[i];c=0;while((c+1)^e<DR,c++);PP=Vec(select(a->a[5]<=c,pairs));PR=Set(vector(#PP,j,PP[j][1]));listput(OUT,[e,c,#PP,#PR,vector(#PP,j,PP[j][1..5])]));
print([DR,Vec(OUT)]);quit;
}
