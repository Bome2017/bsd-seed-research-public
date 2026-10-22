"""Exact rational reading and outward rounding of the final Arb dumps."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
log=root/'evidence'/sys.argv[1]
def dyadic(m,e):
    m,e=int(m,16),int(e,16)
    return Q(m*(1<<e)) if e>=0 else Q(m,1<<-e)
def ball(s):
    a,b,c,d=s.split();return dyadic(a,b),dyadic(c,d)
balls={}
for line in log.read_text().splitlines():
    name,_,value=line.partition(' ')
    if name.endswith('_DUMP'):balls[name[:-5]]=ball(value)
def enclosure(name):
    mid,rad=balls[name];return mid-rad,mid+rad
def outward(bounds,digits=12):
    lo,hi=bounds;scale=10**digits
    a=(lo*scale).__floor__();b=(hi*scale).__ceil__()
    def fmt(x):
        sign='-' if x<0 else '';x=abs(x)
        return sign+str(x//scale)+'.'+str(x%scale).zfill(digits)
    return [fmt(a),fmt(b)]
direct=enclosure('DELTA_INTERVAL');ibp=enclosure('IBP_DELTA_INTERVAL')
overlap=max(direct[0],ibp[0]),min(direct[1],ibp[1])
assert overlap[0]<=overlap[1]
status='ENDPOINT_DELTA_NONZERO_PROVED' if overlap[0]>0 or overlap[1]<0 else 'ENDPOINT_DELTA_ZERO_NOT_RESOLVED'
for prefix in ['', 'IBP_']:
    m,r=balls[prefix+'FINITE_INTEGRAL']; em,er=balls[prefix+'TOTAL_ANALYTIC_ERROR']
    lo,hi=enclosure(prefix+'DELTA_INTERVAL')
    assert lo<=m-r-em-er and hi>=m+r+em+er
error_keys=['BALL_ARITHMETIC_RADIUS','COEFFICIENT_TAIL','COMPRESSION_ERROR',
            'RESIDUAL_SERIES_ERROR','ADAPTIVE_COEFFICIENT_CUTOFF',
            'GAUSS_QUADRATURE_ERROR','INFINITE_INTEGRAL_TAIL','TOTAL_ANALYTIC_ERROR']
data={'status':status,'log':str(log),
      'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),
      'direct_interval':outward(direct),'integration_by_parts_interval':outward(ibp),
      'intersection_interval':outward(overlap),'error_upper_bounds':{}}
# Scientific decimal upper bounds, rounded up at 8 significant figures.
from decimal import Decimal,localcontext,ROUND_CEILING
for prefix in ['', 'IBP_']:
    for key in error_keys:
        m,r=balls[prefix+key];q=m+r
        with localcontext() as ctx:
            ctx.prec=8;ctx.rounding=ROUND_CEILING
            value=Decimal(q.numerator)/Decimal(q.denominator)
        data['error_upper_bounds'][prefix+key]=str(value)
out=root/'evidence'/'CERTIFICATE.json';out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
