#!/usr/bin/env python3
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parent
rows = ast.literal_eval((root/'line_norm_integer_input.gp').read_text())
bound = 419775
sieve = bytearray(b'\1')*(bound+1)
sieve[:2] = b'\0\0'
for q in range(2,int(bound**.5)+1):
    if sieve[q]:
        sieve[q*q:bound+1:q] = b'\0'*((bound-q*q)//q+1)
primes = [q for q in range(2,bound+1) if sieve[q]]
assert len(primes) == 35373
out = []
for i,numerator,denominator,reported_cofactor,admitted in rows:
    cofactor = 1
    for remaining in (abs(numerator),denominator):
        for q in primes:
            while remaining % q == 0:
                remaining //= q
            if remaining == 1:
                break
        cofactor *= remaining
    assert cofactor == reported_cofactor and cofactor > 1 and admitted == 0
    out.append([i,len(str(cofactor)),str(cofactor)])
result = {
    'status':'ALL31_EXACT_NORMS_HAVE_OUTSIDE_RATIONAL_SUPPORT',
    'functions':31,'individual_admitted':0,
    'outside_cofactor_digit_range':[min(x[1] for x in out),max(x[1] for x in out)],
    'rows_id_digits_cofactor':out,
    'method':'Actual5torsion and scalar2 source,31line/tangent incidences and norm-resultant identities checked inGP; independent exhaustivePython trial division through419775',
    'does_not_exclude_cancellation_between_functions':True,
}
print(json.dumps(result,indent=2))
