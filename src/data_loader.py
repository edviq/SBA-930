import pandas as pd


def load_sample_data():
    data = {
        "year": [2019, 2020, 2021, 2022, 2023],
        "gdp_growth": [2.3, -3.4, 5.9, 1.9, 2.5],
        "inflation": [1.8, 1.2, 4.7, 8.0, 4.1],
        "commodity_index": [100, 92, 118, 135, 127],
        "market_index": [2700, 2300, 3100, 2900, 3400],
    }

    return pd.DataFrame(data)