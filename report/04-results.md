# Results

Checkpoint A asks for conceptual results, not a performance number. Nothing has been tested yet.

## The main finding

**An optimizer fed with past average returns rarely beats equal weight on data it has not seen.** Expected returns are hard to estimate. Small errors in them become extreme weights, and those errors eat the gain from optimizing.

Optimizers do better when they lean on risk instead of return, use limits, and trade little. Even so, none wins every time. And no study I found tests a universe of ETFs against one world ETF, after fees.

So the most likely outcome of this project is a tie. That is still an answer: it would mean equal weight, or one world ETF, is enough. For the optimizer to count as the winner, it must beat both benchmarks by at least 0.1 in Sharpe ratio, after fees, on data it has not seen. Anything smaller is treated as noise.

## What the reading confirmed

| Decision | Status |
| --- | --- |
| Hold ETFs, not companies | Supported |
| Inflation block in NTN-B, matched to dated spending | Supported |
| Safety and inflation in reais, the currency of spending | Supported |
| Foreign equities unhedged | Supported by theory, not yet tested on the real |
| Monthly check, bands, new money first | Supported. Rebalancing controls risk; it does not add return |

## What the reading changed in the design

1. **Anchored inputs.** Expected returns come from the world market portfolio, not from each ETF's past average. The covariance matrix is shrunk. Minimum variance runs beside the optimizer as a check.
2. **Exposure before wrapper.** In the first list of 61 ETFs, seven follow the S&P 500 and six follow a world index. The fund first chooses the market, then the cheapest and most tax-efficient ETF for it. Otherwise the optimizer would treat copies as diversification.
3. **Minimum history.** Young ETFs, such as AUVP11 and VWRA11, are recorded but not weighted. Factor ETFs are judged on their live record, not their backtest.
4. **Fixed inflation block.** No study supports moving NTN-B with the real yield. A fixed ladder keeps the focus on the growth fund.
