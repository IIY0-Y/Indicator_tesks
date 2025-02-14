import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLSHORTLINE",
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

def cdlshortline(df, coin_symbol, interval):
    cdlshortline = ta.CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
    cdlshortline_col_name = coin_symbol + "_" + interval + "_cdlshortline"
    df[cdlshortline_col_name] = cdlshortline
    return df

