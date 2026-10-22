{C=read("divisors.gpout");OUT=vector(#C,i,[C[i][1],C[i][2],C[i][3],#C[i][5],#C[i][6]]);write("divisor_profile.json",OUT);print("DIVISOR_PROFILE_EXPORTED");quit;}
