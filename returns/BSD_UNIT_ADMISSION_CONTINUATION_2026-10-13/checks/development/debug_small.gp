D=read("../data/stage1_data.gp");G=D[1];AP=D[10];print(AP[1..5]);print(vector(15,j,denominator(lift(G[j]))));print(vector(15,j,denominator(content(lift(G[j])))));print(matsize(D[7]));quit;
