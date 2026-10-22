---
tags: [ambition-lift]
max_turns: 60
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

be more ambitious with this: bench.py says our patch loader takes ~7 s per epoch and the GPU sits idle waiting on it. i was going to just add multiprocessing workers. make it fast, properly. project is the current folder.

Input files: README.md, bench.py, gen_data.py, loader.py
