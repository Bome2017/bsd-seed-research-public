#!/usr/bin/env python3
import concurrent.futures, hashlib, json, urllib.request, ast
from pathlib import Path
BASE=Path(__file__).resolve().parent
SHA='25cec5ecfec8b9f016eb1631ac633194c2bed39f'
BASE.joinpath('sources').mkdir(exist_ok=True)

def fetch(lo):
    name=f'allbigsha.{lo:05d}-{lo+9999:05d}'
    url=f'https://raw.githubusercontent.com/JohnCremona/ecdata/{SHA}/allbigsha/{name}'
    raw=(BASE/'sources'/name).read_bytes() if (BASE/'sources'/name).exists() else urllib.request.urlopen(url,timeout=45).read()
    (BASE/'sources'/name).write_bytes(raw)
    rows=[]
    for lineno,line in enumerate(raw.decode().splitlines(),1):
        t=line.split()
        if int(t[4])==2 and int(t[6])%9==0:
            rows.append(dict(label=t[0]+t[1]+t[2],conductor=int(t[0]),ainvs=ast.literal_eval(t[3]),rank=int(t[4]),torsion=int(t[5]),analytic_sha_selection=int(t[6]),source_file=name,line=lineno,raw=line,good_at_3=int(t[0])%3!=0))
    return dict(file=name,url=url,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),rows
records=[];rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    for rec,found in ex.map(fetch,range(0,500000,10000)):
        records.append(rec);rows.extend(found)
rows.sort(key=lambda r:(r['conductor'],r['label']))
(BASE/'SOURCE.json').write_text(json.dumps(dict(repository='JohnCremona/ecdata',commit=SHA,scope='allbigsha blocks 0-499999; predicted Sha used only for selection',files=records),indent=2)+'\n')
(BASE/'candidates.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['label'],r['ainvs'],r['analytic_sha_selection'],'good3',r['good_at_3'])
print('TOTAL',len(rows),'GOOD3',sum(r['good_at_3'] for r in rows))
