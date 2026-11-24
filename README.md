# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/ayilinalin/u-po-pu-say-what-actually-broke-a2c153b5-entry/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/ayilinalin/u-po-pu-say-what-actually-broke-a2c153b5-entry/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun.

## The entry

One line of software error copy that tells the user the brutal truth about
what actually broke — and makes them laugh on the way:

> Save failed: the disk is full of 14,000 screenshots you swore you'd sort later.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes that single line
to `/output/entry.txt`, deterministically, every run. It also asserts the
line stays inside the gate: 1–200 characters, one line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
