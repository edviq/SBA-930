import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from data_loader import load_sample_data
from forecasting import summarize_trends


def test_summarize_trends_keys():
    df = load_sample_data()
    result = summarize_trends(df)

    assert "avg_gdp_growth" in result
    assert "avg_inflation" in result
    assert "commodity_change" in result
    assert "market_change" in result