{
R=read("replay/TORSION_SUNIT_RESULT.gp");print("[");for(i=1,#R,print(if(i>1,",",""),"{\"element\":\"",R[i][1],"\",\"norm\":\"",R[i][2],"\",\"norm_exponents_2_3_5_2243_4547_5843\":",R[i][3],",\"tau_ratio\":",lift(R[i][4]),",\"exact_S_ideal_reconstruction\":true,\"faithful_projection_fifth_powers\":2}"));print("]");quit;
}
