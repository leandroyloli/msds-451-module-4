# Term Project Checkpoint A

| | |
| --- | --- |
| University | Northwestern University |
| Program | Master of Science in Data Science |
| Student | Leandro Loli |
| Course | MSDS 451, Section 001 |
| Class | Financial Engineering |
| Term | Fall 2026 |
| Assignment | Term Project Checkpoint A |
| Date | October 19, 2026 |

The sections follow the order of the checkpoint.

1. [Introduction](01-introduction.md). A managed portfolio with three blocks, and a fund of ETFs for growth.
2. [Literature review](02-literature.md). Who has studied portfolios of ETFs, and whether an optimized mix beat a simple one.
3. [Methods](03-methods.md). The three blocks, the growth fund, the screen, the optimizer and rebalancing.
   - [The managed portfolio](03-methods.md#the-managed-portfolio)
   - [The growth fund](03-methods.md#the-growth-fund)
   - [The screen an ETF must pass](03-methods.md#the-screen-an-etf-must-pass)
   - [The objective of the optimizer](03-methods.md#the-objective-of-the-optimizer)
   - [How financial engineering does the work](03-methods.md#how-financial-engineering-does-the-work)
   - [Rebalancing](03-methods.md#rebalancing)
   - [What this is, in the language of the assignment](03-methods.md#what-this-is-in-the-language-of-the-assignment)
4. [Results](04-results.md). What the reading confirmed, and what it changed in the design.
5. [Conclusions](05-conclusions.md). New in its combination, rational in its parts.
6. [Next steps](06-next-steps.md). The path to Checkpoint B, and the first list of ETFs.
   - [Research universe](06-next-steps.md#research-universe)
   - [United States](06-next-steps.md#united-states-listed-in-the-united-states)
   - [World, Irish UCITS](06-next-steps.md#world-irish-ucits)
   - [Brazil](06-next-steps.md#brazil-listed-on-b3)

## Terms used in this report

| Term | Meaning |
| --- | --- |
| Managed portfolio | The whole proposal: three blocks managed by one set of rules. |
| Block | One of the three parts: safety, inflation, growth. Each block has one job. |
| Growth fund | The growth block. An actively managed fund of ETFs, and the fund this course builds. |
| ETF | An exchange-traded fund that the growth fund may hold. |
| Wrapper | Where and how the same market is listed: in the United States, as an Irish UCITS ETF, or on B3. |
| Screen | The tests an ETF must pass before it can receive a weight. |
| Optimizer | The rule that sets the weights inside the growth fund. |
| Benchmarks | Equal weight on the same ETFs, and one world ETF held alone. |
| New money | Cash coming into the portfolio. It is used first to rebalance. |
