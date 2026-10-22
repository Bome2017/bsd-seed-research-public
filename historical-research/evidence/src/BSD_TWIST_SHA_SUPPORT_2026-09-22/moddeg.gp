default(parisize, 2000000000);
E = ellinit([0,159145,0,5207351716,0]);
Em = ellminimalmodel(E);
print("start ", gettime());
r = iferr(alarm(420, ellmoddegree(Em)), err, print("ERROR/TIMEOUT: ", err); -1);
print("ellmoddegree (= deg/c^2) = ", r);
print("elapsed ms ", gettime());
quit();
