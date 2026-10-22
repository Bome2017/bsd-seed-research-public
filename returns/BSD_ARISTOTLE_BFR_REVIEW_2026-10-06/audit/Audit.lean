import RequestProject.Seed.BadPrimes
import RequestProject.Seed.Local4547

-- Independent strengthening of the submitted finite computation only.
-- This is not a formalization of the Kummer, Neron-model or BFR argument.
namespace Audit
open Seed.Local
def residue1274Cert : Bool :=
  let A := Apm1
  ((sb A.X (ml xP A.Z)) % (p*p)) == p * ((1274 * (A.Z % p)) % p)
set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
theorem residue1274Cert_true : residue1274Cert = true := by
  decide +kernel
end Audit

#print axioms Seed.translate_curve_eq_orig
#print axioms Seed.curve_Δ
#print axioms Seed.curve_c₄
#print axioms Seed.disc_factorization
#print axioms Seed.bad_primes_prime
#print axioms Seed.P1_nonsingular
#print axioms Seed.P2_nonsingular
#print axioms Seed.T_nonsingular
#print axioms Seed.T_addOrderOf
#print axioms Seed.orig_points
#print axioms Seed.Rp_nonsingular
#print axioms Seed.dp_neg
#print axioms Seed.dp_not_sq
#print axioms Seed.dp_modEq_one
#print axioms Seed.dp_not_dvd
#print axioms Seed.dp_mul_p_not_sq
#print axioms Seed.exists_sqrt_dp_padic
#print axioms Seed.Rp_padic
#print axioms Seed.Local.index_coprime
#print axioms Seed.Local.reduction_quotient_factorizations
#print axioms Seed.Local.chainCert_true
#print axioms Seed.Rp_padic_2243
#print axioms Seed.Rp_padic_4547
#print axioms Seed.Rp_padic_5843
#print axioms Seed.five_not_dvd_disc
#print axioms Seed.card_affine_F5
#print axioms Audit.residue1274Cert_true
