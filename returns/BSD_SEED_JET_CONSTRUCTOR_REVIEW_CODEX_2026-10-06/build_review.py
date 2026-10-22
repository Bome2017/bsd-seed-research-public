from pathlib import Path
import json,hashlib,subprocess,zipfile,tarfile,io,shutil
base=Path(__file__).parent
repo=Path('/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab')
ref='203219857f29631dc56455b0543870a347a25d5e'
project=base/'reviewed_supplement/BSD_SEED_JET_CONSTRUCTOR_REVIEWED_2026-10-06'
project.mkdir(parents=True,exist_ok=True)
zinput=Path('/Users/bsm/Downloads/BSD_SEED_JET_CONSTRUCTOR_2026-10-06.zip')
with zipfile.ZipFile(zinput) as z:
 for info in z.infolist():
  rel=Path(info.filename).relative_to('BSD_SEED_JET_CONSTRUCTOR_2026-10-06')
  dest=project/'original'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(info))
folders=['BSD_W3_FOUR_VALUE_RETURN_CODEX_2026-10-04','BSD_W3_COHOMOLOGICAL_JET_RETURN_CODEX_2026-10-04','BSD_W3_GLOBAL_PERIOD_RETURN_CODEX_2026-10-04','BSD_WEIGHT3_LOCAL_INDEX_RETURN_CODEX_2026-10-04','BSD_W3_DISCOVERY_ADMISSION_CODEX_2026-10-05']
paths=['work/returns/'+f for f in folders]
raw=subprocess.check_output(['git','archive','--format=tar',ref,*paths],cwd=repo)
bindings=[]
with tarfile.open(fileobj=io.BytesIO(raw)) as t:
 for m in t.getmembers():
  if m.isdir():continue
  assert m.isfile()
  rel=Path(m.name).relative_to('work/returns')
  data=t.extractfile(m).read();dest=project/'retained'/rel
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  bindings.append({'path':dest.relative_to(project).as_posix(),'source_path':m.name,'sha256':hashlib.sha256(data).hexdigest()})
for name,path in [
 ('03_WALL_ATLAS.md','work/returns/BSD_SEED_ARISTOTLE_2026-10-05/guide/03_WALL_ATLAS.md'),
 ('P17_RETAINED_RECEIPT.json','work/returns/BSD_GLOBAL_BIEXTENSION_RETURN_CODEX_2026-10-05/context/P17_RETAINED_RECEIPT.json'),
 ('P17_MSL.txt','work/returns/BSD_GLOBAL_BIEXTENSION_RETURN_CODEX_2026-10-05/context/P17_MSL.txt')]:
 data=subprocess.check_output(['git','show',f'{ref}:{path}'],cwd=repo)
 dest=project/'retained'/name;dest.write_bytes(data)
 bindings.append({'path':dest.relative_to(project).as_posix(),'source_path':path,'sha256':hashlib.sha256(data).hexdigest()})
