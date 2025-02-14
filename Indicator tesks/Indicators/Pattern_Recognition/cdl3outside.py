import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDL3OUTSIDE",
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

def cdl3outside(df, coin_symbol, interval):
    cdl3outside = ta.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
    cdl3outside_col_name = coin_symbol + "_" + interval + "_cdl3outside"
    df[cdl3outside_col_name] = cdl3outside
    return df

