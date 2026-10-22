# Final balanced relation-base gate

The accepted streaming count reproduces the producer's KC=721 and KCZ=175
at C1=4813. It gives these exact dimensions:

| c1 | C1 | KC | KCZ | Dense-cache entries, bytes |
|---|---:|---:|---:|---:|
| 0.02 | 4813 | 721 | 175 | 4,158,728 |
| 0.05 | 12034 | 1653 | 383 | 21,859,272 |
| 0.1 | 24068 | 2821 | 660 | 63,664,328 |
| 0.2 | 48136 | 5077 | 1199 | 206,207,432 |
| default | 419775 | 35749 | 8507 | 10,223,928,008 |

All use the unchanged C2 norm cutoff 419775. The count does not construct
class-group relations or make a completeness claim.

The smallest relation base gave no new columns under either small-norm or
random relation production during the bounded gates. A larger base accepts
more possible smooth ideal factorizations, while its measured dense-cache
cost remains below 256MB. The final parameter gate is therefore the
unmodified documented `bnfinit(NF,1,[0.2,0,-1])`, with a 2GB stack,
177-second internal alarm, and 180-second process-group wall cap.

This is the last parameter gate in this return. It will not be extended if
it produces no relation growth. Completion is accepted only with the explicit
marker and saved BNF, still subject to separate unconditional certification.
