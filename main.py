from src.data_loader import load_sample_data
from src.forecasting import summarize_trends
from src.risk_analysis import identify_basic_risks


def main():
    df = load_sample_data()

    print("=== DATA PREVIEW ===")
    print(df.to_string(index=False))
    print()

    print("=== TREND SUMMARY ===")
    for metric, value in summarize_trends(df).items():
        print(f"{metric}: {value}")
    print()

    print("=== RISK ANALYSIS ===")
    for risk in identify_basic_risks(df):
        print(f"- {risk}")


if __name__ == "__main__":
    main()