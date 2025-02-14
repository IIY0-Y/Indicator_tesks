import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLIDENTICAL3CROWS",
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

def cdlidentical3crows(df, coin_symbol, interval):
    cdlidentical3crows = ta.CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
    cdlidentical3crows_col_name = coin_symbol + "_" + interval + "_cdlidentical3crows"
    df[cdlidentical3crows_col_name] = cdlidentical3crows
    return df

