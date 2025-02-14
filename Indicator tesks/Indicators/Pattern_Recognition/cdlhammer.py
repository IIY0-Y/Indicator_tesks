import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLHAMMER",
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

def cdlhammer(df, coin_symbol, interval):
    cdlhammer = ta.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
    cdlhammer_col_name = coin_symbol + "_" + interval + "_cdlhammer"
    df[cdlhammer_col_name] = cdlhammer
    return df

