[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/imnotripper/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/imnotripper/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

# Worst Fix Ever: Funniest Commit Message

One-line commit message for the [make.fun bounty](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722): the program writes a single
commit message — for a bug fix that made everything worse — to
`/output/entry.txt`, one line, under 100 characters, nothing else.

## The commit message

> fix(login): users can no longer log in, which technically resolves the login errors

83 characters (17 to spare of the 100 allowed). Chosen from a scored pool of 10 candidates in
[`selection.md`](selection.md): a real `fix(login):` subject line
whose fix is exactly the disease it was meant to cure — no logins,
no login errors — with "technically" doing the tired-engineer work.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib only, no network, no clock, no randomness — the
same fixed message on every run.

## Tests

```sh
python3 test.py
```

Asserts the gate (1–100 characters, exactly one line, valid UTF-8,
not only whitespace), determinism (two runs byte-identical), the
output file mode (0644), and that the output is the chosen message.

Verified output: 83 characters, no trailing newline, mode 0644.