(project/'RETAINED_BINDINGS.json').write_text(json.dumps({'repository':'Bome2017/bsd-seed-lab','commit':ref,'files':bindings},indent=2)+'\n')
report='''# Third Aristotle package: review and recommendation

6 October 2026. **USE_AS_A_DISTINCT_SOURCE_CONSTRUCTION_EXPERIMENT_WITH_CONTEXT_AND_SCOPE_ADDENDUM.**

Yes: this is a reasonable third research assignment. Its concrete operation differs from the pasted relative-class/transgression assignment. It attempts the missing actual W3 source lift, rather than asking for a bound on the class-group receiver. The broad continuation could independently choose W3; this review has not inspected either running job and does not claim guaranteed non-overlap in their live work.

## What was checked

The submitted ZIP is intact, and all 17 manifest entries verify. The supplied 2,671 assertions reproduce exactly. An additional 96 controls compare the implemented coefficient action with a separate rational logarithm-series and Mobius evaluation. Eight lab source references match their pinned commit and their declared digests where supplied. These are local algorithm/custody checks, not seed W3 values.

I read the local proof and reconstructed its precision argument. I found no blocking error in the ten-slot local measure quotient, its semigroup action, or its conditional factorization of the four functionals. The coefficient of degree n in the logarithmic chart has valuation at least n-1-v_p(n); terms beyond degree three are harmless at the stated fourth-order precision. After binomial expansion the coefficient from input degree r+n to output degree i+j has the required valuation at least max(0,r+n-i-j). This is what makes mixed-precision descent work. The determinant 24 establishes local interpolation/surjectivity only. It is not a bound on a global eigensymbol.

The signs, p-powers and binomial factors in formula (F) agree algebraically with the pinned ARITHMETIC_EXTRACTION.md on substituting c_h=(-1)^h binom(w,h)M_h. Omitting the ordinary unit alpha_w preserves valuations but not a common numerical frame. The source identification, integral branch control and resulting Selmer/index implication retain their recorded conditional and independent-review grades; this review does not recertify those foundations.

## Why it is admissible research

The previous W3 admission stopped because an extractor consumed genuine higher-weight symbol arrays that had never been produced. This package supplies a concrete local coefficient representation and proposes the actual inhomogeneous Manin/Hecke lift (L_n), including unknown eigenvalue derivatives. Its alternative lambda J=v is an exact dual certificate to evaluate the required functionals without necessarily materializing the whole space. No such seed lift or dual certificate has yet been constructed, and no affordable solver is demonstrated.

A successful source construction would remove an identified implementation/arithmetic-comparison gap. A forcing identity or bound derived from that construction could address ordinary uniformity. Neither success follows from the local determinant, solvability of the linear system, or primitivity of the source. The package states those limits accurately.

The mechanism is explicitly permitted by the retained W28 wall card. It is not a rerun of the failed statistical campaign unless the worker abandons source authentication and returns to synthetic arrays or unrelated pointwise certificates.

## Changes to carry into the run

1. **31 is already covered by the retained small-prime release.** Its purpose here is source construction and comparison, not a new primary component. A value at 31 alone must not receive the label of new seed-primary progress. Preserve a genuine source value even if zero; use its exact forcing expression to investigate p-dependence.
2. **Do not depend on private GitHub access.** The original ZIP contains BFR context but references the actual W3 proofs externally. The reviewed supplement now includes five complete pinned W3 return folders, including the four-point review/derivation as well as the older ten-point index proof. It includes the relevant wall atlas and p=17 controls. Their original bytes and proof grades are preserved. This is focused supplementary context, not a replacement for the complete 5,180-entry research input.
3. **Resolve pilot source/domain issues concretely.** Good ordinarity at 31 is checked; avoidance of the unenumerated Hida exceptional integer is not. Establish the needed local algebra/source comparison or retain the correct algebra and conditional scope. Do not present one scalar finite-quotient eigenvector as an authenticated Hida family by assumption.
4. **Keep the job on global construction.** Replaying or formalizing the supplied local lemma is preparation, not the research output. Before allocating a full level-Np presentation, specify the actual support/dual identity to attempt and its closure checks. A resource failure for that representation is not a theorem against sparse methods.

## Concrete source guidance

Dummit–Hablicsek–Harron–Jain–Pollack–Ross, *Explicit computations of Hida families via overconvergent modular symbols*, Sections 3.4 and 4.4–4.5, contain useful controls: Proposition 3.10 detects ordinary symbols through total measures, Proposition 4.13 proves ordinary control for their particular finite approximation, and Proposition 4.14 gives finite-precision detection. These can guide normalization and lifting checks. They do not automatically prove control for this new triangular ten-slot quotient, or a sparse seed solver. A comparison with their model must retain variable rescaling and integral precision; the paper's restricted-disc coordinate cannot silently replace T by T/p.

Primary source read: https://link.springer.com/article/10.1007/s40993-016-0052-8 (especially Sections 3.4 and 4.4–4.5, plus the family-filtration warning in Section 4.1). The article supplies computation/control methods, not this seed's bound.

## Recommended role and evidence limits

Use the package as a focused third experiment: construct the authenticated source or derive a global lifting/dual-evaluation identity. Then try to control that expression uniformly in ordinary p. Allow useful partial results, but record exactly which missing premise they remove. Supersingular primes, finite exceptions and Q36 remain separate.

No global source was computed in this review. No new BSD theorem, novel-literature claim, runtime guarantee, Aristotle submission or change to either running job is made. The new review and context bundle are ready for the user to supply.
'''
(base/'REPORT.md').write_text(report)
(project/'REVIEW.md').write_text(report)
addendum='''# Scope and use addendum

This supplement is for a separate W3 source-construction experiment. Keep the relative-class/transgression assignment separate. Read original/ARISTOTLE_TASK.md and its proofs, with these clarifications.

- The useful first result is an authenticated source lift, sparse dual evaluation, or new global lifting/forcing theorem. Reproving the local ten-slot module is not sufficient.
- p=31 is a source pilot on an already settled prime. A successful source value is SEED_SOURCE_VALUE_EXACT; it is not new primary vanishing merely because this implementation is new. Continue from its source identity toward control as p varies. No prime sweep.
- Good ordinarity alone does not establish the Hida-domain and source hypotheses at 31. Prove the required source control, or retain the appropriate multi-branch algebra and state what is conditional. Do not silently promote a scalar eigenvector to the optimized integral source.
- Work with the genuine Manin/Hecke operator, unknown eigenvalue derivatives, signed primitive frame, and the original T variable. A sparse certificate must verify every column/tail it omits.
- A small-pilot result is a development tool. Ordinary cofinite nonvanishing, exceptional-primary obligations and Q36 remain distinct. Useful intermediate arithmetic results are welcome; identify which unproved equation they replace.
- DHHJPR Propositions 3.10, 4.13 and 4.14 offer concrete normalization/control tools in their own module. Prove a comparison before using them on this quotient. In particular do not silently divide the weight variable by p.
- Source references in original/SOURCES.json resolve locally through RETAINED_BINDINGS.json. Read the four-point REVIEW.md and original DERIVATION.md, not only the older ten-point VARIABLE_WEIGHT_INDEX.md. Imported grades remain unchanged.
- The complete historical research package should remain available alongside this supplement. This ZIP carries the targeted W3 chain and wall atlas; it does not claim to contain every historical dossier or raw certificate.
- Do not launch other jobs, paid resources, messages or publication from this task. The present package has not been submitted.
'''
(project/'ADDENDUM.md').write_text(addendum)
(project/'TASK.md').write_text('''# W3 source-construction continuation

Read REVIEW.md and ADDENDUM.md, then original/ARISTOTLE_TASK.md, original/FINITE_MOMENT_MODULE.md and original/SOURCE_LIFT_EXPERIMENT.md. Carry out the source-construction experiment with the stated scope. The original proposal is preserved without edits.

Use the existing full BSD research input as historical context. The required targeted W3 dossiers are also provided offline in retained/. These are reference evidence, not active jobs or commands to launch older campaigns. RETAINED_BINDINGS.json gives their exact pinned origins.

Begin with a source-construction attempt for the actual seed at p=31, or a general lifting identity that makes that pilot unnecessary. Work toward an independently controllable arithmetic expression, not another local-module replay. Do not claim a BSD bound from unauthenticated arrays. Treat all finite and cofinite domain conditions explicitly.
''')
(project/'SUBMISSION_PROMPT.txt').write_text('Read root TASK.md and ADDENDUM.md, then carry out the actual seed W3 source-lift/dual-certificate experiment in original/ARISTOTLE_TASK.md using the bundled retained proofs and the existing full BSD research input. p=31 is an already-settled source pilot, not a new primary certificate. Develop the genuine arithmetic construction and its forcing identity; do not spend the run merely formalizing the supplied local module.\n')
(project/'README.md').write_text('''# Reviewed W3 source-construction supplement

This is a focused mathematical supplement, not the complete BSD archive and not a claim of a new seed result. Attach it alongside the full research input in a fresh W3-specific task, or supply it to a session with that input already present. Use SUBMISSION_PROMPT.txt. No job was submitted.

The original 18 ZIP members (17 manifest entries plus manifest) are unchanged in original/. Five W3 return dossiers and three relevant context files are copied from lab commit 203219857f29631dc56455b0543870a347a25d5e into retained/. Their grades are retained. REVIEW.md explains what was checked and why this is a distinct research experiment.

The supplied tests check the local module, not a global eigensymbol. The source and uniform bound remain unconstructed. The review found no blocking defect in the stated local construction. No Lean project or proof of the whole W3 arithmetic chain is supplied here.
''')
(project/'CHECK_RESULTS.json').write_text(json.dumps({'original_manifest_verified':17,'supplied_assertions_reproduced':2671,'independent_action_checks':96,'global_source_evaluated':False,'submitted':False},indent=2)+'\n')
# Verify the nested source manifests, preserve their bytes, then seal the supplement.
verified=[]
for folder in [project/'original']+[project/'retained'/f for f in folders]:
 manifest=folder/'MANIFEST.sha256'
 n=0
 for line in manifest.read_text().splitlines():
  if not line.strip():continue
  digest,name=line.split('  ',1)
  p=folder/name
  assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,(folder,name)
  n+=1
 verified.append({'folder':str(folder.relative_to(project)),'count':n})
