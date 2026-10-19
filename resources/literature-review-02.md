# Literature review Argon 4: lectures and talks on a portfolio of ETFs

> **AI-generated.** Prepared with AI research agents (Argon 4) and edited by the author. Each claim was checked against the captions of its video on 2026-10-19, and the text was edited to match them. Formulas shown only on slides could not be checked.

---

## Context & Objectives

This literature review pass incorporates evidence extracted directly from verified video transcripts and lectures from quantitative researchers, institutional investors, and credentialed practitioners. It complements the academic papers in literature-review.md to address portfolio optimization for a managed portfolio serving a Brazilian investor who spends in BRL and has access to US-listed ETFs, Irish UCITS ETFs, and B3-listed ETFs. The portfolio under study has three blocks:

Safety: 12 months of spending in BRL cash and short-term bonds.

Inflation: Capped inflation-linked government bonds matched to liabilities.

Growth: A long-only ETF sleeve weighted by an optimizer seeking maximum return per unit of risk after fees, evaluated against equal weighting (1/N) and a single broad world equity index.

## 1. Out-of-Sample Optimization

### The Claim

Out-of-sample portfolio optimization is severely degraded by covariance matrix estimation error and matrix inversion (Σ⁻¹), which amplifies sample noise and creates radical weight instability across estimation windows. While naive equal weighting (1/N) eliminates parameter estimation error, it introduces high turnover, unintended sector bets, and negative momentum drag. Advanced structural techniques—such as Hierarchical Risk Parity (HRP), Equal Risk Contribution (ERC / Risk Parity), and Marchenko-Pastur covariance denoising—achieve superior out-of-sample stability and higher risk-adjusted returns without incurring the costs and momentum penalties of equal weighting.

### Verified Video Evidence

