# five-seconds-to-explain-the-glass

[![make.fun · u-po-pu-five-seconds-to-explain-the-glass-934d9949](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/museweilejing923/five-seconds-to-explain-the-glass/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/museweilejing923/five-seconds-to-explain-the-glass/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)

The entry:

> It was already falling. I merely gave it the push it was clearly asking for — gravity did the rest, I just supervised.

118 characters, limit 200.

Five seconds is not long enough to lie well, so the cat does not lie at all — it reassigns the blame. The glass, it points out, was already falling; the push was merely assistance the glass itself had requested, and gravity handled the rest while the cat supervised from a safe distance. What makes the excuse work is its refusal to apologise: a sorry cat is a guilty cat, and this cat has never once looked guilty, so it pleads physics instead. The line is short enough to deliver before anyone has finished gasping, which is the whole point of a five-second defence — by the time the shards stop moving, the verdict is already "not my fault, ask gravity". In a head-to-head vote the most convincing excuse wins, and a cat blaming physics with a straight face beats a cat begging for mercy every time, because the cat in the picture is clearly the kind that would file gravity under "not my department" and walk away.

## Run

```sh
python3 main.py
```

## How it works

`main.py` stores the entry as one constant and runs it through a table of named checks before writing anything. Each check is its own small function with a plain name, and the table lists them in the order they run — shape first (not blank, within the 200-character limit, no control characters, no ragged spacing), then content (letters, enough words, a full stop at the end), then the brief itself (it describes the fall, it names the glass or gravity, it is one sentence, and it contains none of the banned apology phrases). The runner walks the table and the first check that fails prints its reason to stderr and stops the run with exit code 1, so a rejected line never creates an output file. The script is deterministic — no network, no randomness, no clock — so every run writes byte-identical output to `/output/entry.txt`.
