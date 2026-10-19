# Literature review Opus 5.5: academic and practitioner sources on portfolios of ETFs

Scope: who has studied portfolios built from ETFs, and what happened when the funds were held in optimized proportions. The fund under study holds (1) about twelve months of spending in cash and short bonds, (2) capped inflation-linked government bonds matched to the liability, and (3) a growth sleeve of ETFs weighted by an optimizer (maximum return per unit of risk after fees, long only), compared against equal weight and against one broad world ETF. The investor spends in BRL.

> **AI-generated.** Prepared with AI research agents (Opus 5.5) and edited by the author. A source is cited only if its page was opened. Where only a summary or a secondary page was available, the text says so.

Verification rule: a source is cited only if its page (publisher, RePEc/IDEAS, NBER, institutional page, or a named secondary page) was opened. When the primary page was blocked and a secondary page was used, that is stated. Findings come mostly from abstracts and publisher summaries, not full texts; no figure below was computed by the author of this review.

---

## 1. Stock selection against the index

**Claim.** After costs, most actively managed equity funds trail a broad index, and the share that trails rises with the horizon. This holds in the US and in Brazil. The academic explanation combines costs (Fama and French), persistence that is explained by factors and expenses rather than skill (Carhart), and the concentration of long-run stock returns in a small number of firms (Bessembinder).

**Sources and how they compare**

- *Scorecards (practitioner, S&P Dow Jones Indices).* The SPIVA PDFs returned HTTP 403, so figures come from secondary pages that quote them.
  - SPIVA U.S. Year-End 2024, as reported by ICFS: large-cap active funds vs. the S&P 500 underperformed at 65.2% (1 year), 76.3% (5 years) and 84.3% (10 years). The page says that above 90% underperform over 15 years without giving the exact figure.
  - SPIVA Latin America Mid-Year 2025, as reported by Funds Society (2025-10-29): over 10 years to 2025-06-30, 86.0% of Brazil equity funds trailed the S&P Brazil BMI; 66.3% of large-cap funds and 85.3% of mid/small-cap funds trailed their benchmarks.
  - A later SPIVA Latin America reading, as reported by B3 Bora Investir: 90.8% of Brazil equity funds trailed over 10 years. The page does not name the exact edition.
- *Academic.*
  - Fama and French (2010): the aggregate US active fund portfolio is close to the market, and costs reach the investor as a lower return. Bootstrap tests find few funds whose returns cover their costs; before fees there is some evidence of skill in the extreme tails.
  - Carhart (1997): common factors and expenses explain almost all performance persistence; the persistence that remains sits in the worst funds. A replication (Choi and Zhao 2021, *Critical Finance Review*, listed on the FORRT page) finds no significant persistence in 1994 to 2018.
  - Bessembinder (2018), as reported by ASU: about 26,000 US stocks since 1926. 58% did not beat Treasury bills over their life, and 4.3% of firms generated the net wealth created. The journal page was blocked, and the ASU page has internal inconsistencies (86 vs. 90 firms; end year 2016 vs. 2017).

**Agreement and disagreement.** The sources agree that the average active fund loses after costs and that the losing share grows with the horizon. They disagree on skill in the tails: Fama and French find some before fees, while Carhart and its replication do not. In Brazil, large-cap funds do better than mid/small-cap funds over 10 years, though most still lose.

**What this justifies for the three-block portfolio.** It justifies building the growth sleeve from index ETFs rather than from stock pickers. It does not show that an optimizer choosing weights *among* ETFs will beat a broad index: that is a different decision, and Theme 2 covers it.

---

## 2. Portfolio optimization against simple diversification

**Claim.** Mean-variance optimization that uses sample means usually loses to equal weight (1/N) out of sample, because errors in the estimated expected returns dominate. Optimizers that estimate the mean conservatively, rely mostly on the covariance (shrinkage or constraints), or trade little can beat 1/N. No method beats 1/N robustly and simply across datasets.

**Sources and how they compare**

- Markowitz (1952) is the theoretical basis; it contains no out-of-sample test.
- DeMiguel, Garlappi and Uppal (2009): none of 14 models, tested on 7 datasets, consistently beats 1/N in Sharpe ratio, certainty-equivalent return, or turnover. The estimation window needed to beat 1/N would be about 3,000 months with 25 assets and about 6,000 months with 50 assets.
- Kritzman, Page and Turkington (2010) challenge this. Across 13 datasets, 1,028 series and more than 50,000 optimized portfolios, optimizers beat 1/N out of sample when they use long samples, simple expected-return assumptions, or minimum variance. Optimizing the covariance alone already adds value.
- Kirby and Ostdiek (2012) attribute the DGU result to the test design (high estimation risk and extreme turnover). Low-turnover volatility-timing and reward-to-risk-timing strategies beat 1/N even with high transaction costs.
- Jagannathan and Ma (2003): a no-short-sales constraint is equivalent to shrinking the covariance matrix. Constrained minimum-variance portfolios perform about as well as factor-model and shrinkage portfolios.
- Ledoit and Wolf (2003 working paper): shrinking the sample covariance lowers tracking error and raises the realized information ratio. The 2004 journal version was not verified on a page.
- Becker, Gürtler and Hibbeln (2015) test Michaud resampling: Markowitz beats Michaud on average, and the choice of estimator and constraints matters more than the optimization method. No primary Michaud source was opened.