**Reitan Kapital — Prof. Marcos López de Prado, "Professor Marcos Lopez de Prado on Machine Learning in Asset Management - Kapitaleierdagen 2024" (2024-12-17) [https://www.youtube.com/watch?v=fOCzNFwmM7Y]:**

- Notes that standard Markowitz mean-variance optimization acts as an "error maximizer" due to high condition numbers in empirical covariance matrices.
- Demonstrates that applying the Marchenko-Pastur theorem from Random Matrix Theory to denoise covariance matrices yields a 94% reduction in mean squared error (MSE) for Maximum Sharpe portfolios in Monte Carlo trials.
- Identifies "signal-induced instability," showing that high correlation among assets shrinks the matrix determinant (det(Σ) = 1 − ρ²), causing extreme sensitivity in Σ⁻¹.
- Introduces Nested Cluster Optimization (NCO), which partitions the covariance matrix into blocks to isolate instability, reducing out-of-sample MSE by 47% to 55%.

**Finance Research Gate — "Hierarchical Risk Parity HRP Portfolio Optimization" (2026-02-15) [https://www.youtube.com/watch?v=_OPDNwtubZg]:**

- Details HRP tree clustering using a correlation-based distance.
- Explains cluster capital allocation using inverse variance portfolio (IVP) weights.
- Emphasizes that HRP bypasses full covariance matrix inversion.
- In a 4-asset empirical backtest (2000 to 2010, 12-month window, monthly rebalancing), the Minimum Variance Portfolio (MVP) achieved a higher out-of-sample Sharpe than HRP.

**Finance Research Gate — "Risk Parity Portfolio Optimization Explained Equal Risk Contributions in Practice" (2026-02-12) [https://www.youtube.com/watch?v=aIJ9MM7I9kw]:**

- Defines Equal Risk Contribution (ERC) where total risk contribution TRC_i = w_i · (Σw)_i / σ_p = σ_p / N.
- Notes that risk parity lacks a closed-form solution and must be solved iteratively.
- Demonstrates that Minimum Variance Portfolios suffer extreme weight flips across monthly rolling windows due to full matrix inversion (Σ⁻¹).
- Shows that risk parity achieves superior weight stability over time because it avoids full matrix inversion. In the same test, MVP had the higher out-of-sample return, with a similar Sharpe ratio.

**Ben Felix — "The Problem with Equal Weight Index Funds" (2026-01-25) [https://www.youtube.com/watch?v=xu7kMpLbJJs]:**

- Demonstrates that equal-weighted index funds display higher long-term volatility than cap-weighted equivalents.
- Highlights that equal-weighted funds generate average annual turnover >10 times higher than cap-weighted funds.
- Proves via multi-factor regression that equal weighting systematically trades against momentum, loading negatively on the Momentum factor (UMD < 0).

**Dimensional Fund Advisors — Mark Gochner, Jake DeKinder, Wes Krill, "The Death of the 60/40 Portfolio? | The Informed Investor 30" (2026-01-30) [https://www.youtube.com/watch?v=2NSlam-fxuo]:**

- Traces 60/40 origins to mean-variance optimization, noting that reducing equity exposure from 100% to 60% cuts worst-calendar-year drawdowns from ~-40% to ~-20% with minor return sacrifice.
- Shows that even when short-term stock-bond correlations fluctuate, adding fixed income delivers a flat, consistent variance reduction over long horizons.

### Agreement & Contradiction with Academic Sources (literature-review.md)

**DeMiguel, Garlappi and Uppal (2009):** The video evidence strongly supports the academic finding that parameter estimation error renders classic unconstrained mean-variance optimization unreliable out-of-sample. However, Ben Felix directly validates the downside of naive 1/N equal weighting highlighted in academic literature: its high turnover drag and negative momentum exposure (UMD < 0).

**Kritzman, Page and Turkington (2010) & Covariance Shrinkage:** López de Prado (Kapitaleierdagen 2024) reports, in Monte Carlo simulations, that Marchenko-Pastur denoising roughly doubles the error reduction of Ledoit-Wolf shrinkage for minimum variance (about 60 percent against 30 percent), and cuts the error of maximum-Sharpe portfolios by 94 percent. NCO adds a further 47 to 55 percent.

**Empirical vs. Simulation Discrepancies:** Finance Research Gate's 4-asset empirical backtest showed Minimum Variance beating HRP, whereas López de Prado's Monte Carlo simulations reported Sharpe gains above 31 percent for HRP. One small real-data test and one large simulation point in different directions.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies utilizing a cluster-based, noise-robust optimizer (such as HRP or NCO) for the Growth sleeve to allocate capital across ETF asset classes without relying on unstable full matrix inversions.

**What it does NOT justify:** Does NOT justify replacing the Growth sleeve with naive 1/N equal weighting (due to turnover and negative momentum drag), nor does it justify adding complex structured derivatives to the Safety or Inflation sleeves.

## 2. Marcos López de Prado Talks

### The Claim

Quantitative investment strategies frequently fail out-of-sample because conventional finance relies on flawed methodological practices: forced integer differentiation (d = 1), time-based sampling, arbitrary labeling, and uncorrected backtesting. Achieving sustainable out-of-sample alpha requires adopting machine learning architectures grounded in financial theory, including fractional differentiation to preserve memory, non-time sampling (dollar/volume bars), meta-labeling for bet sizing, causal factor selection via Directed Acyclic Graphs (DAGs), and strict backtest overfitting controls like the Deflated Sharpe Ratio (DSR).

### Verified Video Evidence

**Cornell Financial Engineering Manhattan (CFEM) — Marcos López de Prado, "The 7 Reasons Most Machine Learning Funds Fail" (2019-05-13) [https://www.youtube.com/watch?v=npA8sI-k328]:**

- Reason 1 (Sisyphus Paradigm): Siloed researchers working independently produce false discoveries; firms should operate collaborative "meta-strategy assembly lines."
- Reason 2 (Over-differentiation): Computing integer returns (d = 1) erases historical memory/signal. Fractional differentiation (d ∈ (0,1)) achieves stationarity while preserving memory.
- Reason 3 (Canonical Sampling): Time-based bars sample arbitrarily; dollar and volume bars synchronize sampling with information arrival.
- Reason 4 (Wrong Labeling): Standard fixed-horizon labeling ignores path risk. The triple barrier method and meta-labeling (secondary model deciding bet execution) optimize trade size and precision.
- Reason 5 (Non-i.i.d. Samples): Overlapping financial outcomes violate i.i.d. assumptions; sample uniqueness weights must be applied.
- Reason 6 (Cross-Validation Failure): Standard k-fold CV leaks future information; purged and embargoed cross-validation must be used.
- Reason 7 (Backtest Overfitting): Repeated backtesting generates inflated Sharpe ratios. The Deflated Sharpe Ratio (DSR) adjusts for N_trials, sample length, skewness, and kurtosis.

**Reitan Kapital — Prof. Marcos López de Prado, "Professor Marcos Lopez de Prado on Machine Learning in Asset Management - Kapitaleierdagen 2024" (2024-12-17) [https://www.youtube.com/watch?v=fOCzNFwmM7Y]:**

- Demonstrates hierarchical clustering on 5,000 corporate bonds, revealing 4 dominant risk clusters.
- Explains that HRP's tree structure requires only N − 1 observations, reducing historical data requirements from 5 years to 2 months and boosting out-of-sample Sharpe ratios by 31% in simulations.
- Outlines "corrective AI" (meta-labeling) to filter false positive signals generated by primary models or discretionary managers.
- Advocates "allocation to allocators" (bagging/ensembling multiple optimization algorithms) to eliminate single-optimizer point-of-failure risk.

**CFA Institute Research Foundation — Marcos López de Prado & Vincent Zoonekynd, "Causality in Factor Investing: Marcos López de Prado, PhD & Vincent Zoonekynd, PhD" (2026-01-20) [https://www.youtube.com/watch?v=NHQ0Q30fAP4]:**

- Attributes the "Factor Zoo" to P-hacking and brute-force regression trials without causal models.
- Distinguishes explanatory/causal factor models from predictive/forecasting models.
- Explains Collider Bias: controlling for colliders (effects of both cause and return) distorts beta signs, causing models to buy what should be sold.
- Notes that Granger causality measures precedence, not true physical/economic causality.
- Recommends causal discovery algorithms (PC algorithm, GES, LiNGAM) to build Directed Acyclic Graphs (DAGs) and isolate true upstream confounders from downstream colliders.

### Agreement & Contradiction with Academic Sources (literature-review.md)

**Harvey, Liu and Zhu (2016) & P-Hacking:** López de Prado (CFEM; CFA Institute) directly reinforces academic findings on backtest overfitting. The Deflated Sharpe Ratio (DSR) provides a formal mathematical correction for the number of backtest iterations (N_trials) and non-Gaussian returns.

**Factor Zoo & Causal Econometrics:** López de Prado and Zoonekynd (CFA Institute) argue that regressions without a causal graph can suffer from collider bias, which can flip the sign of a factor.

**Structural Optimization (HRP & NCO):** López de Prado (Reitan Kapital) explains that the tree structure of HRP needs far less data than estimating every pairwise link, which he puts at about five years of history.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies grouping the Growth sleeve ETFs into hierarchical risk clusters (HRP/NCO) prior to weight allocation, and applying DSR screening when selecting factor tilt ETFs to avoid overfit backtests.

**What it does NOT justify:** Does NOT justify deploying unconstrained "black-box" price-prediction machine learning models, nor does it justify altering the Safety sleeve's fixed-income allocation based on short-term algorithmic signals.

## 3. Evidence-Based Practitioners

### The Claim

Evidence-based practitioners emphasize that broad market-cap weighted global equity indexing captures ~70% of available equity returns while eliminating single-country ruin risk and active management underperformance. Deviating from market-cap weighting via naive equal weighting or unconstrained tactical shifts introduces unwanted sector concentrations, transaction costs, and complexity without delivering net alpha after fees.

### Verified Video Evidence

**Ben Felix — "The Problem with Equal Weight Index Funds" (2026-01-25) [https://www.youtube.com/watch?v=xu7kMpLbJJs]:**

- Shows that index concentration fluctuates naturally over time and has no strong historical relationship with lower future market returns.
- Demonstrates that equal-weight funds derive historical outperformance from implicit tilts to Size (small-cap) and Value, not equal weighting magic.
- Identifies unintended sector distortions in equal-weighted funds (heavy tech underweight, industrial overweight).
- Argues that intentional, low-turnover factor funds (e.g., Dimensional US Core Equity) capture Size and Value premiums far more efficiently than naive equal weighting.

**Dimensional Fund Advisors — Mark Gochner, Jake DeKinder, Wes Krill, "The Death of the 60/40 Portfolio? | The Informed Investor 30" (2026-01-30) [https://www.youtube.com/watch?v=2NSlam-fxuo]:**

- Explains that combining stocks and bonds reduces portfolio volatility substantially while sacrificing minimal long-term return.
- Shows that 2022 was the only year since 1979 (47 years, Russell 3000 and Bloomberg US Aggregate) in which stocks and bonds fell together.
- Warns that "shiny object" products such as buffered ETFs can bring more complexity, less transparency and higher fees, without being clearly better.

**Otávio Paranhos — "Começando a Carteira GLOBAL do Zero: VT vale a pena?" (2020-09-12) [https://www.youtube.com/watch?v=iqz3OZo9nZQ]:**

- Cites return skewness data showing 40% of individual stocks deliver negative lifetime returns; only 4-7% of stocks drive all net market outperformance above Treasury bills.
- Claims that about 70 percent of returns come from market exposure, citing Fama and French.
- Highlights institutional adoption of neutral market-cap global indexing by Norges Bank Investment Fund (~$1T) and the US Federal Thrift Savings Plan (TSP).

**Abner Araujo — "IVV ou VT: Qual o Melhor ETF para Investir no Exterior" (2025-06-30) [https://www.youtube.com/watch?v=RJbQe-cQnrM]:**

- Cites SPIVA data showing >90% of active fund managers underperform the passive S&P 500 index over 15-year periods. (Note: Presenter provides consulting disclaimers for Portfel/Grupo Primo).
- Compares IVV (S&P 500) to VT (Vanguard Total World Stock), saying VT reduces single-country and local risk.

**Fabio Fares — "Conheça o VT: UM MUNDO INTEIRO EM UM ÚNICO ETF" (2025-09-10) [https://www.youtube.com/watch?v=mInrZVtLAsc]:**

- Outlines VT's tracking of the FTSE Global All Cap Index (~10,000 stocks across 48 countries).
- Explains market-cap weighting as an automatic, objective reflection of global corporate value.
- Proposes a core-satellite portfolio structure: 70% VT as global core, combined with fixed income (SLQD 15%), REITs (VNQ 10%), and small-cap value (AVUV 5%).

### Agreement & Contradiction with Academic Sources (literature-review.md)

**Fama and French & Market Factor:** Ben Felix agrees that size and value drive the excess return of equal weight, and shows that intentional factor funds get the same tilts with less turnover.

**Bessembinder (2018) & Equity Return Skewness:** Otávio Paranhos makes the same point as Bessembinder (2018), without naming him, pointing out that because equity returns are heavily right-skewed (driven by 4-7% of stocks), broad cap-weighted indexing (VT/VWRA) is essential to guarantee holding those rare winning stocks.

**SPIVA & Active Underperformance:** Abner Araujo corroborates Jensen (1968) and modern SPIVA literature on the persistent underperformance of active stock selection after fees.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies using a broad, low-cost global market-cap weighted ETF (e.g., VT or VWRA) as the core benchmark and foundational holding for the Growth sleeve.

**What it does NOT justify:** Does NOT justify paying high fees for complex active market-timing wrappers, nor does it justify replacing market-cap core holdings with naive equal weighting.

## 4. Factor ETFs After Launch

### The Claim

While backtested factor strategies and equal-weighted indexes show strong historical outperformance, live fund performance frequently deteriorates post-launch due to trading drag, high turnover, negative momentum interactions, and backtest overfitting. Systematic factor tilts (Size, Value, Profitability) offer legitimate expected return premiums, but must be implemented via intentional, low-turnover trade rules rather than rigid index rebalancing.

### Verified Video Evidence

**Ben Felix — "The Problem with Equal Weight Index Funds" (2026-01-25) [https://www.youtube.com/watch?v=xu7kMpLbJJs]:**

- Shows that equal-weight funds load positively on Size and Value factors, but trade systematically against Momentum.
- Highlights annual turnover >10x higher in equal-weight ETFs compared to cap-weighted ETFs, generating substantial transaction cost drag.
- Demonstrates that intentional factor implementations (e.g., Dimensional US Core Equity) achieve similar Size and Value factor loadings while controlling sector bets, managing momentum drag, and maintaining low turnover.

**CFA Institute Research Foundation — Marcos López de Prado & Vincent Zoonekynd, "Causality in Factor Investing: Marcos López de Prado, PhD & Vincent Zoonekynd, PhD" (2026-01-20) [https://www.youtube.com/watch?v=NHQ0Q30fAP4]:**

- Explains that factors found without a causal model are often false discoveries that fail out of sample.

**JP Azevedo — "Sobreposição de ETFs: quando fazer e quando não fazer na sua carteira" (2025-08-21) [https://www.youtube.com/watch?v=v8FOFtIjPWI]:**

- Explains that intentional ETF overlap (e.g., combining a cap-weighted core with a targeted Value ETF like VTV or Small-Cap Value like VIOV) is justified when targeting specific factor premiums.
- Warns against redundant core overlap (e.g., holding VT and VTI together, which results in 61% weight overlap without adding factor exposure).

### Agreement & Contradiction with Academic Sources (literature-review.md)

**McLean and Pontiff (2016) & Factor Decay:** López de Prado (CFA Institute) is consistent with the idea that many published factors fail out of sample, but neither video discusses decay after publication. Ben Felix shows that equal weighting carries negative momentum loading and high turnover.

**Jegadeesh and Titman (1993) & Momentum Interaction:** Ben Felix cites Jegadeesh and Titman (1993), showing that rigid equal-weight rebalancing acts as a negative momentum bet, creating an explicit drag on live performance.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies adding targeted, low-turnover factor tilt ETFs as satellite holdings in the Growth sleeve alongside a broad global core.

**What it does NOT justify:** Does NOT justify adding naive equal-weighted or unconstrained commercial smart beta ETFs that introduce high turnover and negative momentum drag.

## 5. Rebalancing

### The Claim

Rebalancing is primarily a risk-control mechanism designed to maintain target asset distributions, rather than a reliable source of excess return. Mandatory high-frequency calendar rebalancing introduces transaction costs and negative momentum exposure, whereas rebalancing via incoming cash flows or wide tolerance bands minimizes turnover, execution drag, and taxable capital gains.

### Verified Video Evidence

**Ben Felix — "The Problem with Equal Weight Index Funds" (2026-01-25) [https://www.youtube.com/watch?v=xu7kMpLbJJs]:**

- Shows that the rebalancing built into equal-weighted ETFs drives turnover more than 10 times higher than cap weighting.
- Demonstrates that frequent rebalancing forces funds to sell recent winners and buy recent losers, systematically penalizing momentum.

**Fabio Fares — "Conheça o VT: UM MUNDO INTEIRO EM UM ÚNICO ETF" (2025-09-10) [https://www.youtube.com/watch?v=mInrZVtLAsc]:**

- Explains that market-cap weighted global equity ETFs rebalance automatically as prices change, with nothing for the investor to do.

### Agreement & Contradiction with Academic Sources (literature-review.md)

**Rebalancing and momentum:** Ben Felix shows that rebalancing sells recent winners and buys recent losers, which costs return when momentum is strong.

**Cash-flow rebalancing:** No video in this review discusses rebalancing with new money; that support comes from the academic review.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies rebalancing across the Safety, Inflation, and Growth jobs primarily using incoming cash inflows, and employing wide tolerance bands (rather than calendar schedules) for internal Growth sleeve rebalancing.

**What it does NOT justify:** Does NOT justify frequent high-frequency calendar rebalancing within the Growth sleeve.

## 6. Brazilian Channels on Investing Abroad with ETFs

### The Claim

For a Brazilian resident spending in BRL, international ETF investing requires optimizing tax friction under Law 14.754/2023, eliminating US estate tax exposure, and choosing between US-listed ETFs (e.g., VT, IVV), Irish-domiciled UCITS ETFs (e.g., VWRA, IWDA), and B3 BDR wrappers (e.g., IVVB11, VWRA11). Irish UCITS ETFs avoid the US estate tax (up to 40 percent) and reduce US dividend withholding, and accumulating share classes reinvest dividends inside the fund. Global currency diversification protects BRL purchasing power over long horizons.

### Verified Video Evidence

**BTG Pactual — Carol, "ETFs UCITS: como investir no exterior pagando menos imposto | Investindo pelo Mundo" (2026-05-27) [https://www.youtube.com/watch?v=unQ4CCrmL30]:**

- Explains UCITS (European-regulated ETF) structural and tax benefits for non-US investors.
- Outlines US tax risks for non-residents: up to 30 percent dividend withholding and US estate tax (imposto sobre herança) up to 40 percent.
- Explains that Ireland-domiciled UCITS ETFs are not exposed to US estate tax.
- Details accumulating (acumulador) UCITS ETFs, which automatically reinvest dividends inside the fund and simplify Brazilian tax declarations. (Note: Content hosted by BTG Pactual promoting international brokerage services).

**Abner Araujo — "IVV ou VT: Qual o Melhor ETF para Investir no Exterior" (2025-06-30) [https://www.youtube.com/watch?v=RJbQe-cQnrM]:**

- Compares US-listed IVV to B3 wrapper IVVB11, noting that direct offshore ETF holdings offer lower expense ratios than local Brazilian wrappers. (Note: Presenter provides consulting disclaimers for Portfel/Grupo Primo).

**Fabio Fares — "Conheça o VT: UM MUNDO INTEIRO EM UM ÚNICO ETF" (2025-09-10) [https://www.youtube.com/watch?v=mInrZVtLAsc]:**

- Details VT's geographic breakdown (US ~64%, Europe ~14%, Pacific ~9%, Emerging ~10%).
- Identifies emerging market volatility (~10% allocation) and US concentration as key structural risks.

**Otávio Paranhos — "Começando a Carteira GLOBAL do Zero: VT vale a pena?" (2020-09-12) [https://www.youtube.com/watch?v=iqz3OZo9nZQ]:**

- Recommends Irish-domiciled UCITS ETFs (e.g., VWRA) via an international broker to reduce dividend taxes.
- Explains currency hedging dynamics: holding emerging market and global currency assets cushions BRL-spending investors against USD/BRL exchange rate swings.

**Papo de Bolsa — "Descubra o ETF VT: O ETF mais Coringa para o Investidor" (2025-01-04) [https://www.youtube.com/watch?v=Kjk8uPTMs1M]:**

- Notes VT holds ~9,974 companies worldwide across developed and emerging markets.
- Highlights how global diversification balances regional economic cycles.

**JP Azevedo — "Sobreposição de ETFs: quando fazer e quando não fazer na sua carteira" (2025-08-21) [https://www.youtube.com/watch?v=v8FOFtIjPWI]:**

- Uses ETF Research Center tool to demonstrate redundant overlap (e.g., SPY + QQQ = 51% overlap).
- Demonstrates that holding VT and VTI together results in 61 percent weight overlap; the two play the same role, so holding both adds nothing.

### Agreement & Contradiction with Academic Sources (literature-review.md)

**International Tax Drag & Estate Tax Risk:** BTG Pactual describes the 30 percent withholding and the estate tax risk of US-domiciled ETFs. The 15 percent rate inside Irish UCITS ETFs is documented by State Street (Huang 2026) in the academic review, not by these videos.

**Law 14.754/2023 (Offshore Taxation in Brazil):** No video in this review discusses the law. Otávio's video predates it. The tax treatment must be checked in the text of the law.

**B3 Wrappers vs. Offshore UCITS:** Abner Araujo notes that IVV charges a lower management fee than IVVB11.

### Implications for the Three-Block Portfolio

**What it justifies:** Justifies considering Irish-domiciled accumulating UCITS ETFs as the wrapper for foreign exposure, to avoid US estate tax and reduce dividend withholding. The tax effect under Law 14.754/2023 still needs to be checked. It justifies holding BRL-denominated short bonds (Safety) and inflation-linked bonds (Inflation) locally in Brazil, while holding the Growth sleeve offshore.

**What it does NOT justify:** Does NOT justify holding large amounts of US-domiciled ETFs without addressing US estate tax exposure, nor does it justify redundant ETF pairings (like holding VT and VTI together).

## Verified Reference List

**Abner Araujo**
Presenter: Abner Araujo (Investment Consultant)
Title: "IVV ou VT: Qual o Melhor ETF para Investir no Exterior"
Upload Date: June 30, 2025
URL: https://www.youtube.com/watch?v=RJbQe-cQnrM

**Ben Felix**
Presenter: Ben Felix (PWL Capital)
Title: "The Problem with Equal Weight Index Funds"
Upload Date: January 25, 2026
URL: https://www.youtube.com/watch?v=xu7kMpLbJJs

**BTG Pactual**
Presenter: Carol (BTG Pactual)
Title: "ETFs UCITS: como investir no exterior pagando menos imposto | Investindo pelo Mundo"
Upload Date: May 27, 2026
URL: https://www.youtube.com/watch?v=unQ4CCrmL30

**CFA Institute Research Foundation**
Presenters: Marcos López de Prado, PhD; Vincent Zoonekynd, PhD; Lada Moberg, PhD
Title: "Causality in Factor Investing: Marcos López de Prado, PhD & Vincent Zoonekynd, PhD"
Upload Date: January 20, 2026
URL: https://www.youtube.com/watch?v=NHQ0Q30fAP4

**Cornell Financial Engineering Manhattan (CFEM)**
Presenter: Marcos López de Prado, PhD
Title: "Marcos Lopez de Prado: The 7 Reasons Most Machine Learning Funds Fail"
Upload Date: May 13, 2019
URL: https://www.youtube.com/watch?v=npA8sI-k328

**Dimensional Fund Advisors**
Presenters: Mark Gochner, Jake DeKinder, Wes Krill
Title: "The Death of the 60/40 Portfolio? | The Informed Investor 30"
Upload Date: January 30, 2026
URL: https://www.youtube.com/watch?v=2NSlam-fxuo

**Fabio Fares**
Presenter: Fabio Fares
Title: "Conheça o VT: UM MUNDO INTEIRO EM UM ÚNICO ETF | ETFs | Investimento no Exterior"
Upload Date: September 10, 2025
URL: https://www.youtube.com/watch?v=mInrZVtLAsc

**Finance Research Gate**
Presenter: Finance Research Gate
Title: "Hierarchical Risk Parity HRP Portfolio Optimization"
Upload Date: February 15, 2026
URL: https://www.youtube.com/watch?v=_OPDNwtubZg

**Finance Research Gate**
Presenter: Finance Research Gate
Title: "Risk Parity Portfolio Optimization Explained Equal Risk Contributions in Practice"
Upload Date: February 12, 2026
URL: https://www.youtube.com/watch?v=aIJ9MM7I9kw

**JP Azevedo**
Presenter: JP Azevedo
Title: "Sobreposição de ETFs: quando fazer e quando não fazer na sua carteira"
Upload Date: August 21, 2025
URL: https://www.youtube.com/watch?v=v8FOFtIjPWI

**Otávio Paranhos**
Presenter: Otávio Paranhos
Title: "Começando a Carteira GLOBAL do Zero: VT vale a pena?"
Upload Date: September 12, 2020
URL: https://www.youtube.com/watch?v=iqz3OZo9nZQ

**Papo de Bolsa**
Presenter: Papo de Bolsa
Title: "Descubra o ETF VT: O ETF mais Coringa para o Investidor"
Upload Date: January 4, 2025
URL: https://www.youtube.com/watch?v=Kjk8uPTMs1M

**Reitan Kapital**
Presenter: Prof. Marcos López de Prado
Title: "Professor Marcos Lopez de Prado on Machine Learning in Asset Management - Kapitaleierdagen 2024"
Upload Date: December 17, 2024
URL: https://www.youtube.com/watch?v=fOCzNFwmM7Y

## Not Found / Content Not Verified

The following videos and specific topics mentioned in the search scope were filtered out, missing, or unavailable via video transcript tools, and were excluded from the review:

- Lead-Lag Media, "Stagflation Is Back: How Risk Parity Actually Works in 2026" (https://www.youtube.com/watch?v=UkTDKOQO_2A) — Filtered by YouTube API corpus restrictions; transcript content not verified.
- Patrick Boyle — No specific video transcripts retrieved for rebalancing or portfolio optimization.
- Corey Hoffstein (Newfound Research) — No specific video transcripts retrieved for rebalancing timing luck.
- Meb Faber — No specific video transcripts retrieved for asset allocation or tail risk.
- Ray Dalio / Bridgewater — No specific video transcripts retrieved for All Weather or Risk Parity.
- Alex Shahidi — No specific video transcripts retrieved.
