# Seed structure experiment

Start with [REPORT.md](REPORT.md). The outcome is an actual seed unit carrying
known excess, plus a conditional one-unit/one-class filtration. It is not a
new primary-vanishing certificate or a uniform bound.

Run `python3 verify_return.py` for hashes, acceptance checks and independent
matrix reconstruction. Run `python3 verify_return.py --gp /path/to/gp` to
repeat the portable positive unit certificate. That replay reconstructs the
number field and actual class images, then checks every compact-factor ideal
valuation. It does not require the large historical bnf cache.

The original exact cover certificate is included in inputs/ and can be run
with `gp -q -D parisizemax=4000000000 -f inputs/verify_certificate.gp`.
Its saved replay is checks/cover_replay.out. Its rank and covering-theorem
inputs retain their recorded grade.

The full discovery producer in seed3/probe.gp reads the two external caches
named and hashed in seed3/RUN_BINDINGS.json. They are not included. Rebuilding
them is expensive and unnecessary for the positive unit replay. Their GRH
class-group completeness is not promoted by this package.

Directories named rejected_trial* contain failed implementation attempts.
Their markers and intermediate files are not accepted arithmetic results.
Only the clean producer, independently checked matrix export and portable
certificate are used in the report.
