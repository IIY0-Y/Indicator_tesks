import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLTRISTAR",
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

def cdltristar(df, coin_symbol, interval):
    cdltristar = ta.CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
    cdltristar_col_name = coin_symbol + "_" + interval + "_cdltristar"
    df[cdltristar_col_name] = cdltristar
    return df

