import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLSPINNINGTOP",
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

def cdlspinningtop(df, coin_symbol, interval):
    cdlspinningtop = ta.CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
    cdlspinningtop_col_name = coin_symbol + "_" + interval + "_cdlspinningtop"
    df[cdlspinningtop_col_name] = cdlspinningtop
    return df