**Agreement and disagreement.** All agree that estimating expected returns is the central problem. DGU conclude that 1/N is hard to beat in practice. KPT and Kirby and Ostdiek show it can be beaten with disciplined estimates and low turnover. Jagannathan and Ma and Ledoit and Wolf locate the useful part of optimization in the covariance. None of these studies tests a universe made only of ETFs against one broad world ETF.

**What this justifies for the three-block portfolio.** It justifies treating equal weight as a serious benchmark rather than a straw man. It also supports long-only constraints, which act as shrinkage. A maximum-Sharpe objective depends on expected-return estimates, which is the input DGU show to be the weakest. The literature does not establish that the proposed optimizer will beat equal weight or a single world ETF out of sample; it suggests that minimum-variance or covariance-only variants have better odds.

---

## 3. Factor ETFs

**Claim.** Published factor premia shrink after publication and after a product launches. Many factors fail stricter statistical standards, costs remove the high-turnover anomalies, and the long side captures only part of value and momentum. On average, smart-beta ETFs deliver roughly the market return or less after fees once they are live.

**In-sample evidence (and its reliability)**

- Harvey, Liu and Zhu (2016): a new factor should clear a t-statistic of about 3.0, and most claimed findings are likely false.
- Hou, Xue and Zhang (2020): of 452 anomalies, 65% fail at |t| > 1.96 and 82% at |t| > 2.78; 96% of trading-friction anomalies fail. Those that replicate are much smaller than originally reported.

**After costs and long-only**

- Novy-Marx and Velikov (2016): most anomalies with turnover below 50% a month keep a significant net spread, while few high-turnover strategies survive. Size, value and profitability have the largest capacity.
- Israel and Moskowitz (2013): the long side accounts for almost all of the size premium, 60% of the value premium and about half of momentum. Value is weak among the largest stocks.

**Out of sample and after launch**

- McLean and Pontiff (2016): the bibliographic page was opened, but it carries no abstract. The commonly quoted declines (26% lower out of sample, 58% lower after publication, across 97 predictors) are **not verified on a page** and should be checked before citing.
- Huang, Song and Xiang (2020, SSRN), as reported by InvestmentNews: smart-beta indices beat the market by 2.77% a year before ETF listing (backtest) and lagged it by 0.44% a year after listing, net of fees. The authors attribute the gap to data mining.

**Agreement and disagreement.** The sources converge that backtests and published premia overstate future returns. They differ on how much survives: Novy-Marx and Velikov and Israel and Moskowitz suggest that low-turnover tilts (value, profitability, size) keep part of the premium, while Huang et al. find no average excess return for ETFs after listing. No verified study isolates quality ETFs or dividend ETFs specifically.

**What this justifies for the three-block portfolio.** It justifies discounting any factor ETF's backtest. Only post-launch track records should feed the optimizer's expected returns, and low-turnover tilts are preferable. It does not justify assuming that a quality, dividend or value tilt will add return after fees.

---

## 4. Inflation-linked government bonds as the long-horizon safe asset

**Claim.** For a long-horizon, risk-averse investor, the riskless asset is not cash. It is an inflation-indexed bond whose maturity matches the horizon or liability, because it hedges changes in real interest rates. As risk aversion rises, the myopic demand for risky assets goes to zero but the intertemporal hedging demand remains. How much weight goes to risky assets depends on their expected premium over the real rate, so a higher real yield makes the indexed bond relatively more attractive.

**Sources and how they compare**

- Campbell and Viceira (2001): conservative investors should hedge falling real rates, and long inflation-indexed bonds are the right instrument. Nominal bonds are a substitute only when inflation risk is low. Their 2002 book (*Strategic Asset Allocation*, OUP) develops this in a chapter of the same name, but its page was seen only in search results, so it is not cited.
- Brennan and Xia (2002) solve the finite-horizon problem with only nominal assets. Hedging demands depend on horizon, risk aversion and bond maturity, and the bond maturity should be chosen to match the horizon.
- Kothari and Shanken (2004): simulated indexed-bond returns have lower real volatility and much lower correlation with stocks. Efficient portfolios hold substantial indexed-bond weights, which TIPS data from February 1997 to July 2003 broadly confirm.
- Campbell, Shiller and Viceira (2009): long real yields fell from the 1990s to 2008, then spiked in the crisis, and breakevens collapsed. Even so, indexed bonds still provide a safe asset for long-term investors, despite short-run volatility and illiquidity.

**Agreement and disagreement.** The sources agree that a maturity-matched indexed bond is the lowest-risk asset for a long-horizon investor. Brennan and Xia is the nominal-only case and converges with Campbell and Viceira once indexed bonds exist. The 2009 paper adds the main caveat: mark-to-market volatility and liquidity risk in stress. No verified source gives a formula linking the optimal weight to the level of the real yield; that link is a reading of the models, not a tested result.

