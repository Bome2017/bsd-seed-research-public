read("cubinv.gp");read("classimg.gp");D=read("stage1_data.gp");F=read("stage3_data.gp");L=read("stage4_local_data.gp");
JM(M)=vector(matsize(M)[1],i,Vec(lift(M[i,])));
print("source_dimension=15");print("field=3");
print("valuation_rows=",JM(D[2]));print("unramified_basis_rows=",JM(D[3]));print("tau_matrix=",JM(D[4]));print("additivity_rows=",JM(D[5]));print("actual_coordinates=",JM(D[6]));print("residue_injectivity_matrix=",JM(D[7]));
print("class_rows_on_unramified_basis=",JM(F[3]));print("unit_basis_rows=",JM(F[4]));print("tau_unit_matrix=",JM(F[5]));print("norm_unit_basis_rows=",JM(F[6]));print("known_unit_basis_rows=",JM(F[7]));print("class_lifts_rows=",JM(F[8]));print("repair_unit_basis_rows=",JM(F[9]));print("repair_coordinates=",JM(F[10]));
print("local_rows=",JM(L[1]));print("local_block_rows=",vector(#L[2],i,[L[2][i][1],JM(L[2][i][5])]));print("local_image_basis_rows=",vector(#L[2],i,[L[2][i][1],JM(L[2][i][3][1])]));
print("local_source_evaluation_rows=",vector(#L[2],i,[L[2][i][1],JM(L[2][i][4])]));
quit;
