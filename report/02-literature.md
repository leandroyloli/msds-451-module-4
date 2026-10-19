# Literature review

> **AI-generated.** This review was prepared with AI research agents and edited by me. A source is cited only if its page or video was opened. The full notes are in two annexes: [academic and practitioner sources](../resources/literature-review.md) and [lectures and talks](../resources/literature-review-02.md).

The question is narrow. Who has studied a portfolio made of ETFs? And when someone held those ETFs in an optimized proportion, did the mix beat a simple alternative on data the rule had not seen? Trading rules such as trend following and technical analysis were outside this search, because the growth fund does not time markets.

## The short answer

- **Holding ETFs instead of picking companies is well supported.**
- **Optimizing the weights is not.** An optimizer fed with past average returns rarely beats equal weight out of sample.
- **Portfolios of ETFs exist, but this three-block design does not.**

## Optimized weights against equal weight

This is the core of the project, and the sources disagree.

| Side | Who | What they found |
| --- | --- | --- |
| Equal weight is hard to beat | DeMiguel, Garlappi and Uppal (2009) | None of 14 optimizers beat equal weight consistently, across 7 datasets. Errors in the estimated returns swamp the gains. |
| Optimization can win | Kritzman, Page and Turkington (2010) | With long samples, simple return assumptions, or minimum variance, optimized portfolios beat equal weight out of sample. |
| Optimization can win | Kirby and Ostdiek (2012) | Low-turnover strategies beat equal weight even after high costs. |
| Risk is the useful input | Jagannathan and Ma (2003); Ledoit and Wolf (2003) | A long-only constraint, or shrinking the covariance matrix, makes the optimizer more stable. |
| Cluster methods | López de Prado (2016; talk, 2024) | Hierarchical risk parity and related methods cut estimation error sharply in Monte Carlo simulations. A small real-data test shown on YouTube (Finance Research Gate 2026) found minimum variance doing better. |

**Where the sources agree.** The weak input is the expected return, not the optimizer.

**Where they disagree.** How much a careful optimizer can recover.

Practitioners say the same thing more plainly. The PyPortfolioOpt documentation warns that poor return estimates can do more harm than good. Betterment, which runs portfolios of ETFs for retail clients, does not optimize on past averages. It starts from the world market portfolio and keeps weights close to a world benchmark.

**The gap.** None of these studies tests a universe of ETFs against one world ETF, after fees. That is the comparison this project makes.

## Who has built a portfolio of ETFs

