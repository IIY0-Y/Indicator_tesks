import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "SIN",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def sin(df, col, coin_symbol, interval, is_price):
    if is_price:
        sin_col_name = coin_symbol + "_" + interval + "_sin"
    else:
        sin_col_name = col + "_sin"
    sin = ta.SIN(df[col])
    df[sin_col_name] = sin
    df=df.dropna()
    return df