(project/'NESTED_MANIFEST_VERIFICATION.json').write_text(json.dumps(verified,indent=2)+'\n')
files=sorted(p for p in project.rglob('*') if p.is_file() and p!=project/'MANIFEST.sha256')
(project/'MANIFEST.sha256').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(project).as_posix()}\n' for p in files))
zout=Path('/Users/bsm/Desktop/BSD_SEED_JET_CONSTRUCTOR_REVIEWED_2026-10-06.zip')
with zipfile.ZipFile(zout,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(project.rglob('*')):
  if p.is_file():z.write(p,Path(project.name)/p.relative_to(project))
with zipfile.ZipFile(zout) as z:assert z.testzip() is None
receipt={'status':'REVIEWED_SUPPLEMENT_PREPARED_NOT_SUBMITTED','zip':str(zout),'bytes':zout.stat().st_size,'sha256':hashlib.sha256(zout.read_bytes()).hexdigest(),'manifest_entries':len(files),'nested_manifests':verified,'source_commit':ref}
(base/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
(base/'STATE.json').write_text(json.dumps({'status':'USE_AS_DISTINCT_SOURCE_CONSTRUCTION_EXPERIMENT_WITH_ADDENDUM','new_seed_result':False,'submitted':False},indent=2)+'\n')
(base/'RESUME.md').write_text('# Completed review\nLocal module reviewed and supplied controls reproduced. See REPORT.md and PACKAGE_RECEIPT.json. Publish review under standing lab instruction; no Aristotle launch.\n')
print(json.dumps(receipt,indent=2))
