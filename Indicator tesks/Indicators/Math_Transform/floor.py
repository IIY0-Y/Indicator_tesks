import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "FLOOR",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def floor(df, col, coin_symbol, interval, is_price):
    if is_price:
        floor_col_name = coin_symbol + "_" + interval + "_floor"
    else:
        floor_col_name = col + "_floor"
    floor = ta.FLOOR(df[col])
    df[floor_col_name] = floor
    df=df.dropna()
    return df

