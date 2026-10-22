# Source notes: what the article says, and what it doesn't

Felix Rieseberg, "How to be more ambitious: A tutorial for humans with models", felixrieseberg.com, published 13 October 2026, about an 8-minute read.
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
The author is an engineering manager at Anthropic who works on Claude ("I work on Claude"); he says his advice "is not model-specific".

Read this before quoting or explaining the article, and whenever you are unsure whether an idea is his or this skill's. Text in double quotes is verbatim; everything else is close paraphrase in the article's order. For anything not covered here, read the original rather than recall it.

## Opening

- He keeps hearing of feats done "with or by Claude" that he "hadn't considered, didn't think possible, or simply lacked the curiosity and time to try" (this month: it "may have helped" discover a new planet, an AI music video he likes, and talk of "a new era of math" linking to Terence Tao's blog; hedged in the source, so don't cite them as established).
- "Model capabilities don't grow uniformly." Quoting Tao, models are "astounding in some directions, while inadequate in others". Some people fly with them; many still ask for capital cities or a less angry email.
- People working on AI keep saying we "ought to be more ambitious"; "we're not ambitious enough" has become a rallying cry. He grants the advice is "tricky" to follow, hence a tutorial.
- Four types: Speed, Altitude, Depth, Range.
  - Speed: "The same work in less time", "the bread and butter for AI's economic value". "Well established and requires little creativity in how you approach AI, so I'll skip this one."
  - Altitude: "Going up in abstraction and considering the outcome rather than the individual task."
  - Depth: "Considering a task the way a field-leading expert would." Go "one level deeper and touch the underlying data, tools, and problems."
  - Range: "Drawing on multiple fields rather than just the one the task might need at the surface, using knowledge, tools, and techniques you normally wouldn't."

## Altitude

- When you give the model a task, "it's executing your best guess at how to get the outcome you want". Ask "what do you want to happen next? What's the goal beyond the goal?"
- His shift: from asking Claude to fix individual crashes to asking it "to simply keep our apps crash-free".
- Running example, a quarterly business review (QBR) deck at an imagined Acme Inc. Resist just updating the template's numbers; give the model "as much data as you can get your hands on so it can understand your business". Three rungs, each more ambitious:
  1. "Tell me what changed this quarter, why, and what we should do about it."
  2. "Work out which three decisions are most urgent in the face of everything you've learned, and start working on potential directions with for/against arguments."
  3. "The review exists so leadership catches problems early and moves money and people to the right places. Design a better way to do that than a quarterly deck, show from our own history that it would have caught things sooner, and run it beside the current one for a quarter."
- Fit: "The altitude approach works best if you really are after some ultimate outcome; it works less well for creative endeavors." The tell-tale sign is "if you're going to have meetings to discuss whatever you're working on".
- Limits: "There are currently limits ("Claude, go make money" doesn't seem to work for most businesses by itself in 2026), but I generally see that models seem to be able to operate at higher levels of abstraction the more capable they become."
- "Altitude is also where people find durable workflows that take the human out of the loop, making it less necessary for you to constantly update the model with task after task." Doing this well "often involves changing your workflow": for crash-free apps he first made sure Claude "can easily fetch crash reports, understand which app version maps to what git commit", and gave it Windows, macOS and Linux computers "so it can actually independently reproduce and verify fixes".

## Depth

- "Being ambitious in depth means pushing the model to use the tools, techniques, media, and knowledge employed by the best professionals in the field - and to keep pushing until even those people might learn something new from your work." Running example: Acme struggles with churn.
- Five techniques, named in the article:
  1. "Insist on the same instruments used by the best in the industry": "When prompted to act like a professional, models often switch vocabulary without actually switching methods." "When Claude reaches for markdown tables, insist on the use of databases and statistical models. You don't necessarily have to know what the experts use, Claude usually does."
  2. "Pick unreasonable goals and tell the model that they're very reasonable": "You need your website to load in 5s instead of 10s? Ask for 200ms." "Reiterate that it's very much solvable, it just needs to keep going."
  3. "Challenge what you know": business beliefs are often "rough approximations of reality"; give the model raw data and ask it "to adversarially check assumptions". "We believe churn is an onboarding problem. Try to reproduce that from the raw data."
  4. "Produce new knowledge": once deep in the data, ask for blind spots. "Build a simulation of our customers that reproduces the last year from our logs. Then find the earliest signal of churn we don't know about yet, and show it predicts on data it has not seen."
  5. "Use an outside judge": "Do not ask the model to judge itself." He expects this to be solved with more capable models, "but in October 2026, I implore you to insist on outside validation. Ideally that's a tool the model can run to get feedback immediately."
