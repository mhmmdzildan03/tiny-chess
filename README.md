# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mhmmdzildan03/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/mhmmdzildan03/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Chess engine in one file (main.py, under 4 KB, Python 3.13 stdlib only).
0x88-style mailbox board, negamax alpha-beta with quiescence, iterative
deepening under a fixed node budget (deterministic, no clock), a Zobrist
transposition table, and piece-square evaluation.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

The engine polls the env at MAKEFUN_ENV_URL for the game in play, and
answers each position with a UCI move.

---
<sub>Entered on [make.fun](https://make.fun/?ref=dk0njb1w&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
