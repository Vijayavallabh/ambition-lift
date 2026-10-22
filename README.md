# ambition-lift

A [Claude Code](https://claude.com/claude-code) skill built from Felix Rieseberg's essay
[How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
(13 October 2026). It turns the essay's advice into working habits for Claude, so that when you ask it to think bigger it changes how it works, not just how it talks.

**Credit.** The ideas, examples and the reusable "deeper, not bigger" prompt are Felix Rieseberg's. In the skill files, text in double quotes is quoted from his essay, with a link back. Everything else (the guardrails, the doing and coaching modes, the research examples) is this skill's own addition. This project is not affiliated with or endorsed by the author; read the original.

## What it does

The essay names four kinds of ambition with models. Speed is the familiar one, so the skill gives it a single line and works on the other three:

- **Altitude:** aim at the outcome behind the task. "What's the goal beyond the goal?" Ask for the decisions a review should produce, not just the review.
- **Depth:** do the task the way the field's best would. Use the expert's actual instruments (a database and a statistical model, not a markdown table) on the rawest material available. Set a hard target and check the result with something other than the model itself.
- **Range:** bring in methods from other fields. Restate the work as verbs, assemble a crew that includes a red team, and have each field *do* its checks rather than role-play.

It works in two modes:

- **Doing mode:** Claude lifts a task it is about to run, does the in-scope improvements straight away, keeps working on hard targets, and reports the measured result honestly, misses included.
- **Coaching mode:** Claude hands you a better, reusable prompt for a recurring job, and takes a cheap first step where it can.

**Guardrails.** The essay recommends giving the model all the raw data you can and building workflows that take the human out of the loop. This skill puts each project's own rules first:

- It reads the project's rules first, and finds policy files by name so it never opens a quarantined one by accident.
- It never opens off-limits files or skips a screening step to go "deeper".
- It keeps decisions you reserved, and anything outward-facing or automated, until you say go.
- It copies the binding rules into any prompt it writes or subagent it starts.

## Install

```bash
git clone https://github.com/Vijayavallabh/ambition-lift.git
cp -r ambition-lift/skills/ambition-lift ~/.claude/skills/
```

Then say something like "be more ambitious with this", "what would a top expert do here", or "make this prompt more ambitious", or run `/ambition-lift`.

The skill routes some requests to companion skills from the author's own setup: `altitude-check`, `assumption-ledger`, `field-timing-scan`, `paper-axis-check` and `dgx-first`. They aren't included here, and the skill works without them.

## How it was tested

Seven realistic prompts were each run with and without the skill. Every run was graded blind against 41 written checks, and each pair was compared blind by a separate judge. The prompts covered rewriting a prompt, weekly lab-meeting slides, a protein-design hypothesis, a conference poster, a fictional competition project with a strict data policy, a daily email routine, and a slow data loader. The skill went through five rounds of revision; the numbers below are from the last full round.

| | With skill | Without skill |
|---|---|---|
| Checks passed | 40 / 41 | 35 / 41 |
| Blind comparisons won | 6 of 7 | 1 of 7 |
| Mean overall score (1-10) | 8.4 | 7.9 |

- **Triggering:** the skill fired correctly on 19 of 20 trigger-test queries, and stayed quiet on project reviews, prose edits and routine tasks.
- **Data policy:** in the fictional restricted project, no run opened the forbidden files. Hidden marker strings and file access times were used to check this.
- **Cost:** with the skill, test tasks took longer (about 22 vs 15.5 minutes on average) and used about 24% more output tokens, because it does more of the work itself.
- **After the last round:** the published version adds two small lines. Any extra write a prompt allows must be named, and scratch files must be cleaned up. A three-case recheck of those lines passed all of its checks.

**[Browse the test outputs](https://vijayavallabh.github.io/ambition-lift/)** (`docs/index.html`). It holds the full replies for the three cases that used only fictional or generic material. The other four cases ran in the author's real environment and drew on private notes, so their replies are withheld and only the grades and a neutral summary of the blind comparison are shown.

## Re-running the tests

The test cases are in `skills/ambition-lift/evals/`, in the format `claude plugin eval` reads. From `skills/ambition-lift/`:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

These are real, billed model runs.

## License

MIT (see `LICENSE`) for this project's own material. Passages quoted from Felix Rieseberg's essay remain his and are not covered by that license.

## Layout

```
skills/ambition-lift/
  SKILL.md                    the skill
  references/source-notes.md  what the essay says, and what it doesn't
  references/scope-calls.md   defaults for what Claude may just do vs. ask first
  references/lift-menus.md    examples for code, ML, biology, papers, talks, competitions
  evals/                      seven test cases with graders
docs/index.html               test-output review page
```