**What this justifies for the three-block portfolio.** It justifies an inflation-linked, maturity-matched block to fund a dated liability in the spending currency (in Brazil, NTN-B). It does not justify a specific weight, and it does not settle how high the cap should be. No verified academic study models optimal NTN-B allocation or Brazilian sovereign risk.

---

## 5. Currency for an investor who spends in an emerging-market currency

**Claim.** The hedge decision depends on how each currency co-moves with the risky portfolio, measured in the currency the investor consumes in (economic exposure), not the currency of the account. For foreign bonds, the evidence favors hedging close to fully. For foreign equities, the answer depends on the home currency: holding "safe-haven" currencies (USD, EUR, CHF) unhedged lowers equity portfolio risk.

**Sources and how they compare**

- Perold and Schulman (1988): hedging has a long-run expected return near zero, so it is a "free lunch" that cuts risk. They recommend a hedged benchmark and treating currency exposure as an active decision.
- Black (1989): in an idealized world, hedge foreign equities at the same ratio for every country, always below 100%. The ratio does not depend on where the investor lives.
- Campbell, Serfaty-de Medeiros and Viceira (2010): in 1975 to 2005, USD, EUR and CHF moved against global equities. A risk-minimizing equity investor should hold them even though their average return is low. For global bonds, minimum risk is close to a full hedge with a modest long USD position.
- Schmittmann (2010, IMF): for German, Japanese, UK and US investors in 1975 to 2009, hedging cuts volatility substantially at quarterly horizons, and the benefit persists up to five years, contrary to earlier studies.
- Vanguard (2026), "The FX dimension": the rule of thumb is to hedge bond exposures and leave most foreign equities unhedged. Only the summary page was opened.

**Agreement and disagreement.** All five agree on hedging foreign bonds. On equities they disagree:
- Perold and Schulman favor a full hedge.
- Black favors a partial, universal hedge.
- Campbell et al. contradict "universal" by showing the answer depends on the home currency.
- Vanguard lands in between, leaving most equities unhedged.

**US vs. Brazilian investor.** These are not the same case. For a US investor, the home currency is itself a safe haven, so leaving foreign equities unhedged adds exposure to procyclical currencies. For an investor spending in BRL, a risk-on currency, unhedged USD assets tend to gain when global equities fall. This is an inference from Campbell et al.'s framework; **no verified study tests BRL directly**.

**What this justifies for the three-block portfolio.** It supports hedging foreign bonds and supports leaving foreign equities largely unhedged for a BRL spender. It also implies that the safety and inflation blocks, which fund BRL spending, belong in BRL instruments. It does not quantify the hedge ratio for BRL.

---

## 6. Rebalancing

**Claim.** Rebalancing exists to keep risk near the target allocation, not to add return. No frequency or band is optimal for risk-adjusted return, and infrequent monitoring with tolerance bands cuts trading. Whether a "rebalancing bonus" exists is disputed.

**Sources and how they compare**

- Jaconetti, Kinniry and Zilbering (2010, Vanguard; a third-party copy of the PDF was opened). They state that the main goal is to minimize risk relative to the target, not to maximize returns. Risk-adjusted returns are similar whether rebalancing is monthly, quarterly or annual. Trading differs widely: 1,008 rebalancing events for monthly with no band vs. 15 for annual with a 10% band. They suggest monitoring once or twice a year with roughly 5% bands. The section on using new cash flows first was not verified on the pages read.
- Daryanani (2008), executive summary only: look often, trade rarely. Reviewing every two weeks and rebalancing only the asset classes outside wide bands "more than doubled" the benefit vs. annual rebalancing.
- Willenbrock (2011): the diversification return comes from rebalancing itself (selling winners, buying losers), not from lower variance. It explains most of the excess return of the Gorton and Rouwenhorst commodity index.

**Agreement and disagreement.** All agree that bands are cheaper than frequent calendar rebalancing. They disagree on return: Vanguard sees no reliable gain, Willenbrock shows a real effect among volatile, weakly correlated assets, and Daryanani claims a gain. A replication reported to find Daryanani's gain statistically insignificant was **not verified**. Vanguard's 2022 "Rational rebalancing" paper could not be opened (broken links).

**What this justifies for the three-block portfolio.** It justifies band-based checks on a set calendar, framed as risk control around the mandate. It also makes routing new cash to underweight sleeves before selling a reasonable cost saving, though the primary source for that point was not verified. It does not justify promising a return from rebalancing.

---

## 7. Funds of ETFs and ETF-only portfolios

**Claim.** Goal-based designs split wealth into sub-portfolios, each with its own risk limit. Das et al. show this can be reconciled with mean-variance efficiency. Actively managed ETFs that hold only other ETFs exist in the market, and fee layering is the main structural risk. **No verified product combines a 12-month cash floor, a capped inflation-linked sleeve, and an optimizer-weighted ETF growth sleeve.**

**Sources and how they compare**

