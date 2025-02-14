import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDL3LINESTRIKE",
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

def cdl3linestrike(df, coin_symbol, interval):
    cdl3linestrike = ta.CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
    cdl3linestrike_col_name = coin_symbol + "_" + interval + "_cdl3linestrike"
    df[cdl3linestrike_col_name] = cdl3linestrike
    return df

