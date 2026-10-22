# Across-prime generating-presentation test

Before computation. On the actual seed and p=5,7,11,13, enumerate Frobenius orbits on nonzero p-torsion vectors for rational good primes q<=2000 with q!=p. Use exact seed point counts and finite-field group invariants to resolve identity-versus-unipotent ambiguity when trace2, determinant1 modp. Count C_(p-1) free orbits of prime ideals with norm<=2000; these and only these contribute to a faithful scalar character.

This is an exact finite generator-demand calculation, not a class-group computation. It measures the columns a relative relation method must address at a common cutoff. It does not assume a prime cutoff generates classgroups, and does not supply an upper bound on classes. Excluded ramified places are listed.

Predicted interpretation: if relation production grows only by isolated selected rows while these columns grow, the tested implementation does not support small complete bounds. A positive output requires actual relation rank plus certified generation; orbit counts alone are insufficient.
