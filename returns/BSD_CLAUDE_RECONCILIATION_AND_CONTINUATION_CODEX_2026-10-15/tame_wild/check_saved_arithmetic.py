#!/usr/bin/env python3
"""Independent exact recheck of saved Oct 14 experiment outputs.

Original roots are read only. This does not regenerate modular symbols,
Fourier/Arb intervals, rational points, or height values.
"""
import hashlib
import json
import math
import re
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HOME = Path('/Users/bsm')
HERE = Path(__file__).resolve().parent
SEED = HOME/'BSD_SEED_FULL_LEVEL_LAW_TEST_2026-10-14'
TAME = HOME/'BSD_TWO_LEG_TAME_EXPERIMENT_2026-10-14'
WILD = HOME/'BSD_WILD_LEG_EXPERIMENT_2026-10-14'
PROOF = HOME/'BSD_TAME_LAW_PROOF_ATTEMPT_OPUS_2026-10-14'
BINDINGS = {}

def read(p):
    b = p.read_bytes()
    BINDINGS[str(p)] = hashlib.sha256(b).hexdigest()
    return b.decode()

def md(x, n):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, n) % n

def valuation(n, p):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def manifest(root):
    path = root/'MANIFEST.sha256'
    if not path.exists():
        return {'present': False}
    total = 0
    failures = []
    for line in read(path).splitlines():
        if not line.strip():
            continue
        expected, name = line.split(None, 1)
        p = (root/name.strip().lstrip('*')).resolve()
        assert p.is_relative_to(root.resolve())
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        total += 1
        if actual != expected:
            failures.append(name)
    assert not failures, (root, failures)
    return {'present': True, 'entries_checked': total, 'mismatches': failures}

def seal(path):
    content = read(path)
    sealpath = Path(str(path)+'.sha256')
    if not sealpath.exists():
        sealpath = path.with_suffix('.sha256')
    expected = read(sealpath).split()[0]
    assert BINDINGS[str(path)] == expected
    return {'sha256': expected, 'matches_current_file': True,
            'independent_timestamp_verified': False}

def vector(s):
    return [F(x.strip()) for x in s.split(',')]

def tame_symbols():
    out = {}
    for p in sorted((TAME/'outputs').glob('sym2_*.txt')):
        for line in read(p).splitlines():
            m = re.fullmatch(r'SYM (\S+) (\d+) (\d+) (\d+) (\d+) \[([^\]]*)\] (\d+) (\d+)', line)
            if not m:
                continue
            key = (m[1], int(m[2]), int(m[3]))
            assert key not in out
            assert m[8] == '1'
            out[key] = vector(m[6])
    return out

def height_det(h, modulus):
    b = (h[2]-h[0]-h[1])*pow(2, -1, modulus) % modulus
    assert (h[2]-h[3]-4*b) % modulus == 0
    return b, (h[0]*h[1]-b*b) % modulus

