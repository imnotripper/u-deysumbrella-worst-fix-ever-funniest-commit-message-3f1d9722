# Selection — Worst Fix Ever: Funniest Commit Message

Judge brief (RULES.txt), in order: (1) reads as a one-line commit
message for a bug fix that made everything worse — loses to any
commit message on the subject; (2) makes a reader laugh out loud,
a real joke, not just a complaint; (3) captures the specific irony
of a repair that broke more than it mended; (4) sounds like a real
commit subject line — short, plain, the kind a tired engineer would
actually type at the end of a bad day; (5) a fresh angle instead of
the obvious ones about reverting, testing in production or breaking
everything. "A line that needs an explanation to be funny is weaker
than one that lands on its own."

Gate: 1–100 characters, one line, UTF-8, not only whitespace. All 10
candidates pass the gate (longest is 83 characters); the duel below
is on the judge brief alone, not on length.

## Candidates

1. (39) "fix: stop the leak by removing the pipe"
2. (83) "fix(login): users can no longer log in, which technically
   resolves the login errors" **WINNER**
3. (73) "fix: the bug is fixed, the feature is now also fixed (in the
   other sense)"
4. (57) "fix: patch the crash by deleting the feature that crashed"
5. (68) "fix: silence the alert by unplugging the thing it was
   alerting about"
6. (46) "fix: improve performance by removing the users"
7. (65) "fix: correct the typo that was holding the entire system
   together"
8. (65) "fix: the workaround is now the bug; the bug is now the
   workaround"
9. (44) "fix: close the ticket by closing the service"
10. (44) "fix: rename the bug to a feature and ship it"

## Pairwise duel (against the brief, in order)

- **2 vs 7:** the closest fight. 7 is elegant — a typo holding the
  system together is a specific, real irony. But 2's laugh is bigger:
  "technically resolves the login errors" is the tired engineer
  redefining success downward, and the fix (nobody can log in) is the
  exact bug it was meant to cure. 2 wins on criterion 2.
- **2 vs 5:** 5 is a good irony (unplug the alerter), but it reads as
  a joke about an alert, not a commit message about a fix — the
  "fix:" prefix does less work. 2 is unmistakably a fix report.
  **2 wins.**
- **2 vs 6:** 6 is funny and short, but "removing the users" is a
  known punchline shape; 2's irony is more specific to the login
  bug it names (criterion 3). **2 wins.**
- **2 vs 3:** 3 rests on a pun ("fixed in the other sense") that
  needs a beat to land; 2 lands on its own (brief: a line that needs
  an explanation is weaker). **2 wins.**
- **2 vs 8:** 8 is clever wordplay but reads as a quip, not a commit
  subject line a tired engineer would type (criterion 4); 2 sounds
  like a real `fix(login):` subject. **2 wins.**
- **2 vs 1 / 4 / 9 / 10:** 1 is too bare — a premise without a joke;
  4 is 1 with more words, same shape; 9 is a service joke, not a
  fix irony; 10 is a known trope ("rename the bug to a feature").
  **2 wins each.**

## Winner

Candidate 2, 83 characters: a real `fix(login):` subject line, the
fix is exactly the disease (no logins, no login errors), and
"technically" is the tired engineer telling the truth while lying
to himself. Lands on its own, no explanation needed. 83 of the 100
allowed characters — 17 to spare, tight without padding.
