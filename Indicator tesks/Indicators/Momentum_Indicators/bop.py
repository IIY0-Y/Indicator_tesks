import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "BOP",
    "indicator_payload": "",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "1"
}

def bop(df, coin_symbol, interval):
    bop = ta.BOP(df['open'], df['high'], df['low'], df['close'])
    bop_col_name = coin_symbol + "_" + interval + "_bop"
    df[bop_col_name] = bop
    return df

