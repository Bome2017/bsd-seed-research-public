\\ p3_reg_robust.gp -- robustness of ord_3 Reg_3 = 2 under 3-integral sigma/E2 normalisation shifts (rank-one update lemma).
\\ Scalar cyclotomic height entries from 1x1 regulators (ellpadicheight returns a 2-vector; ellpadicregulator is the scalar pairing).
\\ Minimal model only (u = 1, x-shift 7578 from the seed model), where PARI's model-translation defect vanishes.
E0 = ellinit([0,-22735,0,106272484,0]); Em = ellminimalmodel(E0, &ch);
P1 = ellchangepoint([4547,327384], ch); P2 = ellchangepoint([5184,281520], ch); P12 = elladd(Em, P1, P2);
p = 3; n = 16;
print("minimal model ", [Em.a1,Em.a2,Em.a3,Em.a4,Em.a6], " ; a_3 = ", ellap(Em,3), " ; PARI Kodaira code at 3 = ", elllocalred(Em,3)[2], " (6 = I_2)");
H11 = ellpadicregulator(Em, p, n, [P1]); H22 = ellpadicregulator(Em, p, n, [P2]); H12 = (ellpadicregulator(Em, p, n, [P12]) - H11 - H22)/2;
R = ellpadicregulator(Em, p, n, [P1, P2]); D = H11*H22 - H12^2;
print("ord_3 [h11, h12, h22] = ", [valuation(H11,3), valuation(H12,3), valuation(H22,3)], " ; ord_3 Reg_3 = ", valuation(R,3), " ; ord_3(det of entries) = ", valuation(D,3), " ; ord_3(R - det) = ", valuation(R - D, 3));
Q1 = ellmul(Em, P1, 8); Q2 = ellmul(Em, P2, 8);
print("8P in E_1(Q_3): v_3(x(8P1)) = ", valuation(Q1[1],3), ", v_3(x(8P2)) = ", valuation(Q2[1],3));
L1 = ellpadiclog(Em, p, n, Q1)/8; L2 = ellpadiclog(Em, p, n, Q2)/8;
v1 = valuation(L1,3); v2 = valuation(L2,3); t1 = 2*v1 + valuation(H22,3); t2 = v1 + v2 + valuation(H12,3); t3 = 2*v2 + valuation(H11,3);
print("ord_3 [log P1, log P2] = ", [v1, v2], " ; ord_3 of update terms l1^2 h22, l1 l2 h12, l2^2 h11 = ", [t1, t2, t3]);
print(if(vecmin([t1,t2,t3]) > valuation(R,3), "ROBUST: any c in Z_3 changes det by ord >= ", "NOT ROBUST: min term ord "), vecmin([t1,t2,t3]), " vs ord det = ", valuation(R,3));
print("ord_3 log_3(4) = ", valuation(log(4 + O(3^n)),3), " => ord_3 Reg_gamma = ", valuation(R,3) - 2*valuation(log(4 + O(3^n)),3));
