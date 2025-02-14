import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Operators",
    "indicator_name": "MAX",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def max(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        max_col_name = coin_symbol + "_" + interval + "_max_" + str(timeperiod)
    else:
        max_col_name = col + "_max_" + str(timeperiod)
    max = ta.MAX(df[col], timeperiod=timeperiod)
    df[max_col_name] = max
    df=df.dropna()
    return df

