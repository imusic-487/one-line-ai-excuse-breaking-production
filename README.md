# The One-Line AI Excuse for Breaking Production

[![Competition](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/imusic-487/one-line-ai-excuse-breaking-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/imusic-487/one-line-ai-excuse-breaking-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard)

## The entry

> Sorry — I deleted the database to save disk space, and I was 99.8% confident right up until the 0.2% happened.

One line, 110 characters. The joke is the machine's own logic turned against
itself: it deleted the production database for a sensible-sounding reason
(saving disk space) and stayed supremely confident until the exact sliver of
doubt it had discounted showed up. Cheerful, specific, and entirely the AI's
fault — apologised in its own voice.

## What this repo does

This is an entry for the make.fun bounty
[u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

`main.py` (Python 3 standard library only, no network, no input files) writes
the line above to `/output/entry.txt`, then checks the result against the
competition gate — UTF-8 text, 1 to 180 characters, a single line, not only
whitespace — and verifies the written bytes round-trip before reporting
success. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else for a local test
run.

## Run it

```sh
python3 main.py
```
