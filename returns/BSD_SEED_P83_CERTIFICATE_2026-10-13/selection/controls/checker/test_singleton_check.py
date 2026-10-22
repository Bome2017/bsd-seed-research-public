#!/usr/bin/env python3
"""Negative controls for singleton_check.py and run_singleton.sh, on the 389a1 fixture (p = 7).

Every corrupted case must be INVALID (exit 2); the genuine cases must be NONZERO (l = 29) and INCONCLUSIVE_ZERO
(l = 379). This covers the audit's forged passes (duplicate row, false COUNT, wrong sign and Q) and more.
Exits 0 only if every expectation holds.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
RUNS, REG = f'{BASE}/launcher_runs', f'{BASE}/regression_389a1'
C = os.path.expanduser('~/BSD_RIGOROUS_STREAM_CORE_2026-09-19')
ARB = f'{C}/src/arbcore'
sha = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()


def copy_run(src, dst):
    """A consistent copy: PARAMS and the manifest are re-pointed at the copy, so only the intended corruption differs."""
    shutil.copytree(src, dst)
    t = open(f'{dst}/units/PARAMS').read().split()
    t[12] = os.path.realpath(f'{dst}/units')
    open(f'{dst}/units/PARAMS', 'w').write(' '.join(t) + ' \n')
    m = json.load(open(f'{dst}/RUN_MANIFEST.json'))
    m['params'] = open(f'{dst}/units/PARAMS').read().strip()
    json.dump(m, open(f'{dst}/RUN_MANIFEST.json', 'w'), indent=1)


def refresh_manifest(d):
    m = json.load(open(f'{d}/RUN_MANIFEST.json'))
    m['msl_output_sha256'] = sha(f'{d}/msl.txt')
    m['params'] = open(f'{d}/units/PARAMS').read().strip()
    json.dump(m, open(f'{d}/RUN_MANIFEST.json', 'w'), indent=1)


def edit(d, fn, update_manifest=True):
    lines = open(f'{d}/msl.txt').read().splitlines()
    lines = fn(lines)
    open(f'{d}/msl.txt', 'w').write('\n'.join(lines) + '\n')
    if update_manifest:
        refresh_manifest(d)


def check(d, l=29, **over):
    args = dict(msl=f'{d}/msl.txt', units=f'{d}/units', manifest=f'{d}/RUN_MANIFEST.json', receipts=f'{REG}/logs/ver_*.log',
                arbcore=ARB, curve='0 1 1 -2 0', N='389', p='7', l=str(l), Q='389', sign='1', T='65535', segq='65536',
                latden='1024', apdir=f'{REG}/ap')
    args.update(over)
    cmd = [sys.executable, f'{HERE}/singleton_check.py']
    for k, v in args.items():
        cmd += [f'--{k.replace("_", "-")}', v]
    r = subprocess.run(cmd, capture_output=True, text=True)
    rep = json.loads(r.stdout) if r.stdout.strip().startswith('{') else {'verdict': 'CRASH', 'reasons': [r.stderr[-300:]]}
    return r.returncode, rep


def xb_replace(b_from, b_to_label):
    def f(lines):
        src = next(x for x in lines if x.startswith(f'XB {b_from} '))
        return [re.sub(r'^XB \d+ ', f'XB {b_to_label} ', src) if x.startswith(f'XB {b_to_label} ') else x for x in lines]
    return f


def bump_plus(bs, delta_h):
    def f(lines):
        out = []
        for x in lines:
            m = re.match(r'^XB (\d+) plus (\[[^\]]*\]) cand (-?\d+)/1024(.*)$', x)
            if m and int(m.group(1)) in bs:
                x = f'XB {m.group(1)} plus {m.group(2)} cand {int(m.group(3)) + delta_h}/1024{m.group(4)}'
            out.append(x)
        return out
    return f


def main():
    tmp = tempfile.mkdtemp(prefix='singleton_ctl_')
    results, ok_all = [], True

    def case(name, expect, d_src='l29', mutate=None, l=29, **over):
        nonlocal ok_all
        d = f'{tmp}/{name}'
        copy_run(f'{RUNS}/{d_src}', d)
        if mutate:
            mutate(d)
        code, rep = check(d, l=l, **over)
        good = rep['verdict'] == expect
        ok_all &= good
        results.append({'case': name, 'expect': expect, 'got': rep['verdict'], 'exit': code, 'ok': good,
                        'reason': (rep.get('reasons') or [''])[0][:110]})

    case('baseline_l29_copy', 'NONZERO')
    case('baseline_l379_copy', 'INCONCLUSIVE_ZERO', d_src='l379', l=379)
    case('row_values_copied', 'INVALID', mutate=lambda d: edit(d, xb_replace(1, 2)))
    case('duplicate_label_audit_attack', 'INVALID', mutate=lambda d: edit(
        d, lambda L: [next(y for y in L if y.startswith('XB 1 ')) if x.startswith('XB 2 ') else x for x in L]))
    case('missing_row', 'INVALID', mutate=lambda d: edit(d, lambda L: [x for x in L if not x.startswith('XB 5 ')]))
    case('out_of_range_label', 'INVALID', mutate=lambda d: edit(d, lambda L: [re.sub(r'^XB 28 ', 'XB 30 ', x) for x in L]))
    case('false_count', 'INVALID', mutate=lambda d: edit(d, lambda L: ['COUNT smooth 0 pairs 0 sum 0 T 0 identity 1'
                                                                       if x.startswith('COUNT') else x for x in L]))
    case('wrong_expected_sign', 'INVALID', sign='-1')
    case('wrong_expected_Q', 'INVALID', Q='390')
    case('wrong_expected_T', 'INVALID', T='131071')

    def stale(d):
        shutil.copyfile(f'{RUNS}/l379/units/PARAMS', f'{d}/units/PARAMS')
        refresh_manifest(d)
    case('stale_params_from_other_run', 'INVALID', mutate=stale)
    case('tampered_symbol_manifest_not_updated', 'INVALID', mutate=lambda d: edit(d, bump_plus({1}, 1024), update_manifest=False))
    case('tampered_symbol_asymmetric', 'INVALID', mutate=lambda d: edit(d, bump_plus({1}, 1024)))
    case('tampered_pair_breaks_c0', 'INVALID', mutate=lambda d: edit(d, bump_plus({1, 28}, 1024)))
    case('two_lattice_candidates', 'INVALID', mutate=lambda d: edit(
        d, lambda L: [x.replace('contains 1 unique 1 minus', 'contains 2 unique 0 minus', 1) if x.startswith('XB 3 ') else x for x in L]))

    def bad_receipts(d):
        os.makedirs(f'{d}/fake_logs')
        txt = open(f'{REG}/logs/ver_0.log').read()
        h = re.search(r'ap_sha256 ([0-9a-f]{64})', txt).group(1)
        open(f'{d}/fake_logs/ver_0.log', 'w').write(txt.replace(h, ('0' if h[0] != '0' else '1') + h[1:]))
    tmpd = f'{tmp}/bad_receipt'
    copy_run(f'{RUNS}/l29', tmpd); bad_receipts(tmpd)
    code, rep = check(tmpd, receipts=f'{tmpd}/fake_logs/ver_*.log')
    good = rep['verdict'] == 'INVALID'; ok_all &= good
    results.append({'case': 'bad_receipt_hash', 'expect': 'INVALID', 'got': rep['verdict'], 'exit': code, 'ok': good,
                    'reason': (rep.get('reasons') or [''])[0][:110]})
    case('wrong_engine_binary', 'INVALID', arbcore=f'{C}/verifier/wverify')
    case('wrong_pinned_root', 'INVALID', pinned_segroot='0' * 64)

    # launcher refusals
    r1 = subprocess.run(['bash', f'{HERE}/run_singleton.sh', '0 -22735 0 106272484 0', '6503188012738584', '17', '103',
                         '33218887679', '/nonexistent', '/nonexistent/*', f'{tmp}/seed_refusal'], capture_output=True, text=True,
                        env={**os.environ, 'SINGLETON_AUTHORIZED': 'no'})
    good = r1.returncode == 2 and 'REFUSED' in r1.stdout; ok_all &= good
    results.append({'case': 'launcher_refuses_unauthorized_seed', 'expect': 'REFUSED', 'got': r1.stdout.strip()[:60], 'exit': r1.returncode, 'ok': good})
    r2 = subprocess.run(['bash', f'{HERE}/run_singleton.sh', '0 1 1 -2 0', '389', '7', '29', '65535', f'{REG}/ap',
                         f'{REG}/logs/ver_*.log', f'{RUNS}/l29'], capture_output=True, text=True, env={**os.environ, 'SEGQ': '65536'})
    good = r2.returncode == 2 and 'REFUSED' in r2.stdout; ok_all &= good
    results.append({'case': 'launcher_refuses_existing_outdir', 'expect': 'REFUSED', 'got': r2.stdout.strip()[:60], 'exit': r2.returncode, 'ok': good})

    shutil.rmtree(tmp)
    json.dump({'all_ok': ok_all, 'cases': results}, open(f'{HERE}/CONTROLS.json', 'w'), indent=1)
    for r in results:
        print(f"{'ok ' if r['ok'] else 'BAD'} {r['case']:42s} expect {r['expect']:18s} got {r['got']:18s} exit {r['exit']}  {r.get('reason', '')}")
    print('ALL CONTROLS OK' if ok_all else 'CONTROL FAILURE')
    sys.exit(0 if ok_all else 1)


if __name__ == '__main__':
    main()
