from sage.all import *
import json, time
E=mwrank_EllipticCurve([1,1,1,1878418,-485198548],verbose=True)
MW=mwrank_MordellWeil(E,verbose=True)
MW.process([[480,22723,1]])
print('SATURATION_START',flush=True)
r=MW.saturate()
print('SATURATION_RETURN',r,flush=True)
print('POINTS',MW.points(),flush=True)
print('SATURATION_DONE',flush=True)
