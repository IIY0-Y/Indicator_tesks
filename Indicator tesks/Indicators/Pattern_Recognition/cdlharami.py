import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLHARAMI",
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

def cdlharami(df, coin_symbol, interval):
    cdlharami = ta.CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
    cdlharami_col_name = coin_symbol + "_" + interval + "_cdlharami"
    df[cdlharami_col_name] = cdlharami
    return df

