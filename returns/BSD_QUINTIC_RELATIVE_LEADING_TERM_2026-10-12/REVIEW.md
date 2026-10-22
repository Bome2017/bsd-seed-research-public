# Review priorities and failure controls

This is the author's review checklist, not independent acceptance.

1. **Real period:** The raw table uses omega_1; the seed has Omega_E=2 omega_1. Divide each character sum by two. F has five real places. Do not mix primitive-cycle and full-real-period conventions.
2. **Character orientation:** chi(6)=zeta_5 and chi is trivial on {1,7,18,24}. In the positive Fourier-antiderivative convention, sum chi(a)lambda(a/25)=tau(chi)L(E,chi^{-1},1). Reversing all paths changes a global sign only; conjugating chi permutes the four factors.
3. **Exact norm versus a recognized decimal:** The norm 52128400 is evaluated in an exact cyclotomic ring and by a multiplication matrix. No bounded-denominator rational recognition is used here. The *input* symbols still retain their original certified reconstruction dependencies.
4. **Discriminant:** The field has discriminant 5^8; the displayed polynomial has discriminant 7^2*5^8. Its power basis is not a full integral basis. Inserting an extra factor 7 is an explicit failing control.
5. **Regulator:** The height in the number-field formula is relative, so it scales by 5. Rank two gives a factor 25. The full point equality rules out an index-square correction. Rank equality by itself would not do so.
6. **Bad local terms:** The split primes are 2243 and 5843. The factor at 5843 occurs five times, not once. The additive place 2 is unramified of residue degree five, and its component fixed group is unchanged. Differential minimality is checked separately.
7. **No hidden BSD assumption:** A_K is a defined real leading-term expression. A_F=19^4 A_Q is proved as an equality of such expressions; neither separate rationality nor equality with Sha is assumed.
8. **No automatic 19-primary theorem:** The character numerator has a factor 19 at each prime above 19, but no Selmer comparison proving the corresponding actual Sha size has been supplied. A conjectural Artin-twist ideal formula is not a substitute.
9. **No base-field bound from a relative identity:** Original ell-primary classes, ell != 5, survive restriction to F. The relative identity does not prove FIN, ORDER9, or Q36.

The executable checker tests the exact algebra and explicit factors. The project arithmetic inputs and number-field structural theorems remain part of the written proof's retained trust base. All new conclusions require independent mathematical review before promotion.
