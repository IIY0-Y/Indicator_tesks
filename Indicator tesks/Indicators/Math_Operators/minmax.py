import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Math Operators",
    "indicator_name": "MINMAX",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": {
        "0": "min",
        "1": "max"
    },
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "1n"
}

def minmax(df, col, coin_symbol, interval, is_price, timeperiod=30):
    minmax = ta.MINMAX(df[col], timeperiod=timeperiod)
    if is_price:
        min_col_name = coin_symbol + "_" + interval + "_min_" + str(timeperiod)
        max_col_name = coin_symbol + "_" + interval + "_max_" + str(timeperiod)
    else:
        min_col_name = col + "_min_" + str(timeperiod)
        max_col_name = col + "_max_" + str(timeperiod)
    cols = [min_col_name, max_col_name]
    for i, c in enumerate(cols):
        df[c] = minmax[i]
    df=df.dropna()
    return df

