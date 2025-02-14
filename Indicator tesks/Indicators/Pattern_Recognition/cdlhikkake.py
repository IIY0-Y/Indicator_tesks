import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLHIKKAKE",
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

def cdlhikkake(df, coin_symbol, interval):
    cdlhikkake = ta.CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
    cdlhikkake_col_name = coin_symbol + "_" + interval + "_cdlhikkake"
    df[cdlhikkake_col_name] = cdlhikkake
    return df

