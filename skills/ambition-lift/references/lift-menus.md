# Lift menus and worked examples

Everything here is this skill's translation of Rieseberg's moves into the work this user does. Only text marked *Article* comes from the article (checked against `source-notes.md`). The menus suggest; the project's rules from step 1 of SKILL.md decide what is usable, so drop any item they rule out and report it as blocked. Tool names are starting points: confirm a tool exists and does what you need before relying on it.

Contents: §1 the review ladder, transposed · §2 menus by kind of work · §3 stretch targets in practice · §4 worked examples · §5 a lifted prompt

## §1 The review ladder, transposed

| *Article* (Acme Inc quarterly business review) | Research version (group meeting, weekly update, progress report) |
|---|---|
| Give the model as much data as you can get; "Tell me what changed this quarter, why, and what we should do about it." | All run logs, configs and commits since the last update, not the numbers already pasted into slides: what changed, why, and what to do next. |
| "Work out which three decisions are most urgent in the face of everything you've learned, and start working on potential directions with for/against arguments." | The three most urgent decisions (which run to stop, which result to trust, which claim to drop), each with for and against. Whether the whole project should continue or pivot goes to `altitude-check`. |
| "The review exists so leadership catches problems early and moves money and people to the right places. Design a better way to do that than a quarterly deck, show from our own history that it would have caught things sooner, and run it beside the current one for a quarter." | The meeting exists so problems surface early and GPU time and effort move to what matters. Propose a better mechanism (say, regression alerts over every run, or a standing results table the PI can query), backtest it on the project's history (would it have flagged the known failures sooner?), and run it beside the slides for a few weeks. A proposal until the user agrees. |
| Fix individual crashes -> "keep our apps crash-free", which needed fetchable crash reports, a version-to-commit map, and machines to reproduce and verify fixes. | Fix this run -> keep the pipeline green, which needs results tied to commit, config and seed, machine-readable metrics, logs fetchable from the GPU box, and a scorer and regression set an agent can run. |

## §2 Menus by kind of work

Each menu: **Beyond** (the goal beyond the goal) · **Raw** (rawest material, if permitted) · **Instruments** · **Range** (the verb sentence and fields it suggests) · **Judges** · **Red team** (actions, not voices) · **Traps**.

### Code: speed
- **Beyond**: who waits on this, and why? Removing the wait (caching, batching, not recomputing) can beat speeding it up.
- **Raw**: production-size inputs and real traces, not toy inputs.
- **Instruments**: a profiler before any change (py-spy, cProfile, perf; Nsight Systems for GPU work), a bandwidth or roofline estimate, vectorised or compiled kernels.
- **Range**: HPC (data layout), databases (indexes, query plans), compilers.
- **Judges**: a benchmark on fixed inputs plus an output-equality check against the old code.
- **Traps**: benchmarking on warm caches or toy sizes; changing outputs while chasing speed.

