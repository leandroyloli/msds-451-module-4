# MSDS 451 — Module 4, Term Project Checkpoint A

Local text repository for the Checkpoint A research report. `report/checkpoint-a.html` is generated from the markdown. Rebuild it with `python render_report.py`.

## Layout

| Path | What it holds |
| --- | --- |
| `report/00-index.md` | The report in order, with a link to each section |
| `report/checkpoint-a.html` | The same report, rendered. Rebuild with `python render_report.py` |
| `report/01-introduction.md` | A managed portfolio with three blocks, and a fund of ETFs for growth |
| `report/02-literature.md` | Who has studied a portfolio of ETFs, by theme |
| `report/03-methods.md` | The three blocks, the growth fund, the screen, the optimizer and rebalancing |
| `report/04-results.md` | What the reading confirmed and changed |
| `report/05-conclusions.md` | Feasibility and concerns |
| `report/06-next-steps.md` | What is still open, and the 61 equity ETFs the screen will read |
| `resources/literature-review.md` | The first literature review, rendered as an annex |
| `resources/literature-review-02.md` | The second literature review, rendered as an annex |

## Assignment

Transcribed from Canvas, Module 4: Term Project Checkpoint A. Due Sunday, October 18, 2026, 11:59pm. 50 points possible. Unlimited attempts. The page does not name the time zone.

### Overview

This is an individual term project that will be shared with the class in the Week 10 discussion board and in the Week 10 sync session.

This first checkpoint asks for a review of the literature on investments and trading. Citations in this checkpoint are associated with references at the end of the write-up for Week 10 Term Project Report and Presentation.

The term project should be associated with a unique, public GitHub repository. This checkpoint assignment should be posted to the term project GitHub repository.

### Background Information

Suppose you are going to start an investment fund. The fund will be either a hedge fund or an exchange-traded fund (ETF). The first ETF was launched in 1993. Rules for ETFs are provided by the [U.S. Securities and Exchange Commission (SEC)](https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-2). In particular, you could be offering an actively managed ETF:

*Actively managed ETFs are not based on an index. Instead, they seek to achieve a stated investment objective by investing in a portfolio of stocks, bonds, and other assets. Unlike with an index-based ETF, an adviser of an actively managed ETF may actively buy or sell components in the portfolio on a daily basis without regard to conformity with an index.*