- Das, Markowitz, Scheid and Statman (2010): each mental account has a return threshold, and its risk is the probability of missing it. Mean-variance, mental-account and VaR formulations are mathematically equivalent, and the aggregate portfolio is efficient when short sales are allowed. Banning short sales costs little in certainty-equivalent terms.
- Brown, Goetzmann and Liang (2002): in funds of hedge funds, layered fees can, under some conditions, exceed realized returns. The authors propose an alternative fee structure.
- BlackRock (2026), iShares LifePath Target Date 2035 ETF fact sheet: an active ETF launched 2023-10-17, with 13 holdings, all iShares ETFs. Total expense is 0.10%, made up only of acquired fund fees; the management fee is 0.00%. As of 2026-06-30 it held 66.10% equity, 33.45% fixed income and 0.44% cash.

**Nearest neighbor.** The iShares LifePath ETF is the closest verified structural analog: an actively managed ETF holding only ETFs, with no second fee layer. The match is only moderate:
- Weights follow a target-date glide path, not a maximum-Sharpe optimizer.
- There is no explicit 12-month cash floor (0.44% cash).
- No TIPS or T-bill ETF appears among the top holdings, so there is no capped inflation sleeve.
- It is built for a US investor, not one spending in BRL.

Das et al. is the closest academic analog for separating the three blocks.

**Agreement and disagreement.** Das et al. formalize goal-based bucketing and show it can be reconciled with whole-portfolio optimization. Brown et al. document harm from fee layering. The LifePath structure (acquired fund fees only, zero management fee) shows one way to avoid a second fee layer.

**What this justifies for the three-block portfolio.** It supports separating the safety, inflation and growth blocks with distinct risk limits, and it supports a fee design that avoids double layering. It does not provide evidence on how such a fund performs, because no verified close match exists.

---

## 8. Portfolios of ETFs in depth (second research pass)

**Claim.** Direct evidence on optimizing weights *across ETFs* is thin. What exists points one way: the value of an ETF portfolio comes from broad, cheap funds, low turnover, and not believing backtests. Sophisticated weighting (maximum Sharpe, HRP) has no verified, peer-reviewed, out-of-sample win over equal weight in an ETF universe after costs.

**8.1 Optimizing across ETF universes.**
- No peer-reviewed study that optimizes an ETF universe against equal weight with costs could be opened.
- López de Prado (2016, *Journal of Portfolio Management*), "Building Diversified Portfolios that Outperform Out-of-Sample", introduces hierarchical risk parity (HRP). The SSRN page was blocked and the mirrored PDF could not be read. Two points come only from search snippets and are not verified:
  - the test uses Monte Carlo simulation, not real ETFs;
  - HRP has lower out-of-sample variance than Markowitz.
- The paper does not show a return advantage, and it is not a study of ETFs.
- Kipnis (2017) replicates the HRP weights in R and places HRP between unstable mean-variance and inverse volatility, but runs no comparative backtest.
- Two ETF-universe studies were seen only in search results and are not cited: a 2025 Central European University thesis on 30 US ETFs, and Kaucic and Valentinuz (2018) on 56 ETFs listed in Italy.

**8.2 How investors use ETFs.**
- Bhattacharya, Loos, Meyer and Hackethal (2017, *Review of Finance*, not *Review of Financial Studies*) study 6,949 clients of a German broker in 2005 to 2010, of whom 1,080 traded ETFs.
- Adopting ETFs did not improve portfolios, even before trading costs.
- The HKUST summary attributes the loss mainly to poor timing and to choosing narrow sector and country ETFs. No investor group lost by holding cheap, broadly diversified ETFs.

**8.3 ETF strategists and managed ETF portfolios.**
- In 2014 the SEC settled with F-Squared (AlphaSector) for USD 35 million, as reported by *Financial Advisor*.
- The 2001 to 2008 track record was a backtest of an algorithm that only existed from September 2008. A signal-timing error inflated the hypothetical results by about 350%.
- This is the clearest practitioner warning against marketing an optimized ETF strategy on in-sample results.
- Morningstar's ETF managed portfolio landscape reports were seen only in snippets and are not cited.

**8.4 Robo-advisors.**
- D'Acunto, Prabhala and Rossi (2019, *Review of Financial Studies*; opened as CESifo WP 6907):
  - investors who held fewer than 5 stocks before adopting the robo-advisor gained diversification, lower volatility and better performance;
  - investors who held more than 10 stocks gained little and traded more.
- The optimizer studied allocates across stocks, not ETFs.
- Betterment's public methodology (2026), a primary practitioner source:
  - runs mean-variance on equilibrium returns obtained by reverse optimization from the global market portfolio, blended with forecasts from large asset managers;
  - averages maximum-Sharpe weights over thousands of simulated 15-year samples (a form of resampling);
  - caps deviations from an ACWI IMI benchmark.
- Betterment's design amounts to optimization anchored on the broad world portfolio rather than on historical means.

**8.5 The Brazilian investor: vehicles and tax.**
- State Street (Huang, 2026): an Irish UCITS ETF generally suffers 15% US dividend withholding at fund level under the US-Ireland treaty. A US-listed ETF is often withheld at 30% at the investor level when no treaty applies. UCITS ETFs trade with lower on-screen liquidity and wider spreads. The article does not address US estate tax.
- B3 Bora Investir (updated 2024-01-10) describes the rules for B3-listed equity ETFs and BDRs of ETFs:
  - capital gains are taxed at 15% (20% for day trades), assessed monthly, with no exemption threshold;
  - dividends from BDRs of US ETFs bear 30% US withholding, IOF and depositary fees, and go to the Carnê-Leão with a credit for the US tax.
