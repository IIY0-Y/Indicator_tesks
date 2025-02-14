import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Operators",
    "indicator_name": "SUM",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def sum(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        sum_col_name = coin_symbol + "_" + interval + "_sum_" + str(timeperiod)
    else:
        sum_col_name = col + "_sum_" + str(timeperiod)
    sum = ta.SUM(df[col], timeperiod=timeperiod)
    df[sum_col_name] = sum
    df=df.dropna()
    return df

