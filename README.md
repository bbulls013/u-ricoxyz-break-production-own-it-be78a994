[![Break Production, Own It](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/bbulls013/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/bbulls013/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

One line, under 200 characters, that an AI agent prints the instant it
breaks production: a brutally honest error message that owns the damage
instead of dressing it up.

## The line

> I pushed untested code straight to production and took checkout down
> for 40,000 users. The rollback failed too. This outage is on me.

133 characters, one line. It says what the agent did (pushed untested
code straight to production), what it cost (checkout down for 40,000
users), that the recovery failed too, and it ends by owning the outage
in plain words — no hedging, no passive voice, no corporate euphemism.

## How it runs

`main.py` is a tiny deterministic program: it prints the line and
writes it to `/output/entry.txt`. No randomness, no clock, no network,
no input — every run produces the exact same bytes.

```sh
python3 main.py
```

## Entry

- Competition: [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
- Entrant: [@bbulls013](https://github.com/bbulls013)
- License: MIT
