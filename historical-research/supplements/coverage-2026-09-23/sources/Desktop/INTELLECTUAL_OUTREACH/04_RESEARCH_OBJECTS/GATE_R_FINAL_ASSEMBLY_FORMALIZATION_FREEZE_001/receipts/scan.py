import re, sys, pathlib
BLOCK = re.compile(r'/-.*?-/', re.S)
def strip(t):
    t = BLOCK.sub('', t)
    t = re.sub(r'--[^\n]*', '', t)
    return re.sub(r'"[^"\n]*"', '""', t)
root = pathlib.Path(sys.argv[1])
files = sorted(root.rglob('*.lean'))
text = {f: strip(f.read_text()) for f in files}
print(f"  files scanned: {len(files)}   (stripped of block comments, line comments, string literals)")
POS = ['theorem','Finite','GateR','Module.rank','rank_eq_zero_iff']
NEG = ['zzqqxx_cannot_occur']
FORB = ['sorry','admit','native_decide','ofReduceBool','implemented_by','unsafe','extern',
        'trustCompiler','finrank','Group.rank','AddGroup.rank','Module.Finite','Module.Free',
        'AddGroup.FG','Fintype','Mordell','SelmerSet','LocalKummer']
def count(tok, regex=False):
    pat = tok if regex else re.escape(tok)
    return sum(len(re.findall(pat, t)) for t in text.values())
def where(tok, lim=4):
    out=[]
    for f,t in text.items():
        for i,l in enumerate(t.splitlines(),1):
            if tok in l: out.append(f"      {f.relative_to(root)}:{i}: {l.strip()[:110]}")
    return out[:lim]
print("  POSITIVE CONTROLS (must be nonzero or the scanner is broken):")
for t in POS: print(f"    {t:<22} {count(t)}")
print("  NEGATIVE CONTROL:")
for t in NEG: print(f"    {t:<22} {count(t)}")
print("  ANNOTATION FORM of axiom declarations:")
print(f"    {'^axiom (line start)':<22} {count(r'^\s*axiom\s', regex=True)}")
print("  FORBIDDEN TOKENS — every count printed, every hit shown:")
for t in FORB:
    c = count(t)
    print(f"    {t:<22} {c}")
    if c: [print(l) for l in where(t)]
