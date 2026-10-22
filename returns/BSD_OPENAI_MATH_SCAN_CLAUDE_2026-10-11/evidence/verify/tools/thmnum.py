"""Approximate amsthm/equation numbering for a LaTeX manuscript whose
main file \input's sections. Usage: python3 -I thmnum.py MAIN.tex
Prints: section numbers/titles, theorem-like environments with numbers,
labels, first line of statement; numbered equations with labels/tags.
Read-only; never executes anything from the manuscript."""
import re, sys, os

main = sys.argv[1]
base = os.path.dirname(main)
src = open(main, encoding='utf-8', errors='replace').read()
# theorem env names sharing the 'theorem' counter
allsrc = src
for inp0 in re.findall(r'^\s*\\input\{([^}]+)\}', src, re.M):
    p0 = os.path.join(base, inp0 if inp0.endswith('.tex') else inp0 + '.tex')
    if os.path.exists(p0): allsrc += open(p0, encoding='utf-8', errors='replace').read()
envs = set(re.findall(r'\\newtheorem\{(\w+)\}\[theorem\]', allsrc)) | {'theorem'}
starred = set(re.findall(r'\\newtheorem\*\{(\w+)\}', src))
inputs = re.findall(r'^\s*\\input\{([^}]+)\}', src, re.M)
files = []
for inp in inputs:
    p = os.path.join(base, inp)
    if not p.endswith('.tex'):
        p += '.tex'
    if os.path.exists(p):
        files.append(p)
sec = 0; thm = 0; eq = 0; app = False
secs = []
out = []
env_re = re.compile(r'\\begin\{(' + '|'.join(sorted(envs)) + r')\}(\[[^\]]*\])?')
for f in files:
    lines = open(f, encoding='utf-8', errors='replace').read().split('\n')
    in_eq = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith('%'):
            continue
        if re.match(r'\\appendix', s):
            app = True; sec = 0
        m = re.match(r'\\section\*?(\[[^\]]*\])?\{(.*)', s)
        if m and not s.startswith('\\section*'):
            m = re.match(r'(.*)', m.group(2))
            sec += 1; thm = 0; eq = 0
            lab = re.search(r'\\label\{([^}]*)\}', line)
            out.append(f"SECTION {chr(64+sec) if app else sec} {m.group(1)[:70]} [{os.path.basename(f)}:{i}] {lab.group(1) if lab else ''}")
            continue
        m = re.match(r'\\subsection\*?\{(.*)', s)
        if m:
            out.append(f"   subsection: {m.group(1)[:80]} [{os.path.basename(f)}:{i}]")
        for m in env_re.finditer(line):
            thm += 1
            lab = re.search(r'\\label\{([^}]*)\}', line) or (re.search(r'\\label\{([^}]*)\}', lines[i] if i < len(lines) else '') )
            out.append(f"  {m.group(1).capitalize()} {chr(64+sec) if app else sec}.{thm} {m.group(2) or ''} label={lab.group(1) if lab else '?'} [{os.path.basename(f)}:{i}]")
        # equations
        if re.search(r'\\begin\{(equation|align|gather|multline|eqnarray)\}', line):
            in_eq = True; eq_start = i; eq_lines = 0; eq_label = None; eq_tag = None; nonumber = False
        if in_eq:
            lab = re.search(r'\\label\{([^}]*)\}', line)
            if lab and not eq_label: eq_label = lab.group(1)
            tag = re.search(r'\\tag\{([^}]*)\}', line)
            if tag: eq_tag = tag.group(1)
            if '\\nonumber' in line or '\\notag' in line: nonumber = True
            if re.search(r'\\\\', line) and not re.search(r'\\begin\{(equation|align)', line): eq_lines += 1
            if re.search(r'\\end\{(equation|align|gather|multline|eqnarray)\}', line):
                in_eq = False
                if eq_tag:
                    out.append(f"  eq tag=({eq_tag}) label={eq_label} [{os.path.basename(f)}:{eq_start}]")
                else:
                    n = 1 + (eq_lines if re.search(r'align|gather', lines[eq_start-1]) else 0)
                    first = eq + 1
                    eq += n
                    out.append(f"  eq ({sec}.{first}{'-' + str(sec) + '.' + str(eq) if n > 1 else ''}) label={eq_label} nonumber={nonumber} [{os.path.basename(f)}:{eq_start}]")
print('\n'.join(out))
