# Handoff: YouTube research on ETF portfolio optimization

For: Gemini (Argon deep research). Date: 2026-10-19.

## Context

The literature review `literature-review.md` (same folder) has 9 themes, built mostly from academic papers and written practitioner sources, all verified by opening the page. The weak spot is YouTube. The previous tool could confirm only the title and channel of each video, through oEmbed, and could not access descriptions or transcripts. So no video content was used as evidence. This pass fixes that.

Put the results in a new file, **`literature-review-02.md`**, in this folder. Do not rewrite `literature-review.md`; the two files will be merged later.

## The fund under study (context only, do not design it)

One actively managed ETF with three jobs:

1. **Safety:** about 12 months of spending in cash and short bonds.
2. **Inflation:** capped inflation-linked government bonds, matched to the liability.
3. **Growth:** a sleeve of ETFs weighted by an optimizer (highest return per unit of risk after fees, long only). The comparisons are equal weight on the same ETFs and one broad world ETF held alone.

The investor lives in Brazil, spends in BRL, and can buy US-listed ETFs, Irish UCITS ETFs and B3-listed ETFs.

## The question

What do the credible YouTube talks, lectures and channels say about optimizing the weights in a portfolio of ETFs? Do they agree or disagree with the academic evidence that equal weight (1/N) is hard to beat out of sample (DeMiguel, Garlappi and Uppal 2009) and the challenge to it (Kritzman, Page and Turkington 2010)?

## Topics, in order of priority

1. **Out-of-sample optimization:**
   - maximum Sharpe vs. minimum variance vs. risk parity vs. HRP vs. Black-Litterman vs. equal weight vs. one world ETF;
   - estimation error, constraints, shrinkage, turnover.
2. **Marcos López de Prado talks:**
   - HRP, "Building Diversified Portfolios that Outperform Out-of-Sample", backtest overfitting;
   - venues such as QuantCon, Quantopian, CFEM Cornell, ADIA.
3. **Evidence-based practitioners:**
   - Ben Felix (and the Rational Reminder podcast) on equal weight, factor ETFs, rebalancing, home bias and currency;
   - Patrick Boyle;
   - Corey Hoffstein (Newfound) on rebalancing timing luck;
   - Meb Faber;
   - Ray Dalio and Bridgewater on All Weather and risk parity;
   - Alex Shahidi.
4. **Factor ETFs after launch.** Backtest vs. live performance (smart beta).
5. **Rebalancing.** Bands vs. calendar, rebalancing with new cash first.
6. **Brazilian channels on investing abroad with ETFs:**
   - UCITS vs. US-listed ETFs;
   - BDRs of ETFs;
   - VT vs. IVV vs. VWRA11/IVVB11;
   - Law 14.754/2023;
   - currency exposure for someone who spends in BRL.

   Prefer channels from regulated institutions or named analysts with credentials. Examples: BTG Pactual "Investindo pelo Mundo", Abner Araujo.

## Videos already identified (title and channel confirmed, content NOT verified)

Watch them or read their transcripts, and summarize what they actually say:

- Finance Research Gate, "Hierarchical Risk Parity HRP Portfolio Optimization": https://www.youtube.com/watch?v=_OPDNwtubZg
- Finance Research Gate, "Risk Parity Portfolio Optimization Explained Equal Risk Contributions in Practice": https://www.youtube.com/watch?v=aIJ9MM7I9kw
- Lead-Lag Media, "Stagflation Is Back: How Risk Parity Actually Works in 2026": https://www.youtube.com/watch?v=UkTDKOQO_2A
- Cornell Financial Engineering Manhattan, "Marcos Lopez de Prado: The 7 Reasons Most Machine Learning Funds Fail": https://www.youtube.com/watch?v=npA8sI-k328
- BTG Pactual, "ETFs UCITS: como investir no exterior pagando menos imposto": https://www.youtube.com/watch?v=unQ4CCrmL30
- Abner Araujo, "IVV ou VT: Qual o Melhor ETF para Investir no Exterior": https://www.youtube.com/watch?v=RJbQe-cQnrM

Seen only in search results. Confirm the channel and content before using:

- López de Prado, Kapitaleierdagen 2024: https://www.youtube.com/watch?v=fOCzNFwmM7Y
- López de Prado, "Causality in Factor Investing": https://www.youtube.com/watch?v=NHQ0Q30fAP4
- Brazilian videos on VT and ETF overlap:
  - https://www.youtube.com/watch?v=mInrZVtLAsc
  - https://www.youtube.com/watch?v=iqz3OZo9nZQ
  - https://www.youtube.com/watch?v=Kjk8uPTMs1M
  - https://www.youtube.com/watch?v=v8FOFtIjPWI
- "The Death of the 60/40 Portfolio?": https://www.youtube.com/watch?v=2NSlam-fxuo (channel unknown)
- Ben Felix, "The Problem with Equal Weight Index Funds" (2026-02-08). Not found on YouTube yet.

## Rules

- Cite a video only if you actually accessed its content (transcript, captions or the video itself). For each one, give the channel, presenter, upload date, title, URL and the timestamp of each claim you use.
- Do not invent videos, numbers or quotes. If you can only see the title, mark the video "content not verified" and do not use it as evidence.
- Prefer presenters with a verifiable track record (academics, named fund managers, CFA charterholders, regulated institutions). Flag sponsored, affiliate or product-selling content.
- When a video cites a paper or study, name that primary source so it can be checked against `literature-review.md`.
- Keep disagreements. Where a YouTuber contradicts the academic evidence, say so.
- Paraphrase only. At most one quote per video, under 15 words.
- Out of scope: ticker recommendations, price history, Sharpe ratios you compute, buy or sell advice.

## Output format for `literature-review-02.md`

Write it in English and organize it by the topics above, comparing the videos within each topic rather than summarizing them one by one. For each topic:

- the claim, in 2 or 3 sentences;
- the videos, with verified details and timestamps;
- where they agree with or contradict the academic sources in `literature-review.md`;
- what this does and does not justify for the three-job fund.

End with:

- a reference list of videos in alphabetical order by channel;
- a **Not found** section listing what you could not verify.
