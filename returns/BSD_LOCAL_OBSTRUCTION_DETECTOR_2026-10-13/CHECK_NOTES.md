# Execution and limitations

The final standard-library checker completes in approximately one second in this runtime. Two fresh successful executions are compared byte-for-byte before sealing the package. No PARI, Sage, Magma, paid service or original large coefficient corpus is used.

During development, the first checker stalled in an auxiliary finite-field polynomial remainder routine: its subtraction lacked the degree offset. Timeout runs produced no accepted RESULTS.json. A stack trace located this defect. The offset was repaired, and the routine now also asserts that each remainder step strictly decreases degree. Only the subsequent completed checks are reported as passing.

The arithmetic used for the local signature precedes the auxiliary polynomial test and is separately specified by exact formulas in PROOF.md. The final full run checks both. No exit code or empty output from a timeout is treated as a mathematical result.

The 125 relation checks evaluate actual products epsilon^a alpha11^b f(P1)^(-c) in Q(sqrt(43737)) and extract certified local leading terms. A precision countercontrol rejects an alpha11 approximation too short to establish its leading unit. The uniform argument in the proof, not extrapolation from the count of checks, proves independence.

The five Pfaffians and their syzygies are recomputed. Hensel witnesses at 5 and 11 are checked with a chosen nonzero three-by-three minor and a complementary matrix unit. This does not replace the source theorem proving local solubility at all places. Global Groebner smoothness, original class/unit certification, rank descent and saturation were not rerun.

The splitting-field result does not provide coordinates of a point on the projective curve. It proves triviality of the corresponding isogeny-covering class after field extension. Period and index statements are consequences for the control, not seed finiteness claims.
