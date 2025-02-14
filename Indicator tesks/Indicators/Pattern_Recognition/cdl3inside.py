import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDL3INSIDE",
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

def cdl3inside(df, coin_symbol, interval):
    cdl3inside = ta.CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
    cdl3inside_col_name = coin_symbol + "_" + interval + "_cdl3inside"
    df[cdl3inside_col_name] = cdl3inside
    return df

