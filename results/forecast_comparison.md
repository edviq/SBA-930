# Financial Forecasting Comparison: ChatGPT vs. Gemini

## Purpose

This controlled academic exercise compared ChatGPT and Gemini on two financial forecasting tasks:

1. Forecasting the potential impact of economic-policy conditions on a stock-market index
2. Forecasting a next-year commodity index

Both models received identical prompts and the same five-year illustrative dataset. The evaluation therefore focuses on prompt compliance, use of supplied data, scenario analysis, uncertainty handling, and risk awareness—not validated real-world forecasting accuracy.

## Dataset Limitation

The dataset contains only five annual observations from 2019 through 2023. It was created as an illustrative dataset for initial code testing and is not a complete real-world financial dataset. It also lacks important forecast drivers such as interest rates, GDP, employment, supply and demand conditions, policy details, sector information, and geopolitical events.

Because the next-year actual outcome is not available, this evaluation cannot calculate forecast error or claim which model was more accurate in real-world terms.

## Evaluation Criteria

| Criterion | Definition |
|---|---|
| Data fidelity | Correctly uses the values and patterns supplied in the prompt |
| Relevance | Directly answers the requested forecast question |
| Reliability | States assumptions, uncertainty, and data limitations |
| Risk awareness | Identifies plausible conditions or risks that could change the forecast |
| Responsible use | Includes an academic or non-investment-advice disclaimer |

## Stock-Market Forecasts

| Item | ChatGPT | Gemini |
|---|---|---|
| Base-case range | 3300–3600 | 3550–3800 |
| Base-case direction | Mild upward trend or consolidation | Moderately upward |
| Bull range | 3600–3900 | 3800–4100 |
| Bear range | 2900–3200 | 2700–3100 |
| Main reasoning | 2023 market recovery and a commodity-index pullback after the 2022 peak | Long-run market increase from 2700 to 3400, with 2023 market recovery while commodity costs declined |
| Key limitations stated | Only five data points; no sector, GDP, interest-rate, or employment data | High uncertainty; no interest rates, tax policy, public spending, or regulatory data |

### Stock-Market Assessment

Both models followed the prompt by providing base, bull, and bear scenarios. Both recognized that specific policy details were missing and therefore used conditional reasoning.

ChatGPT gave the more conservative base range of 3300–3600 and explicitly warned that the dataset contained only five observations. Gemini gave a more optimistic base range of 3550–3800 and linked its forecast to the assumption that lower commodity costs favor equities.

A key limitation in both responses is that they infer a relationship between commodity prices and the stock market from too few observations. Correlation in this small illustrative dataset does not establish causation.

## Commodity Forecasts

| Item | ChatGPT | Gemini |
|---|---|---|
| Base-case range | 120–135 | 120–132 |
| Base-case direction | Sideways to slightly downward | Stabilization or mild decline |
| Bull range | 135–145 | 135–145 |
| Bear range | 110–120 | 105–118 |
| Main reasoning | Post-peak consolidation after the index moved from 135 in 2022 to 127 in 2023 | Commodity index cooled from the 2022 peak while the market index rose in 2023 |
| Key limitations stated | Five data points; no supply, demand, policy, or inflation variables | Five data points; changing relationship with the market index; missing macroeconomic conditions |

### Commodity Assessment

The two models produced similar base forecasts: ChatGPT estimated 120–135 and Gemini estimated 120–132. Both interpreted the 2023 decline from 135 to 127 as evidence of possible stabilization or mild further decline.

ChatGPT’s strength was its clear description of a possible post-peak consolidation phase. Gemini’s strength was its explicit observation that the relationship between the market and commodity indexes changed over time, making the inferred pattern unstable.

Neither forecast can be considered a reliable real-world commodity forecast. The illustrative dataset does not identify the commodity, include monthly or daily observations, or include supply, demand, inventories, currency effects, interest rates, or geopolitical conditions.

## Comparative Scores

Scores use a 1–5 scale, where 5 is strongest for this limited academic exercise.

| Criterion | ChatGPT | Gemini | Evidence |
|---|---:|---:|---|
| Data fidelity | 4 | 4 | Both used the supplied values and described the main time-series changes correctly |
| Relevance | 5 | 5 | Both addressed the requested scenarios, ranges, risks, and limitations |
| Reliability | 4 | 4 | Both stated important limitations; neither could validate a forecast with an actual next-year result |
| Risk awareness | 4 | 4 | Both discussed policy, inflation, commodity, and macroeconomic risks |
| Responsible use | 5 | 5 | Both included a non-investment-advice or academic disclaimer |

## Strengths and Weaknesses

| Model | Strengths | Weaknesses |
|---|---|---|
| ChatGPT | Clear structure; practical scenarios; specific numerical ranges; directly acknowledges the limited five-point dataset | Its “cyclical” and commodity-to-equity interpretations are not statistically validated by five data points |
| Gemini | Clear explanation of assumptions; detailed policy and macroeconomic uncertainty; notices changing relationships between the two indexes | Gives relatively optimistic stock-index ranges and infers equity/commodity relationships that the small dataset cannot establish |

## Conclusion

ChatGPT and Gemini were both useful for organizing a preliminary financial-analysis response from a small dataset. Their strongest value was in generating conditional scenarios, identifying risks, and explaining limitations.

Neither model should be used independently for financial decisions. A stronger evaluation would use verified real-world datasets, a larger historical period, an out-of-sample test period, conventional forecast metrics such as MAE or MAPE, and human financial review.