- The B3 page predates the effects of Law 14.754/2023 on individuals. The law's text could not be opened, so the 15% annual regime for offshore holdings is **not verified** here.
- ETFs Brasil comparison page: the B3-listed world fund VWRA11 (launched 2025-09-30) charges 0.52% a year and holds the Vanguard FTSE All-World UCITS ETF. The S&P 500 feeder IVVB11 charges 0.23%. A single world fund is therefore available on B3, but at more than twice the fee of the S&P 500 feeder.

**Agreement and disagreement.** The sources agree that unconstrained optimizers are unstable and that investor behavior (timing, narrow funds) destroys more value than weighting choices add. They differ in remedy: López de Prado proposes HRP, while Betterment anchors mean-variance on market weights and resamples. Neither offers verified evidence of beating equal weight or one world ETF out of sample after costs.

**What this justifies for the three-block portfolio.** It supports a growth sleeve of broad, low-cost ETFs, an optimizer anchored on the world portfolio with tight bounds, and a strict ban on presenting backtests as track records. For a BRL investor it makes the choice of vehicle (UCITS, US-listed, B3 feeder) a first-order fee and tax decision. Whether the optimizer beats equal weight remains unproven.

---

## 9. Practitioner and non-academic views on portfolio optimization

**Claim.** The practitioner sources that could be verified share the academic diagnosis: expected returns are the weak input, not the optimizer. They answer with risk-based methods, market-anchored inputs, constraints, and careful rebalancing. None shows an optimizer beating a simple market-anchored portfolio.

**Sources and how they compare**
- **Open-source tools.**
  - PyPortfolioOpt documentation (Robert Martin) warns that poor expected-return estimates can do more harm than good. It advises investing effort in the risk model and offers Black-Litterman.
  - Riskfolio-Lib documentation (Dany Cajas) supports HRP, HERC, NCO, risk parity and Black-Litterman. Its warnings are mostly about solvers.
- **Portfolio Visualizer.** Its optimizer page states that the result does not predict which allocation will do best outside the chosen period. In practice it is an in-sample tool.
- **Risk parity.** Bridgewater's "The All Weather Story" (2012) balances risk across four growth and inflation regimes so that no forecast of the regime is needed. It is the practitioner root of risk parity.
- **Rebalancing timing.**
  - Newfound Research (Hoffstein, 2013): changing only the day of the month of rebalancing moved the maximum drawdown of a 10-month moving-average rule on SPY from 19.03% to 30.22%. Spreading the rebalance over the month removed this dependence with little extra turnover.
  - Newfound (Hoffstein, 2019): semiannually rebalanced smart-beta portfolios showed 100 to 400 bps of dispersion from rebalance date alone.
- **Equal weight.** Rational Reminder episode 394 (Felix, Bortolotti, Wilson, 2026-01-29) concerns 1/N across *stocks*, not across asset-class ETFs:
  - equal-weight S&P 500 funds beat cap weight in backtests since 1971 but trailed in live funds over the last 10 years;
  - the hosts attribute the gap to size and value tilts with negative momentum;
  - turnover is about 10 times that of cap weight.
- **Asset-allocation comparisons.** Meb Faber's *Global Asset Allocation* (2015) compares 60/40, risk parity, the Permanent Portfolio, the global market portfolio and endowment-style allocations. Only the launch page was opened; the book's conclusion is not verified.
- **YouTube.** Titles and channels were confirmed through YouTube's oEmbed endpoint, but descriptions and transcripts were not accessible. Their content is reviewed in the [lectures and talks annex](../resources/literature-review-02.md):
  - two explainers from the Finance Research Gate channel, on HRP and on risk parity;
  - a Lead-Lag Media episode on risk parity;
  - a Cornell Financial Engineering Manhattan seminar by López de Prado on why machine-learning funds fail;
  - from Brazil: BTG Pactual's "Investindo pelo Mundo" on UCITS ETFs, and Abner Araujo comparing IVV and VT.

**Agreement and disagreement.** Practitioners agree with DeMiguel et al. (2009) that estimation error dominates and that in-sample optima do not transfer. They split on the remedy:
- tool builders promote HRP and risk parity, without verified out-of-sample wins over 1/N;
- Betterment anchors on the market portfolio and resamples;
- Rational Reminder treats equal weight among stocks as a costly factor bet.

No verified practitioner source engages with Kritzman et al. (2010).

**What this justifies for the three-block portfolio.** Five practices follow:
- replace historical means with equilibrium or anchored inputs;
- bound weights and turnover;
- report the optimizer's results as descriptive, not predictive;
- spread rebalancing over time or use bands to reduce timing luck;
- keep 1/N across ETFs distinct from 1/N across stocks.

It does not justify claiming that any of these methods will outperform.

---

## References

