import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "COSH",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def cosh(df, col, coin_symbol, interval, is_price):
    if is_price:
        cosh_col_name = coin_symbol + "_" + interval + "_cosh"
    else:
        cosh_col_name = col + "_cosh"
    cosh = ta.COSH(df[col])
    df[cosh_col_name] = cosh
    df=df.dropna()
    return df

