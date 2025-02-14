import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Operators",
    "indicator_name": "MIN",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def min(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        min_col_name = coin_symbol + "_" + interval + "_min_" + str(timeperiod)
    else:
        min_col_name = col + "_min_" + str(timeperiod)
    min = ta.MIN(df[col], timeperiod=timeperiod)
    df[min_col_name] = min
    df=df.dropna()
    return df

