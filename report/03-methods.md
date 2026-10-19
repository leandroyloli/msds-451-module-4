# Methods

- [The managed portfolio](#the-managed-portfolio)
- [The growth fund](#the-growth-fund)
- [The screen an ETF must pass](#the-screen-an-etf-must-pass)
- [The objective of the optimizer](#the-objective-of-the-optimizer)
- [How financial engineering does the work](#how-financial-engineering-does-the-work)
- [Rebalancing](#rebalancing)
- [What this is, in the language of the assignment](#what-this-is-in-the-language-of-the-assignment)

This section says what the portfolio will do. It does not test it yet.

## The managed portfolio

A program may change weights. It may not change the jobs.

- **Safety.** Twelve months of spending in cash and short-term bonds, in reais. If the block is short, it is filled first.
- **Inflation.** NTN-B matched to dated spending, capped at about 60 percent of the portfolio. Fixed ladder: about 20 percent short, 35 percent intermediate, 45 percent long.
- **Growth.** Between 25 and 40 percent of the portfolio, in the growth fund. This is where the research happens.

## The growth fund

**What it holds.** Every equity ETF the investor can buy: listed in the United States, as Irish UCITS, or on B3. Leveraged and inverse ETFs are excluded. The 61 ETFs in [the research universe](06-next-steps.md#research-universe) are only the first sample.

**Exposure and wrapper.** The same market is often sold in several ETFs, for example the S&P 500 as a US-listed, an Irish UCITS and a B3 ETF. That choice is the **wrapper**. The fund decides in two steps:

1. **Exposure:** which market, and how much.
2. **Wrapper:** which ETF delivers that market, by cost, domicile, dividend treatment and tax.

**Currency.** Each ETF is held in its own currency, unhedged, as part of the diversification. Results are measured in dollars, so the choice of ETFs is judged apart from the real. The conversion to reais is a separate line.

**Limits.** Caps per ETF, country and currency, set in Checkpoint B.

## The screen an ETF must pass

Every candidate goes through the same tests:

- a minimum history of monthly returns, needed for the backtest and the Monte Carlo simulation (proposed: five years);
- return, volatility, and the depth of the worst fall;
- correlation with the other candidates;
- what is left after fees;
- whether the result still holds on a period the rule did not see.

An ETF that fails gets no weight. A young ETF, such as AUVP11 or VWRA11, is recorded but not weighted.

## The objective of the optimizer

The optimizer runs only inside the growth fund, and only on ETFs the screen approved.

- **Objective.** The highest return per unit of risk, after fees.
- **Constraints.** Long only and fully invested: no borrowing, no short sales. Caps per ETF, country and currency.
- **Inputs.** Expected returns anchored to the world market portfolio, a shrunk covariance matrix, and minimum variance as a check.

Two benchmarks keep it honest:

1. Equal weight on the same approved ETFs, on the same dates.
2. One world ETF, held alone.

The optimizer wins only if its Sharpe ratio beats both benchmarks by at least 0.1, after fees, on data it has not seen. Otherwise the simple option wins, and that is the finding. The optimizer never takes money from the safety or inflation blocks.

## How financial engineering does the work

The course's toolkit answers the two questions of the growth fund: which ETFs, and in what weight. Each step of the rule maps to a method.

| Step | Question | Method | Source |
| --- | --- | --- | --- |
| 1. Describe | Is this ETF worth a place? | Return, volatility, worst fall, and Sharpe ratio after fees | Sharpe (1994) |
| 2. Look through | Is it a new market or a copy? | Correlation matrix and hierarchical clustering. A regression on market, size, value and momentum factors shows what the ETF really holds | Sharpe (1963); Fama and French (1993); López de Prado (2016) |
| 3. Weight | How much of each ETF? | Mean-variance optimization at the highest Sharpe ratio, long only, with caps | Markowitz (1952) |
| 4. Feed | What returns should the optimizer expect? | Equilibrium returns implied by the world market portfolio, and a shrunk covariance matrix | Black and Litterman (1991); Ledoit and Wolf (2003); Grinold and Kahn (2000) |
| 5. Cross-check | Are the weights stable? | Minimum variance and hierarchical risk parity, run beside the optimizer | López de Prado (2016); Hudson and Thames (2020) |
| 6. Test | Would it have worked? | Walk-forward backtest with costs, and a Monte Carlo bootstrap of monthly returns. A deflated Sharpe ratio corrects for the number of variants tried | Bailey and López de Prado (2014) |
| 7. Maintain | How does it stay near the rule? | Monthly bands, written as code, so the fund runs without discretion | Assignment: automated, rule-based trading |

Steps 1 and 2 choose the ETFs. Steps 3 to 6 set and test the weights. Step 7 keeps them.

## Rebalancing

The same rule applies to the three blocks and to the ETFs inside the growth fund. Each target has a band a few percentage points wide.

1. Once a month the program measures. Inside the band, it does nothing.
2. Outside the band, new money goes first to whatever is most behind.
3. Only if new money is not enough does it sell, and only back to the edge of the band, because a sale has a cost and a tax.

The promise is that the mix stays near the rule, not that rebalancing adds return.

## What this is, in the language of the assignment

- **The fund.** The growth fund: an actively managed fund of ETFs, inside a managed portfolio.
- **Method.** Systematic portfolio selection and optimization, in the line of Markowitz and Sharpe.
- **Analysis.** Rule-based, not fundamental stock picking. After an ETF is admitted, the program sees only returns, risk, fees and correlations.
- **Trading.** Closer to buy-and-hold than to daily trading. Holdings change when a band breaks. The fund is long only. The rule aims for turnover below 20 percent a year in the growth fund. Checkpoint B measures the real figure.
- **Not used.** Technical analysis and trend following are not part of the rule. The growth fund holds broad markets for the long run. The safety block, not a timed exit, absorbs a falling market. Trend following can be tested later as a variant.
- **Open question.** A hedge with index options is not in the rule. One option chain I looked at had spreads too wide to serve as that hedge.
- **Cash.** The cash share is the safety block, twelve months of spending.

Checkpoint B specifies the data, the dates and the tests. This checkpoint stops at the rule.

## References for this section

- Bailey, D. H. and López de Prado, M. (2014). The deflated Sharpe ratio: Correcting for selection bias, backtest overfitting and non-normality. *Journal of Portfolio Management* 40(5).
- Black, F. and Litterman, R. (1991). Asset allocation: Combining investor views with market equilibrium. *Journal of Fixed Income* 1(2): 7-18.
- Fama, E. F. and French, K. R. (1993). Common risk factors in the returns on stocks and bonds. *Journal of Financial Economics* 33(1).
- Grinold, R. C. and Kahn, R. N. (2000). *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk*, 2nd ed. New York: McGraw Hill.
- Hudson and Thames (2020). *Guide to Modern Portfolio Optimization*. GitHub. [Link](https://github.com/hudson-and-thames/guide_to_modern_portfolio_optimization/blob/main/Guide%20to%20Modern%20Portfolio%20Optimization.pdf)
- López de Prado, M. (2016). Building diversified portfolios that outperform out of sample. *Journal of Portfolio Management* 42(4).
- Markowitz, H. (1952). Portfolio selection. *Journal of Finance* 7(1): 77-91.
- Sharpe, W. F. (1963). A simplified model for portfolio analysis. *Management Science* 9: 277-293.
- Sharpe, W. F. (1994). The Sharpe ratio. *Journal of Portfolio Management* 21: 49-58.
