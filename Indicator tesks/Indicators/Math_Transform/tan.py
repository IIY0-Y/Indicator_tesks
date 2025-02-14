import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "TAN",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def tan(df, col, coin_symbol, interval, is_price):
    if is_price:
        tan_col_name = coin_symbol + "_" + interval + "_tan"
    else:
        tan_col_name = col + "_tan"
    tan = ta.TAN(df[col])
    df[tan_col_name] = tan
    df=df.dropna()
    return df

