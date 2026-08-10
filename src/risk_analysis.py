def identify_basic_risks(df):
    risks = []

    if df["inflation"].max() > 6:
        risks.append("Inflation risk is elevated based on peak inflation above 6%.")

    if df["market_index"].diff().min() < -300:
        risks.append(
            "Market volatility risk is present due to a sharp decline in the market index."
        )

    if df["commodity_index"].max() - df["commodity_index"].min() > 25:
        risks.append("Commodity price volatility could reduce forecast stability.")

    if not risks:
        risks.append("No major financial risks detected in the sample data.")

    return risks