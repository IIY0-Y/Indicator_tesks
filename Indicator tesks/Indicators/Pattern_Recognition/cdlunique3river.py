import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLUNIQUE3RIVER",
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

def cdlunique3river(df, coin_symbol, interval):
    cdlunique3river = ta.CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
    cdlunique3river_col_name = coin_symbol + "_" + interval + "_cdlunique3river"
    df[cdlunique3river_col_name] = cdlunique3river
    return df

