import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "SINH",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def sinh(df, col, coin_symbol, interval, is_price):
    if is_price:
        sinh_col_name = coin_symbol + "_" + interval + "_sinh"
    else:
        sinh_col_name = col + "_sinh"
    sinh = ta.SINH(df[col])
    df[sinh_col_name] = sinh
    df=df.dropna()
    return df

