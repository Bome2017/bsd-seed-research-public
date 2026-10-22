from verify_principal import *
d=json.loads((D/'line_source_probe.json').read_text())
hp=d['h_coefficients'];product=mul(hp,[(-1)**i*c for i,c in enumerate(hp)])
assert all(product[i]==0 for i in range(1,len(product),2))
g=[0]
for i in range(6):g=add(g,scale(power(h,i),product[2*i]))
norm=Fraction(res(f5,g),5**(len(g)-1))
assert norm==Fraction(d['norm'])
assert val(norm.numerator,1783)==5
for p,v in d['small_support']:assert val(norm.numerator,p)==v
assert val(norm.numerator,7)==1
# Uniqueness of the unsupported point and its scalar orbit values.
points=[]
for x in range(7):
 for y in range(7):
  if y*y%7==ev(h,x,7) and ev(f5,x,7)==0 and ev(hp,y,7)==0:points.append([x,y])
assert points==[[0,6]]
assert [ev(hp,y,7) for y in [6,5,1,2]]==[0,3,5,1]
result={'status':'PASS','norm_exact_match':True,'norm_q_valuation':5,'unsupported_prime':7,'unsupported_norm_valuation':1,'unique_unsupported_point':points[0],'orbit_h_residues':[0,3,5,1],'method':'stdlib 27x27 integer Bareiss resultant, polynomial recurrences, residue enumeration'}
(D/'verify_line_source.json').write_text(json.dumps(result,indent=2)+'\n')
print('LINE_SOURCE_PASS')
