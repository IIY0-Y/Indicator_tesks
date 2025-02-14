import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Transform",
    "indicator_name": "LN",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def ln(df, col, coin_symbol, interval, is_price):
    if is_price:
        ln_col_name = coin_symbol + "_" + interval + "_ln"
    else:
        ln_col_name = col + "_ln"
    ln = ta.LN(df[col])
    df[ln_col_name] = ln
    df=df.dropna()
    return df

