alarm(10);D=read("/Users/bsm/BSD_THREE_WAY_ARITHMETIC_DISCOVERY_2026-10-15/frobenius/inputs/mirror_data.gp");
rc(v)=vector(8,i,my(c=polcoef(lift(v),i-1));[numerator(c),denominator(c)]);
print(Str("{\"source_generators\":",vector(#D[6],i,rc(D[6][i])),",\"torsion_point\":",vector(2,i,rc(D[5][i])),"}"));quit;
