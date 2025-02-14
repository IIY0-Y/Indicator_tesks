import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDL3WHITESOLDIERS",
    "indicator_payload": "",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "integer",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def cdl3whitesoldiers(df, coin_symbol, interval):
    cdl3whitesoldiers = ta.CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
    cdl3whitesoldiers_col_name = coin_symbol + "_" + interval + "_cdl3whitesoldiers"
    df[cdl3whitesoldiers_col_name] = cdl3whitesoldiers
    return df

