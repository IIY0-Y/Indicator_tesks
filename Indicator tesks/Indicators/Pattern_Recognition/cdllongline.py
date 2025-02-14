import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLLONGLINE",
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

def cdllongline(df, coin_symbol, interval):
    cdllongline = ta.CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
    cdllongline_col_name = coin_symbol + "_" + interval + "_cdllongline"
    df[cdllongline_col_name] = cdllongline
    return df