def tame_check():
    rs = json.loads(read(TAME/'predictions.json'))
    ss = tame_symbols()
    rawrows = {}
    constants = {}
    for line in read(TAME/'outputs/reg2.txt').splitlines():
        if line.startswith('CURVE '):
            constants[line.split()[1]] = int(re.search(r'K=(\d+)', line)[1])
        m = re.fullmatch(r'ROW (\S+) (\d+) (\d+) (\d+) (\d+) (-?\d+) (-?\d+) (\d+) (\d+) \[([^\]]*)\] \[([^\]]*)\]', line)
        if m:
            key = (m[1], int(m[2]), int(m[3]))
            rawrows[key] = ([int(x) for x in m[11].split(',')],
                            [int(x) for x in m[10].split(',')],
                            list(map(int, m.groups()[3:9])))
    assert set(ss).issubset(rawrows)
    clean = []
    mismatch = []
    neg = Counter()
    negnz = Counter()
    for r in rs:
        key = (r['curve'], r['l1'], r['l2'])
        h, V, parameters = rawrows[key]
        assert h == r['h_l1']+r['h_l2'] and V == r['V2']
        assert parameters == [r[k] for k in ('g1','g2','a1','a2','cexp','idx')]
        assert constants[r['curve']] == r['K']
        q = r['q']
        assert r['e1'] == valuation(r['l1']-1,q) and r['e2'] == valuation(r['l2']-1,q)
        assert r['e'] == min(r['e1'],r['e2'])
        assert r['clean'] == bool((r['cexp']*r['idx']) % q)
        if not r['clean']:
            continue
        n1,n2,n = q**r['e1'],q**r['e2'],q**r['e']
        b1,d1 = height_det(h[:4],n1)
        b2,d2 = height_det(h[4:],n2)
        dmix = h[0]*h[5]+h[4]*h[1]-2*b1*b2
        den = (r['cexp']**2*r['idx'])**2
        factor = r['K']*(r['a1']-2)*(r['a2']-2)
        expected = [factor*d1*pow(den,-1,n1)%n1,
                    factor*dmix*pow(den,-1,n)%n,
                    factor*d2*pow(den,-1,n2)%n2]
        c = ss[key]
        assert c[0] == 0 and md(c[1],n1) == 0 and md(c[2],n2) == 0
        actual = [md(c[3],n1),md(c[4],n),md(c[5],n2)]
        if expected != actual:
            mismatch.append([key,q,expected,actual])
        assert expected == [r['pred20'],r['pred11'],r['pred02']]
        variants = {
            'sealed':expected[1],
            'no_Euler':r['K']*dmix*pow(den,-1,n)%n,
            'one_Euler':r['K']*(r['a1']-2)*dmix*pow(den,-1,n)%n,
            'wrong_plus_cross':factor*(h[0]*h[5]+h[4]*h[1]+2*b1*b2)*pow(den,-1,n)%n,
            'no_cross':factor*(h[0]*h[5]+h[4]*h[1])*pow(den,-1,n)%n,
            'sign_flip':(-expected[1])%n,
        }
        for name,value in variants.items():
            neg[name] += value == actual[1]
            negnz[name] += value == actual[1] and actual[1] % q != 0
        clean.append(r)
    assert not mismatch
    assert set(ss) == {(r['curve'],r['l1'],r['l2']) for r in clean}
    return {'all_prediction_rows':len(rs), 'raw_height_pairs':len(rawrows), 'raw_symbol_pairs':len(ss),
            'clean_rows':len(clean), 'nonzero_mod_q':sum(r['pred11']%r['q']!=0 for r in clean),
            'by_curve':dict(Counter(r['curve'] for r in clean)),
            'by_q':dict(Counter(r['q'] for r in clean)),
            'max_mixed_modulus_by_q':{q:max(q**r['e'] for r in clean if r['q']==q) for q in sorted(set(r['q'] for r in clean))},
            'negative_controls_matches':dict(neg),'negative_controls_nonzero_matches':dict(negnz),
            'arithmetic_mismatches':mismatch, 'source_raw_height_binding':True}

def wild_symbols(subdir, prefix):
    out = {}
    for p in sorted(subdir.glob(prefix+'*.txt')):
        for line in read(p).splitlines():
            m = re.fullmatch(r'SYM[WM] (\S+) (\d+) (\d+) \[([^\]]*)\] (\d+) (\d+)',line)
            if m:
                key = (m[1],int(m[2]),int(m[3]))
                assert key not in out and m[6] == '1'
                out[key] = vector(m[4])
    return out