- His reusable prompt (verbatim in SKILL.md): "I want a deeper version of this task, not a bigger one. ..." with four questions - what a top professional would do that you're not asking for, the rawest material, the specific methods and tools, and what other than the model or you would show the result is right - then a rewrite of the prompt.

## Range

- "being ambitious in range means that we consider our work from the perspective of different fields - more fields than would have been economical in the past." Every heist movie spends its first half hour assembling a crew. Multi-agent setups ("multiple threads, orchestrators, or simply subagents") make this easier.
- It takes creativity: seeing a colleague, Alex Albert, render interior designs with Blender made him think of Claude-built 3D environments for his homepage. Range is "easily where I see the most magic happen".
- "Try to replace the nouns with verbs", "An old trick from The Art of Innovation by Tom Kelley and Jonathan Littman": a quarterly review isn't "a deck", it's "getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes". Verbs show which fields could help.
- "Assemble the crew": "The deck needs to be amazing, otherwise aliens will blow up Earth. What kind of team will humanity get together?" For production quality "an analyst, a journalist, and an editor"; if presented, "a motion and audio designer"; as an adversarial "red team", "a short seller and a forensic accountant".
- Role play: "It is easy to accidentally engage in role play, which will make your transcript weirder without improving the actual outcome. Use this method to find fields and techniques. Don't ask the model to write like a short seller, ask it to do what a short seller does to research their position."
- Prerequisite for every type: "All the ways in which I describe ambition require the model to have a computer with the ability to install software and access to all kinds of relevant data (either using MCP connectors or other means)." He recommends using a tool that provides this.

## We have been here before (about people, not models)

- "We humans have always been held back by what we believe possible", and we trust ourselves only in narrow disciplines: Michelangelo didn't want to paint the Sistine Chapel because he was a sculptor.
- Psychology calls it self-efficacy; people who believe in their abilities accomplish more, and it can be hacked. Locke and Latham's review of 35 years of goal-setting research: people given specific hard goals "perform better than those who are simply told to try their best". Patrick Collison's "Fast" list records feats done under audacious goals and tight deadlines.
- Three documented hacks:
  - Believing it possible: George Dantzig, in 1939, solved two unsolved statistics problems he had copied off the blackboard as homework.
  - Watching someone else do it: Roger Bannister's four-minute mile (May 1954) stood alone for only 46 days; Sabastian Sawe ran the first official sub-two-hour marathon in London "this April", and the runner-up also broke two hours.
  - Permission to fail: The Inner Game of Tennis (you don't play your best when trying really hard); Linux, announced as "just a hobby, won't be big and professional like gnu".
- "Self-efficacy isn't a new problem, but it is a more powerful one now", with abilities making leaps "every couple of weeks". He invites readers to send him more techniques.
- Header image: Francisco Goya, "Modo de volar" (A Way of Flying).

## What the article does not say

Do not attribute these to Rieseberg; they are this skill's:

- Anything about project rules, data policies, quarantined files, screening steps, exclusion windows, competitions, pre-registration, sign-offs or authorship. The whole rules-first guardrail, the do-now / ask-first / blocked sort, and the exposure handling are this skill's.
- It does not say to take people out of decisions in general. It says altitude is where people find workflows that make it less necessary to keep feeding the model "task after task".
- It does not connect the goal-setting research or the self-efficacy hacks to prompting models; that section is about people. Using them to set targets or coach a user is this skill's extrapolation.
- That a hard target needs a judge fixed before the work and out of the model's reach, or that hard targets invite metric gaming; the hard-target loop and honest reporting are this skill's.
- Any technique for Speed. He does not dismiss Speed; he calls it AI's economic bread and butter and skips it as well established.
- That 'you are a world-class X' openers should be dropped. He warns that models switch vocabulary without switching methods and that role play doesn't improve outcomes; dropping such openers is this skill's rule of thumb. So is the crew-deletion test for role play.
- Research, ML or biology examples. His examples are Acme's review deck and churn, app crashes, website load time, and Blender interiors. Every research translation in `lift-menus.md` is this skill's.
- The prompt anatomy (Outcome, Material, Instruments, Target, Judge, Boundaries, Hand-back), the lift sheet, and the questions (0) and (5) added to his prompt.
