## Optimization and Enhancement

A controlled prompt-optimization test was performed on the ChatGPT financial-risk analysis. The optimized prompt required structured sections, direct evidence with dataset values, separation of assumptions from evidence, explicit missing-data safeguards, confidence ratings, hypothesis labels, and a human-review checklist.

The optimized response was more transparent about limitations than the baseline response. It avoided unsupported causal claims and clearly identified the missing credit- and liquidity-risk measures needed for stronger conclusions. Structured prompting improved consistency, traceability, and reliability, but it cannot replace missing data or human review.

Artifacts:
- `results/chatgpt_risk_analysis.txt` — baseline ChatGPT risk analysis
- `results/chatgpt_optimized_risk_analysis.txt` — optimized ChatGPT risk analysis
- `results/optimization_impact.md` — optimization methods, observed impact, limitations, and recommendations