def wild_check():
    old = wild_symbols(WILD/'outputs','symw_')
    new = wild_symbols(WILD/'confirm','symc_')
    assert not set(old).intersection(new)
    datasets = []
    for filename,symbols,regfile in [('predictions_wild.json',old,'outputs/reg_wild.txt'),('confirm/predictions_confirm.json',new,'confirm/reg_confirm.txt')]:
        rs = json.loads(read(WILD/filename))
        raw = {}; constants = {}
        for line in read(WILD/regfile).splitlines():
            if line.startswith('CURVE '):
                constants[line.split()[1]]=int(re.search(r'K=(\d+)',line)[1])
            match = re.fullmatch(r'WROW (\S+) (\d+) (-?\d+) (\d+) (\d+) \[([^\]]*)\]',line)
            if match:
                raw[(match[1],int(match[2]),0)]={'ap':int(match[3]),'cexp':int(match[4]),
                    'idx':int(match[5]),'w':[int(v) for v in match[6].split(',')]}
            match = re.fullmatch(r'MROW (\S+) (\d+) (\d+) (\d+) (-?\d+) (-?\d+) (\d+) (\d+) \[([^\]]*)\] \[([^\]]*)\]',line)
            if match:
                raw[(match[1],int(match[2]),int(match[3]))]={'g':int(match[4]),'ap':int(match[5]),
                    'al':int(match[6]),'cexp':int(match[7]),'idx':int(match[8]),
                    'h':[int(v) for v in match[9].split(',')],'w':[int(v) for v in match[10].split(',')]}
        stats = {'all_prediction_rows':len(rs),'clean_pure':0,'clean_mixed':0,
                 'nonzero_pure':0,'nonzero_mixed':0,'augmentation_and_linear_checks':0,
                 'squared_factor_pure_matches':0,'squared_factor_mixed_matches':0,
                 'forced_wild_squared_matches':0,'curves':{}, 'candidate_matches':{}}
        candidates = {'ap-1':lambda a:a-1,'ap-2':lambda a:a-2,'1':lambda a:1,
                      '1-ap':lambda a:1-a,'ap':lambda a:a}
        cc = Counter()
        for r in rs:
            p = r['p']; l = r.get('l',0)
            key = (r['curve'],p,l)
            assert all(r[k]==v for k,v in raw[key].items())
            assert r['K']==constants[r['curve']]
            assert r['clean'] == bool((r['cexp']*r['idx'])%p)
            if not r['clean']:
                continue
            c = symbols[key]
            assert c[0] == 0
            assert md(c[1],p if not l else p**valuation(l-1,p)) == 0
            if l:
                assert md(c[2],p) == 0
            stats['augmentation_and_linear_checks'] += 1
            bw,dw = height_det(r['w'],p)
            den = pow((r['cexp']**2*r['idx'])**2,-1,p)
            if not l:
                base = r['K']*dw*den
                actual = md(c[2],p)
                kind = 'pure'
            else:
                bl,_ = height_det(r['h'],p)
                h,w = r['h'],r['w']
                dmix = h[0]*w[1]+w[0]*h[1]-2*bl*bw
                base = (r['al']-2)*r['K']*dmix*den
                actual = md(c[4],p)
                kind = 'mixed'
                pure = new.get((r['curve'],p,0),old.get((r['curve'],p,0)))
                assert pure is not None
                stats['forced_wild_squared_matches'] += md(c[5],p) == (r['al']-2)*md(pure[2],p)%p
            stats['clean_'+kind] += 1
            stats['nonzero_'+kind] += actual != 0
            stats['squared_factor_'+kind+'_matches'] += (r['ap']-1)**2*base%p == actual
            for name,fc in candidates.items():
                for sign in ([1] if not l else [1,-1]):
                    cc[kind+':'+str(sign)+'*'+name] += sign*fc(r['ap'])*base%p == actual
            stats['curves'][r['curve']] = stats['curves'].get(r['curve'],0)+1
        stats['candidate_matches'] = dict(cc)
        stats['source_raw_height_binding'] = True
        datasets.append(stats)
    for s in datasets:
        assert s['clean_pure'] == s['squared_factor_pure_matches']
        assert s['clean_mixed'] == s['squared_factor_mixed_matches'] == s['forced_wild_squared_matches']
    return {'initial':datasets[0], 'fresh_confirmation':datasets[1],
            'raw_initial_keys':len(old),'raw_confirmation_keys':len(new),
            'overlapping_raw_arithmetic_keys':0}

