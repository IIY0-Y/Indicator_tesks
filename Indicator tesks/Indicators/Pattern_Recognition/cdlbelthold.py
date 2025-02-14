import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLBELTHOLD",
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

def cdlbelthold(df, coin_symbol, interval):
    cdlbelthold = ta.CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
    cdlbelthold_col_name = coin_symbol + "_" + interval + "_cdlbelthold"
    df[cdlbelthold_col_name] = cdlbelthold
    return df