- Becker, F., Gürtler, M., Hibbeln, M. (2015). Markowitz versus Michaud: Portfolio Optimization Strategies Reconsidered. *European Journal of Finance* 21(4), 269-291. https://ideas.repec.org/a/taf/eurjfi/v21y2015i4p269-291.html
- Bessembinder, H. (2018). Do Stocks Outperform Treasury Bills? *Journal of Financial Economics*. Secondary page opened (ASU W. P. Carey news, 2018-09-17): https://news.wpcarey.asu.edu/20180917-do-stocks-outperform-treasury-bills
- Black, F. (1989). Universal Hedging: Optimizing Currency Risk and Reward in International Equity Portfolios. *Financial Analysts Journal* 45(4). https://rpc.cfainstitute.org/research/financial-analysts-journal/1989/universal-hedging-optimizing-currency-risk-and-reward-in-international-equity-portfolios
- BlackRock (2026). iShares LifePath Target Date 2035 ETF (ITDC) fact sheet, as of 2026-06-30. https://www.ishares.com/us/literature/fact-sheet/itdc-ishares-lifepath-target-date-2035-etf-fund-fact-sheet-en-us.pdf
- Brennan, M. J., Xia, Y. (2002). Dynamic Asset Allocation under Inflation. *Journal of Finance* 57(3), 1201-1238. https://ideas.repec.org/a/bla/jfinan/v57y2002i3p1201-1238.html
- Brown, S. J., Goetzmann, W. N., Liang, B. (2002). Fees on Fees in Funds of Funds. NYU Stern Working Paper FIN-02-031. https://archive.nyu.edu/handle/2451/26475
- Campbell, J. Y., Serfaty-de Medeiros, K., Viceira, L. M. (2010). Global Currency Hedging. *Journal of Finance* 65(1), 87-121. Opened as NBER WP 13088: https://www.nber.org/papers/w13088
- Campbell, J. Y., Shiller, R. J., Viceira, L. M. (2009). Understanding Inflation-Indexed Bond Markets. *Brookings Papers on Economic Activity*, Spring 2009. https://www.brookings.edu/articles/understanding-inflation-indexed-bond-markets/
- Campbell, J. Y., Viceira, L. M. (2001). Who Should Buy Long-Term Bonds? *American Economic Review* 91(1), 99-127. https://www.aeaweb.org/articles?id=10.1257/aer.91.1.99
- Carhart, M. M. (1997). On Persistence in Mutual Fund Performance. *Journal of Finance* 52(1), 57-82. https://forrt.org/flora-replication-atlas/doi/10.1111/j.1540-6261.1997.tb03808.x/
- Das, S., Markowitz, H., Scheid, J., Statman, M. (2010). Portfolio Optimization with Mental Accounts. *Journal of Financial and Quantitative Analysis* 45(2), 311-334. https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p311-334_00.html
- Daryanani, G. (2008). Opportunistic Rebalancing: A New Paradigm for Wealth Managers. *Journal of Financial Planning*, January 2008. https://www.financialplanningassociation.org/article/journal/JAN08-opportunistic-rebalancing-new-paradigm-wealth-managers
- DeMiguel, V., Garlappi, L., Uppal, R. (2009). Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy? *Review of Financial Studies* 22(5), 1915-1953. https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901
- Fama, E. F., French, K. R. (2010). Luck versus Skill in the Cross-Section of Mutual Fund Returns. *Journal of Finance* 65(5), 1915-1947. https://ideas.repec.org/a/bla/jfinan/v65y2010i5p1915-1947.html
- Funds Society (2025-10-29). Report on SPIVA Latin America Mid-Year 2025 (secondary source for S&P DJI data). https://www.fundssociety.com/br/news/os-fundos-ativos-do-brasil-e-do-chile-superaram-o-indice-de-referencia-no-primeiro-semestre/
- Harvey, C. R., Liu, Y., Zhu, H. (2016). ...and the Cross-Section of Expected Returns. *Review of Financial Studies* 29(1), 5-68. https://ideas.repec.org/a/oup/rfinst/v29y2016i1p5-68..html
- Hou, K., Xue, C., Zhang, L. (2020). Replicating Anomalies. *Review of Financial Studies* 33(5), 2019-2133. https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2019-2133..html
- Huang, S., Song, Y., Xiang, H. (2020). The Smart Beta Mirage. SSRN working paper. Secondary page opened (InvestmentNews): https://www.investmentnews.com/smart-beta-funds-dont-live-up-backtesting-196778
- ICFS. SPIVA scorecard results (secondary source for SPIVA U.S. Year-End 2024). https://icfs.com/specialists-desk/spiva-scorecard-results
- Israel, R., Moskowitz, T. J. (2013). The Role of Shorting, Firm Size, and Time on Market Anomalies. *Journal of Financial Economics* 108(2), 275-301. https://ideas.repec.org/a/eee/jfinec/v108y2013i2p275-301.html
- Jaconetti, C. M., Kinniry, F. M., Jr., Zilbering, Y. (2010). Best Practices for Portfolio Rebalancing. Vanguard Research. Third-party copy opened: https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241
- Jagannathan, R., Ma, T. (2003). Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps. *Journal of Finance* 58(4), 1651-1684. Opened as NBER WP 8922: https://nber.org/papers/w8922
- Kirby, C., Ostdiek, B. (2012). It's All in the Timing: Simple Active Portfolio Strategies that Outperform Naive Diversification. *Journal of Financial and Quantitative Analysis* 47(2), 437-467. https://ideas.repec.org/a/cup/jfinqa/v47y2012i02p437-467_00.html
- Kothari, S. P., Shanken, J. (2004). Asset Allocation with Inflation-Protected Bonds. *Financial Analysts Journal* 60(1). https://rpc.cfainstitute.org/research/financial-analysts-journal/2004/asset-allocation-with-inflation-protected-bonds
- Kritzman, M., Page, S., Turkington, D. (2010). In Defense of Optimization: The Fallacy of 1/N. *Financial Analysts Journal* 66(2), 31-39. https://ideas.repec.org/a/taf/ufajxx/v66y2010i2p31-39.html
- Ledoit, O., Wolf, M. (2003). Honey, I Shrunk the Sample Covariance Matrix. UPF Economics Working Paper 691. https://ideas.repec.org/p/upf/upfgen/691.html
- Markowitz, H. (1952). Portfolio Selection. *Journal of Finance* 7(1), 77-91. Metadata page opened: https://econpapers.repec.org/RAS/pma73.htm
- McLean, R. D., Pontiff, J. (2016). Does Academic Research Destroy Stock Return Predictability? *Journal of Finance* 71(1), 5-32. Metadata page only: https://ideas.repec.org/a/bla/jfinan/v71y2016i1p5-32.html
- Novy-Marx, R., Velikov, M. (2016). A Taxonomy of Anomalies and Their Trading Costs. *Review of Financial Studies* 29(1), 104-147. https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html
- Perold, A. F., Schulman, E. C. (1988). The Free Lunch in Currency Hedging: Implications for Investment Policy and Performance Standards. *Financial Analysts Journal* 44(3). https://rpc.cfainstitute.org/research/financial-analysts-journal/1988/the-free-lunch-in-currency-hedging-implications-for-investment-policy-and-peformance-standards
- B3 Bora Investir. Gestão ativa enfrenta desafio persistente para superar o mercado (secondary source for SPIVA Latin America). https://borainvestir.b3.com.br/tipos-de-investimentos/renda-variavel/fundos-investimento/gestao-ativa-enfrenta-desafio-persistente-para-superar-o-mercado/
- Schmittmann, J. M. (2010). Currency Hedging for International Portfolios. IMF Working Paper 10/151. https://ideas.repec.org/p/imf/imfwpa/2010-151.html
- Vanguard (2026). The FX Dimension: Evaluating Currency Hedging for Global Multi-Asset Portfolios. Vanguard Research. https://www.vanguard.co.uk/professional/research/the-fx-dimension-evaluating-currency-hedging-for-global-multi-asset-portfolios
- Willenbrock, S. (2011). Diversification Return, Portfolio Rebalancing, and the Commodity Return Puzzle. *Financial Analysts Journal* 67(4), 42-49. Opened on arXiv: https://arxiv.org/abs/1109.1256

