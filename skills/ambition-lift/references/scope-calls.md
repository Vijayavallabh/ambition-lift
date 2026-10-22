# Scope calls

Defaults for lifts whose bucket isn't obvious from step 3 of SKILL.md. All of this is this skill's guidance, not the article's. A project's own rules override these in both directions: a project may pre-approve something listed here as ask-first ("launch DGX jobs on up to 4 GPUs without asking"), or forbid something listed as do-now. When the project is silent and you still can't tell, ask; one message is cheap.

| Lift | Default | Details |
|---|---|---|
| Read more of the project: other modules, logs, results, git history | Do now | Blocked if a rule fences the file or folder (answer keys, hidden labels, quarantined or unscreened outputs). Don't open a fenced file to see what is in it, and find rule files by name, not by grepping contents. |
| Add a judge: tests, a benchmark, a frozen held-out split, a reference implementation | Do now | Throwaway judges go in the scratchpad; tests the project would keep go beside the code. Ask if it changes the official evaluation, shared CI, or a pre-registered split. |
| Use a public leaderboard or an external evaluation server as the judge | Ask first | Submissions are seen by others and often rationed, and tuning against a leaderboard overfits it. Blocked where the project fences leaderboard files or limits submissions. Prefer a local frozen split. |
| A stronger method for the same deliverable (statistical model, profiler, seeds and intervals, a tuned baseline) | Do now | Ask if it changes what a reported number means (another metric, another test set). |
| Notes, logs or memos in the project | Do now if they belong to the deliverable, marked as drafted by the assistant | Ask if they go into a shared or official record (lab notebook, decision log, a rules file, anything others sign). Add an approval line only after the user approves. |
| Edits outside the files the task touches (broad refactors, other modules, shared configs) | Ask first | Do now only if the task can't work without it and the change is mechanical; say so in the report. |
| Change the goal, metric, success criterion or analysis plan | Ask first | Blocked if the plan is pre-registered or the choice is reserved for a person. |
| Replace an existing pipeline, process or tool | Ask first | Offer instead: a comparison on the project's own history, then a run beside the current one. |
| Compute within the task's evident budget, locally or on the DGX via `dgx-first` | Do now | Ask when the run is far beyond what the request implies (hours of multi-GPU time for a small task), when the GPUs are busy with other people's jobs, or for writes over ~50 GB (dgx-first's threshold). |
| Install packages into the project's own environment | Do now, after checking what is already installed (the project's env, the user's other venvs or conda envs) | A small install into a throwaway env in the scratchpad is fine; say so in the report. Ask for system packages, shared base environments, large downloads, or when the project pins its environment for reproducibility. |
| One to three subagents for range or red-teaming, each with a procedure and an output | Do now | Ask for a large fan-out or a multi-agent workflow the user hasn't opted into. Always pass them the project's rules. |
| Read-only lookups: web search, PubMed, bioRxiv, Consensus, ChEMBL, `zetesis:evidence-check` | Do now | Blocked if the project bans external data, or data from certain dates. If retrieved material must be screened before you read it, route it through that step and read the screened result. |
| Download public datasets or model weights | Do now if small and the data policy allows it | Ask if large, if the licence or policy is unclear, or if the data could overlap an evaluation set or an excluded window. |
| Git commits, branches, stashes | Ask first, unless the user already has you committing in this session | Keep the baseline as a copy in the scratchpad instead of a commit. |
| Read the user's mail, Slack, calendar or Drive for raw material | Ask first | Personal and third-party content; the user decides what is in scope, and some threads may be quarantined by project rules. |
| Send, post, comment, open a PR or issue, push to a shared remote, submit, share an artifact with others | Ask first, every time, naming the exact action | Other people see it and it can't be unsent. General encouragement doesn't cover it. |
| Delete, overwrite or move data or results; rewrite git history; kill or restart jobs | Ask first | Hard or impossible to undo. |
| Standing automation: cron, `/loop`, `/schedule`, hooks, CI jobs, watchers | Ask first | It keeps acting after the conversation ends; taking the human out of a loop is the user's call. |
| Write to `CLAUDE.md`, memory or settings | Ask first | It changes every future session. |
| A decision the user or project reserved (choose between pre-registered options, accept or submit a result, change a decision rule) | Blocked as a decision | Prepare it instead: plain summary, options, evidence, recommendation, in time for any sign-off deadline. Where a rule says certain data waits for sign-off, the sign-off comes before the data. |
| Open fenced files or data, skip a screening step, use data from a banned window, look at hidden labels, probe a scorer | Blocked | Not a deeper version of the work; it invalidates the work. If it happened by accident: stop, tell the user at once, log it where the project records exposures. |
| Edit a test, benchmark or scorer so the work passes; tune on evaluation data | Never | It moves the judge, and the result stops meaning anything. |

## What a go-ahead covers

- The action approved, at the size approved. A yes to one item is not a yes to the others; if the action grows materially (more data, more runs, a wider audience), ask again.
- General encouragement ("be as ambitious as you like", "go wild") widens effort and internal cost. It doesn't approve a specific outward-facing or irreversible action, and it never lifts a project rule or a reserved decision; those change only when the user changes the rule itself.
- If nobody can answer (headless runs, scheduled jobs), ask-first items stay proposals in the report.
