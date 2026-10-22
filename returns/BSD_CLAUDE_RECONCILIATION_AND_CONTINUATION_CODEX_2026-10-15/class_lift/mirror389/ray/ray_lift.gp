alarm(120);C=read("certificate.gp");nf=C[1];J=C[5];betpr=C[6];J3=idealhnf(nf,betpr);if(J3!=idealpow(nf,J,3),error("cube ideal mismatch"));RAY=read("ray.bin");
RC=bnrisprincipal(RAY,J,0);RB=bnrisprincipal(RAY,J3,0);
if(vector(#RAY.cyc,i,(3*RC[i]-RB[i])%RAY.cyc[i])!=vector(#RAY.cyc),error("ray ideal cube relation"));
RO=1;for(i=1,#RAY.cyc,RO=lcm(RO,RAY.cyc[i]/gcd(RAY.cyc[i],RC[i])));print("RAY_LIFT_COORDINATES=",RC,";RAY_LIFT_ORDER=",RO,";BETA_COORDINATES=",RB);
write("ray_coordinates.gp",[RAY.cyc,RC,RB,RO]);print("ACTUAL_RAY_GROUP_AND_LIFT_PASS");quit;
