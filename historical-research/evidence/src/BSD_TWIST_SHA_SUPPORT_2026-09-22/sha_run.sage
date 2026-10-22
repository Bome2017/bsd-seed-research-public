import sys, signal
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM, handler)
def attempt(name, fn, secs):
    print("---- %s (limit %ds) ----" % (name,secs)); sys.stdout.flush()
    signal.alarm(secs)
    try:
        r = fn(); signal.alarm(0); print("%s = %r" % (name,r))
    except TO:
        signal.alarm(0); print("%s : TIMED OUT after %ds" % (name,secs))
    except Exception as e:
        signal.alarm(0); print("%s : RAISED %s: %s" % (name,type(e).__name__,e))
    sys.stdout.flush()
Em = EllipticCurve([0,159145,0,5207351716,0]).minimal_model()
print("conductor =", Em.conductor())
print("additive primes (Kodaira) :", [p for p in [2,3,7,2243,4547,5843] if Em.local_data(p).has_additive_reduction()])
print("multiplicative primes     :", [p for p in [2,3,7,2243,4547,5843] if Em.local_data(p).has_multiplicative_reduction()])
for p in [2,3,7,2243,4547,5843]:
    ld = Em.local_data(p); print("  p=%-5d kodaira=%-6s c_p=%d additive=%s split_mult=%s" % (p, ld.kodaira_symbol(), ld.tamagawa_number(), ld.has_additive_reduction(), ld.has_split_multiplicative_reduction()))
attempt("isogeny_class_size", lambda: len(Em.isogeny_class()), 300)
attempt("non_surjective", lambda: Em.galois_representation().non_surjective(), 600)
attempt("L_ratio", lambda: Em.lseries().L_ratio(), 600)
attempt("sha.an", lambda: Em.sha().an(), 600)
attempt("sha.bound_kato", lambda: Em.sha().bound_kato(), 600)
