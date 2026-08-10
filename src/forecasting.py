def summarize_trends(df):
    return {
        "avg_gdp_growth": round(df["gdp_growth"].mean(), 2),
        "avg_inflation": round(df["inflation"].mean(), 2),
        "commodity_change": int(
            df["commodity_index"].iloc[-1] - df["commodity_index"].iloc[0]
        ),
        "market_change": int(
            df["market_index"].iloc[-1] - df["market_index"].iloc[0]
        ),
    }