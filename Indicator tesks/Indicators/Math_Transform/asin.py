import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "ASIN",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def asin(df, col, coin_symbol, interval, is_price):
    if is_price:
        asin_col_name = coin_symbol + "_" + interval + "_asin"
    else:
        asin_col_name = col + "_asin"
    asin = ta.ASIN(df[col])
    df[asin_col_name] = asin
    df=df.dropna()
    return df

