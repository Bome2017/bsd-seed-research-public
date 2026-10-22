alarm(30);A=read("inputs/A_data.gp");B=read("inputs/B_data.gp");NA=read("inputs/A_norms.gp");NB=read("inputs/B_norms.gp");P=read("paired_certificate.gp");if(subst(NA[2],z,P[1])!=0||subst(NB[4],z,P[2])!=0,error("dual isomorphism"));
for(j=1,#P[3],if(subst(lift(NA[7][j]),z,P[1])!=P[3][j]||P[3][j]!=P[7][j]^3*prod(i=1,#B[6],B[6][i]^lift(P[5][i,j])),error("literal AB coordinate")));
for(j=1,#P[4],if(subst(lift(NB[3][j]),z,P[2])!=P[4][j]||P[4][j]!=P[8][j]^3*prod(i=1,#A[6],A[6][i]^lift(P[6][i,j])),error("literal BA coordinate")));
if(NB[1]*P[9]!=P[5]||NA[5]*P[10]!=P[6],error("scalar coordinates"));if(P[9]*P[10]!=0*(P[9]*P[10])||P[10]*P[9]!=0*(P[10]*P[9]),error("complex"));
if(matrank(matconcat([P[13],A[10]]))!=2||matrank(A[10])!=2,error("A norm image versus points"));
print("NINE_LITERAL_SOURCE_MAP_IDENTITIES_PASS;EXACT_FIELD_MAPS_PASS;NORM_COMPLEX_PASS;A_IMAGE_EQUALS_POINT_PLANE");quit;
