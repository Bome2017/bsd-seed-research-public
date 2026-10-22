alarm(30);
E=ellinit([1,1,0,-34,-135]);gettime();R=ellrank(E,0);print("ELLRANK ",R," TIME_MS ",gettime());print("TORSION ",elltors(E));print("COMPLETE");quit;
