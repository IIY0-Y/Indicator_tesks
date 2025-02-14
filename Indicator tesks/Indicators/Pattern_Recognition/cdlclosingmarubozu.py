import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLCLOSINGMARUBOZU",
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

def cdlclosingmarubozu(df, coin_symbol, interval):
    cdlclosingmarubozu = ta.CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
    cdlclosingmarubozu_col_name = coin_symbol + "_" + interval + "_cdlclosingmarubozu"
    df[cdlclosingmarubozu_col_name] = cdlclosingmarubozu
    return df

