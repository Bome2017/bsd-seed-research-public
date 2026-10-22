alarm(30);
E=ellinit([1,-1,0,-1367381,615777525]);gettime();R=ellrank(E,0);print("ELLRANK ",R," TIME_MS ",gettime());print("TORSION ",elltors(E));print("POINT_ON_CURVE ",ellisoncurve(E,[653,675]));print("COMPLETE");quit;
