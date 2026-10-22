C=read("ideal_map_certificate.gp");
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
F=C[7];out=vector(matsize(F)[1],i,[F[i,1].p,F[i,1].e,F[i,1].f,F[i,2],F[i,2]/3]);
print("{\"source_class_invariants\":",C[17],",\"target_class_invariants\":",C[18],",\"source_ideal_norm\":",abs(matdet(C[5])),",\"image_ideal_norm\":",abs(matdet(C[8])),",\"norm_beta_prime_data_p_e_f_val_div3\":",out,",\"unit_map_matrix\":",jm(C[13]),",\"unit_map_rank_mod3\":",matrank(Mod(C[13],3)),",\"connecting_unit_coordinates\":",C[14]~,",\"repair_exponents_mod3\":",lift(C[15])~,",\"class_kernel_dimension\":1,\"connecting_rank\":0}");quit;
