# Index-one proof for the displayed basis: eclib saturation with an automatically computed (proven) prime bound.
E = EllipticCurve([0,-22735,0,106272484,0])
P1, P2 = E(4547, 327384), E(5184, 281520)
pts, index, reg = E.saturation([P1, P2], max_prime=-1, verbose=True)
print("saturation index:", index)
print("saturated points equal input:", set(pts) == {P1, P2})
print("regulator of input basis (Sage normalization):", E.regulator_of_points([P1, P2]))
print("torsion order:", E.torsion_order())
