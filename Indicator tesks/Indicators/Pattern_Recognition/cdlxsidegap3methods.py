import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLXSIDEGAP3METHODS",
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

def cdlxsidegap3methods(df, coin_symbol, interval):
    cdlxsidegap3methods = ta.CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])
    cdlxsidegap3methods_col_name = coin_symbol + "_" + interval + "_cdlxsidegap3methods"
    df[cdlxsidegap3methods_col_name] = cdlxsidegap3methods
    return df

