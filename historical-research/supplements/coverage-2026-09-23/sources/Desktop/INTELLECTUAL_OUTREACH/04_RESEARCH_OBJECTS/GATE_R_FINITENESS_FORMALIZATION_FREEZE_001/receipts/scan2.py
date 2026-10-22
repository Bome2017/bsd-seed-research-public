import re, sys, pathlib
BLOCK = re.compile(r'/-.*?-/', re.S)
def strip_keep_lines(t):
    # replace comment bodies with equal-length blanks so LINE NUMBERS ARE PRESERVED
    def blank(m): return re.sub(r'[^\n]', ' ', m.group(0))
    t = BLOCK.sub(blank, t)
    t = re.sub(r'--[^\n]*', blank, t)
    t = re.sub(r'"[^"\n]*"', blank, t)
    return t
root = pathlib.Path(sys.argv[1])
files = sorted(root.rglob('*.lean'))
text = {f: strip_keep_lines(f.read_text()) for f in files}
print(f"  files scanned: {len(files)}  (comments blanked in place, so line numbers match the ORIGINAL file)")
# declaration-form patterns, ALL with re.M
DECL = {
 'axiom declaration'      : r'(?m)^\s*axiom\s',
 'unsafe declaration'     : r'(?m)^\s*unsafe\s',
 'partial def'            : r'(?m)^\s*partial\s+def\s',
 '@[implemented_by]'      : r'(?m)^\s*@\[implemented_by',
 '@[extern]'              : r'(?m)^\s*@\[extern',
 'theorem (POS CONTROL)'  : r'(?m)^\s*theorem\s',
 'lemma (POS CONTROL)'    : r'(?m)^\s*lemma\s',
}
TOK = ['sorry','admit','native_decide','ofReduceBool','trustCompiler','sorryAx']
print("  DECLARATION FORMS (every pattern uses re.MULTILINE):")
for name, pat in DECL.items():
    hits = [(f.relative_to(root), t[:m.start()].count('\n')+1, t.splitlines()[t[:m.start()].count('\n')].strip())
            for f, t in text.items() for m in re.finditer(pat, t)]
    print(f"    {name:<24} {len(hits)}")
    for h in hits[:200]:   # NO truncation below 200
        print(f"        {h[0]}:{h[1]}: {h[2][:100]}")
print("  BARE TOKENS:")
for tok in TOK:
    hits = [(f.relative_to(root), t[:m.start()].count('\n')+1) for f,t in text.items() for m in re.finditer(re.escape(tok), t)]
    print(f"    {tok:<24} {len(hits)}" + ("" if not hits else "  " + str(hits[:20])))
