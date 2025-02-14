import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "ACOS",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def acos(df, col, coin_symbol, interval, is_price):
    if is_price:
        acos_col_name = coin_symbol + "_" + interval + "_acos"
    else:
        acos_col_name = col + "_acos"
    acos = ta.ACOS(df[col])
    df[acos_col_name] = acos
    df=df.dropna()
    return df

