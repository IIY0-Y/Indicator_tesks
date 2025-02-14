import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "COS",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def cos(df, col, coin_symbol, interval, is_price):
    if is_price:
        cos_col_name = coin_symbol + "_" + interval + "_cos"
    else:
        cos_col_name = col + "_cos"
    cos = ta.COS(df[col])
    df[cos_col_name] = cos
    df=df.dropna()
    return df

