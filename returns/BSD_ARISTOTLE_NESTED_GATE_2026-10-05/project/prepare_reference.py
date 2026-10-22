"""Verify and expose the original reading set. No network or research execution."""
from pathlib import Path, PurePosixPath
import hashlib, json, zipfile, shutil
ROOT=Path(__file__).resolve().parent
bundle=ROOT/'payload/COMPLETE_READING_SET.zip'
receipt=json.loads((ROOT/'READING_SET_BINDING.json').read_text())
if hashlib.sha256(bundle.read_bytes()).hexdigest()!=receipt['sha256']:
    raise SystemExit('Reading-set archive digest mismatch')
dest=ROOT/'reading_set'
if dest.exists():
    raise SystemExit('reading_set already exists; verify it before reusing or remove only that generated copy')
with zipfile.ZipFile(bundle) as z:
    for i in z.infolist():
        p=PurePosixPath(i.filename)
        if p.is_absolute() or '..' in p.parts or (i.external_attr>>16)&0o170000==0o120000:
            raise SystemExit('Unsafe archive member: '+i.filename)
    for i in z.infolist():
        out=dest.joinpath(*PurePosixPath(i.filename).parts)
        if i.is_dir():out.mkdir(parents=True,exist_ok=True);continue
        out.parent.mkdir(parents=True,exist_ok=True)
        with z.open(i) as src,out.open('wb') as target:shutil.copyfileobj(src,target)
base=dest/receipt['root']
checked=0
for line in (base/'STARTER_MANIFEST.sha256').read_text().splitlines():
    expected,name=line.split('  ',1)
    actual=hashlib.sha256((base/name).read_bytes()).hexdigest()
    if actual!=expected:raise SystemExit('Member digest mismatch: '+name)
    checked+=1
print(json.dumps({'status':'READING_SET_VERIFIED','members_checked':checked,'path':str(base)},indent=2))
