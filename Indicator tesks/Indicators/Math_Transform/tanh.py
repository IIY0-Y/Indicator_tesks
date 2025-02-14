import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "TANH",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def tanh(df, col, coin_symbol, interval, is_price):
    if is_price:
        tanh_col_name = coin_symbol + "_" + interval + "_tanh"
    else:
        tanh_col_name = col + "_tanh"
    tanh = ta.TANH(df[col])
    df[tanh_col_name] = tanh
    df=df.dropna()
    return df