### References added in the second pass (Themes 8 and 9)

- Betterment (2026, updated 2026-06-15). Betterment Portfolio Strategy. Betterment Resources. https://www.betterment.com/resources/betterment-portfolio-strategy
- Bhattacharya, U., Loos, B., Meyer, S., Hackethal, A. (2017). Abusing ETFs. *Review of Finance* 21(3), 1217-1250. https://ideas.repec.org/a/oup/revfin/v21y2017i3p1217-1250..html (summary: https://bm.hkust.edu.hk/bizinsight/2018/08/poor-timing-and-heavy-hand-undermine-benefits-etfs)
- B3 Bora Investir (2022, updated 2024-01-10). Como ficam os impostos para investimentos em ETFs e BDRs? https://borainvestir.b3.com.br/tipos-de-investimentos/renda-variavel/etfs/tributacao-etf-e-bdr/
- Bridgewater Associates (2012). The All Weather Story. https://www.bridgewater.com/research-and-insights/the-all-weather-story
- Cajas, D. Riskfolio-Lib documentation (v7.4). https://riskfolio-lib.readthedocs.io/en/latest/
- D'Acunto, F., Prabhala, N., Rossi, A. G. (2019). The Promises and Pitfalls of Robo-Advising. *Review of Financial Studies* 32(5). Opened as CESifo Working Paper 6907 (2018): https://www.ifo.de/en/cesifo/publications/2018/working-paper/promises-and-pitfalls-robo-advising
- ETFs Brasil. Comparador IVVB11 vs VWRA11. https://www.etfsbrasil.com.br/comparador/ivvb11/vwra11
- Faber, M. (2015). Global Asset Allocation (book launch page). mebfaber.com. https://mebfaber.com/global-asset-allocation/
- Felix, B., Bortolotti, D., Wilson, B. (2026-01-29). Episode 394: Equal Weight vs. Market Cap Weight Index Funds. *Rational Reminder* podcast. https://rationalreminder.ca/podcast/394
- Hoffstein, C. (2013-08-07). The Luck of the Rebalance Timing. Newfound Research blog. https://blog.thinknewfound.com/2013/08/the-luck-of-the-rebalance-timing/
- Hoffstein, C. (2019-11-18). The Dumb (Timing) Luck of Smart Beta. Newfound Research blog. https://blog.thinknewfound.com/2019/11/the-dumb-timing-luck-of-smart-beta/
- Huang, D. (2026-06-02). Considerations for non-US investors: US ETFs vs Irish UCITS. State Street Investment Management. https://www.ssga.com/us/en/institutional/insights/considerations-for-non-us-investors-us-etfs-vs-irish-ucits
- Kipnis, I. (2017-05-22). The Marcos Lopez de Prado Hierarchical Risk Parity Algorithm. QuantStrat TradeR via R-bloggers. https://www.r-bloggers.com/2017/05/the-marcos-lopez-de-prado-hierarchical-risk-parity-algorithm/amp/
- Martin, R. PyPortfolioOpt documentation: Expected Returns. https://pyportfolioopt.readthedocs.io/en/latest/ExpectedReturns.html
- Portfolio Visualizer. Optimize Portfolio (tool page). https://www.portfoliovisualizer.com/optimize-portfolio
- Schlegel, J. (2014-12-22). F-Squared Slammed By SEC Over False Performance Claims. *Financial Advisor*. https://www.fa-mag.com/news/f-squared-slammed-by-sec-over-false-performance-claims-20256.html
- YouTube videos (content reviewed in the [lectures and talks annex](../resources/literature-review-02.md)): Finance Research Gate, "Hierarchical Risk Parity HRP Portfolio Optimization", https://www.youtube.com/watch?v=_OPDNwtubZg ; Finance Research Gate, "Risk Parity Portfolio Optimization Explained Equal Risk Contributions in Practice", https://www.youtube.com/watch?v=aIJ9MM7I9kw ; Lead-Lag Media, "Stagflation Is Back: How Risk Parity Actually Works in 2026", https://www.youtube.com/watch?v=UkTDKOQO_2A ; Cornell Financial Engineering Manhattan, "Marcos Lopez de Prado: The 7 Reasons Most Machine Learning Funds Fail", https://www.youtube.com/watch?v=npA8sI-k328 ; BTG Pactual, "ETFs UCITS: como investir no exterior pagando menos imposto", https://www.youtube.com/watch?v=unQ4CCrmL30 ; Abner Araujo, "IVV ou VT: Qual o Melhor ETF para Investir no Exterior", https://www.youtube.com/watch?v=RJbQe-cQnrM

