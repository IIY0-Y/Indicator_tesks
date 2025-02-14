import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLGRAVESTONEDOJI",
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

def cdlgravestonedoji(df, coin_symbol, interval):
    cdlgravestonedoji = ta.CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
    cdlgravestonedoji_col_name = coin_symbol + "_" + interval + "_cdlgravestonedoji"
    df[cdlgravestonedoji_col_name] = cdlgravestonedoji
    return df

