#!/usr/bin/env python3
"""Reviewer's checkpoint tampering helper (acts ONLY on copies inside the review folder).

  tamper.py rehash FILE                      recompute the SHA-256 trailer
  tamper.py flip FILE M K BYTE [rehash]      xor 0x01 into byte BYTE (0..15, little-endian) of i128 entry K
  tamper.py add FILE M K DELTA [rehash]      add the integer DELTA (units of 2^-96) to i128 entry K
  tamper.py delU FILE U [fixnrec] [rehash]   delete the 'U <U> ...' record line (optionally decrement NREC)
  tamper.py info FILE M                       print NREC, units, fp of each record
"""
import sys, hashlib, re
def load(fn):
    d = open(fn, 'rb').read(); assert d[-70:-65] == b'\nEND ' and d[-1:] == b'\n'; return d[:-70]
def save(fn, body, rehash, old_trailer=None):
    if rehash: tr = b'\nEND ' + hashlib.sha256(body).hexdigest().encode() + b'\n'
    else: tr = old_trailer
    open(fn, 'wb').write(body + tr)
cmd, fn = sys.argv[1], sys.argv[2]
raw = open(fn, 'rb').read(); old_tr = raw[-70:]; body = raw[:-70]
if cmd == 'rehash':
    save(fn, body, True)
elif cmd in ('flip', 'add'):
    M, K = int(sys.argv[3]), int(sys.argv[4]); rehash = 'rehash' in sys.argv[5:]
    off = len(body) - 16 * M + 16 * K
    b = bytearray(body)
    if cmd == 'flip':
        byte = int(sys.argv[5]); b[off + byte] ^= 1
    else:
        delta = int(sys.argv[5]); v = int.from_bytes(b[off:off + 16], 'little', signed=True) + delta
        b[off:off + 16] = v.to_bytes(16, 'little', signed=True)
    save(fn, bytes(b), rehash, old_tr)
elif cmd == 'delU':
    u = int(sys.argv[3]); fix = 'fixnrec' in sys.argv[4:]; rehash = 'rehash' in sys.argv[4:]
    i = body.index(b'\nU %d fp ' % u) + 1; j = body.index(b'\n', i) + 1
    nb = body[:i] + body[j:]
    if fix:
        m = re.search(rb'\nNREC (\d+)\n', nb); n = int(m.group(1))
        nb = nb[:m.start()] + b'\nNREC %d\n' % (n - 1) + nb[m.end():]
    save(fn, nb, rehash, old_tr)
elif cmd == 'info':
    M = int(sys.argv[3]); text = body[:len(body) - 16 * M].decode()
    recs = re.findall(r'^U (\d+) fp ([0-9a-f]+) nterm (\d+) cnt (\d+)', text, re.M)
    print('NREC', re.search(r'NREC (\d+)', text).group(1), 'units', [int(r[0]) for r in recs][:12], '...')
    for r in recs[:5]: print('  U', r[0], 'fp', r[1], 'nterm', r[2], 'cnt', r[3])
