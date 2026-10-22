"""Exact enumeration of the changed-model local inputs; no Selmer answers."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def check(E,p,points):
    a1,a2,a3,a4,a6=E
    def equation(x,y):return y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6
    finite=[(x,y) for x in range(p) for y in range(p) if equation(x,y)%p==0]
    errors=[equation(x,y) for x,y in points]
    assert not any(errors)
    n=1+len(finite);a=p+1-n
    return {'curve':E,'coefficient_prime':p,'finite_points':finite,
            'point_count':n,'trace':a,'ordinary':a%p!=0,
            'nonanomalous':n%p!=0,'rational_points':points,
            'point_equations':errors}

def main():
    rows=[check([0,0,1,-13,18],7,[(1,2),(3,2)]),
          check([0,-1,1,-22826,2411880],7,[(63,1104),(110,1104)])]
    assert [r['point_count'] for r in rows]==[11,10]
    (HERE/'CURVE_COUNT_REPLAY.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows))

if __name__=='__main__':main()
