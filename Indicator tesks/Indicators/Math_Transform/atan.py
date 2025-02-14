import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "ATAN",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def atan(df, col, coin_symbol, interval, is_price):
    if is_price:
        atan_col_name = coin_symbol + "_" + interval + "_atan"
    else:
        atan_col_name = col + "_atan"
    atan = ta.ATAN(df[col])
    df[atan_col_name] = atan
    df=df.dropna()
    return df

