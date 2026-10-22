#!/usr/bin/env python3
"""Independent metadata/custody replay after supervisor completion."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math, re

R = Path(__file__).resolve().parent
H = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = json.loads((R / "RESULT.json").read_text())
assert result["status"] == "TWIST_D23_NONZERO_CERTIFIED"
T = result["cutoff"]
inputs = json.loads((R / "INPUT_BINDINGS.json").read_text())
build = json.loads((R / "BUILD_BINDINGS.json").read_text())
for n, h in build["sha256"].items():
    assert H(R/n) == h, n
assert H(R/"INPUT_BINDINGS.json") == result["input_bindings_sha256"]
assert H(R/"BUILD_BINDINGS.json") == result["build_bindings_sha256"]
nseg=(T+1)//2**24
nblk=(T+2**22-1)//2**22
assert result["unit_count"] == nseg+nblk
expected_root=hashlib.sha256(b"".join(bytes.fromhex(x["coefficients"]["sha256"])
    for x in inputs["segments"][:nseg])).hexdigest()
assert expected_root == result["coefficient_root"]
for x in inputs["segments"][:nseg]:
    for k in ["coefficients","verifier_record"]:
        assert H(Path(x[k]["path"])) == x[k]["sha256"]
# Independent small-prime count for the large-prime part of segment zero.
bound=math.isqrt(T)
sieve=bytearray(b"\1")*(bound+1);sieve[:2]=b"\0\0"
for p in range(2,math.isqrt(bound)+1):
    if sieve[p]:
        sieve[p*p:bound+1:p]=b"\0"*(((bound-p*p)//p)+1)
small_primes=sum(sieve)
seen=set();smooth=pairs=0
first_count=json.loads((R/"FIRST_SEGMENT_COUNT_CHECK.json").read_text())
for rec in result["units"]:
    p=Path(rec["path"]);raw=p.read_bytes()
    assert len(raw)==rec["bytes"] and H(p)==rec["sha256"]
    content,end=raw.rsplit(b"END ",1)
    assert hashlib.sha256(content).hexdigest()==end.strip().decode()
    header=content.splitlines()[0].decode()
    if header.startswith("LSEG "):
        m=re.fullmatch(r"LSEG (\d+) lo (\d+) hi (\d+) apsha ([a-f0-9]{64}) bigprimes (\d+) pairs (\d+) nnz (\d+)",header)
        assert m
        s,lo,hi=int(m[1]),int(m[2]),int(m[3])
        assert 0<=s<nseg and lo==s*2**24 and hi==(s+1)*2**24
        assert m[4]==inputs["segments"][s]["coefficients"]["sha256"]
        assert int(m[5])==inputs["segments"][s]["prime_count"]-(small_primes if s==0 else 0)
        if s==0:
            assert int(m[6])==first_count["independent_pairs"]
            assert int(m[7])==first_count["independent_nonzero_weighted_terms"]
        assert ("L",s) not in seen;seen.add(("L",s));pairs+=int(m[6])
    else:
        m=re.fullmatch(r"BLK (\d+) lo (\d+) hi (\d+) leaf ([a-f0-9]{64}) nnz (\d+) smooth (\d+)",header)
        assert m
        b,lo,hi=int(m[1]),int(m[2]),int(m[3])
        assert 0<=b<nblk and lo==b*2**22+1 and hi==min(lo+2**22,T+1)
        assert ("S",b) not in seen;seen.add(("S",b));smooth+=int(m[6])
assert len(seen)==nseg+nblk and smooth+pairs==T
log=R/f"run_T{T}.log";replay=R/f"combine_T{T}.log"
assert H(log)==result["engine_log_sha256"] and H(replay)==result["combine_log_sha256"]
assert log.read_text().split("COUNT ",1)[1]==replay.read_text().split("COUNT ",1)[1]
m=re.fullmatch(r"\[(-?\d+), (-?\d+)\] / (\d+)",result["interval"])
assert m
lo,hi,den=map(int,m.groups())
assert den>0 and lo<=hi and (lo>0 or hi<0)
binding=Path(inputs["binding_source"])
assert H(binding)==inputs["binding_source_sha256"]
for f in json.loads(binding.read_text())["engine_files"]:
    assert H(Path(f["path"]))==f["sha256"]
review={"time_utc":datetime.now(timezone.utc).isoformat(),
    "result":"PASS_WITH_DECLARED_COMPUTER_ASSISTED_TRUST_BASE",
    "cutoff":T,"atomic_units_verified":len(seen),"coefficient_segments_rehashed":nseg,
    "counts":{"smooth":smooth,"pairs":pairs,"total":smooth+pairs},
    "integer_decimal_interval":{"lower_numerator":lo,"upper_numerator":hi,"denominator":den},
    "zero_excluded":True,"fresh_recombination_identical":True,
    "first_segment_independent_count_check":True,
    "sealed_engine_unchanged":True,"formal_proof":False,"second_full_numerical_implementation":False}
(R/"COMPLETION_REVIEW.json").write_text(json.dumps(review,indent=2)+"\n")
print(json.dumps(review,indent=2))
