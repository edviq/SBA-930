# Economic Trend Forecast Backtest: ChatGPT vs. Gemini

## Method

This backtest asked ChatGPT and Gemini to forecast 2023 GDP growth and inflation using only the 2019–2022 observations. The actual 2023 values were withheld from both models during forecasting.

Actual 2023 values used for evaluation:

- GDP growth: 2.5%
- Inflation: 4.1%

Absolute error was calculated as:

Absolute error = |forecast - actual|

## Results

| Metric | Actual 2023 | ChatGPT Forecast | ChatGPT Absolute Error | Gemini Forecast | Gemini Absolute Error |
|---|---:|---:|---:|---:|---:|
| GDP growth | 2.5% | 2.5% | 0.0 percentage points | 1.2% | 1.3 percentage points |
| Inflation | 4.1% | 5.5% | 1.4 percentage points | 5.5% | 1.4 percentage points |

## Range Coverage

| Metric | Actual 2023 | ChatGPT Range | Actual in ChatGPT Range? | Gemini Range | Actual in Gemini Range? |
|---|---:|---:|---|---:|---|
| GDP growth | 2.5% | 1.0%–3.5% | Yes | 0.5%–2.2% | No |
| Inflation | 4.1% | 3.5%–7.0% | Yes | 4.0%–7.0% | Yes |

## Interpretation

ChatGPT performed better in this limited backtest. Its GDP point forecast exactly matched the held-out 2023 value of 2.5%, while Gemini underestimated GDP growth by 1.3 percentage points.

Both models forecast inflation at 5.5%, which overestimated the actual 2023 inflation value of 4.1% by 1.4 percentage points. Both models correctly anticipated inflation would decline from 8.0% in 2022, but neither predicted the full size of the decline.

ChatGPT’s forecast ranges included both actual outcomes. Gemini’s inflation range included the actual value, but its GDP range did not include the actual 2.5% outcome.

## Limitations

This is a very small backtest with only one forecast year and four historical observations. It cannot establish that either model is consistently more accurate. The input excluded important variables such as interest rates, fiscal policy, employment, energy prices, consumer spending, and external shocks.

The results should be treated as an academic illustration of forecast evaluation, not as evidence that either LLM can make dependable economic or investment forecasts without verified data, statistical validation, and human review.