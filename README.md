# News-image 25 Nov 2026 — the world in one page

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Sasikianlarasati/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Sasikianlarasati/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for make.fun's **"Sum up 25 November's world news in one image"**
bounty ($100 in USDC, 50 places paid): a program that writes one image of
the day's news to `/output/entry.png`.

## The image

`entry.png` (1024×1024) sums up Wednesday 25 November 2026 — nine real stories
reported that day, verified against live news sources (Reuters, AFP, AP,
BBC, The Times of India) on the morning of 25 November 2026:

- **Lead — Middle East:** Houthis strike Riyadh's tallest tower, the PIF
  Tower, for the second time in under a week — 11 wounded; the Saudi-led
  coalition condemns a "terrorist attack". Houthi forces are also within
  60 km of Aden.
- **Technology — Huawei:** convicted in a sprawling US criminal trial —
  guilty of stealing trade secrets over its Iran business, acquitted of
  racketeering.
- **USA — Security:** the CIA and ODNI suffer a cybersecurity breach; some
  unclassified information compromised, Reuters reports.
- **Ukraine:** President Zelenskiy confirms Ukraine hit a Russian cargo ship
  in the Gulf of Finland on Saturday; ally Norway urges caution.
- **Russia:** Putin says retaliation is "inevitable" after Ukraine struck
  Russian oil plants; both sides trade accusations at the UN.
- **France:** former President Nicolas Sarkozy and his wife Carla Bruni are
  ordered to stand trial in a corruption case; first hearing April 2027.
- **Trade:** the Trump administration is set to unveil new tariffs after a
  probe into excess factory capacity.
- **Markets:** Anthropic shares slide below the $83 IPO price, on track to
  shed nearly $200bn in value.
- **Space:** NATO vows space defence amid reports Russia may launch a
  nuclear-armed satellite, possibly in December.
- **Sport:** England beat Australia in the 2nd T20I to level the series;
  Sooryavanshi smashes the fastest List A double hundred.
- **Also today:** North Korea threatens to shut Switzerland's diplomatic
  office in Pyongyang over youth-camp sanctions; Iraq's PM orders federal
  control of Kurdish oilfields, Kurds reject the move; 25 Nov is the
  International Day for the Elimination of Violence against Women.

## Run

```sh
python3 main.py
```

Writes `entry.png` to `/output/entry.png`. Python 3.13 and its standard
library alone — deterministic (byte-identical on every run), no network.
