# psi^* omega' = c * omega: Sage Velu isogeny scaling factor, and the u of the isomorphisms to the global minimal model of E'
m=2243; n=12; A=m+16*n^2; B=m+25*n^2
E=EllipticCurve([0,-5*A,0,4*A*B,0]); T=E(0,0)
psi=E.isogeny(T); Ev=psi.codomain()
print("Velu codomain:",Ev.ainvs()," scaling_factor (psi^*omega' = c*omega):",psi.scaling_factor())
Estd=EllipticCurve([0,10*A,0,9*m*A,0]); i1=Ev.isomorphism_to(Estd); Em=Estd.minimal_model(); i2=Estd.isomorphism_to(Em)
print("iso Velu->standard u =",i1.u," ; standard->minimal u =",i2.u, " ; composite scaling:", psi.scaling_factor()/(i1.u*i2.u))
print("E minimal (u=1):",E.is_global_minimal_model()," Estd minimal:",Estd.is_global_minimal_model())
# real components and where psi(E(R)) lands: image of the non-identity component point T+? take a real point on the egg of E
e=sorted([r for r,_ in (x^3-5*A*x^2+4*A*B*x).roots(RR)]); print("2-division roots E:",e)
xe=RR((e[0]+e[1])/2); ye=sqrt(xe^3-5*A*xe^2+4*A*B*xe); Ep_R=EllipticCurve(RR,Estd.ainvs())
X=ye^2/xe^2; print("psi(egg point) x-coordinate:",X, " E' 2-division roots:",sorted([r for r,_ in (x^3+10*A*x^2+9*m*A*x).roots(RR)]))