You have complete flexibility about the types of securities to be included in the fund: stocks, bonds, indexes, or commodities. The most widely known ETFs have been designed for commodities and indexes. But ETFs can be created for any security type. Think of an ETF as a mutual fund with the flexibility to be traded 24/7, the ability to be highly leveraged, and no requirement to be fully (or nearly fully) invested in assets other than cash. If you want to know what it means to start an ETF company, check out Gray (2020b) and [ETF Architect](https://etfarchitect.com/). If you are interested in starting a commodities EFT, check out Harris (2023).

You are building an ETF financial services firm by drawing on your data science expertise. As a model for financial services firms with a strong quantitative focus, and you are a hedge fund "quant," much in the tradition of the now defunct Medallion Fund (Cornell 2019). There are current examples of quantitative hedge fund providers such as [QTS Capital Management](http://www.qtscm.com), [LAB Quantitative Strategies](https://www.lab-qs.com/), and [Aspect Capital](https://www.aspectcapital.com/). Rather than offering hedge fund research and management services to a small group of wealthy investors, you will be offering research and management services to all investors (large and small) who buy shares in your ETF.

Learning about ETFs as an investment class is a benefit of working on this assignment. If you are interested in adding ETFs to your personal investment portfolio, check out Garner (2009) and Wild (2022).

As data scientists, you are in a good position to serve in quantitative (quant) roles in financial services. A web search of "quant firms" will provide links to many, including [AQR Capital](https://www.aqr.com/), [DE Shaw](https://www.deshaw.com/), [Citadel](https://www.citadel.com/), [Two Sigma](https://www.twosigma.com/), and [Jane Street Capital](https://www.janestreet.com/), among others. Of special note is [Renaissance Technologies](https://www.rentec.com/Home.action?index=true) due to its exceptional performance for more than 30 years (Simons 2015; Zuckerberg 2019).

### Prospectus

You are asked to be fund managers, which means that you need to develop a fund prospectus that outlines the investment philosophy of the fund and the financial securities that comprise the fund. What approaches will you use to select securities? Will you be using fundamental or technical analysis methods? How will you make decisions about buying and selling securities (market timing)?

Ensure that your investment philosophy can be defined by explicit rules that you employ for selecting markets, sectors or investment types within markets, and securities within investment types. Ensure that your philosophy translates into explicit rules for buying and selling securities.

Are you employing a **buy-and-hold strategy** (Siegel 2022; Morris 2025)? How would you describe your frequency of trading (how much of your portfolio turns over each year)? Is your investment approach based on **fundamental analysis** (Graham 2006) or **technical analysis** (Meyers 2011; Edwards, Magee, and Bassetti 2019; Rockefeller 2020; Trivedi and Kyal 2021)? To what extent is your portfolio diversified across stocks versus bonds, industry sectors within stocks, or investment types (stocks, bonds, indexes, and commodities)? Is your strategy guided by systematic portfolio selection and optimization (Markowitz 1952, 1956; Sharpe 1963, 1994; Hudson and Thames 2020; Grinold and Kahn 2023)? Are you using a risk-management approach such as **trend following**, going both long and short within asset types (Greyserman and Kaminski 2014; Carver 2015; Covel 2009, 2011, 2017; Radge 2019; Penfold 2020; Clenow 2023; Zakamulin and Giner 2024; Zarattini, Pagani, and Wilcox 2025)? Across a twenty-five-year period, what proportion of your capital can be expected to be invested in assets versus held in cash? Do you have a well-defined hedging strategy to protect the portfolio during market downturns and crashes (Krishnan 2017)?

When it comes to investing, there are many investing strategies and trading rules from which to choose (Parker 2017; Cornell, Cornell, and Cornell 2018; Kaufman 2019). To simplify the definition of your investment philosophy, it is fine to follow a published philosophy of an existing mutual or exchange-traded fund as long as it is an actively traded fund. Your general investment philosophy could be stated in a couple paragraphs. It should be something that attracts new investors to your exchange-traded fund. Think of the text to be placed on the home page of your fund or investment service.

Warren Buffett: *The stock market is a device for transferring money from the impatient to the patient.*

Whatever philosophy you adopt, it should be something that you can implement in a program or robot trader. You need to define the rules that you use for trading in each market in which you participate, and you need to implement those trading rules in software. Automated trading is the way things have been done for more than a decade (Patterson 2011, 2013; Steiner 2012; Lewis 2015, Simons 2015; Wilmott and Orrell 2017; Zuckerman 2019; FD Finance 2024).

Learning about investment philosophies is a benefit of working on this assignment. You will be a more informed personal investor in the future, building wealth in your personal portfolio.

Learning about specific industries, companies, or investment opportunities is a benefit of working on this assignment. You are free to select the type of securities, as well as specific securities that interest you. So, if you want to learn more about commodities, including cryptocurrencies, then your list of securities might be Bitcoin, Ethereum, GLD (a gold ETF), COPX (a copper ETF), among others.

You are free to select data science methods of interest to you, including traditional time series, hidden Markov models, deep-learning, or AI-based models. You will find examples of each of these in the literature on quantitative finance and trading. So, you can make this assignment a way of learning about data science as well as decision analytics and finance.

### Checkpoint Deliverable: Research Report (50 points)

**The deliverable for this checkpoint is a research report posted to the GitHub repository for the term project.** Answer the questions in bold type below:

* Introduction (10 points). **Why** are you conducting this research? Identify potential users of the knowledge base and application(s) that you intend to develop.
* Literature review (10 points). **Who** else has conducted research like this?
* Methods (10 points). **How** are you conducting the research? Make sure you address the issues that are the focus of this checkpoint assignment.
* Results (10 points). **What** did you learn from your research so far?
* Conclusions (10 points). **So, what** does it all mean? Do you have any concerns about the term project at this point?

| Research Report Section | At this checkpoint, your report should... |
| --- | --- |
| **Introduction** | Clearly describe the investment problem or opportunity you are addressing and introduce the concept of the ETF or hedge fund you intend to develop. Explain your investment philosophy at a high level (e.g., fundamental vs. technical, long-term vs. active trading) and why this approach is worth studying. Identify the target users or investors and explain why your proposed strategy or fund would be valuable to them. This section establishes the purpose and direction of your project. |
| **Literature Review** | Provide a focused review of investment strategies, trading philosophies, and quantitative finance approaches relevant to your proposed fund. This includes topics such as fundamental vs. technical analysis, portfolio optimization (Markowitz), risk management, trading rules, and algorithmic trading approaches. Rather than summarizing individual papers, organize the literature into key themes and explain how different approaches compare. This section should justify your chosen investment philosophy and demonstrate awareness of both academic and practitioner perspectives. |
| **Methods** | Describe your proposed approach to constructing and managing the fund, even if it is still conceptual at this stage. This includes: Investment philosophy and rules — how you will select assets, define markets/sectors, and determine buy/sell decisions. Strategy type — whether you are using fundamental analysis, technical analysis, or a hybrid approach. Portfolio structure — types of securities included (stocks, bonds, ETFs, commodities, etc.) and initial ideas about diversification. Trading approach — whether your strategy is buy-and-hold, active trading, long/short, or hedged. Automation potential — how your strategy could be translated into explicit, rule-based logic suitable for algorithmic implementation. This section is about defining what you plan to do, not yet implementing or testing it. |
| **Results** | At this stage, results are conceptual and exploratory, not empirical. You should present: Key insights from the literature that influenced your strategy design. Initial observations about your chosen markets or asset classes (if explored). Refinements to your investment philosophy based on your research. The goal is to show that your thinking has evolved and that your proposed strategy is becoming more clearly defined and grounded in research. |
| **Conclusions** | Reflect on what you have learned about investment strategies and fund design and assess the feasibility of your proposed approach. Discuss any uncertainties, limitations, or open questions that need to be addressed in future checkpoints (e.g., data availability, modeling complexity, evaluation methods). Clearly explain how you will move from conceptual design (Checkpoint A) to data and modeling (Checkpoint B). |

Keep the end-goal in mind. By week 10 you should have defined an investment fund that is uniquely yours, that draws on research that you have conducted, and that can be implemented in an automated, algorithmic manner. For more detail on the structure of your report, see [Structure of Formal Research Reports](https://canvas.northwestern.edu/courses/260285/pages/structure-of-formal-research-reports).

### References

See [Bibliography for the Course](https://canvas.northwestern.edu/courses/260285/pages/bibliography-for-financial-engineering).
