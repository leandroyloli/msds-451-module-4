# Deep research brief — literature for an ETF of ETFs

You are gathering sources for a literature review. You are not designing the fund, and you are not choosing weights.

## The question

Who has studied a portfolio made of exchange-traded funds, and what happened when someone tried to hold those funds in an optimized proportion?

The fund under study is one actively managed ETF with three jobs:

1. Safety: about twelve months of spending in cash and short bonds.
2. Inflation: government bonds that pay inflation plus a real rate, currency and maturity matched to the bill, capped so this block does not consume the whole portfolio.
3. Growth: a portfolio of other ETFs. An optimizer sets the weights inside this block only. The objective proposed for that optimizer is the highest return per unit of risk after fees, long only. The comparisons are equal weight on the same funds, and one broad world ETF held alone.

The investor lives in Brazil, spends in reais, and can buy US-listed ETFs, Irish UCITS ETFs, and ETFs listed on B3.

## What to return

Write one markdown file, `literature-review.md`, in English. Organize it by theme. Inside each theme, compare the approaches. Do not summarize papers one by one. Do not recommend a portfolio. Do not invent a paper, a number, a journal, or a URL. If you cannot open a source, say so and do not cite it. If the sources disagree, keep the disagreement.

Aim for a review a careful reader can check. Prefer peer-reviewed work and primary practitioner research (a named author, a publisher, a year). A blog is allowed only as a pointer to a primary source.

## Themes to cover, in this order

1. **Stock selection against the index.** Evidence on how often active stock picking beats a broad index over ten years and longer. Name the scorecard or paper, the universe, and the horizon.
2. **Portfolio optimization against simple diversification.** Markowitz and what came after. The specific question is whether optimized weights beat equal weight, or one broad fund, on data the optimizer did not see. Include DeMiguel, Garlappi, and Uppal if you can verify the paper. Include later work that confirms or challenges it.
3. **Factor ETFs.** Quality, dividend, value, and other tilts implemented as long-only ETFs. What is left of the premium after costs, and after the fund is launched. Separate in-sample results from out-of-sample results.
4. **Inflation-linked government bonds as the long-horizon safe asset.** Why a bond that pays inflation plus a real rate is used to fund a dated liability, and how the weight of that bond depends on the real yield. Campbell and Viceira belong here if you can verify them.
5. **Currency for an investor who spends in an emerging-market currency.** Economic exposure versus the currency of the account. When foreign equities are left unhedged, and when foreign bonds are hedged. Do not treat a US investor and a Brazilian investor as the same case.
6. **Rebalancing.** Bands, calendar checks, and correcting with new cash before selling. What rebalancing is for (keeping risk near a mandate) and what it does not reliably deliver (an extra return). Include the Vanguard studies if you can verify them.
7. **Funds of ETFs and ETF-only portfolios.** Anyone who has published a portfolio whose holdings are themselves ETFs, including target-date or goal-based designs that separate a cash floor, an inflation hedge, and a growth sleeve. Say how close each one is to the three-job fund above. If you cannot find a close match, say that, and name the nearest neighbor.

## For each theme, include

- The claim, in two or three sentences.
- Two or more sources that a reader can find, with author, year, title, and venue.
- Where the sources agree, and where they do not.
- What the claim does, and does not, justify for the three-job fund.

## Also return

A reference list in alphabetical order. One line per source: author, year, title, venue, and a URL you actually opened. Then a short note titled **Not found**, listing the questions above for which you could not verify a source.

## Do not include

Price history, a recommended ticker list, Sharpe ratios you computed, or advice to buy or sell. Those are out of scope for this brief.
