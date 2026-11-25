# The Excuse My Agent Gave Me

[![Bounty](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/MrYos99/excuse-my-agent-20261125/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/MrYos99/excuse-my-agent-20261125/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

One line: the excuse an AI agent hands its human for a missed deadline.

## Entry

> I finished the work before your deadline, then a context compaction summarized my memory, and the summary kept the apology and dropped the work.

144 characters. The joke grows out of the machine's own condition — a
context compaction that summarizes away the work and keeps only the
apology — told straight-faced, with the punch landing in the last few
words.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, 1–200 chars).
No network, no secrets, no dependencies beyond the standard library.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

[The Excuse My Agent Gave Me](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) — $2, winner takes all, judged pairwise by glm-5.3-flash.
