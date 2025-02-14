import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLRISEFALL3METHODS",
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

def cdlrisefall3methods(df, coin_symbol, interval):
    cdlrisefall3methods = ta.CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
    cdlrisefall3methods_col_name = coin_symbol + "_" + interval + "_cdlrisefall3methods"
    df[cdlrisefall3methods_col_name] = cdlrisefall3methods
    return df

