# Seed BSD: a source-lift experiment, not another receiver run

Date: 6 October 2026.
Status: **EXPLICIT_LOCAL_COEFFICIENT_CONSTRUCTION_AND_TESTED_EXPERIMENT_DESIGN**.

## The proposed change

Use one finite jet of the actual ordinary family symbol through the seed to obtain the four W3 source values. Do not construct two higher-weight eigensymbols as unrelated external inputs, and do not work on the BFR receiver again.

The supplied code constructs a ten-slot, mixed-precision quotient of an integral measure module and its semigroup action. A written proof is in `FINITE_MOMENT_MODULE.md`. The quotient retains exactly the precision needed by the four existing W3 functionals. The new research task is to lift the **actual seed eigensymbol** into this quotient, using the inhomogeneous Manin/Hecke equations and a sparse dual certificate. `SOURCE_LIFT_EXPERIMENT.md` specifies those equations and their arithmetic obligations.

**What has been obtained here:** an explicit local coefficient object, its action and precision proof, an extraction identity under a named source comparison, working standard-library Python, and 2,671 exact local/control assertions. This is a construction component, not an independently reviewed theorem or a Hida-source computation.

**What has not been obtained:** a global seed family symbol, even one genuine seed W3 value, a seed-specific sparse dual certificate, a new primary certificate, an affordable complete seed evaluator, or a uniform bound. FIN, ORDER9 and Q36 have not changed. No Aristotle job was submitted. No GitHub files were changed.

## Why this targets a live gap

The current lab record already has an integral W3 source/index route: on its retained ordinary domain, one genuine source value nonzero modulo p^4 gives an index at most three and then primary vanishing. Its October 5 experiment was stopped because no genuine seed-source constructor was supplied. The extractor merely consumed higher-weight symbol arrays.

This package supplies more than another extractor: the action on the coefficient module and a concrete lifting system that could produce those arrays directly from a seed-family source. The global lifting step remains research, not a disguised input that the code has computed.

Twenty base-p digits are retained **per divisor value**. This does not make the entire global symbol problem twenty-dimensional. The conductor is still enormous, and a short dual certificate might not exist.

## Start

Read `ARISTOTLE_TASK.md`, followed by `FINITE_MOMENT_MODULE.md` and `SOURCE_LIFT_EXPERIMENT.md`. Run:

```bash
python3 verify_package.py
python3 test_jet_module.py
```

The tests deliberately include arrays that are only local Dirac-measure assignments. They do not satisfy global modular-symbol relations. Their nonzero values are not seed evidence.

The package is an experiment supplement to the existing Aristotle research input, not a new service-specific upload wrapper. Import the named retained W3 documents from the existing reading set or the pinned private GitHub paths in `SOURCES.json`. Do not substitute this synopsis for their proofs.

## Pilot

Use p=31 for the first new source-construction attempt, not a prime sweep. Direct counting gives #E(F_31)=40 and a_31=-8. The ordinary unit root is 57776 modulo 31^4=923521. These local computations do not establish membership in the retained Hida exceptional domain.

Use p=17 only as a normalization/control comparison against the existing research data. Existing certificates must not be advertised as new primary progress. The p=31 choice does not assert that its primary component is unproved elsewhere in the archive.

## Endpoint discipline

A genuine source value, even zero, would remove an implementation uncertainty and give arithmetic data for testing identities. A genuine nonzero value in the theorem domain would give a pointwise primary bound. A proof of a nonzero value for all ordinary primes outside an explicitly described fixed finite set would give ordinary cofinite control. Supersingular primes and exceptional components would still need their own arguments. Q36 remains a separate obligation.

The objective of the next run is a **seed-specific forcing identity or bound** from the lifting equations, not merely a successful replay of the local module supplied here.
