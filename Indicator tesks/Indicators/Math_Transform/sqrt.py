import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "SQRT",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def sqrt(df, col, coin_symbol, interval, is_price):
    if is_price:
        sqrt_col_name = coin_symbol + "_" + interval + "_sqrt"
    else:
        sqrt_col_name = col + "_sqrt"
    sqrt = ta.SQRT(df[col])
    df[sqrt_col_name] = sqrt
    df=df.dropna()
    return df

