import inspect, sys
from sage.schemes.elliptic_curves.lseries_ell import Lseries_ell
src = inspect.getsource(Lseries_ell.L_ratio)
print(src)
