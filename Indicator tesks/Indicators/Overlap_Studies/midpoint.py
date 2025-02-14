import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "MIDPOINT",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def midpoint(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        midpoint_col_name = coin_symbol + "_" + interval + "_midpoint_" + str(timeperiod)
    else:
        midpoint_col_name = col + "_midpoint_" + str(timeperiod)
    midpoint = ta.MIDPOINT(df[col], timeperiod=timeperiod)
    df[midpoint_col_name] = midpoint
    df=df.dropna()
    return df