| Who | What it is | How close to this design |
| --- | --- | --- |
| iShares LifePath ETFs (BlackRock) | An active ETF that holds only iShares ETFs, with no fee on top of theirs | Closest in structure. But the weights follow a date, not an optimizer, and there is no safety or inflation block |
| Betterment | A portfolio of ETFs per client, with a market-anchored optimizer | Close in method. Built for a US investor |
| Robo-advisors (D'Acunto, Prabhala and Rossi 2019) | Automated portfolios for retail clients | Poorly diversified investors gained. Diversified ones traded more without gaining |
| Goal-based investing (Das, Markowitz, Scheid and Statman 2010) | Separate accounts, each with its own goal and risk limit | The closest idea in theory: splitting wealth into jobs can still be efficient |
| F-Squared (SEC case, 2014) | Tactical ETF portfolios sold to advisers | A warning. The track record was a backtest, and the firm paid USD 35 million to settle |

Three warnings apply to any portfolio of ETFs:

- **Fees.** A fund of funds can stack two layers of fees (Brown, Goetzmann and Liang 2002).
- **Behavior.** Investors lost by timing trades and buying narrow ETFs. Broad, cheap ETFs hurt no one (Bhattacharya, Loos, Meyer and Hackethal 2017).
- **Wrapper.** An Irish UCITS ETF usually pays 15 percent US withholding on dividends, against 30 percent for a US-listed ETF (Huang 2026).

## What else the literature supports

| Theme | Finding | Sources | Meaning for this portfolio |
| --- | --- | --- | --- |
| Stock picking | 84 to 91 percent of active equity funds trail their index over ten years, in the United States and in Brazil | SPIVA scorecards; Fama and French (2010); Bessembinder (2018) | Hold index ETFs, not companies |
| Factor ETFs | Backtests overstate returns. Smart-beta indexes beat the market by 2.77 percent a year before listing and trailed it by 0.44 percent after | Huang, Song and Xiang (2020); Hou, Xue and Zhang (2020); Novy-Marx and Velikov (2016) | Judge factor ETFs on their live record only |
| Inflation | For a long-horizon investor, a bond that pays inflation plus a real rate is the safe asset | Campbell and Viceira (2001); Kothari and Shanken (2004) | NTN-B matched to dated spending |
| Currency | The dollar tends to rise when world stocks fall | Campbell, Serfaty-de Medeiros and Viceira (2010) | Foreign equities unhedged for someone who spends in reais. Not yet tested on the real |
| Rebalancing | Rebalancing controls risk. It does not reliably add return, and the date chosen changes results | Jaconetti, Kinniry and Zilbering (2010); Hoffstein (2013) | Monthly check, bands, new money first, several start dates |

## What the literature does not answer

- Whether an optimized portfolio of ETFs beats equal weight and one world ETF, after fees, out of sample.
- How the real behaves against world equities, from a Brazilian investor's point of view.
- How the Brazilian tax law for offshore investments (Law 14.754/2023) applies. The text was not verified.

## References

- Bessembinder, H. (2018). Do stocks outperform Treasury bills? *Journal of Financial Economics*. [Summary](https://news.wpcarey.asu.edu/20180917-do-stocks-outperform-treasury-bills)
- Betterment (2026). Betterment portfolio strategy. [Link](https://www.betterment.com/resources/betterment-portfolio-strategy)
- Bhattacharya, U., Loos, B., Meyer, S. and Hackethal, A. (2017). Abusing ETFs. *Review of Finance* 21(3). [Link](https://ideas.repec.org/a/oup/revfin/v21y2017i3p1217-1250..html)
- BlackRock (2026). iShares LifePath Target Date 2035 ETF, fact sheet. [Link](https://www.ishares.com/us/literature/fact-sheet/itdc-ishares-lifepath-target-date-2035-etf-fund-fact-sheet-en-us.pdf)
- Brown, S. J., Goetzmann, W. N. and Liang, B. (2002). Fees on fees in funds of funds. NYU Stern working paper. [Link](https://archive.nyu.edu/handle/2451/26475)
- Campbell, J. Y., Serfaty-de Medeiros, K. and Viceira, L. M. (2010). Global currency hedging. *Journal of Finance* 65(1). [Link](https://www.nber.org/papers/w13088)
- Campbell, J. Y. and Viceira, L. M. (2001). Who should buy long-term bonds? *American Economic Review* 91(1). [Link](https://www.aeaweb.org/articles?id=10.1257/aer.91.1.99)
- D'Acunto, F., Prabhala, N. and Rossi, A. G. (2019). The promises and pitfalls of robo-advising. *Review of Financial Studies* 32(5). [Link](https://www.ifo.de/en/cesifo/publications/2018/working-paper/promises-and-pitfalls-robo-advising)
- Das, S., Markowitz, H., Scheid, J. and Statman, M. (2010). Portfolio optimization with mental accounts. *Journal of Financial and Quantitative Analysis* 45(2). [Link](https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p311-334_00.html)
- DeMiguel, V., Garlappi, L. and Uppal, R. (2009). Optimal versus naive diversification. *Review of Financial Studies* 22(5). [Link](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901)
- Fama, E. F. and French, K. R. (2010). Luck versus skill in the cross-section of mutual fund returns. *Journal of Finance* 65(5). [Link](https://ideas.repec.org/a/bla/jfinan/v65y2010i5p1915-1947.html)
- Finance Research Gate (2026). Hierarchical risk parity HRP portfolio optimization. YouTube. [Link](https://www.youtube.com/watch?v=_OPDNwtubZg)
- Hoffstein, C. (2013). The luck of the rebalance timing. Newfound Research. [Link](https://blog.thinknewfound.com/2013/08/the-luck-of-the-rebalance-timing/)
- Hou, K., Xue, C. and Zhang, L. (2020). Replicating anomalies. *Review of Financial Studies* 33(5). [Link](https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2019-2133..html)
- Huang, D. (2026). Considerations for non-US investors: US ETFs vs Irish UCITS. State Street Investment Management. [Link](https://www.ssga.com/us/en/institutional/insights/considerations-for-non-us-investors-us-etfs-vs-irish-ucits)
- Huang, S., Song, Y. and Xiang, H. (2020). The smart beta mirage. SSRN working paper. [Summary](https://www.investmentnews.com/smart-beta-funds-dont-live-up-backtesting-196778)
- Jaconetti, C. M., Kinniry, F. M. and Zilbering, Y. (2010). Best practices for portfolio rebalancing. Vanguard Research. [Link](https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241)
- Jagannathan, R. and Ma, T. (2003). Risk reduction in large portfolios. *Journal of Finance* 58(4). [Link](https://nber.org/papers/w8922)
- Kirby, C. and Ostdiek, B. (2012). It's all in the timing. *Journal of Financial and Quantitative Analysis* 47(2). [Link](https://ideas.repec.org/a/cup/jfinqa/v47y2012i02p437-467_00.html)
- Kothari, S. P. and Shanken, J. (2004). Asset allocation with inflation-protected bonds. *Financial Analysts Journal* 60(1). [Link](https://rpc.cfainstitute.org/research/financial-analysts-journal/2004/asset-allocation-with-inflation-protected-bonds)
- Kritzman, M., Page, S. and Turkington, D. (2010). In defense of optimization: The fallacy of 1/N. *Financial Analysts Journal* 66(2). [Link](https://ideas.repec.org/a/taf/ufajxx/v66y2010i2p31-39.html)
- Ledoit, O. and Wolf, M. (2003). Honey, I shrunk the sample covariance matrix. UPF working paper 691. [Link](https://ideas.repec.org/p/upf/upfgen/691.html)
- López de Prado, M. (2016). Building diversified portfolios that outperform out of sample. *Journal of Portfolio Management* 42(4). Full text not opened.
- López de Prado, M. (2024). Machine learning in asset management. Kapitaleierdagen 2024, Reitan Kapital. YouTube. [Link](https://www.youtube.com/watch?v=fOCzNFwmM7Y)
- Novy-Marx, R. and Velikov, M. (2016). A taxonomy of anomalies and their trading costs. *Review of Financial Studies* 29(1). [Link](https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html)
- PyPortfolioOpt documentation. Expected returns. [Link](https://pyportfolioopt.readthedocs.io/en/latest/ExpectedReturns.html)
- Schlegel, J. (2014). F-Squared slammed by SEC over false performance claims. *Financial Advisor*. [Link](https://www.fa-mag.com/news/f-squared-slammed-by-sec-over-false-performance-claims-20256.html)
- S&P Dow Jones Indices. SPIVA U.S. and Latin America scorecards, via [ICFS](https://icfs.com/specialists-desk/spiva-scorecard-results) and [B3 Bora Investir](https://borainvestir.b3.com.br/tipos-de-investimentos/renda-variavel/fundos-investimento/gestao-ativa-enfrenta-desafio-persistente-para-superar-o-mercado/).