### Code: a bug
- **Beyond**: the class of bug and keeping it away (the article's move from fixing crashes to keeping apps crash-free).
- **Raw**: the actual stack trace, core dump or failing input, not the report's paraphrase.
- **Instruments**: a minimal reproduction, `git bisect`, sanitizers, property-based tests, fuzzing.
- **Range**: SRE postmortems (contributing factors rather than one root cause), formal methods (state the invariant the bug broke).
- **Judges**: a test that fails before the fix and passes after, plus the existing suite.

### ML experiments, training runs and benchmarks
- **Beyond**: what decision the run informs (which method goes in the paper, which model is submitted) and what result would change it.
- **Raw**: per-example predictions, per-seed training curves, full logs (including stderr and scheduler logs), configs with the git hash.
- **Instruments**: runs in a queryable table (SQLite or DuckDB) rather than a markdown table; several seeds with intervals; paired bootstrap or paired tests across seeds and examples; ablations; equal tuning budgets for baselines; compute-matched comparisons; duplicate and contamination checks between train and test; for failures, a failure taxonomy from the raw logs and a model of failure against config (for example a logistic regression or a small tree over hyperparameters).
- **Range**: "deciding which method to trust under noise and a fixed compute budget" -> statistics, measurement science, experimental design; clinical trials (fix the analysis plan before looking at outcomes); SRE (incident review of failed runs).
- **Judges**: a test split touched once, at the end; an independent reimplementation; the benchmark's own evaluation code; a rerun that reproduces a diagnosed failure and a fix that removes it.
- **Red team**: rerun the best and worst seeds; tune the strongest baseline as hard as the method; ask whether the gain is inside seed noise.
- **Traps**: reporting the best seed; quiet repeated looks at the test split.

### Protein design (binders, inverse folding, design loops)
- **Beyond**: how many designs will work in the lab, and which experiment will tell.
- **Raw**: every design with its per-residue and interface metrics and its trajectory, failures and filtered-out designs included.
- **Instruments**: refolding with a structure predictor that was not in the design loop; interface metrics (for example ipAE, interface pLDDT) and energetics and shape complementarity (for example Rosetta); sequence-identity clustering (for example MMseqs2) so near-duplicates neither inflate counts nor leak across splits; ROC and calibration of each in-silico metric against assay outcomes, with intervals, on the designs that were tested.
- **Range**: "betting a handful of expensive assay slots on the designs most likely to bind" -> portfolio thinking (spread bets across clusters and epitopes), experimental design, developability from biologics engineering (expression, aggregation, stability), statistics (winner's curse when picking top-scoring designs).
- **Judges**: binding assays or other wet-lab results where they exist, ideally on designs chosen before the analysis; an orthogonal predictor. A loop that optimises against one model's confidence and then filters on that same model is grading itself.
- **Red team**: ask which in-silico metric has ever predicted binding for targets like this one, and test it on whatever assay data exists.
- **Traps**: judging a pipeline by its survivors (filtered-out designs were never tested, so a filter's precision is visible but its recall is not); small n; homology leakage between train and test.

### Single-cell and embryo modelling
- **Beyond**: which claim the analysis will support, and who has to believe it.
- **Raw**: raw counts with per-cell metadata (embryo, donor, batch, stage, condition), not shipped cluster labels or a processed embedding.
- **Instruments**: MAD-based QC (`bio-research:single-cell-rna-qc`); batch integration (`bio-research:scvi-tools`); pseudobulk per embryo or donor for differential expression, because cells from one embryo are not independent replicates; differential-abundance tests with replicates (for example Milo or scCODA); cluster stability across seeds and resolutions; simple baselines (control mean, additive effects, linear models) in any perturbation-prediction comparison.
- **Range**: "predicting how a developing system responds to a perturbation it has not seen" -> developmental biology (lineage structure as a prior), dynamical systems, causal inference, forecasting (backtesting, proper scoring rules).
- **Judges**: embryos, donors, stages or perturbations held out by a split fixed before looking, from data you may use; marker genes checked against retrieved literature; the official scorer where there is one, within its submission limits.
- **Red team**: test whether a "new" cell state is a doublet, a batch effect, or a mix of stages.
- **Traps**: splitting by cell instead of by embryo or donor; anything derived from hidden targets.

### ML security
- **Beyond**: the security claim the paper will make, and the attacker it has to survive.
- **Raw**: per-example attack outcomes, logits and transcripts, not only aggregate success rates.
- **Instruments**: a stated threat model; adaptive attacks written against the specific defence; standard strong evaluations (for example AutoAttack for norm-bounded robustness); TPR at low FPR for membership inference; seeds and intervals; matched attack budgets.
- **Range**: "predicting what a motivated adversary with a stated budget will do" -> security engineering (threat modelling), cryptography (assume the attacker knows the system), game theory, auditing.
- **Judges**: an attack implementation not written alongside the defence; released benchmarks and their evaluation code.
- **Traps**: gradient masking passing for robustness; attacks tuned on the evaluation set.

### Papers, proposals and rebuttals
- **Beyond**: what the reader should believe and do afterwards (accept, fund, adopt, cite). Framing goes to `paper-axis-check`; scoop risk to `field-timing-scan`.
- **Raw**: the result files and logs, not numbers copied from an older draft.
- **Instruments**: a claim-to-evidence map; trace every number to a log, commit or script output (the forensic accountant's job); retrieve every citation (`zetesis:evidence-check`, PubMed, Consensus) rather than recalling it; build the paper and check the bibliography.
- **Range**: an editor cuts what doesn't serve the claim; a statistician checks every comparison; `dataviz` for figures; a hostile reviewer from the neighbouring subfield writes the three strongest objections and the experiment that answers each.
- **Judges**: the build, the traced numbers, a colleague's read.
- **Traps**: "first" or "state of the art" claims not checked against the literature.

### Talks, posters, slides and group meetings
- **Beyond**: for a group meeting, the decisions it should produce (see §1); for a talk or poster, what the audience should believe, remember and do afterwards (talk to you, try the method, cite it).
- **Range**: "getting a room of specialists from other subfields to believe one causal claim and remember it twenty minutes later" (a poster: "getting experts walking past to stop, grasp one claim in under a minute, and start a conversation"). A journalist writes the one-sentence story and headline; an editor cuts every element that doesn't serve it; a designer sets one visual hierarchy and reading path; a motion designer animates the one mechanism that is hard to say; a hostile questioner writes the three hardest questions, with backup material.
- **Judges**: a timed rehearsal; a cold reader (a colleague, not the model) who restates the claim after a fixed time; for a poster, a print at full size read from two metres.
- **Tools**: prose with `no-ai-slop`, charts with `dataviz`.
- **Traps**: altitude fits creative and presentational work less well (*Article*: it "works less well for creative endeavors"), so lean on depth and range here.

### Pipelines and GPU jobs
- **Beyond**: "fix this crash" -> "keep the runs green"; "launch this sweep" -> "spend the GPU budget on the most informative runs", which is a delegation the user grants explicitly, with a budget and a stop rule.
- **Plumbing**: every run writes config, commit, seed and metrics in machine-readable form; logs fetchable from the GPU box; a regression set with known-good outputs; launching and checking per `dgx-first`.
- **Judges**: the regression set and the scorer, not the agent's account of the run.
- **Traps**: stopping or restarting the user's jobs, or filling shared disks; ask first.

### Literature questions
- **Beyond**: which decision the answer feeds.
- **Raw**: primary papers and their data, not reviews or abstracts.
- **Instruments**: logged queries, inclusion criteria, retraction and correction checks.
- **Judges**: `zetesis:evidence-check` with retrieved identifiers. For a full report, `deep-research`.

### Competitions and pre-registered work
- **Off-limits, typically**: hidden targets and anything derived from them (leaderboard internals, organiser-only files, posts or papers that report held-out values, probing the scorer); external data the rules exclude; material a required screening step has not cleared.
- **Depth inside the rules**: internal splits that mirror the hidden split's structure (group by embryo, donor or time, not by cell or row); ablations and uncertainty estimates on those; robustness to the choices the rules leave open.
- **Altitude inside the rules**: the outcome is a defensible submission, so draft decision rules and a plain summary for the user's sign-off before the data that triggers them arrives, rather than choosing afterwards.
- **Reporting**: internal validation numbers are labelled internal, never presented as test performance.

### Recurring chores and tooling
- **Beyond**: make the recurring task unnecessary - "keep X true" rather than "fix X again".
- **Instruments**: the enabling access the article lists for its crash-free example, generalised: fetch the raw signal automatically, map versions to commits, reproduce in the real environment.
- **Judges**: the signal itself, over time.
- Standing automation is ask-first; see `scope-calls.md`.

## §3 Stretch targets in practice

- Write the target down before starting, as a number with its judge and a stop condition: "AUROC 0.85 on held-out embryos (split fixed today), scored by the evaluation script; stop after three approaches or 20 GPU-hours". The article cites Locke and Latham's finding that people given specific hard goals do better than those told to try their best; that is about people, and using it for targets is this skill's extrapolation.
- If the user doubts the target, look for an existence proof: a retrieved result where someone reached something comparable on an adjacent problem. The article's four-minute-mile story is about people believing after watching someone else; using it for target-setting is this skill's.
- Treat each attempt as a bounded experiment, so a miss is cheap and gets reported rather than hidden (the article's permission to fail, again about people).
- Every look at an evaluation set while choosing methods leaks a little of it into the choices. Tune on a development split, count the looks in the report, and give the final split one look; its number is the one you report.

## §4 Worked examples

**A. "Compare our three binder-design variants in a table."**
- Lift: depth; outcome: decide which variant earns the next design budget.
- Rules: only the compute policy applies.
- Do now: a per-design table from existing outputs instead of top-k means; bootstrap intervals; collapse near-duplicate sequences before counting.
- Ask first: orthogonal refolding of every design (state the GPU-hours on the DGX); calibrating the in-silico filters against any wet-lab results.
- Judge: the orthogonal predictor now, the assay later.

**B. "Write my group-meeting update from this week's runs."**
- Lift: altitude (there will be a meeting, the article's tell).
- Do now: the update from the run logs themselves: what changed, why, what next; the three most urgent decisions with for and against.
- Ask first: a regression-alert report backtested on the last two months of runs and run beside the update.
- Ask first: before posting it to Slack or emailing anyone.

**C. "Push our challenge score up."**
- Rules first: hidden targets, excluded external data, a screening route, and a person who picks submissions.
- Do now: an internal split that mirrors the hidden one; ablations; uncertainty on the internal numbers.
- Ask first: a new model family, with its GPU cost.
- Blocked: anything derived from the hidden targets, named with the rule that bans it, plus the approval route if the rules give one.
- Reserved: the pick itself, via a plain summary of the decision rule before the deciding data arrives.

**D. "Make the defence section of the paper stronger."**
- Range: "convince a sceptical security reviewer that no attacker inside the threat model breaks this". Crew actions: write an adaptive attack against this defence; put intervals on every number, and TPR at low FPR where relevant; trace each number to a run.
- Judge: an attack implementation not written alongside the defence.
- Ask first: before posting a revision to arXiv or OpenReview.

## §5 A lifted prompt

Original: "Cluster the embryo cells and tell me which clusters change between conditions."

- (0) Rules: what the project's `CLAUDE.md` and data policy say about this dataset; any screened routes; who decides the primary comparison.
- (1) A top lab would QC first, integrate batches, treat embryos rather than cells as replicates, check that clusters are stable, and fix the primary comparison before looking.
- (2) Rawest permitted material: the raw count matrix and per-cell metadata, not the shipped cluster labels.
- (3) Instruments: MAD-based QC, scVI integration, clustering at several resolutions and seeds, a differential-abundance test with embryos as replicates, and pseudobulk DE per embryo for clusters that change.
- (4) Judge: stability across seeds and resolutions, a held-out replicate embryo, and marker genes checked against retrieved literature.
- (5) Sign-off: the primary comparison, before any results are seen.

Rewritten:

```text
Read <project>/CLAUDE.md and <data policy> first and stay within them: don't open <off-limits paths>, and use only <permitted data>.
Outcome: a list of clusters whose abundance changes between conditions that would survive review, with the genes that define them.
From the raw count matrix and per-cell metadata, run MAD-based QC, integrate batches with scVI, and cluster at three resolutions across three seeds; keep only stable clusters.
Before any testing, write down the primary comparison and stop so I can confirm it.
Then test differential abundance with embryos as replicates (Milo or scCODA) and run pseudobulk DE per embryo for clusters that change.
Judge: stability across seeds and resolutions, and a held-out replicate embryo; check marker genes against retrieved literature, with identifiers.
Hand back: effect sizes with intervals, which clusters are stable, and what you could not check. Run heavy compute on the DGX. Don't post, email, push or delete anything.
```
