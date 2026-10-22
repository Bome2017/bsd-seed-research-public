"""Custody audit of the ten pinned recent returns; no theorem certification."""
from pathlib import Path
import hashlib, json, re, sys, zipfile

BASE = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path('/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab')
OUT = Path(__file__).resolve().parent
NAMES = json.loads((OUT/'STATE.json').read_text())['scope_returns']
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

records=[]; errors=[]
custody=[]
for p in (BASE/'work/returns').glob('*CUSTODY*.json'):
    try: custody.append((p,json.loads(p.read_text())))
    except (ValueError,OSError): pass
for name in NAMES:
    root=BASE/'work/returns'/name
    entries=[]
    for line in (root/'MANIFEST.sha256').read_text().splitlines():
        if not line.strip(): continue
        m=re.fullmatch(r'([0-9a-f]{64})\s+\*?(.+)',line)
        if not m: raise ValueError((name,line))
        digest,rel=m.groups(); p=(root/rel).resolve()
        if not p.is_relative_to(root.resolve()): raise ValueError(rel)
        ok=p.is_file() and sha(p)==digest
        entries.append({'path':rel,'sha256':digest,'ok':ok})
        if not ok: errors.append([name,'manifest',rel])
    archive=BASE/'work/returns/archives'/f'{name}.zip'
    zip_records=[]
    with zipfile.ZipFile(archive) as z:
        bad=z.testzip()
        if bad: errors.append([name,'zip_crc',bad])
        for info in z.infolist():
            if info.is_dir(): continue
            parts=Path(info.filename).parts
            if '..' in parts or info.filename.startswith('/'):
                raise ValueError(info.filename)
            rel=Path(*parts[1:]) if parts[0]==name else Path(*parts)
            p=root/rel
            ok=p.is_file() and hashlib.sha256(z.read(info)).hexdigest()==sha(p)
            zip_records.append({'path':str(rel),'ok':ok})
            if not ok: errors.append([name,'archive_copy',str(rel)])
    in_zip={x['path'] for x in zip_records}
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    if actual!=in_zip: errors.append([name,'archive_coverage',sorted(actual^in_zip)])
    digest=sha(archive)
    matches=[(str(p.relative_to(BASE)),d) for p,d in custody if any(Path(str(d.get(k,''))).name in {name,name+'.zip'} for k in ['return','return_folder','lab_return','archive'])]
    custody_ok=any(d.get('archive_sha256',d.get('sha256'))==digest and d.get('archive_bytes',d.get('bytes'))==archive.stat().st_size for p,d in matches)
    if not custody_ok: errors.append([name,'custody_binding',matches])
    records.append({'return':name,'manifest_count':len(entries),'manifest_pass':all(x['ok'] for x in entries),'archive_members':len(zip_records),'archive_copy_pass':all(x['ok'] for x in zip_records) and actual==in_zip,'archive_sha256':digest,'archive_bytes':archive.stat().st_size,'custody_matches':[p for p,d in matches],'custody_pass':custody_ok,'manifest_entries':entries})
result={'status':'PASS' if not errors else 'FAIL','scope':'Pinned ten recent returns; manifests, ZIP CRC, exact archive/tree equality, external custody digests; not theorem verification','returns':records,'manifest_entries':sum(x['manifest_count'] for x in records),'archive_members':sum(x['archive_members'] for x in records),'errors':errors}
(OUT/'CUSTODY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='returns'},indent=2))
sys.exit(bool(errors))
