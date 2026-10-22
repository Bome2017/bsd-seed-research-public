alarm(30);gettime();D=read("inputs/data.gp");N=read("norm_data.gp");S=N[1];NV=N[3];FB=N[4];K=N[7];KC=matsolve(S,K);rows=List();q=3;rk=0;
{while(rk<3,q=nextprime(q+1);if(q>10000,error("no rank certificate in bound"));if(q%3!=1||q==433,next);rs=polrootsmod(FB,q);om=znprimroot(q)^((q-1)/3);
for(j=1,#rs,if(subst(deriv(FB),z,rs[j])==0,next);ok=1;iferr(vals=vector(#NV,i,subst(lift(NV[i]),z,rs[j]));for(i=1,#NV,if(vals[i]==0,ok=0)),er,ok=0);if(!ok,next);
row=vector(#NV,i,my(t=vals[i]^((q-1)/3));if(t==1,0,if(t==om,1,if(t==om^2,2,error("noncubic character")))));listput(rows,row);R=Mod(matrix(#rows,#NV,i,j,rows[i][j]),3);rk=matrank(R);
if(R*KC!=0*(R*KC)||rk>3,error("positive/negative norm contradiction"));
write("norm_residue_rows.jsonl",Str("{\"q\":",q,",\"root\":",lift(rs[j]),",\"omega\":",lift(om),",\"values\":",lift(vals),",\"characters\":",row,"}"));
));}
if(#matker(R)!=3||matrank(KC)!=3,error("kernel dimension"));write("norm_map_certificate.gp",[S,K,KC,R]);
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
write("norm_map.json",Str("{\"source_dimension\":13,\"scalar_dimension\":6,\"scalar_basis\":",jm(S),",\"global_norm_kernel\":",jm(K),",\"kernel_in_scalar_coordinates\":",jm(KC),",\"residue_map\":",jm(R),",\"norm_image_rank\":",rk,"}"));
rc(v)=vector(8,i,my(c=polcoef(lift(v),i-1));[numerator(c),denominator(c)]);
write("norm_polynomials.json",Str("{\"line_field\":",vector(9,i,polcoef(FB,i-1)),",\"six_norms\":",vector(#NV,i,rc(NV[i])),"}"));
print("EXACT_NORM_KERNEL_DIM=3;IMAGE_RANK=",rk,";WITNESS_ROWS=",#rows,";LAST_Q=",q,";MS=",gettime());quit;
