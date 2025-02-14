import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "CEIL",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def ceil(df, col, coin_symbol, interval, is_price):
    if is_price:
        ceil_col_name = coin_symbol + "_" + interval + "_ceil"
    else:
        ceil_col_name = col + "_ceil"
    ceil = ta.CEIL(df[col])
    df[ceil_col_name] = ceil
    df=df.dropna()
    return df