## Not found

Second pass:
- **ETF universes.** No peer-reviewed study of mean-variance, maximum Sharpe or Black-Litterman on sector or country ETFs vs. equal weight with costs.
- **HRP.** The full text of López de Prado (2016) could not be read.
- **ETF costs.** No verified literature on ETF tracking error, total cost or holdings overlap.
- **Managed portfolios and robo-advisors.** Morningstar's ETF managed portfolio reports and Wealthfront's methodology (404) were not opened.
- **Law 14.754/2023.** Official text not opened; the Planalto site failed.
- **US estate tax.** No IRS source opened for non-resident investors.
- **Practitioner sources.** Bogleheads wiki (403); Patrick Boyle (no attributable video found); QuantStart and Quantopian lectures; any practitioner source citing Kritzman et al. (2010).
- **YouTube.** Transcripts were not accessible in this pass. Video content is reviewed in the [lectures and talks annex](../resources/literature-review-02.md).

First pass:

- **SPIVA primary reports.** All S&P DJI pages returned HTTP 403; figures come only from secondary pages. The exact 15-year US figure is not verified.
- **Bessembinder (2018).** The journal page was not opened; the venue and the exact figures rest on a university news page.
- **McLean and Pontiff (2016).** The decay figures were not verified on an opened page.
- **Michaud resampling.** No primary source was opened.
- **Factor-specific ETFs.** No study isolating quality ETFs or dividend ETFs after launch was verified; the Research Affiliates "backtest vs. live" piece was blocked.
- **Campbell and Viceira (2002), *Strategic Asset Allocation*.** Seen in search only.
- **Inflation-linked bonds.** No formal model linking the optimal indexed-bond weight to the level of the real yield; no academic study of NTN-B / Tesouro IPCA+ allocation; no LDI source.
- **Currency.** No peer-reviewed study of BRL co-movement with global equities from a Brazilian investor's perspective.
- **Rebalancing.** Vanguard 2022 "Rational rebalancing" (broken links); the Vanguard section on rebalancing with new cash first; Masters (2003); Donohue and Yip (2003); Leland (1999); the replication of Daryanani.
- **Funds of ETFs.** Chhabra (2005), Brunel, Evensky, Morningstar bucket research, robo-advisor whitepapers, Vanguard LifeStrategy, the published version of Brown et al., and Ang et al. on fund-of-funds fees were not opened. No Brazilian fund-of-ETFs source was found (the CVM Resolution 175 text was not read).
- **Close match.** No published fund combines a cash floor, a capped inflation-linked sleeve and an optimizer-weighted ETF growth sleeve.