BALL = re.compile(r'\[(?:(-?[\d.eE+\-]+) )?\+/- ([\d.eE+\-]+)\]')
def identify_ball(s):
    m = BALL.search(s)
    center,radius = F(m[1] or 0),F(m[2])
    lo,hi = (center-radius)*1024,(center+radius)*1024
    low = -((-lo.numerator)//lo.denominator)
    high = hi.numerator//hi.denominator
    assert low == high
    return F(low,1024)

def generators(l):
    gs = []
    for g in range(2,l):
        image = []; a=1
        for j in range(l-1):
            image.append(a);a=a*g%l
        if len(set(image)) == l-1:
            gs.append((g,{a:j for j,a in enumerate(image)}))
            if len(gs)==2:
                return gs

def seed_check():
    regs = [json.loads(s) for s in read(SEED/'eval/regulator_independent.jsonl').splitlines()]
    output=[]; moduli=[]; count=0
    for reg in regs:
        l,m = reg['l'],reg['m'];moduli.append(m)
        text = read(SEED/f'production/l{l}/msl.txt')
        plus,minus = {},{}
        for line in text.splitlines():
            if not line.startswith('XB '): continue
            a = int(line.split()[1]);assert a not in plus
            before,after = line.split(' minus ',1)
            plus[a] = identify_ball(before.split(' plus ',1)[1]);minus[a]=identify_ball(after)
        assert set(plus)==set(range(1,l))
        assert all(plus[a]==plus[l-a] and minus[a]==-minus[l-a] for a in plus)
        assert all(x.denominator==1 for x in plus.values())
        count+=len(plus)
        singleton = json.loads(read(SEED/f'production/l{l}/SINGLETON_REPORT.json'))
        assert singleton['msl_sha256']==BINDINGS[str(SEED/f'production/l{l}/msl.txt')]
        assert not set(singleton['reasons'])-{'p must be a prime >= 5','v_p(l-1) > 1: outside the frozen k = 1 model'}
        row = {'ell':l,'m':m,'symbol_intervals_reidentified':2*len(plus),'roots':[],
               'historical_singleton_verdict':singleton['verdict'], 'historical_singleton_reasons':singleton['reasons']}
        # Independent point-count check on the stated minimal model.
        cardinality = 1 + sum(1 if z==0 else 2 if pow(z,(l-1)//2,l)==1 else 0
                             for x in range(l) for z in [(x**3-x*x-66020924*x-65074271436)%l])
        assert cardinality==reg['E_Fl'] and l+1-cardinality==reg['a_l']
        for g,index in generators(l):
            exact=[sum(F(math.comb(index[a],k))*plus[a] for a in plus) for k in range(3)]
            reduced=[md(sum(F(math.comb(index[a]%m,k))*plus[a] for a in plus),m) for k in range(3)]
            assert [md(x,m) for x in exact] == reduced
            assert exact[0]==0 and reduced[1]==0
            R_values=[]
            for r in reg['rows']:
                if r['g']!=g:continue
                # This output stores [h1,h2,b12], not [h1,h2,h(Q1+Q2)].
                h=r['h']; b=h[2]
                R=(h[0]*h[1]-b*b)*pow(r['M']**4,-1,m)%m
                assert R==r['R']
                assert 288*(reg['a_l']-2)*R%m==reduced[2]==r['pred_c2']
                R_values.append(R)
            assert len(R_values)==2 and len(set(R_values))==1
            divisor=(reg['a_l']-2)*R_values[0]
            assert math.gcd(divisor,m)==1
            K_residue=reduced[2]*pow(divisor,-1,m)%m
            exact3=md(sum(F(math.comb(index[a],3))*plus[a] for a in plus),m)
            reduced3=md(sum(F(math.comb(index[a]%m,3))*plus[a] for a in plus),m)
            row['roots'].append({'g':g,'coefficients_0_to_2':list(map(str,exact)),
                                 'coefficient_residues_0_to_2':reduced,'regulator':R_values[0],
                                 'deduced_K_residue':K_residue,
                                 'degree3_full_index_residue':exact3,'degree3_reduced_index_residue':reduced3})
        output.append(row)
    modulus=math.lcm(*moduli)
    assert modulus==14175
    return {'auxiliary_primes':len(regs),'plus_symbols':count,'plus_and_minus_intervals':2*count,
            'rows':output,'constant_constraint_modulus':modulus,
            'distinct_integer_constant_passing_same_seven_rows':288+modulus,
            'degree3_warning':{'m':9,'j':0,'binomial_shift_difference_mod_m':math.comb(9,3)%9,
                               'affects_reported_degree2_conclusion':False}}

def formal_checks():
    # Exact coefficient identity det(A X+B Y), without a CAS or a p-adic height assertion.
    tests=0
    for a,b,c,d,e,f in __import__('itertools').product(range(-1,2),repeat=6):
        for X,Y in [(1,2),(2,-1),(-1,-2)]:
            lhs=(a*X+d*Y)*(c*X+f*Y)-(b*X+e*Y)**2
            rhs=(a*c-b*b)*X*X+(a*f+c*d-2*b*e)*X*Y+(d*f-e*e)*Y*Y
            assert lhs==rhs;tests+=1
    wild=0
    for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
        def phi(a):return (-(pow(a,p-1,p*p)-1)//p)%p
        assert phi(1+p)==1 and phi(p*p-1)==0
        for a in range(1,p*p):
            if a%p:
                assert phi(a)==phi(p*p-a)
                for b in [1+p,2,p*p-1]:
                    assert phi(a*b) == (phi(a)+phi(b))%p
                wild+=1
        assert math.comb(p,3)%p==0
    return {'determinant_polarization_integer_cases':tests,'wild_coordinate_unit_cases':wild,
            'p_ge5_degree2_transfer_sum_zero':True,
            'not_a_proof_of_global_or_canonical_height_comparison':True}

def main():
    for root in (SEED,TAME,WILD,PROOF):
        for p in root.glob('*.md'):
            read(p)
        for sub in ('scripts','confirm','eval'):
            for pattern in ('*.gp','*.py'):
                for p in (root/sub).glob(pattern):
                    read(p)
    out={'scope':'Saved-output arithmetic and source-code audit; no new modular-symbol, Arb, or height production.',
         'manifests':{p.name:manifest(p) for p in (SEED,TAME,WILD,PROOF)},
         'seals':{str(p):seal(p) for p in (SEED/'PREDICTIONS_SEALED.md',TAME/'predictions.json',
                                         WILD/'predictions_wild.json',WILD/'confirm/predictions_confirm.json')},
         'seed':seed_check(),'two_leg_tame':tame_check(),'wild':wild_check(),
         'formal_algebra':formal_checks()}
    (HERE/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    (HERE/'INPUT_BINDINGS.json').write_text(json.dumps(BINDINGS,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('seed','seals')},indent=2))
    print('SEED:',out['seed']['auxiliary_primes'],'tables;',out['seed']['plus_and_minus_intervals'],'intervals; K modulus',out['seed']['constant_constraint_modulus'])

if __name__=='__main__':main()
