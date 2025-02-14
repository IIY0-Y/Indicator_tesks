import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLHIGHWAVE",
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

def cdlhighwave(df, coin_symbol, interval):
    cdlhighwave = ta.CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
    cdlhighwave_col_name = coin_symbol + "_" + interval + "_cdlhighwave"
    df[cdlhighwave_col_name] = cdlhighwave
    return df

