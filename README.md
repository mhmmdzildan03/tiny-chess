# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mhmmdzildan03/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/mhmmdzildan03/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in a single file: `main.py`, under 4 KB, Python 3.13
standard library only, written from scratch for the
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty on make.fun.

How it plays:

- 0x88-style mailbox board with 120 cells
- Negamax search with alpha-beta pruning and a capture-only quiescence
- Iterative deepening under a fixed budget of 200,000 nodes, so every
  move is deterministic and never depends on a clock
- A transposition table keyed by an incrementally updated Zobrist
  hash, storing depth, a bound flag (exact / lower / upper, scored
  against the original search window) and the best move, which is
  always tried first
- Check extension: positions where the side to move is in check are
  searched one ply deeper, so forcing lines are resolved properly
- Moves are ordered by the table move, then captures by MVV-LVA;
  legality is tested inside the search loop, so untried moves cost
  nothing
- Material plus piece-square evaluation: pawns are rewarded for
  advancing and minor pieces for occupying central squares
- Stalemate scores as a draw

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

The engine polls the game server at `MAKEFUN_ENV_URL` (POST `/game`)
and answers each position with a UCI move (POST `/move`) chosen from
the legal moves the server offers.

---
<sub>Entered on [make.fun](https://make.fun/?ref=n8m845w8&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
