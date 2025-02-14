import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "EXP",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def exp(df, col, coin_symbol, interval, is_price):
    if is_price:
        exp_col_name = coin_symbol + "_" + interval + "_exp"
    else:
        exp_col_name = col + "_exp"
    exp = ta.EXP(df[col])
    df[exp_col_name] = exp
    df=df.dropna()
    return df

