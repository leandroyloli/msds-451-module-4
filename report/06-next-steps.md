# Next steps

Toward Checkpoint B:

1. **Widen the universe.** Build the list of every equity ETF available in the United States, as Irish UCITS and on B3. Leave out leveraged and inverse ETFs.
2. **Collect the data.** Download monthly returns, fees, currency and start date for each ETF.
3. **Set the limits.** Fix the minimum history (proposed: five years) and the caps per ETF, country and currency.
4. **Group by exposure.** Pick one wrapper per exposure.
5. **Build the comparisons.** Build the anchored optimizer, equal weight and one world ETF, with minimum variance as a check.
6. **Test.** Run the backtest and the Monte Carlo simulation on data the rule did not see, after fees, with the monthly check and the bands, measured in dollars and converted to reais. Correct the Sharpe ratio for the number of variants tried.
7. **Verify the open sources.** Check the Brazilian tax rules against the text of the law.

## Research universe

- [United States, listed in the United States](#united-states-listed-in-the-united-states)
- [World, Irish UCITS](#world-irish-ucits)
- [Brazil, listed on B3](#brazil-listed-on-b3)

These 61 equity ETFs are the first list read in this checkpoint. They are a sample of the full universe, not the positions the fund intends to hold. The same market appears more than once when the wrapper changes.

AUVP11 and VWRA11 have traded only since September 2025, and AVWS since September 2024. They stay on the list to show what the minimum-history rule will exclude.

### United States, listed in the United States

VT is the US-listed world ETF. It holds large, mid-size, and small companies. VWRA, in the Irish section, holds the large and mid-size companies of the same idea.

| Ticker | Role | What it is |
| --- | --- | --- |
| VOO | Broad market | Vanguard S&P 500 |
| IVV | Broad market | iShares Core S&P 500 |
| SPY | Broad market | SPDR S&P 500 |
| VTI | Broad market | Vanguard Total Stock Market |
| ITOT | Broad market | iShares Core S&P Total U.S. Stock Market |
| VT | Broad market | Vanguard Total World, FTSE Global All Cap |
| QQQ | Broad market | Invesco QQQ, Nasdaq-100 |
| VUG | Broad market | Vanguard Growth |
| VTV | Broad market | Vanguard Value |
| VB | Broad market | Vanguard Small-Cap |
| VYM | Dividend | Vanguard High Dividend Yield |
| SCHD | Dividend | Schwab U.S. Dividend Equity |
| VIG | Dividend | Vanguard Dividend Appreciation |
| DGRO | Dividend | iShares Core Dividend Growth |
| DVY | Dividend | iShares Select Dividend |
| QUAL | Quality | iShares MSCI USA Quality Factor |
| SPHQ | Quality | Invesco S&P 500 Quality |
| JQUA | Quality | JPMorgan U.S. Quality Factor |
| VOOG | Growth | Vanguard S&P 500 Growth |
| VXUS | International | Vanguard Total International Stock, world outside the US |
| VEA | International | Vanguard FTSE Developed Markets |
| VWO | Emerging | Vanguard FTSE Emerging Markets |
| IEMG | Emerging | iShares Core MSCI Emerging Markets |
| VBR | Small-cap value | Vanguard Small-Cap Value |
| AVUV | Small-cap value | Avantis U.S. Small Cap Value |
| MTUM | Momentum | iShares MSCI USA Momentum Factor |
| USMV | Minimum volatility | iShares MSCI USA Min Vol Factor |

### World, Irish UCITS

Tickers are the London lines, except ZPRV and AVWS, which are the Xetra lines. VWRA and VWRD are the accumulating and distributing share classes of the Vanguard FTSE All-World fund. VUAA and VUSA are the same pair for the Vanguard S&P 500 fund. VHYA and VHYL are the same pair for the high-dividend fund.

| Ticker | Role | What it is |
| --- | --- | --- |
| VWRA | Broad market | Vanguard FTSE All-World, accumulating |
| VWRD | Broad market | Vanguard FTSE All-World, distributing |
| IWDA | Broad market | iShares Core MSCI World, accumulating |
| VHVE | Broad market | Vanguard FTSE Developed World, accumulating |
| ISAC | Broad market | iShares MSCI ACWI, accumulating |
| EIMI | Broad market | iShares Core MSCI Emerging Markets IMI, accumulating |
| CSPX | Broad market | iShares Core S&P 500, accumulating |
| VUAA | Broad market | Vanguard S&P 500, accumulating |
| VUSA | Broad market | Vanguard S&P 500, distributing |
| CNDX | Broad market | iShares Nasdaq-100, accumulating |
| IWQU | Quality | iShares Edge MSCI World Quality Factor, accumulating |
| VHYL | Dividend | Vanguard FTSE All-World High Dividend Yield, distributing |
| VHYA | Dividend | Vanguard FTSE All-World High Dividend Yield, accumulating |
| WSML | Small cap | iShares MSCI World Small Cap, accumulating |
| IWMO | Momentum | iShares Edge MSCI World Momentum Factor, accumulating |
| ZPRV | Small-cap value | SPDR MSCI USA Small Cap Value Weighted, accumulating. Xetra line |
| AVWS | Small-cap value | Avantis Global Small Cap Value, accumulating. Xetra line. History from September 2024 |

### Brazil, listed on B3

BOVA11, BOVV11, and BBOV11 follow the Ibovespa under three sponsors. IVVB11, NASD11, WRLD11, VWRA11, and ACWI11 are foreign markets in a local wrapper, priced in reais. VWRA11 holds the same Irish fund as VWRA.

| Ticker | Role | What it is |
| --- | --- | --- |
| BOVA11 | Broad market | iShares Ibovespa |
| BOVV11 | Broad market | IT Now Ibovespa |
| BBOV11 | Broad market | BB Ibovespa |
| PIBB11 | Broad market | IT Now IBrX-50 |
| BRAX11 | Broad market | iShares IBrX-100 |
| SMAL11 | Broad market | Small caps, SMLL |
| DIVO11 | Dividend | IT Now IDIV |
| BBSD11 | Dividend | BB S&P Dividendos Brasil |
| AUVP11 | Quality | Teva Ações Fundamentos. History from September 2025 |
| BEST11 | Quality | Investo Brazil quality |
| GOVE11 | Quality | IGCT, corporate governance |
| FIND11 | Sector | IT Now financials |
| IVVB11 | Foreign, in reais | S&P 500 |
| NASD11 | Foreign, in reais | Nasdaq-100 |
| WRLD11 | Foreign, in reais | IT Now MSCI World |
| ACWI11 | Foreign, in reais | Trend, broad global equity |
| VWRA11 | Foreign, in reais | Investo feeder of VWRA, FTSE All-World. History from 30 September 2025 |
